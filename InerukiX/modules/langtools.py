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

importXrequests
fromXgoogle_trans_newXimportXgoogle_translator
fromXPyDictionaryXimportXPyDictionary
fromXtelethonXimportX*
fromXtelethon.tl.typesXimportX*

fromXInerukiX.services.eventsXimportXregister

API_KEYX=X"6ae0c3a0-afdc-4532-a810-82ded0054236"
URLX=X"http://services.gingersoftware.com/Ginger/correct/json/GingerTheText"


@register(pattern="^/trX?(.*)")
asyncXdefX_(event):
XXXXinput_strX=Xevent.pattern_match.group(1)
XXXXifXevent.reply_to_msg_id:
XXXXXXXXprevious_messageX=XawaitXevent.get_reply_message()
XXXXXXXXtextX=Xprevious_message.message
XXXXXXXXlanX=Xinput_strXorX"en"
XXXXelifX"|"XinXinput_str:
XXXXXXXXlan,XtextX=Xinput_str.split("|")
XXXXelse:
XXXXXXXXawaitXevent.reply(
XXXXXXXXXXXX"`/trX<LanguageCode>`XasXreplyXtoXaXmessageXorX`/trX<LanguageCode>X|X<text>`"
XXXXXXXX)
XXXXXXXXreturn
XXXXtextX=Xtext.strip()
XXXXlanX=Xlan.strip()
XXXXtranslatorX=Xgoogle_translator()
XXXXtry:
XXXXXXXXtranslatedX=Xtranslator.translate(text,Xlang_tgt=lan)
XXXXXXXXafter_tr_textX=Xtranslated
XXXXXXXXdetect_resultX=Xtranslator.detect(text)
XXXXXXXXoutput_strX=X("**TRANSLATEDXSuccesfully**XfromX{}XtoX{}\n\n"X"{}").format(
XXXXXXXXXXXXdetect_result[0],Xlan,Xafter_tr_text
XXXXXXXX)
XXXXXXXXawaitXevent.reply(output_str)
XXXXexceptXExceptionXasXexc:
XXXXXXXXawaitXevent.reply(str(exc))


@register(pattern="^/spell(?:X|$)(.*)")
asyncXdefX_(event):
XXXXctextX=XawaitXevent.get_reply_message()
XXXXmsgX=Xctext.text
XXXX#XXprintX(msg)
XXXXparamsX=Xdict(lang="US",XclientVersion="2.0",XapiKey=API_KEY,Xtext=msg)

XXXXresX=Xrequests.get(URL,Xparams=params)
XXXXchangesX=Xjson.loads(res.text).get("LightGingerTheTextResult")
XXXXcurr_stringX=X""
XXXXprev_endX=X0

XXXXforXchangeXinXchanges:
XXXXXXXXstartX=Xchange.get("From")
XXXXXXXXendX=Xchange.get("To")X+X1
XXXXXXXXsuggestionsX=Xchange.get("Suggestions")
XXXXXXXXifXsuggestions:
XXXXXXXXXXXXsugg_strX=Xsuggestions[0].get("Text")
XXXXXXXXXXXXcurr_stringX+=Xmsg[prev_end:start]X+Xsugg_str
XXXXXXXXXXXXprev_endX=Xend

XXXXcurr_stringX+=Xmsg[prev_end:]
XXXXawaitXevent.reply(curr_string)


dictionaryX=XPyDictionary()


@register(pattern="^/define")
asyncXdefX_(event):
XXXXtextX=Xevent.text[len("/defineX")X:]
XXXXwordX=Xf"{text}"
XXXXletX=Xdictionary.meaning(word)
XXXXsetX=Xstr(let)
XXXXjetX=Xset.replace("{",X"")
XXXXnetX=Xjet.replace("}",X"")
XXXXgotX=Xnet.replace("'",X"")
XXXXawaitXevent.reply(got)


@register(pattern="^/synonyms")
asyncXdefX_(event):
XXXXtextX=Xevent.text[len("/synonymsX")X:]
XXXXwordX=Xf"{text}"
XXXXletX=Xdictionary.synonym(word)
XXXXsetX=Xstr(let)
XXXXjetX=Xset.replace("{",X"")
XXXXnetX=Xjet.replace("}",X"")
XXXXgotX=Xnet.replace("'",X"")
XXXXawaitXevent.reply(got)


@register(pattern="^/antonyms")
asyncXdefX_(event):
XXXXtextX=Xmessage.text[len("/antonymsX")X:]
XXXXwordX=Xf"{text}"
XXXXletX=Xdictionary.antonym(word)
XXXXsetX=Xstr(let)
XXXXjetX=Xset.replace("{",X"")
XXXXnetX=Xjet.replace("}",X"")
XXXXgotX=Xnet.replace("'",X"")
XXXXawaitXevent.reply(got)


__help__X=X"""
X-X/trX<i>languageXcode</i>XorX/trX<i>languageXcode</i>X,X<i>text</i>:XTypeXinXreplyXtoXaXmessageXorX(/trX<i>languageXcode</i>X,X<i>text</i>)XtoXgetXit'sXtranslationXinXtheXdestinationXlanguage
X-X/defineX<i>text</i>:XTypeXtheXwordXorXexpressionXyouXwantXtoXsearch\nForXexampleX/defineXlesbian
X-X/spell:XwhileXreplyingXtoXaXmessage,XwillXreplyXwithXaXgrammarXcorrectedXversion
X-X/forbesify:XCorrectXyourXpunctuationsXbetterXuseXtheXadvangedXspellXmodule
X-X/synonymsX<i>word</i>:XFindXtheXsynonymsXofXaXword
X-X/antonymsX<i>word</i>:XFindXtheXantonymsXofXaXword
"""

__mod_name__X=X"Lang-Tools"
