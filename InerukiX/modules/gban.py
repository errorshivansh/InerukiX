importasyncio
importos

frompymongoimportMongoClient
fromtelethonimportevents
fromtelethon.tl.functions.channelsimportEditBannedRequest
fromtelethon.tl.typesimportChatBannedRights

fromInerukiimportOWNER_ID,SUDO_USERS,tbot

BANNED_RIGHTS=ChatBannedRights(
until_date=None,
view_messages=True,
send_messages=True,
send_media=True,
send_stickers=True,
send_gifs=True,
send_games=True,
send_inline=True,
embed_links=True,
)


MONGO_DB_URI=os.environ.get("MONGO_DB_URI")
sed=os.environ.get("GBAN_LOGS")


defget_reason(id):
returngbanned.find_one({"user":id})


client=MongoClient()
client=MongoClient(MONGO_DB_URI)
db=client["Inerukix"]
gbanned=db.gban

edit_time=3


@tbot.on(events.NewMessage(pattern="^/gban(.*)"))
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.sender_idinSUDO_USERS:
pass
elifevent.sender_id==OWNER_ID:
pass
else:
return

quew=event.pattern_match.group(1)
sun="None"
if"|"inquew:
iid,reasonn=quew.split("|")
cid=iid.strip()
reason=reasonn.strip()
elif"|"notinquew:
cid=quew
reason=sun
ifcid.isnumeric():
cid=int(cid)
entity=awaittbot.get_input_entity(cid)
try:
r_sender_id=entity.user_id
exceptException:
awaitevent.reply("Couldn'tfetchthatuser.")
return
ifnotreason:
awaitevent.reply("Needareasonforgban.")
return
chats=gbanned.find({})

ifr_sender_id==OWNER_ID:
awaitevent.reply("Fool,howcanIgbanmymaster?")
return
ifr_sender_idinSUDO_USERS:
awaitevent.reply("Heythat'sasudouseridiot.")
return

forcinchats:
ifr_sender_id==c["user"]:
to_check=get_reason(id=r_sender_id)
gbanned.update_one(
{
"_id":to_check["_id"],
"bannerid":to_check["bannerid"],
"user":to_check["user"],
"reason":to_check["reason"],
},
{"$set":{"reason":reason,"bannerid":event.sender_id}},
)
awaitevent.reply(
"Thisuserisalreadygbanned,Iamupdatingthereasonofthegbanwithyourreason."
)
awaitevent.client.send_message(
sed,
"**GLOBALBANUPDATE**\n\n**PERMALINK:**[user](tg://user?id={})\n**UPDATER:**`{}`**\nREASON:**`{}`".format(
r_sender_id,event.sender_id,reason
),
)
return

gbanned.insert_one(
{"bannerid":event.sender_id,"user":r_sender_id,"reason":reason}
)
k=awaitevent.reply("InitiatingGban.")
awaitasyncio.sleep(edit_time)
awaitk.edit("GbannedSuccessfully!")
awaitevent.client.send_message(
GBAN_LOGS,
"**NEWGLOBALBAN**\n\n**PERMALINK:**[user](tg://user?id={})\n**BANNER:**`{}`\n**REASON:**`{}`".format(
r_sender_id,event.sender_id,reason
),
)


@tbot.on(events.NewMessage(pattern="^/ungban(.*)"))
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.sender_idinSUDO_USERS:
pass
elifevent.sender_id==OWNER_ID:
pass
else:
return

quew=event.pattern_match.group(1)

if"|"inquew:
iid,reasonn=quew.split("|")
cid=iid.strip()
reason=reasonn.strip()
ifcid.isnumeric():
cid=int(cid)
entity=awaittbot.get_input_entity(cid)
try:
r_sender_id=entity.user_id
exceptException:
awaitevent.reply("Couldn'tfetchthatuser.")
return
ifnotreason:
awaitevent.reply("Needareasonforungban.")
return
chats=gbanned.find({})

ifr_sender_id==OWNER_ID:
awaitevent.reply("Fool,howcanIungbanmymaster?")
return
ifr_sender_idinSUDO_USERS:
awaitevent.reply("Heythat'sasudouseridiot.")
return

forcinchats:
ifr_sender_id==c["user"]:
to_check=get_reason(id=r_sender_id)
gbanned.delete_one({"user":r_sender_id})
h=awaitevent.reply("InitiatingUngban")
awaitasyncio.sleep(edit_time)
awaith.edit("UngbannedSuccessfully!")
awaitevent.client.send_message(
GBAN_LOGS,
"**REMOVALOFGLOBALBAN**\n\n**PERMALINK:**[user](tg://user?id={})\n**REMOVER:**`{}`\n**REASON:**`{}`".format(
r_sender_id,event.sender_id,reason
),
)
return
awaitevent.reply("Isthatuserevengbanned?")


@tbot.on(events.ChatAction())
asyncdefjoin_ban(event):
ifevent.chat_id==int(sed):
return
ifevent.chat_id==int(sed):
return
user=event.user_id
chats=gbanned.find({})
forcinchats:
ifuser==c["user"]:
ifevent.user_joined:
try:
to_check=get_reason(id=user)
reason=to_check["reason"]
bannerid=to_check["bannerid"]
awaittbot(EditBannedRequest(event.chat_id,user,BANNED_RIGHTS))
awaitevent.reply(
"Thisuserisgbannedandhasbeenremoved!\n\n**GbannedBy**:`{}`\n**Reason**:`{}`".format(
bannerid,reason
)
)
exceptExceptionase:
print(e)
return


@tbot.on(events.NewMessage(pattern=None))
asyncdeftype_ban(event):
ifevent.chat_id==int(sed):
return
ifevent.chat_id==int(sed):
return
chats=gbanned.find({})
forcinchats:
ifevent.sender_id==c["user"]:
try:
to_check=get_reason(id=event.sender_id)
reason=to_check["reason"]
bannerid=to_check["bannerid"]
awaittbot(
EditBannedRequest(event.chat_id,event.sender_id,BANNED_RIGHTS)
)
awaitevent.reply(
"Thisuserisgbannedandhasbeenremoved!\n\n**GbannedBy**:`{}`\n**Reason**:`{}`".format(
bannerid,reason
)
)
exceptException:
return
