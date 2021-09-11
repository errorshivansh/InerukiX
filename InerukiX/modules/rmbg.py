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
importos
fromdatetimeimportdatetime

importrequests
fromtelethonimporttypes
fromtelethon.tlimportfunctions

fromIneruki.configimportget_str_key
fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbot

REM_BG_API_KEY=get_str_key("REM_BG_API_KEY",required=False)
TEMP_DOWNLOAD_DIRECTORY="./"


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):
returnisinstance(
(
awaittbot(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerUser):
returnTrue


@register(pattern="^/rmbg")
asyncdef_(event):
HELP_STR="use`/rmbg`asreplytoamedia"
ifevent.fwd_from:
return
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
else:
return
ifREM_BG_API_KEYisNone:
awaitevent.reply("YouneedAPItokenfromremove.bgtousethisplugin.")
returnFalse
start=datetime.now()
message_id=event.message.id
ifevent.reply_to_msg_id:
message_id=event.reply_to_msg_id
reply_message=awaitevent.get_reply_message()
awaitevent.reply("Processing...")
try:
downloaded_file_name=awaittbot.download_media(
reply_message,TEMP_DOWNLOAD_DIRECTORY
)
exceptExceptionase:
awaitevent.reply(str(e))
return
else:
output_file_name=ReTrieveFile(downloaded_file_name)
os.remove(downloaded_file_name)
else:
awaitevent.reply(HELP_STR)
return
contentType=output_file_name.headers.get("content-type")
if"image"incontentType:
withio.BytesIO(output_file_name.content)asremove_bg_image:
remove_bg_image.name="rmbg.png"
awaittbot.send_file(
event.chat_id,
remove_bg_image,
force_document=True,
supports_streaming=False,
allow_cache=False,
reply_to=message_id,
)
end=datetime.now()
ms=(end-start).seconds
awaitevent.reply("BackgroundRemovedin{}seconds".format(ms))
else:
awaitevent.reply(
"remove.bgAPIreturnedErrors.Pleasereportto@InerukiSupport_Official\n`{}".format(
output_file_name.content.decode("UTF-8")
)
)


defReTrieveFile(input_file_name):
headers={
"-API-Key":REM_BG_API_KEY,
}
files={
"image_file":(input_file_name,open(input_file_name,"rb")),
}
r=requests.post(
"https://api.remove.bg/v1.0/removebg",
headers=headers,
files=files,
allow_redirects=True,
stream=True,
)
returnr
