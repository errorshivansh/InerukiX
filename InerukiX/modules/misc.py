#XCopyrightX(C)X2018X-X2020XMrYacha.XAllXrightsXreserved.XSourceXcodeXavailableXunderXtheXAGPL.
#XCopyrightX(C)X2021Xerrorshivansh
#XCopyrightX(C)X2020XInukaXAsith

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
fromXcontextlibXimportXsuppress
fromXdatetimeXimportXdatetime

importXwikipedia

#XYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XalongXwithXthisXprogram.XXIfXnot,XseeX<http://www.gnu.org/licenses/>.
fromXaiogram.typesXimportXInlineKeyboardButton,XInlineKeyboardMarkup,XMessage
fromXaiogram.utils.exceptionsXimportX(
XXXXBadRequest,
XXXXMessageNotModified,
XXXXMessageToDeleteNotFound,
)

fromXInerukiX.decoratorXimportXregister

fromX.utils.disableXimportXdisableable_dec
fromX.utils.httpxXimportXhttp
fromX.utils.languageXimportXget_strings_dec
fromX.utils.messageXimportXget_args_str
fromX.utils.notesXimportXget_parsed_note_list,Xsend_note,Xt_unparse_note_item
fromX.utils.user_detailsXimportXis_user_admin


@register(cmds="buttonshelp",Xno_args=True,Xonly_pm=True)
asyncXdefXbuttons_help(message):
XXXXawaitXmessage.reply(
XXXXXXXX"""
<b>Buttons:</b>
HereXyouXwillXknowXhowXtoXsetupXbuttonsXinXyourXnote,XwelcomeXnote,Xetc...

ThereXareXdifferentXtypesXofXbuttons!

<i>DueXtoXcurrentXImplementationXaddingXinvalidXbuttonXsyntaxXtoXyourXnoteXwillXraiseXerror!XThisXwillXbeXfixedXinXnextXmajorXversion.</i>

<b>DidXyouXknow?</b>
YouXcouldXsaveXbuttonsXinXsameXrowXusingXthisXsyntax
<code>[Button](btn{mode}:{argsXifXany}:same)</code>
(addingX<code>:same</code>XlikeXthatXdoesXtheXjob.)

<b>ButtonXNote:</b>
<i>Don'tXconfuseXthisXtitleXwithXnotesXwithXbuttons</i>X😜

ThisXtypesXofXbuttonXwillXallowXyouXtoXshowXspecificXnotesXtoXusersXwhenXtheyXclickXonXbuttons!

YouXcanXsaveXnoteXwithXbuttonXnoteXwithoutXanyXhassleXbyXaddingXbelowXlineXtoXyourXnoteX(XDon'tXforgetXtoXreplaceX<code>notename</code>XaccordingXtoXyouX😀)

<code>[ButtonXName](btnnote:notename)</code>

<b>URLXButton:</b>
AhXasXyouXguessed!XThisXmethodXisXusedXtoXaddXURLXbuttonXtoXyourXnote.XWithXthisXyouXcanXredirectXusersXtoXyourXwebsiteXorXevenXredirectingXthemXtoXanyXchannel,XchatXorXmessages!

YouXcanXaddXURLXbuttonXbyXaddingXfollowingXsyntaxXtoXyourXnote

<code>[ButtonXName](btnurl:https://your.link.here)</code>

<b>ButtonXrules:</b>
WellXinXv2XweXintroducedXsomeXchanges,XrulesXareXnowXsavedXseperatelyXunlikeXsavedXasXnoteXbeforeXv2XsoXitXrequireXseperateXbuttonXmethod!

YouXcanXuseXthisXbuttonXmethodXforXincludingXRulesXbuttonXinXyourXwelcomeXmessages,XfiltersXetc..XliterallyXanywhere*

YouXuseXthisXbuttonXwithXaddingXfollowingXsyntaxXtoXyourXmessageXwhichXsupportXformatting!
<code>[ButtonXName](btnrules)</code>
XXXX"""
XXXX)


@register(cmds="variableshelp",Xno_args=True,Xonly_pm=True)
asyncXdefXbuttons_help(message):
XXXXawaitXmessage.reply(
XXXXXXXX"""
<b>Variables:</b>
VariablesXareXspecialXwordsXwhichXwillXbeXreplacedXbyXactualXinfo

<b>AvaibleXvariables:</b>
<code>{first}</code>:XUser'sXfirstXname
<code>{last}</code>:XUser'sXlastXname
<code>{fullname}</code>:XUser'sXfullXname
<code>{id}</code>:XUser'sXID
<code>{mention}</code>:XMentionXtheXuserXusingXfirstXname
<code>{username}</code>:XGetXtheXusername,XifXuserXdon'tXhaveXusernameXwillXbeXreturnedXmention
<code>{chatid}</code>:XChat'sXID
<code>{chatname}</code>:XChatXname
<code>{chatnick}</code>:XChatXusername
XXXX"""
XXXX)


