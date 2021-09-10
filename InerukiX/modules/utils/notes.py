#XCopyrightX(C)X2018X-X2020XMrYacha.XAllXrightsXreserved.XSourceXcodeXavailableXunderXtheXAGPL.
#XCopyrightX(C)X2019XAiogram
#
#XThisXfileXisXpartXofXAllMightBot.
#
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

importXhtml
importXre
importXsys
fromXdatetimeXimportXdatetime

fromXaiogram.typesXimportXMessage
fromXaiogram.types.inline_keyboardXimportXInlineKeyboardButton,XInlineKeyboardMarkup
fromXaiogram.utilsXimportXmarkdown
fromXbabel.datesXimportXformat_date,Xformat_datetime,Xformat_time
fromXtelethon.errorsXimportX(
XXXXBadRequestError,
XXXXButtonUrlInvalidError,
XXXXMediaEmptyError,
XXXXMessageEmptyError,
XXXXRPCError,
)
fromXtelethon.errors.rpcerrorlistXimportXChatWriteForbiddenError
fromXtelethon.tl.customXimportXButton

importXInerukiX.modules.utils.tmarkdownXasXtmarkdown
fromXInerukiXXimportXBOT_USERNAME
fromXInerukiX.services.telethonXimportXtbot

fromX...utils.loggerXimportXlog
fromX.languageXimportXget_chat_lang
fromX.messageXimportXget_args
fromX.tmarkdownXimportXtbold,Xtcode,Xtitalic,Xtlink,Xtpre,Xtstrikethrough,Xtunderline
fromX.user_detailsXimportXget_user_link

BUTTONSX=X{}

ALLOWED_COLUMNSX=X["parse_mode",X"file",X"text",X"preview"]


defXtparse_ent(ent,Xtext,Xas_html=True):
XXXXifXnotXtext:
XXXXXXXXreturnXtext

XXXXetypeX=Xent.type
XXXXoffsetX=Xent.offset
XXXXlengthX=Xent.length

XXXXifXsys.maxunicodeX==X0xFFFF:
XXXXXXXXreturnXtext[offsetX:XoffsetX+Xlength]

XXXXifXnotXisinstance(text,Xbytes):
XXXXXXXXentity_textX=Xtext.encode("utf-16-le")
XXXXelse:
XXXXXXXXentity_textX=Xtext

XXXXentity_textX=Xentity_text[offsetX*X2X:X(offsetX+Xlength)X*X2].decode("utf-16-le")

XXXXifXetypeX==X"bold":
XXXXXXXXmethodX=Xmarkdown.hboldXifXas_htmlXelseXtbold
XXXXXXXXreturnXmethod(entity_text)
XXXXifXetypeX==X"italic":
XXXXXXXXmethodX=Xmarkdown.hitalicXifXas_htmlXelseXtitalic
XXXXXXXXreturnXmethod(entity_text)
XXXXifXetypeX==X"pre":
XXXXXXXXmethodX=Xmarkdown.hpreXifXas_htmlXelseXtpre
XXXXXXXXreturnXmethod(entity_text)
XXXXifXetypeX==X"code":
XXXXXXXXmethodX=Xmarkdown.hcodeXifXas_htmlXelseXtcode
XXXXXXXXreturnXmethod(entity_text)
XXXXifXetypeX==X"strikethrough":
XXXXXXXXmethodX=Xmarkdown.hstrikethroughXifXas_htmlXelseXtstrikethrough
XXXXXXXXreturnXmethod(entity_text)
XXXXifXetypeX==X"underline":
XXXXXXXXmethodX=Xmarkdown.hunderlineXifXas_htmlXelseXtunderline
XXXXXXXXreturnXmethod(entity_text)
XXXXifXetypeX==X"url":
XXXXXXXXreturnXentity_text
XXXXifXetypeX==X"text_link":
XXXXXXXXmethodX=Xmarkdown.hlinkXifXas_htmlXelseXtlink
XXXXXXXXreturnXmethod(entity_text,Xent.url)
XXXXifXetypeX==X"text_mention"XandXent.user:
XXXXXXXXreturnXent.user.get_mention(entity_text,Xas_html=as_html)

XXXXreturnXentity_text


defXget_parsed_msg(message):
XXXXifXnotXmessage.textXandXnotXmessage.caption:
XXXXXXXXreturnX"",X"md"

