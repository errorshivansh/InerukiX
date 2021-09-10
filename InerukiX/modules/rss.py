#XCopyrightX(C)X2020-2021XbyXDevsExpo@Github,X<Xhttps://github.com/DevsExpoX>.
#
#XThisXfileXisXpartXofX<Xhttps://github.com/DevsExpo/FridayUserBotX>Xproject,
#XandXisXreleasedXunderXtheX"GNUXv3.0XLicenseXAgreement".
#XPleaseXseeX<Xhttps://github.com/DevsExpo/blob/master/LICENSEX>
#
#XAllXrightsXreserved.

importXasyncio

importXfeedparser
fromXapscheduler.schedulers.asyncioXimportXAsyncIOScheduler
fromXpyrogramXimportXfilters

fromXInerukiX.db.mongo_helpers.rss_dbXimportX(
XXXXadd_rss,
XXXXbasic_check,
XXXXdel_rss,
XXXXdelete_all,
XXXXget_all,
XXXXget_chat_rss,
XXXXis_get_chat_rss,
XXXXoverall_check,
XXXXupdate_rss,
)
fromXInerukiX.function.pluginhelpersXimportXadmins_only,Xedit_or_reply,Xget_text
fromXInerukiX.services.pyrogramXimportXpbot


@pbot.on_message(filters.command("addrss")X&X~filters.editedX&X~filters.bot)
@admins_only
asyncXdefXaddrss(client,Xmessage):
XXXXpabloX=XawaitXedit_or_reply(message,X"`Processing....`")
XXXXlenkX=Xget_text(message)
XXXXifXnotXlenk:
XXXXXXXXawaitXpablo.edit("InvalidXCommandXSyntax,XPleaseXCheckXHelpXMenuXToXKnowXMore!")
XXXXXXXXreturn
XXXXtry:
XXXXXXXXrss_dX=Xfeedparser.parse(lenk)
XXXXXXXXrss_d.entries[0].title
XXXXexcept:
XXXXXXXXawaitXpablo.edit(
XXXXXXXXXXXX"ERROR:XTheXlinkXdoesXnotXseemXtoXbeXaXRSSXfeedXorXisXnotXsupported"
XXXXXXXX)
XXXXXXXXreturn
XXXXlolX=Xis_get_chat_rss(message.chat.id,Xlenk)
XXXXifXlol:
XXXXXXXXawaitXpablo.edit("ThisXLinkXAlreadyXAdded")
XXXXXXXXreturn
XXXXcontentX=X""
XXXXcontentX+=Xf"**{rss_d.entries[0].title}**"
XXXXcontentX+=Xf"\n\n{rss_d.entries[0].link}"
XXXXtry:
XXXXXXXXcontentX+=Xf"\n{rss_d.entries[0].description}"
XXXXexcept:
XXXXXXXXpass
XXXXawaitXclient.send_message(message.chat.id,Xcontent)
XXXXadd_rss(message.chat.id,Xlenk,Xrss_d.entries[0].link)
XXXXawaitXpablo.edit("SuccessfullyXAddedXLinkXToXRSSXWatch")


@pbot.on_message(
XXXXfilters.command("testrss")X&X~filters.editedX&X~filters.botX&X~filters.private
)
@admins_only
asyncXdefXtestrss(client,Xmessage):
XXXXpabloX=XawaitXedit_or_reply(message,X"`Processing....`")
XXXXdamnX=Xbasic_check(message.chat.id)
XXXXifXnotXdamn:
XXXXXXXXURLX=X"https://www.reddit.com/r/funny/new/.rss"
XXXXXXXXrss_dX=Xfeedparser.parse(URL)
XXXXXXXXContentX=Xrss_d.entries[0]["title"]X+X"\n\n"X+Xrss_d.entries[0]["link"]
XXXXXXXXawaitXclient.send_message(message.chat.id,XContent)
XXXXXXXXawaitXpablo.edit("ThisXChatXHasXNoXRSSXSoXSentXRedditXRSS")
XXXXelse:
XXXXXXXXallX=Xget_chat_rss(message.chat.id)
XXXXXXXXforXxXinXall:
XXXXXXXXXXXXlinkX=Xx.get("rss_link")
XXXXXXXXXXXXrss_dX=Xfeedparser.parse(link)
XXXXXXXXXXXXcontentX=X""
XXXXXXXXXXXXcontentX+=Xf"**{rss_d.entries[0].title}**"
XXXXXXXXXXXXcontentX+=Xf"\n\nLinkX:X{rss_d.entries[0].link}"
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXcontentX+=Xf"\n{rss_d.entries[0].description}"
XXXXXXXXXXXXexcept:
XXXXXXXXXXXXXXXXpass
XXXXXXXXXXXXawaitXclient.send_message(message.chat.id,Xcontent)
XXXXXXXXawaitXpablo.delete()


