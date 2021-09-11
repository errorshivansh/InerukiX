#Portedfromhttps://github.com/TheHamkerCat/WilliamButcherBot
"""
MITLicense
Copyright(c)2021TheHamkerCat
Permissionisherebygranted,freeofcharge,toanypersonobtainingacopy
ofthissoftwareandassociateddocumentationfiles(the"Software"),todeal
intheSoftwarewithoutrestriction,includingwithoutlimitationtherights
touse,copy,modify,merge,publish,distribute,sublicense,and/orsell
copiesoftheSoftware,andtopermitpersonstowhomtheSoftwareis
furnishedtodoso,subjecttothefollowingconditions:
Theabovecopyrightnoticeandthispermissionnoticeshallbeincludedinall
copiesorsubstantialportionsoftheSoftware.
THESOFTWAREISPROVIDED"ASIS",WITHOUTWARRANTYOFANYKIND,EPRESSOR
IMPLIED,INCLUDINGBUTNOTLIMITEDTOTHEWARRANTIESOFMERCHANTABILITY,
FITNESSFORAPARTICULARPURPOSEANDNONINFRINGEMENT.INNOEVENTSHALLTHE
AUTHORSORCOPYRIGHTHOLDERSBELIABLEFORANYCLAIM,DAMAGESOROTHER
LIABILITY,WHETHERINANACTIONOFCONTRACT,TORTOROTHERWISE,ARISINGFROM,
OUTOFORINCONNECTIONWITHTHESOFTWAREORTHEUSEOROTHERDEALINGSINTHE
SOFTWARE.
"""

importjson
importsys
fromrandomimportrandint
fromtimeimporttime

importaiohttp
fromaiohttpimportClientSession
fromgoogletransimportTranslator
frommotorimportversionasmongover
frompykeyboardimportInlineKeyboard
frompyrogramimport__version__aspyrover
frompyrogram.raw.functionsimportPing
frompyrogram.typesimport(
InlineKeyboardButton,
InlineQueryResultArticle,
InlineQueryResultPhoto,
InputTextMessageContent,
)
fromPython_ARQimportARQ
fromsearch_engine_parserimportGoogleSearch

fromInerukiimportBOT_USERNAME,OWNER_ID
fromIneruki.configimportget_str_key
fromIneruki.function.pluginhelpersimportconvert_seconds_to_minutesastime_convert
fromIneruki.function.pluginhelpersimportfetch
fromIneruki.services.pyrogramimportpbot

ARQ_API=get_str_key("ARQ_API",required=True)
ARQ_API_KEY=ARQ_API
SUDOERS=OWNER_ID
ARQ_API_URL="https://thearq.tech"

#AiohttpClient
print("[INFO]:INITIALZINGAIOHTTPSESSION")
aiohttpsession=ClientSession()
#ARQClient
print("[INFO]:INITIALIZINGARQCLIENT")
arq=ARQ(ARQ_API_URL,ARQ_API_KEY,aiohttpsession)

app=pbot
importsocket


asyncdef_netcat(host,port,content):
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,int(port)))
s.sendall(content.encode())
s.shutdown(socket.SHUT_WR)
whileTrue:
data=s.recv(4096).decode("utf-8").strip("\n\x00")
ifnotdata:
break
returndata
s.close()


asyncdefpaste(content):
link=await_netcat("ezup.dev",9999,content)
returnlink


asyncdefinline_help_func(__HELP__):
buttons=InlineKeyboard(row_width=2)
buttons.add(
InlineKeyboardButton("GetMoreHelp.",url=f"t.me/{BOT_USERNAME}?start=start"),
InlineKeyboardButton("GoInline!",switch_inline_query_current_chat=""),
)
answerss=[
InlineQueryResultArticle(
title="InlineCommands",
description="HelpRelatedToInlineUsage.",
input_message_content=InputTextMessageContent(__HELP__),
thumb_url="https://telegra.ph/file/109e8fe98acc6d262b7c6.jpg",
reply_markup=buttons,
)
]
answerss=awaitalive_function(answerss)
returnanswerss


asyncdefalive_function(answers):
buttons=InlineKeyboard(row_width=2)
bot_state="Dead"ifnotawaitapp.get_me()else"Alive"
#ubot_state='Dead'ifnotawaitapp2.get_me()else'Alive'
buttons.add(
InlineKeyboardButton("MainBot",url="https://t.me/Inerukibot"),
InlineKeyboardButton("GoInline!",switch_inline_query_current_chat=""),
)

