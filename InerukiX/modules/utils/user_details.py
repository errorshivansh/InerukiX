#ThisfileispartofIneruki(TelegramBot)

#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseas
#publishedbytheFreeSoftwareFoundation,eitherversion3ofthe
#License,or(atyouroption)anylaterversion.

#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.

#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<http://www.gnu.org/licenses/>.

importpickle
importre
fromcontextlibimportsuppress
fromtypingimportUnion

fromaiogram.dispatcher.handlerimportSkipHandler
fromaiogram.typesimportCallbackQuery,Message
fromaiogram.utils.exceptionsimportBadRequest,ChatNotFound,Unauthorized
fromtelethon.tl.functions.usersimportGetFullUserRequest

fromInerukiimportOPERATORS,bot
fromIneruki.services.mongoimportdb
fromIneruki.services.redisimportbredis
fromIneruki.services.telethonimporttbot

from.languageimportget_string
from.messageimportget_arg


asyncdefadd_user_to_db(user):
ifhasattr(user,"user"):
user=user.user

new_user={
"user_id":user.id,
"first_name":user.first_name,
"last_name":user.last_name,
"username":user.username,
}

user=awaitdb.user_list.find_one({"user_id":new_user["user_id"]})
ifnotuseroruserisNone:
user=new_user

if"chats"notinuser:
new_user["chats"]=[]
if"user_lang"notinuser:
new_user["user_lang"]="en"
ifhasattr(user,"user_lang"):
new_user["user_lang"]=user.user_lang

awaitdb.user_list.update_one(
{"user_id":user["user_id"]},{"$set":new_user},upsert=True
)

returnnew_user


asyncdefget_user_by_id(user_id:int):
ifnotuser_id<=2147483647:
returnNone

user=awaitdb.user_list.find_one({"user_id":user_id})
ifnotuser:
try:
user=awaitadd_user_to_db(awaittbot(GetFullUserRequest(user_id)))
except(ValueError,TypeError):
user=None

returnuser


asyncdefget_id_by_nick(data):
#Checkifdataisuser_id
user=awaitdb.user_list.find_one({"username":data.replace("@","")})
ifuser:
returnuser["user_id"]

user=awaittbot(GetFullUserRequest(data))
returnuser


asyncdefget_user_by_username(username):
#Searchusernameindatabase
if"@"inusername:
#Remove'@'
username=username[1:]

user=awaitdb.user_list.find_one({"username":username.lower()})

#Ohnu,wedon'thavethisuserinDB
ifnotuser:
try:
user=awaitadd_user_to_db(awaittbot(GetFullUserRequest(username)))
except(ValueError,TypeError):
user=None

returnuser


asyncdefget_user_link(user_id,custom_name=None,md=False):
user=awaitdb.user_list.find_one({"user_id":user_id})

ifuser:
user_name=user["first_name"]
else:
try:
user=awaitadd_user_to_db(awaittbot(GetFullUserRequest(int(user_id))))
except(ValueError,TypeError):
user_name=str(user_id)
else:
user_name=user["first_name"]

ifcustom_name:
user_name=custom_name

ifmd:
return"[{name}](tg://user?id={id})".format(name=user_name,id=user_id)
else:
return'<ahref="tg://user?id={id}">{name}</a>'.format(
name=user_name,id=user_id
)


asyncdefget_admins_rights(chat_id,force_update=False):
key="admin_cache:"+str(chat_id)
if(alist:=bredis.get(key))andnotforce_update:
returnpickle.loads(alist)
else:
alist={}
admins=awaitbot.get_chat_administrators(chat_id)
foradmininadmins:
user_id=admin["user"]["id"]
alist[user_id]={
"status":admin["status"],
"admin":True,
"title":admin["custom_title"],
"anonymous":admin["is_anonymous"],
"can_change_info":admin["can_change_info"],
"can_delete_messages":admin["can_delete_messages"],
"can_invite_users":admin["can_invite_users"],
"can_restrict_members":admin["can_restrict_members"],
"can_pin_messages":admin["can_pin_messages"],
"can_promote_members":admin["can_promote_members"],
}