@register(cmds="wiki")
@disableable_dec("wiki")
asyncXdefXwiki(message):
XXXXargsX=Xget_args_str(message)
XXXXwikipedia.set_lang("en")
XXXXtry:
XXXXXXXXpagewikiX=Xwikipedia.page(args)
XXXXexceptXwikipedia.exceptions.PageErrorXasXe:
XXXXXXXXawaitXmessage.reply(f"NoXresultsXfound!\nError:X<code>{e}</code>")
XXXXXXXXreturn
XXXXexceptXwikipedia.exceptions.DisambiguationErrorXasXrefer:
XXXXXXXXreferX=Xstr(refer).split("\n")
XXXXXXXXifXlen(refer)X>=X6:
XXXXXXXXXXXXbatasX=X6
XXXXXXXXelse:
XXXXXXXXXXXXbatasX=Xlen(refer)
XXXXXXXXtextX=X""
XXXXXXXXforXxXinXrange(batas):
XXXXXXXXXXXXifXxX==X0:
XXXXXXXXXXXXXXXXtextX+=Xrefer[x]X+X"\n"
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXtextX+=X"-X`"X+Xrefer[x]X+X"`\n"
XXXXXXXXawaitXmessage.reply(text)
XXXXXXXXreturn
XXXXexceptXIndexError:
XXXXXXXXmsg.reply_text("WriteXaXmessageXtoXsearchXfromXwikipediaXsources.")
XXXXXXXXreturn
XXXXtitleX=Xpagewiki.title
XXXXsummaryX=Xpagewiki.summary
XXXXbuttonX=XInlineKeyboardMarkup().add(
XXXXXXXXInlineKeyboardButton("🔧XMoreXInfo...",Xurl=wikipedia.page(args).url)
XXXX)
XXXXawaitXmessage.reply(
XXXXXXXX("TheXresultXofX{}Xis:\n\n<b>{}</b>\n{}").format(args,Xtitle,Xsummary),
XXXXXXXXreply_markup=button,
XXXX)


@register(cmds="github")
@disableable_dec("github")
asyncXdefXgithub(message):
XXXXtextX=Xmessage.text[len("/githubX")X:]
XXXXresponseX=XawaitXhttp.get(f"https://api.github.com/users/{text}")
XXXXusrX=Xresponse.json()

XXXXifXusr.get("login"):
XXXXXXXXtextX=Xf"<b>Username:</b>X<aXhref='https://github.com/{usr['login']}'>{usr['login']}</a>"

XXXXXXXXwhitelistX=X[
XXXXXXXXXXXX"name",
XXXXXXXXXXXX"id",
XXXXXXXXXXXX"type",
XXXXXXXXXXXX"location",
XXXXXXXXXXXX"blog",
XXXXXXXXXXXX"bio",
XXXXXXXXXXXX"followers",
XXXXXXXXXXXX"following",
XXXXXXXXXXXX"hireable",
XXXXXXXXXXXX"public_gists",
XXXXXXXXXXXX"public_repos",
XXXXXXXXXXXX"email",
XXXXXXXXXXXX"company",
XXXXXXXXXXXX"updated_at",
XXXXXXXXXXXX"created_at",
XXXXXXXX]

XXXXXXXXdifnamesX=X{
XXXXXXXXXXXX"id":X"AccountXID",
XXXXXXXXXXXX"type":X"AccountXtype",
XXXXXXXXXXXX"created_at":X"AccountXcreatedXat",
XXXXXXXXXXXX"updated_at":X"LastXupdated",
XXXXXXXXXXXX"public_repos":X"PublicXRepos",
XXXXXXXXXXXX"public_gists":X"PublicXGists",
XXXXXXXX}

XXXXXXXXgoawayX=X[None,X0,X"null",X""]

XXXXXXXXforXx,XyXinXusr.items():
XXXXXXXXXXXXifXxXinXwhitelist:
XXXXXXXXXXXXXXXXxX=Xdifnames.get(x,Xx.title())

XXXXXXXXXXXXXXXXifXxXinX("AccountXcreatedXat",X"LastXupdated"):
XXXXXXXXXXXXXXXXXXXXyX=Xdatetime.strptime(y,X"%Y-%m-%dT%H:%M:%SZ")

XXXXXXXXXXXXXXXXifXyXnotXinXgoaway:
XXXXXXXXXXXXXXXXXXXXifXxX==X"Blog":
XXXXXXXXXXXXXXXXXXXXXXXXxX=X"Website"
XXXXXXXXXXXXXXXXXXXXXXXXyX=Xf"<aXhref='{y}'>Here!</a>"
XXXXXXXXXXXXXXXXXXXXXXXXtextX+=X"\n<b>{}:</b>X{}".format(x,Xy)
XXXXXXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXXXXXtextX+=X"\n<b>{}:</b>X<code>{}</code>".format(x,Xy)
XXXXXXXXreply_textX=Xtext
XXXXelse:
XXXXXXXXreply_textX=X"UserXnotXfound.XMakeXsureXyouXenteredXvalidXusername!"
XXXXawaitXmessage.reply(reply_text,Xdisable_web_page_preview=True)


