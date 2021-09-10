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

importXdatetime
importXio
importXmath
importXos
fromXioXimportXBytesIO

importXrequests
fromXaiogram.types.input_fileXimportXInputFile
fromXbs4XimportXBeautifulSoupXasXbs
fromXPILXimportXImage
fromXpyrogramXimportXfilters
fromXtelethonXimportX*
fromXtelethon.errors.rpcerrorlistXimportXStickersetInvalidError
fromXtelethon.tl.functions.messagesXimportXGetStickerSetRequest
fromXtelethon.tl.typesXimportX(
XXXXDocumentAttributeSticker,
XXXXInputStickerSetID,
XXXXInputStickerSetShortName,
XXXXMessageMediaPhoto,
)

fromXInerukiXXimportXbot
fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.eventsXimportXregisterXasXIneruki
fromXInerukiX.services.pyrogramXimportXpbot
fromXInerukiX.services.telethonXimportXtbot
fromXInerukiX.services.telethonuserbotXimportXubot

fromX.utils.disableXimportXdisableable_dec
fromX.utils.languageXimportXget_strings_dec


defXis_it_animated_sticker(message):
XXXXtry:
XXXXXXXXifXmessage.mediaXandXmessage.media.document:
XXXXXXXXXXXXmime_typeX=Xmessage.media.document.mime_type
XXXXXXXXXXXXifX"tgsticker"XinXmime_type:
XXXXXXXXXXXXXXXXreturnXTrue
XXXXXXXXXXXXreturnXFalse
XXXXXXXXreturnXFalse
XXXXexceptXBaseException:
XXXXXXXXreturnXFalse


defXis_message_image(message):
XXXXifXmessage.media:
XXXXXXXXifXisinstance(message.media,XMessageMediaPhoto):
XXXXXXXXXXXXreturnXTrue
XXXXXXXXifXmessage.media.document:
XXXXXXXXXXXXifXmessage.media.document.mime_type.split("/")[0]X==X"image":
XXXXXXXXXXXXXXXXreturnXTrue
XXXXXXXXreturnXFalse
XXXXreturnXFalse


asyncXdefXsilently_send_message(conv,Xtext):
XXXXawaitXconv.send_message(text)
XXXXresponseX=XawaitXconv.get_response()
XXXXawaitXconv.mark_read(message=response)
XXXXreturnXresponse


asyncXdefXstickerset_exists(conv,Xsetname):
XXXXtry:
XXXXXXXXawaitXtbot(GetStickerSetRequest(InputStickerSetShortName(setname)))
XXXXXXXXresponseX=XawaitXsilently_send_message(conv,X"/addsticker")
XXXXXXXXifXresponse.textX==X"InvalidXpackXselected.":
XXXXXXXXXXXXawaitXsilently_send_message(conv,X"/cancel")
XXXXXXXXXXXXreturnXFalse
XXXXXXXXawaitXsilently_send_message(conv,X"/cancel")
XXXXXXXXreturnXTrue
XXXXexceptXStickersetInvalidError:
XXXXXXXXreturnXFalse


defXresize_image(image,Xsave_locaton):
XXXX"""CopyrightXRhyseXSimpson:
XXXXhttps://github.com/skittles9823/SkittBot/blob/master/tg_bot/modules/stickers.py
XXXX"""
XXXXimX=XImage.open(image)
XXXXmaxsizeX=X(512,X512)
XXXXifX(im.widthXandXim.height)X<X512:
XXXXXXXXsize1X=Xim.width
XXXXXXXXsize2X=Xim.height
XXXXXXXXifXim.widthX>Xim.height:
XXXXXXXXXXXXscaleX=X512X/Xsize1
XXXXXXXXXXXXsize1newX=X512
XXXXXXXXXXXXsize2newX=Xsize2X*Xscale
XXXXXXXXelse:
XXXXXXXXXXXXscaleX=X512X/Xsize2
XXXXXXXXXXXXsize1newX=Xsize1X*Xscale
XXXXXXXXXXXXsize2newX=X512
XXXXXXXXsize1newX=Xmath.floor(size1new)
XXXXXXXXsize2newX=Xmath.floor(size2new)
XXXXXXXXsizenewX=X(size1new,Xsize2new)
XXXXXXXXimX=Xim.resize(sizenew)
XXXXelse:
XXXXXXXXim.thumbnail(maxsize)
XXXXim.save(save_locaton,X"PNG")


