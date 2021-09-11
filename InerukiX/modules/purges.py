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

fromtelethon.errors.rpcerrorlistimportMessageDeleteForbiddenError

fromInerukiimportbot
fromIneruki.decoratorimportregister
fromIneruki.services.telethonimporttbot

from.utils.languageimportget_strings_dec
from.utils.notesimportBUTTONS


@register(cmds="del",bot_can_delete_messages=True,user_can_delete_messages=True)
@get_strings_dec("msg_deleting")
asyncdefdel_message(message,strings):
ifnotmessage.reply_to_message:
awaitmessage.reply(strings["reply_to_msg"])
return
msgs=[message.message_id,message.reply_to_message.message_id]
awaittbot.delete_messages(message.chat.id,msgs)


@register(
cmds="purge",
no_args=True,
bot_can_delete_messages=True,
user_can_delete_messages=True,
)
@get_strings_dec("msg_deleting")
asyncdeffast_purge(message,strings):
ifnotmessage.reply_to_message:
awaitmessage.reply(strings["reply_to_msg"])
return
msg_id=message.reply_to_message.message_id
delete_to=message.message_id

chat_id=message.chat.id
msgs=[]
form_idinrange(int(delete_to),msg_id-1,-1):
msgs.append(m_id)
iflen(msgs)==100:
awaittbot.delete_messages(chat_id,msgs)
msgs=[]

try:
awaittbot.delete_messages(chat_id,msgs)
exceptMessageDeleteForbiddenError:
awaitmessage.reply(strings["purge_error"])
return

msg=awaitbot.send_message(chat_id,strings["fast_purge_done"])
awaitasyncio.sleep(5)
awaitmsg.delete()


BUTTONS.update({"delmsg":"btn_deletemsg_cb"})


@register(regexp=r"btn_deletemsg:(\w+)",f="cb",allow_kwargs=True)
asyncdefdelmsg_btn(event,regexp=None,**kwargs):
awaitevent.message.delete()


__mod_name__="Purges"

__help__="""
Needtodeletelotsofmessages?That'swhatpurgesarefor!

<b>Availablecommands:</b>
-/purge:Deletesallmessagesfromthemessageyourepliedto,tothecurrentmessage.
-/del:Deletesthemessageyourepliedtoandyour"<code>/del</code>"commandmessage.
"""