withsuppress(KeyError):#Optionalpermissions
alist[user_id]["can_post_messages"]=admin["can_post_messages"]

bredis.set(key,pickle.dumps(alist))
bredis.expire(key,900)
returnalist


asyncdefis_user_admin(chat_id,user_id):
#User'spmshouldhaveadminrights
ifchat_id==user_id:
returnTrue

ifuser_idinOPERATORS:
returnTrue

#Workaroundtosupportanonymousadmins
ifuser_id==1087968824:
returnTrue

try:
admins=awaitget_admins_rights(chat_id)
exceptBadRequest:
returnFalse
else:
ifuser_idinadmins:
returnTrue
else:
returnFalse


asyncdefcheck_admin_rights(
event:Union[Message,CallbackQuery],chat_id,user_id,rights
):
#User'spmshouldhaveadminrights
ifchat_id==user_id:
returnTrue

ifuser_idinOPERATORS:
returnTrue

#Workaroundtosupportanonymousadmins
ifuser_id==1087968824:
ifnotisinstance(event,Message):
raiseValueError(
f"Cannotextractsignuatureofanonymousadminfrom{type(event)}"
)

ifnotevent.author_signature:
returnTrue

foradminin(awaitget_admins_rights(chat_id)).values():
if"title"inadminandadmin["title"]==event.author_signature:
forpermissioninrights:
ifnotadmin[permission]:
returnpermission
returnTrue

admin_rights=awaitget_admins_rights(chat_id)
ifuser_idnotinadmin_rights:
returnFalse

ifadmin_rights[user_id]["status"]=="creator":
returnTrue

forpermissioninrights:
ifnotadmin_rights[user_id][permission]:
returnpermission

returnTrue


asyncdefcheck_group_admin(event,user_id,no_msg=False):
ifhasattr(event,"chat_id"):
chat_id=event.chat_id
elifhasattr(event,"chat"):
chat_id=event.chat.id
ifawaitis_user_admin(chat_id,user_id)isTrue:
returnTrue
else:
ifno_msgisFalse:
awaitevent.reply("Youshouldbeaadmintodoit!")
returnFalse


asyncdefis_chat_creator(event:Union[Message,CallbackQuery],chat_id,user_id):
admin_rights=awaitget_admins_rights(chat_id)

ifuser_id==1087968824:
_co,possible_creator=0,None
foradmininadmin_rights.values():
ifadmin["title"]==event.author_signature:
_co+=1
possible_creator=admin

if_co>1:
awaitevent.answer(
awaitget_string(chat_id,"global","unable_identify_creator")
)
raiseSkipHandler

ifpossible_creator["status"]=="creator":
returnTrue
returnFalse

ifuser_idnotinadmin_rights:
returnFalse

ifadmin_rights[user_id]["status"]=="creator":
returnTrue

returnFalse


asyncdefget_user_by_text(message,text:str):
#Getallentities
entities=filter(
lambdaent:ent["type"]=="text_mention"orent["type"]=="mention",
message.entities,
)
forentityinentities:
#Ifusernamematchesentity'stext
iftextinentity.get_text(message.text):
ifentity.type=="mention":
#Thisoneentityiscomeswithmentionbyusername,like@rInerukiBot
returnawaitget_user_by_username(text)
elifentity.type=="text_mention":
#Thisoneislinkmention,mostlyusedforuserswithoutanusername
returnawaitget_user_by_id(entity.user.id)

#Nowlet'strygetuserwithuser_id
#Wetryingthisnotfirstbecauseuserlinkmentionalsocanhavenumbers
iftext.isdigit():
user_id=int(text)
ifuser:=awaitget_user_by_id(user_id):
returnuser

#Notfoundanything😞
returnNone


