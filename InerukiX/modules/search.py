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

importXre
importXurllib
importXurllib.request

importXbs4
importXrequests
fromXbs4XimportXBeautifulSoup
fromXpyrogramXimportXfilters

#XThisXpluginXisXportedXfromXhttps://github.com/thehamkercat/WilliamButcherBot
fromXsearch_engine_parserXimportXGoogleSearch

fromXInerukiX.modules.utils.fetchXimportXfetch
fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.pyrogramXimportXpbotXasXapp

ARQX=X"https://thearq.tech/"


@app.on_message(filters.command("ud")X&X~filters.edited)
asyncXdefXurbandict(_,Xmessage):
XXXXifXlen(message.command)X<X2:
XXXXXXXXawaitXmessage.reply_text('"/ud"XNeedsXAnXArgument.')
XXXXXXXXreturn
XXXXtextX=Xmessage.text.split(None,X1)[1]
XXXXtry:
XXXXXXXXresultsX=XawaitXfetch(f"{ARQ}ud?query={text}")
XXXXXXXXreply_textX=Xf"""**Definition:**X__{results["list"][0]["definition"]}__
**Example:**X__{results["list"][0]["example"]}__"""
XXXXexceptXIndexError:
XXXXXXXXreply_textX=X"SorryXcouldXnotXfindXanyXmatchingXresults!"
XXXXignore_charsX=X"[]"
XXXXreplyX=Xreply_text
XXXXforXcharsXinXignore_chars:
XXXXXXXXreplyX=Xreply.replace(chars,X"")
XXXXifXlen(reply)X>=X4096:
XXXXXXXXreplyX=Xreply[:4096]
XXXXawaitXmessage.reply_text(reply)


#Xgoogle


@app.on_message(filters.command("google")X&X~filters.edited)
asyncXdefXgoogle(_,Xmessage):
XXXXtry:
XXXXXXXXifXlen(message.command)X<X2:
XXXXXXXXXXXXawaitXmessage.reply_text("/googleXNeedsXAnXArgument")
XXXXXXXXXXXXreturn
XXXXXXXXtextX=Xmessage.text.split(None,X1)[1]
XXXXXXXXgresultsX=XawaitXGoogleSearch().async_search(text,X1)
XXXXXXXXresultX=X""
XXXXXXXXforXiXinXrange(4):
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXtitleX=Xgresults["titles"][i].replace("\n",X"X")
XXXXXXXXXXXXXXXXsourceX=Xgresults["links"][i]
XXXXXXXXXXXXXXXXdescriptionX=Xgresults["descriptions"][i]
XXXXXXXXXXXXXXXXresultX+=Xf"[{title}]({source})\n"
XXXXXXXXXXXXXXXXresultX+=Xf"`{description}`\n\n"
XXXXXXXXXXXXexceptXIndexError:
XXXXXXXXXXXXXXXXpass
XXXXXXXXawaitXmessage.reply_text(result,Xdisable_web_page_preview=True)
XXXXexceptXExceptionXasXe:
XXXXXXXXawaitXmessage.reply_text(str(e))


#XStackOverflowX[ThisXisXalsoXaXgoogleXsearchXwithXsomeXaddedXargs]


@app.on_message(filters.command("so")X&X~filters.edited)
asyncXdefXstack(_,Xmessage):
XXXXtry:
XXXXXXXXifXlen(message.command)X<X2:
XXXXXXXXXXXXawaitXmessage.reply_text('"/so"XNeedsXAnXArgument')
XXXXXXXXXXXXreturn
XXXXXXXXgettX=Xmessage.text.split(None,X1)[1]
XXXXXXXXtextX=XgettX+X'X"site:stackoverflow.com"'
XXXXXXXXgresultsX=XawaitXGoogleSearch().async_search(text,X1)
XXXXXXXXresultX=X""
XXXXXXXXforXiXinXrange(4):
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXtitleX=Xgresults["titles"][i].replace("\n",X"X")
XXXXXXXXXXXXXXXXsourceX=Xgresults["links"][i]
XXXXXXXXXXXXXXXXdescriptionX=Xgresults["descriptions"][i]
XXXXXXXXXXXXXXXXresultX+=Xf"[{title}]({source})\n"
XXXXXXXXXXXXXXXXresultX+=Xf"`{description}`\n\n"
XXXXXXXXXXXXexceptXIndexError:
XXXXXXXXXXXXXXXXpass
XXXXXXXXawaitXmessage.reply_text(result,Xdisable_web_page_preview=True)
XXXXexceptXExceptionXasXe:
XXXXXXXXawaitXmessage.reply_text(str(e))


#XGithubX[ThisXisXalsoXaXgoogleXsearchXwithXsomeXaddedXargs]