XXXXtextX=Xmessage.captionXorXmessage.text

XXXXmodeX=Xget_msg_parse(text)
XXXXifXmodeX==X"html":
XXXXXXXXas_htmlX=XTrue
XXXXelse:
XXXXXXXXas_htmlX=XFalse

XXXXentitiesX=Xmessage.caption_entitiesXorXmessage.entities

XXXXifXnotXentities:
XXXXXXXXreturnXtext,Xmode

XXXXifXnotXsys.maxunicodeX==X0xFFFF:
XXXXXXXXtextX=Xtext.encode("utf-16-le")

XXXXresultX=X""
XXXXoffsetX=X0

XXXXforXentityXinXsorted(entities,Xkey=lambdaXitem:Xitem.offset):
XXXXXXXXentity_textX=Xtparse_ent(entity,Xtext,Xas_html=as_html)

XXXXXXXXifXsys.maxunicodeX==X0xFFFF:
XXXXXXXXXXXXpartX=Xtext[offsetX:Xentity.offset]
XXXXXXXXXXXXresultX+=XpartX+Xentity_text
XXXXXXXXelse:
XXXXXXXXXXXXpartX=Xtext[offsetX*X2X:Xentity.offsetX*X2].decode("utf-16-le")
XXXXXXXXXXXXresultX+=XpartX+Xentity_text

XXXXXXXXoffsetX=Xentity.offsetX+Xentity.length

XXXXifXsys.maxunicodeX==X0xFFFF:
XXXXXXXXresultX+=Xtext[offset:]
XXXXelse:
XXXXXXXXresultX+=Xtext[offsetX*X2X:].decode("utf-16-le")

XXXXresultX=Xre.sub(r"\[format:(\w+)\]",X"",Xresult)
XXXXresultX=Xre.sub(r"%PARSEMODE_(\w+)",X"",Xresult)

XXXXifXnotXresult:
XXXXXXXXresultX=X""

XXXXreturnXresult,Xmode


defXget_msg_parse(text,Xdefault_md=True):
XXXXifX"[format:html]"XinXtextXorX"%PARSEMODE_HTML"XinXtext:
XXXXXXXXreturnX"html"
XXXXelifX"[format:none]"XinXtextXorX"%PARSEMODE_NONE"XinXtext:
XXXXXXXXreturnX"none"
XXXXelifX"[format:md]"XinXtextXorX"%PARSEMODE_MD"XinXtext:
XXXXXXXXreturnX"md"
XXXXelse:
XXXXXXXXifXnotXdefault_md:
XXXXXXXXXXXXreturnXNone
XXXXXXXXreturnX"md"


defXparse_button(data,Xname):
XXXXraw_buttonX=Xdata.split("_")
XXXXraw_btn_typeX=Xraw_button[0]

XXXXpatternX=Xre.match(r"btn(.+)(sm|cb|start)",Xraw_btn_type)
XXXXifXnotXpattern:
XXXXXXXXreturnX""

XXXXactionX=Xpattern.group(1)
XXXXargsX=Xraw_button[1]

XXXXifXactionXinXBUTTONS:
XXXXXXXXtextX=Xf"\n[{name}](btn{action}:{args}*!repl!*)"
XXXXelse:
XXXXXXXXifXargs:
XXXXXXXXXXXXtextX=Xf"\n[{name}].(btn{action}:{args})"
XXXXXXXXelse:
XXXXXXXXXXXXtextX=Xf"\n[{name}].(btn{action})"

XXXXreturnXtext


defXget_reply_msg_btns_text(message):
XXXXtextX=X""
XXXXforXcolumnXinXmessage.reply_markup.inline_keyboard:
XXXXXXXXbtn_numX=X0
XXXXXXXXforXbtnXinXcolumn:
XXXXXXXXXXXXbtn_numX+=X1
XXXXXXXXXXXXnameX=Xbtn["text"]

XXXXXXXXXXXXifX"url"XinXbtn:
XXXXXXXXXXXXXXXXurlX=Xbtn["url"]
XXXXXXXXXXXXXXXXifX"?start="XinXurl:
XXXXXXXXXXXXXXXXXXXXraw_btnX=Xurl.split("?start=")[1]
XXXXXXXXXXXXXXXXXXXXtextX+=Xparse_button(raw_btn,Xname)
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXtextX+=Xf"\n[{btn['text']}](btnurl:{btn['url']}*!repl!*)"
XXXXXXXXXXXXelifX"callback_data"XinXbtn:
XXXXXXXXXXXXXXXXtextX+=Xparse_button(btn["callback_data"],Xname)