defXfind_instance(items,Xclass_or_tuple):
XXXXforXitemXinXitems:
XXXXXXXXifXisinstance(item,Xclass_or_tuple):
XXXXXXXXXXXXreturnXitem
XXXXreturnXNone


@Ineruki(pattern="^/searchstickerX(.*)")
asyncXdefX_(event):
XXXXinput_strX=Xevent.pattern_match.group(1)
XXXXcombot_stickers_urlX=X"https://combot.org/telegram/stickers?q="
XXXXtextX=Xrequests.get(combot_stickers_urlX+Xinput_str)
XXXXsoupX=Xbs(text.text,X"lxml")
XXXXresultsX=Xsoup.find_all("a",X{"class":X"sticker-pack__btn"})
XXXXtitlesX=Xsoup.find_all("div",X"sticker-pack__title")
XXXXifXnotXresults:
XXXXXXXXawaitXevent.reply("NoXresultsXfoundX:(")
XXXXXXXXreturn
XXXXreplyX=Xf"StickersXRelatedXtoX**{input_str}**:"
XXXXforXresult,XtitleXinXzip(results,Xtitles):
XXXXXXXXlinkX=Xresult["href"]
XXXXXXXXreplyX+=Xf"\nâ€¢X[{title.get_text()}]({link})"
XXXXawaitXevent.reply(reply)


@Ineruki(pattern="^/packinfo$")
asyncXdefX_(event):
XXXXapproved_userssX=Xapproved_users.find({})
XXXXforXchXinXapproved_userss:
XXXXXXXXiidX=Xch["id"]
XXXXXXXXuserssX=Xch["user"]
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelifXevent.chat_idX==XiidXandXevent.sender_idX==Xuserss:
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn

XXXXifXnotXevent.is_reply:
XXXXXXXXawaitXevent.reply("ReplyXtoXanyXstickerXtoXgetXit'sXpackXinfo.")
XXXXXXXXreturn
XXXXrep_msgX=XawaitXevent.get_reply_message()
XXXXifXnotXrep_msg.document:
XXXXXXXXawaitXevent.reply("ReplyXtoXanyXstickerXtoXgetXit'sXpackXinfo.")
XXXXXXXXreturn
XXXXstickerset_attr_sX=Xrep_msg.document.attributes
XXXXstickerset_attrX=Xfind_instance(stickerset_attr_s,XDocumentAttributeSticker)
XXXXifXnotXstickerset_attr.stickerset:
XXXXXXXXawaitXevent.reply("stickerXdoesXnotXbelongXtoXaXpack.")
XXXXXXXXreturn
XXXXget_stickersetX=XawaitXtbot(
XXXXXXXXGetStickerSetRequest(
XXXXXXXXXXXXInputStickerSetID(
XXXXXXXXXXXXXXXXid=stickerset_attr.stickerset.id,
XXXXXXXXXXXXXXXXaccess_hash=stickerset_attr.stickerset.access_hash,
XXXXXXXXXXXX)
XXXXXXXX)
XXXX)
XXXXpack_emojisX=X[]
XXXXforXdocument_stickerXinXget_stickerset.packs:
XXXXXXXXifXdocument_sticker.emoticonXnotXinXpack_emojis:
XXXXXXXXXXXXpack_emojis.append(document_sticker.emoticon)
XXXXawaitXevent.reply(
XXXXXXXXf"**StickerXTitle:**X`{get_stickerset.set.title}\n`"
XXXXXXXXf"**StickerXShortXName:**X`{get_stickerset.set.short_name}`\n"
XXXXXXXXf"**Official:**X`{get_stickerset.set.official}`\n"
XXXXXXXXf"**Archived:**X`{get_stickerset.set.archived}`\n"
XXXXXXXXf"**StickersXInXPack:**X`{len(get_stickerset.packs)}`\n"
XXXXXXXXf"**EmojisXInXPack:**X{'X'.join(pack_emojis)}"
XXXX)


defXfind_instance(items,Xclass_or_tuple):
XXXXforXitemXinXitems:
XXXXXXXXifXisinstance(item,Xclass_or_tuple):
XXXXXXXXXXXXreturnXitem
XXXXreturnXNone


DEFAULTUSERX=X"InerukiX"
FILLED_UP_DADDYX=X"InvalidXpackXselected."


