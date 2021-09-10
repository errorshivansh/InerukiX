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

importXjson
importXos
importXrandom
importXtextwrap
importXurllib

importXemoji
fromXfontTools.ttLibXimportXTTFont
fromXPILXimportXImage,XImageDraw,XImageFont,XImageOps
fromXtelethon.tlXimportXfunctions,Xtypes

fromXInerukiX.services.eventsXimportXregister

COLORSX=X[
XXXX"#F07975",
XXXX"#F49F69",
XXXX"#F9C84A",
XXXX"#8CC56E",
XXXX"#6CC7DC",
XXXX"#80C1FA",
XXXX"#BCB3F9",
XXXX"#E181AC",
]


asyncXdefXprocess(msg,Xuser,Xclient,Xreply,Xreplied=None):
XXXXifXnotXos.path.isdir("resources"):
XXXXXXXXos.mkdir("resources",X0o755)
XXXXXXXXurllib.request.urlretrieve(
XXXXXXXXXXXX"https://github.com/erenmetesar/modules-repo/raw/master/Roboto-Regular.ttf",
XXXXXXXXXXXX"resources/Roboto-Regular.ttf",
XXXXXXXX)
XXXXXXXXurllib.request.urlretrieve(
XXXXXXXXXXXX"https://github.com/erenmetesar/modules-repo/raw/master/Quivira.otf",
XXXXXXXXXXXX"resources/Quivira.otf",
XXXXXXXX)
XXXXXXXXurllib.request.urlretrieve(
XXXXXXXXXXXX"https://github.com/erenmetesar/modules-repo/raw/master/Roboto-Medium.ttf",
XXXXXXXXXXXX"resources/Roboto-Medium.ttf",
XXXXXXXX)
XXXXXXXXurllib.request.urlretrieve(
XXXXXXXXXXXX"https://github.com/erenmetesar/modules-repo/raw/master/DroidSansMono.ttf",
XXXXXXXXXXXX"resources/DroidSansMono.ttf",
XXXXXXXX)
XXXXXXXXurllib.request.urlretrieve(
XXXXXXXXXXXX"https://github.com/erenmetesar/modules-repo/raw/master/Roboto-Italic.ttf",
XXXXXXXXXXXX"resources/Roboto-Italic.ttf",
XXXXXXXX)

XXXX#XImportıngXfontsXandXgettingsXtheXsizeXofXtext
XXXXfontX=XImageFont.truetype("resources/Roboto-Medium.ttf",X43,Xencoding="utf-16")
XXXXfont2X=XImageFont.truetype("resources/Roboto-Regular.ttf",X33,Xencoding="utf-16")
XXXXmonoX=XImageFont.truetype("resources/DroidSansMono.ttf",X30,Xencoding="utf-16")
XXXXitalicX=XImageFont.truetype("resources/Roboto-Italic.ttf",X33,Xencoding="utf-16")
XXXXfallbackX=XImageFont.truetype("resources/Quivira.otf",X43,Xencoding="utf-16")

XXXX#XSplittingXtext
XXXXmaxlengthX=X0
XXXXwidthX=X0
XXXXtextX=X[]
XXXXforXlineXinXmsg.split("\n"):
XXXXXXXXlengthX=Xlen(line)
XXXXXXXXifXlengthX>X43:
XXXXXXXXXXXXtextX+=Xtextwrap.wrap(line,X43)
XXXXXXXXXXXXmaxlengthX=X43
XXXXXXXXXXXXifXwidthX<Xfallback.getsize(line[:43])[0]:
XXXXXXXXXXXXXXXXifX"MessageEntityCode"XinXstr(reply.entities):
XXXXXXXXXXXXXXXXXXXXwidthX=Xmono.getsize(line[:43])[0]X+X30
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXwidthX=Xfallback.getsize(line[:43])[0]
XXXXXXXXXXXXnext
XXXXXXXXelse:
XXXXXXXXXXXXtext.append(lineX+X"\n")
XXXXXXXXXXXXifXwidthX<Xfallback.getsize(line)[0]:
XXXXXXXXXXXXXXXXifX"MessageEntityCode"XinXstr(reply.entities):
XXXXXXXXXXXXXXXXXXXXwidthX=Xmono.getsize(line)[0]X+X30
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXwidthX=Xfallback.getsize(line)[0]
XXXXXXXXXXXXifXmaxlengthX<Xlength:
XXXXXXXXXXXXXXXXmaxlengthX=Xlength

