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

frompymongoimportMongoClient
fromtelethonimport*
fromtelethon.tlimport*

fromInerukiimportBOT_ID
fromIneruki.configimportget_str_key
fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbot

MONGO_DB_URI=get_str_key("MONGO_URI",required=True)
client=MongoClient()
client=MongoClient(MONGO_DB_URI)
db=client["Ineruki"]
approved_users=db.approve
dbb=client["Ineruki"]
poll_id=dbb.pollid


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):
returnisinstance(
(
awaittbot(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerChat):
ui=awaittbot.get_peer_id(user)
ps=(
awaittbot(functions.messages.GetFullChatRequest(chat.chat_id))
).full_chat.participants.participants
returnisinstance(
next((pforpinpsifp.user_id==ui),None),
(types.ChatParticipantAdmin,types.ChatParticipantCreator),
)
returnNone


@register(pattern="^/poll(.*)")
asyncdef_(event):
approved_userss=approved_users.find({})
forchinapproved_userss:
iid=ch["id"]
userss=ch["user"]
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
elifevent.chat_id==iidandevent.sender_id==userss:
pass
else:
return
try:
quew=event.pattern_match.group(1)
exceptException:
awaitevent.reply("Whereisthequestion?")
return
if"|"inquew:
secrets,quess,options=quew.split("|")
secret=secrets.strip()

ifnotsecret:
awaitevent.reply("Ineedapollidof5digitstomakeapoll")
return

try:
secret=str(secret)
exceptValueError:
awaitevent.reply("Pollidshouldcontainonlynumbers")
return

#print(secret)

iflen(secret)!=5:
awaitevent.reply("Pollidshouldbeanintegerof5digits")
return

allpoll=poll_id.find({})
#print(secret)
forcinallpoll:
ifevent.sender_id==c["user"]:
awaitevent.reply(
"Pleasestopthepreviouspollbeforecreatinganewone!"
)
return
poll_id.insert_one({"user":event.sender_id,"pollid":secret})

ques=quess.strip()
option=options.strip()
quiz=option.split("")[1-1]
if"True"inquiz:
quizy=True
if"@"inquiz:
one,two=quiz.split("@")
rightone=two.strip()
else:
awaitevent.reply(
"YouneedtoselecttherightanswerwithquestionnumberlikeTrue@1,True@3etc.."
)
return

quizoptionss=[]
try:
ab=option.split("")[4-1]
cd=option.split("")[5-1]
quizoptionss.append(types.PollAnswer(ab,b"1"))
quizoptionss.append(types.PollAnswer(cd,b"2"))
exceptException:
awaitevent.reply("Atleastneedtwooptionstocreateapoll")
return
try:
ef=option.split("")[6-1]
quizoptionss.append(types.PollAnswer(ef,b"3"))
exceptException:
ef=None
try:
gh=option.split("")[7-1]
quizoptionss.append(types.PollAnswer(gh,b"4"))
exceptException:
gh=None
try:
ij=option.split("")[8-1]
quizoptionss.append(types.PollAnswer(ij,b"5"))
exceptException:
ij=None
try:
kl=option.split("")[9-1]
quizoptionss.append(types.PollAnswer(kl,b"6"))
exceptException:
kl=None
try:
mn=option.split("")[10-1]
quizoptionss.append(types.PollAnswer(mn,b"7"))
exceptException:
mn=None
try:
op=option.split("")[11-1]
quizoptionss.append(types.PollAnswer(op,b"8"))
exceptException:
op=None
try:
qr=option.split("")[12-1]
quizoptionss.append(types.PollAnswer(qr,b"9"))
exceptException:
qr=None
try:
st=option.split("")[13-1]
quizoptionss.append(types.PollAnswer(st,b"10"))
exceptException:
st=None

elif"False"inquiz:
quizy=False
else:
awaitevent.reply("Wrongargumentsprovided!")
return

pvote=option.split("")[2-1]
if"True"inpvote:
pvoty=True
elif"False"inpvote:
pvoty=False
else:
awaitevent.reply("Wrongargumentsprovided!")
return
mchoice=option.split("")[3-1]
if"True"inmchoice:
mchoicee=True
elif"False"inmchoice:
mchoicee=False
else:
awaitevent.reply("Wrongargumentsprovided!")
return
optionss=[]
try:
ab=option.split("")[4-1]
cd=option.split("")[5-1]
optionss.append(types.PollAnswer(ab,b"1"))
optionss.append(types.PollAnswer(cd,b"2"))
exceptException:
awaitevent.reply("Atleastneedtwooptionstocreateapoll")
return
try:
ef=option.split("")[6-1]
optionss.append(types.PollAnswer(ef,b"3"))
exceptException:
ef=None
try:
gh=option.split("")[7-1]
optionss.append(types.PollAnswer(gh,b"4"))
exceptException:
gh=None
try:
ij=option.split("")[8-1]
optionss.append(types.PollAnswer(ij,b"5"))
exceptException:
ij=None
try:
kl=option.split("")[9-1]
optionss.append(types.PollAnswer(kl,b"6"))
exceptException:
kl=None
try:
mn=option.split("")[10-1]
optionss.append(types.PollAnswer(mn,b"7"))
exceptException:
mn=None
try:
op=option.split("")[11-1]
optionss.append(types.PollAnswer(op,b"8"))
exceptException:
op=None
try:
qr=option.split("")[12-1]
optionss.append(types.PollAnswer(qr,b"9"))
exceptException:
qr=None
try:
st=option.split("")[13-1]
optionss.append(types.PollAnswer(st,b"10"))
exceptException:
st=None

ifpvotyisFalseandquizyisFalseandmchoiceeisFalse:
awaittbot.send_file(
event.chat_id,
types.InputMediaPoll(
poll=types.Poll(id=12345,question=ques,answers=optionss,quiz=False)
),
)

ifpvotyisTrueandquizyisFalseandmchoiceeisTrue:
awaittbot.send_file(
event.chat_id,
types.InputMediaPoll(
poll=types.Poll(
id=12345,
question=ques,
answers=optionss,
quiz=False,
multiple_choice=True,
public_voters=True,
)
),
)

ifpvotyisFalseandquizyisFalseandmchoiceeisTrue:
awaittbot.send_file(
event.chat_id,
types.InputMediaPoll(
poll=types.Poll(
id=12345,
question=ques,
answers=optionss,
quiz=False,
multiple_choice=True,
public_voters=False,
)
),
)

ifpvotyisTrueandquizyisFalseandmchoiceeisFalse:
awaittbot.send_file(
event.chat_id,
types.InputMediaPoll(
poll=types.Poll(
id=12345,
question=ques,
answers=optionss,
quiz=False,
multiple_choice=False,
public_voters=True,
)
),
)

ifpvotyisFalseandquizyisTrueandmchoiceeisFalse:
awaittbot.send_file(
event.chat_id,
types.InputMediaPoll(
poll=types.Poll(
id=12345,question=ques,answers=quizoptionss,quiz=True
),
correct_answers=[f"{rightone}"],
),
)

ifpvotyisTrueandquizyisTrueandmchoiceeisFalse:
awaittbot.send_file(
event.chat_id,
types.InputMediaPoll(
poll=types.Poll(
id=12345,
question=ques,
answers=quizoptionss,
quiz=True,
public_voters=True,
),
correct_answers=[f"{rightone}"],
),
)

ifpvotyisTrueandquizyisTrueandmchoiceeisTrue:
awaitevent.reply("Youcan'tusemultiplevotingwithquizmode")
return
ifpvotyisFalseandquizyisTrueandmchoiceeisTrue:
awaitevent.reply("Youcan'tusemultiplevotingwithquizmode")
return


@register(pattern="^/stoppoll(.*)")
asyncdefstop(event):
secret=event.pattern_match.group(1)
#print(secret)
approved_userss=approved_users.find({})
forchinapproved_userss:
iid=ch["id"]
userss=ch["user"]
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
elifevent.chat_id==iidandevent.sender_id==userss:
pass
else:
return

ifnotevent.reply_to_msg_id:
awaitevent.reply("Pleasereplytoapolltostopit")
return

ifinputisNone:
awaitevent.reply("Whereisthepollid?")
return

try:
secret=str(secret)
exceptValueError:
awaitevent.reply("Pollidshouldcontainonlynumbers")
return

iflen(secret)!=5:
awaitevent.reply("Pollidshouldbeanintegerof5digits")
return

msg=awaitevent.get_reply_message()

ifstr(msg.sender_id)!=str(BOT_ID):
awaitevent.reply(
"Ican'tdothisoperationonthispoll.\nProbablyit'snotcreatedbyme"
)
return
print(secret)
ifmsg.poll:
allpoll=poll_id.find({})
forcinallpoll:
ifnotevent.sender_id==c["user"]andnotsecret==c["pollid"]:
awaitevent.reply(
"Oops,eitheryouhaven'tcreatedthispolloryouhavegivenwrongpollid"
)
return
ifmsg.poll.poll.closed:
awaitevent.reply("Oops,thepollisalreadyclosed.")
return
poll_id.delete_one({"user":event.sender_id})
pollid=msg.poll.poll.id
awaitmsg.edit(
file=types.InputMediaPoll(
poll=types.Poll(id=pollid,question="",answers=[],closed=True)
)
)
awaitevent.reply("Successfullystoppedthepoll")
else:
awaitevent.reply("Thisisn'tapoll")


@register(pattern="^/forgotpollid$")
asyncdefstop(event):
approved_userss=approved_users.find({})
forchinapproved_userss:
iid=ch["id"]
userss=ch["user"]
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
elifevent.chat_id==iidandevent.sender_id==userss:
pass
else:
return
allpoll=poll_id.find({})
forcinallpoll:
ifevent.sender_id==c["user"]:
try:
poll_id.delete_one({"user":event.sender_id})
awaitevent.reply("Doneyoucannowcreateanewpoll.")
exceptException:
awaitevent.reply("Seemslikeyouhaven'tcreatedanypollyet!")


__help__="""
YoucannowsendpollsanonymouslywithIneruki
Hereishowyoucandoit:
<b>Parameters</b>-
-poll-id-apollidconsistsofan5digitrandominteger,thisidisautomaticallyremovedfromthesystemwhenyoustopyourpreviouspoll
-question-thequestionyouwannaask
-[True@optionnumber/False](1)-quizmode,youmuststatethecorrectanswerwith@eg:True@orTrue@2
-[True/False](2)-publicvotes
-[True/False](3)-multiplechoice
<b>Syntax</b>-
-/poll[poll-id]<i>question</i>|<i>True@optionnumber/False</i>[True/False][True/False][option1][option2]...upto[option10]
<b>Examples</b>-
-/poll12345|amicool?|FalseFalseFalseyesno`
-/poll12345|amicool?|True@1FalseFalseyesno`
<b>Tostopapoll</b>
Replytothepollwith`/stoppoll[poll-id]`tostopthepoll
<b>Fogotpollid</b>
-/forgotpollid-toresetpoll

"""


__mod_name__="Polls"
