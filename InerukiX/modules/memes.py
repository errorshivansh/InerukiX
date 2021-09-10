#XThisXfileXisXcopiedXfromX@Missjuliarobot
#XFullXcreditsXtoXoriginalXauthor

importXasyncio
importXio
importXjson
importXos
importXrandom
importXre
importXstring
importXsubprocess
importXtextwrap
importXurllib.request
fromXrandomXimportXrandint,Xrandrange,Xuniform

importXemoji
importXnltk
fromXcowpyXimportXcow
fromXfontTools.ttLibXimportXTTFont
fromXPILXimportXImage,XImageDraw,XImageEnhance,XImageFont,XImageOps
fromXseleniumXimportXwebdriver
fromXselenium.webdriver.chrome.optionsXimportXOptions
fromXtelethonXimportX*
fromXtelethon.tlXimportXfunctions
fromXtelethon.tl.typesXimportX*
fromXzalgo_textXimportXzalgo

fromXInerukiXXimportX*
fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbot
fromXInerukiX.services.telethonuserbotXimportXubot

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

WIDE_MAPX=X{i:XiX+X0xFEE0XforXiXinXrange(0x21,X0x7F)}
WIDE_MAP[0x20]X=X0x3000


@register(pattern="^/owu$")
asyncXdefXmsg(event):

XXXXreply_texX=XawaitXevent.get_reply_message()
XXXXreply_textX=Xreply_tex.text
XXXXifXreply_textXisXNone:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXmessageXtoXmakeXmeme.")
XXXXXXXXreturn
XXXXfacesX=X[
XXXXXXXX"(・`ω´・)",
XXXXXXXX";;w;;",
XXXXXXXX"owo",
XXXXXXXX"UwU",
XXXXXXXX">w<",
XXXXXXXX"^w^",
XXXXXXXXr"\(^o\)X(/o^)/",
XXXXXXXX"(X^X_X^)∠☆",
XXXXXXXX"(ô_ô)",
XXXXXXXX"~:o",
XXXXXXXX";____;",
XXXXXXXX"(*^*)",
XXXXXXXX"(>_",
XXXXXXXX"(♥_♥)",
XXXXXXXX"*(^O^)*",
XXXXXXXX"((+_+))",
XXXX]
XXXXtextX=Xre.sub(r"[rl]",X"w",Xreply_text)
XXXXtextX=Xre.sub(r"[ｒｌ]",X"ｗ",Xreply_text)
XXXXtextX=Xre.sub(r"[RL]",X"W",Xtext)
XXXXtextX=Xre.sub(r"[ＲＬ]",X"Ｗ",Xtext)
XXXXtextX=Xre.sub(r"n([aeiouａｅｉｏｕ])",Xr"ny\1",Xtext)
XXXXtextX=Xre.sub(r"ｎ([ａｅｉｏｕ])",Xr"ｎｙ\1",Xtext)
XXXXtextX=Xre.sub(r"N([aeiouAEIOU])",Xr"Ny\1",Xtext)
XXXXtextX=Xre.sub(r"Ｎ([ａｅｉｏｕＡＥＩＯＵ])",Xr"Ｎｙ\1",Xtext)
XXXXtextX=Xre.sub(r"\!+",X"X"X+Xrandom.choice(faces),Xtext)
XXXXtextX=Xre.sub(r"！+",X"X"X+Xrandom.choice(faces),Xtext)
XXXXtextX=Xtext.replace("ove",X"uv")
XXXXtextX=Xtext.replace("ｏｖｅ",X"ｕｖ")
XXXXtextX+=X"X"X+Xrandom.choice(faces)
XXXXawaitXevent.reply(text)


@register(pattern="^/copypasta$")
asyncXdefXmsg(event):

XXXXrtexX=XawaitXevent.get_reply_message()
XXXXrtextX=Xrtex.text
XXXXifXrtextXisXNone:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXmessageXttoXmakeXmeme.")
XXXXXXXXreturn
XXXXemojisX=X[
XXXXXXXX"😂",
XXXXXXXX"😂",
XXXXXXXX"👌",
XXXXXXXX"✌",
XXXXXXXX"💞",
XXXXXXXX"👍",
XXXXXXXX"👌",
XXXXXXXX"💯",
XXXXXXXX"🎶",
XXXXXXXX"👀",
XXXXXXXX"😂",
XXXXXXXX"👓",
XXXXXXXX"👏",
XXXXXXXX"👐",
XXXXXXXX"🍕",
XXXXXXXX"💥",
XXXXXXXX"🍴",
XXXXXXXX"💦",
XXXXXXXX"💦",
XXXXXXXX"🍑",
XXXXXXXX"🍆",
XXXXXXXX"😩",
XXXXXXXX"😏",
XXXXXXXX"👉👌",
XXXXXXXX"👀",
XXXXXXXX"👅",
XXXXXXXX"😩",
XXXXXXXX"🚰",
XXXX]
XXXXreply_textX=Xrandom.choice(emojis)
XXXXb_charX=Xrandom.choice(rtext).lower()
XXXXforXcXinXrtext:
XXXXXXXXifXcX==X"X":
XXXXXXXXXXXXreply_textX+=Xrandom.choice(emojis)
XXXXXXXXelifXcXinXemojis:
XXXXXXXXXXXXreply_textX+=Xc
XXXXXXXXXXXXreply_textX+=Xrandom.choice(emojis)
XXXXXXXXelifXc.lower()X==Xb_char:
XXXXXXXXXXXXreply_textX+=X"🅱️"
XXXXXXXXelse:
XXXXXXXXXXXXifXbool(random.getrandbits(1)):
XXXXXXXXXXXXXXXXreply_textX+=Xc.upper()
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXreply_textX+=Xc.lower()
XXXXreply_textX+=Xrandom.choice(emojis)
XXXXawaitXevent.reply(reply_text)


@register(pattern="^/bmoji$")
asyncXdefXmsg(event):

XXXXrtexX=XawaitXevent.get_reply_message()
XXXXrtextX=Xrtex.text
XXXXifXrtextXisXNone:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXmessageXtoXmakeXmeme.")
XXXXXXXXreturn
XXXXb_charX=Xrandom.choice(rtext).lower()
XXXXreply_textX=Xrtext.replace(b_char,X"🅱️").replace(b_char.upper(),X"🅱️")
XXXXawaitXevent.reply(reply_text)


@register(pattern="^/clapmoji$")
asyncXdefXmsg(event):

XXXXrtexX=XawaitXevent.get_reply_message()
XXXXrtextX=Xrtex.text
XXXXifXrtextXisXNone:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXmessageXtoXmakeXmeme.")
XXXXXXXXreturn
XXXXreply_textX=X"👏X"
XXXXreply_textX+=Xrtext.replace("X",X"X👏X")
XXXXreply_textX+=X"X👏"
XXXXawaitXevent.reply(reply_text)


@register(pattern="^/stretch$")
asyncXdefXmsg(event):

XXXXrtexX=XawaitXevent.get_reply_message()
XXXXrtextX=Xrtex.text
XXXXifXrtextXisXNone:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXmessageXtoXmakeXmeme.")
XXXXXXXXreturn
XXXXcountX=Xrandom.randint(3,X10)
XXXXreply_textX=Xre.sub(r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵ])",X(r"\1"X*Xcount),Xrtext)
XXXXawaitXevent.reply(reply_text)


@register(pattern="^/vapor(?:X|$)(.*)")
asyncXdefXmsg(event):

XXXXrtexX=XawaitXevent.get_reply_message()
XXXXrtextX=Xrtex.text
XXXXifXrtext:
XXXXXXXXdataX=Xrtext
XXXXelse:
XXXXXXXXdataX=Xevent.pattern_match.group(1)
XXXXifXdataXisXNone:
XXXXXXXXawaitXevent.reply("EitherXprovideXsomeXinputXorXreplyXtoXaXmessage.")
XXXXXXXXreturn

XXXXreply_textX=Xstr(data).translate(WIDE_MAP)
XXXXawaitXevent.reply(reply_text)


@register(pattern="^/zalgofy$")
asyncXdefXmsg(event):