msg=f"""
**[Ineruki✨](https://github.com/errorshivansh):**
**MainBot:**`{bot_state}`
**UserBot:**`Alive`
**Python:**`3.9`
**Pyrogram:**`{pyrover}`
**MongoDB:**`{mongover}`
**Platform:**`{sys.platform}`
**Profiles:**[BOT](t.me/{BOT_USERNAME})|[UBOT](t.me/Inerukixhelper)
"""
answers.append(
InlineQueryResultArticle(
title="Alive",
description="CheckBot'sStats",
thumb_url="https://telegra.ph/file/debc179305d2e1f140636.jpg",
input_message_content=InputTextMessageContent(
msg,disable_web_page_preview=True
),
reply_markup=buttons,
)
)
returnanswers


asyncdefwebss(url):
start_time=time()
if"."notinurl:
return
screenshot=awaitfetch(f"https://patheticprogrammers.cf/ss?site={url}")
end_time=time()
#m=awaitapp.send_photo(LOG_GROUP_ID,photo=screenshot["url"])
awaitm.delete()
a=[]
pic=InlineQueryResultPhoto(
photo_url=screenshot["url"],
caption=(f"`{url}`\n__Took{round(end_time-start_time)}Seconds.__"),
)
a.append(pic)
returna


asyncdeftranslate_func(answers,lang,tex):
i=Translator().translate(tex,dest=lang)
msg=f"""
__**Translatedfrom{i.src}to{lang}**__

**INPUT:**
{tex}

**OUTPUT:**
{i.text}"""
answers.extend(
[
InlineQueryResultArticle(
title=f"Translatedfrom{i.src}to{lang}.",
description=i.text,
input_message_content=InputTextMessageContent(msg),
),
InlineQueryResultArticle(
title=i.text,input_message_content=InputTextMessageContent(i.text)
),
]
)
returnanswers


asyncdefurban_func(answers,text):
results=awaitarq.urbandict(text)
ifnotresults.ok:
answers.append(
InlineQueryResultArticle(
title="Error",
description=results.result,
input_message_content=InputTextMessageContent(results.result),
)
)
returnanswers
results=results.result
limit=0
foriinresults:
iflimit>48:
break
limit+=1
msg=f"""
**Query:**{text}

**Definition:**__{i.definition}__

**Example:**__{i.example}__"""

answers.append(
InlineQueryResultArticle(
title=i.word,
description=i.definition,
input_message_content=InputTextMessageContent(msg),
)
)
returnanswers


asyncdefgoogle_search_func(answers,text):
gresults=awaitGoogleSearch().async_search(text)
limit=0
foriingresults:
iflimit>48:
break
limit+=1

try:
msg=f"""
[{i['titles']}]({i['links']})
{i['descriptions']}"""

answers.append(
InlineQueryResultArticle(
title=i["titles"],
description=i["descriptions"],
input_message_content=InputTextMessageContent(
msg,disable_web_page_preview=True
),
)
)
exceptKeyError:
pass
returnanswers


asyncdefwall_func(answers,text):
results=awaitarq.wall(text)
ifnotresults.ok:
answers.append(
InlineQueryResultArticle(
title="Error",
description=results.result,
input_message_content=InputTextMessageContent(results.result),
)
)
returnanswers
limit=0
results=results.result
foriinresults:
iflimit>48:
break
limit+=1
answers.append(
InlineQueryResultPhoto(
photo_url=i.url_image,
thumb_url=i.url_thumb,
caption=f"[Source]({i.url_image})",
)
)
returnanswers


asyncdefsaavn_func(answers,text):
buttons_list=[]
results=awaitarq.saavn(text)
ifnotresults.ok:
answers.append(
InlineQueryResultArticle(
title="Error",
description=results.result,
input_message_content=InputTextMessageContent(results.result),
)
)
returnanswers
results=results.result
forcount,iinenumerate(results):
buttons=InlineKeyboard(row_width=1)
buttons.add(InlineKeyboardButton("Download|Play",url=i.media_url))
buttons_list.append(buttons)
duration=awaittime_convert(i.duration)
caption=f"""
**Title:**{i.song}
**Album:**{i.album}
**Duration:**{duration}
**Release:**{i.year}
**Singers:**{i.singers}"""
description=f"{i.album}|{duration}"+f"|{i.singers}({i.year})"
answers.append(
InlineQueryResultArticle(
title=i.song,
input_message_content=InputTextMessageContent(
caption,disable_web_page_preview=True
),
description=description,
thumb_url=i.image,
reply_markup=buttons_list[count],
)
)
returnanswers


asyncdefpaste_func(answers,text):
start_time=time()
url=awaitpaste(text)
msg=f"__**{url}**__"
end_time=time()
answers.append(
InlineQueryResultArticle(
title=f"PastedIn{round(end_time-start_time)}Seconds.",
description=url,
input_message_content=InputTextMessageContent(msg),
)
)
returnanswers


