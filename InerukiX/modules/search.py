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
importurllib
importurllib.request

importbs4
importrequests
frombs4importBeautifulSoup
frompyrogramimportfilters

#Thispluginisportedfromhttps://github.com/thehamkercat/WilliamButcherBot
fromsearch_engine_parserimportGoogleSearch

fromIneruki.modules.utils.fetchimportfetch
fromIneruki.services.eventsimportregister
fromIneruki.services.pyrogramimportpbotasapp

ARQ="https://thearq.tech/"


@app.on_message(filters.command("ud")&~filters.edited)
asyncdefurbandict(_,message):
iflen(message.command)<2:
awaitmessage.reply_text('"/ud"NeedsAnArgument.')
return
text=message.text.split(None,1)[1]
try:
results=awaitfetch(f"{ARQ}ud?query={text}")
reply_text=f"""**Definition:**__{results["list"][0]["definition"]}__
**Example:**__{results["list"][0]["example"]}__"""
exceptIndexError:
reply_text="Sorrycouldnotfindanymatchingresults!"
ignore_chars="[]"
reply=reply_text
forcharsinignore_chars:
reply=reply.replace(chars,"")
iflen(reply)>=4096:
reply=reply[:4096]
awaitmessage.reply_text(reply)


#google


@app.on_message(filters.command("google")&~filters.edited)
asyncdefgoogle(_,message):
try:
iflen(message.command)<2:
awaitmessage.reply_text("/googleNeedsAnArgument")
return
text=message.text.split(None,1)[1]
gresults=awaitGoogleSearch().async_search(text,1)
result=""
foriinrange(4):
try:
title=gresults["titles"][i].replace("\n","")
source=gresults["links"][i]
description=gresults["descriptions"][i]
result+=f"[{title}]({source})\n"
result+=f"`{description}`\n\n"
exceptIndexError:
pass
awaitmessage.reply_text(result,disable_web_page_preview=True)
exceptExceptionase:
awaitmessage.reply_text(str(e))


#StackOverflow[Thisisalsoagooglesearchwithsomeaddedargs]


@app.on_message(filters.command("so")&~filters.edited)
asyncdefstack(_,message):
try:
iflen(message.command)<2:
awaitmessage.reply_text('"/so"NeedsAnArgument')
return
gett=message.text.split(None,1)[1]
text=gett+'"site:stackoverflow.com"'
gresults=awaitGoogleSearch().async_search(text,1)
result=""
foriinrange(4):
try:
title=gresults["titles"][i].replace("\n","")
source=gresults["links"][i]
description=gresults["descriptions"][i]
result+=f"[{title}]({source})\n"
result+=f"`{description}`\n\n"
exceptIndexError:
pass
awaitmessage.reply_text(result,disable_web_page_preview=True)
exceptExceptionase:
awaitmessage.reply_text(str(e))


#Github[Thisisalsoagooglesearchwithsomeaddedargs]


@app.on_message(filters.command("gh")&~filters.edited)
asyncdefgithub(_,message):
try:
iflen(message.command)<2:
awaitmessage.reply_text('"/gh"NeedsAnArgument')
return
gett=message.text.split(None,1)[1]
text=gett+'"site:github.com"'
gresults=awaitGoogleSearch().async_search(text,1)
result=""
foriinrange(4):
try:
title=gresults["titles"][i].replace("\n","")
source=gresults["links"][i]
description=gresults["descriptions"][i]
result+=f"[{title}]({source})\n"
result+=f"`{description}`\n\n"
exceptIndexError:
pass
awaitmessage.reply_text(result,disable_web_page_preview=True)
exceptExceptionase:
awaitmessage.reply_text(str(e))


#YouTube


@app.on_message(filters.command("yts")&~filters.edited)
asyncdefytsearch(_,message):
try:
iflen(message.command)<2:
awaitmessage.reply_text("/ytneedsanargument")
return
query=message.text.split(None,1)[1]
m=awaitmessage.reply_text("Searching....")
results=awaitfetch(f"{ARQ}youtube?query={query}&count=3")
i=0
text=""
whilei<3:
text+=f"Title-{results[i]['title']}\n"
text+=f"Duration-{results[i]['duration']}\n"
text+=f"Views-{results[i]['views']}\n"
text+=f"Channel-{results[i]['channel']}\n"
text+=f"https://youtube.com{results[i]['url_suffix']}\n\n"
i+=1
awaitm.edit(text,disable_web_page_preview=True)
exceptExceptionase:
awaitmessage.reply_text(str(e))


