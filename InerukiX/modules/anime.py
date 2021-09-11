#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2021HitaloSama.
#Copyright(C)2021errorshivansh
#Copyright(C)2020InukaAsith

#ThisfileispartofIneruki(TelegramBot)

#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseas
#publishedbytheFreeSoftwareFoundation,eitherversion3ofthe
#License,or(atyouroption)anylaterversion.

#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.

#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<http://www.gnu.org/licenses/>.

importhtml

importbs4
importjikanpy
importrequests
fromaiogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup
frompyrogramimportfilters

fromIneruki.decoratorimportregister
fromIneruki.services.pyrogramimportpbot

from.utils.animeimport(
airing_query,
anime_query,
character_query,
manga_query,
shorten,
t,
)
from.utils.disableimportdisableable_dec

url="https://graphql.anilist.co"


@register(cmds="airing")
@disableable_dec("airing")
asyncdefanime_airing(message):
search_str=message.text.split("",1)
iflen(search_str)==1:
awaitmessage.reply("Provideanimename!")
return

variables={"search":search_str[1]}
response=requests.post(
url,json={"query":airing_query,"variables":variables}
).json()["data"]["Media"]
ms_g=f"<b>Name</b>:<b>{response['title']['romaji']}</b>(<code>{response['title']['native']}</code>)\n<b>ID</b>:<code>{response['id']}</code>"
ifresponse["nextAiringEpisode"]:
airing_time=response["nextAiringEpisode"]["timeUntilAiring"]*1000
airing_time_final=t(airing_time)
ms_g+=f"\n<b>Episode</b>:<code>{response['nextAiringEpisode']['episode']}</code>\n<b>AiringIn</b>:<code>{airing_time_final}</code>"
else:
ms_g+=f"\n<b>Episode</b>:<code>{response['episodes']}</code>\n<b>Status</b>:<code>N/A</code>"
awaitmessage.reply(ms_g)


@register(cmds="anime")
@disableable_dec("anime")
asyncdefanime_search(message):
search=message.text.split("",1)
iflen(search)==1:
awaitmessage.reply("Provideanimename!")
return
else:
search=search[1]
variables={"search":search}
json=(
requests.post(url,json={"query":anime_query,"variables":variables})
.json()["data"]
.get("Media",None)
)
ifjson:
msg=f"<b>{json['title']['romaji']}</b>(<code>{json['title']['native']}</code>)\n<b>Type</b>:{json['format']}\n<b>Status</b>:{json['status']}\n<b>Episodes</b>:{json.get('episodes','N/A')}\n<b>Duration</b>:{json.get('duration','N/A')}PerEp.\n<b>Score</b>:{json['averageScore']}\n<b>Genres</b>:<code>"
forxinjson["genres"]:
msg+=f"{x},"
msg=msg[:-2]+"</code>\n"
msg+="<b>Studios</b>:<code>"
forxinjson["studios"]["nodes"]:
msg+=f"{x['name']},"
msg=msg[:-2]+"</code>\n"
info=json.get("siteUrl")
trailer=json.get("trailer",None)
iftrailer:
trailer_id=trailer.get("id",None)
site=trailer.get("site",None)
ifsite=="youtube":
trailer="https://youtu.be/"+trailer_id
description=(
json.get("description","N/A")
.replace("<i>","")
.replace("</i>","")
.replace("<br>","")
)
msg+=shorten(description,info)
image=info.replace("anilist.co/anime/","img.anili.st/media/")
iftrailer:
buttons=InlineKeyboardMarkup().add(
InlineKeyboardButton(text="MoreInfo",url=info),
InlineKeyboardButton(text="Trailer🎬",url=trailer),
)
else:
buttons=InlineKeyboardMarkup().add(
InlineKeyboardButton(text="MoreInfo",url=info)
)

ifimage:
try:
awaitmessage.reply_photo(image,caption=msg,reply_markup=buttons)
except:
msg+=f"[〽️]({image})"
awaitmessage.reply(msg)
else:
awaitmessage.reply(msg)


@register(cmds="character")
@disableable_dec("character")
asyncdefcharacter_search(message):
search=message.text.split("",1)
iflen(search)==1:
awaitmessage.reply("Providecharactername!")
return
search=search[1]
variables={"query":search}
json=(
requests.post(url,json={"query":character_query,"variables":variables})
.json()["data"]
.get("Character",None)
)
ifjson:
ms_g=f"<b>{json.get('name').get('full')}</b>(<code>{json.get('name').get('native')}</code>)\n"
description=(f"{json['description']}").replace("__","")
site_url=json.get("siteUrl")
ms_g+=shorten(description,site_url)
image=json.get("image",None)
ifimage:
image=image.get("large")
awaitmessage.reply_photo(image,caption=ms_g)
else:
awaitmessage.reply(ms_g)


@register(cmds="manga")
@disableable_dec("manga")
asyncdefmanga_search(message):
search=message.text.split("",1)
iflen(search)==1:
awaitmessage.reply("Providemanganame!")
return
search=search[1]
variables={"search":search}
json=(
requests.post(url,json={"query":manga_query,"variables":variables})
.json()["data"]
.get("Media",None)
)
ms_g=""
ifjson:
title,title_native=json["title"].get("romaji",False),json["title"].get(
"native",False
)
start_date,status,score=(
json["startDate"].get("year",False),
json.get("status",False),
json.get("averageScore",False),
)
iftitle:
ms_g+=f"<b>{title}</b>"
iftitle_native:
ms_g+=f"(<code>{title_native}</code>)"
ifstart_date:
ms_g+=f"\n<b>StartDate</b>-<code>{start_date}</code>"
ifstatus:
ms_g+=f"\n<b>Status</b>-<code>{status}</code>"
ifscore:
ms_g+=f"\n<b>Score</b>-<code>{score}</code>"
ms_g+="\n<b>Genres</b>-"
forxinjson.get("genres",[]):
ms_g+=f"{x},"
ms_g=ms_g[:-2]

