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

importXbs4
importXrequests
fromXtelethonXimportXtypes
fromXtelethon.tlXimportXfunctions

fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbot

langiX=X"en"


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXtbot(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXifXisinstance(chat,Xtypes.InputPeerUser):
XXXXXXXXreturnXTrue


@register(pattern="^/imdbX(.*)")
asyncXdefXimdb(e):
XXXXifXe.is_group:
XXXXXXXXifXawaitXis_register_admin(e.input_chat,Xe.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn

XXXXtry:
XXXXXXXXmovie_nameX=Xe.pattern_match.group(1)
XXXXXXXXremove_spaceX=Xmovie_name.split("X")
XXXXXXXXfinal_nameX=X"+".join(remove_space)
XXXXXXXXpageX=Xrequests.get(
XXXXXXXXXXXX"https://www.imdb.com/find?ref_=nv_sr_fn&q="X+Xfinal_nameX+X"&s=all"
XXXXXXXX)
XXXXXXXXstr(page.status_code)
XXXXXXXXsoupX=Xbs4.BeautifulSoup(page.content,X"lxml")
XXXXXXXXoddsX=Xsoup.findAll("tr",X"odd")
XXXXXXXXmov_titleX=Xodds[0].findNext("td").findNext("td").text
XXXXXXXXmov_linkX=X(
XXXXXXXXXXXX"http://www.imdb.com/"X+Xodds[0].findNext("td").findNext("td").a["href"]
XXXXXXXX)
XXXXXXXXpage1X=Xrequests.get(mov_link)
XXXXXXXXsoupX=Xbs4.BeautifulSoup(page1.content,X"lxml")
XXXXXXXXifXsoup.find("div",X"poster"):
XXXXXXXXXXXXposterX=Xsoup.find("div",X"poster").img["src"]
XXXXXXXXelse:
XXXXXXXXXXXXposterX=X""
XXXXXXXXifXsoup.find("div",X"title_wrapper"):
XXXXXXXXXXXXpgX=Xsoup.find("div",X"title_wrapper").findNext("div").text
XXXXXXXXXXXXmov_detailsX=Xre.sub(r"\s+",X"X",Xpg)
XXXXXXXXelse:
XXXXXXXXXXXXmov_detailsX=X""
XXXXXXXXcreditsX=Xsoup.findAll("div",X"credit_summary_item")
XXXXXXXXifXlen(credits)X==X1:
XXXXXXXXXXXXdirectorX=Xcredits[0].a.text
XXXXXXXXXXXXwriterX=X"NotXavailable"
XXXXXXXXXXXXstarsX=X"NotXavailable"
XXXXXXXXelifXlen(credits)X>X2:
XXXXXXXXXXXXdirectorX=Xcredits[0].a.text
XXXXXXXXXXXXwriterX=Xcredits[1].a.text
XXXXXXXXXXXXactorsX=X[]
XXXXXXXXXXXXforXxXinXcredits[2].findAll("a"):
XXXXXXXXXXXXXXXXactors.append(x.text)
XXXXXXXXXXXXactors.pop()
XXXXXXXXXXXXstarsX=Xactors[0]X+X","X+Xactors[1]X+X","X+Xactors[2]
XXXXXXXXelse:
XXXXXXXXXXXXdirectorX=Xcredits[0].a.text
XXXXXXXXXXXXwriterX=X"NotXavailable"
XXXXXXXXXXXXactorsX=X[]
XXXXXXXXXXXXforXxXinXcredits[1].findAll("a"):
XXXXXXXXXXXXXXXXactors.append(x.text)
XXXXXXXXXXXXactors.pop()
XXXXXXXXXXXXstarsX=Xactors[0]X+X","X+Xactors[1]X+X","X+Xactors[2]
XXXXXXXXifXsoup.find("div",X"inlineXcanwrap"):
XXXXXXXXXXXXstory_lineX=Xsoup.find("div",X"inlineXcanwrap").findAll("p")[0].text
XXXXXXXXelse:
XXXXXXXXXXXXstory_lineX=X"NotXavailable"
XXXXXXXXinfoX=Xsoup.findAll("div",X"txt-block")
XXXXXXXXifXinfo:
XXXXXXXXXXXXmov_countryX=X[]
XXXXXXXXXXXXmov_languageX=X[]
XXXXXXXXXXXXforXnodeXinXinfo:
XXXXXXXXXXXXXXXXaX=Xnode.findAll("a")
XXXXXXXXXXXXXXXXforXiXinXa:
XXXXXXXXXXXXXXXXXXXXifX"country_of_origin"XinXi["href"]:
XXXXXXXXXXXXXXXXXXXXXXXXmov_country.append(i.text)
XXXXXXXXXXXXXXXXXXXXelifX"primary_language"XinXi["href"]:
XXXXXXXXXXXXXXXXXXXXXXXXmov_language.append(i.text)
XXXXXXXXifXsoup.findAll("div",X"ratingValue"):
XXXXXXXXXXXXforXrXinXsoup.findAll("div",X"ratingValue"):
XXXXXXXXXXXXXXXXmov_ratingX=Xr.strong["title"]
XXXXXXXXelse:
XXXXXXXXXXXXmov_ratingX=X"NotXavailable"
XXXXXXXXawaitXe.reply(
XXXXXXXXXXXX"<aXhref="X+XposterX+X">&#8203;</a>"
XXXXXXXXXXXX"<b>TitleX:X</b><code>"
XXXXXXXXXXXX+Xmov_title
XXXXXXXXXXXX+X"</code>\n<code>"
XXXXXXXXXXXX+Xmov_details
XXXXXXXXXXXX+X"</code>\n<b>RatingX:X</b><code>"
XXXXXXXXXXXX+Xmov_rating
XXXXXXXXXXXX+X"</code>\n<b>CountryX:X</b><code>"
XXXXXXXXXXXX+Xmov_country[0]
XXXXXXXXXXXX+X"</code>\n<b>LanguageX:X</b><code>"
XXXXXXXXXXXX+Xmov_language[0]
XXXXXXXXXXXX+X"</code>\n<b>DirectorX:X</b><code>"
XXXXXXXXXXXX+Xdirector
XXXXXXXXXXXX+X"</code>\n<b>WriterX:X</b><code>"
XXXXXXXXXXXX+Xwriter
XXXXXXXXXXXX+X"</code>\n<b>StarsX:X</b><code>"
XXXXXXXXXXXX+Xstars
XXXXXXXXXXXX+X"</code>\n<b>IMDBXUrlX:X</b>"
XXXXXXXXXXXX+Xmov_link
XXXXXXXXXXXX+X"\n<b>StoryXLineX:X</b>"
XXXXXXXXXXXX+Xstory_line,
XXXXXXXXXXXXlink_preview=True,
XXXXXXXXXXXXparse_mode="HTML",
XXXXXXXX)
XXXXexceptXIndexError:
XXXXXXXXawaitXe.reply("PleaseXenterXaXvalidXmovieXnameX!")