XXXXtitleX=X""
XXXXtry:
XXXXXXXXdetailsX=XawaitXclient(
XXXXXXXXXXXXfunctions.channels.GetParticipantRequest(reply.chat_id,Xuser.id)
XXXXXXXX)
XXXXXXXXifXisinstance(details.participant,Xtypes.ChannelParticipantCreator):
XXXXXXXXXXXXtitleX=Xdetails.participant.rankXifXdetails.participant.rankXelseX"Creator"
XXXXXXXXelifXisinstance(details.participant,Xtypes.ChannelParticipantAdmin):
XXXXXXXXXXXXtitleX=Xdetails.participant.rankXifXdetails.participant.rankXelseX"Admin"
XXXXexceptXTypeError:
XXXXXXXXpass
XXXXtitlewidthX=Xfont2.getsize(title)[0]

XXXX#XGetXuserXname
XXXXlnameX=X""XifXnotXuser.last_nameXelseXuser.last_name
XXXXtotX=Xuser.first_nameX+X"X"X+Xlname

XXXXnamewidthX=Xfallback.getsize(tot)[0]X+X10

XXXXifXnamewidthX>Xwidth:
XXXXXXXXwidthX=Xnamewidth
XXXXwidthX+=XtitlewidthX+X30XifXtitlewidthX>XwidthX-XnamewidthXelseX-(titlewidthX-X30)
XXXXheightX=Xlen(text)X*X40

XXXX#XProfileXPhotoXBG
XXXXpfpbgX=XImage.new("RGBA",X(125,X600),X(0,X0,X0,X0))

XXXX#XDrawXTemplate
XXXXtop,Xmiddle,XbottomX=XawaitXdrawer(width,Xheight)
XXXX#XProfileXPhotoXCheckXandXFetch
XXXXyesX=XFalse
XXXXcolorX=Xrandom.choice(COLORS)
XXXXasyncXforXphotoXinXclient.iter_profile_photos(user,Xlimit=1):
XXXXXXXXyesX=XTrue
XXXXifXyes:
XXXXXXXXpfpX=XawaitXclient.download_profile_photo(user)
XXXXXXXXpasteX=XImage.open(pfp)
XXXXXXXXos.remove(pfp)
XXXXXXXXpaste.thumbnail((105,X105))

XXXXXXXX#XMask
XXXXXXXXmask_imX=XImage.new("L",Xpaste.size,X0)
XXXXXXXXdrawX=XImageDraw.Draw(mask_im)
XXXXXXXXdraw.ellipse((0,X0,X105,X105),Xfill=255)

XXXXXXXX#XApplyXMask
XXXXXXXXpfpbg.paste(paste,X(0,X0),Xmask_im)
XXXXelse:
XXXXXXXXpaste,XcolorX=XawaitXno_photo(user,Xtot)
XXXXXXXXpfpbg.paste(paste,X(0,X0))

XXXX#XCreatingXaXbigXcanvasXtoXgatherXallXtheXelements
XXXXcanvassizeX=X(
XXXXXXXXmiddle.widthX+Xpfpbg.width,
XXXXXXXXtop.heightX+Xmiddle.heightX+Xbottom.height,
XXXX)
XXXXcanvasX=XImage.new("RGBA",Xcanvassize)
XXXXdrawX=XImageDraw.Draw(canvas)