image=json.get("bannerImage",False)
ms_g+=(
(f"\n<i>{json.get('description',None)}</i>")
.replace("<br>","")
.replace("</br>","")
)
ifimage:
try:
awaitmessage.reply_photo(image,caption=ms_g)
except:
ms_g+=f"[〽️]({image})"
awaitmessage.reply(ms_g)
else:
awaitmessage.reply(ms_g)


@register(cmds="upcoming")
@disableable_dec("upcoming")
asyncdefupcoming(message):
jikan=jikanpy.jikan.Jikan()
upcoming=jikan.top("anime",page=1,subtype="upcoming")

upcoming_list=[entry["title"]forentryinupcoming["top"]]
upcoming_message=""

forentry_numinrange(len(upcoming_list)):
ifentry_num==10:
break
upcoming_message+=f"{entry_num+1}.{upcoming_list[entry_num]}\n"

awaitmessage.reply(upcoming_message)


asyncdefsite_search(message,site:str):
args=message.text.split("",1)
more_results=True

try:
search_query=args[1]
exceptIndexError:
awaitmessage.reply("Givesomethingtosearch")
return

ifsite=="kaizoku":
search_url=f"https://animekaizoku.com/?s={search_query}"
html_text=requests.get(search_url).text
soup=bs4.BeautifulSoup(html_text,"html.parser")
search_result=soup.find_all("h2",{"class":"post-title"})

ifsearch_result:
result=f"<b>Searchresultsfor</b><code>{html.escape(search_query)}</code><b>on</b><code>AnimeKaizoku</code>:\n"
forentryinsearch_result:
post_link=entry.a["href"]
post_name=html.escape(entry.text)
result+=f"•<ahref='{post_link}'>{post_name}</a>\n"
else:
more_results=False
result=f"<b>Noresultfoundfor</b><code>{html.escape(search_query)}</code><b>on</b><code>AnimeKaizoku</code>"

elifsite=="kayo":
search_url=f"https://animekayo.com/?s={search_query}"
html_text=requests.get(search_url).text
soup=bs4.BeautifulSoup(html_text,"html.parser")
search_result=soup.find_all("h2",{"class":"title"})

result=f"<b>Searchresultsfor</b><code>{html.escape(search_query)}</code><b>on</b><code>AnimeKayo</code>:\n"
forentryinsearch_result:

ifentry.text.strip()=="NothingFound":
result=f"<b>Noresultfoundfor</b><code>{html.escape(search_query)}</code><b>on</b><code>AnimeKayo</code>"
more_results=False
break

post_link=entry.a["href"]
post_name=html.escape(entry.text.strip())
result+=f"•<ahref='{post_link}'>{post_name}</a>\n"

elifsite=="ganime":
search_url=f"https://gogoanime2.org/search/{search_query}"
html_text=requests.get(search_url).text
soup=bs4.BeautifulSoup(html_text,"html.parser")
search_result=soup.find_all("h2",{"class":"title"})

result=f"<b>Searchresultsfor</b><code>{html.escape(search_query)}</code><b>on</b><code>gogoanime</code>:\n"
forentryinsearch_result:

ifentry.text.strip()=="NothingFound":
result=f"<b>Noresultfoundfor</b><code>{html.escape(search_query)}</code><b>on</b><code>gogoanime</code>"
more_results=False
break

post_link=entry.a["href"]
post_name=html.escape(entry.text.strip())
result+=f"•<ahref='{post_link}'>{post_name}</a>\n"

buttons=InlineKeyboardMarkup().add(
InlineKeyboardButton(text="Seeallresults",url=search_url)
)

ifmore_results:
awaitmessage.reply(result,reply_markup=buttons,disable_web_page_preview=True)
else:
awaitmessage.reply(result)


@register(cmds="kaizoku")
@disableable_dec("kaizoku")
asyncdefkaizoku(message):
awaitsite_search(message,"kaizoku")


@register(cmds="kayo")
@disableable_dec("kayo")
asyncdefkayo(message):
awaitsite_search(message,"kayo")


@register(cmds="ganime")
@disableable_dec("ganime")
asyncdefkayo(message):
awaitsite_search(message,"ganime")


@pbot.on_message(filters.command("aq"))
defquote(_,message):
quote=requests.get("https://animechan.vercel.app/api/random").json()
quote=truth.get("quote")
message.reply_text(quote)


#addedganimesearchbasedongogoanime2.org

__mod_name__="Anime"

__help__="""
Getinformationaboutanime,mangaoranimecharacters.

<b>Availablecommands:</b>
-/anime(anime):returnsinformationabouttheanime.
-/character(character):returnsinformationaboutthecharacter.
-/manga(manga):returnsinformationaboutthemanga.
-/airing(anime):returnsanimeairinginfo.
-/kaizoku(anime):searchananimeonanimekaizoku.com
-/kayo(anime):searchananimeonanimekayo.com
-/ganime(anime):searchananimeongogoanime.so
-/upcoming:returnsalistofnewanimeintheupcomingseasons.
-/aq:getanimerandomquote
"""
