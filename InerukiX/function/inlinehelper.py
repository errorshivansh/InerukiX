#XPortedXfromXhttps://github.com/TheHamkerCat/WilliamButcherBot
"""
MITXLicense
CopyrightX(c)X2021XTheHamkerCat
PermissionXisXherebyXgranted,XfreeXofXcharge,XtoXanyXpersonXobtainingXaXcopy
ofXthisXsoftwareXandXassociatedXdocumentationXfilesX(theX"Software"),XtoXdeal
inXtheXSoftwareXwithoutXrestriction,XincludingXwithoutXlimitationXtheXrights
toXuse,Xcopy,Xmodify,Xmerge,Xpublish,Xdistribute,Xsublicense,Xand/orXsell
copiesXofXtheXSoftware,XandXtoXpermitXpersonsXtoXwhomXtheXSoftwareXis
furnishedXtoXdoXso,XsubjectXtoXtheXfollowingXconditions:
TheXaboveXcopyrightXnoticeXandXthisXpermissionXnoticeXshallXbeXincludedXinXall
copiesXorXsubstantialXportionsXofXtheXSoftware.
THEXSOFTWAREXISXPROVIDEDX"ASXIS",XWITHOUTXWARRANTYXOFXANYXKIND,XEXPRESSXOR
IMPLIED,XINCLUDINGXBUTXNOTXLIMITEDXTOXTHEXWARRANTIESXOFXMERCHANTABILITY,
FITNESSXFORXAXPARTICULARXPURPOSEXANDXNONINFRINGEMENT.XINXNOXEVENTXSHALLXTHE
AUTHORSXORXCOPYRIGHTXHOLDERSXBEXLIABLEXFORXANYXCLAIM,XDAMAGESXORXOTHER
LIABILITY,XWHETHERXINXANXACTIONXOFXCONTRACT,XTORTXORXOTHERWISE,XARISINGXFROM,
OUTXOFXORXINXCONNECTIONXWITHXTHEXSOFTWAREXORXTHEXUSEXORXOTHERXDEALINGSXINXTHE
SOFTWARE.
"""

importXjson
importXsys
fromXrandomXimportXrandint
fromXtimeXimportXtime

importXaiohttp
fromXaiohttpXimportXClientSession
fromXgoogletransXimportXTranslator
fromXmotorXimportXversionXasXmongover
fromXpykeyboardXimportXInlineKeyboard
fromXpyrogramXimportX__version__XasXpyrover
fromXpyrogram.raw.functionsXimportXPing
fromXpyrogram.typesXimportX(
XXXXInlineKeyboardButton,
XXXXInlineQueryResultArticle,
XXXXInlineQueryResultPhoto,
XXXXInputTextMessageContent,
)
fromXPython_ARQXimportXARQ
fromXsearch_engine_parserXimportXGoogleSearch

fromXInerukiXXimportXBOT_USERNAME,XOWNER_ID
fromXInerukiX.configXimportXget_str_key
fromXInerukiX.function.pluginhelpersXimportXconvert_seconds_to_minutesXasXtime_convert
fromXInerukiX.function.pluginhelpersXimportXfetch
fromXInerukiX.services.pyrogramXimportXpbot

ARQ_APIX=Xget_str_key("ARQ_API",Xrequired=True)
ARQ_API_KEYX=XARQ_API
SUDOERSX=XOWNER_ID
ARQ_API_URLX=X"https://thearq.tech"

#XAiohttpXClient
print("[INFO]:XINITIALZINGXAIOHTTPXSESSION")
aiohttpsessionX=XClientSession()
#XARQXClient
print("[INFO]:XINITIALIZINGXARQXCLIENT")
arqX=XARQ(ARQ_API_URL,XARQ_API_KEY,Xaiohttpsession)

appX=Xpbot
importXsocket


asyncXdefX_netcat(host,Xport,Xcontent):
XXXXsX=Xsocket.socket(socket.AF_INET,Xsocket.SOCK_STREAM)
XXXXs.connect((host,Xint(port)))
XXXXs.sendall(content.encode())
XXXXs.shutdown(socket.SHUT_WR)
XXXXwhileXTrue:
XXXXXXXXdataX=Xs.recv(4096).decode("utf-8").strip("\n\x00")
XXXXXXXXifXnotXdata:
XXXXXXXXXXXXbreak
XXXXXXXXreturnXdata
XXXXs.close()


