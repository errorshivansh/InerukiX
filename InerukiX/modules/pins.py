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

fromaiogram.utils.exceptionsimportBadRequest

fromInerukiimportbot
fromIneruki.decoratorimportregister

from.utils.connectionsimportchat_connection
from.utils.languageimportget_strings_dec
from.utils.messageimportget_arg


@register(cmds="unpin",user_can_pin_messages=True,bot_can_pin_messages=True)
@chat_connection(admin=True)
@get_strings_dec("pins")
asyncdefunpin_message(message,chat,strings):
#supportunpinningall
ifget_arg(message)in{"all"}:
returnawaitbot.unpin_all_chat_messages(chat["chat_id"])

try:
awaitbot.unpin_chat_message(chat["chat_id"])
exceptBadRequest:
awaitmessage.reply(strings["chat_not_modified_unpin"])
return


@register(cmds="pin",user_can_pin_messages=True,bot_can_pin_messages=True)
@get_strings_dec("pins")
asyncdefpin_message(message,strings):
if"reply_to_message"notinmessage:
awaitmessage.reply(strings["no_reply_msg"])
return
msg=message.reply_to_message.message_id
arg=get_arg(message).lower()

dnd=True
loud=["loud","notify"]
ifarginloud:
dnd=False

try:
awaitbot.pin_chat_message(message.chat.id,msg,disable_notification=dnd)
exceptBadRequest:
awaitmessage.reply(strings["chat_not_modified_pin"])


__mod_name__="Pinning"

__help__="""
Allthepinrelatedcommandscanbefoundhere;keepyourchatuptodateonthelatestnewswithasimplepinnedmessage!

<b>BasicPins</b>
-/pin:silentlypinsthemessagerepliedto-add'loud'or'notify'togivenotifstousers.
-/unpin:unpinsthecurrentlypinnedmessage-add'all'tounpinallpinnedmessages.

<b>Other</b>
-/permapin[reply]:Pinacustommessagethroughthebot.Thismessagecancontainmarkdown,buttons,andalltheothercoolfeatures.
-/unpinall:Unpinsallpinnedmessages.
-/antichannelpin[yes/no/on/off]:Don'tlettelegramauto-pinlinkedchannels.Ifnoargumentsaregiven,showscurrentsetting.
-/cleanlinked[yes/no/on/off]:Deletemessagessentbythelinkedchannel.

Note:Whenusingantichannelpins,makesuretousethe/unpincommand,insteadofdoingitmanually.Otherwise,theoldmessagewillgetre-pinnedwhenthechannelsendsanymessages.
"""