asyncdefget_user(message,allow_self=False):
args=message.text.split(None,2)
user=None

#Only1way
iflen(args)<2and"reply_to_message"inmessage:
returnawaitget_user_by_id(message.reply_to_message.from_user.id)

#Usedefaultfunctiontogetuser
iflen(args)>1:
user=awaitget_user_by_text(message,args[1])

ifnotuserandbool(message.reply_to_message):
user=awaitget_user_by_id(message.reply_to_message.from_user.id)

ifnotuserandallow_self:
#TODO:Fetchuserfrommessageinsteadofdb?!lessoverhead
returnawaitget_user_by_id(message.from_user.id)

#Noargsandnowaytogetuser
ifnotuserandlen(args)<2:
returnNone

returnuser


asyncdefget_user_and_text(message,**kwargs):
args=message.text.split("",2)
user=awaitget_user(message,**kwargs)

iflen(args)>1:
if(test_user:=awaitget_user_by_text(message,args[1]))==user:
iftest_user:
print(len(args))
iflen(args)>2:
returnuser,args[2]
else:
returnuser,""

iflen(args)>1:
returnuser,message.text.split("",1)[1]
else:
returnuser,""


asyncdefget_users(message):
args=message.text.split(None,2)
text=args[1]
users=[]

fortextintext.split("|"):
ifuser:=awaitget_user_by_text(message,text):
users.append(user)

returnusers


asyncdefget_users_and_text(message):
users=awaitget_users(message)
args=message.text.split(None,2)

iflen(args)>1:
returnusers,args[1]
else:
returnusers,""


defget_user_and_text_dec(**dec_kwargs):
defwrapped(func):
asyncdefwrapped_1(*args,**kwargs):
message=args[0]
ifhasattr(message,"message"):
message=message.message

user,text=awaitget_user_and_text(message,**dec_kwargs)
ifnotuser:
awaitmessage.reply("Ican'tgettheuser!")
return
else:
returnawaitfunc(*args,user,text,**kwargs)

returnwrapped_1

returnwrapped


defget_user_dec(**dec_kwargs):
defwrapped(func):
asyncdefwrapped_1(*args,**kwargs):
message=args[0]
ifhasattr(message,"message"):
message=message.message

user,text=awaitget_user_and_text(message,**dec_kwargs)
ifnotbool(user):
awaitmessage.reply("Ican'tgettheuser!")
return
else:
returnawaitfunc(*args,user,**kwargs)

returnwrapped_1

returnwrapped


defget_chat_dec(allow_self=False,fed=False):
defwrapped(func):
asyncdefwrapped_1(*args,**kwargs):
message=args[0]
ifhasattr(message,"message"):
message=message.message

arg=get_arg(message)
iffedisTrue:
iflen(text:=message.get_args().split())>1:
iftext[0].count("-")==4:
arg=text[1]
else:
arg=text[0]

ifarg.startswith("-")orarg.isdigit():
chat=awaitdb.chat_list.find_one({"chat_id":int(arg)})
ifnotchat:
try:
chat=awaitbot.get_chat(arg)
exceptChatNotFound:
returnawaitmessage.reply(
"Icouldn'tfindthechat/channel!MaybeIamnotthere!"
)
exceptUnauthorized:
returnawaitmessage.reply(
"Icouldn'taccesschat/channel!MaybeIwaskickedfromthere!"
)
elifarg.startswith("@"):
chat=awaitdb.chat_list.find_one(
{"chat_nick":re.compile(arg.strip("@"),re.IGNORECASE)}
)
elifallow_selfisTrue:
chat=awaitdb.chat_list.find_one({"chat_id":message.chat.id})
else:
awaitmessage.reply("PleasegivemevalidchatID/username")
return

ifnotchat:
awaitmessage.reply("Ican'tfindanychatsongiveninformation!")
return

returnawaitfunc(*args,chat,**kwargs)

returnwrapped_1

returnwrapped