XXXXrtexX=XawaitXevent.get_reply_message()
XXXXrtextX=Xrtex.text
XXXXifXrtextXisXNone:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXmessageXtoXmakeXmeme.")
XXXXXXXXreturn
XXXXreply_textX=Xzalgo.zalgo().zalgofy(rtext)
XXXXawaitXevent.reply(reply_text)


@register(pattern="^/forbesify$")
asyncXdefXmsg(event):

XXXXrtexX=XawaitXevent.get_reply_message()
XXXXrtextX=Xrtex.text
XXXXifXrtextXisXNone:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXmessageXtoXmakeXmeme.")
XXXXXXXXreturn
XXXXdataX=Xrtext

XXXXdataX=Xdata.lower()
XXXXaccidentalsX=X["VB",X"VBD",X"VBG",X"VBN"]
XXXXreply_textX=Xdata.split()
XXXXoffsetX=X0

XXXXtaggedX=Xdict(nltk.pos_tag(reply_text))

XXXXforXkXinXrange(len(reply_text)):
XXXXXXXXiX=Xreply_text[kX+Xoffset]
XXXXXXXXifXtagged.get(i)XinXaccidentals:
XXXXXXXXXXXXreply_text.insert(kX+Xoffset,X"accidentally")
XXXXXXXXXXXXoffsetX+=X1

XXXXreply_textX=Xstring.capwords("X".join(reply_text))
XXXXawaitXevent.reply(reply_text)


@register(pattern="^/shoutX(.*)")
asyncXdefXmsg(event):

XXXXrtextX=Xevent.pattern_match.group(1)

XXXXargsX=Xrtext

XXXXifXlen(args)X==X0:
XXXXXXXXawaitXevent.reply("WhereXisXtext?")
XXXXXXXXreturn

XXXXmsgX=X"```"
XXXXtextX=X"X".join(args)
XXXXresultX=X[]
XXXXresult.append("X".join(list(text)))
XXXXforXpos,XsymbolXinXenumerate(text[1:]):
XXXXXXXXresult.append(symbolX+X"X"X+X"XX"X*XposX+Xsymbol)
XXXXresultX=Xlist("\n".join(result))
XXXXresult[0]X=Xtext[0]
XXXXresultX=X"".join(result)
XXXXmsgX=X"```\n"X+XresultX+X"```"
XXXXawaitXevent.reply(msg)


@register(pattern="^/angrymoji$")
asyncXdefXmsg(event):

XXXXrtexX=XawaitXevent.get_reply_message()
XXXXrtextX=Xrtex.text
XXXXifXrtextXisXNone:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXmessageXtoXmakeXmeme.")
XXXXXXXXreturn
XXXXreply_textX=X"😡X"
XXXXforXiXinXrtext:
XXXXXXXXifXiX==X"X":
XXXXXXXXXXXXreply_textX+=X"X😡X"
XXXXXXXXelse:
XXXXXXXXXXXXreply_textX+=Xi
XXXXreply_textX+=X"X😡"
XXXXawaitXevent.reply(reply_text)


@register(pattern="^/crymoji$")
asyncXdefXmsg(event):

XXXXrtexX=XawaitXevent.get_reply_message()
XXXXrtextX=Xrtex.text
XXXXifXrtextXisXNone:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXmessageXtoXmakeXmeme.")
XXXXXXXXreturn
XXXXreply_textX=X"😭X"
XXXXforXiXinXrtext:
XXXXXXXXifXiX==X"X":
XXXXXXXXXXXXreply_textX+=X"X😭X"
XXXXXXXXelse:
XXXXXXXXXXXXreply_textX+=Xi
XXXXreply_textX+=X"X😭"
XXXXawaitXevent.reply(reply_text)


CARBONLANGX=X"en"


@register(pattern="^/carbonX(.*)")
asyncXdefXcarbon_api(e):

XXXXjjX=X"`Processing..`"
XXXXggX=XawaitXe.reply(jj)
XXXXCARBONX=X"https://carbon.now.sh/?bg=rgba(239%2C40%2C44%2C1)&t=one-light&wt=none&l=application%2Ftypescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={code}"
XXXXglobalXCARBONLANG
XXXXcodeX=Xe.pattern_match.group(1)
XXXXawaitXgg.edit("`Processing..\n25%`")
XXXXos.chdir("./")
XXXXifXos.path.isfile("./carbon.png"):
XXXXXXXXos.remove("./carbon.png")
XXXXurlX=XCARBON.format(code=code,Xlang=CARBONLANG)
XXXXchrome_optionsX=XOptions()
XXXXchrome_options.add_argument("--headless")
XXXXchrome_options.binary_locationX=XGOOGLE_CHROME_BIN
XXXXchrome_options.add_argument("--window-size=1920x1080")
XXXXchrome_options.add_argument("--disable-dev-shm-usage")
XXXXchrome_options.add_argument("--no-sandbox")
XXXXchrome_options.add_argument("--disable-gpu")
XXXXprefsX=X{"download.default_directory":X"./"}
XXXXchrome_options.add_experimental_option("prefs",Xprefs)
XXXXdriverX=Xwebdriver.Chrome(executable_path=CHROME_DRIVER,Xoptions=chrome_options)
XXXXdriver.get(url)
XXXXawaitXgg.edit("`Processing..\n50%`")
XXXXdownload_pathX=X"./"
XXXXdriver.command_executor._commands["send_command"]X=X(
XXXXXXXX"POST",
XXXXXXXX"/session/$sessionId/chromium/send_command",
XXXX)
XXXXparamsX=X{
XXXXXXXX"cmd":X"Page.setDownloadBehavior",
XXXXXXXX"params":X{"behavior":X"allow",X"downloadPath":Xdownload_path},
XXXX}
XXXXdriver.execute("send_command",Xparams)
XXXXdriver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
XXXXawaitXgg.edit("`Processing..\n75%`")
XXXXwhileXnotXos.path.isfile("./carbon.png"):
XXXXXXXXawaitXasyncio.sleep(1)
XXXXawaitXgg.edit("`Processing..\n100%`")
XXXXfileX=X"./carbon.png"
XXXXawaitXe.edit("`Uploading..`")
XXXXawaitXtbot.send_file(
XXXXXXXXe.chat_id,
XXXXXXXXfile,
XXXXXXXXcaption="MadeXusingX[Carbon](https://carbon.now.sh/about/),\
XXXXXXXX\naXprojectXbyX[DawnXLabs](https://dawnlabs.io/)",
XXXXXXXXforce_document=True,
XXXX)
XXXXos.remove("./carbon.png")
XXXXdriver.quit()


@register(pattern="^/deepfry(?:X|$)(.*)")
asyncXdefXdeepfryer(event):

XXXXtry:
XXXXXXXXfrycountX=Xint(event.pattern_match.group(1))
XXXXXXXXifXfrycountX<X1:
XXXXXXXXXXXXraiseXValueError
XXXXexceptXValueError:
XXXXXXXXfrycountX=X1
XXXXifXevent.is_reply:
XXXXXXXXreply_messageX=XawaitXevent.get_reply_message()
XXXXXXXXdataX=XawaitXcheck_media(reply_message)
XXXXXXXXifXisinstance(data,Xbool):
XXXXXXXXXXXXawaitXevent.reply("`IXcan'tXdeepXfryXthat!`")
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXawaitXevent.reply("`ReplyXtoXanXimageXorXstickerXtoXdeepXfryXit!`")
XXXXXXXXreturn

XXXXimageX=Xio.BytesIO()
XXXXawaitXtbot.download_media(data,Ximage)
XXXXimageX=XImage.open(image)

XXXXforX_XinXrange(frycount):
XXXXXXXXimageX=XawaitXdeepfry(image)
XXXXfried_ioX=Xio.BytesIO()
XXXXfried_io.nameX=X"image.jpeg"
XXXXimage.save(fried_io,X"JPEG")
XXXXfried_io.seek(0)
XXXXawaitXevent.reply(file=fried_io)


