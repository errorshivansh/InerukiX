#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2021errorshivansh
#Copyright(C)2020InukaAsith

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


importasyncio
importcsv
importhtml
importio
importos
importre
importtime
importuuid
fromcontextlibimportsuppress
fromdatetimeimportdatetime,timedelta
fromtypingimportOptional

importbabel
importrapidjson
fromaiogramimporttypes
fromaiogram.dispatcher.filters.stateimportState,StatesGroup
fromaiogram.typesimportInputFile,Message
fromaiogram.types.inline_keyboardimportInlineKeyboardButton,InlineKeyboardMarkup
fromaiogram.utils.callback_dataimportCallbackData
fromaiogram.utils.exceptionsimport(
ChatNotFound,
NeedAdministratorRightsInTheChannel,
Unauthorized,
)
frombabel.datesimportformat_timedelta
frompymongoimportDeleteMany,InsertOne

fromInerukiimportBOT_ID,OPERATORS,OWNER_ID,bot,decorator
fromIneruki.services.mongoimportdb
fromIneruki.services.redisimportredis
fromIneruki.services.telethonimporttbot

from..utils.cachedimportcached
from.utils.connectionsimportchat_connection,get_connected_chat
from.utils.languageimportget_string,get_strings,get_strings_dec
from.utils.messageimportget_cmd,need_args_dec
from.utils.restrictionsimportban_user,unban_user
from.utils.user_detailsimport(
check_admin_rights,
get_chat_dec,
get_user_and_text,
get_user_link,
is_chat_creator,
is_user_admin,
)


classImportFbansFileWait(StatesGroup):
waiting=State()


delfed_cb=CallbackData("delfed_cb","fed_id","creator_id")


#functions


asyncdefget_fed_f(message):
chat=awaitget_connected_chat(message,admin=True)
if"err_msg"notinchat:
ifchat["status"]=="private":
#returnfedwhichuseriscreated
fed=awaitget_fed_by_creator(chat["chat_id"])
else:
fed=awaitdb.feds.find_one({"chats":{"$in":[chat["chat_id"]]}})
ifnotfed:
returnFalse
returnfed


asyncdeffed_post_log(fed,text):
if"log_chat_id"notinfed:
return
chat_id=fed["log_chat_id"]
withsuppress(Unauthorized,NeedAdministratorRightsInTheChannel,ChatNotFound):
awaitbot.send_message(chat_id,text)


#decorators


defget_current_chat_fed(func):
asyncdefwrapped_1(*args,**kwargs):
message=args[0]
real_chat_id=message.chat.id
ifnot(fed:=awaitget_fed_f(message)):
awaitmessage.reply(
awaitget_string(real_chat_id,"feds","chat_not_in_fed")
)
return

returnawaitfunc(*args,fed,**kwargs)

returnwrapped_1


defget_fed_user_text(skip_no_fed=False,self=False):
defwrapped(func):
asyncdefwrapped_1(*args,**kwargs):
fed=None
message=args[0]
real_chat_id=message.chat.id
user,text=awaitget_user_and_text(message)
strings=awaitget_strings(real_chat_id,"feds")

#Checknonexitsuser
data=message.get_args().split("")
if(
notuser
andlen(data)>0
anddata[0].isdigit()
andint(data[0])<=2147483647
):
user={"user_id":int(data[0])}
text="".join(data[1:])iflen(data)>1elseNone
elifnotuser:
ifselfisTrue:
user=awaitdb.user_list.find_one(
{"user_id":message.from_user.id}
)
else:
awaitmessage.reply(strings["cant_get_user"])
#Passing'None'userwillthrowerr
return

#Checkfed_idinargs
iftext:
text_args=text.split("",1)
iflen(text_args)>=1:
iftext_args[0].count("-")==4:
text=text_args[1]iflen(text_args)>1else""
ifnot(fed:=awaitget_fed_by_id(text_args[0])):
awaitmessage.reply(strings["fed_id_invalid"])
return
else:
text="".join(text_args)

ifnotfed:
ifnot(fed:=awaitget_fed_f(message)):
ifnotskip_no_fed:
awaitmessage.reply(strings["chat_not_in_fed"])
return
else:
fed=None

returnawaitfunc(*args,fed,user,text,**kwargs)

returnwrapped_1

returnwrapped


defget_fed_dec(func):
asyncdefwrapped_1(*args,**kwargs):
fed=None
message=args[0]
real_chat_id=message.chat.id

ifmessage.text:
text_args=message.text.split("",2)
ifnotlen(text_args)<2andtext_args[1].count("-")==4:
ifnot(fed:=awaitget_fed_by_id(text_args[1])):
awaitmessage.reply(
awaitget_string(real_chat_id,"feds","fed_id_invalid")
)
return

#CheckwhetherfedisstillNone;Thiswillallowabovefedvariabletobepassed
#TODO(Betterhandling?)
iffedisNone:
ifnot(fed:=awaitget_fed_f(message)):
awaitmessage.reply(
awaitget_string(real_chat_id,"feds","chat_not_in_fed")
)
return

returnawaitfunc(*args,fed,**kwargs)

returnwrapped_1


defis_fed_owner(func):
asyncdefwrapped_1(*args,**kwargs):
message=args[0]
fed=args[1]
user_id=message.from_user.id

#checkonanon
ifuser_idin[1087968824,777000]:
return

ifnotuser_id==fed["creator"]anduser_id!=OWNER_ID:
text=(awaitget_string(message.chat.id,"feds","need_fed_admin")).format(
name=html.escape(fed["fed_name"],False)
)
awaitmessage.reply(text)
return

