"""	AnimeDownloadCommand		
Repo-https://github.com/Red-Aura/WatchAnimeBot
Credits-@cosmicauracommunity
"""

fromgogoanimeapiimportgogoanimeasanime
fromtelethonimportButton,events

fromIneruki.services.telethonimporttbotasGogoAnime


@GogoAnime.on(events.NewMessage(pattern="^/gogo?(.*)"))
asyncdefgogo(event):
args=event.pattern_match.group(1)
ifnotargs:
returnawaitevent.respond(
"YourQueryshouldbeinThisformat:/search<space>NameoftheAnimeyouwanttoSearch."
)
result=anime.get_search_results(args)
buttons=[]
foriinresult:
k=[
Button.inline("{}".format(i["name"]),data="search_{}".format(i["animeid"]))
]
buttons.append(k)
iflen(buttons)==99:
break
awaitevent.reply("search",buttons=buttons)


@GogoAnime.on(events.CallbackQuery(pattern="search(\_(.*))"))
asyncdefsearch(event):
tata=event.pattern_match.group(1)
data=tata.decode()
input=data.split("_",1)[1]
animeid=input
awaitevent.answer("FetchingAnimeDetails")
result=anime.get_anime_details(animeid)
episodes=result["episodes"]
nfo=f"{animeid}?{episodes}"
buttons=Button.inline("Download",data="episode_{}".format(nfo))
text="""
{}(Released:{})

Type:{}

Status:{}

Generies:{}

Episodes:{}

Summary:{}
"""
awaitevent.edit(
text.format(
result["title"],
result["year"],
result["type"],
result["status"],
result["genre"],
result["episodes"],
result["plot_summary"],
),
buttons=buttons,
)


@GogoAnime.on(events.CallbackQuery(pattern="episode(\_(.*))"))
asyncdefepisode(event):
tata=event.pattern_match.group(1)
data=tata.decode()
input=data.split("_",1)[1]
animeid,episodes=input.split("?",1)
animeid=animeid.strip()
epsd=int(episodes.strip())
buttons=[]
cbutton=[]
foriinrange(epsd):
nfo=f"{i}?{animeid}"
button=Button.inline(f"{i}",data="download_{}".format(nfo))
buttons.append(button)
iflen(buttons)==4:
cbutton.append(buttons)
buttons=[]
text=f"Youselected{animeid},\n\nSelecttheEpisodeyouwant:-"
awaitevent.edit(text,buttons=cbutton)


@GogoAnime.on(events.CallbackQuery(pattern="download(\_(.*))"))
asyncdefepisode(event):
tata=event.pattern_match.group(1)
data=tata.decode()
input=data.split("_",1)[1]
imd,episode=input.split("?",1)
animeid=episode.strip()
epsd=imd.strip()
result=anime.get_episodes_link(animeid,epsd)
text="YouarewatchingEpisode{}of{}:\n\nNote:SelectHDPlinkforfasterstreaming.".format(
epsd,animeid
)
butons=[]
cbutton=[]
foriinresult:
ifnoti=="title":
k=Button.url(f"{i}",f"{result[i]}")
butons.append(k)
iflen(butons)==1:
cbutton.append(butons)
butons=[]
awaitevent.edit(text,buttons=cbutton)