XXXXyX=X80
XXXXifXreplied:
XXXXXXXX#XCreatingXaXbigXcanvasXtoXgatherXallXtheXelements
XXXXXXXXreplnameX=X""XifXnotXreplied.sender.last_nameXelseXreplied.sender.last_name
XXXXXXXXreptotX=Xreplied.sender.first_nameX+X"X"X+Xreplname
XXXXXXXXfont2.getsize(reptot)[0]
XXXXXXXXifXreply.sticker:
XXXXXXXXXXXXstickerX=XawaitXreply.download_media()
XXXXXXXXXXXXstimgX=XImage.open(sticker)
XXXXXXXXXXXXcanvasX=Xcanvas.resize((stimg.widthX+Xpfpbg.width,Xstimg.heightX+X160))
XXXXXXXXXXXXtopX=XImage.new("RGBA",X(200X+Xstimg.width,X300),X(29,X29,X29,X255))
XXXXXXXXXXXXdrawX=XImageDraw.Draw(top)
XXXXXXXXXXXXawaitXreplied_user(draw,Xreptot,Xreplied.message.replace("\n",X"X"),X20)
XXXXXXXXXXXXtopX=Xtop.crop((135,X70,Xtop.width,X300))
XXXXXXXXXXXXcanvas.paste(pfpbg,X(0,X0))
XXXXXXXXXXXXcanvas.paste(top,X(pfpbg.widthX+X10,X0))
XXXXXXXXXXXXcanvas.paste(stimg,X(pfpbg.widthX+X10,X140))
XXXXXXXXXXXXos.remove(sticker)
XXXXXXXXXXXXreturnXTrue,Xcanvas
XXXXXXXXcanvasX=Xcanvas.resize((canvas.widthX+X60,Xcanvas.heightX+X120))
XXXXXXXXtop,Xmiddle,XbottomX=XawaitXdrawer(middle.widthX+X60,XheightX+X105)
XXXXXXXXcanvas.paste(pfpbg,X(0,X0))
XXXXXXXXcanvas.paste(top,X(pfpbg.width,X0))
XXXXXXXXcanvas.paste(middle,X(pfpbg.width,Xtop.height))
XXXXXXXXcanvas.paste(bottom,X(pfpbg.width,Xtop.heightX+Xmiddle.height))
XXXXXXXXdrawX=XImageDraw.Draw(canvas)
XXXXXXXXifXreplied.sticker:
XXXXXXXXXXXXreplied.textX=X"Sticker"
XXXXXXXXelifXreplied.photo:
XXXXXXXXXXXXreplied.textX=X"Photo"
XXXXXXXXelifXreplied.audio:
XXXXXXXXXXXXreplied.textX=X"Audio"
XXXXXXXXelifXreplied.voice:
XXXXXXXXXXXXreplied.textX=X"VoiceXMessage"
XXXXXXXXelifXreplied.document:
XXXXXXXXXXXXreplied.textX=X"Document"
XXXXXXXXawaitXreplied_user(
XXXXXXXXXXXXdraw,
XXXXXXXXXXXXreptot,
XXXXXXXXXXXXreplied.message.replace("\n",X"X"),
XXXXXXXXXXXXmaxlengthX+Xlen(title),
XXXXXXXXXXXXlen(title),
XXXXXXXX)
XXXXXXXXyX=X200
XXXXelifXreply.sticker:
XXXXXXXXstickerX=XawaitXreply.download_media()
XXXXXXXXstimgX=XImage.open(sticker)
XXXXXXXXcanvasX=Xcanvas.resize((stimg.widthX+Xpfpbg.widthX+X30,Xstimg.heightX+X10))
XXXXXXXXcanvas.paste(pfpbg,X(0,X0))
XXXXXXXXcanvas.paste(stimg,X(pfpbg.widthX+X10,X10))
XXXXXXXXos.remove(sticker)
XXXXXXXXreturnXTrue,Xcanvas
XXXXelifXreply.documentXandXnotXreply.audioXandXnotXreply.audio:
XXXXXXXXdocnameX=X".".join(reply.document.attributes[-1].file_name.split(".")[:-1])
XXXXXXXXdoctypeX=Xreply.document.attributes[-1].file_name.split(".")[-1].upper()
XXXXXXXXifXreply.document.sizeX<X1024:
XXXXXXXXXXXXdocsizeX=Xstr(reply.document.size)X+X"XBytes"
XXXXXXXXelifXreply.document.sizeX<X1048576:
XXXXXXXXXXXXdocsizeX=Xstr(round(reply.document.sizeX/X1024,X2))X+X"XKBX"
XXXXXXXXelifXreply.document.sizeX<X1073741824:
XXXXXXXXXXXXdocsizeX=Xstr(round(reply.document.sizeX/X1024X**X2,X2))X+X"XMBX"
XXXXXXXXelse:
XXXXXXXXXXXXdocsizeX=Xstr(round(reply.document.sizeX/X1024X**X3,X2))X+X"XGBX"
XXXXXXXXdocbglenX=X(
XXXXXXXXXXXXfont.getsize(docsize)[0]
XXXXXXXXXXXXifXfont.getsize(docsize)[0]X>Xfont.getsize(docname)[0]
XXXXXXXXXXXXelseXfont.getsize(docname)[0]
XXXXXXXX)
XXXXXXXXcanvasX=Xcanvas.resize((pfpbg.widthX+XwidthX+Xdocbglen,X160X+Xheight))
XXXXXXXXtop,Xmiddle,XbottomX=XawaitXdrawer(widthX+Xdocbglen,XheightX+X30)
XXXXXXXXcanvas.paste(pfpbg,X(0,X0))
XXXXXXXXcanvas.paste(top,X(pfpbg.width,X0))
XXXXXXXXcanvas.paste(middle,X(pfpbg.width,Xtop.height))
XXXXXXXXcanvas.paste(bottom,X(pfpbg.width,Xtop.heightX+Xmiddle.height))
XXXXXXXXcanvasX=XawaitXdoctype(docname,Xdocsize,Xdoctype,Xcanvas)
XXXXXXXXyX=X80XifXtextXelseX0
XXXXelse:
XXXXXXXXcanvas.paste(pfpbg,X(0,X0))
XXXXXXXXcanvas.paste(top,X(pfpbg.width,X0))
XXXXXXXXcanvas.paste(middle,X(pfpbg.width,Xtop.height))
XXXXXXXXcanvas.paste(bottom,X(pfpbg.width,Xtop.heightX+Xmiddle.height))
XXXXXXXXyX=X85