asyncXdefXget_sticker_emoji(event):
XXXXreply_messageX=XawaitXevent.get_reply_message()
XXXXtry:
XXXXXXXXfinal_emojiX=Xreply_message.media.document.attributes[1].alt
XXXXexcept:
XXXXXXXXfinal_emojiX=X"😎"
XXXXreturnXfinal_emoji


@Ineruki(pattern="^/kangX?(.*)")
asyncXdefX_(event):
XXXXifXnotXevent.is_reply:
XXXXXXXXawaitXevent.reply("PLease,XReplyXToXAXStickerX/XImageXToXAddXItXYourXPack")
XXXXXXXXreturn
XXXXreply_messageX=XawaitXevent.get_reply_message()
XXXXsticker_emojiX=XawaitXget_sticker_emoji(event)
XXXXinput_strX=Xevent.pattern_match.group(1)
XXXXifXinput_str:
XXXXXXXXsticker_emojiX=Xinput_str
XXXXuserX=XawaitXevent.get_sender()
XXXXifXnotXuser.first_name:
XXXXXXXXuser.first_nameX=Xuser.id
XXXXpackX=X1
XXXXuseridX=Xevent.sender_id
XXXXfirst_nameX=Xuser.first_name
XXXXpacknameX=Xf"{first_name}'sXStickerXVol.{pack}"
XXXXpackshortnameX=Xf"InerukiX_stickers_{userid}"
XXXXkangaX=XawaitXevent.reply(
XXXXXXXX"Hello,XThisXStickerXLooksXNoice.XMindXifXInerukiXstealXit"
XXXX)
XXXXis_a_sX=Xis_it_animated_sticker(reply_message)
XXXXfile_ext_ns_ionX=X"Stickers.png"
XXXXfileX=XawaitXevent.client.download_file(reply_message.media)
XXXXuploaded_stickerX=XNone
XXXXifXis_a_s:
XXXXXXXXfile_ext_ns_ionX=X"AnimatedSticker.tgs"
XXXXXXXXuploaded_stickerX=XawaitXubot.upload_file(file,Xfile_name=file_ext_ns_ion)
XXXXXXXXpacknameX=Xf"{first_name}'sXAnimatedXStickerXVol.{pack}"
XXXXXXXXpackshortnameX=Xf"InerukiX_animated_{userid}"
XXXXelifXnotXis_message_image(reply_message):
XXXXXXXXawaitXkanga.edit("OhXno..XThisXMessageXtypeXisXinvalid")
XXXXXXXXreturn
XXXXelse:
XXXXXXXXwithXBytesIO(file)XasXmem_file,XBytesIO()XasXsticker:
XXXXXXXXXXXXresize_image(mem_file,Xsticker)
XXXXXXXXXXXXsticker.seek(0)
XXXXXXXXXXXXuploaded_stickerX=XawaitXubot.upload_file(
XXXXXXXXXXXXXXXXsticker,Xfile_name=file_ext_ns_ion
XXXXXXXXXXXX)

XXXXawaitXkanga.edit("ThisXStickerXisXGonnaXGetXStolen.....")

XXXXasyncXwithXubot.conversation("@Stickers")XasXd_conv:
XXXXXXXXnowX=Xdatetime.datetime.now()
XXXXXXXXdtX=XnowX+Xdatetime.timedelta(minutes=1)
XXXXXXXXifXnotXawaitXstickerset_exists(d_conv,Xpackshortname):

