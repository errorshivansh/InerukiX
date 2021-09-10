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


importXio
importXos
fromXdatetimeXimportXdatetime

importXrequests
fromXtelethonXimportXtypes
fromXtelethon.tlXimportXfunctions

fromXInerukiX.configXimportXget_str_key
fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbot

REM_BG_API_KEYX=Xget_str_key("REM_BG_API_KEY",Xrequired=False)
TEMP_DOWNLOAD_DIRECTORYX=X"./"


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


@register(pattern="^/rmbg")
asyncXdefX_(event):
XXXXHELP_STRX=X"useX`/rmbg`XasXreplyXtoXaXmedia"
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXifXREM_BG_API_KEYXisXNone:
XXXXXXXXawaitXevent.reply("YouXneedXAPIXtokenXfromXremove.bgXtoXuseXthisXplugin.")
XXXXXXXXreturnXFalse
XXXXstartX=Xdatetime.now()
XXXXmessage_idX=Xevent.message.id
XXXXifXevent.reply_to_msg_id:
XXXXXXXXmessage_idX=Xevent.reply_to_msg_id
XXXXXXXXreply_messageX=XawaitXevent.get_reply_message()
XXXXXXXXawaitXevent.reply("Processing...")
XXXXXXXXtry:
XXXXXXXXXXXXdownloaded_file_nameX=XawaitXtbot.download_media(
XXXXXXXXXXXXXXXXreply_message,XTEMP_DOWNLOAD_DIRECTORY
XXXXXXXXXXXX)
XXXXXXXXexceptXExceptionXasXe:
XXXXXXXXXXXXawaitXevent.reply(str(e))
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXoutput_file_nameX=XReTrieveFile(downloaded_file_name)
XXXXXXXXXXXXos.remove(downloaded_file_name)
XXXXelse:
XXXXXXXXawaitXevent.reply(HELP_STR)
XXXXXXXXreturn
XXXXcontentTypeX=Xoutput_file_name.headers.get("content-type")
XXXXifX"image"XinXcontentType:
XXXXXXXXwithXio.BytesIO(output_file_name.content)XasXremove_bg_image:
XXXXXXXXXXXXremove_bg_image.nameX=X"rmbg.png"
XXXXXXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXXXXXremove_bg_image,
XXXXXXXXXXXXXXXXforce_document=True,
XXXXXXXXXXXXXXXXsupports_streaming=False,
XXXXXXXXXXXXXXXXallow_cache=False,
XXXXXXXXXXXXXXXXreply_to=message_id,
XXXXXXXXXXXX)
XXXXXXXXendX=Xdatetime.now()
XXXXXXXXmsX=X(endX-Xstart).seconds
XXXXXXXXawaitXevent.reply("BackgroundXRemovedXinX{}Xseconds".format(ms))
XXXXelse:
XXXXXXXXawaitXevent.reply(
XXXXXXXXXXXX"remove.bgXAPIXreturnedXErrors.XPleaseXreportXtoX@InerukiSupport_Official\n`{}".format(
XXXXXXXXXXXXXXXXoutput_file_name.content.decode("UTF-8")
XXXXXXXXXXXX)
XXXXXXXX)


defXReTrieveFile(input_file_name):
XXXXheadersX=X{
XXXXXXXX"X-API-Key":XREM_BG_API_KEY,
XXXX}
XXXXfilesX=X{
XXXXXXXX"image_file":X(input_file_name,Xopen(input_file_name,X"rb")),
XXXX}
XXXXrX=Xrequests.post(
XXXXXXXX"https://api.remove.bg/v1.0/removebg",
XXXXXXXXheaders=headers,
XXXXXXXXfiles=files,
XXXXXXXXallow_redirects=True,
XXXXXXXXstream=True,
XXXX)
XXXXreturnXr
