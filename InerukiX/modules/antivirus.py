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

importcloudmersive_virus_api_client
fromtelethon.tlimportfunctions,types
fromtelethon.tl.typesimportDocumentAttributeFilename,MessageMediaDocument

fromIneruki.configimportget_str_key
fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbot


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


VIRUS_API_KEY=get_str_key("VIRUS_API_KEY",required=False)
configuration=cloudmersive_virus_api_client.Configuration()
configuration.api_key["Apikey"]=VIRUS_API_KEY
api_instance=cloudmersive_virus_api_client.ScanApi(
cloudmersive_virus_api_client.ApiClient(configuration)
)
allow_executables=True
allow_invalid_files=True
allow_scripts=True
allow_password_protected_files=True


@register(pattern="^/scanit$")
asyncdefvirusscan(event):
ifevent.fwd_from:
return
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
else:
return
ifnotevent.reply_to_msg_id:
awaitevent.reply("Replytoafiletoscanit.")
return

c=awaitevent.get_reply_message()
try:
c.media.document
exceptException:
awaitevent.reply("Thatsnotafile.")
return
h=c.media
try:
k=h.document.attributes
exceptException:
awaitevent.reply("Thatsnotafile.")
return
ifnotisinstance(h,MessageMediaDocument):
awaitevent.reply("Thatsnotafile.")
return
ifnotisinstance(k[0],DocumentAttributeFilename):
awaitevent.reply("Thatsnotafile.")
return
try:
virus=c.file.name
awaitevent.client.download_file(c,virus)
gg=awaitevent.reply("Scanningthefile...")
fsize=c.file.size
ifnotfsize<=3145700:#MA=3MB
awaitgg.edit("Filesizeexceeds3MB")
return
api_response=api_instance.scan_file_advanced(
c.file.name,
allow_executables=allow_executables,
allow_invalid_files=allow_invalid_files,
allow_scripts=allow_scripts,
allow_password_protected_files=allow_password_protected_files,
)
ifapi_response.clean_resultisTrue:
awaitgg.edit("Thisfileissafe✔️\nNovirusdetected🐞")
else:
awaitgg.edit("ThisfileisDangerous☠️️\nVirusdetected🐞")
os.remove(virus)
exceptExceptionase:
print(e)
os.remove(virus)
awaitgg.edit("Someerroroccurred.")
return


_mod_name_="VirusScan"
_help_="""
-/scanit:Scanafileforvirus(MASIZE=3MB)
"""