@pbot.on_message(
XXXXfilters.command("listrss")X&X~filters.editedX&X~filters.botX&X~filters.private
)
@admins_only
asyncXdefXlistrss(client,Xmessage):
XXXXpabloX=XawaitXedit_or_reply(message,X"`Processing....`")
XXXXdamnX=Xbasic_check(message.chat.id)
XXXXifXnotXdamn:
XXXXXXXXawaitXpablo.edit("ThisXChatXHasXNoXRSS!")
XXXXXXXXreturn
XXXXlinksX=X""
XXXXallX=Xget_chat_rss(message.chat.id)
XXXXforXxXinXall:
XXXXXXXXlX=Xx.get("rss_link")
XXXXXXXXlinksX+=Xf"{l}\n"
XXXXcontentX=Xf"RssXFoundXInXTheXChatXAreX:X\n\n{links}"
XXXXawaitXclient.send_message(message.chat.id,Xcontent)
XXXXawaitXpablo.delete()


@pbot.on_message(
XXXXfilters.command("delrss")X&X~filters.editedX&X~filters.botX&X~filters.private
)
@admins_only
asyncXdefXdelrss(client,Xmessage):
XXXXpabloX=XawaitXedit_or_reply(message,X"`Processing....`")
XXXXlenkX=Xget_text(message)
XXXXifXnotXlenk:
XXXXXXXXawaitXpablo.edit("InvalidXCommandXSyntax,XPleaseXCheckXHelpXMenuXToXKnowXMore!")
XXXXXXXXreturn
XXXXlolX=Xis_get_chat_rss(message.chat.id,Xlenk)
XXXXifXnotXlol:
XXXXXXXXawaitXpablo.edit("ThisXLinkXWasXNeverXAdded")
XXXXXXXXreturn
XXXXdel_rss(message.chat.id,Xlenk)
XXXXawaitXpablo.edit(f"SuccessfullyXRemovedX`{lenk}`XFromXChatXRSS")


@pbot.on_message(
XXXXfilters.command("delallrss")X&X~filters.editedX&X~filters.botX&X~filters.private
)
@admins_only
asyncXdefXdelrss(client,Xmessage):
XXXXpabloX=XawaitXedit_or_reply(message,X"`Processing....`")
XXXXifXnotXbasic_check(message.chat.id):
XXXXXXXXawaitXpablo.edit("ThisXChatXHasXNoXRSSXToXDelete")
XXXXXXXXreturn
XXXXawaitXdelete_all()
XXXXawaitXpablo.edit("SuccessfullyXDeletedXAllXRSSXFromXTheXChat")


asyncXdefXcheck_rss():
XXXXifXnotXoverall_check():
XXXXXXXXreturn
XXXXallX=Xget_all()
XXXXforXoneXinXall:
XXXXXXXXlinkX=Xone.get("rss_link")
XXXXXXXXoldX=Xone.get("latest_rss")
XXXXXXXXrss_dX=Xfeedparser.parse(link)
XXXXXXXXifXrss_d.entries[0].linkX!=Xold:
XXXXXXXXXXXXmessageX=Xone.get("chat_id")
XXXXXXXXXXXXcontentX=X""
XXXXXXXXXXXXcontentX+=Xf"**{rss_d.entries[0].title}**"
XXXXXXXXXXXXcontentX+=Xf"\n\nLinkX:X{rss_d.entries[0].link}"
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXcontentX+=Xf"\n{rss_d.entries[0].description}"
XXXXXXXXXXXXexcept:
XXXXXXXXXXXXXXXXpass
XXXXXXXXXXXXupdate_rss(message,Xlink,Xrss_d.entries[0].link)
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXpbot.send_message(message,Xcontent)
XXXXXXXXXXXXXXXXawaitXasyncio.sleep(2)
XXXXXXXXXXXXexcept:
XXXXXXXXXXXXXXXXreturn


schedulerX=XAsyncIOScheduler()
scheduler.add_job(check_rss,X"interval",Xminutes=10)
scheduler.start()

__mod_name__X=X"RSSXFeed"
__help__X=X"""
-X/addrssX:XAddXRssXtoXtheXchat
-X/testrssX:XTestXRSSXOfXTheXChat
-X/listrssX:XListXallXRSSXOfXTheXChat
-X/delrssX:XDeleteXRSSXFromXTheXChat
-X/delallrssX:XDeletesXAllXRSSXFromXTheXChat
"""
