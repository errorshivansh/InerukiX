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

importre

fromaiogram.dispatcher.filters.builtinimportCommandStart
fromaiogram.typesimportCallbackQuery
fromaiogram.types.inline_keyboardimportInlineKeyboardButton,InlineKeyboardMarkup
fromaiogram.utils.callback_dataimportCallbackData
fromaiogram.utils.deep_linkingimportget_start_link
fromaiogram.utils.exceptionsimportBotBlocked,CantInitiateConversation

fromInerukiimportbot
fromIneruki.decoratorimportregister
fromIneruki.services.mongoimportdb
fromIneruki.services.redisimportredis

from.utils.connectionsimportchat_connection,get_connection_data,set_connected_chat
from.utils.languageimportget_strings_dec
from.utils.messageimportget_arg
from.utils.notesimportBUTTONS
from.utils.user_detailsimportget_chat_dec,is_user_admin

connect_to_chat_cb=CallbackData("connect_to_chat_cb","chat_id")


@get_strings_dec("connections")
asyncdefdef_connect_chat(message,user_id,chat_id,chat_title,strings,edit=False):
awaitset_connected_chat(user_id,chat_id)

text=strings["pm_connected"].format(chat_name=chat_title)
ifedit:
awaitmessage.edit_text(text)
else:
awaitmessage.reply(text)


#Inchat-connectdirectlytochat
@register(cmds="connect",only_groups=True,no_args=True)
@get_strings_dec("connections")
asyncdefconnect_to_chat_direct(message,strings):
user_id=message.from_user.id
chat_id=message.chat.id

ifuser_id==1087968824:
#justwarntheuserthatconnectionswithadminrightsdoesn'twork
returnawaitmessage.reply(
strings["anon_admin_conn"],
reply_markup=InlineKeyboardMarkup().add(
InlineKeyboardButton(
strings["click_here"],callback_data="anon_conn_cb"
)
),
)

chat=awaitdb.chat_list.find_one({"chat_id":chat_id})
chat_title=chat["chat_title"]ifchatisnotNoneelsemessage.chat.title
text=strings["pm_connected"].format(chat_name=chat_title)

try:
awaitbot.send_message(user_id,text)
awaitdef_connect_chat(message,user_id,chat_id,chat_title)
except(BotBlocked,CantInitiateConversation):
awaitmessage.reply(strings["connected_pm_to_me"].format(chat_name=chat_title))
redis.set("Ineruki_connected_start_state:"+str(user_id),1)


#Inpmwithoutargs-showlastconnectedchats
@register(cmds="connect",no_args=True,only_pm=True)
@get_strings_dec("connections")
@chat_connection()
asyncdefconnect_chat_keyboard(message,strings,chat):
connected_data=awaitget_connection_data(message.from_user.id)
ifnotconnected_data:
returnawaitmessage.reply(strings["u_wasnt_connected"])

ifchat["status"]!="private":
text=strings["connected_chat"].format(chat_name=chat["chat_title"])
elif"command"inconnected_data:
ifchat:=awaitdb.chat_list.find_one({"chat_id":connected_data["chat_id"]}):
chat_title=chat["chat_title"]
else:
chat_title=connected_data["chat_id"]
text=strings["connected_chat:cmds"].format(
chat_name=chat_title,
#disconnectisbuiltincommand,shouldnotbeshown
commands=",".join(
f"<code>/{cmd}</code>"
forcmdinconnected_data["command"]
ifcmd!="disconnect"
),
)
else:
text=""

text+=strings["select_chat_to_connect"]
markup=InlineKeyboardMarkup(row_width=1)
forchat_idinreversed(connected_data["history"][-3:]):
chat=awaitdb.chat_list.find_one({"chat_id":chat_id})
markup.insert(
InlineKeyboardButton(
chat["chat_title"],
callback_data=connect_to_chat_cb.new(chat_id=chat_id),
)
)

awaitmessage.reply(text,reply_markup=markup)


#Callbackforprev.function
@register(connect_to_chat_cb.filter(),f="cb",allow_kwargs=True)
asyncdefconnect_chat_keyboard_cb(message,callback_data=False,**kwargs):
chat_id=int(callback_data["chat_id"])
chat=awaitdb.chat_list.find_one({"chat_id":chat_id})
awaitdef_connect_chat(
message.message,message.from_user.id,chat_id,chat["chat_title"],edit=True
)


#Inpmwithargs-connecttochatbyarg
@register(cmds="connect",has_args=True,only_pm=True)
@get_chat_dec()
@get_strings_dec("connections")
asyncdefconnect_to_chat_from_arg(message,chat,strings):
user_id=message.from_user.id
chat_id=chat["chat_id"]