asyncXdefXpaste(content):
XXXXlinkX=XawaitX_netcat("ezup.dev",X9999,Xcontent)
XXXXreturnXlink


asyncXdefXinline_help_func(__HELP__):
XXXXbuttonsX=XInlineKeyboard(row_width=2)
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton("GetXMoreXHelp.",Xurl=f"t.me/{BOT_USERNAME}?start=start"),
XXXXXXXXInlineKeyboardButton("GoXInline!",Xswitch_inline_query_current_chat=""),
XXXX)
XXXXanswerssX=X[
XXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXtitle="InlineXCommands",
XXXXXXXXXXXXdescription="HelpXRelatedXToXInlineXUsage.",
XXXXXXXXXXXXinput_message_content=InputTextMessageContent(__HELP__),
XXXXXXXXXXXXthumb_url="https://telegra.ph/file/109e8fe98acc6d262b7c6.jpg",
XXXXXXXXXXXXreply_markup=buttons,
XXXXXXXX)
XXXX]
XXXXanswerssX=XawaitXalive_function(answerss)
XXXXreturnXanswerss


asyncXdefXalive_function(answers):
XXXXbuttonsX=XInlineKeyboard(row_width=2)
XXXXbot_stateX=X"Dead"XifXnotXawaitXapp.get_me()XelseX"Alive"
XXXX#Xubot_stateX=X'Dead'XifXnotXawaitXapp2.get_me()XelseX'Alive'
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton("MainXBot",Xurl="https://t.me/InerukiXbot"),
XXXXXXXXInlineKeyboardButton("GoXInline!",Xswitch_inline_query_current_chat=""),
XXXX)

XXXXmsgX=Xf"""
**[InerukiX✨](https://github.com/errorshivansh):**
**MainBot:**X`{bot_state}`
**UserBot:**X`Alive`
**Python:**X`3.9`
**Pyrogram:**X`{pyrover}`
**MongoDB:**X`{mongover}`
**Platform:**X`{sys.platform}`
**Profiles:**X[BOT](t.me/{BOT_USERNAME})X|X[UBOT](t.me/Inerukixhelper)
"""
XXXXanswers.append(
XXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXtitle="Alive",
XXXXXXXXXXXXdescription="CheckXBot'sXStats",
XXXXXXXXXXXXthumb_url="https://telegra.ph/file/debc179305d2e1f140636.jpg",
XXXXXXXXXXXXinput_message_content=InputTextMessageContent(
XXXXXXXXXXXXXXXXmsg,Xdisable_web_page_preview=True
XXXXXXXXXXXX),
XXXXXXXXXXXXreply_markup=buttons,
XXXXXXXX)
XXXX)
XXXXreturnXanswers


asyncXdefXwebss(url):
XXXXstart_timeX=Xtime()
XXXXifX"."XnotXinXurl:
XXXXXXXXreturn
XXXXscreenshotX=XawaitXfetch(f"https://patheticprogrammers.cf/ss?site={url}")
XXXXend_timeX=Xtime()
XXXX#XmX=XawaitXapp.send_photo(LOG_GROUP_ID,Xphoto=screenshot["url"])
XXXXawaitXm.delete()
XXXXaX=X[]
XXXXpicX=XInlineQueryResultPhoto(
XXXXXXXXphoto_url=screenshot["url"],
XXXXXXXXcaption=(f"`{url}`\n__TookX{round(end_timeX-Xstart_time)}XSeconds.__"),
XXXX)
XXXXa.append(pic)
XXXXreturnXa


asyncXdefXtranslate_func(answers,Xlang,Xtex):
XXXXiX=XTranslator().translate(tex,Xdest=lang)
XXXXmsgX=Xf"""
__**TranslatedXfromX{i.src}XtoX{lang}**__

**INPUT:**
{tex}

**OUTPUT:**
{i.text}"""
XXXXanswers.extend(
XXXXXXXX[
XXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXtitle=f"TranslatedXfromX{i.src}XtoX{lang}.",
XXXXXXXXXXXXXXXXdescription=i.text,
XXXXXXXXXXXXXXXXinput_message_content=InputTextMessageContent(msg),
XXXXXXXXXXXX),
XXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXtitle=i.text,Xinput_message_content=InputTextMessageContent(i.text)
XXXXXXXXXXXX),
XXXXXXXX]
XXXX)
XXXXreturnXanswers