asyncdefdeezer_func(answers,text):
buttons_list=[]
results=awaitarq.deezer(text,5)
ifnotresults.ok:
answers.append(
InlineQueryResultArticle(
title="Error",
description=results.result,
input_message_content=InputTextMessageContent(results.result),
)
)
returnanswers
results=results.result
forcount,iinenumerate(results):
buttons=InlineKeyboard(row_width=1)
buttons.add(InlineKeyboardButton("Download|Play",url=i.url))
buttons_list.append(buttons)
duration=awaittime_convert(i.duration)
caption=f"""
**Title:**{i.title}
**Artist:**{i.artist}
**Duration:**{duration}
**Source:**[Deezer]({i.source})"""
description=f"{i.artist}|{duration}"
answers.append(
InlineQueryResultArticle(
title=i.title,
thumb_url=i.thumbnail,
description=description,
input_message_content=InputTextMessageContent(
caption,disable_web_page_preview=True
),
reply_markup=buttons_list[count],
)
)
returnanswers


#Usedmyapikeyhere,don'tfuckwithit
asyncdefshortify(url):
if"."notinurl:
return
header={
"Authorization":"Bearerad39983fa42d0b19e4534f33671629a4940298dc",
"Content-Type":"application/json",
}
payload={"long_url":f"{url}"}
payload=json.dumps(payload)
asyncwithaiohttp.ClientSession()assession:
asyncwithsession.post(
"https://api-ssl.bitly.com/v4/shorten",headers=header,data=payload
)asresp:
data=awaitresp.json()
msg=data["link"]
a=[]
b=InlineQueryResultArticle(
title="LinkShortened!",
description=data["link"],
input_message_content=InputTextMessageContent(
msg,disable_web_page_preview=True
),
)
a.append(b)
returna


asyncdeftorrent_func(answers,text):
results=awaitarq.torrent(text)
ifnotresults.ok:
answers.append(
InlineQueryResultArticle(
title="Error",
description=results.result,
input_message_content=InputTextMessageContent(results.result),
)
)
returnanswers
limit=0
results=results.result
foriinresults:
iflimit>48:
break
title=i.name
size=i.size
seeds=i.seeds
leechs=i.leechs
upload_date=i.uploaded+"Ago"
magnet=i.magnet
caption=f"""
**Title:**__{title}__
**Size:**__{size}__
**Seeds:**__{seeds}__
**Leechs:**__{leechs}__
**Uploaded:**__{upload_date}__
**Magnet:**`{magnet}`"""

description=f"{size}|{upload_date}|Seeds:{seeds}"
answers.append(
InlineQueryResultArticle(
title=title,
description=description,
input_message_content=InputTextMessageContent(
caption,disable_web_page_preview=True
),
)
)
limit+=1
returnanswers


asyncdefwiki_func(answers,text):
data=awaitarq.wiki(text)
ifnotdata.ok:
answers.append(
InlineQueryResultArticle(
title="Error",
description=data.result,
input_message_content=InputTextMessageContent(data.result),
)
)
returnanswers
data=data.result
msg=f"""
**QUERY:**
{data.title}

**ANSWER:**
__{data.answer}__"""
answers.append(
InlineQueryResultArticle(
title=data.title,
description=data.answer,
input_message_content=InputTextMessageContent(msg),
)
)
returnanswers


asyncdefping_func(answers):
t1=time()
ping=Ping(ping_id=randint(696969,6969696))
awaitapp.send(ping)
t2=time()
ping=f"{str(round((t2-t1),2))}Seconds"
answers.append(
InlineQueryResultArticle(
title=ping,input_message_content=InputTextMessageContent(f"__**{ping}**__")
)
)
returnanswers


asyncdefpokedexinfo(answers,pokemon):
Pokemon=f"https://some-random-api.ml/pokedex?pokemon={pokemon}"
result=awaitfetch(Pokemon)
buttons=InlineKeyboard(row_width=1)
buttons.add(
InlineKeyboardButton("Pokedex",switch_inline_query_current_chat="pokedex")
)
caption=f"""
**Pokemon:**`{result['name']}`
**Pokedex:**`{result['id']}`
**Type:**`{result['type']}`
**Abilities:**`{result['abilities']}`
**Height:**`{result['height']}`
**Weight:**`{result['weight']}`
**Gender:**`{result['gender']}`
**Stats:**`{result['stats']}`
**Description:**`{result['description']}`"""
answers.append(
InlineQueryResultPhoto(
photo_url=f"https://img.pokemondb.net/artwork/large/{pokemon}.jpg",
title=result["name"],
description=result["description"],
caption=caption,
reply_markup=buttons,
)
)
returnanswers
