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

importhtml

fromaiogram.utils.exceptionsimportChatAdminRequired
fromtelethon.errorsimportAdminRankEmojiNotAllowedError

fromInerukiimportBOT_ID,bot
fromIneruki.decoratorimportregister
fromIneruki.services.telethonimporttbot

from.utils.connectionsimportchat_connection
from.utils.languageimportget_strings_dec
from.utils.user_detailsimport(
get_admins_rights,
get_user_and_text_dec,
get_user_dec,
get_user_link,
)


@register(cmds="promote",bot_can_promote_members=True,user_can_promote_members=True)
@chat_connection(admin=True,only_groups=True)
@get_user_and_text_dec()
@get_strings_dec("promotes")
asyncdefpromote(message,chat,user,args,strings):
chat_id=chat["chat_id"]
text=strings["promote_success"].format(
user=awaitget_user_link(user["user_id"]),chat_name=chat["chat_title"]
)

ifuser["user_id"]==BOT_ID:
return

ifuser["user_id"]==message.from_user.id:
returnawaitmessage.reply(strings["cant_promote_yourself"])

title=None

ifargs:
iflen(args)>16:
awaitmessage.reply(strings["rank_to_loong"])
return
title=args
text+=strings["promote_title"].format(role=html.escape(title,quote=False))

try:
awaittbot.edit_admin(
chat_id,
user["user_id"],
invite_users=True,
change_info=True,
ban_users=True,
delete_messages=True,
pin_messages=True,
title=title,
)
exceptValueError:
returnawaitmessage.reply(strings["cant_get_user"])
exceptAdminRankEmojiNotAllowedError:
returnawaitmessage.reply(strings["emoji_not_allowed"])
awaitget_admins_rights(chat_id,force_update=True)#Resetacache
awaitmessage.reply(text)


@register(cmds="demote",bot_can_promote_members=True,user_can_promote_members=True)
@chat_connection(admin=True,only_groups=True)
@get_user_dec()
@get_strings_dec("promotes")
asyncdefdemote(message,chat,user,strings):
chat_id=chat["chat_id"]
ifuser["user_id"]==BOT_ID:
return

try:
awaitbot.promote_chat_member(chat_id,user["user_id"])
exceptChatAdminRequired:
returnawaitmessage.reply(strings["demote_failed"])

awaitget_admins_rights(chat_id,force_update=True)#Resetacache
awaitmessage.reply(
strings["demote_success"].format(
user=awaitget_user_link(user["user_id"]),chat_name=chat["chat_title"]
)
)