XXXXXXXXXXXXifXbtn_numX>X1:
XXXXXXXXXXXXXXXXtextX=Xtext.replace("*!repl!*",X":same")
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXtextX=Xtext.replace("*!repl!*",X"")
XXXXreturnXtext


asyncXdefXget_msg_file(message):
XXXXmessage_idX=Xmessage.message_id

XXXXtmsgX=XawaitXtbot.get_messages(message.chat.id,Xids=message_id)

XXXXfile_typesX=X[
XXXXXXXX"sticker",
XXXXXXXX"photo",
XXXXXXXX"document",
XXXXXXXX"video",
XXXXXXXX"audio",
XXXXXXXX"video_note",
XXXXXXXX"voice",
XXXX]
XXXXforXfile_typeXinXfile_types:
XXXXXXXXifXfile_typeXnotXinXmessage:
XXXXXXXXXXXXcontinue
XXXXXXXXreturnX{"id":Xtmsg.file.id,X"type":Xfile_type}
XXXXreturnXNone


asyncXdefXget_parsed_note_list(message,Xallow_reply_message=True,Xsplit_args=1):
XXXXnoteX=X{}
XXXXifX"reply_to_message"XinXmessageXandXallow_reply_message:
XXXXXXXX#XGetXparsedXreplyXmsgXtext
XXXXXXXXtext,Xnote["parse_mode"]X=Xget_parsed_msg(message.reply_to_message)
XXXXXXXX#XGetXparsedXoriginXmsgXtext
XXXXXXXXtextX+=X"X"
XXXXXXXXto_splitX=X"".join(["X"X+XqXforXqXinXget_args(message)[:split_args]])
XXXXXXXXifXnotXto_split:
XXXXXXXXXXXXto_splitX=X"X"
XXXXXXXXtextX+=Xget_parsed_msg(message)[0].partition(message.get_command()X+Xto_split)[
XXXXXXXXXXXX2
XXXXXXXX][1:]
XXXXXXXX#XSetXparse_modeXifXoriginXmsgXoverrideXit
XXXXXXXXifXmodeX:=Xget_msg_parse(message.text,Xdefault_md=False):
XXXXXXXXXXXXnote["parse_mode"]X=Xmode

XXXXXXXX#XGetXmessageXkeyboard
XXXXXXXXifX(
XXXXXXXXXXXX"reply_markup"XinXmessage.reply_to_message
XXXXXXXXXXXXandX"inline_keyboard"XinXmessage.reply_to_message.reply_markup
XXXXXXXX):
XXXXXXXXXXXXtextX+=Xget_reply_msg_btns_text(message.reply_to_message)

XXXXXXXX#XCheckXonXattachment
XXXXXXXXifXmsg_fileX:=XawaitXget_msg_file(message.reply_to_message):
XXXXXXXXXXXXnote["file"]X=Xmsg_file
XXXXelse:
XXXXXXXXtext,Xnote["parse_mode"]X=Xget_parsed_msg(message)
XXXXXXXXifXmessage.get_command()XandXmessage.get_args():
XXXXXXXXXXXX#XRemoveXcmdXandXargXfromXmessage'sXtext
XXXXXXXXXXXXtextX=Xre.sub(message.get_command()X+Xr"\s?",X"",Xtext,X1)
XXXXXXXXXXXXifXsplit_argsX>X0:
XXXXXXXXXXXXXXXXtextX=Xre.sub(re.escape(get_args(message)[0])X+Xr"\s?",X"",Xtext,X1)
XXXXXXXX#XCheckXonXattachment
XXXXXXXXifXmsg_fileX:=XawaitXget_msg_file(message):
XXXXXXXXXXXXnote["file"]X=Xmsg_file

XXXXifXtext.replace("X",X""):
XXXXXXXXnote["text"]X=Xtext

XXXX#XPreview
XXXXifX"text"XinXnoteXandXre.search(r"[$|%]PREVIEW",Xnote["text"]):
XXXXXXXXnote["text"]X=Xre.sub(r"[$|%]PREVIEW",X"",Xnote["text"])
XXXXXXXXnote["preview"]X=XTrue

XXXXreturnXnote


asyncXdefXt_unparse_note_item(
XXXXmessage,Xdb_item,Xchat_id,Xnoformat=None,Xevent=None,Xuser=None
):
XXXXtextX=Xdb_item["text"]XifX"text"XinXdb_itemXelseX""

XXXXfile_idX=XNone
XXXXpreviewX=XNone

XXXXifXnotXuser:
XXXXXXXXuserX=Xmessage.from_user

XXXXifX"file"XinXdb_item:
XXXXXXXXfile_idX=Xdb_item["file"]["id"]

XXXXifXnoformat:
XXXXXXXXmarkupX=XNone
XXXXXXXXifX"parse_mode"XnotXinXdb_itemXorXdb_item["parse_mode"]X==X"none":
XXXXXXXXXXXXtextX+=X"\n%PARSEMODE_NONE"
XXXXXXXXelifXdb_item["parse_mode"]X==X"html":
XXXXXXXXXXXXtextX+=X"\n%PARSEMODE_HTML"

XXXXXXXXifX"preview"XinXdb_itemXandXdb_item["preview"]:
XXXXXXXXXXXXtextX+=X"\n%PREVIEW"

XXXXXXXXdb_item["parse_mode"]X=XNone

XXXXelse:
XXXXXXXXpmX=XTrueXifXmessage.chat.typeX==X"private"XelseXFalse
XXXXXXXXtext,XmarkupX=Xbutton_parser(chat_id,Xtext,Xpm=pm)

XXXXXXXXifXnotXtextXandXnotXfile_id:
XXXXXXXXXXXXtextX=X("#"X+Xdb_item["names"][0])XifX"names"XinXdb_itemXelseX"404"

XXXXXXXXifX"parse_mode"XnotXinXdb_itemXorXdb_item["parse_mode"]X==X"none":
XXXXXXXXXXXXdb_item["parse_mode"]X=XNone
XXXXXXXXelifXdb_item["parse_mode"]X==X"md":
XXXXXXXXXXXXtextX=XawaitXvars_parser(
XXXXXXXXXXXXXXXXtext,Xmessage,Xchat_id,Xmd=True,Xevent=event,Xuser=user
XXXXXXXXXXXX)
XXXXXXXXelifXdb_item["parse_mode"]X==X"html":
XXXXXXXXXXXXtextX=XawaitXvars_parser(
XXXXXXXXXXXXXXXXtext,Xmessage,Xchat_id,Xmd=False,Xevent=event,Xuser=user
XXXXXXXXXXXX)

XXXXXXXXifX"preview"XinXdb_itemXandXdb_item["preview"]:
XXXXXXXXXXXXpreviewX=XTrue

XXXXreturnXtext,X{
XXXXXXXX"buttons":Xmarkup,
XXXXXXXX"parse_mode":Xdb_item["parse_mode"],
XXXXXXXX"file":Xfile_id,
XXXXXXXX"link_preview":Xpreview,
XXXX}


asyncXdefXsend_note(send_id,Xtext,X**kwargs):
XXXXifXtext:
XXXXXXXXtextX=Xtext[:4090]

XXXXifX"parse_mode"XinXkwargsXandXkwargs["parse_mode"]X==X"md":
XXXXXXXXkwargs["parse_mode"]X=Xtmarkdown

XXXXtry:
XXXXXXXXreturnXawaitXtbot.send_message(send_id,Xtext,X**kwargs)

XXXXexceptX(ButtonUrlInvalidError,XMessageEmptyError,XMediaEmptyError):
XXXXXXXXreturnXawaitXtbot.send_message(
XXXXXXXXXXXXsend_id,X"IXfoundXthisXnoteXinvalid!XPleaseXupdateXitX(readXhelp)."
XXXXXXXX)
XXXXexceptXRPCError:
XXXXXXXXlog.error("SendXNoteXErrorXbotXisXKicked/MutedXinXchatX[IGNORE]")
XXXXXXXXreturn
XXXXexceptXChatWriteForbiddenError:
XXXXXXXXlog.error("SendXNoteXErrorXbotXisXKicked/MutedXinXchatX[IGNORE]")
XXXXXXXXreturn
XXXXexceptXBadRequestError:XX#XifXreplyXmessageXdeleted
XXXXXXXXdelXkwargs["reply_to"]
XXXXXXXXreturnXawaitXtbot.send_message(send_id,Xtext,X**kwargs)
XXXXexceptXExceptionXasXerr:
XXXXXXXXlog.error("SomethingXhappenedXonXsendingXnote",Xexc_info=err)


