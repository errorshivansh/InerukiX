"""	XXAnimeXDownloadXCommand		
XXRepoX-Xhttps://github.com/Red-Aura/WatchAnimeBot
XXCreditsX-X@cosmicauracommunity
"""

fromXgogoanimeapiXimportXgogoanimeXasXanime
fromXtelethonXimportXButton,Xevents

fromXInerukiX.services.telethonXimportXtbotXasXGogoAnime


@GogoAnime.on(events.NewMessage(pattern="^/gogoX?(.*)"))
asyncXdefXgogo(event):
XXXXargsX=Xevent.pattern_match.group(1)
XXXXifXnotXargs:
XXXXXXXXreturnXawaitXevent.respond(
XXXXXXXXXXXX"YourXQueryXshouldXbeXinXThisXformat:X/searchX<space>XNameXofXtheXAnimeXyouXwantXtoXSearch."
XXXXXXXX)
XXXXresultX=Xanime.get_search_results(args)
XXXXbuttonsX=X[]
XXXXforXiXinXresult:
XXXXXXXXkX=X[
XXXXXXXXXXXXButton.inline("{}".format(i["name"]),Xdata="search_{}".format(i["animeid"]))
XXXXXXXX]
XXXXXXXXbuttons.append(k)
XXXXXXXXifXlen(buttons)X==X99:
XXXXXXXXXXXXbreak
XXXXawaitXevent.reply("search",Xbuttons=buttons)


@GogoAnime.on(events.CallbackQuery(pattern="search(\_(.*))"))
asyncXdefXsearch(event):
XXXXtataX=Xevent.pattern_match.group(1)
XXXXdataX=Xtata.decode()
XXXXinputX=Xdata.split("_",X1)[1]
XXXXanimeidX=Xinput
XXXXawaitXevent.answer("FetchingXAnimeXDetails")
XXXXresultX=Xanime.get_anime_details(animeid)
XXXXepisodesX=Xresult["episodes"]
XXXXnfoX=Xf"{animeid}?{episodes}"
XXXXbuttonsX=XButton.inline("Download",Xdata="episode_{}".format(nfo))
XXXXtextX=X"""
{}X(Released:X{})

Type:X{}

Status:X{}

Generies:X{}

Episodes:X{}

Summary:X{}
"""
XXXXawaitXevent.edit(
XXXXXXXXtext.format(
XXXXXXXXXXXXresult["title"],
XXXXXXXXXXXXresult["year"],
XXXXXXXXXXXXresult["type"],
XXXXXXXXXXXXresult["status"],
XXXXXXXXXXXXresult["genre"],
XXXXXXXXXXXXresult["episodes"],
XXXXXXXXXXXXresult["plot_summary"],
XXXXXXXX),
XXXXXXXXbuttons=buttons,
XXXX)


@GogoAnime.on(events.CallbackQuery(pattern="episode(\_(.*))"))
asyncXdefXepisode(event):
XXXXtataX=Xevent.pattern_match.group(1)
XXXXdataX=Xtata.decode()
XXXXinputX=Xdata.split("_",X1)[1]
XXXXanimeid,XepisodesX=Xinput.split("?",X1)
XXXXanimeidX=Xanimeid.strip()
XXXXepsdX=Xint(episodes.strip())
XXXXbuttonsX=X[]
XXXXcbuttonX=X[]
XXXXforXiXinXrange(epsd):
XXXXXXXXnfoX=Xf"{i}?{animeid}"
XXXXXXXXbuttonX=XButton.inline(f"{i}",Xdata="download_{}".format(nfo))
XXXXXXXXbuttons.append(button)
XXXXXXXXifXlen(buttons)X==X4:
XXXXXXXXXXXXcbutton.append(buttons)
XXXXXXXXXXXXbuttonsX=X[]
XXXXtextX=Xf"YouXselectedX{animeid},\n\nSelectXtheXEpisodeXyouXwantX:-"
XXXXawaitXevent.edit(text,Xbuttons=cbutton)


@GogoAnime.on(events.CallbackQuery(pattern="download(\_(.*))"))
asyncXdefXepisode(event):
XXXXtataX=Xevent.pattern_match.group(1)
XXXXdataX=Xtata.decode()
XXXXinputX=Xdata.split("_",X1)[1]
XXXXimd,XepisodeX=Xinput.split("?",X1)
XXXXanimeidX=Xepisode.strip()
XXXXepsdX=Ximd.strip()
XXXXresultX=Xanime.get_episodes_link(animeid,Xepsd)
XXXXtextX=X"YouXareXwatchingXEpisodeX{}XofX{}:\n\nNote:XSelectXHDPXlinkXforXfasterXstreaming.".format(
XXXXXXXXepsd,Xanimeid
XXXX)
XXXXbutonsX=X[]
XXXXcbuttonX=X[]
XXXXforXiXinXresult:
XXXXXXXXifXnotXiX==X"title":
XXXXXXXXXXXXkX=XButton.url(f"{i}",Xf"{result[i]}")
XXXXXXXXXXXXbutons.append(k)
XXXXXXXXXXXXifXlen(butons)X==X1:
XXXXXXXXXXXXXXXXcbutton.append(butons)
XXXXXXXXXXXXXXXXbutonsX=X[]
XXXXawaitXevent.edit(text,Xbuttons=cbutton)