asyncXdefXdeepfry(img:XImage)X->XImage:
XXXXcoloursX=X(
XXXXXXXX(randint(50,X200),Xrandint(40,X170),Xrandint(40,X190)),
XXXXXXXX(randint(190,X255),Xrandint(170,X240),Xrandint(180,X250)),
XXXX)
XXXXimgX=Ximg.copy().convert("RGB")
XXXXimgX=Ximg.convert("RGB")
XXXXwidth,XheightX=Ximg.width,Ximg.height
XXXXimgX=Ximg.resize(
XXXXXXXX(int(widthX**Xuniform(0.8,X0.9)),Xint(heightX**Xuniform(0.8,X0.9))),
XXXXXXXXresample=Image.LANCZOS,
XXXX)
XXXXimgX=Ximg.resize(
XXXXXXXX(int(widthX**Xuniform(0.85,X0.95)),Xint(heightX**Xuniform(0.85,X0.95))),
XXXXXXXXresample=Image.BILINEAR,
XXXX)
XXXXimgX=Ximg.resize(
XXXXXXXX(int(widthX**Xuniform(0.89,X0.98)),Xint(heightX**Xuniform(0.89,X0.98))),
XXXXXXXXresample=Image.BICUBIC,
XXXX)
XXXXimgX=Ximg.resize((width,Xheight),Xresample=Image.BICUBIC)
XXXXimgX=XImageOps.posterize(img,Xrandint(3,X7))
XXXXoverlayX=Ximg.split()[0]
XXXXoverlayX=XImageEnhance.Contrast(overlay).enhance(uniform(1.0,X2.0))
XXXXoverlayX=XImageEnhance.Brightness(overlay).enhance(uniform(1.0,X2.0))
XXXXoverlayX=XImageOps.colorize(overlay,Xcolours[0],Xcolours[1])
XXXXimgX=XImage.blend(img,Xoverlay,Xuniform(0.1,X0.4))
XXXXimgX=XImageEnhance.Sharpness(img).enhance(randint(5,X300))
XXXXreturnXimg


asyncXdefXcheck_media(reply_message):
XXXXifXreply_messageXandXreply_message.media:
XXXXXXXXifXreply_message.photo:
XXXXXXXXXXXXdataX=Xreply_message.photo
XXXXXXXXelifXreply_message.document:
XXXXXXXXXXXXifX(
XXXXXXXXXXXXXXXXDocumentAttributeFilename(file_name="AnimatedSticker.tgs")
XXXXXXXXXXXXXXXXinXreply_message.media.document.attributes
XXXXXXXXXXXX):
XXXXXXXXXXXXXXXXreturnXFalse
XXXXXXXXXXXXifX(
XXXXXXXXXXXXXXXXreply_message.gif
XXXXXXXXXXXXXXXXorXreply_message.video
XXXXXXXXXXXXXXXXorXreply_message.audio
XXXXXXXXXXXXXXXXorXreply_message.voice
XXXXXXXXXXXX):
XXXXXXXXXXXXXXXXreturnXFalse
XXXXXXXXXXXXdataX=Xreply_message.media.document
XXXXXXXXelse:
XXXXXXXXXXXXreturnXFalse
XXXXelse:
XXXXXXXXreturnXFalse
XXXXifXnotXdataXorXdataXisXNone:
XXXXXXXXreturnXFalse
XXXXreturnXdata


@register(pattern="^/typeX(.*)")
asyncXdefXtypewriter(typew):

XXXXmessageX=Xtypew.pattern_match.group(1)
XXXXifXmessage:
XXXXXXXXpass
XXXXelse:
XXXXXXXXawaitXtypew.reply("`GiveXaXtextXtoXtype!`")
XXXXXXXXreturn
XXXXtyping_symbolX=X"|"
XXXXold_textX=X""
XXXXnowX=XawaitXtypew.reply(typing_symbol)
XXXXawaitXasyncio.sleep(2)
XXXXforXcharacterXinXmessage:
XXXXXXXXold_textX=Xold_textX+X""X+Xcharacter
XXXXXXXXtyping_textX=Xold_textX+X""X+Xtyping_symbol
XXXXXXXXawaitXnow.edit(typing_text)
XXXXXXXXawaitXasyncio.sleep(2)
XXXXXXXXawaitXnow.edit(old_text)
XXXXXXXXawaitXasyncio.sleep(2)


@register(pattern="^/stickletX(.*)")
asyncXdefXsticklet(event):

XXXXRX=Xrandom.randint(0,X256)
XXXXGX=Xrandom.randint(0,X256)
XXXXBX=Xrandom.randint(0,X256)

XXXX#XgetXtheXinputXtext
XXXX#XtheXtextXonXwhichXweXwouldXlikeXtoXdoXtheXmagicXon
XXXXsticktextX=Xevent.pattern_match.group(1)

XXXX#XdeleteXtheXuserbotXcommand,
XXXX#XiXdon'tXknowXwhyXthisXisXrequired
XXXX#XawaitXevent.delete()

XXXX#Xhttps://docs.python.org/3/library/textwrap.html#textwrap.wrap
XXXXsticktextX=Xtextwrap.wrap(sticktext,Xwidth=10)
XXXX#XconvertsXbackXtheXlistXtoXaXstring
XXXXsticktextX=X"\n".join(sticktext)

XXXXimageX=XImage.new("RGBA",X(512,X512),X(255,X255,X255,X0))
XXXXdrawX=XImageDraw.Draw(image)
XXXXfontsizeX=X230

XXXXFONT_FILEX=XawaitXget_font_file(ubot,X"@IndianBot_Fonts")

XXXXfontX=XImageFont.truetype(FONT_FILE,Xsize=fontsize)

XXXXwhileXdraw.multiline_textsize(sticktext,Xfont=font)X>X(512,X512):
XXXXXXXXfontsizeX-=X3
XXXXXXXXfontX=XImageFont.truetype(FONT_FILE,Xsize=fontsize)

XXXXwidth,XheightX=Xdraw.multiline_textsize(sticktext,Xfont=font)
XXXXdraw.multiline_text(
XXXXXXXX((512X-Xwidth)X/X2,X(512X-Xheight)X/X2),Xsticktext,Xfont=font,Xfill=(R,XG,XB)
XXXX)

XXXXimage_streamX=Xio.BytesIO()
XXXXimage_stream.nameX=X"@Julia.webp"
XXXXimage.save(image_stream,X"WebP")
XXXXimage_stream.seek(0)

XXXX#Xfinally,XreplyXtheXsticker
XXXXawaitXevent.reply(file=image_stream,Xreply_to=event.message.reply_to_msg_id)
XXXX#XreplacingXupperXlineXwithXthisXtoXgetXreplyXtags

XXXX#Xcleanup
XXXXtry:
XXXXXXXXos.remove(FONT_FILE)
XXXXexceptXBaseException:
XXXXXXXXpass


asyncXdefXget_font_file(client,Xchannel_id):
XXXX#XfirstXgetXtheXfontXmessages
XXXXfont_file_message_sX=XawaitXclient.get_messages(
XXXXXXXXentity=channel_id,
XXXXXXXXfilter=InputMessagesFilterDocument,
XXXXXXXX#XthisXmightXcauseXFLOODXWAIT,
XXXXXXXX#XifXusedXtooXmanyXtimes
XXXXXXXXlimit=None,
XXXX)
XXXX#XgetXaXrandomXfontXfromXtheXlistXofXfonts
XXXX#Xhttps://docs.python.org/3/library/random.html#random.choice
XXXXfont_file_messageX=Xrandom.choice(font_file_message_s)
XXXX#XdownloadXandXreturnXtheXfileXpath
XXXXreturnXawaitXclient.download_media(font_file_message)


@register(pattern=r"^/(\w+)sayX(.*)")
asyncXdefXunivsaye(cowmsg):

XXXX"""ForX.cowsayXmodule,XuniborgXwrapperXforXcowXwhichXsaysXthings."""
XXXXifXnotXcowmsg.text[0].isalpha()XandXcowmsg.text[0]XnotXinX("#",X"@"):
XXXXXXXXargX=Xcowmsg.pattern_match.group(1).lower()
XXXXXXXXtextX=Xcowmsg.pattern_match.group(2)

