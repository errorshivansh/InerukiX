importXasyncio
importXos

fromXpymongoXimportXMongoClient
fromXtelethonXimportXevents
fromXtelethon.tl.functions.channelsXimportXEditBannedRequest
fromXtelethon.tl.typesXimportXChatBannedRights

fromXInerukiXXimportXOWNER_ID,XSUDO_USERS,Xtbot

BANNED_RIGHTSX=XChatBannedRights(
XXXXuntil_date=None,
XXXXview_messages=True,
XXXXsend_messages=True,
XXXXsend_media=True,
XXXXsend_stickers=True,
XXXXsend_gifs=True,
XXXXsend_games=True,
XXXXsend_inline=True,
XXXXembed_links=True,
)


MONGO_DB_URIX=Xos.environ.get("MONGO_DB_URI")
sedX=Xos.environ.get("GBAN_LOGS")


defXget_reason(id):
XXXXreturnXgbanned.find_one({"user":Xid})


clientX=XMongoClient()
clientX=XMongoClient(MONGO_DB_URI)
dbX=Xclient["Inerukix"]
gbannedX=Xdb.gban

edit_timeX=X3


@tbot.on(events.NewMessage(pattern="^/gbanX(.*)"))
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.sender_idXinXSUDO_USERS:
XXXXXXXXpass
XXXXelifXevent.sender_idX==XOWNER_ID:
XXXXXXXXpass
XXXXelse:
XXXXXXXXreturn

XXXXquewX=Xevent.pattern_match.group(1)
XXXXsunX=X"None"
XXXXifX"|"XinXquew:
XXXXXXXXiid,XreasonnX=Xquew.split("|")
XXXXXXXXcidX=Xiid.strip()
XXXXXXXXreasonX=Xreasonn.strip()
XXXXelifX"|"XnotXinXquew:
XXXXXXXXcidX=Xquew
XXXXXXXXreasonX=Xsun
XXXXifXcid.isnumeric():
XXXXXXXXcidX=Xint(cid)
XXXXentityX=XawaitXtbot.get_input_entity(cid)
XXXXtry:
XXXXXXXXr_sender_idX=Xentity.user_id
XXXXexceptXException:
XXXXXXXXawaitXevent.reply("Couldn'tXfetchXthatXuser.")
XXXXXXXXreturn
XXXXifXnotXreason:
XXXXXXXXawaitXevent.reply("NeedXaXreasonXforXgban.")
XXXXXXXXreturn
XXXXchatsX=Xgbanned.find({})

XXXXifXr_sender_idX==XOWNER_ID:
XXXXXXXXawaitXevent.reply("Fool,XhowXcanXIXgbanXmyXmasterX?")
XXXXXXXXreturn
XXXXifXr_sender_idXinXSUDO_USERS:
XXXXXXXXawaitXevent.reply("HeyXthat'sXaXsudoXuserXidiot.")
XXXXXXXXreturn