returnawaitfunc(*args,**kwargs)

returnwrapped_1


defis_fed_admin(func):
asyncdefwrapped_1(*args,**kwargs):
message=args[0]
fed=args[1]
user_id=message.from_user.id

#checkonanon
ifuser_idin[1087968824,777000]:
return

ifnotuser_id==fed["creator"]anduser_id!=OWNER_ID:
if"admins"notinfedoruser_idnotinfed["admins"]:
text=(
awaitget_string(message.chat.id,"feds","need_fed_admin")
).format(name=html.escape(fed["fed_name"],False))
returnawaitmessage.reply(text)

returnawaitfunc(*args,**kwargs)

returnwrapped_1


#cmds


@decorator.register(cmds=["newfed","fnew"])
@need_args_dec()
@get_strings_dec("feds")
asyncdefnew_fed(message,strings):
fed_name=html.escape(message.get_args())
user_id=message.from_user.id
#dontsupportcreationofnewfedasanonadmin
ifuser_id==1087968824:
returnawaitmessage.reply(strings["disallow_anon"])

ifnotfed_name:
awaitmessage.reply(strings["no_args"])

iflen(fed_name)>60:
awaitmessage.reply(strings["fed_name_long"])
return

ifawaitget_fed_by_creator(user_id)andnotuser_id==OWNER_ID:
awaitmessage.reply(strings["can_only_1_fed"])
return

ifawaitdb.feds.find_one({"fed_name":fed_name}):
awaitmessage.reply(strings["name_not_avaible"].format(name=fed_name))
return

data={"fed_name":fed_name,"fed_id":str(uuid.uuid4()),"creator":user_id}
awaitdb.feds.insert_one(data)
awaitget_fed_by_id.reset_cache(data["fed_id"])
awaitget_fed_by_creator.reset_cache(data["creator"])
awaitmessage.reply(
strings["created_fed"].format(
name=fed_name,id=data["fed_id"],creator=awaitget_user_link(user_id)
)
)


@decorator.register(cmds=["joinfed","fjoin"])
@need_args_dec()
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("feds")
asyncdefjoin_fed(message,chat,strings):
fed_id=message.get_args().split("")[0]
user_id=message.from_user.id
chat_id=chat["chat_id"]

ifnotawaitis_chat_creator(message,chat_id,user_id):
awaitmessage.reply(strings["only_creators"])
return

#AssumeFedIDinvalid
ifnot(fed:=awaitget_fed_by_id(fed_id)):
awaitmessage.reply(strings["fed_id_invalid"])
return

#Assumechatalreadyjoinedthis/otherfed
if"chats"infedandchat_idinfed["chats"]:
awaitmessage.reply(strings["joined_fed_already"])
return

awaitdb.feds.update_one(
{"_id":fed["_id"]},{"$addToSet":{"chats":{"$each":[chat_id]}}}
)
awaitget_fed_by_id.reset_cache(fed["fed_id"])
awaitmessage.reply(
strings["join_fed_success"].format(
chat=chat["chat_title"],fed=html.escape(fed["fed_name"],False)
)
)
awaitfed_post_log(
fed,
strings["join_chat_fed_log"].format(
fed_name=fed["fed_name"],
fed_id=fed["fed_id"],
chat_name=chat["chat_title"],
chat_id=chat_id,
),
)


@decorator.register(cmds=["leavefed","fleave"])
@chat_connection(admin=True,only_groups=True)
@get_current_chat_fed
@get_strings_dec("feds")
asyncdefleave_fed_comm(message,chat,fed,strings):
user_id=message.from_user.id
ifnotawaitis_chat_creator(message,chat["chat_id"],user_id):
awaitmessage.reply(strings["only_creators"])
return

awaitdb.feds.update_one({"_id":fed["_id"]},{"$pull":{"chats":chat["chat_id"]}})
awaitget_fed_by_id.reset_cache(fed["fed_id"])
awaitmessage.reply(
strings["leave_fed_success"].format(
chat=chat["chat_title"],fed=html.escape(fed["fed_name"],False)
)
)

awaitfed_post_log(
fed,
strings["leave_chat_fed_log"].format(
fed_name=html.escape(fed["fed_name"],False),
fed_id=fed["fed_id"],
chat_name=chat["chat_title"],
chat_id=chat["chat_id"],
),
)


@decorator.register(cmds="fsub")
@need_args_dec()
@get_current_chat_fed
@is_fed_owner
@get_strings_dec("feds")
asyncdeffed_sub(message,fed,strings):
fed_id=message.get_args().split("")[0]

#AssumeFedIDisvalid
ifnot(fed2:=awaitget_fed_by_id(fed_id)):
awaitmessage.reply(strings["fed_id_invalid"])
return

#Assumechatalreadyjoinedthis/otherfed
if"subscribed"infedandfed_idinfed["subscribed"]:
awaitmessage.reply(
strings["already_subsed"].format(
name=html.escape(fed["fed_name"],False),
name2=html.escape(fed2["fed_name"],False),
)
)
return

awaitdb.feds.update_one(
{"_id":fed["_id"]},{"$addToSet":{"subscribed":{"$each":[fed_id]}}}
)
awaitget_fed_by_id.reset_cache(fed["fed_id"])
awaitmessage.reply(
strings["subsed_success"].format(
name=html.escape(fed["fed_name"],False),
name2=html.escape(fed2["fed_name"],False),
)
)


@decorator.register(cmds="funsub")
@need_args_dec()
@get_current_chat_fed
@is_fed_owner
@get_strings_dec("feds")
asyncdeffed_unsub(message,fed,strings):
fed_id=message.get_args().split("")[0]

ifnot(fed2:=awaitget_fed_by_id(fed_id)):
awaitmessage.reply(strings["fed_id_invalid"])
return

if"subscribed"infedandfed_idnotinfed["subscribed"]:
message.reply(
strings["not_subsed"].format(
name=html.escape(fed["fed_name"],False),name2=fed2["fed_name"]
)
)
return

awaitdb.feds.update_one(
{"_id":fed["_id"]},{"$pull":{"subscribed":str(fed_id)}}
)
awaitget_fed_by_id.reset_cache(fed["fed_id"])
awaitmessage.reply(
strings["unsubsed_success"].format(
name=html.escape(fed["fed_name"],False),
name2=html.escape(fed2["fed_name"],False),
)
)


@decorator.register(cmds="fpromote")
@get_fed_user_text()
@is_fed_owner
@get_strings_dec("feds")
asyncdefpromote_to_fed(message,fed,user,text,strings):
restricted_ids=[1087968824,777000]
ifuser["user_id"]inrestricted_ids:
returnawaitmessage.reply(strings["restricted_user:promote"])
awaitdb.feds.update_one(
{"_id":fed["_id"]},{"$addToSet":{"admins":{"$each":[user["user_id"]]}}}
)
awaitget_fed_by_id.reset_cache(fed["fed_id"])
awaitmessage.reply(
strings["admin_added_to_fed"].format(
user=awaitget_user_link(user["user_id"]),
name=html.escape(fed["fed_name"],False),
)
)

awaitfed_post_log(
fed,
strings["promote_user_fed_log"].format(
fed_name=html.escape(fed["fed_name"],False),
fed_id=fed["fed_id"],
user=awaitget_user_link(user["user_id"]),
user_id=user["user_id"],
),
)


@decorator.register(cmds="fdemote")
@get_fed_user_text()
@is_fed_owner
@get_strings_dec("feds")
asyncdefdemote_from_fed(message,fed,user,text,strings):
awaitdb.feds.update_one(
{"_id":fed["_id"]},{"$pull":{"admins":user["user_id"]}}
)
awaitget_fed_by_id.reset_cache(fed["fed_id"])

awaitmessage.reply(
strings["admin_demoted_from_fed"].format(
user=awaitget_user_link(user["user_id"]),
name=html.escape(fed["fed_name"],False),
)
)

awaitfed_post_log(
fed,
strings["demote_user_fed_log"].format(
fed_name=html.escape(fed["fed_name"],False),
fed_id=fed["fed_id"],
user=awaitget_user_link(user["user_id"]),
user_id=user["user_id"],
),
)


@decorator.register(cmds=["fsetlog","setfedlog"],only_groups=True)
@get_fed_dec
@get_chat_dec(allow_self=True,fed=True)
@is_fed_owner
@get_strings_dec("feds")
asyncdefset_fed_log_chat(message,fed,chat,strings):
chat_id=chat["chat_id"]if"chat_id"inchatelsechat["id"]
ifchat["type"]=="channel":
if(
awaitcheck_admin_rights(message,chat_id,BOT_ID,["can_post_messages"])
isnotTrue
):
returnawaitmessage.reply(strings["no_right_to_post"])

if"log_chat_id"infedandfed["log_chat_id"]:
awaitmessage.reply(
strings["already_have_chatlog"].format(
name=html.escape(fed["fed_name"],False)
)
)
return

awaitdb.feds.update_one({"_id":fed["_id"]},{"$set":{"log_chat_id":chat_id}})
awaitget_fed_by_id.reset_cache(fed["fed_id"])

text=strings["set_chat_log"].format(name=html.escape(fed["fed_name"],False))
awaitmessage.reply(text)

#Currentfedvariableisnotupdated
awaitfed_post_log(
awaitget_fed_by_id(fed["fed_id"]),
strings["set_log_fed_log"].format(
fed_name=html.escape(fed["fed_name"],False),fed_id=fed["fed_id"]
),
)


@decorator.register(cmds=["funsetlog","unsetfedlog"],only_groups=True)
@get_fed_dec
@is_fed_owner
@get_strings_dec("feds")
asyncdefunset_fed_log_chat(message,fed,strings):
if"log_chat_id"notinfedornotfed["log_chat_id"]:
awaitmessage.reply(
strings["already_have_chatlog"].format(
name=html.escape(fed["fed_name"],False)
)
)
return

awaitdb.feds.update_one({"_id":fed["_id"]},{"$unset":{"log_chat_id":1}})
awaitget_fed_by_id.reset_cache(fed["fed_id"])

text=strings["logging_removed"].format(name=html.escape(fed["fed_name"],False))
awaitmessage.reply(text)

awaitfed_post_log(
fed,
strings["unset_log_fed_log"].format(
fed_name=html.escape(fed["fed_name"],False),fed_id=fed["fed_id"]
),
)


@decorator.register(cmds=["fchatlist","fchats"])
@get_fed_dec
@is_fed_admin
@get_strings_dec("feds")
asyncdeffed_chat_list(message,fed,strings):
text=strings["chats_in_fed"].format(name=html.escape(fed["fed_name"],False))
if"chats"notinfed:
returnawaitmessage.reply(
strings["no_chats"].format(name=html.escape(fed["fed_name"],False))
)

forchat_idinfed["chats"]:
chat=awaitdb.chat_list.find_one({"chat_id":chat_id})
text+="*{}(<code>{}</code>)\n".format(chat["chat_title"],chat_id)
iflen(text)>4096:
awaitmessage.answer_document(
InputFile(io.StringIO(text),filename="chatlist.txt"),
strings["too_large"],
reply=message.message_id,
)
return
awaitmessage.reply(text)


@decorator.register(cmds=["fadminlist","fadmins"])
@get_fed_dec
@is_fed_admin
@get_strings_dec("feds")
asyncdeffed_admins_list(message,fed,strings):
text=strings["fadmins_header"].format(
fed_name=html.escape(fed["fed_name"],False)
)
text+="*{}(<code>{}</code>)\n".format(
awaitget_user_link(fed["creator"]),fed["creator"]
)
if"admins"infed:
foruser_idinfed["admins"]:
text+="*{}(<code>{}</code>)\n".format(
awaitget_user_link(user_id),user_id
)
awaitmessage.reply(text,disable_notification=True)


@decorator.register(cmds=["finfo","fedinfo"])
@get_fed_dec
@get_strings_dec("feds")
asyncdeffed_info(message,fed,strings):
text=strings["finfo_text"]
banned_num=awaitdb.fed_bans.count_documents({"fed_id":fed["fed_id"]})
text=text.format(
name=html.escape(fed["fed_name"],False),
fed_id=fed["fed_id"],
creator=awaitget_user_link(fed["creator"]),
chats=len(fed["chats"]if"chats"infedelse[]),
fbanned=banned_num,
)

if"subscribed"infedandlen(fed["subscribed"])>0:
text+=strings["finfo_subs_title"]
forsfedinfed["subscribed"]:
sfed=awaitget_fed_by_id(sfed)
text+=f"*{sfed['fed_name']}(<code>{sfed['fed_id']}</code>)\n"

awaitmessage.reply(text,disable_notification=True)


asyncdefget_all_subs_feds_r(fed_id,new):
new.append(fed_id)

fed=awaitget_fed_by_id(fed_id)
asyncforitemindb.feds.find({"subscribed":{"$in":[fed["fed_id"]]}}):
ifitem["fed_id"]innew:
continue
new=awaitget_all_subs_feds_r(item["fed_id"],new)

returnnew


@decorator.register(cmds=["fban","sfban"])
@get_fed_user_text()
@is_fed_admin
@get_strings_dec("feds")
asyncdeffed_ban_user(message,fed,user,reason,strings):
user_id=user["user_id"]

#Checks
ifuser_idinOPERATORS:
awaitmessage.reply(strings["user_wl"])
return

elifuser_id==message.from_user.id:
awaitmessage.reply(strings["fban_self"])
return

elifuser_id==BOT_ID:
awaitmessage.reply(strings["fban_self"])
return

elifuser_id==fed["creator"]:
awaitmessage.reply(strings["fban_creator"])
return

elif"admins"infedanduser_idinfed["admins"]:
awaitmessage.reply(strings["fban_fed_admin"])
return

elifdata:=awaitdb.fed_bans.find_one(
{"fed_id":fed["fed_id"],"user_id":user_id}
):
if"reason"notindataordata["reason"]!=reason:
operation="$set"ifreasonelse"$unset"
awaitdb.fed_bans.update_one(
{"_id":data["_id"]},{operation:{"reason":reason}}
)
returnawaitmessage.reply(strings["update_fban"].format(reason=reason))
awaitmessage.reply(
strings["already_fbanned"].format(user=awaitget_user_link(user_id))
)
return

text=strings["fbanned_header"]
text+=strings["fban_info"].format(
fed=html.escape(fed["fed_name"],False),
fadmin=awaitget_user_link(message.from_user.id),
user=awaitget_user_link(user_id),
user_id=user["user_id"],
)
ifreason:
text+=strings["fbanned_reason"].format(reason=reason)

#fbanprocessingmsg
num=len(fed["chats"])if"chats"infedelse0
msg=awaitmessage.reply(text+strings["fbanned_process"].format(num=num))

user=awaitdb.user_list.find_one({"user_id":user_id})

banned_chats=[]

if"chats"infed:
forchat_idinfed["chats"]:
#Wenotfoundtheuseroruserwasn'tdetected
ifnotuseror"chats"notinuser:
continue

ifchat_idinuser["chats"]:
awaitasyncio.sleep(0)#Donotslowdownotherupdates
ifawaitban_user(chat_id,user_id):
banned_chats.append(chat_id)

new={
"fed_id":fed["fed_id"],
"user_id":user_id,
"banned_chats":banned_chats,
"time":datetime.now(),
"by":message.from_user.id,
}

ifreason:
new["reason"]=reason

awaitdb.fed_bans.insert_one(new)

channel_text=strings["fban_log_fed_log"].format(
fed_name=html.escape(fed["fed_name"],False),
fed_id=fed["fed_id"],
user=awaitget_user_link(user_id),
user_id=user_id,
by=awaitget_user_link(message.from_user.id),
chat_count=len(banned_chats),
all_chats=num,
)

ifreason:
channel_text+=strings["fban_reason_fed_log"].format(reason=reason)

#Checkifsilent
silent=False
ifget_cmd(message)=="sfban":
silent=True
key="leave_silent:"+str(message.chat.id)
redis.set(key,user_id)
redis.expire(key,30)
text+=strings["fbanned_silence"]

#SubsFedsprocess
iflen(sfeds_list:=awaitget_all_subs_feds_r(fed["fed_id"],[]))>1:
sfeds_list.remove(fed["fed_id"])
this_fed_banned_count=len(banned_chats)

awaitmsg.edit_text(
text+strings["fbanned_subs_process"].format(feds=len(sfeds_list))
)

