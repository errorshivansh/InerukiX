#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2019Aiogram
#
#ThisfileispartofIneruki(TelegramBot)
#
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

importdatetime
importhtml

fromaiogram.dispatcher.middlewaresimportBaseMiddleware

fromInerukiimportdp
fromIneruki.decoratorimportregister
fromIneruki.modulesimportLOADED_MODULES
fromIneruki.services.mongoimportdb
fromIneruki.utils.loggerimportlog

from.utils.connectionsimportchat_connection
from.utils.disableimportdisableable_dec
from.utils.languageimportget_strings_dec
from.utils.user_detailsimport(
get_admins_rights,
get_user_dec,
get_user_link,
is_user_admin,
)


asyncdefupdate_users_handler(message):
chat_id=message.chat.id

#Updatechat
new_chat=message.chat
ifnotnew_chat.type=="private":

old_chat=awaitdb.chat_list.find_one({"chat_id":chat_id})

ifnothasattr(new_chat,"username"):
chatnick=None
else:
chatnick=new_chat.username

ifold_chatand"first_detected_date"inold_chat:
first_detected_date=old_chat["first_detected_date"]
else:
first_detected_date=datetime.datetime.now()

chat_new={
"chat_id":chat_id,
"chat_title":html.escape(new_chat.title,quote=False),
"chat_nick":chatnick,
"type":new_chat.type,
"first_detected_date":first_detected_date,
}

#CheckonoldchatinDBwithsameusername
find_old_chat={
"chat_nick":chat_new["chat_nick"],
"chat_id":{"$ne":chat_new["chat_id"]},
}
ifchat_new["chat_nick"]and(
check:=awaitdb.chat_list.find_one(find_old_chat)
):
awaitdb.chat_list.delete_one({"_id":check["_id"]})
log.info(
f"Foundchat({check['chat_id']})withsameusernameas({chat_new['chat_id']}),oldchatwasdeleted."
)

awaitdb.chat_list.update_one(
{"chat_id":chat_id},{"$set":chat_new},upsert=True
)

log.debug(f"Users:Chat{chat_id}updated")

#Updateusers
awaitupdate_user(chat_id,message.from_user)

if(
"reply_to_message"inmessage
andhasattr(message.reply_to_message.from_user,"chat_id")
andmessage.reply_to_message.from_user.chat_id
):
awaitupdate_user(chat_id,message.reply_to_message.from_user)

if"forward_from"inmessage:
awaitupdate_user(chat_id,message.forward_from)


asyncdefupdate_user(chat_id,new_user):
old_user=awaitdb.user_list.find_one({"user_id":new_user.id})

new_chat=[chat_id]

ifold_userand"chats"inold_user:
ifold_user["chats"]:
new_chat=old_user["chats"]
ifnotnew_chatorchat_idnotinnew_chat:
new_chat.append(chat_id)

ifold_userand"first_detected_date"inold_user:
first_detected_date=old_user["first_detected_date"]
else:
first_detected_date=datetime.datetime.now()

ifnew_user.username:
username=new_user.username.lower()
else:
username=None

ifhasattr(new_user,"last_name")andnew_user.last_name:
last_name=html.escape(new_user.last_name,quote=False)
else:
last_name=None

first_name=html.escape(new_user.first_name,quote=False)

user_new={
"user_id":new_user.id,
"first_name":first_name,
"last_name":last_name,
"username":username,
"user_lang":new_user.language_code,
"chats":new_chat,
"first_detected_date":first_detected_date,
}

#CheckonolduserinDBwithsameusername
find_old_user={
"username":user_new["username"],
"user_id":{"$ne":user_new["user_id"]},
}
ifuser_new["username"]and(check:=awaitdb.user_list.find_one(find_old_user)):
awaitdb.user_list.delete_one({"_id":check["_id"]})
log.info(
f"Founduser({check['user_id']})withsameusernameas({user_new['user_id']}),olduserwasdeleted."
)