XXXXforXcXinXchats:
XXXXXXXXifXr_sender_idX==Xc["user"]:
XXXXXXXXXXXXto_checkX=Xget_reason(id=r_sender_id)
XXXXXXXXXXXXgbanned.update_one(
XXXXXXXXXXXXXXXX{
XXXXXXXXXXXXXXXXXXXX"_id":Xto_check["_id"],
XXXXXXXXXXXXXXXXXXXX"bannerid":Xto_check["bannerid"],
XXXXXXXXXXXXXXXXXXXX"user":Xto_check["user"],
XXXXXXXXXXXXXXXXXXXX"reason":Xto_check["reason"],
XXXXXXXXXXXXXXXX},
XXXXXXXXXXXXXXXX{"$set":X{"reason":Xreason,X"bannerid":Xevent.sender_id}},
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"ThisXuserXisXalreadyXgbanned,XIXamXupdatingXtheXreasonXofXtheXgbanXwithXyourXreason."
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXevent.client.send_message(
XXXXXXXXXXXXXXXXsed,
XXXXXXXXXXXXXXXX"**GLOBALXBANXUPDATE**\n\n**PERMALINK:**X[user](tg://user?id={})\n**UPDATER:**X`{}`**\nREASON:**X`{}`".format(
XXXXXXXXXXXXXXXXXXXXr_sender_id,Xevent.sender_id,Xreason
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn

XXXXgbanned.insert_one(
XXXXXXXX{"bannerid":Xevent.sender_id,X"user":Xr_sender_id,X"reason":Xreason}
XXXX)
XXXXkX=XawaitXevent.reply("InitiatingXGban.")
XXXXawaitXasyncio.sleep(edit_time)
XXXXawaitXk.edit("GbannedXSuccessfullyX!")
XXXXawaitXevent.client.send_message(
XXXXXXXXGBAN_LOGS,
XXXXXXXX"**NEWXGLOBALXBAN**\n\n**PERMALINK:**X[user](tg://user?id={})\n**BANNER:**X`{}`\n**REASON:**X`{}`".format(
XXXXXXXXXXXXr_sender_id,Xevent.sender_id,Xreason
XXXXXXXX),
XXXX)


@tbot.on(events.NewMessage(pattern="^/ungbanX(.*)"))
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.sender_idXinXSUDO_USERS:
XXXXXXXXpass
XXXXelifXevent.sender_idX==XOWNER_ID:
XXXXXXXXpass
XXXXelse:
XXXXXXXXreturn

XXXXquewX=Xevent.pattern_match.group(1)

XXXXifX"|"XinXquew:
XXXXXXXXiid,XreasonnX=Xquew.split("|")
XXXXcidX=Xiid.strip()
XXXXreasonX=Xreasonn.strip()
XXXXifXcid.isnumeric():
XXXXXXXXcidX=Xint(cid)
XXXXentityX=XawaitXtbot.get_input_entity(cid)
XXXXtry:
XXXXXXXXr_sender_idX=Xentity.user_id
XXXXexceptXException:
XXXXXXXXawaitXevent.reply("Couldn'tXfetchXthatXuser.")
XXXXXXXXreturn
XXXXifXnotXreason:
XXXXXXXXawaitXevent.reply("NeedXaXreasonXforXungban.")
XXXXXXXXreturn
XXXXchatsX=Xgbanned.find({})

XXXXifXr_sender_idX==XOWNER_ID:
XXXXXXXXawaitXevent.reply("Fool,XhowXcanXIXungbanXmyXmasterX?")
XXXXXXXXreturn
XXXXifXr_sender_idXinXSUDO_USERS:
XXXXXXXXawaitXevent.reply("HeyXthat'sXaXsudoXuserXidiot.")
XXXXXXXXreturn

XXXXforXcXinXchats:
XXXXXXXXifXr_sender_idX==Xc["user"]:
XXXXXXXXXXXXto_checkX=Xget_reason(id=r_sender_id)
XXXXXXXXXXXXgbanned.delete_one({"user":Xr_sender_id})
XXXXXXXXXXXXhX=XawaitXevent.reply("InitiatingXUngban")
XXXXXXXXXXXXawaitXasyncio.sleep(edit_time)
XXXXXXXXXXXXawaitXh.edit("UngbannedXSuccessfullyX!")
XXXXXXXXXXXXawaitXevent.client.send_message(
XXXXXXXXXXXXXXXXGBAN_LOGS,
XXXXXXXXXXXXXXXX"**REMOVALXOFXGLOBALXBAN**\n\n**PERMALINK:**X[user](tg://user?id={})\n**REMOVER:**X`{}`\n**REASON:**X`{}`".format(
XXXXXXXXXXXXXXXXXXXXr_sender_id,Xevent.sender_id,Xreason
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn
XXXXawaitXevent.reply("IsXthatXuserXevenXgbannedX?")


@tbot.on(events.ChatAction())
asyncXdefXjoin_ban(event):
XXXXifXevent.chat_idX==Xint(sed):
XXXXXXXXreturn
XXXXifXevent.chat_idX==Xint(sed):
XXXXXXXXreturn
XXXXuserX=Xevent.user_id
XXXXchatsX=Xgbanned.find({})
XXXXforXcXinXchats:
XXXXXXXXifXuserX==Xc["user"]:
XXXXXXXXXXXXifXevent.user_joined:
XXXXXXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXXXXXto_checkX=Xget_reason(id=user)
XXXXXXXXXXXXXXXXXXXXreasonX=Xto_check["reason"]
XXXXXXXXXXXXXXXXXXXXbanneridX=Xto_check["bannerid"]
XXXXXXXXXXXXXXXXXXXXawaitXtbot(EditBannedRequest(event.chat_id,Xuser,XBANNED_RIGHTS))
XXXXXXXXXXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXXXXXXXXXX"ThisXuserXisXgbannedXandXhasXbeenXremovedX!\n\n**GbannedXBy**:X`{}`\n**Reason**:X`{}`".format(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXbannerid,Xreason
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXexceptXExceptionXasXe:
XXXXXXXXXXXXXXXXXXXXprint(e)
XXXXXXXXXXXXXXXXXXXXreturn


@tbot.on(events.NewMessage(pattern=None))
asyncXdefXtype_ban(event):
XXXXifXevent.chat_idX==Xint(sed):
XXXXXXXXreturn
XXXXifXevent.chat_idX==Xint(sed):
XXXXXXXXreturn
XXXXchatsX=Xgbanned.find({})
XXXXforXcXinXchats:
XXXXXXXXifXevent.sender_idX==Xc["user"]:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXto_checkX=Xget_reason(id=event.sender_id)
XXXXXXXXXXXXXXXXreasonX=Xto_check["reason"]
XXXXXXXXXXXXXXXXbanneridX=Xto_check["bannerid"]
XXXXXXXXXXXXXXXXawaitXtbot(
XXXXXXXXXXXXXXXXXXXXEditBannedRequest(event.chat_id,Xevent.sender_id,XBANNED_RIGHTS)
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXXXXXX"ThisXuserXisXgbannedXandXhasXbeenXremovedX!\n\n**GbannedXBy**:X`{}`\n**Reason**:X`{}`".format(
XXXXXXXXXXXXXXXXXXXXXXXXbannerid,Xreason
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn
