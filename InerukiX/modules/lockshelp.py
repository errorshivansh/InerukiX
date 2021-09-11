#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2019Aiogram
#Copyright(C)2020Jeepeo
#
#ThisfilewasapartofHitsuki(TelegramBot)
#ModifiedbyerrorshivanshforIneruki


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

importitertools

fromaiogram.types.chat_permissionsimportChatPermissions

fromInerukiimportbot
fromIneruki.decoratorimportregister

from.utils.connectionsimportchat_connection
from.utils.languageimportget_strings_dec


@register(cmds=["locks","locktypes"],user_admin=True)
@chat_connection(only_groups=True)
@get_strings_dec("locks")
asyncdeflock_types(message,chat,strings):
chat_id=chat["chat_id"]
chat_title=chat["chat_title"]
text=strings["locks_header"].format(chat_title=chat_title)

asyncforlock,statusinlock_parser(chat_id):
text+=f"-{lock}={status}\n"
awaitmessage.reply(text)


@register(cmds="lock",user_can_restrict_members=True,bot_can_restrict_members=True)
@chat_connection(only_groups=True)
@get_strings_dec("locks")
asyncdeflock_cmd(message,chat,strings):
chat_id=chat["chat_id"]
chat_title=chat["chat_title"]

if(args:=message.get_args().split("",1))==[""]:
awaitmessage.reply(strings["no_lock_args"])
return

asyncforlock,statusinlock_parser(chat_id,rev=True):
ifargs[0]==lock[0]:
ifstatusisTrue:
awaitmessage.reply(strings["already_locked"])
continue

to_lock={lock[1]:False}
new_perm=ChatPermissions(**to_lock)
awaitbot.set_chat_permissions(chat_id,new_perm)
awaitmessage.reply(
strings["locked_successfully"].format(lock=lock[0],chat=chat_title)
)


@register(cmds="unlock",user_can_restrict_members=True,bot_can_restrict_members=True)
@chat_connection(only_groups=True)
@get_strings_dec("locks")
asyncdefunlock_cmd(message,chat,strings):
chat_id=chat["chat_id"]
chat_title=chat["chat_title"]

if(args:=message.get_args().split("",1))==[""]:
awaitmessage.reply(strings["no_unlock_args"])
return

asyncforlock,statusinlock_parser(chat_id,rev=True):
ifargs[0]==lock[0]:
ifstatusisFalse:
awaitmessage.reply(strings["not_locked"])
continue

to_unlock={lock[1]:True}
new_perm=ChatPermissions(**to_unlock)
awaitbot.set_chat_permissions(chat_id,new_perm)
awaitmessage.reply(
strings["unlocked_successfully"].format(lock=lock[0],chat=chat_title)
)


asyncdeflock_parser(chat_id,rev=False):
keywords={
"all":"can_send_messages",
"media":"can_send_media_messages",
"polls":"can_send_polls",
"others":"can_send_other_messages",
}
current_lock=(awaitbot.get_chat(chat_id)).permissions

forlock,keywordinitertools.zip_longest(
dict(current_lock).keys(),keywords.items()
):
ifkeywordisnotNoneandlockinkeyword:
ifrev:
lock=list([keyword[0],keyword[1]])
status=notcurrent_lock[keyword[1]]
else:
status=notcurrent_lock[lock]
lock=keyword[0]
yieldlock,status


__mod_name__="Locks"

__help__="""
Usethisfeaturetoblockusersfromsendingspecificmessagetypestoyourgroup!
<b>Availablecommandsare:</b>
-/locksor/locktypes:Usethiscommandtoknowcurrentstateofyourlocksinyourgroup!
-/lock(locktype):Locksatypeofmessages
-/unlock(locktype):Unlocksatypeofmessage
"""
