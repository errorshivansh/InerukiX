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
importXtime
importXzipfile

fromXtelethonXimportXtypes
fromXtelethon.tlXimportXfunctions

fromXInerukiXXimportXTEMP_DOWNLOAD_DIRECTORY
fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbotXasXclient


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):

XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXclient(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXifXisinstance(chat,Xtypes.InputPeerChat):

XXXXXXXXuiX=XawaitXclient.get_peer_id(user)
XXXXXXXXpsX=X(
XXXXXXXXXXXXawaitXclient(functions.messages.GetFullChatRequest(chat.chat_id))
XXXXXXXX).full_chat.participants.participants
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXXnext((pXforXpXinXpsXifXp.user_idX==Xui),XNone),
XXXXXXXXXXXX(types.ChatParticipantAdmin,Xtypes.ChatParticipantCreator),
XXXXXXXX)
XXXXreturnXNone


@register(pattern="^/zip")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn

XXXXifXnotXevent.is_reply:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXfileXtoXcompressXit.")
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXnotX(awaitXis_register_admin(event.input_chat,Xevent.message.sender_id)):
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"Hai..XYouXareXnotXadmin..XYouXcan'tXuseXthisXcommand..XButXyouXcanXuseXinXmyXpm"
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn

XXXXmoneX=XawaitXevent.reply("`⏳️XPleaseXwait...`")
XXXXifXnotXos.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
XXXXXXXXos.makedirs(TEMP_DOWNLOAD_DIRECTORY)
XXXXifXevent.reply_to_msg_id:
XXXXXXXXreply_messageX=XawaitXevent.get_reply_message()
XXXXXXXXtry:
XXXXXXXXXXXXtime.time()
XXXXXXXXXXXXdownloaded_file_nameX=XawaitXevent.client.download_media(
XXXXXXXXXXXXXXXXreply_message,XTEMP_DOWNLOAD_DIRECTORY
XXXXXXXXXXXX)
XXXXXXXXXXXXdirectory_nameX=Xdownloaded_file_name
XXXXXXXXexceptXExceptionXasXe:XX#Xpylint:disable=C0103,W0703
XXXXXXXXXXXXawaitXmone.reply(str(e))
XXXXzipfile.ZipFile(directory_nameX+X".zip",X"w",Xzipfile.ZIP_DEFLATED).write(
XXXXXXXXdirectory_name
XXXX)
XXXXawaitXevent.client.send_file(
XXXXXXXXevent.chat_id,
XXXXXXXXdirectory_nameX+X".zip",
XXXXXXXXforce_document=True,
XXXXXXXXallow_cache=False,
XXXXXXXXreply_to=event.message.id,
XXXX)


defXzipdir(path,Xziph):
XXXX#XziphXisXzipfileXhandle
XXXXforXroot,Xdirs,XfilesXinXos.walk(path):
XXXXXXXXforXfileXinXfiles:
XXXXXXXXXXXXziph.write(os.path.join(root,Xfile))
XXXXXXXXXXXXos.remove(os.path.join(root,Xfile))


fromXdatetimeXimportXdatetime

fromXhachoir.metadataXimportXextractMetadata
fromXhachoir.parserXimportXcreateParser
fromXtelethon.tl.typesXimportXDocumentAttributeVideo

extractedX=XTEMP_DOWNLOAD_DIRECTORYX+X"extracted/"
thumb_image_pathX=XTEMP_DOWNLOAD_DIRECTORYX+X"/thumb_image.jpg"
ifXnotXos.path.isdir(extracted):
XXXXos.makedirs(extracted)


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):

XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXclient(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXifXisinstance(chat,Xtypes.InputPeerChat):

XXXXXXXXuiX=XawaitXclient.get_peer_id(user)
XXXXXXXXpsX=X(
XXXXXXXXXXXXawaitXclient(functions.messages.GetFullChatRequest(chat.chat_id))
XXXXXXXX).full_chat.participants.participants
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXXnext((pXforXpXinXpsXifXp.user_idX==Xui),XNone),
XXXXXXXXXXXX(types.ChatParticipantAdmin,Xtypes.ChatParticipantCreator),
XXXXXXXX)
XXXXreturnXNone


@register(pattern="^/unzip")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn

XXXXifXnotXevent.is_reply:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXzipXfile.")
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXnotX(awaitXis_register_admin(event.input_chat,Xevent.message.sender_id)):
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"XHai..XYouXareXnotXadmin..XYouXcan'tXuseXthisXcommand..XButXyouXcanXuseXinXmyXpm🙈"
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn

XXXXmoneX=XawaitXevent.reply("ProcessingX...")
XXXXifXnotXos.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
XXXXXXXXos.makedirs(TEMP_DOWNLOAD_DIRECTORY)
XXXXifXevent.reply_to_msg_id:
XXXXXXXXstartX=Xdatetime.now()
XXXXXXXXreply_messageX=XawaitXevent.get_reply_message()
XXXXXXXXtry:
XXXXXXXXXXXXtime.time()
XXXXXXXXXXXXdownloaded_file_nameX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXreply_message,XTEMP_DOWNLOAD_DIRECTORY
XXXXXXXXXXXX)
XXXXXXXXexceptXExceptionXasXe:
XXXXXXXXXXXXawaitXmone.reply(str(e))
XXXXXXXXelse:
XXXXXXXXXXXXendX=Xdatetime.now()
XXXXXXXXXXXX(endX-Xstart).seconds

XXXXXXXXwithXzipfile.ZipFile(downloaded_file_name,X"r")XasXzip_ref:
XXXXXXXXXXXXzip_ref.extractall(extracted)
XXXXXXXXfilenameX=Xsorted(get_lst_of_files(extracted,X[]))
XXXXXXXXawaitXevent.reply("UnzippingXnow")
XXXXXXXXforXsingle_fileXinXfilename:
XXXXXXXXXXXXifXos.path.exists(single_file):
XXXXXXXXXXXXXXXXcaption_rtsX=Xos.path.basename(single_file)
XXXXXXXXXXXXXXXXforce_documentX=XTrue
XXXXXXXXXXXXXXXXsupports_streamingX=XFalse
XXXXXXXXXXXXXXXXdocument_attributesX=X[]
XXXXXXXXXXXXXXXXifXsingle_file.endswith((".mp4",X".mp3",X".flac",X".webm")):
XXXXXXXXXXXXXXXXXXXXmetadataX=XextractMetadata(createParser(single_file))
XXXXXXXXXXXXXXXXXXXXdurationX=X0
XXXXXXXXXXXXXXXXXXXXwidthX=X0
XXXXXXXXXXXXXXXXXXXXheightX=X0
XXXXXXXXXXXXXXXXXXXXifXmetadata.has("duration"):
XXXXXXXXXXXXXXXXXXXXXXXXdurationX=Xmetadata.get("duration").seconds
XXXXXXXXXXXXXXXXXXXXifXos.path.exists(thumb_image_path):
XXXXXXXXXXXXXXXXXXXXXXXXmetadataX=XextractMetadata(createParser(thumb_image_path))
XXXXXXXXXXXXXXXXXXXXXXXXifXmetadata.has("width"):
XXXXXXXXXXXXXXXXXXXXXXXXXXXXwidthX=Xmetadata.get("width")
XXXXXXXXXXXXXXXXXXXXXXXXifXmetadata.has("height"):
XXXXXXXXXXXXXXXXXXXXXXXXXXXXheightX=Xmetadata.get("height")
XXXXXXXXXXXXXXXXXXXXdocument_attributesX=X[
XXXXXXXXXXXXXXXXXXXXXXXXDocumentAttributeVideo(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXduration=duration,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXw=width,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXh=height,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXround_message=False,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXsupports_streaming=True,
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXXXXXawaitXclient.send_file(
XXXXXXXXXXXXXXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXXXXXXXXXXXXXsingle_file,
XXXXXXXXXXXXXXXXXXXXXXXXforce_document=force_document,
XXXXXXXXXXXXXXXXXXXXXXXXsupports_streaming=supports_streaming,
XXXXXXXXXXXXXXXXXXXXXXXXallow_cache=False,
XXXXXXXXXXXXXXXXXXXXXXXXreply_to=event.message.id,
XXXXXXXXXXXXXXXXXXXXXXXXattributes=document_attributes,
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXexceptXExceptionXasXe:
XXXXXXXXXXXXXXXXXXXXawaitXclient.send_message(
XXXXXXXXXXXXXXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXXXXXXXXXXXXX"{}XcausedX`{}`".format(caption_rts,Xstr(e)),
XXXXXXXXXXXXXXXXXXXXXXXXreply_to=event.message.id,
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXcontinue
XXXXXXXXXXXXXXXXos.remove(single_file)
XXXXXXXXos.remove(downloaded_file_name)


defXget_lst_of_files(input_directory,Xoutput_lst):
XXXXfilesinfolderX=Xos.listdir(input_directory)
XXXXforXfile_nameXinXfilesinfolder:
XXXXXXXXcurrent_file_nameX=Xos.path.join(input_directory,Xfile_name)
XXXXXXXXifXos.path.isdir(current_file_name):
XXXXXXXXXXXXreturnXget_lst_of_files(current_file_name,Xoutput_lst)
XXXXXXXXoutput_lst.append(current_file_name)
XXXXreturnXoutput_lst