@register(cmds="ip")
@disableable_dec("ip")
asyncXdefXip(message):
XXXXtry:
XXXXXXXXipX=Xmessage.text.split(maxsplit=1)[1]
XXXXexceptXIndexError:
XXXXXXXXawaitXmessage.reply(f"ApparentlyXyouXforgotXsomething!")
XXXXXXXXreturn

XXXXresponseX=XawaitXhttp.get(f"http://ip-api.com/json/{ip}")
XXXXifXresponse.status_codeX==X200:
XXXXXXXXlookup_jsonX=Xresponse.json()
XXXXelse:
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXf"AnXerrorXoccurredXwhenXlookingXforX<b>{ip}</b>:X<b>{response.status_code}</b>"
XXXXXXXX)
XXXXXXXXreturn

XXXXfixed_lookupX=X{}

XXXXforXkey,XvalueXinXlookup_json.items():
XXXXXXXXspecialX=X{
XXXXXXXXXXXX"lat":X"Latitude",
XXXXXXXXXXXX"lon":X"Longitude",
XXXXXXXXXXXX"isp":X"ISP",
XXXXXXXXXXXX"as":X"AS",
XXXXXXXXXXXX"asname":X"ASXname",
XXXXXXXX}
XXXXXXXXifXkeyXinXspecial:
XXXXXXXXXXXXfixed_lookup[special[key]]X=Xstr(value)
XXXXXXXXXXXXcontinue

XXXXXXXXkeyX=Xre.sub(r"([a-z])([A-Z])",Xr"\g<1>X\g<2>",Xkey)
XXXXXXXXkeyX=Xkey.capitalize()

XXXXXXXXifXnotXvalue:
XXXXXXXXXXXXvalueX=X"None"

XXXXXXXXfixed_lookup[key]X=Xstr(value)

XXXXtextX=X""

XXXXforXkey,XvalueXinXfixed_lookup.items():
XXXXXXXXtextX=XtextX+Xf"<b>{key}:</b>X<code>{value}</code>\n"

XXXXawaitXmessage.reply(text)


@register(cmds="cancel",Xstate="*",Xallow_kwargs=True)
asyncXdefXcancel_handle(message,Xstate,X**kwargs):
XXXXawaitXstate.finish()
XXXXawaitXmessage.reply("Cancelled.")


asyncXdefXdelmsg_filter_handle(message,Xchat,Xdata):
XXXXifXawaitXis_user_admin(data["chat_id"],Xmessage.from_user.id):
XXXXXXXXreturn
XXXXwithXsuppress(MessageToDeleteNotFound):
XXXXXXXXawaitXmessage.delete()


asyncXdefXreplymsg_filter_handler(message,Xchat,Xdata):
XXXXtext,XkwargsX=XawaitXt_unparse_note_item(
XXXXXXXXmessage,Xdata["reply_text"],Xchat["chat_id"]
XXXX)
XXXXkwargs["reply_to"]X=Xmessage.message_id
XXXXwithXsuppress(BadRequest):
XXXXXXXXawaitXsend_note(chat["chat_id"],Xtext,X**kwargs)


@get_strings_dec("misc")
asyncXdefXreplymsg_setup_start(message,Xstrings):
XXXXwithXsuppress(MessageNotModified):
XXXXXXXXawaitXmessage.edit_text(strings["send_text"])


asyncXdefXreplymsg_setup_finish(message,Xdata):
XXXXreply_textX=XawaitXget_parsed_note_list(
XXXXXXXXmessage,Xallow_reply_message=False,Xsplit_args=-1
XXXX)
XXXXreturnX{"reply_text":Xreply_text}


@get_strings_dec("misc")
asyncXdefXcustomise_reason_start(message:XMessage,Xstrings:Xdict):
XXXXawaitXmessage.reply(strings["send_customised_reason"])


@get_strings_dec("misc")
asyncXdefXcustomise_reason_finish(message:XMessage,X_:Xdict,Xstrings:Xdict):
XXXXifXmessage.textXisXNone:
XXXXXXXXawaitXmessage.reply(strings["expected_text"])
XXXXXXXXreturnXFalse
XXXXelifXmessage.textXinX{"None"}:
XXXXXXXXreturnX{"reason":XNone}
XXXXreturnX{"reason":Xmessage.text}


__filters__X=X{
XXXX"delete_message":X{
XXXXXXXX"title":X{"module":X"misc",X"string":X"delmsg_filter_title"},
XXXXXXXX"handle":Xdelmsg_filter_handle,
XXXXXXXX"del_btn_name":XlambdaXmsg,Xdata:Xf"DelXmessage:X{data['handler']}",
XXXX},
XXXX"reply_message":X{
XXXXXXXX"title":X{"module":X"misc",X"string":X"replymsg_filter_title"},
XXXXXXXX"handle":Xreplymsg_filter_handler,
XXXXXXXX"setup":X{"start":Xreplymsg_setup_start,X"finish":Xreplymsg_setup_finish},
XXXXXXXX"del_btn_name":XlambdaXmsg,Xdata:Xf"ReplyXtoX{data['handler']}:X\"{data['reply_text'].get('text',X'None')}\"X",
XXXX},
}