opener=urllib.request.build_opener()
useragent="Mozilla/5.0(Linux;Android9;SM-G960FBuild/PPR1.180610.011;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/74.0.3729.157MobileSafari/537.36"
opener.addheaders=[("User-agent",useragent)]


asyncdefParseSauce(googleurl):
"""Parse/ScrapetheHTMLcodefortheinfowewant."""

source=opener.open(googleurl).read()
soup=BeautifulSoup(source,"html.parser")

results={"similar_images":"","best_guess":""}

try:
forsimilar_imageinsoup.findAll("input",{"class":"gLFyf"}):
url="https://www.google.com/search?tbm=isch&q="+urllib.parse.quote_plus(
similar_image.get("value")
)
results["similar_images"]=url
exceptBaseException:
pass

forbest_guessinsoup.findAll("div",attrs={"class":"r5a77d"}):
results["best_guess"]=best_guess.get_text()

returnresults


asyncdefscam(results,lim):

single=opener.open(results["similar_images"]).read()
decoded=single.decode("utf-8")

imglinks=[]
counter=0

pattern=r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
oboi=re.findall(pattern,decoded,re.I|re.M)

forimglinkinoboi:
counter+=1
ifcounter<int(lim):
imglinks.append(imglink)
else:
break

returnimglinks


@register(pattern="^/app(.*)")
asyncdefapk(e):
try:
app_name=e.pattern_match.group(1)
remove_space=app_name.split("")
final_name="+".join(remove_space)
page=requests.get(
"https://play.google.com/store/search?q="+final_name+"&c=apps"
)
str(page.status_code)
soup=bs4.BeautifulSoup(page.content,"lxml",from_encoding="utf-8")
results=soup.findAll("div","ZmHEEd")
app_name=(
results[0].findNext("div","Vpfmgd").findNext("div","WsMG1cnnK0zc").text
)
app_dev=results[0].findNext("div","Vpfmgd").findNext("div","KoLSrc").text
app_dev_link=(
"https://play.google.com"
+results[0].findNext("div","Vpfmgd").findNext("a","mnKHRc")["href"]
)
app_rating=(
results[0]
.findNext("div","Vpfmgd")
.findNext("div","pf5lIe")
.find("div")["aria-label"]
)
app_link=(
"https://play.google.com"
+results[0]
.findNext("div","Vpfmgd")
.findNext("div","vU6FJp63iDd")
.a["href"]
)
app_icon=(
results[0]
.findNext("div","Vpfmgd")
.findNext("div","uzcko")
.img["data-src"]
)
app_details="<ahref='"+app_icon+"'>📲&#8203;</a>"
app_details+="<b>"+app_name+"</b>"
app_details+=(
"\n\n<code>Developer:</code><ahref='"
+app_dev_link
+"'>"
+app_dev
+"</a>"
)
app_details+="\n<code>Rating:</code>"+app_rating.replace(
"Rated","⭐"
).replace("outof","/").replace("stars","",1).replace(
"stars","⭐"
).replace(
"five","5"
)
app_details+=(
"\n<code>Features:</code><ahref='"
+app_link
+"'>ViewinPlayStore</a>"
)
app_details+="\n\n===>@InerukiSupport_Official<==="
awaite.reply(app_details,link_preview=True,parse_mode="HTML")
exceptIndexError:
awaite.reply("Noresultfoundinsearch.Pleaseenter**Validappname**")
exceptExceptionaserr:
awaite.reply("ExceptionOccured:-"+str(err))


__help__="""
-/google<i>text</i>:Performagooglesearch
-/so-SearchForSomethingOnStackOverFlow
-/gh-SearchForSomethingOnGitHub
-/yts-SearchForSomethingOnYouTub
-/app<i>appname</i>:SearchesforanappinPlayStoreandreturnsitsdetails.
"""

__mod_name__="Search"