awaitdb.user_list.update_one(
{"user_id":new_user.id},{"$set":user_new},upsert=True
)

log.debug(f"Users:User{new_user.id}updated")

returnuser_new


@register(cmds="info")
@disableable_dec("info")
@get_user_dec(allow_self=True)
@get_strings_dec("users")
asyncdefuser_info(message,user,strings):
chat_id=message.chat.id

text=strings["user_info"]
text+=strings["info_id"].format(id=user["user_id"])
text+=strings["info_first"].format(first_name=str(user["first_name"]))

ifuser["last_name"]isnotNone:
text+=strings["info_last"].format(last_name=str(user["last_name"]))

ifuser["username"]isnotNone:
text+=strings["info_username"].format(username="@"+str(user["username"]))

text+=strings["info_link"].format(
user_link=str(awaitget_user_link(user["user_id"]))
)

text+="\n"

ifawaitis_user_admin(chat_id,user["user_id"])isTrue:
text+=strings["info_admeme"]

formodulein[mforminLOADED_MODULESifhasattr(m,"__user_info__")]:
iftxt:=awaitmodule.__user_info__(message,user["user_id"]):
text+=txt

text+=strings["info_saw"].format(num=len(user["chats"])if"chats"inuserelse0)

awaitmessage.reply(text)


@register(cmds="admincache",is_admin=True)
@chat_connection(only_groups=True,admin=True)
@get_strings_dec("users")
asyncdefreset_admins_cache(message,chat,strings):
#Resetacache
awaitget_admins_rights(chat["chat_id"],force_update=True)
awaitmessage.reply(strings["upd_cache_done"])


@register(cmds=["id","chatid","userid"])
@disableable_dec("id")
@get_user_dec(allow_self=True)
@get_strings_dec("misc")
@chat_connection()
asyncdefget_id(message,user,strings,chat):
user_id=message.from_user.id

text=strings["your_id"].format(id=user_id)
ifmessage.chat.id!=user_id:
text+=strings["chat_id"].format(id=message.chat.id)

ifchat["status"]isTrue:
text+=strings["conn_chat_id"].format(id=chat["chat_id"])

ifnotuser["user_id"]==user_id:
text+=strings["user_id"].format(
user=awaitget_user_link(user["user_id"]),id=user["user_id"]
)

if(
"reply_to_message"inmessage
and"forward_from"inmessage.reply_to_message
andnotmessage.reply_to_message.forward_from.id
==message.reply_to_message.from_user.id
):
text+=strings["user_id"].format(
user=awaitget_user_link(message.reply_to_message.forward_from.id),
id=message.reply_to_message.forward_from.id,
)

awaitmessage.reply(text)


@register(cmds=["adminlist","admins"])
@disableable_dec("adminlist")
@chat_connection(only_groups=True)
@get_strings_dec("users")
asyncdefadminlist(message,chat,strings):
admins=awaitget_admins_rights(chat["chat_id"])
text=strings["admins"]
foradmin,rightsinadmins.items():
ifrights["anonymous"]:
continue
text+="-{}(<code>{}</code>)\n".format(awaitget_user_link(admin),admin)

awaitmessage.reply(text,disable_notification=True)


classSaveUser(BaseMiddleware):
asyncdefon_process_message(self,message,data):
awaitupdate_users_handler(message)


asyncdef__before_serving__(loop):
dp.middleware.setup(SaveUser())


asyncdef__stats__():
text="*<code>{}</code>totalusers,in<code>{}</code>chats\n".format(
awaitdb.user_list.count_documents({}),awaitdb.chat_list.count_documents({})
)

text+="*<code>{}</code>newusersand<code>{}</code>newchatsinthelast48hours\n".format(
awaitdb.user_list.count_documents(
{
"first_detected_date":{
"$gte":datetime.datetime.now()-datetime.timedelta(days=2)
}
}
),
awaitdb.chat_list.count_documents(
{
"first_detected_date":{
"$gte":datetime.datetime.now()-datetime.timedelta(days=2)
}
}
),
)

returntext