all_banned_chats_count=0
fors_fed_idinsfeds_list:
if(
awaitdb.fed_bans.find_one({"fed_id":s_fed_id,"user_id":user_id})
isnotNone
):
#userisalreadybannedinsubscribedfederation,skip
continue
s_fed=awaitget_fed_by_id(s_fed_id)
banned_chats=[]
new={
"fed_id":s_fed_id,
"user_id":user_id,
"banned_chats":banned_chats,
"time":datetime.now(),
"origin_fed":fed["fed_id"],
"by":message.from_user.id,
}
forchat_idins_fed["chats"]:
ifnotuser:
continue

elifchat_id==user["user_id"]:
continue

elif"chats"notinuser:
continue

elifchat_idnotinuser["chats"]:
continue

#Donotslowdownotherupdates
awaitasyncio.sleep(0.2)

ifawaitban_user(chat_id,user_id):
banned_chats.append(chat_id)
all_banned_chats_count+=1

ifreason:
new["reason"]=reason

awaitdb.fed_bans.insert_one(new)

awaitmsg.edit_text(
text
+strings["fbanned_subs_done"].format(
chats=this_fed_banned_count,
subs_chats=all_banned_chats_count,
feds=len(sfeds_list),
)
)

channel_text+=strings["fban_subs_fed_log"].format(
subs_chats=all_banned_chats_count,feds=len(sfeds_list)
)

else:
awaitmsg.edit_text(
text+strings["fbanned_done"].format(num=len(banned_chats))
)

awaitfed_post_log(fed,channel_text)

ifsilent:
to_del=[msg.message_id,message.message_id]
if(
"reply_to_message"inmessage
andmessage.reply_to_message.from_user.id==user_id
):
to_del.append(message.reply_to_message.message_id)
awaitasyncio.sleep(5)
awaittbot.delete_messages(message.chat.id,to_del)


@decorator.register(cmds=["unfban","funban"])
@get_fed_user_text()
@is_fed_admin
@get_strings_dec("feds")
asyncdefunfed_ban_user(message,fed,user,text,strings):
user_id=user["user_id"]

ifuser==BOT_ID:
awaitmessage.reply(strings["unfban_self"])
return

elifnot(
banned:=awaitdb.fed_bans.find_one(
{"fed_id":fed["fed_id"],"user_id":user_id}
)
):
awaitmessage.reply(
strings["user_not_fbanned"].format(user=awaitget_user_link(user_id))
)
return

text=strings["un_fbanned_header"]
text+=strings["fban_info"].format(
fed=html.escape(fed["fed_name"],False),
fadmin=awaitget_user_link(message.from_user.id),
user=awaitget_user_link(user["user_id"]),
user_id=user["user_id"],
)

banned_chats=[]
if"banned_chats"inbanned:
banned_chats=banned["banned_chats"]

#unfbanprocessingmsg
msg=awaitmessage.reply(
text+strings["un_fbanned_process"].format(num=len(banned_chats))
)

counter=0
forchat_idinbanned_chats:
awaitasyncio.sleep(0)#Donotslowdownotherupdates
ifawaitunban_user(chat_id,user_id):
counter+=1

awaitdb.fed_bans.delete_one({"fed_id":fed["fed_id"],"user_id":user_id})

channel_text=strings["un_fban_log_fed_log"].format(
fed_name=html.escape(fed["fed_name"],False),
fed_id=fed["fed_id"],
user=awaitget_user_link(user["user_id"]),
user_id=user["user_id"],
by=awaitget_user_link(message.from_user.id),
chat_count=len(banned_chats),
all_chats=len(fed["chats"])if"chats"infedelse0,
)

#Subsfeds
iflen(sfeds_list:=awaitget_all_subs_feds_r(fed["fed_id"],[]))>1:
sfeds_list.remove(fed["fed_id"])
this_fed_unbanned_count=counter

awaitmsg.edit_text(
text+strings["un_fbanned_subs_process"].format(feds=len(sfeds_list))
)

all_unbanned_chats_count=0
forsfed_idinsfeds_list:
#revision19/10/2020:unfbansonlythosewhogotbannedby`this`fed
ban=awaitdb.fed_bans.find_one(
{"fed_id":sfed_id,"origin_fed":fed["fed_id"],"user_id":user_id}
)
ifbanisNone:
#probablyoldfban
ban=awaitdb.fed_bans.find_one(
{"fed_id":sfed_id,"user_id":user_id}
)
#ifban['time']>`replaceherewithdatetimeofreleaseofv2.2`:
#continue
banned_chats=[]
ifbanisnotNoneand"banned_chats"inban:
banned_chats=ban["banned_chats"]

forchat_idinbanned_chats:
awaitasyncio.sleep(0.2)#Donotslowdownotherupdates
ifawaitunban_user(chat_id,user_id):
all_unbanned_chats_count+=1

awaitdb.fed_bans.delete_one(
{"fed_id":sfed_id,"user_id":user_id}
)

awaitmsg.edit_text(
text
+strings["un_fbanned_subs_done"].format(
chats=this_fed_unbanned_count,
subs_chats=all_unbanned_chats_count,
feds=len(sfeds_list),
)
)

channel_text+=strings["fban_subs_fed_log"].format(
subs_chats=all_unbanned_chats_count,feds=len(sfeds_list)
)
else:
awaitmsg.edit_text(text+strings["un_fbanned_done"].format(num=counter))

awaitfed_post_log(fed,channel_text)


@decorator.register(cmds=["delfed","fdel"])
@get_fed_dec
@is_fed_owner
@get_strings_dec("feds")
asyncdefdel_fed_cmd(message,fed,strings):
fed_name=html.escape(fed["fed_name"],False)
fed_id=fed["fed_id"]
fed_owner=fed["creator"]

