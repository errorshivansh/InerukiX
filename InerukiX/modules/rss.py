#Copyright(C)2020-2021byDevsExpo@Github,<https://github.com/DevsExpo>.
#
#Thisfileispartof<https://github.com/DevsExpo/FridayUserBot>project,
#andisreleasedunderthe"GNUv3.0LicenseAgreement".
#Pleasesee<https://github.com/DevsExpo/blob/master/LICENSE>
#
#Allrightsreserved.

importasyncio

importfeedparser
fromapscheduler.schedulers.asyncioimportAsyncIOScheduler
frompyrogramimportfilters

fromIneruki.db.mongo_helpers.rss_dbimport(
add_rss,
basic_check,
del_rss,
delete_all,
get_all,
get_chat_rss,
is_get_chat_rss,
overall_check,
update_rss,
)
fromIneruki.function.pluginhelpersimportadmins_only,edit_or_reply,get_text
fromIneruki.services.pyrogramimportpbot


@pbot.on_message(filters.command("addrss")&~filters.edited&~filters.bot)
@admins_only
asyncdefaddrss(client,message):
pablo=awaitedit_or_reply(message,"`Processing....`")
lenk=get_text(message)
ifnotlenk:
awaitpablo.edit("InvalidCommandSyntax,PleaseCheckHelpMenuToKnowMore!")
return
try:
rss_d=feedparser.parse(lenk)
rss_d.entries[0].title
except:
awaitpablo.edit(
"ERROR:ThelinkdoesnotseemtobeaRSSfeedorisnotsupported"
)
return
lol=is_get_chat_rss(message.chat.id,lenk)
iflol:
awaitpablo.edit("ThisLinkAlreadyAdded")
return
content=""
content+=f"**{rss_d.entries[0].title}**"
content+=f"\n\n{rss_d.entries[0].link}"
try:
content+=f"\n{rss_d.entries[0].description}"
except:
pass
awaitclient.send_message(message.chat.id,content)
add_rss(message.chat.id,lenk,rss_d.entries[0].link)
awaitpablo.edit("SuccessfullyAddedLinkToRSSWatch")


@pbot.on_message(
filters.command("testrss")&~filters.edited&~filters.bot&~filters.private
)
@admins_only
asyncdeftestrss(client,message):
pablo=awaitedit_or_reply(message,"`Processing....`")
damn=basic_check(message.chat.id)
ifnotdamn:
URL="https://www.reddit.com/r/funny/new/.rss"
rss_d=feedparser.parse(URL)
Content=rss_d.entries[0]["title"]+"\n\n"+rss_d.entries[0]["link"]
awaitclient.send_message(message.chat.id,Content)
awaitpablo.edit("ThisChatHasNoRSSSoSentRedditRSS")
else:
all=get_chat_rss(message.chat.id)
forxinall:
link=x.get("rss_link")
rss_d=feedparser.parse(link)
content=""
content+=f"**{rss_d.entries[0].title}**"
content+=f"\n\nLink:{rss_d.entries[0].link}"
try:
content+=f"\n{rss_d.entries[0].description}"
except:
pass
awaitclient.send_message(message.chat.id,content)
awaitpablo.delete()


@pbot.on_message(
filters.command("listrss")&~filters.edited&~filters.bot&~filters.private
)
@admins_only
asyncdeflistrss(client,message):
pablo=awaitedit_or_reply(message,"`Processing....`")
damn=basic_check(message.chat.id)
ifnotdamn:
awaitpablo.edit("ThisChatHasNoRSS!")
return
links=""
all=get_chat_rss(message.chat.id)
forxinall:
l=x.get("rss_link")
links+=f"{l}\n"
content=f"RssFoundInTheChatAre:\n\n{links}"
awaitclient.send_message(message.chat.id,content)
awaitpablo.delete()


@pbot.on_message(
filters.command("delrss")&~filters.edited&~filters.bot&~filters.private
)
@admins_only
asyncdefdelrss(client,message):
pablo=awaitedit_or_reply(message,"`Processing....`")
lenk=get_text(message)
ifnotlenk:
awaitpablo.edit("InvalidCommandSyntax,PleaseCheckHelpMenuToKnowMore!")
return
lol=is_get_chat_rss(message.chat.id,lenk)
ifnotlol:
awaitpablo.edit("ThisLinkWasNeverAdded")
return
del_rss(message.chat.id,lenk)
awaitpablo.edit(f"SuccessfullyRemoved`{lenk}`FromChatRSS")


@pbot.on_message(
filters.command("delallrss")&~filters.edited&~filters.bot&~filters.private
)
@admins_only
asyncdefdelrss(client,message):
pablo=awaitedit_or_reply(message,"`Processing....`")
ifnotbasic_check(message.chat.id):
awaitpablo.edit("ThisChatHasNoRSSToDelete")
return
awaitdelete_all()
awaitpablo.edit("SuccessfullyDeletedAllRSSFromTheChat")


asyncdefcheck_rss():
ifnotoverall_check():
return
all=get_all()
foroneinall:
link=one.get("rss_link")
old=one.get("latest_rss")
rss_d=feedparser.parse(link)
ifrss_d.entries[0].link!=old:
message=one.get("chat_id")
content=""
content+=f"**{rss_d.entries[0].title}**"
content+=f"\n\nLink:{rss_d.entries[0].link}"
try:
content+=f"\n{rss_d.entries[0].description}"
except:
pass
update_rss(message,link,rss_d.entries[0].link)
try:
awaitpbot.send_message(message,content)
awaitasyncio.sleep(2)
except:
return


scheduler=AsyncIOScheduler()
scheduler.add_job(check_rss,"interval",minutes=10)
scheduler.start()

__mod_name__="RSSFeed"
__help__="""
-/addrss:AddRsstothechat
-/testrss:TestRSSOfTheChat
-/listrss:ListallRSSOfTheChat
-/delrss:DeleteRSSFromTheChat
-/delallrss:DeletesAllRSSFromTheChat
"""