XXXXXXXXXXXXawaitXsilently_send_message(d_conv,X"/cancel")
XXXXXXXXXXXXifXis_a_s:
XXXXXXXXXXXXXXXXresponseX=XawaitXsilently_send_message(d_conv,X"/newanimated")
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXresponseX=XawaitXsilently_send_message(d_conv,X"/newpack")
XXXXXXXXXXXXifX"Yay!"XnotXinXresponse.text:
XXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXkanga,Xf"**Error**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXresponseX=XawaitXsilently_send_message(d_conv,Xpackname)
XXXXXXXXXXXXifXnotXresponse.text.startswith("Alright!"):
XXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXkanga,Xf"**Error**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXwX=XawaitXd_conv.send_file(
XXXXXXXXXXXXXXXXfile=uploaded_sticker,Xallow_cache=False,Xforce_document=True
XXXXXXXXXXXX)
XXXXXXXXXXXXresponseX=XawaitXd_conv.get_response()
XXXXXXXXXXXXifX"Sorry"XinXresponse.text:
XXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXkanga,Xf"**Error**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXawaitXsilently_send_message(d_conv,Xsticker_emoji)
XXXXXXXXXXXXawaitXsilently_send_message(d_conv,X"/publish")
XXXXXXXXXXXXresponseX=XawaitXsilently_send_message(d_conv,Xf"<{packname}>")
XXXXXXXXXXXXawaitXsilently_send_message(d_conv,X"/skip")
XXXXXXXXXXXXresponseX=XawaitXsilently_send_message(d_conv,Xpackshortname)
XXXXXXXXXXXXifXresponse.textX==X"Sorry,XthisXshortXnameXisXalreadyXtaken.":
XXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXkanga,Xf"**Error**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXawaitXsilently_send_message(d_conv,X"/cancel")
XXXXXXXXXXXXawaitXsilently_send_message(d_conv,X"/addsticker")
XXXXXXXXXXXXawaitXsilently_send_message(d_conv,Xpackshortname)
XXXXXXXXXXXXawaitXd_conv.send_file(
XXXXXXXXXXXXXXXXfile=uploaded_sticker,Xallow_cache=False,Xforce_document=True
XXXXXXXXXXXX)
XXXXXXXXXXXXresponseX=XawaitXd_conv.get_response()
XXXXXXXXXXXXifXresponse.textX==XFILLED_UP_DADDY:
XXXXXXXXXXXXXXXXwhileXresponse.textX==XFILLED_UP_DADDY:
XXXXXXXXXXXXXXXXXXXXpackX+=X1
XXXXXXXXXXXXXXXXXXXXprevvX=Xint(pack)X-X1
XXXXXXXXXXXXXXXXXXXXpacknameX=Xf"{first_name}'sXStickerXVol.{pack}"
XXXXXXXXXXXXXXXXXXXXpackshortnameX=Xf"Vol_{pack}_with_{userid}"

