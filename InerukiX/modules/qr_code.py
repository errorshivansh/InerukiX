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

importos
fromasyncioimportsleep
fromdatetimeimportdatetime

fromrequestsimportget,post
fromtelethon.tlimportfunctions,types

fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbotasclient


defprogress(current,total):
"""Calculateandreturnthedownloadprogresswithgivenarguments."""
print(
"Downloaded{}of{}\nCompleted{}".format(
current,total,(current/total)*100
)
)


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):

returnisinstance(
(
awaitclient(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
elifisinstance(chat,types.InputPeerChat):

ui=awaitclient.get_peer_id(user)
ps=(
awaitclient(functions.messages.GetFullChatRequest(chat.chat_id))
).full_chat.participants.participants
returnisinstance(
next((pforpinpsifp.user_id==ui),None),
(types.ChatParticipantAdmin,types.ChatParticipantCreator),
)
else:
returnNone


@register(pattern=r"^/getqr$")
asyncdefparseqr(qr_e):
"""For.getqrcommand,getQRCodecontentfromtherepliedphoto."""
ifqr_e.fwd_from:
return
start=datetime.now()
downloaded_file_name=awaitqr_e.client.download_media(
awaitqr_e.get_reply_message(),progress_callback=progress
)
url="https://api.qrserver.com/v1/read-qr-code/?outputformat=json"
file=open(downloaded_file_name,"rb")
files={"file":file}
resp=post(url,files=files).json()
qr_contents=resp[0]["symbol"][0]["data"]
file.close()
os.remove(downloaded_file_name)
end=datetime.now()
duration=(end-start).seconds
awaitqr_e.reply(
"ObtainedQRCodecontentsin{}seconds.\n{}".format(duration,qr_contents)
)


@register(pattern=r"^/makeqr(?:|$)([\s\S]*)")
asyncdefmake_qr(qrcode):
"""For.makeqrcommand,makeaQRCodecontainingthegivencontent."""
ifqrcode.fwd_from:
return
start=datetime.now()
input_str=qrcode.pattern_match.group(1)
message="SYNTA:`.makeqr<longtexttoinclude>`"
reply_msg_id=None
ifinput_str:
message=input_str
elifqrcode.reply_to_msg_id:
previous_message=awaitqrcode.get_reply_message()
reply_msg_id=previous_message.id
ifprevious_message.media:
downloaded_file_name=awaitqrcode.client.download_media(
previous_message,progress_callback=progress
)
m_list=None
withopen(downloaded_file_name,"rb")asfile:
m_list=file.readlines()
message=""
formediainm_list:
message+=media.decode("UTF-8")+"\r\n"
os.remove(downloaded_file_name)
else:
message=previous_message.message

url="https://api.qrserver.com/v1/create-qr-code/?data={}&\
size=200x200&charset-source=UTF-8&charset-target=UTF-8\
&ecc=L&color=0-0-0&bgcolor=255-255-255\
&margin=1&qzone=0&format=jpg"

resp=get(url.format(message),stream=True)
required_file_name="temp_qr.webp"
withopen(required_file_name,"w+b")asfile:
forchunkinresp.iter_content(chunk_size=128):
file.write(chunk)
awaitqrcode.client.send_file(
qrcode.chat_id,
required_file_name,
reply_to=reply_msg_id,
progress_callback=progress,
)
os.remove(required_file_name)
duration=(datetime.now()-start).seconds
awaitqrcode.reply("CreatedQRCodein{}seconds".format(duration))
awaitsleep(5)
