#Copyright(C)2021errorshivansh


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

importio

fromtelethonimporttypes
fromtelethon.tlimportfunctions,types
fromtelethon.tl.typesimport*

fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbotasborg


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):

returnisinstance(
(
awaitborg(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerChat):

ui=awaitborg.get_peer_id(user)
ps=(
awaitborg(functions.messages.GetFullChatRequest(chat.chat_id))
).full_chat.participants.participants
returnisinstance(
next((pforpinpsifp.user_id==ui),None),
(types.ChatParticipantAdmin,types.ChatParticipantCreator),
)
returnNone


@register(pattern="^/json$")
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
elifevent.chat_id==iidandevent.sender_id==userss:
pass
else:
return
the_real_message=None
reply_to_id=None
ifevent.reply_to_msg_id:
previous_message=awaitevent.get_reply_message()
the_real_message=previous_message.stringify()
reply_to_id=event.reply_to_msg_id
else:
the_real_message=event.stringify()
reply_to_id=event.message.id
iflen(the_real_message)>4095:
withio.BytesIO(str.encode(the_real_message))asout_file:
out_file.name="json.text"
awaitborg.send_file(
event.chat_id,
out_file,
force_document=True,
allow_cache=False,
reply_to=reply_to_id,
)
awaitevent.delete()
else:
awaitevent.reply("`{}`".format(the_real_message))
