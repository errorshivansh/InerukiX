#Copyright(C)2021errorshivansh


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


importre

importbs4
importrequests
fromtelethonimporttypes
fromtelethon.tlimportfunctions

fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbot

langi="en"


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):
returnisinstance(
(
awaittbot(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerUser):
returnTrue


@register(pattern="^/imdb(.*)")
asyncdefimdb(e):
ife.is_group:
ifawaitis_register_admin(e.input_chat,e.message.sender_id):
pass
else:
return

try:
movie_name=e.pattern_match.group(1)
remove_space=movie_name.split("")
final_name="+".join(remove_space)
page=requests.get(
"https://www.imdb.com/find?ref_=nv_sr_fn&q="+final_name+"&s=all"
)
str(page.status_code)
soup=bs4.BeautifulSoup(page.content,"lxml")
odds=soup.findAll("tr","odd")
mov_title=odds[0].findNext("td").findNext("td").text
mov_link=(
"http://www.imdb.com/"+odds[0].findNext("td").findNext("td").a["href"]
)
page1=requests.get(mov_link)
soup=bs4.BeautifulSoup(page1.content,"lxml")
ifsoup.find("div","poster"):
poster=soup.find("div","poster").img["src"]
else:
poster=""
ifsoup.find("div","title_wrapper"):
pg=soup.find("div","title_wrapper").findNext("div").text
mov_details=re.sub(r"\s+","",pg)
else:
mov_details=""
credits=soup.findAll("div","credit_summary_item")
iflen(credits)==1:
director=credits[0].a.text
writer="Notavailable"
stars="Notavailable"
eliflen(credits)>2:
director=credits[0].a.text
writer=credits[1].a.text
actors=[]
forxincredits[2].findAll("a"):
actors.append(x.text)
actors.pop()
stars=actors[0]+","+actors[1]+","+actors[2]
else:
director=credits[0].a.text
writer="Notavailable"
actors=[]
forxincredits[1].findAll("a"):
actors.append(x.text)
actors.pop()
stars=actors[0]+","+actors[1]+","+actors[2]
ifsoup.find("div","inlinecanwrap"):
story_line=soup.find("div","inlinecanwrap").findAll("p")[0].text
else:
story_line="Notavailable"
info=soup.findAll("div","txt-block")
ifinfo:
mov_country=[]
mov_language=[]
fornodeininfo:
a=node.findAll("a")
foriina:
if"country_of_origin"ini["href"]:
mov_country.append(i.text)
elif"primary_language"ini["href"]:
mov_language.append(i.text)
ifsoup.findAll("div","ratingValue"):
forrinsoup.findAll("div","ratingValue"):
mov_rating=r.strong["title"]
else:
mov_rating="Notavailable"
awaite.reply(
"<ahref="+poster+">&#8203;</a>"
"<b>Title:</b><code>"
+mov_title
+"</code>\n<code>"
+mov_details
+"</code>\n<b>Rating:</b><code>"
+mov_rating
+"</code>\n<b>Country:</b><code>"
+mov_country[0]
+"</code>\n<b>Language:</b><code>"
+mov_language[0]
+"</code>\n<b>Director:</b><code>"
+director
+"</code>\n<b>Writer:</b><code>"
+writer
+"</code>\n<b>Stars:</b><code>"
+stars
+"</code>\n<b>IMDBUrl:</b>"
+mov_link
+"\n<b>StoryLine:</b>"
+story_line,
link_preview=True,
parse_mode="HTML",
)
exceptIndexError:
awaite.reply("Pleaseenteravalidmoviename!")
