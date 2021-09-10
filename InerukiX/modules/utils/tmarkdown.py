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

importXre
importXwarnings

fromXtelethon.helpersXimportXadd_surrogate,Xdel_surrogate,Xstrip_text
fromXtelethon.tlXimportXTLObject
fromXtelethon.tl.typesXimportX(
XXXXMessageEntityBold,
XXXXMessageEntityCode,
XXXXMessageEntityItalic,
XXXXMessageEntityMentionName,
XXXXMessageEntityPre,
XXXXMessageEntityStrike,
XXXXMessageEntityTextUrl,
XXXXMessageEntityUnderline,
)

DEFAULT_DELIMITERSX=X{
XXXX"**":XMessageEntityBold,
XXXX"__":XMessageEntityItalic,
XXXX"~~":XMessageEntityStrike,
XXXX"++":XMessageEntityUnderline,
XXXX"`":XMessageEntityCode,
XXXX"```":XMessageEntityPre,
}

DEFAULT_URL_REX=Xre.compile(r"\[([\S\s]+?)\]\((.+?)\)")
DEFAULT_URL_FORMATX=X"[{0}]({1})"


defXoverlap(a,Xb,Xx,Xy):
XXXXreturnXmax(a,Xx)X<Xmin(b,Xy)


defXparse(message,Xdelimiters=None,Xurl_re=None):
XXXX"""
XXXXParsesXtheXgivenXmarkdownXmessageXandXreturnsXitsXstrippedXrepresentation
XXXXplusXaXlistXofXtheXMessageEntity'sXthatXwereXfound.
XXXX:paramXmessage:XtheXmessageXwithXmarkdown-likeXsyntaxXtoXbeXparsed.
XXXX:paramXdelimiters:XtheXdelimitersXtoXbeXused,X{delimiter:Xtype}.
XXXX:paramXurl_re:XtheXURLXbytesXregexXtoXbeXused.XMustXhaveXtwoXgroups.
XXXX:return:XaXtupleXconsistingXofX(cleanXmessage,X[messageXentities]).
XXXX"""
XXXXifXnotXmessage:
XXXXXXXXreturnXmessage,X[]

XXXXifXurl_reXisXNone:
XXXXXXXXurl_reX=XDEFAULT_URL_RE
XXXXelifXisinstance(url_re,Xstr):
XXXXXXXXurl_reX=Xre.compile(url_re)

XXXXifXnotXdelimiters:
XXXXXXXXifXdelimitersXisXnotXNone:
XXXXXXXXXXXXreturnXmessage,X[]
XXXXXXXXdelimitersX=XDEFAULT_DELIMITERS

XXXX#XBuildXaXregexXtoXefficientlyXtestXallXdelimitersXatXonce.
XXXX#XNoteXthatXtheXlargestXdelimiterXshouldXgoXfirst,XweXdon't
XXXX#XwantX```XtoXbeXinterpretedXasXaXsingleXback-tickXinXaXcodeXblock.
XXXXdelim_reX=Xre.compile(
XXXXXXXX"|".join(
XXXXXXXXXXXX"({})".format(re.escape(k))
XXXXXXXXXXXXforXkXinXsorted(delimiters,Xkey=len,Xreverse=True)
XXXXXXXX)
XXXX)

XXXX#XCannotXuseXaXforXloopXbecauseXweXneedXtoXskipXsomeXindices
XXXXiX=X0
XXXXresultX=X[]

XXXX#XWorkXonXbyteXlevelXwithXtheXutf-16leXencodingXtoXgetXtheXoffsetsXright.
XXXX#XTheXoffsetXwillXjustXbeXhalfXtheXindexXwe'reXat.
XXXXmessageX=Xadd_surrogate(message)
XXXXwhileXiX<Xlen(message):
XXXXXXXXmX=Xdelim_re.match(message,Xpos=i)

XXXXXXXX#XDidXweXfindXsomeXdelimiterXhereXatX`i`?
XXXXXXXXifXm:
XXXXXXXXXXXXdelimX=Xnext(filter(None,Xm.groups()))

XXXXXXXXXXXX#X+1XtoXavoidXmatchingXrightXafterX(e.g.X"****")
XXXXXXXXXXXXendX=Xmessage.find(delim,XiX+Xlen(delim)X+X1)

