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

fromtelethon.errors.rpcerrorlistimportYouBlockedUserError
fromtelethon.tlimportfunctions,types

fromIneruki.services.eventsimportregisterasIneruki
fromIneruki.services.telethonimporttbot
fromIneruki.services.telethonuserbotimportubot


asyncdefis_register_admin(chat,user):

ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):

returnisinstance(
(
awaittbot(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerChat):

ui=awaittbot.get_peer_id(user)
ps=(
awaittbot(functions.messages.GetFullChatRequest(chat.chat_id))
).full_chat.participants.participants
returnisinstance(
next((pforpinpsifp.user_id==ui),None),
(types.ChatParticipantAdmin,types.ChatParticipantCreator),
)
returnNone


asyncdefsilently_send_message(conv,text):
awaitconv.send_message(text)
response=awaitconv.get_response()
awaitconv.mark_read(message=response)
returnresponse


@Ineruki(pattern="^/namehistory?(.*)")
asyncdef_(event):

ifevent.fwd_from:

return

ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
else:
return
ifnotevent.reply_to_msg_id:

awaitevent.reply("```Replytoanyusermessage.```")

return

reply_message=awaitevent.get_reply_message()

ifnotreply_message.text:

awaitevent.reply("```replytotextmessage```")

return

chat="@DetectiveInfoBot"
uid=reply_message.sender_id
reply_message.sender

ifreply_message.sender.bot:

awaitevent.edit("```Replytoactualusersmessage.```")

return

lol=awaitevent.reply("```Processing```")

asyncwithubot.conversation(chat)asconv:

try:

#response=conv.wait_event(
#events.NewMessage(incoming=True,from_users=1706537835)
#)

awaitsilently_send_message(conv,f"/detect_id{uid}")

#response=awaitresponse
responses=awaitsilently_send_message(conv,f"/detect_id{uid}")
exceptYouBlockedUserError:

awaitevent.reply("```Pleaseunblock@DetectiveInfoBotandtryagain```")

return
awaitlol.edit(f"{responses.text}")
#awaitlol.edit(f"{response.message.message}")