defXbutton_parser(chat_id,Xtexts,Xpm=False,Xaio=False,Xrow_width=None):
XXXXbuttonsX=XInlineKeyboardMarkup(row_width=row_width)XifXaioXelseX[]
XXXXpatternX=Xr"\[(.+?)\]\((button|btn|#)(.+?)(:.+?|)(:same|)\)(\n|)"
XXXXraw_buttonsX=Xre.findall(pattern,Xtexts)
XXXXtextX=Xre.sub(pattern,X"",Xtexts)
XXXXbtnX=XNone
XXXXforXraw_buttonXinXraw_buttons:
XXXXXXXXnameX=Xraw_button[0]
XXXXXXXXactionX=X(
XXXXXXXXXXXXraw_button[1]XifXraw_button[1]XnotXinX("button",X"btn")XelseXraw_button[2]
XXXXXXXX)

XXXXXXXXifXraw_button[3]:
XXXXXXXXXXXXargumentX=Xraw_button[3][1:].lower().replace("`",X"")
XXXXXXXXelifXactionXinX("#"):
XXXXXXXXXXXXargumentX=Xraw_button[2]
XXXXXXXXXXXXprint(raw_button[2])
XXXXXXXXelse:
XXXXXXXXXXXXargumentX=X""

XXXXXXXXifXactionXinXBUTTONS.keys():
XXXXXXXXXXXXcbX=XBUTTONS[action]
XXXXXXXXXXXXstringX=Xf"{cb}_{argument}_{chat_id}"XifXargumentXelseXf"{cb}_{chat_id}"
XXXXXXXXXXXXifXaio:
XXXXXXXXXXXXXXXXstart_btnX=XInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXname,Xurl=f"https://t.me/{BOT_USERNAME}?start="X+Xstring
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXcb_btnX=XInlineKeyboardButton(name,Xcallback_data=string)
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXstart_btnX=XButton.url(
XXXXXXXXXXXXXXXXXXXXname,Xf"https://t.me/{BOT_USERNAME}?start="X+Xstring
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXcb_btnX=XButton.inline(name,Xstring)

XXXXXXXXXXXXifXcb.endswith("sm"):
XXXXXXXXXXXXXXXXbtnX=Xcb_btnXifXpmXelseXstart_btn
XXXXXXXXXXXXelifXcb.endswith("cb"):
XXXXXXXXXXXXXXXXbtnX=Xcb_btn
XXXXXXXXXXXXelifXcb.endswith("start"):
XXXXXXXXXXXXXXXXbtnX=Xstart_btn
XXXXXXXXXXXXelifXcb.startswith("url"):
XXXXXXXXXXXXXXXX#XWorkaroundXtoXmakeXURLsXcase-sensitiveXTODO:XmakeXbetter
XXXXXXXXXXXXXXXXargumentX=Xraw_button[3][1:].replace("`",X"")XifXraw_button[3]XelseX""
XXXXXXXXXXXXXXXXbtnX=XButton.url(name,Xargument)
XXXXXXXXXXXXelifXcb.endswith("rules"):
XXXXXXXXXXXXXXXXbtnX=Xstart_btn
XXXXXXXXelifXactionX==X"url":
XXXXXXXXXXXXargumentX=Xraw_button[3][1:].replace("`",X"")XifXraw_button[3]XelseX""
XXXXXXXXXXXXifXargument[0]X==X"/"XandXargument[1]X==X"/":
XXXXXXXXXXXXXXXXargumentX=Xargument[2:]
XXXXXXXXXXXXbtnX=X(
XXXXXXXXXXXXXXXXInlineKeyboardButton(name,Xurl=argument)
XXXXXXXXXXXXXXXXifXaio
XXXXXXXXXXXXXXXXelseXButton.url(name,Xargument)
XXXXXXXXXXXX)
XXXXXXXXelse:
XXXXXXXXXXXX#XIfXbtnXnotXregistred
XXXXXXXXXXXXbtnX=XNone
XXXXXXXXXXXXifXargument:
XXXXXXXXXXXXXXXXtextX+=Xf"\n[{name}].(btn{action}:{argument})"
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXtextX+=Xf"\n[{name}].(btn{action})"
XXXXXXXXXXXXXXXXcontinue

XXXXXXXXifXbtn:
XXXXXXXXXXXXifXaio:
XXXXXXXXXXXXXXXXbuttons.insert(btn)XifXraw_button[4]XelseXbuttons.add(btn)
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXifXlen(buttons)X<X1XandXraw_button[4]:
XXXXXXXXXXXXXXXXXXXXbuttons.add(btn)XifXaioXelseXbuttons.append([btn])
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXbuttons[-1].append(btn)XifXraw_button[4]XelseXbuttons.append([btn])

XXXXifXnotXaioXandXlen(buttons)X==X0:
XXXXXXXXbuttonsX=XNone

XXXXifXnotXtextXorXtext.isspace():XX#XTODO:XSometimesXweXcanXreturnXtextX==X'X'
XXXXXXXXtextX=XNone

XXXXreturnXtext,Xbuttons


asyncXdefXvars_parser(
XXXXtext,Xmessage,Xchat_id,Xmd=False,Xevent:XMessageX=XNone,Xuser=None
):
XXXXifXeventXisXNone:
XXXXXXXXeventX=Xmessage

XXXXifXnotXtext:
XXXXXXXXreturnXtext

XXXXlanguage_codeX=XawaitXget_chat_lang(chat_id)
XXXXcurrent_datetimeX=Xdatetime.now()

XXXXfirst_nameX=Xhtml.escape(user.first_name,Xquote=False)
XXXXlast_nameX=Xhtml.escape(user.last_nameXorX"",Xquote=False)
XXXXuser_idX=X(
XXXXXXXX[user.idXforXuserXinXevent.new_chat_members][0]
XXXXXXXXifX"new_chat_members"XinXeventXandXevent.new_chat_membersX!=X[]
XXXXXXXXelseXuser.id
XXXX)
XXXXmentionX=XawaitXget_user_link(user_id,Xmd=md)

XXXXifX(
XXXXXXXXhasattr(event,X"new_chat_members")
XXXXXXXXandXevent.new_chat_members
XXXXXXXXandXevent.new_chat_members[0].username
XXXX):
XXXXXXXXusernameX=X"@"X+Xevent.new_chat_members[0].username
XXXXelifXuser.username:
XXXXXXXXusernameX=X"@"X+Xuser.username
XXXXelse:
XXXXXXXXusernameX=Xmention

XXXXchat_idX=Xmessage.chat.id
XXXXchat_nameX=Xhtml.escape(message.chat.titleXorX"Local",Xquote=False)
XXXXchat_nickX=Xmessage.chat.usernameXorXchat_name

XXXXcurrent_dateX=Xhtml.escape(
XXXXXXXXformat_date(date=current_datetime,Xlocale=language_code),Xquote=False
XXXX)
XXXXcurrent_timeX=Xhtml.escape(
XXXXXXXXformat_time(time=current_datetime,Xlocale=language_code),Xquote=False
XXXX)
XXXXcurrent_timedateX=Xhtml.escape(
XXXXXXXXformat_datetime(datetime=current_datetime,Xlocale=language_code),Xquote=False
XXXX)

XXXXtextX=X(
XXXXXXXXtext.replace("{first}",Xfirst_name)
XXXXXXXX.replace("{last}",Xlast_name)
XXXXXXXX.replace("{fullname}",Xfirst_nameX+X"X"X+Xlast_name)
XXXXXXXX.replace("{id}",Xstr(user_id).replace("{userid}",Xstr(user_id)))
XXXXXXXX.replace("{mention}",Xmention)
XXXXXXXX.replace("{username}",Xusername)
XXXXXXXX.replace("{chatid}",Xstr(chat_id))
XXXXXXXX.replace("{chatname}",Xstr(chat_name))
XXXXXXXX.replace("{chatnick}",Xstr(chat_nick))
XXXXXXXX.replace("{date}",Xstr(current_date))
XXXXXXXX.replace("{time}",Xstr(current_time))
XXXXXXXX.replace("{timedate}",Xstr(current_timedate))
XXXX)
XXXXreturnXtext