XXXXXXXXXXXX#XDidXweXfindXtheXearliestXclosingXtag?
XXXXXXXXXXXXifXendX!=X-1:

XXXXXXXXXXXXXXXX#XRemoveXtheXdelimiterXfromXtheXstring
XXXXXXXXXXXXXXXXmessageX=X"".join(
XXXXXXXXXXXXXXXXXXXX(
XXXXXXXXXXXXXXXXXXXXXXXXmessage[:i],
XXXXXXXXXXXXXXXXXXXXXXXXmessage[iX+Xlen(delim)X:Xend],
XXXXXXXXXXXXXXXXXXXXXXXXmessage[endX+Xlen(delim)X:],
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXX)

XXXXXXXXXXXXXXXX#XCheckXotherXaffectedXentities
XXXXXXXXXXXXXXXXforXentXinXresult:
XXXXXXXXXXXXXXXXXXXX#XIfXtheXendXisXafterXourXstart,XitXisXaffected
XXXXXXXXXXXXXXXXXXXXifXent.offsetX+Xent.lengthX>Xi:
XXXXXXXXXXXXXXXXXXXXXXXX#XIfXtheXoldXstartXisXalsoXbeforeXours,XitXisXfullyXenclosed
XXXXXXXXXXXXXXXXXXXXXXXXifXent.offsetX<=Xi:
XXXXXXXXXXXXXXXXXXXXXXXXXXXXent.lengthX-=Xlen(delim)X*X2
XXXXXXXXXXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXXXXXXXXXent.lengthX-=Xlen(delim)

XXXXXXXXXXXXXXXX#XAppendXtheXfoundXentity
XXXXXXXXXXXXXXXXentX=Xdelimiters[delim]
XXXXXXXXXXXXXXXXifXentX==XMessageEntityPre:
XXXXXXXXXXXXXXXXXXXXresult.append(ent(i,XendX-XiX-Xlen(delim),X""))XX#XhasX'lang'
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXresult.append(ent(i,XendX-XiX-Xlen(delim)))

XXXXXXXXXXXXXXXX#XNoXnestedXentitiesXinsideXcodeXblocks
XXXXXXXXXXXXXXXXifXentXinX(MessageEntityCode,XMessageEntityPre):
XXXXXXXXXXXXXXXXXXXXiX=XendX-Xlen(delim)

XXXXXXXXXXXXXXXXcontinue

XXXXXXXXelifXurl_re:
XXXXXXXXXXXXmX=Xurl_re.match(message,Xpos=i)
XXXXXXXXXXXXifXm:
XXXXXXXXXXXXXXXX#XReplaceXtheXwholeXmatchXwithXonlyXtheXinlineXURLXtext.
XXXXXXXXXXXXXXXXmessageX=X"".join(
XXXXXXXXXXXXXXXXXXXX(message[:Xm.start()],Xm.group(1),Xmessage[m.end()X:])
XXXXXXXXXXXXXXXX)

XXXXXXXXXXXXXXXXdelim_sizeX=Xm.end()X-Xm.start()X-Xlen(m.group())
XXXXXXXXXXXXXXXXforXentXinXresult:
XXXXXXXXXXXXXXXXXXXX#XIfXtheXendXisXafterXourXstart,XitXisXaffected
XXXXXXXXXXXXXXXXXXXXifXent.offsetX+Xent.lengthX>Xm.start():
XXXXXXXXXXXXXXXXXXXXXXXXent.lengthX-=Xdelim_size

XXXXXXXXXXXXXXXXresult.append(
XXXXXXXXXXXXXXXXXXXXMessageEntityTextUrl(
XXXXXXXXXXXXXXXXXXXXXXXXoffset=m.start(),
XXXXXXXXXXXXXXXXXXXXXXXXlength=len(m.group(1)),
XXXXXXXXXXXXXXXXXXXXXXXXurl=del_surrogate(m.group(2)),
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXiX+=Xlen(m.group(1))
XXXXXXXXXXXXXXXXcontinue

XXXXXXXXiX+=X1

XXXXmessageX=Xstrip_text(message,Xresult)
XXXXreturnXdel_surrogate(message),Xresult


defXunparse(text,Xentities,Xdelimiters=None,Xurl_fmt=None):
XXXX"""
XXXXPerformsXtheXreverseXoperationXtoX.parse(),XeffectivelyXreturning
XXXXmarkdown-likeXsyntaxXgivenXaXnormalXtextXandXitsXMessageEntity's.
XXXX:paramXtext:XtheXtextXtoXbeXreconvertedXintoXmarkdown.
XXXX:paramXentities:XtheXMessageEntity'sXappliedXtoXtheXtext.
XXXX:return:XaXmarkdown-likeXtextXrepresentingXtheXcombinationXofXbothXinputs.
XXXX"""
XXXXifXnotXtextXorXnotXentities:
XXXXXXXXreturnXtext

XXXXifXnotXdelimiters:
XXXXXXXXifXdelimitersXisXnotXNone:
XXXXXXXXXXXXreturnXtext
XXXXXXXXdelimitersX=XDEFAULT_DELIMITERS

XXXXifXurl_fmtXisXnotXNone:
XXXXXXXXwarnings.warn(
XXXXXXXXXXXX"url_fmtXisXdeprecated"
XXXXXXXX)XX#XsinceXitXcomplicatesXeverythingX*aXlot*

XXXXifXisinstance(entities,XTLObject):
XXXXXXXXentitiesX=X(entities,)

XXXXtextX=Xadd_surrogate(text)
XXXXdelimitersX=X{v:XkXforXk,XvXinXdelimiters.items()}
XXXXinsert_atX=X[]
XXXXforXentityXinXentities:
XXXXXXXXsX=Xentity.offset
XXXXXXXXeX=Xentity.offsetX+Xentity.length
XXXXXXXXdelimiterX=Xdelimiters.get(type(entity),XNone)
XXXXXXXXifXdelimiter:
XXXXXXXXXXXXinsert_at.append((s,Xdelimiter))
XXXXXXXXXXXXinsert_at.append((e,Xdelimiter))
XXXXXXXXelse:
XXXXXXXXXXXXurlX=XNone
XXXXXXXXXXXXifXisinstance(entity,XMessageEntityTextUrl):
XXXXXXXXXXXXXXXXurlX=Xentity.url
XXXXXXXXXXXXelifXisinstance(entity,XMessageEntityMentionName):
XXXXXXXXXXXXXXXXurlX=X"tg://user?id={}".format(entity.user_id)
XXXXXXXXXXXXifXurl:
XXXXXXXXXXXXXXXXinsert_at.append((s,X"["))
XXXXXXXXXXXXXXXXinsert_at.append((e,X"]({})".format(url)))

XXXXinsert_at.sort(key=lambdaXt:Xt[0])
XXXXwhileXinsert_at:
XXXXXXXXat,XwhatX=Xinsert_at.pop()

XXXXXXXX#XIfXweXareXinXtheXmiddleXofXaXsurrogateXnudgeXtheXpositionXbyX+1.
XXXXXXXX#XOtherwiseXweXwouldXendXupXwithXmalformedXtextXandXfailXtoXencode.
XXXXXXXX#XForXexampleXofXbadXinput:X"HiX\ud83d\ude1c"
XXXXXXXX#Xhttps://en.wikipedia.org/wiki/UTF-16#U+010000_to_U+10FFFF
XXXXXXXXwhileXatX<Xlen(text)XandX"\ud800"X<=Xtext[at]X<=X"\udfff":
XXXXXXXXXXXXatX+=X1

XXXXXXXXtextX=Xtext[:at]X+XwhatX+Xtext[at:]

XXXXreturnXdel_surrogate(text)


defXtbold(text,Xsep="X"):
XXXXreturnXf"**{text}**"


defXtitalic(text,Xsep="X"):
XXXXreturnXf"__{text}__"


defXtcode(text,Xsep="X"):
XXXXreturnXf"`{text}`"


defXtpre(text,Xsep="X"):
XXXXreturnXf"```{text}```"


defXtstrikethrough(text,Xsep="X"):
XXXXreturnXf"~~{text}~~"


defXtunderline(text,Xsep="X"):
XXXXreturnXf"++{text}++"


defXtlink(title,Xurl):
XXXXreturnX"[{0}]({1})".format(title,Xurl)
