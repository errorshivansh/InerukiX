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
fromXdatetimeXimportXdatetime

fromXPILXimportXImage
fromXtelegraphXimportXTelegraph,Xexceptions,Xupload_file
fromXtelethonXimportXevents

fromXInerukiX.services.telethonXimportXtbotXasXborg

telegraphX=XTelegraph()
rX=Xtelegraph.create_account(short_name="InerukiX")
auth_urlX=Xr["auth_url"]

#XWillXchangeXlater
TMP_DOWNLOAD_DIRECTORYX=X"./"

BOTLOGX=XFalse


@borg.on(events.NewMessage(pattern="/telegraphX(media|text)X?(.*)"))
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXoptional_titleX=Xevent.pattern_match.group(2)
XXXXifXevent.reply_to_msg_id:
XXXXXXXXstartX=Xdatetime.now()
XXXXXXXXr_messageX=XawaitXevent.get_reply_message()
XXXXXXXXinput_strX=Xevent.pattern_match.group(1)
XXXXXXXXifXinput_strX==X"media":
XXXXXXXXXXXXdownloaded_file_nameX=XawaitXborg.download_media(
XXXXXXXXXXXXXXXXr_message,XTMP_DOWNLOAD_DIRECTORY
XXXXXXXXXXXX)
XXXXXXXXXXXXendX=Xdatetime.now()
XXXXXXXXXXXXmsX=X(endX-Xstart).seconds
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"DownloadedXtoX{}XinX{}Xseconds.".format(downloaded_file_name,Xms)
XXXXXXXXXXXX)
XXXXXXXXXXXXifXdownloaded_file_name.endswith((".webp")):
XXXXXXXXXXXXXXXXresize_image(downloaded_file_name)
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXstartX=Xdatetime.now()
XXXXXXXXXXXXXXXXmedia_urlsX=Xupload_file(downloaded_file_name)
XXXXXXXXXXXXexceptXexceptions.TelegraphExceptionXasXexc:
XXXXXXXXXXXXXXXXawaitXevent.edit("ERROR:X"X+Xstr(exc))
XXXXXXXXXXXXXXXXos.remove(downloaded_file_name)
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXendX=Xdatetime.now()
XXXXXXXXXXXXXXXXms_twoX=X(endX-Xstart).seconds
XXXXXXXXXXXXXXXXos.remove(downloaded_file_name)
XXXXXXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXXXXXX"UploadedXtoXhttps://telegra.ph{}XinX{}Xseconds.".format(
XXXXXXXXXXXXXXXXXXXXXXXXmedia_urls[0],X(msX+Xms_two)
XXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXlink_preview=True,
XXXXXXXXXXXXXXXX)
XXXXXXXXelifXinput_strX==X"text":
XXXXXXXXXXXXuser_objectX=XawaitXborg.get_entity(r_message.sender_id)
XXXXXXXXXXXXtitle_of_pageX=Xuser_object.first_nameXX#X+X"X"X+Xuser_object.last_name
XXXXXXXXXXXX#Xapparently,XallXUsersXdoXnotXhaveXlast_nameXfield
XXXXXXXXXXXXifXoptional_title:
XXXXXXXXXXXXXXXXtitle_of_pageX=Xoptional_title
XXXXXXXXXXXXpage_contentX=Xr_message.message
XXXXXXXXXXXXifXr_message.media:
XXXXXXXXXXXXXXXXifXpage_contentX!=X"":
XXXXXXXXXXXXXXXXXXXXtitle_of_pageX=Xpage_content
XXXXXXXXXXXXXXXXdownloaded_file_nameX=XawaitXborg.download_media(
XXXXXXXXXXXXXXXXXXXXr_message,XTMP_DOWNLOAD_DIRECTORY
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXm_listX=XNone
XXXXXXXXXXXXXXXXwithXopen(downloaded_file_name,X"rb")XasXfd:
XXXXXXXXXXXXXXXXXXXXm_listX=Xfd.readlines()
XXXXXXXXXXXXXXXXforXmXinXm_list:
XXXXXXXXXXXXXXXXXXXXpage_contentX+=Xm.decode("UTF-8")X+X"\n"
XXXXXXXXXXXXXXXXos.remove(downloaded_file_name)
XXXXXXXXXXXXpage_contentX=Xpage_content.replace("\n",X"<br>")
XXXXXXXXXXXXresponseX=Xtelegraph.create_page(title_of_page,Xhtml_content=page_content)
XXXXXXXXXXXXendX=Xdatetime.now()
XXXXXXXXXXXXmsX=X(endX-Xstart).seconds
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"PastedXtoXhttps://telegra.ph/{}XinX{}Xseconds.".format(
XXXXXXXXXXXXXXXXXXXXresponse["path"],Xms
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXlink_preview=True,
XXXXXXXXXXXX)
XXXXelse:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXmessageXtoXgetXaXpermanentXtelegra.phXlink.X")


defXresize_image(image):
XXXXimX=XImage.open(image)
XXXXim.save(image,X"PNG")


__mod_name__X=X"""
<b>XTelegraphXtext/videoXuploadXpluginX</b>
X-X/telegraphXmediaX<i>replyXtoXimageXorXvideo<i>X:XUploadXimageXandXvideoXdirectlyXtoXtelegraph.
X-X/telegraphXtextX<i>replyXtoXtext</i>X:XuploadXtextXdirectlyXtoXtelegraphX.
"""

__mod_name__X=X"Telegraph"