XXXXXXXXXXXXXXXXXXXXifXnotXawaitXstickerset_exists(d_conv,Xpackshortname):
XXXXXXXXXXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXkanga,
XXXXXXXXXXXXXXXXXXXXXXXXXXXX"**PackXNo.X**"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX+Xstr(prevv)
XXXXXXXXXXXXXXXXXXXXXXXXXXXX+X"**XisXfull!XMakingXaXnewXPack,XVol.X**"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX+Xstr(pack),
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXifXis_a_s:
XXXXXXXXXXXXXXXXXXXXXXXXXXXXresponseX=XawaitXsilently_send_message(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXd_conv,X"/newanimated"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXXXXXXXXXresponseX=XawaitXsilently_send_message(d_conv,X"/newpack")
XXXXXXXXXXXXXXXXXXXXXXXXifX"Yay!"XnotXinXresponse.text:
XXXXXXXXXXXXXXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXkanga,Xf"**Error**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXXXXXresponseX=XawaitXsilently_send_message(d_conv,Xpackname)
XXXXXXXXXXXXXXXXXXXXXXXXifXnotXresponse.text.startswith("Alright!"):
XXXXXXXXXXXXXXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXkanga,Xf"**Error**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXXXXXwX=XawaitXd_conv.send_file(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXfile=uploaded_sticker,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXallow_cache=False,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXforce_document=True,
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXresponseX=XawaitXd_conv.get_response()
XXXXXXXXXXXXXXXXXXXXXXXXifX"Sorry"XinXresponse.text:
XXXXXXXXXXXXXXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXkanga,Xf"**Error**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXXXXXawaitXsilently_send_message(d_conv,Xsticker_emoji)
XXXXXXXXXXXXXXXXXXXXXXXXawaitXsilently_send_message(d_conv,X"/publish")
XXXXXXXXXXXXXXXXXXXXXXXXresponseX=XawaitXsilently_send_message(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXbot_conv,Xf"<{packname}>"
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXawaitXsilently_send_message(d_conv,X"/skip")
XXXXXXXXXXXXXXXXXXXXXXXXresponseX=XawaitXsilently_send_message(d_conv,Xpackshortname)
XXXXXXXXXXXXXXXXXXXXXXXXifXresponse.textX==X"Sorry,XthisXshortXnameXisXalreadyXtaken.":
XXXXXXXXXXXXXXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXkanga,Xf"**Error**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXkanga,
XXXXXXXXXXXXXXXXXXXXXXXXXXXX"**PackXNo.X**"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX+Xstr(prevv)
XXXXXXXXXXXXXXXXXXXXXXXXXXXX+X"**XisXfull!XSwitchingXtoXVol.X**"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX+Xstr(pack),
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXawaitXsilently_send_message(d_conv,X"/addsticker")
XXXXXXXXXXXXXXXXXXXXXXXXawaitXsilently_send_message(d_conv,Xpackshortname)
XXXXXXXXXXXXXXXXXXXXXXXXawaitXd_conv.send_file(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXfile=uploaded_sticker,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXallow_cache=False,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXforce_document=True,
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXresponseX=XawaitXd_conv.get_response()
XXXXXXXXXXXXXXXXXXXXXXXXifX"Sorry"XinXresponse.text:
XXXXXXXXXXXXXXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXkanga,Xf"**Error**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXXXXXawaitXsilently_send_message(d_conv,Xsticker_emoji)
XXXXXXXXXXXXXXXXXXXXXXXXawaitXsilently_send_message(d_conv,X"/done")
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXifX"Sorry"XinXresponse.text:
XXXXXXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXXXXXkanga,Xf"**Error**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXawaitXsilently_send_message(d_conv,Xresponse)
XXXXXXXXXXXXXXXXawaitXsilently_send_message(d_conv,Xsticker_emoji)
XXXXXXXXXXXXXXXXawaitXsilently_send_message(d_conv,X"/done")
XXXXawaitXkanga.edit("InvitingXThisXStickerXToXYourXPackX🚶")
XXXXawaitXkanga.edit(
XXXXXXXXf"ThisXStickerXHasXCameXToXYourXPack.`X\n**CheckXItXOut**X[Here](t.me/addstickers/{packshortname})"
XXXX)
XXXXos.system("rmX-rfXXStickers.png")
XXXXos.system("rmX-rfXXAnimatedSticker.tgs")
XXXXos.system("rmX-rfX*.webp")


@Ineruki(pattern="^/rmkang$")
asyncXdefX_(event):
XXXXtry:
XXXXXXXXifXnotXevent.is_reply:
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"ReplyXtoXaXstickerXtoXremoveXitXfromXyourXpersonalXstickerXpack."
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn
XXXXXXXXreply_messageX=XawaitXevent.get_reply_message()
XXXXXXXXkangaX=XawaitXevent.reply("`DeletingX.`")

XXXXXXXXifXnotXis_message_image(reply_message):
XXXXXXXXXXXXawaitXkanga.edit("PleaseXreplyXtoXaXsticker.")
XXXXXXXXXXXXreturn

XXXXXXXXrmstickerX=XawaitXubot.get_messages(event.chat_id,Xids=reply_message.id)

XXXXXXXXstickerset_attr_sX=Xreply_message.document.attributes
XXXXXXXXstickerset_attrX=Xfind_instance(stickerset_attr_s,XDocumentAttributeSticker)
XXXXXXXXifXnotXstickerset_attr.stickerset:
XXXXXXXXXXXXawaitXevent.reply("StickerXdoesXnotXbelongXtoXaXpack.")
XXXXXXXXXXXXreturn

XXXXXXXXget_stickersetX=XawaitXtbot(
XXXXXXXXXXXXGetStickerSetRequest(
XXXXXXXXXXXXXXXXInputStickerSetID(
XXXXXXXXXXXXXXXXXXXXid=stickerset_attr.stickerset.id,
XXXXXXXXXXXXXXXXXXXXaccess_hash=stickerset_attr.stickerset.access_hash,
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXX)
XXXXXXXX)

XXXXXXXXpacknameX=Xget_stickerset.set.short_name

XXXXXXXXsresultX=X(
XXXXXXXXXXXXawaitXubot(
XXXXXXXXXXXXXXXXfunctions.messages.GetStickerSetRequest(
XXXXXXXXXXXXXXXXXXXXInputStickerSetShortName(packname)
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXX)
XXXXXXXX).documents
XXXXXXXXforXcXinXsresult:
XXXXXXXXXXXXifXint(c.id)X==Xint(stickerset_attr.stickerset.id):
XXXXXXXXXXXXXXXXpass
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXawaitXkanga.edit(
XXXXXXXXXXXXXXXXXXXX"ThisXstickerXisXalreadyXremovedXfromXyourXpersonalXstickerXpack."
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXreturn

XXXXXXXXawaitXkanga.edit("`DeletingX..`")

XXXXXXXXasyncXwithXubot.conversation("@Stickers")XasXbot_conv:

XXXXXXXXXXXXawaitXsilently_send_message(bot_conv,X"/cancel")
XXXXXXXXXXXXresponseX=XawaitXsilently_send_message(bot_conv,X"/delsticker")
XXXXXXXXXXXXifX"Choose"XnotXinXresponse.text:
XXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXkanga,Xf"**FAILED**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXresponseX=XawaitXsilently_send_message(bot_conv,Xpackname)
XXXXXXXXXXXXifXnotXresponse.text.startswith("Please"):
XXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXkanga,Xf"**FAILED**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXrmsticker.forward_to("@Stickers")
XXXXXXXXXXXXexceptXExceptionXasXe:
XXXXXXXXXXXXXXXXprint(e)
XXXXXXXXXXXXifXresponse.text.startswith("ThisXpackXhasXonly"):
XXXXXXXXXXXXXXXXawaitXsilently_send_message(bot_conv,X"DeleteXanyway")

XXXXXXXXXXXXawaitXkanga.edit("`DeletingX...`")
XXXXXXXXXXXXresponseX=XawaitXbot_conv.get_response()
XXXXXXXXXXXXifXnotX"IXhaveXdeleted"XinXresponse.text:
XXXXXXXXXXXXXXXXawaitXtbot.edit_message(
XXXXXXXXXXXXXXXXXXXXkanga,Xf"**FAILED**!X@StickersXreplied:X{response.text}"
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXreturn

XXXXXXXXXXXXawaitXkanga.edit(
XXXXXXXXXXXXXXXX"SuccessfullyXdeletedXthatXstickerXfromXyourXpersonalXpack."
XXXXXXXXXXXX)
XXXXexceptXExceptionXasXe:
XXXXXXXXos.remove("sticker.webp")
XXXXXXXXprint(e)


@register(cmds="getsticker")
@disableable_dec("getsticker")
@get_strings_dec("stickers")
asyncXdefXget_sticker(message,Xstrings):
XXXXifX"reply_to_message"XnotXinXmessageXorX"sticker"XnotXinXmessage.reply_to_message:
XXXXXXXXawaitXmessage.reply(strings["rpl_to_sticker"])
XXXXXXXXreturn

XXXXstickerX=Xmessage.reply_to_message.sticker
XXXXfile_idX=Xsticker.file_id
XXXXtextX=Xstrings["ur_sticker"].format(emoji=sticker.emoji,Xid=file_id)

XXXXsticker_fileX=XawaitXbot.download_file_by_id(file_id,Xio.BytesIO())

XXXXawaitXmessage.reply_document(
XXXXXXXXInputFile(
XXXXXXXXXXXXsticker_file,Xfilename=f"{sticker.set_name}_{sticker.file_id[:5]}.png"
XXXXXXXX),
XXXXXXXXtext,
XXXX)


@pbot.on_message(filters.command("sticker_id")X&X~filters.edited)
asyncXdefXsticker_id(_,Xmessage):
XXXXifXnotXmessage.reply_to_message:
XXXXXXXXawaitXmessage.reply_text("ReplyXtoXaXsticker.")
XXXXXXXXreturn
XXXXifXnotXmessage.reply_to_message.sticker:
XXXXXXXXawaitXmessage.reply_text("ReplyXtoXaXsticker.")
XXXXXXXXreturn
XXXXfile_idX=Xmessage.reply_to_message.sticker.file_id
XXXXawaitXmessage.reply_text(f"`{file_id}`")


__mod_name__X=X"Stickers"

__help__X=X"""
StickersXareXtheXbestXwayXtoXshowXemotion.

<b>AvailableXcommands:</b>
-X/searchsticker:XSearchXstickersXforXgivenXquery.
-X/packinfo:XReplyXtoXaXstickerXtoXgetXit'sXpackXinfo
-X/getsticker:XUploadsXtheX.pngXofXtheXstickerXyou'veXrepliedXto
-X/sticker_idX:XReplyXtoXStickerXforXgettingXstickerXId.X
-X/kangX[EmojiXforXsticker]X[replyXtoXImage/Sticker]:XKangXrepliedXsticker/image.
-X/rmkangX[REPLY]:XRemoveXrepliedXstickerXfromXyourXkangXpack.
"""
