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
importtime
importzipfile

fromtelethonimporttypes
fromtelethon.tlimportfunctions

fromInerukiimportTEMP_DOWNLOAD_DIRECTORY
fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbotasclient


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):

returnisinstance(
(
awaitclient(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerChat):

ui=awaitclient.get_peer_id(user)
ps=(
awaitclient(functions.messages.GetFullChatRequest(chat.chat_id))
).full_chat.participants.participants
returnisinstance(
next((pforpinpsifp.user_id==ui),None),
(types.ChatParticipantAdmin,types.ChatParticipantCreator),
)
returnNone


@register(pattern="^/zip")
asyncdef_(event):
ifevent.fwd_from:
return

ifnotevent.is_reply:
awaitevent.reply("Replytoafiletocompressit.")
return
ifevent.is_group:
ifnot(awaitis_register_admin(event.input_chat,event.message.sender_id)):
awaitevent.reply(
"Hai..Youarenotadmin..Youcan'tusethiscommand..Butyoucanuseinmypm"
)
return

mone=awaitevent.reply("`⏳️Pleasewait...`")
ifnotos.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
ifevent.reply_to_msg_id:
reply_message=awaitevent.get_reply_message()
try:
time.time()
downloaded_file_name=awaitevent.client.download_media(
reply_message,TEMP_DOWNLOAD_DIRECTORY
)
directory_name=downloaded_file_name
exceptExceptionase:#pylint:disable=C0103,W0703
awaitmone.reply(str(e))
zipfile.ZipFile(directory_name+".zip","w",zipfile.ZIP_DEFLATED).write(
directory_name
)
awaitevent.client.send_file(
event.chat_id,
directory_name+".zip",
force_document=True,
allow_cache=False,
reply_to=event.message.id,
)


defzipdir(path,ziph):
#ziphiszipfilehandle
forroot,dirs,filesinos.walk(path):
forfileinfiles:
ziph.write(os.path.join(root,file))
os.remove(os.path.join(root,file))


fromdatetimeimportdatetime

fromhachoir.metadataimportextractMetadata
fromhachoir.parserimportcreateParser
fromtelethon.tl.typesimportDocumentAttributeVideo

extracted=TEMP_DOWNLOAD_DIRECTORY+"extracted/"
thumb_image_path=TEMP_DOWNLOAD_DIRECTORY+"/thumb_image.jpg"
ifnotos.path.isdir(extracted):
os.makedirs(extracted)


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):

returnisinstance(
(
awaitclient(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerChat):

ui=awaitclient.get_peer_id(user)
ps=(
awaitclient(functions.messages.GetFullChatRequest(chat.chat_id))
).full_chat.participants.participants
returnisinstance(
next((pforpinpsifp.user_id==ui),None),
(types.ChatParticipantAdmin,types.ChatParticipantCreator),
)
returnNone


@register(pattern="^/unzip")
asyncdef_(event):
ifevent.fwd_from:
return

ifnotevent.is_reply:
awaitevent.reply("Replytoazipfile.")
return
ifevent.is_group:
ifnot(awaitis_register_admin(event.input_chat,event.message.sender_id)):
awaitevent.reply(
"Hai..Youarenotadmin..Youcan'tusethiscommand..Butyoucanuseinmypm🙈"
)
return

mone=awaitevent.reply("Processing...")
ifnotos.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
ifevent.reply_to_msg_id:
start=datetime.now()
reply_message=awaitevent.get_reply_message()
try:
time.time()
downloaded_file_name=awaitclient.download_media(
reply_message,TEMP_DOWNLOAD_DIRECTORY
)
exceptExceptionase:
awaitmone.reply(str(e))
else:
end=datetime.now()
(end-start).seconds

withzipfile.ZipFile(downloaded_file_name,"r")aszip_ref:
zip_ref.extractall(extracted)
filename=sorted(get_lst_of_files(extracted,[]))
awaitevent.reply("Unzippingnow")
forsingle_fileinfilename:
ifos.path.exists(single_file):
caption_rts=os.path.basename(single_file)
force_document=True
supports_streaming=False
document_attributes=[]
ifsingle_file.endswith((".mp4",".mp3",".flac",".webm")):
metadata=extractMetadata(createParser(single_file))
duration=0
width=0
height=0
ifmetadata.has("duration"):
duration=metadata.get("duration").seconds
ifos.path.exists(thumb_image_path):
metadata=extractMetadata(createParser(thumb_image_path))
ifmetadata.has("width"):
width=metadata.get("width")
ifmetadata.has("height"):
height=metadata.get("height")
document_attributes=[
DocumentAttributeVideo(
duration=duration,
w=width,
h=height,
round_message=False,
supports_streaming=True,
)
]
try:
awaitclient.send_file(
event.chat_id,
single_file,
force_document=force_document,
supports_streaming=supports_streaming,
allow_cache=False,
reply_to=event.message.id,
attributes=document_attributes,
)
exceptExceptionase:
awaitclient.send_message(
event.chat_id,
"{}caused`{}`".format(caption_rts,str(e)),
reply_to=event.message.id,
)
continue
os.remove(single_file)
os.remove(downloaded_file_name)


defget_lst_of_files(input_directory,output_lst):
filesinfolder=os.listdir(input_directory)
forfile_nameinfilesinfolder:
current_file_name=os.path.join(input_directory,file_name)
ifos.path.isdir(current_file_name):
returnget_lst_of_files(current_file_name,output_lst)
output_lst.append(current_file_name)
returnoutput_lst