buttons=InlineKeyboardMarkup()
buttons.add(
InlineKeyboardButton(
text=strings["delfed_btn_yes"],
callback_data=delfed_cb.new(fed_id=fed_id,creator_id=fed_owner),
)
)
buttons.add(
InlineKeyboardButton(
text=strings["delfed_btn_no"],callback_data=f"cancel_{fed_owner}"
)
)

awaitmessage.reply(strings["delfed"]%fed_name,reply_markup=buttons)


@decorator.register(delfed_cb.filter(),f="cb",allow_kwargs=True)
@get_strings_dec("feds")
asyncdefdel_fed_func(event,strings,callback_data=None,**kwargs):
fed_id=callback_data["fed_id"]
fed_owner=callback_data["creator_id"]

ifevent.from_user.id!=int(fed_owner):
return

awaitdb.feds.delete_one({"fed_id":fed_id})
awaitget_fed_by_id.reset_cache(fed_id)
awaitget_fed_by_creator.reset_cache(int(fed_owner))
asyncforsubscribed_fedindb.feds.find({"subscribed":fed_id}):
awaitdb.feds.update_one(
{"_id":subscribed_fed["_id"]},{"$pull":{"subscribed":fed_id}}
)
awaitget_fed_by_id.reset_cache(subscribed_fed["fed_id"])

#deleteallfbansofit
awaitdb.fed_bans.delete_many({"fed_id":fed_id})

awaitevent.message.edit_text(strings["delfed_success"])


@decorator.register(regexp="cancel_(.*)",f="cb")
asyncdefcancel(event):
ifevent.from_user.id!=int((re.search(r"cancel_(.*)",event.data)).group(1)):
return
awaitevent.message.delete()


@decorator.register(cmds="frename")
@need_args_dec()
@get_fed_dec
@is_fed_owner
@get_strings_dec("feds")
asyncdeffed_rename(message,fed,strings):
#CheckwhetherfirstargisfedID|TODO:Removethis
args=message.get_args().split("",2)
iflen(args)>1andargs[0].count("-")==4:
new_name="".join(args[1:])
else:
new_name="".join(args[0:])

ifnew_name==fed["fed_name"]:
awaitmessage.reply(strings["frename_same_name"])
return

awaitdb.feds.update_one({"_id":fed["_id"]},{"$set":{"fed_name":new_name}})
awaitget_fed_by_id.reset_cache(fed["fed_id"])
awaitmessage.reply(
strings["frename_success"].format(
old_name=html.escape(fed["fed_name"],False),
new_name=html.escape(new_name,False),
)
)


@decorator.register(cmds=["fbanlist","exportfbans","fexport"])
@get_fed_dec
@is_fed_admin
@get_strings_dec("feds")
asyncdeffban_export(message,fed,strings):
fed_id=fed["fed_id"]
key="fbanlist_lock:"+str(fed_id)
ifredis.get(key)andmessage.from_user.idnotinOPERATORS:
ttl=format_timedelta(
timedelta(seconds=redis.ttl(key)),strings["language_info"]["babel"]
)
awaitmessage.reply(strings["fbanlist_locked"]%ttl)
return

redis.set(key,1)
redis.expire(key,600)

msg=awaitmessage.reply(strings["creating_fbanlist"])
fields=["user_id","reason","by","time","banned_chats"]
withio.StringIO()asf:
writer=csv.DictWriter(f,fields)
writer.writeheader()
asyncforbanned_dataindb.fed_bans.find({"fed_id":fed_id}):
awaitasyncio.sleep(0)

data={"user_id":banned_data["user_id"]}

if"reason"inbanned_data:
data["reason"]=banned_data["reason"]

if"time"inbanned_data:
data["time"]=int(time.mktime(banned_data["time"].timetuple()))

if"by"inbanned_data:
data["by"]=banned_data["by"]

if"banned_chats"inbanned_data:
data["banned_chats"]=banned_data["banned_chats"]

writer.writerow(data)

text=strings["fbanlist_done"]%html.escape(fed["fed_name"],False)
f.seek(0)
awaitmessage.answer_document(InputFile(f,filename="fban_export.csv"),text)
awaitmsg.delete()


@decorator.register(cmds=["importfbans","fimport"])
@get_fed_dec
@is_fed_admin
@get_strings_dec("feds")
asyncdefimportfbans_cmd(message,fed,strings):
fed_id=fed["fed_id"]
key="importfbans_lock:"+str(fed_id)
ifredis.get(key)andmessage.from_user.idnotinOPERATORS:
ttl=format_timedelta(
timedelta(seconds=redis.ttl(key)),strings["language_info"]["babel"]
)
awaitmessage.reply(strings["importfbans_locked"]%ttl)
return

redis.set(key,1)
redis.expire(key,600)

if"document"inmessage:
document=message.document
else:
if"reply_to_message"notinmessage:
awaitImportFbansFileWait.waiting.set()
awaitmessage.reply(strings["send_import_file"])
return

elif"document"notinmessage.reply_to_message:
awaitmessage.reply(strings["rpl_to_file"])
return
document=message.reply_to_message.document

awaitimportfbans_func(message,fed,document=document)


@get_strings_dec("feds")
asyncdefimportfbans_func(message,fed,strings,document=None):
globaluser_id
file_type=os.path.splitext(document["file_name"])[1][1:]