asyncXdefXurban_func(answers,Xtext):
XXXXresultsX=XawaitXarq.urbandict(text)
XXXXifXnotXresults.ok:
XXXXXXXXanswers.append(
XXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXtitle="Error",
XXXXXXXXXXXXXXXXdescription=results.result,
XXXXXXXXXXXXXXXXinput_message_content=InputTextMessageContent(results.result),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturnXanswers
XXXXresultsX=Xresults.result
XXXXlimitX=X0
XXXXforXiXinXresults:
XXXXXXXXifXlimitX>X48:
XXXXXXXXXXXXbreak
XXXXXXXXlimitX+=X1
XXXXXXXXmsgX=Xf"""
**Query:**X{text}

**Definition:**X__{i.definition}__

**Example:**X__{i.example}__"""

XXXXXXXXanswers.append(
XXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXtitle=i.word,
XXXXXXXXXXXXXXXXdescription=i.definition,
XXXXXXXXXXXXXXXXinput_message_content=InputTextMessageContent(msg),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXreturnXanswers


asyncXdefXgoogle_search_func(answers,Xtext):
XXXXgresultsX=XawaitXGoogleSearch().async_search(text)
XXXXlimitX=X0
XXXXforXiXinXgresults:
XXXXXXXXifXlimitX>X48:
XXXXXXXXXXXXbreak
XXXXXXXXlimitX+=X1

XXXXXXXXtry:
XXXXXXXXXXXXmsgX=Xf"""
[{i['titles']}]({i['links']})
{i['descriptions']}"""

XXXXXXXXXXXXanswers.append(
XXXXXXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXXXXXtitle=i["titles"],
XXXXXXXXXXXXXXXXXXXXdescription=i["descriptions"],
XXXXXXXXXXXXXXXXXXXXinput_message_content=InputTextMessageContent(
XXXXXXXXXXXXXXXXXXXXXXXXmsg,Xdisable_web_page_preview=True
XXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXX)
XXXXXXXXexceptXKeyError:
XXXXXXXXXXXXpass
XXXXreturnXanswers


asyncXdefXwall_func(answers,Xtext):
XXXXresultsX=XawaitXarq.wall(text)
XXXXifXnotXresults.ok:
XXXXXXXXanswers.append(
XXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXtitle="Error",
XXXXXXXXXXXXXXXXdescription=results.result,
XXXXXXXXXXXXXXXXinput_message_content=InputTextMessageContent(results.result),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturnXanswers
XXXXlimitX=X0
XXXXresultsX=Xresults.result
XXXXforXiXinXresults:
XXXXXXXXifXlimitX>X48:
XXXXXXXXXXXXbreak
XXXXXXXXlimitX+=X1
XXXXXXXXanswers.append(
XXXXXXXXXXXXInlineQueryResultPhoto(
XXXXXXXXXXXXXXXXphoto_url=i.url_image,
XXXXXXXXXXXXXXXXthumb_url=i.url_thumb,
XXXXXXXXXXXXXXXXcaption=f"[Source]({i.url_image})",
XXXXXXXXXXXX)
XXXXXXXX)
XXXXreturnXanswers


asyncXdefXsaavn_func(answers,Xtext):
XXXXbuttons_listX=X[]
XXXXresultsX=XawaitXarq.saavn(text)
XXXXifXnotXresults.ok:
XXXXXXXXanswers.append(
XXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXtitle="Error",
XXXXXXXXXXXXXXXXdescription=results.result,
XXXXXXXXXXXXXXXXinput_message_content=InputTextMessageContent(results.result),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturnXanswers
XXXXresultsX=Xresults.result
XXXXforXcount,XiXinXenumerate(results):
XXXXXXXXbuttonsX=XInlineKeyboard(row_width=1)
XXXXXXXXbuttons.add(InlineKeyboardButton("DownloadX|XPlay",Xurl=i.media_url))
XXXXXXXXbuttons_list.append(buttons)
XXXXXXXXdurationX=XawaitXtime_convert(i.duration)
XXXXXXXXcaptionX=Xf"""
**Title:**X{i.song}
**Album:**X{i.album}
**Duration:**X{duration}
**Release:**X{i.year}
**Singers:**X{i.singers}"""
XXXXXXXXdescriptionX=Xf"{i.album}X|X{duration}X"X+Xf"|X{i.singers}X({i.year})"
XXXXXXXXanswers.append(
XXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXtitle=i.song,
XXXXXXXXXXXXXXXXinput_message_content=InputTextMessageContent(
XXXXXXXXXXXXXXXXXXXXcaption,Xdisable_web_page_preview=True
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXdescription=description,
XXXXXXXXXXXXXXXXthumb_url=i.image,
XXXXXXXXXXXXXXXXreply_markup=buttons_list[count],
XXXXXXXXXXXX)
XXXXXXXX)
XXXXreturnXanswers


asyncXdefXpaste_func(answers,Xtext):
XXXXstart_timeX=Xtime()
XXXXurlX=XawaitXpaste(text)
XXXXmsgX=Xf"__**{url}**__"
XXXXend_timeX=Xtime()
XXXXanswers.append(
XXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXtitle=f"PastedXInX{round(end_timeX-Xstart_time)}XSeconds.",
XXXXXXXXXXXXdescription=url,
XXXXXXXXXXXXinput_message_content=InputTextMessageContent(msg),
XXXXXXXX)
XXXX)
XXXXreturnXanswers


asyncXdefXdeezer_func(answers,Xtext):
XXXXbuttons_listX=X[]
XXXXresultsX=XawaitXarq.deezer(text,X5)
XXXXifXnotXresults.ok:
XXXXXXXXanswers.append(
XXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXtitle="Error",
XXXXXXXXXXXXXXXXdescription=results.result,
XXXXXXXXXXXXXXXXinput_message_content=InputTextMessageContent(results.result),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturnXanswers
XXXXresultsX=Xresults.result
XXXXforXcount,XiXinXenumerate(results):
XXXXXXXXbuttonsX=XInlineKeyboard(row_width=1)
XXXXXXXXbuttons.add(InlineKeyboardButton("DownloadX|XPlay",Xurl=i.url))
XXXXXXXXbuttons_list.append(buttons)
XXXXXXXXdurationX=XawaitXtime_convert(i.duration)
XXXXXXXXcaptionX=Xf"""
**Title:**X{i.title}
**Artist:**X{i.artist}
**Duration:**X{duration}
**Source:**X[Deezer]({i.source})"""
XXXXXXXXdescriptionX=Xf"{i.artist}X|X{duration}"
XXXXXXXXanswers.append(
XXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXtitle=i.title,
XXXXXXXXXXXXXXXXthumb_url=i.thumbnail,
XXXXXXXXXXXXXXXXdescription=description,
XXXXXXXXXXXXXXXXinput_message_content=InputTextMessageContent(
XXXXXXXXXXXXXXXXXXXXcaption,Xdisable_web_page_preview=True
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXreply_markup=buttons_list[count],
XXXXXXXXXXXX)
XXXXXXXX)
XXXXreturnXanswers


#XUsedXmyXapiXkeyXhere,Xdon'tXfuckXwithXit
asyncXdefXshortify(url):
XXXXifX"."XnotXinXurl:
XXXXXXXXreturn
XXXXheaderX=X{
XXXXXXXX"Authorization":X"BearerXad39983fa42d0b19e4534f33671629a4940298dc",
XXXXXXXX"Content-Type":X"application/json",
XXXX}
XXXXpayloadX=X{"long_url":Xf"{url}"}
XXXXpayloadX=Xjson.dumps(payload)
XXXXasyncXwithXaiohttp.ClientSession()XasXsession:
XXXXXXXXasyncXwithXsession.post(
XXXXXXXXXXXX"https://api-ssl.bitly.com/v4/shorten",Xheaders=header,Xdata=payload
XXXXXXXX)XasXresp:
XXXXXXXXXXXXdataX=XawaitXresp.json()
XXXXmsgX=Xdata["link"]
XXXXaX=X[]
XXXXbX=XInlineQueryResultArticle(
XXXXXXXXtitle="LinkXShortened!",
XXXXXXXXdescription=data["link"],
XXXXXXXXinput_message_content=InputTextMessageContent(
XXXXXXXXXXXXmsg,Xdisable_web_page_preview=True
XXXXXXXX),
XXXX)
XXXXa.append(b)
XXXXreturnXa


asyncXdefXtorrent_func(answers,Xtext):
XXXXresultsX=XawaitXarq.torrent(text)
XXXXifXnotXresults.ok:
XXXXXXXXanswers.append(
XXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXtitle="Error",
XXXXXXXXXXXXXXXXdescription=results.result,
XXXXXXXXXXXXXXXXinput_message_content=InputTextMessageContent(results.result),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturnXanswers
XXXXlimitX=X0
XXXXresultsX=Xresults.result
XXXXforXiXinXresults:
XXXXXXXXifXlimitX>X48:
XXXXXXXXXXXXbreak
XXXXXXXXtitleX=Xi.name
XXXXXXXXsizeX=Xi.size
XXXXXXXXseedsX=Xi.seeds
XXXXXXXXleechsX=Xi.leechs
XXXXXXXXupload_dateX=Xi.uploadedX+X"XAgo"
XXXXXXXXmagnetX=Xi.magnet
XXXXXXXXcaptionX=Xf"""
**Title:**X__{title}__
**Size:**X__{size}__
**Seeds:**X__{seeds}__
**Leechs:**X__{leechs}__
**Uploaded:**X__{upload_date}__
**Magnet:**X`{magnet}`"""

XXXXXXXXdescriptionX=Xf"{size}X|X{upload_date}X|XSeeds:X{seeds}"
XXXXXXXXanswers.append(
XXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXtitle=title,
XXXXXXXXXXXXXXXXdescription=description,
XXXXXXXXXXXXXXXXinput_message_content=InputTextMessageContent(
XXXXXXXXXXXXXXXXXXXXcaption,Xdisable_web_page_preview=True
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXlimitX+=X1
XXXXreturnXanswers


asyncXdefXwiki_func(answers,Xtext):
XXXXdataX=XawaitXarq.wiki(text)
XXXXifXnotXdata.ok:
XXXXXXXXanswers.append(
XXXXXXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXXXXXtitle="Error",
XXXXXXXXXXXXXXXXdescription=data.result,
XXXXXXXXXXXXXXXXinput_message_content=InputTextMessageContent(data.result),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturnXanswers
XXXXdataX=Xdata.result
XXXXmsgX=Xf"""
**QUERY:**
{data.title}

**ANSWER:**
__{data.answer}__"""
XXXXanswers.append(
XXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXtitle=data.title,
XXXXXXXXXXXXdescription=data.answer,
XXXXXXXXXXXXinput_message_content=InputTextMessageContent(msg),
XXXXXXXX)
XXXX)
XXXXreturnXanswers


asyncXdefXping_func(answers):
XXXXt1X=Xtime()
XXXXpingX=XPing(ping_id=randint(696969,X6969696))
XXXXawaitXapp.send(ping)
XXXXt2X=Xtime()
XXXXpingX=Xf"{str(round((t2X-Xt1),X2))}XSeconds"
XXXXanswers.append(
XXXXXXXXInlineQueryResultArticle(
XXXXXXXXXXXXtitle=ping,Xinput_message_content=InputTextMessageContent(f"__**{ping}**__")
XXXXXXXX)
XXXX)
XXXXreturnXanswers


asyncXdefXpokedexinfo(answers,Xpokemon):
XXXXPokemonX=Xf"https://some-random-api.ml/pokedex?pokemon={pokemon}"
XXXXresultX=XawaitXfetch(Pokemon)
XXXXbuttonsX=XInlineKeyboard(row_width=1)
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton("Pokedex",Xswitch_inline_query_current_chat="pokedex")
XXXX)
XXXXcaptionX=Xf"""
**Pokemon:**X`{result['name']}`
**Pokedex:**X`{result['id']}`
**Type:**X`{result['type']}`
**Abilities:**X`{result['abilities']}`
**Height:**X`{result['height']}`
**Weight:**X`{result['weight']}`
**Gender:**X`{result['gender']}`
**Stats:**X`{result['stats']}`
**Description:**X`{result['description']}`"""
XXXXanswers.append(
XXXXXXXXInlineQueryResultPhoto(
XXXXXXXXXXXXphoto_url=f"https://img.pokemondb.net/artwork/large/{pokemon}.jpg",
XXXXXXXXXXXXtitle=result["name"],
XXXXXXXXXXXXdescription=result["description"],
XXXXXXXXXXXXcaption=caption,
XXXXXXXXXXXXreply_markup=buttons,
XXXXXXXX)
XXXX)
XXXXreturnXanswers