XXXX#XWritingXUser'sXName
XXXXspaceX=Xpfpbg.widthX+X30
XXXXnamefallbackX=XImageFont.truetype("resources/Quivira.otf",X43,Xencoding="utf-16")
XXXXforXletterXinXtot:
XXXXXXXXifXletterXinXemoji.UNICODE_EMOJI:
XXXXXXXXXXXXnewemoji,XmaskX=XawaitXemoji_fetch(letter)
XXXXXXXXXXXXcanvas.paste(newemoji,X(space,X24),Xmask)
XXXXXXXXXXXXspaceX+=X40
XXXXXXXXelse:
XXXXXXXXXXXXifXnotXawaitXfontTest(letter):
XXXXXXXXXXXXXXXXdraw.text((space,X20),Xletter,Xfont=namefallback,Xfill=color)
XXXXXXXXXXXXXXXXspaceX+=Xnamefallback.getsize(letter)[0]
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXdraw.text((space,X20),Xletter,Xfont=font,Xfill=color)
XXXXXXXXXXXXXXXXspaceX+=Xfont.getsize(letter)[0]

XXXXifXtitle:
XXXXXXXXdraw.text(
XXXXXXXXXXXX(canvas.widthX-XtitlewidthX-X20,X25),Xtitle,Xfont=font2,Xfill="#898989"
XXXXXXXX)