iffile_type=="json":
ifdocument["file_size"]>1000000:
awaitmessage.reply(strings["big_file_json"].format(num="1"))
return
eliffile_type=="csv":
ifdocument["file_size"]>52428800:
awaitmessage.reply(strings["big_file_csv"].format(num="50"))
return
else:
awaitmessage.reply(strings["wrong_file_ext"])
return

f=awaitbot.download_file_by_id(document.file_id,io.BytesIO())
msg=awaitmessage.reply(strings["importing_process"])

data=None
iffile_type=="json":
try:
data=rapidjson.load(f).items()
exceptValueError:
returnawaitmessage.reply(strings["invalid_file"])
eliffile_type=="csv":
data=csv.DictReader(io.TextIOWrapper(f))

real_counter=0

queue_del=[]
queue_insert=[]
current_time=datetime.now()
forrowindata:
iffile_type=="json":
user_id=row[0]
data=row[1]
eliffile_type=="csv":
if"user_id"inrow:
user_id=int(row["user_id"])
elif"id"inrow:
user_id=int(row["id"])
else:
continue
else:
raiseNotImplementedError

new={"fed_id":fed["fed_id"],"user_id":user_id}

if"reason"inrow:
new["reason"]=row["reason"]

if"by"inrow:
new["by"]=int(row["by"])
else:
new["by"]=message.from_user.id

if"time"inrow:
new["time"]=datetime.fromtimestamp(int(row["time"]))
else:
new["time"]=current_time

if"banned_chats"inrowandtype(row["banned_chats"])islist:
new["banned_chats"]=row["banned_chats"]

queue_del.append(DeleteMany({"fed_id":fed["fed_id"],"user_id":user_id}))
queue_insert.append(InsertOne(new))

iflen(queue_insert)==1000:
real_counter+=len(queue_insert)

#Makedeleteoperationorderedbeforeinserting.
ifqueue_del:
awaitdb.fed_bans.bulk_write(queue_del,ordered=False)
awaitdb.fed_bans.bulk_write(queue_insert,ordered=False)

queue_del=[]
queue_insert=[]

#Processlastbans
real_counter+=len(queue_insert)
ifqueue_del:
awaitdb.fed_bans.bulk_write(queue_del,ordered=False)
ifqueue_insert:
awaitdb.fed_bans.bulk_write(queue_insert,ordered=False)

awaitmsg.edit_text(strings["import_done"].format(num=real_counter))


@decorator.register(
state=ImportFbansFileWait.waiting,
content_types=types.ContentTypes.DOCUMENT,
allow_kwargs=True,
)
@get_fed_dec
@is_fed_admin
asyncdefimport_state(message,fed,state=None,**kwargs):
awaitimportfbans_func(message,fed,document=message.document)
awaitstate.finish()


@decorator.register(only_groups=True)
@chat_connection(only_groups=True)
@get_strings_dec("feds")
asyncdefcheck_fbanned(message:Message,chat,strings):
ifmessage.sender_chat:
#shouldbechannel/anon
return

user_id=message.from_user.id
chat_id=chat["chat_id"]

ifnot(fed:=awaitget_fed_f(message)):
return

elifawaitis_user_admin(chat_id,user_id):
return

feds_list=[fed["fed_id"]]

if"subscribed"infed:
feds_list.extend(fed["subscribed"])

ifban:=awaitdb.fed_bans.find_one(
{"fed_id":{"$in":feds_list},"user_id":user_id}
):

#checkwhetherbannedfed_idischat'sfedidelse
#userisbannedinsubfed
iffed["fed_id"]==ban["fed_id"]and"origin_fed"notinban:
text=strings["automatic_ban"].format(
user=awaitget_user_link(user_id),
fed_name=html.escape(fed["fed_name"],False),
)
else:
s_fed=awaitget_fed_by_id(
ban["fed_id"]if"origin_fed"notinbanelseban["origin_fed"]
)
ifs_fedisNone:
return

text=strings["automatic_ban_sfed"].format(
user=awaitget_user_link(user_id),fed_name=s_fed["fed_name"]
)

if"reason"inban:
text+=strings["automatic_ban_reason"].format(text=ban["reason"])

ifnotawaitban_user(chat_id,user_id):
return

awaitmessage.reply(text)

awaitdb.fed_bans.update_one(
{"_id":ban["_id"]},{"$addToSet":{"banned_chats":chat_id}}
)


@decorator.register(cmds=["fcheck","fbanstat"])
@get_fed_user_text(skip_no_fed=True,self=True)
@get_strings_dec("feds")
asyncdeffedban_check(message,fed,user,_,strings):
fbanned_fed=False#Avariabletofindifuserisbannedincurrentfedofchat
fban_data=None

total_count=awaitdb.fed_bans.count_documents({"user_id":user["user_id"]})
iffed:
fed_list=[fed["fed_id"]]
#checkfbannedinsubscribed
if"subscribed"infed:
fed_list.extend(fed["subscribed"])

iffban_data:=awaitdb.fed_bans.find_one(
{"user_id":user["user_id"],"fed_id":{"$in":fed_list}}
):
fbanned_fed=True

#re-assignfedifuserisbannedinsub-fed
iffban_data["fed_id"]!=fed["fed_id"]or"origin_fed"infban_data:
fed=awaitget_fed_by_id(
fban_data[
"fed_id"if"origin_fed"notinfban_dataelse"origin_fed"
]
)