XXXXXXXXifXargX==X"cow":
XXXXXXXXXXXXargX=X"default"
XXXXXXXXifXargXnotXinXcow.COWACTERS:
XXXXXXXXXXXXreturn
XXXXXXXXcheeseX=Xcow.get_cow(arg)
XXXXXXXXcheeseX=Xcheese()

XXXXXXXXawaitXcowmsg.reply(f"`{cheese.milk(text).replace('`',X'´')}`")


@register(pattern="^/basketball$")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn

XXXXinput_strX=Xprint(randrange(6))
XXXXrX=XawaitXevent.reply(file=InputMediaDice("🏀"))
XXXXifXinput_str:
XXXXXXXXtry:
XXXXXXXXXXXXrequired_numberX=Xint(input_str)
XXXXXXXXXXXXwhileXnotXr.media.valueX==Xrequired_number:
XXXXXXXXXXXXXXXXawaitXr.delete()
XXXXXXXXXXXXXXXXrX=XawaitXevent.reply(file=InputMediaDice("🏀"))
XXXXXXXXexceptXBaseException:
XXXXXXXXXXXXpass


@register(pattern="^/jackpot$")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn

XXXXawaitXevent.reply(file=InputMediaDice("🎰"))


@register(pattern="^/dart$")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn

XXXXinput_strX=Xprint(randrange(7))
XXXXrX=XawaitXevent.reply(file=InputMediaDice("🎯"))
XXXXifXinput_str:
XXXXXXXXtry:
XXXXXXXXXXXXrequired_numberX=Xint(input_str)
XXXXXXXXXXXXwhileXnotXr.media.valueX==Xrequired_number:
XXXXXXXXXXXXXXXXawaitXr.delete()
XXXXXXXXXXXXXXXXrX=XawaitXevent.reply(file=InputMediaDice("🎯"))
XXXXXXXXexceptXBaseException:
XXXXXXXXXXXXpass


#XOringinalXSourceXfromXNicegrill:Xhttps://github.com/erenmetesar/NiceGrill/
#XPortedXtoXLyndaXby:X@pokurt

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
XXXXimgX=Xemojis["⛔"]
XXXXreturnXawaitXtransparent(urllib.request.urlretrieve(img,X"resources/emoji.png")[0])


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


@register(pattern="^/quotly$")
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


EMOJI_PATTERNX=Xre.compile(
XXXX"["
XXXX"\U0001F1E0-\U0001F1FF"XX#XflagsX(iOS)
XXXX"\U0001F300-\U0001F5FF"XX#XsymbolsX&Xpictographs
XXXX"\U0001F600-\U0001F64F"XX#Xemoticons
XXXX"\U0001F680-\U0001F6FF"XX#XtransportX&XmapXsymbols
XXXX"\U0001F700-\U0001F77F"XX#XalchemicalXsymbols
XXXX"\U0001F780-\U0001F7FF"XX#XGeometricXShapesXExtended
XXXX"\U0001F800-\U0001F8FF"XX#XSupplementalXArrows-C
XXXX"\U0001F900-\U0001F9FF"XX#XSupplementalXSymbolsXandXPictographs
XXXX"\U0001FA00-\U0001FA6F"XX#XChessXSymbols
XXXX"\U0001FA70-\U0001FAFF"XX#XSymbolsXandXPictographsXExtended-A
XXXX"\U00002702-\U000027B0"XX#XDingbats
XXXX"]+"
)


defXdeEmojify(inputString:Xstr)X->Xstr:
XXXX"""RemoveXemojisXandXotherXnon-safeXcharactersXfromXstring"""
XXXXreturnXre.sub(EMOJI_PATTERN,X"",XinputString)


#XMadeXByX@MissJulia_Robot


@register(pattern="^/animateX(.*)")
asyncXdefXstickerizer(event):

XXXXnewtextX=Xevent.pattern_match.group(1)
XXXXanimusX=X[20,X32,X33,X40,X41,X42,X58]
XXXXsticcersX=XawaitXubot.inline_query(
XXXXXXXX"stickerizerbot",Xf"#{random.choice(animus)}{(deEmojify(newtext))}"
XXXX)
XXXXnullX=XawaitXsticcers[0].download_media(TEMP_DOWNLOAD_DIRECTORY)
XXXXbaraX=Xstr(null)
XXXXawaitXevent.client.send_file(event.chat_id,Xbara,Xreply_to=event.id)
XXXXos.remove(bara)


@register(pattern="^/dice$")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn

XXXXinput_strX=Xprint(randrange(7))
XXXXrX=XawaitXevent.reply(file=InputMediaDice(""))
XXXXifXinput_str:
XXXXXXXXtry:
XXXXXXXXXXXXrequired_numberX=Xint(input_str)
XXXXXXXXXXXXwhileXnotXr.media.valueX==Xrequired_number:
XXXXXXXXXXXXXXXXawaitXr.delete()
XXXXXXXXXXXXXXXXrX=XawaitXevent.reply(file=InputMediaDice(""))
XXXXXXXXexceptXBaseException:
XXXXXXXXXXXXpass