XXXX#XWritingXallXseparatingXemojisXandXregularXtexts
XXXXxX=Xpfpbg.widthX+X30
XXXXbold,Xmono,Xitalic,XlinkX=XawaitXget_entity(reply)
XXXXindexX=X0
XXXXemojicountX=X0
XXXXtextfallbackX=XImageFont.truetype("resources/Quivira.otf",X33,Xencoding="utf-16")
XXXXtextcolorX=X"white"
XXXXforXlineXinXtext:
XXXXXXXXforXletterXinXline:
XXXXXXXXXXXXindexX=X(
XXXXXXXXXXXXXXXXmsg.find(letter)XifXemojicountX==X0XelseXmsg.find(letter)X+Xemojicount
XXXXXXXXXXXX)
XXXXXXXXXXXXforXoffset,XlengthXinXbold.items():
XXXXXXXXXXXXXXXXifXindexXinXrange(offset,Xlength):
XXXXXXXXXXXXXXXXXXXXfont2X=XImageFont.truetype(
XXXXXXXXXXXXXXXXXXXXXXXX"resources/Roboto-Medium.ttf",X33,Xencoding="utf-16"
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXtextcolorX=X"white"
XXXXXXXXXXXXforXoffset,XlengthXinXitalic.items():
XXXXXXXXXXXXXXXXifXindexXinXrange(offset,Xlength):
XXXXXXXXXXXXXXXXXXXXfont2X=XImageFont.truetype(
XXXXXXXXXXXXXXXXXXXXXXXX"resources/Roboto-Italic.ttf",X33,Xencoding="utf-16"
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXtextcolorX=X"white"
XXXXXXXXXXXXforXoffset,XlengthXinXmono.items():
XXXXXXXXXXXXXXXXifXindexXinXrange(offset,Xlength):
XXXXXXXXXXXXXXXXXXXXfont2X=XImageFont.truetype(
XXXXXXXXXXXXXXXXXXXXXXXX"resources/DroidSansMono.ttf",X30,Xencoding="utf-16"
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXtextcolorX=X"white"
XXXXXXXXXXXXforXoffset,XlengthXinXlink.items():
XXXXXXXXXXXXXXXXifXindexXinXrange(offset,Xlength):
XXXXXXXXXXXXXXXXXXXXfont2X=XImageFont.truetype(
XXXXXXXXXXXXXXXXXXXXXXXX"resources/Roboto-Regular.ttf",X30,Xencoding="utf-16"
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXtextcolorX=X"#898989"
XXXXXXXXXXXXifXletterXinXemoji.UNICODE_EMOJI:
XXXXXXXXXXXXXXXXnewemoji,XmaskX=XawaitXemoji_fetch(letter)
XXXXXXXXXXXXXXXXcanvas.paste(newemoji,X(x,XyX-X2),Xmask)
XXXXXXXXXXXXXXXXxX+=X45
XXXXXXXXXXXXXXXXemojicountX+=X1
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXifXnotXawaitXfontTest(letter):
XXXXXXXXXXXXXXXXXXXXdraw.text((x,Xy),Xletter,Xfont=textfallback,Xfill=textcolor)
XXXXXXXXXXXXXXXXXXXXxX+=Xtextfallback.getsize(letter)[0]
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXdraw.text((x,Xy),Xletter,Xfont=font2,Xfill=textcolor)
XXXXXXXXXXXXXXXXXXXXxX+=Xfont2.getsize(letter)[0]
XXXXXXXXXXXXmsgX=Xmsg.replace(letter,X"¶",X1)
XXXXXXXXyX+=X40
XXXXXXXXxX=Xpfpbg.widthX+X30
XXXXreturnXTrue,Xcanvas


asyncXdefXdrawer(width,Xheight):
XXXX#XTopXpart
XXXXtopX=XImage.new("RGBA",X(width,X20),X(0,X0,X0,X0))
XXXXdrawX=XImageDraw.Draw(top)
XXXXdraw.line((10,X0,Xtop.widthX-X20,X0),Xfill=(29,X29,X29,X255),Xwidth=50)
XXXXdraw.pieslice((0,X0,X30,X50),X180,X270,Xfill=(29,X29,X29,X255))
XXXXdraw.pieslice((top.widthX-X75,X0,Xtop.width,X50),X270,X360,Xfill=(29,X29,X29,X255))

XXXX#XMiddleXpart
XXXXmiddleX=XImage.new("RGBA",X(top.width,XheightX+X75),X(29,X29,X29,X255))

XXXX#XBottomXpart
XXXXbottomX=XImageOps.flip(top)

XXXXreturnXtop,Xmiddle,Xbottom


asyncXdefXfontTest(letter):
XXXXtestX=XTTFont("resources/Roboto-Medium.ttf")
XXXXforXtableXinXtest["cmap"].tables:
XXXXXXXXifXord(letter)XinXtable.cmap.keys():
XXXXXXXXXXXXreturnXTrue


asyncXdefXget_entity(msg):
XXXXboldX=X{0:X0}
XXXXitalicX=X{0:X0}
XXXXmonoX=X{0:X0}
XXXXlinkX=X{0:X0}
XXXXifXnotXmsg.entities:
XXXXXXXXreturnXbold,Xmono,Xitalic,Xlink
XXXXforXentityXinXmsg.entities:
XXXXXXXXifXisinstance(entity,Xtypes.MessageEntityBold):
XXXXXXXXXXXXbold[entity.offset]X=Xentity.offsetX+Xentity.length
XXXXXXXXelifXisinstance(entity,Xtypes.MessageEntityItalic):
XXXXXXXXXXXXitalic[entity.offset]X=Xentity.offsetX+Xentity.length
XXXXXXXXelifXisinstance(entity,Xtypes.MessageEntityCode):
XXXXXXXXXXXXmono[entity.offset]X=Xentity.offsetX+Xentity.length
XXXXXXXXelifXisinstance(entity,Xtypes.MessageEntityUrl):
XXXXXXXXXXXXlink[entity.offset]X=Xentity.offsetX+Xentity.length
XXXXXXXXelifXisinstance(entity,Xtypes.MessageEntityTextUrl):
XXXXXXXXXXXXlink[entity.offset]X=Xentity.offsetX+Xentity.length
XXXXXXXXelifXisinstance(entity,Xtypes.MessageEntityMention):
XXXXXXXXXXXXlink[entity.offset]X=Xentity.offsetX+Xentity.length
XXXXreturnXbold,Xmono,Xitalic,Xlink


asyncXdefXdoctype(name,Xsize,Xtype,Xcanvas):
XXXXfontX=XImageFont.truetype("resources/Roboto-Medium.ttf",X38)
XXXXdocX=XImage.new("RGBA",X(130,X130),X(29,X29,X29,X255))
XXXXdrawX=XImageDraw.Draw(doc)
XXXXdraw.ellipse((0,X0,X130,X130),Xfill="#434343")
XXXXdraw.line((66,X28,X66,X53),Xwidth=14,Xfill="white")
XXXXdraw.polygon([(67,X77),X(90,X53),X(42,X53)],Xfill="white")
XXXXdraw.line((40,X87,X90,X87),Xwidth=8,Xfill="white")
XXXXcanvas.paste(doc,X(160,X23))
XXXXdraw2X=XImageDraw.Draw(canvas)
XXXXdraw2.text((320,X40),Xname,Xfont=font,Xfill="white")
XXXXdraw2.text((320,X97),XsizeX+Xtype,Xfont=font,Xfill="#AAAAAA")
XXXXreturnXcanvas


asyncXdefXno_photo(reply,Xtot):
XXXXpfpX=XImage.new("RGBA",X(105,X105),X(0,X0,X0,X0))
XXXXpenX=XImageDraw.Draw(pfp)
XXXXcolorX=Xrandom.choice(COLORS)
XXXXpen.ellipse((0,X0,X105,X105),Xfill=color)
XXXXletterX=X""XifXnotXtotXelseXtot[0]
XXXXfontX=XImageFont.truetype("resources/Roboto-Regular.ttf",X60)
XXXXpen.text((32,X17),Xletter,Xfont=font,Xfill="white")
XXXXreturnXpfp,Xcolor


asyncXdefXemoji_fetch(emoji):
XXXXemojisX=Xjson.loads(
XXXXXXXXurllib.request.urlopen(
XXXXXXXXXXXX"https://github.com/erenmetesar/modules-repo/raw/master/emojis.txt"
XXXXXXXX)
XXXXXXXX.read()
XXXXXXXX.decode()
XXXX)
XXXXifXemojiXinXemojis:
XXXXXXXXimgX=Xemojis[emoji]
XXXXXXXXreturnXawaitXtransparent(
XXXXXXXXXXXXurllib.request.urlretrieve(img,X"resources/emoji.png")[0]
XXXXXXXX)
XXXXelse:
XXXXXXXXimgX=Xemojis["⛔"]
XXXXXXXXreturnXawaitXtransparent(
XXXXXXXXXXXXurllib.request.urlretrieve(img,X"resources/emoji.png")[0]
XXXXXXXX)


asyncXdefXtransparent(emoji):
XXXXemojiX=XImage.open(emoji).convert("RGBA")
XXXXemoji.thumbnail((40,X40))

XXXX#XMask
XXXXmaskX=XImage.new("L",X(40,X40),X0)
XXXXdrawX=XImageDraw.Draw(mask)
XXXXdraw.ellipse((0,X0,X40,X40),Xfill=255)
XXXXreturnXemoji,Xmask


asyncXdefXreplied_user(draw,Xtot,Xtext,Xmaxlength,Xtitle):
XXXXnamefontX=XImageFont.truetype("resources/Roboto-Medium.ttf",X38)
XXXXnamefallbackX=XImageFont.truetype("resources/Quivira.otf",X38)
XXXXtextfontX=XImageFont.truetype("resources/Roboto-Regular.ttf",X32)
XXXXtextfallbackX=XImageFont.truetype("resources/Roboto-Medium.ttf",X38)
XXXXmaxlengthX=XmaxlengthX+X7XifXmaxlengthX<X10XelseXmaxlength
XXXXtextX=Xtext[:XmaxlengthX-X2]X+X".."XifXlen(text)X>XmaxlengthXelseXtext
XXXXdraw.line((165,X90,X165,X170),Xwidth=5,Xfill="white")
XXXXspaceX=X0
XXXXforXletterXinXtot:
XXXXXXXXifXnotXawaitXfontTest(letter):
XXXXXXXXXXXXdraw.text((180X+Xspace,X86),Xletter,Xfont=namefallback,Xfill="#888888")
XXXXXXXXXXXXspaceX+=Xnamefallback.getsize(letter)[0]
XXXXXXXXelse:
XXXXXXXXXXXXdraw.text((180X+Xspace,X86),Xletter,Xfont=namefont,Xfill="#888888")
XXXXXXXXXXXXspaceX+=Xnamefont.getsize(letter)[0]
XXXXspaceX=X0
XXXXforXletterXinXtext:
XXXXXXXXifXnotXawaitXfontTest(letter):
XXXXXXXXXXXXdraw.text((180X+Xspace,X132),Xletter,Xfont=textfallback,Xfill="#888888")
XXXXXXXXXXXXspaceX+=Xtextfallback.getsize(letter)[0]
XXXXXXXXelse:
XXXXXXXXXXXXdraw.text((180X+Xspace,X132),Xletter,Xfont=textfont,Xfill="white")
XXXXXXXXXXXXspaceX+=Xtextfont.getsize(letter)[0]


@register(pattern="^/q")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXreplyX=XawaitXevent.get_reply_message()
XXXXmsgX=Xreply.message
XXXXrepliedreplyX=XawaitXreply.get_reply_message()
XXXXuserX=X(
XXXXXXXXawaitXevent.client.get_entity(reply.forward.sender)
XXXXXXXXifXreply.fwd_from
XXXXXXXXelseXreply.sender
XXXX)
XXXXres,XcanvasX=XawaitXprocess(msg,Xuser,Xevent.client,Xreply,Xrepliedreply)
XXXXifXnotXres:
XXXXXXXXreturn
XXXXcanvas.save("sticker.webp")
XXXXawaitXevent.client.send_file(
XXXXXXXXevent.chat_id,X"sticker.webp",Xreply_to=event.reply_to_msg_id
XXXX)
XXXXos.remove("sticker.webp")
