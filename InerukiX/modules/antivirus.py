#XCopyrightX(C)X2021Xerrorshivansh


#XThisXfileXisXpartXofXInerukiX(TelegramXBot)

#XThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXas
#XpublishedXbyXtheXFreeXSoftwareXFoundation,XeitherXversionX3XofXthe
#XLicense,XorX(atXyourXoption)XanyXlaterXversion.

#XThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.

#XYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XalongXwithXthisXprogram.XXIfXnot,XseeX<http://www.gnu.org/licenses/>.


importXos

importXcloudmersive_virus_api_client
fromXtelethon.tlXimportXfunctions,Xtypes
fromXtelethon.tl.typesXimportXDocumentAttributeFilename,XMessageMediaDocument

fromXInerukiX.configXimportXget_str_key
fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbot


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXtbot(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXifXisinstance(chat,Xtypes.InputPeerUser):
XXXXXXXXreturnXTrue


VIRUS_API_KEYX=Xget_str_key("VIRUS_API_KEY",Xrequired=False)
configurationX=Xcloudmersive_virus_api_client.Configuration()
configuration.api_key["Apikey"]X=XVIRUS_API_KEY
api_instanceX=Xcloudmersive_virus_api_client.ScanApi(
XXXXcloudmersive_virus_api_client.ApiClient(configuration)
)
allow_executablesX=XTrue
allow_invalid_filesX=XTrue
allow_scriptsX=XTrue
allow_password_protected_filesX=XTrue


@register(pattern="^/scanit$")
asyncXdefXvirusscan(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXifXnotXevent.reply_to_msg_id:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXfileXtoXscanXit.")
XXXXXXXXreturn

XXXXcX=XawaitXevent.get_reply_message()
XXXXtry:
XXXXXXXXc.media.document
XXXXexceptXException:
XXXXXXXXawaitXevent.reply("ThatsXnotXaXfile.")
XXXXXXXXreturn
XXXXhX=Xc.media
XXXXtry:
XXXXXXXXkX=Xh.document.attributes
XXXXexceptXException:
XXXXXXXXawaitXevent.reply("ThatsXnotXaXfile.")
XXXXXXXXreturn
XXXXifXnotXisinstance(h,XMessageMediaDocument):
XXXXXXXXawaitXevent.reply("ThatsXnotXaXfile.")
XXXXXXXXreturn
XXXXifXnotXisinstance(k[0],XDocumentAttributeFilename):
XXXXXXXXawaitXevent.reply("ThatsXnotXaXfile.")
XXXXXXXXreturn
XXXXtry:
XXXXXXXXvirusX=Xc.file.name
XXXXXXXXawaitXevent.client.download_file(c,Xvirus)
XXXXXXXXggX=XawaitXevent.reply("ScanningXtheXfileX...")
XXXXXXXXfsizeX=Xc.file.size
XXXXXXXXifXnotXfsizeX<=X3145700:XX#XMAXX=X3MB
XXXXXXXXXXXXawaitXgg.edit("FileXsizeXexceedsX3MB")
XXXXXXXXXXXXreturn
XXXXXXXXapi_responseX=Xapi_instance.scan_file_advanced(
XXXXXXXXXXXXc.file.name,
XXXXXXXXXXXXallow_executables=allow_executables,
XXXXXXXXXXXXallow_invalid_files=allow_invalid_files,
XXXXXXXXXXXXallow_scripts=allow_scripts,
XXXXXXXXXXXXallow_password_protected_files=allow_password_protected_files,
XXXXXXXX)
XXXXXXXXifXapi_response.clean_resultXisXTrue:
XXXXXXXXXXXXawaitXgg.edit("ThisXfileXisXsafeX✔️\nNoXvirusXdetectedX🐞")
XXXXXXXXelse:
XXXXXXXXXXXXawaitXgg.edit("ThisXfileXisXDangerousX☠️️\nVirusXdetectedX🐞")
XXXXXXXXos.remove(virus)
XXXXexceptXExceptionXasXe:
XXXXXXXXprint(e)
XXXXXXXXos.remove(virus)
XXXXXXXXawaitXgg.edit("SomeXerrorXoccurred.")
XXXXXXXXreturn


_mod_name_X=X"VirusXScan"
_help_X=X"""
X-X/scanit:XScanXaXfileXforXvirusX(MAXXSIZEX=X3MB)
X"""