@app.on_message(filters.command("gh")X&X~filters.edited)
asyncXdefXgithub(_,Xmessage):
XXXXtry:
XXXXXXXXifXlen(message.command)X<X2:
XXXXXXXXXXXXawaitXmessage.reply_text('"/gh"XNeedsXAnXArgument')
XXXXXXXXXXXXreturn
XXXXXXXXgettX=Xmessage.text.split(None,X1)[1]
XXXXXXXXtextX=XgettX+X'X"site:github.com"'
XXXXXXXXgresultsX=XawaitXGoogleSearch().async_search(text,X1)
XXXXXXXXresultX=X""
XXXXXXXXforXiXinXrange(4):
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXtitleX=Xgresults["titles"][i].replace("\n",X"X")
XXXXXXXXXXXXXXXXsourceX=Xgresults["links"][i]
XXXXXXXXXXXXXXXXdescriptionX=Xgresults["descriptions"][i]
XXXXXXXXXXXXXXXXresultX+=Xf"[{title}]({source})\n"
XXXXXXXXXXXXXXXXresultX+=Xf"`{description}`\n\n"
XXXXXXXXXXXXexceptXIndexError:
XXXXXXXXXXXXXXXXpass
XXXXXXXXawaitXmessage.reply_text(result,Xdisable_web_page_preview=True)
XXXXexceptXExceptionXasXe:
XXXXXXXXawaitXmessage.reply_text(str(e))


#XYouTube


@app.on_message(filters.command("yts")X&X~filters.edited)
asyncXdefXytsearch(_,Xmessage):
XXXXtry:
XXXXXXXXifXlen(message.command)X<X2:
XXXXXXXXXXXXawaitXmessage.reply_text("/ytXneedsXanXargument")
XXXXXXXXXXXXreturn
XXXXXXXXqueryX=Xmessage.text.split(None,X1)[1]
XXXXXXXXmX=XawaitXmessage.reply_text("Searching....")
XXXXXXXXresultsX=XawaitXfetch(f"{ARQ}youtube?query={query}&count=3")
XXXXXXXXiX=X0
XXXXXXXXtextX=X""
XXXXXXXXwhileXiX<X3:
XXXXXXXXXXXXtextX+=Xf"TitleX-X{results[i]['title']}\n"
XXXXXXXXXXXXtextX+=Xf"DurationX-X{results[i]['duration']}\n"
XXXXXXXXXXXXtextX+=Xf"ViewsX-X{results[i]['views']}\n"
XXXXXXXXXXXXtextX+=Xf"ChannelX-X{results[i]['channel']}\n"
XXXXXXXXXXXXtextX+=Xf"https://youtube.com{results[i]['url_suffix']}\n\n"
XXXXXXXXXXXXiX+=X1
XXXXXXXXawaitXm.edit(text,Xdisable_web_page_preview=True)
XXXXexceptXExceptionXasXe:
XXXXXXXXawaitXmessage.reply_text(str(e))


openerX=Xurllib.request.build_opener()
useragentX=X"Mozilla/5.0X(Linux;XAndroidX9;XSM-G960FXBuild/PPR1.180610.011;Xwv)XAppleWebKit/537.36X(KHTML,XlikeXGecko)XVersion/4.0XChrome/74.0.3729.157XMobileXSafari/537.36"
opener.addheadersX=X[("User-agent",Xuseragent)]


asyncXdefXParseSauce(googleurl):
XXXX"""Parse/ScrapeXtheXHTMLXcodeXforXtheXinfoXweXwant."""

XXXXsourceX=Xopener.open(googleurl).read()
XXXXsoupX=XBeautifulSoup(source,X"html.parser")

XXXXresultsX=X{"similar_images":X"",X"best_guess":X""}

XXXXtry:
XXXXXXXXforXsimilar_imageXinXsoup.findAll("input",X{"class":X"gLFyf"}):
XXXXXXXXXXXXurlX=X"https://www.google.com/search?tbm=isch&q="X+Xurllib.parse.quote_plus(
XXXXXXXXXXXXXXXXsimilar_image.get("value")
XXXXXXXXXXXX)
XXXXXXXXXXXXresults["similar_images"]X=Xurl
XXXXexceptXBaseException:
XXXXXXXXpass

XXXXforXbest_guessXinXsoup.findAll("div",Xattrs={"class":X"r5a77d"}):
XXXXXXXXresults["best_guess"]X=Xbest_guess.get_text()

XXXXreturnXresults


asyncXdefXscam(results,Xlim):

XXXXsingleX=Xopener.open(results["similar_images"]).read()
XXXXdecodedX=Xsingle.decode("utf-8")

XXXXimglinksX=X[]
XXXXcounterX=X0

XXXXpatternX=Xr"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
XXXXoboiX=Xre.findall(pattern,Xdecoded,Xre.IX|Xre.M)

XXXXforXimglinkXinXoboi:
XXXXXXXXcounterX+=X1
XXXXXXXXifXcounterX<Xint(lim):
XXXXXXXXXXXXimglinks.append(imglink)
XXXXXXXXelse:
XXXXXXXXXXXXbreak

XXXXreturnXimglinks


@register(pattern="^/appX(.*)")
asyncXdefXapk(e):
XXXXtry:
XXXXXXXXapp_nameX=Xe.pattern_match.group(1)
XXXXXXXXremove_spaceX=Xapp_name.split("X")
XXXXXXXXfinal_nameX=X"+".join(remove_space)
XXXXXXXXpageX=Xrequests.get(
XXXXXXXXXXXX"https://play.google.com/store/search?q="X+Xfinal_nameX+X"&c=apps"
XXXXXXXX)
XXXXXXXXstr(page.status_code)
XXXXXXXXsoupX=Xbs4.BeautifulSoup(page.content,X"lxml",Xfrom_encoding="utf-8")
XXXXXXXXresultsX=Xsoup.findAll("div",X"ZmHEEd")
XXXXXXXXapp_nameX=X(
XXXXXXXXXXXXresults[0].findNext("div",X"Vpfmgd").findNext("div",X"WsMG1cXnnK0zc").text
XXXXXXXX)
XXXXXXXXapp_devX=Xresults[0].findNext("div",X"Vpfmgd").findNext("div",X"KoLSrc").text
XXXXXXXXapp_dev_linkX=X(
XXXXXXXXXXXX"https://play.google.com"
XXXXXXXXXXXX+Xresults[0].findNext("div",X"Vpfmgd").findNext("a",X"mnKHRc")["href"]
XXXXXXXX)
XXXXXXXXapp_ratingX=X(
XXXXXXXXXXXXresults[0]
XXXXXXXXXXXX.findNext("div",X"Vpfmgd")
XXXXXXXXXXXX.findNext("div",X"pf5lIe")
XXXXXXXXXXXX.find("div")["aria-label"]
XXXXXXXX)
XXXXXXXXapp_linkX=X(
XXXXXXXXXXXX"https://play.google.com"
XXXXXXXXXXXX+Xresults[0]
XXXXXXXXXXXX.findNext("div",X"Vpfmgd")
XXXXXXXXXXXX.findNext("div",X"vU6FJXp63iDd")
XXXXXXXXXXXX.a["href"]
XXXXXXXX)
XXXXXXXXapp_iconX=X(
XXXXXXXXXXXXresults[0]
XXXXXXXXXXXX.findNext("div",X"Vpfmgd")
XXXXXXXXXXXX.findNext("div",X"uzcko")
XXXXXXXXXXXX.img["data-src"]
XXXXXXXX)
XXXXXXXXapp_detailsX=X"<aXhref='"X+Xapp_iconX+X"'>📲&#8203;</a>"
XXXXXXXXapp_detailsX+=X"X<b>"X+Xapp_nameX+X"</b>"
XXXXXXXXapp_detailsX+=X(
XXXXXXXXXXXX"\n\n<code>DeveloperX:</code>X<aXhref='"
XXXXXXXXXXXX+Xapp_dev_link
XXXXXXXXXXXX+X"'>"
XXXXXXXXXXXX+Xapp_dev
XXXXXXXXXXXX+X"</a>"
XXXXXXXX)
XXXXXXXXapp_detailsX+=X"\n<code>RatingX:</code>X"X+Xapp_rating.replace(
XXXXXXXXXXXX"RatedX",X"⭐X"
XXXXXXXX).replace("XoutXofX",X"/").replace("Xstars",X"",X1).replace(
XXXXXXXXXXXX"Xstars",X"⭐X"
XXXXXXXX).replace(
XXXXXXXXXXXX"five",X"5"
XXXXXXXX)
XXXXXXXXapp_detailsX+=X(
XXXXXXXXXXXX"\n<code>FeaturesX:</code>X<aXhref='"
XXXXXXXXXXXX+Xapp_link
XXXXXXXXXXXX+X"'>ViewXinXPlayXStore</a>"
XXXXXXXX)
XXXXXXXXapp_detailsX+=X"\n\n===>X@InerukiSupport_OfficialX<==="
XXXXXXXXawaitXe.reply(app_details,Xlink_preview=True,Xparse_mode="HTML")
XXXXexceptXIndexError:
XXXXXXXXawaitXe.reply("NoXresultXfoundXinXsearch.XPleaseXenterX**ValidXappXname**")
XXXXexceptXExceptionXasXerr:
XXXXXXXXawaitXe.reply("ExceptionXOccured:-X"X+Xstr(err))


__help__X=X"""
X-X/googleX<i>text</i>:XPerformXaXgoogleXsearch
X-X/soX-XSearchXForXSomethingXOnXStackXOverFlow
X-X/ghX-XSearchXForXSomethingXOnXGitHub
X-X/ytsX-XSearchXForXSomethingXOnXYouTub
X-X/appX<i>appname</i>:XSearchesXforXanXappXinXPlayXStoreXandXreturnsXitsXdetails.
"""

__mod_name__X=X"Search"