arg=get_arg(message)
ifarg.startswith("-"):
chat_id=int(arg)

ifnotchat_id:
awaitmessage.reply(strings["cant_find_chat_use_id"])
return

awaitdef_connect_chat(message,user_id,chat_id,chat["chat_title"])


@register(cmds="disconnect",only_pm=True)
@get_strings_dec("connections")
asyncdefdisconnect_from_chat_direct(message,strings):
if(data:=awaitget_connection_data(message.from_user.id))and"chat_id"indata:
chat=awaitdb.chat_list.find_one({"chat_id":data["chat_id"]})
user_id=message.from_user.id
awaitset_connected_chat(user_id,None)
awaitmessage.reply(
strings["disconnected"].format(chat_name=chat["chat_title"])
)


@register(cmds="allowusersconnect")
@get_strings_dec("connections")
@chat_connection(admin=True,only_groups=True)
asyncdefallow_users_to_connect(message,strings,chat):
chat_id=chat["chat_id"]
arg=get_arg(message).lower()
ifnotarg:
status=strings["enabled"]
data=awaitdb.chat_connection_settings.find_one({"chat_id":chat_id})
if(
data
and"allow_users_connect"indata
anddata["allow_users_connect"]isFalse
):
status=strings["disabled"]
awaitmessage.reply(
strings["chat_users_connections_info"].format(
status=status,chat_name=chat["chat_title"]
)
)
return
enable=("enable","on","ok","yes")
disable=("disable","off","no")
ifarginenable:
r_bool=True
status=strings["enabled"]
elifargindisable:
r_bool=False
status=strings["disabled"]
else:
awaitmessage.reply(strings["bad_arg_bool"])
return

awaitdb.chat_connection_settings.update_one(
{"chat_id":chat_id},{"$set":{"allow_users_connect":r_bool}},upsert=True
)
awaitmessage.reply(
strings["chat_users_connections_cng"].format(
status=status,chat_name=chat["chat_title"]
)
)


@register(cmds="start",only_pm=True)
@get_strings_dec("connections")
@chat_connection()
asyncdefconnected_start_state(message,strings,chat):
key="Ineruki_connected_start_state:"+str(message.from_user.id)
ifredis.get(key):
awaitmessage.reply(
strings["pm_connected"].format(chat_name=chat["chat_title"])
)
redis.delete(key)


BUTTONS.update({"connect":"btn_connect_start"})


@register(CommandStart(re.compile(r"btn_connect_start")),allow_kwargs=True)
@get_strings_dec("connections")
asyncdefconnect_start(message,strings,regexp=None,**kwargs):
args=message.get_args().split("_")

#Incaseifbuttonhaveargitwillbeused.#TODO:Checkchat_id,parsechatnickname.
arg=args[3]

ifarg.startswith("-")orarg.isdigit():
chat=awaitdb.chat_list.find_one({"chat_id":int(arg)})
elifarg.startswith("@"):
chat=awaitdb.chat_list.find_one({"chat_nick":arg.lower()})
else:
awaitmessage.reply(strings["cant_find_chat_use_id"])
return

awaitdef_connect_chat(
message,message.from_user.id,chat["chat_id"],chat["chat_title"]
)


@register(regexp="anon_conn_cb",f="cb")
asyncdefconnect_anon_admins(event:CallbackQuery):
ifnotawaitis_user_admin(event.message.chat.id,event.from_user.id):
return

if(
event.message.chat.id
notin(data:=awaitdb.user_list.find_one({"user_id":event.from_user.id}))[
"chats"
]
):
awaitdb.user_list.update_one(
{"_id":data["_id"]},{"$addToSet":{"chats":event.message.chat.id}}
)
returnawaitevent.answer(
url=awaitget_start_link(f"btn_connect_start_{event.message.chat.id}")
)


__mod_name__="Connections"

__help__="""
Sometimesyouneedchangesomethinginyourchat,likenotes,butyoudon'twanttospaminit,tryconnections,thisallowyouchangechatsettingsandmanagechat'scontentinpersonalmessagewithIneruki.

<b>Availablecommandsare:</b>
<b>AvaibleonlyinPM:</b>
-/connect:Showlastconnectedchatsbuttonforfastconnection
-/connect(chatIDorchatnickname):Connecttochatbyargumentwhichyouprovided
-/reconnect:Connecttolastconnectedchatbefore
-/disconnect:Disconnectfrom

<b>Avaibleonlyingroups:</b>
-/connect:Directconnecttothisgroup

<b>Othercommands:</b>
-/allowusersconnect(on/offenable/disable):Enableordisableconnectionfeatureforregularusers,foradminsconnectionswillbeworksalways
"""
