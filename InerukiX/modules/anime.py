#XCopyrightX(C)X2018X-X2020XMrYacha.XAllXrightsXreserved.XSourceXcodeXavailableXunderXtheXAGPL.
#XCopyrightX(C)X2021XHitaloSama.
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

importXhtml

importXbs4
importXjikanpy
importXrequests
fromXaiogram.typesXimportXInlineKeyboardButton,XInlineKeyboardMarkup
fromXpyrogramXimportXfilters

fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.pyrogramXimportXpbot

fromX.utils.animeXimportX(
XXXXairing_query,
XXXXanime_query,
XXXXcharacter_query,
XXXXmanga_query,
XXXXshorten,
XXXXt,
)
fromX.utils.disableXimportXdisableable_dec

urlX=X"https://graphql.anilist.co"


@register(cmds="airing")
@disableable_dec("airing")
asyncXdefXanime_airing(message):
XXXXsearch_strX=Xmessage.text.split("X",X1)
XXXXifXlen(search_str)X==X1:
XXXXXXXXawaitXmessage.reply("ProvideXanimeXname!")
XXXXXXXXreturn

XXXXvariablesX=X{"search":Xsearch_str[1]}
XXXXresponseX=Xrequests.post(
XXXXXXXXurl,Xjson={"query":Xairing_query,X"variables":Xvariables}
XXXX).json()["data"]["Media"]
XXXXms_gX=Xf"<b>Name</b>:X<b>{response['title']['romaji']}</b>(<code>{response['title']['native']}</code>)\n<b>ID</b>:X<code>{response['id']}</code>"
XXXXifXresponse["nextAiringEpisode"]:
XXXXXXXXairing_timeX=Xresponse["nextAiringEpisode"]["timeUntilAiring"]X*X1000
XXXXXXXXairing_time_finalX=Xt(airing_time)
XXXXXXXXms_gX+=Xf"\n<b>Episode</b>:X<code>{response['nextAiringEpisode']['episode']}</code>\n<b>AiringXIn</b>:X<code>{airing_time_final}</code>"
XXXXelse:
XXXXXXXXms_gX+=Xf"\n<b>Episode</b>:X<code>{response['episodes']}</code>\n<b>Status</b>:X<code>N/A</code>"
XXXXawaitXmessage.reply(ms_g)


@register(cmds="anime")
@disableable_dec("anime")
asyncXdefXanime_search(message):
XXXXsearchX=Xmessage.text.split("X",X1)
XXXXifXlen(search)X==X1:
XXXXXXXXawaitXmessage.reply("ProvideXanimeXname!")
XXXXXXXXreturn
XXXXelse:
XXXXXXXXsearchX=Xsearch[1]
XXXXvariablesX=X{"search":Xsearch}
XXXXjsonX=X(
XXXXXXXXrequests.post(url,Xjson={"query":Xanime_query,X"variables":Xvariables})
XXXXXXXX.json()["data"]
XXXXXXXX.get("Media",XNone)
XXXX)
XXXXifXjson:
XXXXXXXXmsgX=Xf"<b>{json['title']['romaji']}</b>(<code>{json['title']['native']}</code>)\n<b>Type</b>:X{json['format']}\n<b>Status</b>:X{json['status']}\n<b>Episodes</b>:X{json.get('episodes',X'N/A')}\n<b>Duration</b>:X{json.get('duration',X'N/A')}XPerXEp.\n<b>Score</b>:X{json['averageScore']}\n<b>Genres</b>:X<code>"
XXXXXXXXforXxXinXjson["genres"]:
XXXXXXXXXXXXmsgX+=Xf"{x},X"
XXXXXXXXmsgX=Xmsg[:-2]X+X"</code>\n"
XXXXXXXXmsgX+=X"<b>Studios</b>:X<code>"
XXXXXXXXforXxXinXjson["studios"]["nodes"]:
XXXXXXXXXXXXmsgX+=Xf"{x['name']},X"
XXXXXXXXmsgX=Xmsg[:-2]X+X"</code>\n"
XXXXXXXXinfoX=Xjson.get("siteUrl")
XXXXXXXXtrailerX=Xjson.get("trailer",XNone)
XXXXXXXXifXtrailer:
XXXXXXXXXXXXtrailer_idX=Xtrailer.get("id",XNone)
XXXXXXXXXXXXsiteX=Xtrailer.get("site",XNone)
XXXXXXXXXXXXifXsiteX==X"youtube":
XXXXXXXXXXXXXXXXtrailerX=X"https://youtu.be/"X+Xtrailer_id
XXXXXXXXdescriptionX=X(
XXXXXXXXXXXXjson.get("description",X"N/A")
XXXXXXXXXXXX.replace("<i>",X"")
XXXXXXXXXXXX.replace("</i>",X"")
XXXXXXXXXXXX.replace("<br>",X"")
XXXXXXXX)
XXXXXXXXmsgX+=Xshorten(description,Xinfo)
XXXXXXXXimageX=Xinfo.replace("anilist.co/anime/",X"img.anili.st/media/")
XXXXXXXXifXtrailer:
XXXXXXXXXXXXbuttonsX=XInlineKeyboardMarkup().add(
XXXXXXXXXXXXXXXXInlineKeyboardButton(text="MoreXInfo",Xurl=info),
XXXXXXXXXXXXXXXXInlineKeyboardButton(text="TrailerX🎬",Xurl=trailer),
XXXXXXXXXXXX)
XXXXXXXXelse:
XXXXXXXXXXXXbuttonsX=XInlineKeyboardMarkup().add(
XXXXXXXXXXXXXXXXInlineKeyboardButton(text="MoreXInfo",Xurl=info)
XXXXXXXXXXXX)

XXXXXXXXifXimage:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_photo(image,Xcaption=msg,Xreply_markup=buttons)
XXXXXXXXXXXXexcept:
XXXXXXXXXXXXXXXXmsgX+=Xf"X[〽️]({image})"
XXXXXXXXXXXXXXXXawaitXmessage.reply(msg)
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply(msg)


@register(cmds="character")
@disableable_dec("character")
asyncXdefXcharacter_search(message):
XXXXsearchX=Xmessage.text.split("X",X1)
XXXXifXlen(search)X==X1:
XXXXXXXXawaitXmessage.reply("ProvideXcharacterXname!")
XXXXXXXXreturn
XXXXsearchX=Xsearch[1]
XXXXvariablesX=X{"query":Xsearch}
XXXXjsonX=X(
XXXXXXXXrequests.post(url,Xjson={"query":Xcharacter_query,X"variables":Xvariables})
XXXXXXXX.json()["data"]
XXXXXXXX.get("Character",XNone)
XXXX)
XXXXifXjson:
XXXXXXXXms_gX=Xf"<b>{json.get('name').get('full')}</b>(<code>{json.get('name').get('native')}</code>)\n"
XXXXXXXXdescriptionX=X(f"{json['description']}").replace("__",X"")
XXXXXXXXsite_urlX=Xjson.get("siteUrl")
XXXXXXXXms_gX+=Xshorten(description,Xsite_url)
XXXXXXXXimageX=Xjson.get("image",XNone)
XXXXXXXXifXimage:
XXXXXXXXXXXXimageX=Ximage.get("large")
XXXXXXXXXXXXawaitXmessage.reply_photo(image,Xcaption=ms_g)
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply(ms_g)


@register(cmds="manga")
@disableable_dec("manga")
asyncXdefXmanga_search(message):
XXXXsearchX=Xmessage.text.split("X",X1)
XXXXifXlen(search)X==X1:
XXXXXXXXawaitXmessage.reply("ProvideXmangaXname!")
XXXXXXXXreturn
XXXXsearchX=Xsearch[1]
XXXXvariablesX=X{"search":Xsearch}
XXXXjsonX=X(
XXXXXXXXrequests.post(url,Xjson={"query":Xmanga_query,X"variables":Xvariables})
XXXXXXXX.json()["data"]
XXXXXXXX.get("Media",XNone)
XXXX)
XXXXms_gX=X""
XXXXifXjson:
XXXXXXXXtitle,Xtitle_nativeX=Xjson["title"].get("romaji",XFalse),Xjson["title"].get(
XXXXXXXXXXXX"native",XFalse
XXXXXXXX)
XXXXXXXXstart_date,Xstatus,XscoreX=X(
XXXXXXXXXXXXjson["startDate"].get("year",XFalse),
XXXXXXXXXXXXjson.get("status",XFalse),
XXXXXXXXXXXXjson.get("averageScore",XFalse),
XXXXXXXX)
XXXXXXXXifXtitle:
XXXXXXXXXXXXms_gX+=Xf"<b>{title}</b>"
XXXXXXXXXXXXifXtitle_native:
XXXXXXXXXXXXXXXXms_gX+=Xf"(<code>{title_native}</code>)"
XXXXXXXXifXstart_date:
XXXXXXXXXXXXms_gX+=Xf"\n<b>StartXDate</b>X-X<code>{start_date}</code>"
XXXXXXXXifXstatus:
XXXXXXXXXXXXms_gX+=Xf"\n<b>Status</b>X-X<code>{status}</code>"
XXXXXXXXifXscore:
XXXXXXXXXXXXms_gX+=Xf"\n<b>Score</b>X-X<code>{score}</code>"
XXXXXXXXms_gX+=X"\n<b>Genres</b>X-X"
XXXXXXXXforXxXinXjson.get("genres",X[]):
XXXXXXXXXXXXms_gX+=Xf"{x},X"
XXXXXXXXms_gX=Xms_g[:-2]

XXXXXXXXimageX=Xjson.get("bannerImage",XFalse)
XXXXXXXXms_gX+=X(
XXXXXXXXXXXX(f"\n<i>{json.get('description',XNone)}</i>")
XXXXXXXXXXXX.replace("<br>",X"")
XXXXXXXXXXXX.replace("</br>",X"")
XXXXXXXX)
XXXXXXXXifXimage:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_photo(image,Xcaption=ms_g)
XXXXXXXXXXXXexcept:
XXXXXXXXXXXXXXXXms_gX+=Xf"X[〽️]({image})"
XXXXXXXXXXXXXXXXawaitXmessage.reply(ms_g)
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply(ms_g)


@register(cmds="upcoming")
@disableable_dec("upcoming")
asyncXdefXupcoming(message):
XXXXjikanX=Xjikanpy.jikan.Jikan()
XXXXupcomingX=Xjikan.top("anime",Xpage=1,Xsubtype="upcoming")

XXXXupcoming_listX=X[entry["title"]XforXentryXinXupcoming["top"]]
XXXXupcoming_messageX=X""

XXXXforXentry_numXinXrange(len(upcoming_list)):
XXXXXXXXifXentry_numX==X10:
XXXXXXXXXXXXbreak
XXXXXXXXupcoming_messageX+=Xf"{entry_numX+X1}.X{upcoming_list[entry_num]}\n"

XXXXawaitXmessage.reply(upcoming_message)


asyncXdefXsite_search(message,Xsite:Xstr):
XXXXargsX=Xmessage.text.split("X",X1)
XXXXmore_resultsX=XTrue

XXXXtry:
XXXXXXXXsearch_queryX=Xargs[1]
XXXXexceptXIndexError:
XXXXXXXXawaitXmessage.reply("GiveXsomethingXtoXsearch")
XXXXXXXXreturn

XXXXifXsiteX==X"kaizoku":
XXXXXXXXsearch_urlX=Xf"https://animekaizoku.com/?s={search_query}"
XXXXXXXXhtml_textX=Xrequests.get(search_url).text
XXXXXXXXsoupX=Xbs4.BeautifulSoup(html_text,X"html.parser")
XXXXXXXXsearch_resultX=Xsoup.find_all("h2",X{"class":X"post-title"})

XXXXXXXXifXsearch_result:
XXXXXXXXXXXXresultX=Xf"<b>SearchXresultsXfor</b>X<code>{html.escape(search_query)}</code>X<b>on</b>X<code>AnimeKaizoku</code>:X\n"
XXXXXXXXXXXXforXentryXinXsearch_result:
XXXXXXXXXXXXXXXXpost_linkX=Xentry.a["href"]
XXXXXXXXXXXXXXXXpost_nameX=Xhtml.escape(entry.text)
XXXXXXXXXXXXXXXXresultX+=Xf"•X<aXhref='{post_link}'>{post_name}</a>\n"
XXXXXXXXelse:
XXXXXXXXXXXXmore_resultsX=XFalse
XXXXXXXXXXXXresultX=Xf"<b>NoXresultXfoundXfor</b>X<code>{html.escape(search_query)}</code>X<b>on</b>X<code>AnimeKaizoku</code>"

XXXXelifXsiteX==X"kayo":
XXXXXXXXsearch_urlX=Xf"https://animekayo.com/?s={search_query}"
XXXXXXXXhtml_textX=Xrequests.get(search_url).text
XXXXXXXXsoupX=Xbs4.BeautifulSoup(html_text,X"html.parser")
XXXXXXXXsearch_resultX=Xsoup.find_all("h2",X{"class":X"title"})

XXXXXXXXresultX=Xf"<b>SearchXresultsXfor</b>X<code>{html.escape(search_query)}</code>X<b>on</b>X<code>AnimeKayo</code>:X\n"
XXXXXXXXforXentryXinXsearch_result:

XXXXXXXXXXXXifXentry.text.strip()X==X"NothingXFound":
XXXXXXXXXXXXXXXXresultX=Xf"<b>NoXresultXfoundXfor</b>X<code>{html.escape(search_query)}</code>X<b>on</b>X<code>AnimeKayo</code>"
XXXXXXXXXXXXXXXXmore_resultsX=XFalse
XXXXXXXXXXXXXXXXbreak

XXXXXXXXXXXXpost_linkX=Xentry.a["href"]
XXXXXXXXXXXXpost_nameX=Xhtml.escape(entry.text.strip())
XXXXXXXXXXXXresultX+=Xf"•X<aXhref='{post_link}'>{post_name}</a>\n"

XXXXelifXsiteX==X"ganime":
XXXXXXXXsearch_urlX=Xf"https://gogoanime2.org/search/{search_query}"
XXXXXXXXhtml_textX=Xrequests.get(search_url).text
XXXXXXXXsoupX=Xbs4.BeautifulSoup(html_text,X"html.parser")
XXXXXXXXsearch_resultX=Xsoup.find_all("h2",X{"class":X"title"})

XXXXXXXXresultX=Xf"<b>SearchXresultsXfor</b>X<code>{html.escape(search_query)}</code>X<b>on</b>X<code>gogoanime</code>:X\n"
XXXXXXXXforXentryXinXsearch_result:

XXXXXXXXXXXXifXentry.text.strip()X==X"NothingXFound":
XXXXXXXXXXXXXXXXresultX=Xf"<b>NoXresultXfoundXfor</b>X<code>{html.escape(search_query)}</code>X<b>on</b>X<code>gogoanime</code>"
XXXXXXXXXXXXXXXXmore_resultsX=XFalse
XXXXXXXXXXXXXXXXbreak

XXXXXXXXXXXXpost_linkX=Xentry.a["href"]
XXXXXXXXXXXXpost_nameX=Xhtml.escape(entry.text.strip())
XXXXXXXXXXXXresultX+=Xf"•X<aXhref='{post_link}'>{post_name}</a>\n"

XXXXbuttonsX=XInlineKeyboardMarkup().add(
XXXXXXXXInlineKeyboardButton(text="SeeXallXresults",Xurl=search_url)
XXXX)

XXXXifXmore_results:
XXXXXXXXawaitXmessage.reply(result,Xreply_markup=buttons,Xdisable_web_page_preview=True)
XXXXelse:
XXXXXXXXawaitXmessage.reply(result)


@register(cmds="kaizoku")
@disableable_dec("kaizoku")
asyncXdefXkaizoku(message):
XXXXawaitXsite_search(message,X"kaizoku")


@register(cmds="kayo")
@disableable_dec("kayo")
asyncXdefXkayo(message):
XXXXawaitXsite_search(message,X"kayo")


@register(cmds="ganime")
@disableable_dec("ganime")
asyncXdefXkayo(message):
XXXXawaitXsite_search(message,X"ganime")


@pbot.on_message(filters.command("aq"))
defXquote(_,Xmessage):
XXXXquoteX=Xrequests.get("https://animechan.vercel.app/api/random").json()
XXXXquoteX=Xtruth.get("quote")
XXXXmessage.reply_text(quote)


#XaddedXganimeXsearchXbasedXonXgogoanime2.org

__mod_name__X=X"Anime"

__help__X=X"""
GetXinformationXaboutXanime,XmangaXorXanimeXcharacters.

<b>AvailableXcommands:</b>
-X/animeX(anime):XreturnsXinformationXaboutXtheXanime.
-X/characterX(character):XreturnsXinformationXaboutXtheXcharacter.
-X/mangaX(manga):XreturnsXinformationXaboutXtheXmanga.
-X/airingX(anime):XreturnsXanimeXairingXinfo.
-X/kaizokuX(anime):XsearchXanXanimeXonXanimekaizoku.com
-X/kayoX(anime):XsearchXanXanimeXonXanimekayo.com
-X/ganimeX(anime):XsearchXanXanimeXonXgogoanime.so
-X/upcoming:XreturnsXaXlistXofXnewXanimeXinXtheXupcomingXseasons.
-X/aqX:XgetXanimeXrandomXquote
"""