#createtext
text=strings["fcheck_header"]
ifmessage.chat.type=="private"andmessage.from_user.id==user["user_id"]:
ifbool(fed):
ifbool(fban_data):
if"reason"notinfban_data:
text+=strings["fban_info:fcheck"].format(
fed=html.escape(fed["fed_name"],False),
date=babel.dates.format_date(
fban_data["time"],
"long",
locale=strings["language_info"]["babel"],
),
)
else:
text+=strings["fban_info:fcheck:reason"].format(
fed=html.escape(fed["fed_name"],False),
date=babel.dates.format_date(
fban_data["time"],
"long",
locale=strings["language_info"]["babel"],
),
reason=fban_data["reason"],
)
else:
returnawaitmessage.reply(strings["didnt_fbanned"])
else:
text+=strings["fbanned_count_pm"].format(count=total_count)
iftotal_count>0:
count=0
asyncforfbanindb.fed_bans.find({"user_id":user["user_id"]}):
count+=1
_fed=awaitget_fed_by_id(fban["fed_id"])
if_fed:
fed_name=_fed["fed_name"]
text+=f'{count}:<code>{fban["fed_id"]}</code>:{fed_name}\n'
else:
iftotal_count>0:
text+=strings["fbanned_data"].format(
user=awaitget_user_link(user["user_id"]),count=total_count
)
else:
text+=strings["fbanned_nowhere"].format(
user=awaitget_user_link(user["user_id"])
)

iffbanned_fedisTrue:
if"reason"infban_data:
text+=strings["fbanned_in_fed:reason"].format(
fed=html.escape(fed["fed_name"],False),reason=fban_data["reason"]
)
else:
text+=strings["fbanned_in_fed"].format(
fed=html.escape(fed["fed_name"],False)
)
eliffedisnotNone:
text+=strings["not_fbanned_in_fed"].format(
fed_name=html.escape(fed["fed_name"],quote=False)
)

iftotal_count>0:
ifmessage.from_user.id==user["user_id"]:
text+=strings["contact_in_pm"]
iflen(text)>4096:
returnawaitmessage.answer_document(
InputFile(io.StringIO(text),filename="fban_info.txt"),
strings["too_long_fbaninfo"],
reply=message.message_id,
)
awaitmessage.reply(text)


@cached()
asyncdefget_fed_by_id(fed_id:str)->Optional[dict]:
returnawaitdb.feds.find_one({"fed_id":fed_id})


@cached()
asyncdefget_fed_by_creator(creator:int)->Optional[dict]:
returnawaitdb.feds.find_one({"creator":creator})


asyncdef__export__(chat_id):
ifchat_fed:=awaitdb.feds.find_one({"chats":[chat_id]}):
return{"feds":{"fed_id":chat_fed["fed_id"]}}


asyncdef__import__(chat_id,data):
iffed_id:=data["fed_id"]:
ifcurrent_fed:=awaitdb.feds.find_one({"chats":[int(chat_id)]}):
awaitdb.feds.update_one(
{"_id":current_fed["_id"]},{"$pull":{"chats":chat_id}}
)
awaitget_fed_by_id.reset_cache(current_fed["fed_id"])
awaitdb.feds.update_one({"fed_id":fed_id},{"$addToSet":{"chats":chat_id}})
awaitget_fed_by_id.reset_cache(fed_id)


__mod_name__="Federations"

__help__="""
Wellbasicallythereis2reasonstouseFederations:
1.Youhavemanychatsandwanttobanusersinallofthemwith1command
2.YouwanttosubscribetoanyoftheantispamFederationstohaveyourchat(s)protected.
InbothcasesInerukiwillhelpyou.
<b>Argumentstypeshelp:</b>
<code>()</code>:requiredargument
<code>(user)</code>:requiredbutyoucanreplyonanyuser'smessageinstead
<code>(file)</code>:requiredfile,iffileisn'tprovidedyouwillbeenteredinfilestate,thismeansInerukiwillwaitfilemessagefromyou.Type/canceltoleavefromit.
<code>(?)</code>:additionalargument
<b>OnlyFederationowner:</b>
-/fnew(name)or/newfed(name):CreatesanewFederation
-/frename(?FedID)(newname):Renamesyourfederation
-/fdel(?FedID)or/delfed(?FedID):RemovesyourFederation
-/fpromote(user)(?FedID):PromotesausertotheyourFederation
-/fdemote(user)(?FedID):DemotesauserfromtheyourFederation
-/fsub(FedID):SubscibesyourFederationoverprovided
-/funsub(FedID):unsubscibesyourFederationfromprovided
-/fsetlog(?FedID)(?chat/channelid)or/setfedlog(?FedID)(?chat/channelid):Set'salogchat/channelforyourFederation
-/funsetlog(?FedID)or/unsetfedlog(?FedID):UnsetsaFederationlogchat\channel
-/fexport(?FedID):ExportsFederationbans
-/fimport(?FedID)(file):ImportsFederationbans
<b>OnlyChatowner:</b>
-/fjoin(FedID)or/joinfed(FedID):JoinscurrentchattoprovidedFederation
-/fleaveor/leavefed:Leavescurrentchatfromthefed
<b>AvaibleforFederationadminsandowners:</b>
-/fchatlist(?FedID)or/fchats(?FedID):ShowsalistofchatsintheyourFederationlist
-/fban(user)(?FedID)(?reason):BansuserintheFedandFedswhichsubscribedonthisFed
-/sfban(user)(?FedID)(?reason):Asabove,butsilently-meansthemessagesaboutfbanningandrepliedmessage(ifwasprovided)willberemoved
-/unfban(user)(?FedID)(?reason):UnbansauserfromaFederation
<b>Avaibleforallusers:</b>
-/fcheck(?user):Checkuser'sfederationbaninfo
-/finfo(?FedID):InfoaboutFederation
"""