@register(pattern="^/fortune$")
asyncXdefXfortunate(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn

XXXXjitX=Xsubprocess.check_output(["python",X"fortune.py"])
XXXXpitX=Xjit.decode()
XXXXawaitXevent.reply(pit)


ABUSE_STRINGSX=X(
XXXX"FuckXoff",
XXXX"StfuXgoXfuckXyourself",
XXXX"UrXmumXgey",
XXXX"UrXdadXlesbo",
XXXX"YouXAssfucker",
XXXX"Nigga",
XXXX"UrXgrannyXtranny",
XXXX"youXnoob",
XXXX"RelaxXyourXRear,dersXnothingXtoXfear,TheXRapeXtrainXisXfinallyXhere",
XXXX"StfuXbc",
XXXX"StfuXandXGtfoXUXnub",
XXXX"GTFOXbsdk",
XXXX"CUnt",
XXXX"Madharchod",
XXXX"XGayXisXhere",
XXXX"UrXdadXgeyXbcX",
)

EYESX=X[
XXXX["⌐■",X"■"],
XXXX["X͠°",X"X°"],
XXXX["⇀",X"↼"],
XXXX["´•X",X"X•`"],
XXXX["´",X"`"],
XXXX["`",X"´"],
XXXX["ó",X"ò"],
XXXX["ò",X"ó"],
XXXX["⸌",X"⸍"],
XXXX[">",X"<"],
XXXX["Ƹ̵̡",X"Ʒ"],
XXXX["ᗒ",X"ᗕ"],
XXXX["⟃",X"⟄"],
XXXX["⪧",X"⪦"],
XXXX["⪦",X"⪧"],
XXXX["⪩",X"⪨"],
XXXX["⪨",X"⪩"],
XXXX["⪰",X"⪯"],
XXXX["⫑",X"⫒"],
XXXX["⨴",X"⨵"],
XXXX["⩿",X"⪀"],
XXXX["⩾",X"⩽"],
XXXX["⩺",X"⩹"],
XXXX["⩹",X"⩺"],
XXXX["◥▶",X"◀◤"],
XXXX["◍",X"◎"],
XXXX["/͠-",X"┐͡-\\"],
XXXX["⌣",X"⌣”"],
XXXX["X͡⎚",X"X͡⎚"],
XXXX["≋"],
XXXX["૦ઁ"],
XXXX["XXͯ"],
XXXX["XX͌"],
XXXX["ළ"],
XXXX["◉"],
XXXX["☉"],
XXXX["・"],
XXXX["▰"],
XXXX["ᵔ"],
XXXX["Xﾟ"],
XXXX["□"],
XXXX["☼"],
XXXX["*"],
XXXX["`"],
XXXX["⚆"],
XXXX["⊜"],
XXXX[">"],
XXXX["❍"],
XXXX["￣"],
XXXX["─"],
XXXX["✿"],
XXXX["•"],
XXXX["T"],
XXXX["^"],
XXXX["ⱺ"],
XXXX["@"],
XXXX["ȍ"],
XXXX["XX"],
XXXX["XX"],
XXXX["x"],
XXXX["-"],
XXXX["$"],
XXXX["Ȍ"],
XXXX["ʘ"],
XXXX["Ꝋ"],
XXXX[""],
XXXX["⸟"],
XXXX["๏"],
XXXX["ⴲ"],
XXXX["◕"],
XXXX["◔"],
XXXX["✧"],
XXXX["■"],
XXXX["♥"],
XXXX["X͡°"],
XXXX["¬"],
XXXX["XºX"],
XXXX["⨶"],
XXXX["⨱"],
XXXX["⏓"],
XXXX["⏒"],
XXXX["⍜"],
XXXX["⍤"],
XXXX["ᚖ"],
XXXX["ᴗ"],
XXXX["ಠ"],
XXXX["σ"],
XXXX["☯"],
]

MOUTHSX=X[
XXXX["v"],
XXXX["ᴥ"],
XXXX["ᗝ"],
XXXX["Ѡ"],
XXXX["ᗜ"],
XXXX["Ꮂ"],
XXXX["ᨓ"],
XXXX["ᨎ"],
XXXX["ヮ"],
XXXX["╭͜ʖ╮"],
XXXX["X͟ل͜"],
XXXX["X͜ʖ"],
XXXX["X͟ʖ"],
XXXX["Xʖ̯"],
XXXX["ω"],
XXXX["X³"],
XXXX["XεX"],
XXXX["﹏"],
XXXX["□"],
XXXX["ل͜"],
XXXX["‿"],
XXXX["╭╮"],
XXXX["‿‿"],
XXXX["▾"],
XXXX["‸"],
XXXX["Д"],
XXXX["∀"],
XXXX["!"],
XXXX["人"],
XXXX["."],
XXXX["ロ"],
XXXX["_"],
XXXX["෴"],
XXXX["ѽ"],
XXXX["ഌ"],
XXXX["⏠"],
XXXX["⏏"],
XXXX["⍊"],
XXXX["⍘"],
XXXX["ツ"],
XXXX["益"],
XXXX["╭∩╮"],
XXXX["Ĺ̯"],
XXXX["◡"],
XXXX["X͜つ"],
]

EARSX=X[
XXXX["q",X"p"],
XXXX["ʢ",X"ʡ"],
XXXX["⸮",X"?"],
XXXX["ʕ",X"ʔ"],
XXXX["ᖗ",X"ᖘ"],
XXXX["ᕦ",X"ᕥ"],
XXXX["ᕦ(",X")ᕥ"],
XXXX["ᕙ(",X")ᕗ"],
XXXX["ᘳ",X"ᘰ"],
XXXX["ᕮ",X"ᕭ"],
XXXX["ᕳ",X"ᕲ"],
XXXX["(",X")"],
XXXX["[",X"]"],
XXXX["¯\\_",X"_/¯"],
XXXX["୧",X"୨"],
XXXX["୨",X"୧"],
XXXX["⤜(",X")⤏"],
XXXX["☞",X"☞"],
XXXX["ᑫ",X"ᑷ"],
XXXX["ᑴ",X"ᑷ"],
XXXX["ヽ(",X")ﾉ"],
XXXX["\\(",X")/"],
XXXX["乁(",X")ㄏ"],
XXXX["└[",X"]┘"],
XXXX["(づ",X")づ"],
XXXX["(ง",X")ง"],
XXXX["⎝",X"⎠"],
XXXX["ლ(",X"ლ)"],
XXXX["ᕕ(",X")ᕗ"],
XXXX["(∩",X")⊃━☆ﾟ.*"],
]

TOSSX=X(
XXXX"Heads",
XXXX"Tails",
)


@register(pattern="^/roll$")
asyncXdefXmsg(event):

XXXXawaitXevent.reply(str(random.choice(range(1,X7))))


@register(pattern="^/toss$")
asyncXdefXmsg(event):
XXXXawaitXevent.reply(random.choice(TOSS))


@register(pattern="^/abuse$")
asyncXdefXmsg(event):

XXXXifXevent.reply_to_msg_id:
XXXXXXXXreplyX=XawaitXevent.get_reply_message()
XXXXXXXXreplytoX=Xreply.sender_id
XXXXelse:
XXXXXXXXreplytoX=Xevent.sender_id
XXXXawaitXtbot.send_message(
XXXXXXXXevent.chat_id,Xrandom.choice(ABUSE_STRINGS),Xreply_to=replyto
XXXX)


@register(pattern="^/bluetext$")
asyncXdefXmsg(event):

XXXXifXevent.reply_to_msg_id:
XXXXXXXXreplyX=XawaitXevent.get_reply_message()
XXXXXXXXreplytoX=Xreply.sender_id
XXXXelse:
XXXXXXXXreplytoX=Xevent.sender_id
XXXXawaitXtbot.send_message(
XXXXXXXXevent.chat_id,
XXXXXXXX"/BLUEX/TEXTX/MUSTX/CLICKX/IX/AMX/AX/STUPIDX/ANIMALX/THATX/ISX/ATTRACTEDX/TOX/COLORS",
XXXXXXXXreply_to=replyto,
XXXX)


@register(pattern="^/rlg$")
asyncXdefX_(event):

XXXXeyesX=Xrandom.choice(EYES)
XXXXmouthX=Xrandom.choice(MOUTHS)
XXXXearsX=Xrandom.choice(EARS)
XXXXreplX=Xformat(earsX+XeyesX+XmouthX+XeyesX+Xears)
XXXXawaitXevent.reply(repl)


@register(pattern="^/decide$")
asyncXdefX_(event):

XXXXrX=Xrandint(1,X100)
XXXXifXrX<=X65:
XXXXXXXXawaitXevent.reply("Yes.")
XXXXelifXrX<=X90:
XXXXXXXXawaitXevent.reply("NoU.")
XXXXelse:
XXXXXXXXawaitXevent.reply("Maybe.")


@register(pattern="^/table$")
asyncXdefX_(event):

XXXXrX=Xrandint(1,X100)
XXXXifXrX<=X45:
XXXXXXXXawaitXevent.reply("(╯°□°）╯彡X┻━┻")
XXXXelifXrX<=X90:
XXXXXXXXawaitXevent.reply("SendXmoneyXtoXbuyXnewXtableXtoXflip")
XXXXelse:
XXXXXXXXawaitXevent.reply("GoXdoXsomeXworkXinsteadXofXflippingXtablesXmaXboy.")


SFW_STRINGSX=X(
XXXX"OwwwX...XSuchXaXstupidXidiot.",
XXXX"Don'tXdrinkXandXtype.",
XXXX"IXthinkXyouXshouldXgoXhomeXorXbetterXaXmentalXasylum.",
XXXX"CommandXnotXfound.XJustXlikeXyourXbrain.",
XXXX"DoXyouXrealizeXyouXareXmakingXaXfoolXofXyourself?XApparentlyXnot.",
XXXX"YouXcanXtypeXbetterXthanXthat.",
XXXX"BotXruleX544XsectionX9XpreventsXmeXfromXreplyingXtoXstupidXhumansXlikeXyou.",
XXXX"Sorry,XweXdoXnotXsellXbrains.",
XXXX"BelieveXmeXyouXareXnotXnormal.",
XXXX"IXbetXyourXbrainXfeelsXasXgoodXasXnew,XseeingXthatXyouXneverXuseXit.",
XXXX"IfXIXwantedXtoXkillXmyselfXI'dXclimbXyourXegoXandXjumpXtoXyourXIQ.",
XXXX"ZombiesXeatXbrains...Xyou'reXsafe.",
XXXX"YouXdidn'tXevolveXfromXapes,XtheyXevolvedXfromXyou.",
XXXX"ComeXbackXandXtalkXtoXmeXwhenXyourXI.Q.XexceedsXyourXage.",
XXXX"I'mXnotXsayingXyou'reXstupid,XI'mXjustXsayingXyou'veXgotXbadXluckXwhenXitXcomesXtoXthinking.",
XXXX"WhatXlanguageXareXyouXspeaking?XCauseXitXsoundsXlikeXbullshit.",
XXXX"StupidityXisXnotXaXcrimeXsoXyouXareXfreeXtoXgo.",
XXXX"YouXareXproofXthatXevolutionXCANXgoXinXreverse.",
XXXX"IXwouldXaskXyouXhowXoldXyouXareXbutXIXknowXyouXcan'tXcountXthatXhigh.",
XXXX"AsXanXoutsider,XwhatXdoXyouXthinkXofXtheXhumanXrace?",
XXXX"BrainsXaren'tXeverything.XInXyourXcaseXthey'reXnothing.",
XXXX"OrdinarilyXpeopleXliveXandXlearn.XYouXjustXlive.",
XXXX"IXdon'tXknowXwhatXmakesXyouXsoXstupid,XbutXitXreallyXworks.",
XXXX"KeepXtalking,XsomedayXyou'llXsayXsomethingXintelligent!X(IXdoubtXitXthough)",
XXXX"ShockXme,XsayXsomethingXintelligent.",
XXXX"YourXIQ'sXlowerXthanXyourXshoeXsize.",
XXXX"Alas!XYourXneurotransmittersXareXnoXmoreXworking.",
XXXX"AreXyouXcrazyXyouXfool.",
XXXX"EveryoneXhasXtheXrightXtoXbeXstupidXbutXyouXareXabusingXtheXprivilege.",
XXXX"I'mXsorryXIXhurtXyourXfeelingsXwhenXIXcalledXyouXstupid.XIXthoughtXyouXalreadyXknewXthat.",
XXXX"YouXshouldXtryXtastingXcyanide.",
XXXX"YourXenzymesXareXmeantXtoXdigestXratXpoison.",
XXXX"YouXshouldXtryXsleepingXforever.",
XXXX"PickXupXaXgunXandXshootXyourself.",
XXXX"YouXcouldXmakeXaXworldXrecordXbyXjumpingXfromXaXplaneXwithoutXparachute.",
XXXX"StopXtalkingXBSXandXjumpXinXfrontXofXaXrunningXbulletXtrain.",
XXXX"TryXbathingXwithXHydrochloricXAcidXinsteadXofXwater.",
XXXX"TryXthis:XifXyouXholdXyourXbreathXunderwaterXforXanXhour,XyouXcanXthenXholdXitXforever.",
XXXX"GoXGreen!XStopXinhalingXOxygen.",
XXXX"GodXwasXsearchingXforXyou.XYouXshouldXleaveXtoXmeetXhim.",
XXXX"giveXyourX100%.XNow,XgoXdonateXblood.",
XXXX"TryXjumpingXfromXaXhundredXstoryXbuildingXbutXyouXcanXdoXitXonlyXonce.",
XXXX"YouXshouldXdonateXyourXbrainXseeingXthatXyouXneverXusedXit.",
XXXX"VolunteerXforXtargetXinXanXfiringXrange.",
XXXX"HeadXshotsXareXfun.XGetXyourselfXone.",
XXXX"YouXshouldXtryXswimmingXwithXgreatXwhiteXsharks.",
XXXX"YouXshouldXpaintXyourselfXredXandXrunXinXaXbullXmarathon.",
XXXX"YouXcanXstayXunderwaterXforXtheXrestXofXyourXlifeXwithoutXcomingXbackXup.",
XXXX"HowXaboutXyouXstopXbreathingXforXlikeX1Xday?XThat'llXbeXgreat.",
XXXX"TryXprovokingXaXtigerXwhileXyouXbothXareXinXaXcage.",
XXXX"HaveXyouXtriedXshootingXyourselfXasXhighXasX100mXusingXaXcanon.",
XXXX"YouXshouldXtryXholdingXTNTXinXyourXmouthXandXignitingXit.",
XXXX"TryXplayingXcatchXandXthrowXwithXRDXXitsXfun.",
XXXX"IXheardXphogineXisXpoisonousXbutXiXguessXyouXwontXmindXinhalingXitXforXfun.",
XXXX"LaunchXyourselfXintoXouterXspaceXwhileXforgettingXoxygenXonXEarth.",
XXXX"YouXshouldXtryXplayingXsnakeXandXladders,XwithXrealXsnakesXandXnoXladders.",
XXXX"DanceXnakedXonXaXcoupleXofXHTXwires.",
XXXX"ActiveXVolcanoXisXtheXbestXswimmingXpoolXforXyou.",
XXXX"YouXshouldXtryXhotXbathXinXaXvolcano.",
XXXX"TryXtoXspendXoneXdayXinXaXcoffinXandXitXwillXbeXyoursXforever.",
XXXX"HitXUraniumXwithXaXslowXmovingXneutronXinXyourXpresence.XItXwillXbeXaXworthwhileXexperience.",
XXXX"YouXcanXbeXtheXfirstXpersonXtoXstepXonXsun.XHaveXaXtry.",
XXXX"PeopleXlikeXyouXareXtheXreasonXweXhaveXmiddleXfingers.",
XXXX"WhenXyourXmomXdroppedXyouXoffXatXtheXschool,XsheXgotXaXticketXforXlittering.",
XXXX"You’reXsoXuglyXthatXwhenXyouXcry,XtheXtearsXrollXdownXtheXbackXofXyourXhead…justXtoXavoidXyourXface.",
XXXX"IfXyou’reXtalkingXbehindXmyXbackXthenXyou’reXinXaXperfectXpositionXtoXkissXmyXa**!.",
XXXX"StupidityXisXnotXaXcrimeXsoXyouXareXfreeXtoXgo.",
)


@register(pattern="^/insult$")
asyncXdefX_(event):

XXXXifXevent.reply_to_msg_id:
XXXXXXXXreplyX=XawaitXevent.get_reply_message()
XXXXXXXXreplytoX=Xreply.sender_id
XXXXelse:
XXXXXXXXreplytoX=Xevent.sender_id
XXXXawaitXtbot.send_message(event.chat_id,Xrandom.choice(SFW_STRINGS),Xreply_to=replyto)


reactionhappyX=X[
XXXX"''̵͇З=X(X▀X͜͞ʖ▀)X=Ε/̵͇/’’",
XXXX"ʕ•ᴥ•ʔ",
XXXX"(づ｡◕‿‿◕｡)づ",
XXXX"(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧X✧ﾟ･:X*ヽ(◕ヮ◕ヽ)",
XXXX"(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
XXXX"(☞ﾟ∀ﾟ)☞",
XXXX"|X(•X◡•)|X(❍ᴥ❍Ʋ)",
XXXX"(◕‿◕✿)",
XXXX"(ᵔᴥᵔ)",
XXXX"(☞ﾟヮﾟ)☞X☜(ﾟヮﾟ☜)",
XXXX"(づ￣X³￣)づ",
XXXX"♪~Xᕕ(ᐛ)ᕗ",
XXXX"♥️‿♥️",
XXXX"༼XつX͡°X͜ʖX͡°X༽つ",
XXXX"༼XつXಥ_ಥX༽つ",
XXXX"ヾ(⌐■_■)ノ♪",
XXXX"~(˘▾˘~)",
XXXX"◉_◉",
XXXX"(•◡•)X/",
XXXX"(~˘▾˘)~",
XXXX"(｡◕‿‿◕｡)",
XXXX"☜(˚▽˚)☞",
XXXX"(•Ω•)",
XXXX"(｡◕‿◕｡)",
XXXX"(っ˘ڡ˘Σ)",
XXXX"｡◕‿‿◕｡",
XXXX"☜(⌒▽⌒)☞",
XXXX"｡◕‿◕｡",
XXXX"(ღ˘⌣˘ღ)",
XXXX"(▰˘◡˘▰)",
XXXX"^̮^",
XXXX"^̮^",
XXXX">_>",
XXXX"(^̮^)",
XXXX"^̮^",
XXXX"^̮^",
]
reactionangryX=X[
XXXX"▄︻̷┻═━一",
XXXX"(▀Ĺ̯▀X)",
XXXX"(งX͠°X͟ل͜X͡°)ง",
XXXX"༼XつX◕_◕X༽つ",
XXXX"ಠ_ಠ",
XXXX"''̵͇З=(X͠°X͟ʖX͡°)=Ε/̵͇/'",
XXXX"(ง'̀-'́)ง",
XXXX"(ノಠ益ಠ)ノ彡┻━┻",
XXXX"(╯°□°)╯︵XꞰOOQƎƆⱯɟ",
XXXX"ლ(ಠ益ಠლ)",
XXXX"ಠ╭╮ಠ",
XXXX"''̵͇З=(•_•)=Ε/̵͇/''",
XXXX"(╯°□°）╯︵X┻━┻",
XXXX"┻━┻X︵ヽ(Д´)ﾉ︵X┻━┻",
XXXX"⌐╦╦═─",
XXXX"（╯°□°）╯︵(X.O.)",
XXXX":')",
XXXX"┬──┬Xノ(X゜-゜ノ)",
XXXX"ლ(´ڡლ)",
XXXX"(°ロ°)☝️",
XXXX"ლ,ᔑ•ﺪ͟͠•ᔐ.ლ",
XXXX"┬─┬ノ(XºX_Xºノ)",
XXXX"┬─┬﻿X︵X/(.□.X）",
]

reactionsX=X[
XXXX"(X͡°X͜ʖX͡°)",
XXXX"(X.X•́X_ʖX•̀X.)",
XXXX"(XಠX͜ʖXಠ)",
XXXX"(X͡X͜ʖX͡X)",
XXXX"(ʘX͜ʖXʘ)",
XXXX"ヾ(´〇`)ﾉ♪♪♪",
XXXX"ヽ(o´∀`)ﾉ♪♬",
XXXX"♪♬((d⌒ω⌒b))♬♪",
XXXX"└(＾＾)┐",
XXXX"(￣▽￣)/♫•*¨*•.¸¸♪",
XXXX"ヾ(⌐■_■)ノ♪",
XXXX"乁(X•XωX•乁)",
XXXX"♬♫♪◖(●XoX●)◗♪♫♬",
XXXX"(っ˘ڡ˘ς)",
XXXX"(X˘▽˘)っ♨",
XXXX"(　・ω・)⊃-[二二]",
XXXX"(*´ー`)旦X旦(￣ω￣*)",
XXXX"(X￣▽￣)[]X[](≧▽≦X)",
XXXX"(*￣▽￣)旦X且(´∀`*)",
XXXX"(ノX˘_˘)ノ　ζ|||ζ　ζ|||ζ　ζ|||ζ",
XXXX"(ノ°∀°)ノ⌒･*:.｡.X.｡.:*･゜ﾟ･*☆",
XXXX"(⊃｡•́‿•̀｡)⊃━✿✿✿✿✿✿",
XXXX"(∩`XﾛX´)⊃━炎炎炎炎炎",
XXXX"(X・∀・)・・・--------☆",
XXXX"(X-ω-)／占~~~~~",
XXXX"○∞∞∞∞ヽ(^ー^X)",
XXXX"(*＾＾)/~~~~~~~~~~◎",
XXXX"(((X￣□)_／",
XXXX"(ﾒ￣▽￣)︻┳═一",
XXXX"ヽ(X･∀･)ﾉ_θ彡☆Σ(ノX`Д´)ノ",
XXXX"(*`0´)θ☆(メ°皿°)ﾉ",
XXXX"(;X-_-)――――――C<―_-)",
XXXX"ヽ(>_<ヽ)X―⊂|=0ヘ(^‿^X)",
XXXX"(҂`XﾛX´)︻デ═一X＼(ºX□XºXl|l)/",
XXXX"/(X.□.)＼X︵╰(°益°)╯︵X/(.□.X/)",
XXXX"(`⌒*)O-(`⌒´Q)",
XXXX"(っ•﹏•)っX✴==≡눈٩(`皿´҂)ง",
XXXX"ヾ(・ω・)メ(・ω・)ノ",
XXXX"(*^ω^)八(⌒▽⌒)八(-‿‿-X)ヽ",
XXXX"ヽ(X⌒ω⌒)人(=^‥^=X)ﾉ",
XXXX"｡*:☆(・ω・人・ω・)｡:゜☆｡",
XXXX"(°(°ω(°ω°(☆ω☆)°ω°)ω°)°)",
XXXX"(っ˘▽˘)(˘▽˘)˘▽˘ς)",
XXXX"(*＾ω＾)人(＾ω＾*)",
XXXXr"＼(▽￣X\X(￣▽￣)X/X￣▽)／",
XXXX"(￣Θ￣)",
XXXX"＼(XˋXΘX´X)／",
XXXX"(X´(00)ˋX)",
XXXX"＼(￣(oo)￣)／",
XXXX"／(≧XxX≦)＼",
XXXX"／(=･XxX･=)＼",
XXXX"(=^･ω･^=)",
XXXX"(=X;XｪX;X=)",
XXXX"(=⌒‿‿⌒=)",
XXXX"(＾•XωX•＾)",
XXXX"ଲ(ⓛXωXⓛ)ଲ",
XXXX"ଲ(ⓛXωXⓛ)ଲ",
XXXX"(^◔ᴥ◔^)",
XXXX"[(－－)]..zzZ",
XXXX"(￣o￣)XzzZZzzZZ",
XXXX"(＿X＿*)XZXzXz",
XXXX"☆ﾐ(o*･ω･)ﾉ",
XXXX"ε=ε=ε=ε=┌(;￣▽￣)┘",
XXXX"ε===(っ≧ω≦)っ",
XXXX"__φ(．．)",
XXXX"ヾ(X`ー´)シφ__",
XXXX"(X^▽^)ψ__",
XXXX"|･ω･)",
XXXX"|д･)",
XXXX"┬┴┬┴┤･ω･)ﾉ",
XXXX"|･д･)ﾉ",
XXXX"(*￣ii￣)",
XXXX"(＾〃＾)",
XXXX"m(_X_)m",
XXXX"人(_X_*)",
XXXX"(シ.X.)シ",
XXXX"(^_~)",
XXXX"(>ω^)",
XXXX"(^_<)〜☆",
XXXX"(^_<)",
XXXX"(づ￣X³￣)づ",
XXXX"(⊃｡•́‿•̀｡)⊃",
XXXX"⊂(´•XωX•`⊂)",
XXXX"(*・ω・)ﾉ",
XXXX"(^-^*)/",
XXXX"ヾ(*'▽'*)",
XXXX"(^０^)ノ",
XXXX"(*°ｰ°)ﾉ",
XXXX"(￣ω￣)/",
XXXX"(≧▽≦)/",
XXXX"w(°ｏ°)w",
XXXX"(⊙_⊙)",
XXXX"(°ロ°)X!",
XXXX"∑(O_O;)",
XXXX"(￢_￢)",
XXXX"(¬_¬X)",
XXXX"(↼_↼)",
XXXX"(￣ω￣;)",
XXXX"┐('～`;)┌",
XXXX"(・_・;)",
XXXX"(＠_＠)",
XXXX"(•ิ_•ิ)?",
XXXX"ヽ(ー_ーX)ノ",
XXXX"┐(￣ヘ￣)┌",
XXXX"┐(￣～￣)┌",
XXXX"┐(X´XдX`X)┌",
XXXX"╮(︶▽︶)╭",
XXXX"ᕕ(XᐛX)ᕗ",
XXXX"(ノωヽ)",
XXXX"(″ロ゛)",
XXXX"(/ω＼)",
XXXX"(((＞＜)))",
XXXX"~(>_<~)",
XXXX"(×_×)",
XXXX"(×﹏×)",
XXXX"(ノ_<。)",
XXXX"(μ_μ)",
XXXX"o(TヘTo)",
XXXX"(Xﾟ，_ゝ｀)",
XXXX"(X╥ω╥X)",
XXXX"(／ˍ・、)",
XXXX"(つω`｡)",
XXXX"(T_T)",
XXXX"o(〒﹏〒)o",
XXXX"(＃`Д´)",
XXXX"(・`ω´・)",
XXXX"(X`ε´X)",
XXXX"(ﾒ`XﾛX´)",
XXXX"Σ(▼□▼メ)",
XXXX"(҂X`з´X)",
XXXX"٩(╬ʘ益ʘ╬)۶",
XXXX"↑_(ΦwΦ)Ψ",
XXXX"(ﾉಥ益ಥ)ﾉ",
XXXX"(＃＞＜)",
XXXX"(；￣Д￣)",
XXXX"(￢_￢;)",
XXXX"(＾＾＃)",
XXXX"(￣︿￣)",
XXXX"ヾ(X￣O￣)ツ",
XXXX"(ᗒᗣᗕ)՞",
XXXX"(ノ_<。)ヾ(´X▽X`X)",
XXXX"ヽ(￣ω￣(。。X)ゝ",
XXXX"(ﾉ_；)ヾ(´X∀X`X)",
XXXX"(´-ω-`(X_X_X)",
XXXX"(⌒_⌒;)",
XXXX"(*/_＼)",
XXXX"(X◡‿◡X*)",
XXXX"(//ω//)",
XXXX"(￣▽￣*)ゞ",
XXXX"(„ಡωಡ„)",
XXXX"(ﾉ´XзX`)ノ",
XXXX"(♡-_-♡)",
XXXX"(─‿‿─)♡",
XXXX"(´XωX`♡)",
XXXX"(ღ˘⌣˘ღ)",
XXXX"(´•XωX•`)X♡",
XXXX"╰(*´︶`*)╯♡",
XXXX"(≧◡≦)X♡",
XXXX"♡X(˘▽˘>ԅ(X˘⌣˘)",
XXXX"σ(≧ε≦σ)X♡",
XXXX"(˘∀˘)/(μ‿μ)X❤",
XXXX"Σ>―(〃°ω°〃)♡→",
XXXX"(*X^XωX^)",
XXXX"(o^▽^o)",
XXXX"ヽ(・∀・)ﾉ",
XXXX"(o･ω･o)",
XXXX"(^人^)",
XXXX"(X´XωX`X)",
XXXX"(´•XωX•`)",
XXXX"╰(▔∀▔)╯",
XXXX"(✯◡✯)",
XXXX"(⌒‿⌒)",
XXXX"(*°▽°*)",
XXXX"(´｡•XᵕX•｡`)",
XXXX"ヽ(>∀<☆)ノ",
XXXX"＼(￣▽￣)／",
XXXX"(o˘◡˘o)",
XXXX"(╯✧▽✧)╯",
XXXX"(X‾́X◡X‾́X)",
XXXX"(๑˘︶˘๑)",
XXXX"(´･ᴗ･X`X)",
XXXX"(X͡°Xʖ̯X͡°)",
XXXX"(XఠX͟ʖXఠ)",
XXXX"(XಥXʖ̯Xಥ)",
XXXX"(≖X͜ʖ≖)",
XXXX"ヘ(￣ω￣ヘ)",
XXXX"(ﾉ≧∀≦)ﾉ",
XXXX"└(￣-￣└))",
XXXX"┌(＾＾)┘",
XXXX"(^_^♪)",
XXXX"(〜￣△￣)〜",
XXXX"(｢•XωX•)｢",
XXXX"(X˘Xɜ˘)X♬♪♫",
XXXX"(Xo˘◡˘o)X┌iii┐",
XXXX"♨o(>_<)o♨",
XXXX"(X・・)つ―{}@{}@{}-",
XXXX"(*´з`)口ﾟ｡ﾟ口(・∀・X)",
XXXX"(X*^^)o∀*∀o(^^*X)",
XXXX"-●●●-ｃ(・・X)",
XXXX"(ﾉ≧∀≦)ﾉX‥…━━━★",
XXXX"╰(X͡°X͜ʖX͡°X)つ──☆*:・ﾟ",
XXXX"(∩ᄑ_ᄑ)⊃━☆ﾟ*･｡*･:≡(Xε:)",
]


@register(pattern="^/react$")
asyncXdefX_(event):

XXXXifXevent.reply_to_msg_id:
XXXXXXXXreplyX=XawaitXevent.get_reply_message()
XXXXXXXXreplytoX=Xreply.sender_id
XXXXelse:
XXXXXXXXreplytoX=Xevent.sender_id
XXXXreactX=Xrandom.choice(reactions)
XXXXawaitXevent.reply(react,Xreply_to=replyto)


@register(pattern="^/rhappy$")
asyncXdefX_(event):

XXXXifXevent.reply_to_msg_id:
XXXXXXXXreplyX=XawaitXevent.get_reply_message()
XXXXXXXXreplytoX=Xreply.sender_id
XXXXelse:
XXXXXXXXreplytoX=Xevent.sender_id
XXXXrhappyX=Xrandom.choice(reactionhappy)
XXXXawaitXevent.reply(rhappy,Xreply_to=replyto)


@register(pattern="^/rangry$")
asyncXdefX_(event):

XXXXifXevent.reply_to_msg_id:
XXXXXXXXreplyX=XawaitXevent.get_reply_message()
XXXXXXXXreplytoX=Xreply.sender_id
XXXXelse:
XXXXXXXXreplytoX=Xevent.sender_id
XXXXrangryX=Xrandom.choice(reactionangry)
XXXXawaitXevent.reply(rangry,Xreply_to=replyto)


file_helpX=Xos.path.basename(__file__)
file_helpX=Xfile_help.replace(".py",X"")
file_helpoX=Xfile_help.replace("_",X"X")

__help__X=X"""
**SomeXmemesXcommand,XfindXitXallXoutXyourselfX!**

X-X/owo:XOWOXdeXtext
X-X/stretch:XSTRETCHXdeXtext
X-X/clapmoji:XTypeXinXreplyXtoXaXmessageXandXseeXmagic
X-X/bmoji:XTypeXinXreplyXtoXaXmessageXandXseeXmagic
X-X/copypasta:XTypeXinXreplyXtoXaXmessageXandXseeXmagic
X-X/vapor:XowoXvaporXdis
X-X/shoutX<i>text</i>:XWriteXanythingXthatXuXwantXitXtoXshould
X-X/zalgofy:XreplyXtoXaXmessageXtoXglitchXitXout!
X-X/table:XgetXflip/unflipX:v.
X-X/decide:XRandomlyXanswersXyes/no/maybe
X-X/bluetext:XMustXtypeXforXfun
X-X/toss:XTossesXAXcoin
X-X/abuse:XAbusesXtheXcunt
X-X/insult:XInsultXtheXcunt
X-X/slap:XSlapsXtheXcunt
X-X/roll:XRollXaXdice.
X-X/rlg:XJoinXears,nose,mouthXandXcreateXanXemoX;-;
X-X/react:XCheckXonXyourXown
X-X/rhappy:XCheckXonXyourXown
X-X/rangry:XCheckXonXyourXown
X-X/angrymoji:XCheckXonXyourXown
X-X/crymoji:XCheckXonXyourXown
X-X/cowsay,X/tuxsayX,X/milksayX,X/kisssayX,X/wwwsayX,X/defaultsayX,X/bunnysayX,X/moosesayX,X/sheepsayX,X/rensayX,X/cheesesayX,X/ghostbusterssayX,X/skeletonsayX<i>text</i>:XReturnsXaXstylishXartXtextXfromXtheXgivenXtext
X-X/deepfry:XTypeXthisXinXreplyXtoXanXimage/stickerXtoXroastXtheXimage/sticker
X-X/figlet:XAnotherXStyleXart
X-X/dice:XRollXAXdice
X-X/dart:XThrowXaXdartXandXtryXyourXluck
X-X/basketball:XTryXyourXluckXifXyouXcanXenterXtheXballXinXtheXring
X-X/typeX<i>text</i>:XMakeXtheXbotXtypeXsomethingXforXyouXinXaXprofessionalXway
X-X/carbonX<i>text</i>:XBeautifiesXyourXtextXandXenwrapsXinsideXaXterminalXimageX[ENGLISHXONLY]
X-X/stickletX<i>text</i>:XTurnXaXtextXintoXaXsticker
X-X/fortune:XgetsXaXrandomXfortuneXquote
X-X/quotly:XTypeX/quotlyXinXreplyXtoXaXmessageXtoXmakeXaXstickerXofXthat
X-X/animate:XEnwrapXyourXtextXinXaXbeautifulXanime
X
"""

__mod_name__X=X"Memes"
