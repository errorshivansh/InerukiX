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
fromXasyncioXimportXsleep
fromXdatetimeXimportXdatetime

fromXrequestsXimportXget,Xpost
fromXtelethon.tlXimportXfunctions,Xtypes

fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbotXasXclient


defXprogress(current,Xtotal):
XXXX"""CalculateXandXreturnXtheXdownloadXprogressXwithXgivenXarguments."""
XXXXprint(
XXXXXXXX"DownloadedX{}XofX{}\nCompletedX{}".format(
XXXXXXXXXXXXcurrent,Xtotal,X(currentX/Xtotal)X*X100
XXXXXXXX)
XXXX)


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):

XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXclient(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXelifXisinstance(chat,Xtypes.InputPeerChat):

XXXXXXXXuiX=XawaitXclient.get_peer_id(user)
XXXXXXXXpsX=X(
XXXXXXXXXXXXawaitXclient(functions.messages.GetFullChatRequest(chat.chat_id))
XXXXXXXX).full_chat.participants.participants
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXXnext((pXforXpXinXpsXifXp.user_idX==Xui),XNone),
XXXXXXXXXXXX(types.ChatParticipantAdmin,Xtypes.ChatParticipantCreator),
XXXXXXXX)
XXXXelse:
XXXXXXXXreturnXNone


@register(pattern=r"^/getqr$")
asyncXdefXparseqr(qr_e):
XXXX"""ForX.getqrXcommand,XgetXQRXCodeXcontentXfromXtheXrepliedXphoto."""
XXXXifXqr_e.fwd_from:
XXXXXXXXreturn
XXXXstartX=Xdatetime.now()
XXXXdownloaded_file_nameX=XawaitXqr_e.client.download_media(
XXXXXXXXawaitXqr_e.get_reply_message(),Xprogress_callback=progress
XXXX)
XXXXurlX=X"https://api.qrserver.com/v1/read-qr-code/?outputformat=json"
XXXXfileX=Xopen(downloaded_file_name,X"rb")
XXXXfilesX=X{"file":Xfile}
XXXXrespX=Xpost(url,Xfiles=files).json()
XXXXqr_contentsX=Xresp[0]["symbol"][0]["data"]
XXXXfile.close()
XXXXos.remove(downloaded_file_name)
XXXXendX=Xdatetime.now()
XXXXdurationX=X(endX-Xstart).seconds
XXXXawaitXqr_e.reply(
XXXXXXXX"ObtainedXQRCodeXcontentsXinX{}Xseconds.\n{}".format(duration,Xqr_contents)
XXXX)


@register(pattern=r"^/makeqr(?:X|$)([\s\S]*)")
asyncXdefXmake_qr(qrcode):
XXXX"""ForX.makeqrXcommand,XmakeXaXQRXCodeXcontainingXtheXgivenXcontent."""
XXXXifXqrcode.fwd_from:
XXXXXXXXreturn
XXXXstartX=Xdatetime.now()
XXXXinput_strX=Xqrcode.pattern_match.group(1)
XXXXmessageX=X"SYNTAX:X`.makeqrX<longXtextXtoXinclude>`"
XXXXreply_msg_idX=XNone
XXXXifXinput_str:
XXXXXXXXmessageX=Xinput_str
XXXXelifXqrcode.reply_to_msg_id:
XXXXXXXXprevious_messageX=XawaitXqrcode.get_reply_message()
XXXXXXXXreply_msg_idX=Xprevious_message.id
XXXXXXXXifXprevious_message.media:
XXXXXXXXXXXXdownloaded_file_nameX=XawaitXqrcode.client.download_media(
XXXXXXXXXXXXXXXXprevious_message,Xprogress_callback=progress
XXXXXXXXXXXX)
XXXXXXXXXXXXm_listX=XNone
XXXXXXXXXXXXwithXopen(downloaded_file_name,X"rb")XasXfile:
XXXXXXXXXXXXXXXXm_listX=Xfile.readlines()
XXXXXXXXXXXXmessageX=X""
XXXXXXXXXXXXforXmediaXinXm_list:
XXXXXXXXXXXXXXXXmessageX+=Xmedia.decode("UTF-8")X+X"\r\n"
XXXXXXXXXXXXos.remove(downloaded_file_name)
XXXXXXXXelse:
XXXXXXXXXXXXmessageX=Xprevious_message.message

XXXXurlX=X"https://api.qrserver.com/v1/create-qr-code/?data={}&\
size=200x200&charset-source=UTF-8&charset-target=UTF-8\
&ecc=L&color=0-0-0&bgcolor=255-255-255\
&margin=1&qzone=0&format=jpg"

XXXXrespX=Xget(url.format(message),Xstream=True)
XXXXrequired_file_nameX=X"temp_qr.webp"
XXXXwithXopen(required_file_name,X"w+b")XasXfile:
XXXXXXXXforXchunkXinXresp.iter_content(chunk_size=128):
XXXXXXXXXXXXfile.write(chunk)
XXXXawaitXqrcode.client.send_file(
XXXXXXXXqrcode.chat_id,
XXXXXXXXrequired_file_name,
XXXXXXXXreply_to=reply_msg_id,
XXXXXXXXprogress_callback=progress,
XXXX)
XXXXos.remove(required_file_name)
XXXXdurationX=X(datetime.now()X-Xstart).seconds
XXXXawaitXqrcode.reply("CreatedXQRCodeXinX{}Xseconds".format(duration))
XXXXawaitXsleep(5)
