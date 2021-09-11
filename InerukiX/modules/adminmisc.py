#Copyright(C)2021Alain&errorshivansh

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

importos
fromtimeimportsleep

fromtelethonimport*
fromtelethonimportevents
fromtelethon.errorsimport*
fromtelethon.errorsimportFloodWaitError
fromtelethon.tlimport*
fromtelethon.tlimportfunctions,types
fromtelethon.tl.functions.channelsimportEditAdminRequest,EditBannedRequest
fromtelethon.tl.typesimport*
fromtelethon.tl.typesimport(
ChatAdminRights,
ChatBannedRights,
MessageEntityMentionName,
)

fromInerukiimportOWNER_ID
fromIneruki.services.telethonimporttbotasbot

#===================CONSTANT===================
PP_TOO_SMOL="**Theimageistoosmall**"
PP_ERROR="**Failurewhileprocessingimage**"
NO_ADMIN="**Iamnotanadmin**"
NO_PERM="**Idon'thavesufficientpermissions!**"

CHAT_PP_CHANGED="**ChatPictureChanged**"
CHAT_PP_ERROR=(
"**Someissuewithupdatingthepic,**"
"**maybeyouaren'tanadmin,**"
"**ordon'thavethedesiredrights.**"
)
INVALID_MEDIA="InvalidExtension"
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
UNBAN_RIGHTS=ChatBannedRights(
until_date=None,
send_messages=None,
send_media=None,
send_stickers=None,
send_gifs=None,
send_games=None,
send_inline=None,
embed_links=None,
)
KICK_RIGHTS=ChatBannedRights(until_date=None,view_messages=True)
MUTE_RIGHTS=ChatBannedRights(until_date=None,send_messages=True)
UNMUTE_RIGHTS=ChatBannedRights(until_date=None,send_messages=False)


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):
returnisinstance(
(
awaitbot(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerUser):
returnTrue


asyncdefcan_promote_users(message):
result=awaitbot(
functions.channels.GetParticipantRequest(
channel=message.chat_id,
user_id=message.sender_id,
)
)
p=result.participant
returnisinstance(p,types.ChannelParticipantCreator)or(
isinstance(p,types.ChannelParticipantAdmin)andp.admin_rights.ban_users
)


asyncdefcan_ban_users(message):
result=awaitbot(
functions.channels.GetParticipantRequest(
channel=message.chat_id,
user_id=message.sender_id,
)
)
p=result.participant
returnisinstance(p,types.ChannelParticipantCreator)or(
isinstance(p,types.ChannelParticipantAdmin)andp.admin_rights.ban_users
)


asyncdefcan_change_info(message):
result=awaitbot(
functions.channels.GetParticipantRequest(
channel=message.chat_id,
user_id=message.sender_id,
)
)
p=result.participant
returnisinstance(p,types.ChannelParticipantCreator)or(
isinstance(p,types.ChannelParticipantAdmin)andp.admin_rights.change_info
)


asyncdefcan_del(message):
result=awaitbot(
functions.channels.GetParticipantRequest(
channel=message.chat_id,
user_id=message.sender_id,
)
)
p=result.participant
returnisinstance(p,types.ChannelParticipantCreator)or(
isinstance(p,types.ChannelParticipantAdmin)andp.admin_rights.delete_messages
)


asyncdefcan_pin_msg(message):
result=awaitbot(
functions.channels.GetParticipantRequest(
channel=message.chat_id,
user_id=message.sender_id,
)
)
p=result.participant
returnisinstance(p,types.ChannelParticipantCreator)or(
isinstance(p,types.ChannelParticipantAdmin)andp.admin_rights.pin_messages
)


asyncdefget_user_sender_id(user,event):
ifisinstance(user,str):
user=int(user)

try:
user_obj=awaitbot.get_entity(user)
except(TypeError,ValueError)aserr:
awaitevent.edit(str(err))
returnNone

returnuser_obj


asyncdefget_user_from_event(event):
"""Gettheuserfromargumentorrepliedmessage."""
ifevent.reply_to_msg_id:
previous_message=awaitevent.get_reply_message()
user_obj=awaitbot.get_entity(previous_message.sender_id)
else:
user=event.pattern_match.group(1)

ifuser.isnumeric():
user=int(user)

ifnotuser:
awaitevent.reply(
"**Idon'tknowwhoyou'retalkingabout,you'regoingtoneedtospecifyauser...!**"
)
return

ifevent.message.entitiesisnotNone:
probable_user_mention_entity=event.message.entities[0]

ifisinstance(probable_user_mention_entity,MessageEntityMentionName):
user_id=probable_user_mention_entity.user_id
user_obj=awaitbot.get_entity(user_id)
returnuser_obj
try:
user_obj=awaitbot.get_entity(user)
except(TypeError,ValueError)aserr:
awaitevent.reply(str(err))
returnNone

returnuser_obj


deffind_instance(items,class_or_tuple):
foriteminitems:
ifisinstance(item,class_or_tuple):
returnitem
returnNone


@bot.on(events.NewMessage(pattern="/lowpromote?(.*)"))
asyncdeflowpromote(promt):
ifpromt.is_group:
ifpromt.sender_id==OWNER_ID:
pass
else:
ifnotawaitcan_promote_users(message=promt):
return
else:
return

user=awaitget_user_from_event(promt)
ifpromt.is_group:
ifawaitis_register_admin(promt.input_chat,user.id):
awaitpromt.reply("**Well!icantpromoteuserwhoisalreadyanadmin**")
return
else:
return

new_rights=ChatAdminRights(
add_admins=False,
invite_users=True,
change_info=False,
ban_users=False,
delete_messages=True,
pin_messages=False,
)

ifuser:
pass
else:
return
quew=promt.pattern_match.group(1)
ifquew:
title=quew
else:
title="Moderator"
#Trytopromoteifcurrentuserisadminorcreator
try:
awaitbot(EditAdminRequest(promt.chat_id,user.id,new_rights,title))
awaitpromt.reply("**Successfullypromoted!**")

#IfTelethonspitBadRequestError,assume
#wedon'thavePromotepermission
exceptException:
awaitpromt.reply("Failedtopromote.")
return


@bot.on(events.NewMessage(pattern="/midpromote?(.*)"))
asyncdefmidpromote(promt):
ifpromt.is_group:
ifpromt.sender_id==OWNER_ID:
pass
else:
ifnotawaitcan_promote_users(message=promt):
return
else:
return

user=awaitget_user_from_event(promt)
ifpromt.is_group:
ifawaitis_register_admin(promt.input_chat,user.id):
awaitpromt.reply("**Well!icantpromoteuserwhoisalreadyanadmin**")
return
else:
return

new_rights=ChatAdminRights(
add_admins=False,
invite_users=True,
change_info=True,
ban_users=False,
delete_messages=True,
pin_messages=True,
)

ifuser:
pass
else:
return
quew=promt.pattern_match.group(1)
ifquew:
title=quew
else:
title="Admin"
#Trytopromoteifcurrentuserisadminorcreator
try:
awaitbot(EditAdminRequest(promt.chat_id,user.id,new_rights,title))
awaitpromt.reply("**Successfullypromoted!**")

#IfTelethonspitBadRequestError,assume
#wedon'thavePromotepermission
exceptException:
awaitpromt.reply("Failedtopromote.")
return


@bot.on(events.NewMessage(pattern="/highpromote?(.*)"))
asyncdefhighpromote(promt):
ifpromt.is_group:
ifpromt.sender_id==OWNER_ID:
pass
else:
ifnotawaitcan_promote_users(message=promt):
return
else:
return

user=awaitget_user_from_event(promt)
ifpromt.is_group:
ifawaitis_register_admin(promt.input_chat,user.id):
awaitpromt.reply("**Well!icantpromoteuserwhoisalreadyanadmin**")
return
else:
return

new_rights=ChatAdminRights(
add_admins=True,
invite_users=True,
change_info=True,
ban_users=True,
delete_messages=True,
pin_messages=True,
)

ifuser:
pass
else:
return
quew=promt.pattern_match.group(1)
ifquew:
title=quew
else:
title="Admin"
#Trytopromoteifcurrentuserisadminorcreator
try:
awaitbot(EditAdminRequest(promt.chat_id,user.id,new_rights,title))
awaitpromt.reply("**Successfullypromoted!**")

#IfTelethonspitBadRequestError,assume
#wedon'thavePromotepermission
exceptException:
awaitpromt.reply("Failedtopromote.")
return


@bot.on(events.NewMessage(pattern="/lowdemote(?:|$)(.*)"))
asyncdeflowdemote(dmod):
ifdmod.is_group:
ifnotawaitcan_promote_users(message=dmod):
return
else:
return

user=awaitget_user_from_event(dmod)
ifdmod.is_group:
ifnotawaitis_register_admin(dmod.input_chat,user.id):
awaitdmod.reply("**Hehe,icantdemotenon-admin**")
return
else:
return

ifuser:
pass
else:
return

#Newrightsafterdemotion
newrights=ChatAdminRights(
add_admins=False,
invite_users=True,
change_info=False,
ban_users=False,
delete_messages=True,
pin_messages=False,
)
#EditAdminPermission
try:
awaitbot(EditAdminRequest(dmod.chat_id,user.id,newrights,"Admin"))
awaitdmod.reply("**DemotedSuccessfully!**")

#IfwecatchBadRequestErrorfromTelethon
#Assumewedon'thavepermissiontodemote
exceptException:
awaitdmod.reply("**Failedtodemote.**")
return


@bot.on(events.NewMessage(pattern="/middemote(?:|$)(.*)"))
asyncdefmiddemote(dmod):
ifdmod.is_group:
ifnotawaitcan_promote_users(message=dmod):
return
else:
return

user=awaitget_user_from_event(dmod)
ifdmod.is_group:
ifnotawaitis_register_admin(dmod.input_chat,user.id):
awaitdmod.reply("**Hehe,icantdemotenon-admin**")
return
else:
return

ifuser:
pass
else:
return

#Newrightsafterdemotion
newrights=ChatAdminRights(
add_admins=False,
invite_users=True,
change_info=True,
ban_users=False,
delete_messages=True,
pin_messages=True,
)
#EditAdminPermission
try:
awaitbot(EditAdminRequest(dmod.chat_id,user.id,newrights,"Admin"))
awaitdmod.reply("**DemotedSuccessfully!**")

#IfwecatchBadRequestErrorfromTelethon
#Assumewedon'thavepermissiontodemote
exceptException:
awaitdmod.reply("**Failedtodemote.**")
return


@bot.on(events.NewMessage(pattern="/users$"))
asyncdefget_users(show):
ifnotshow.is_group:
return
ifshow.is_group:
ifnotawaitis_register_admin(show.input_chat,show.sender_id):
return
info=awaitbot.get_entity(show.chat_id)
title=info.titleifinfo.titleelse"thischat"
mentions="Usersin{}:\n".format(title)
asyncforuserinbot.iter_participants(show.chat_id):
ifnotuser.deleted:
mentions+=f"\n[{user.first_name}](tg://user?id={user.id}){user.id}"
else:
mentions+=f"\nDeletedAccount{user.id}"
file=open("userslist.txt","w+")
file.write(mentions)
file.close()
awaitbot.send_file(
show.chat_id,
"userslist.txt",
caption="Usersin{}".format(title),
reply_to=show.id,
)
os.remove("userslist.txt")


@bot.on(events.NewMessage(pattern="/kickthefools$"))
asyncdef_(event):
ifevent.fwd_from:
return

ifevent.is_group:
ifnotawaitcan_ban_users(message=event):
return
else:
return

#Herelayingthesanitycheck
chat=awaitevent.get_chat()
admin=chat.admin_rights.ban_users
creator=chat.creator

#Well
ifnotadminandnotcreator:
awaitevent.reply("`Idon'thaveenoughpermissions!`")
return

c=0
KICK_RIGHTS=ChatBannedRights(until_date=None,view_messages=True)
done=awaitevent.reply("Working...")
asyncforiinbot.iter_participants(event.chat_id):

ifisinstance(i.status,UserStatusLastMonth):
status=awaittbot(EditBannedRequest(event.chat_id,i,KICK_RIGHTS))
ifnotstatus:
return
c=c+1

ifisinstance(i.status,UserStatusLastWeek):
status=awaittbot(EditBannedRequest(event.chat_id,i,KICK_RIGHTS))
ifnotstatus:
return
c=c+1

ifc==0:
awaitdone.edit("Gotnoonetokick😔")
return

required_string="SuccessfullyKicked**{}**users"
awaitevent.reply(required_string.format(c))


@bot.on(events.NewMessage(pattern="/unbanall$"))
asyncdef_(event):
ifnotevent.is_group:
return

ifevent.is_group:
ifnotawaitcan_ban_users(message=event):
return

#Herelayingthesanitycheck
chat=awaitevent.get_chat()
admin=chat.admin_rights.ban_users
creator=chat.creator

#Well
ifnotadminandnotcreator:
awaitevent.reply("`Idon'thaveenoughpermissions!`")
return

done=awaitevent.reply("SearchingParticipantLists.")
p=0
asyncforiinbot.iter_participants(
event.chat_id,filter=ChannelParticipantsKicked,aggressive=True
):
rights=ChatBannedRights(until_date=0,view_messages=False)
try:
awaitbot(functions.channels.EditBannedRequest(event.chat_id,i,rights))
exceptFloodWaitErrorasex:
logger.warn("sleepingfor{}seconds".format(ex.seconds))
sleep(ex.seconds)
exceptExceptionasex:
awaitevent.reply(str(ex))
else:
p+=1

ifp==0:
awaitdone.edit("Nooneisbannedinthischat")
return
required_string="Successfullyunbanned**{}**users"
awaitevent.reply(required_string.format(p))


@bot.on(events.NewMessage(pattern="/unmuteall$"))
asyncdef_(event):
ifnotevent.is_group:
return
ifevent.is_group:
ifnotawaitcan_ban_users(message=event):
return

#Herelayingthesanitycheck
chat=awaitevent.get_chat()
admin=chat.admin_rights.ban_users
creator=chat.creator

#Well
ifnotadminandnotcreator:
awaitevent.reply("`Idon'thaveenoughpermissions!`")
return

done=awaitevent.reply("Working...")
p=0
asyncforiinbot.iter_participants(
event.chat_id,filter=ChannelParticipantsBanned,aggressive=True
):
rights=ChatBannedRights(
until_date=0,
send_messages=False,
)
try:
awaitbot(functions.channels.EditBannedRequest(event.chat_id,i,rights))
exceptFloodWaitErrorasex:
logger.warn("sleepingfor{}seconds".format(ex.seconds))
sleep(ex.seconds)
exceptExceptionasex:
awaitevent.reply(str(ex))
else:
p+=1

ifp==0:
awaitdone.edit("Nooneismutedinthischat")
return
required_string="Successfullyunmuted**{}**users"
awaitevent.reply(required_string.format(p))


@bot.on(events.NewMessage(pattern="/banme$"))
asyncdefbanme(bon):
ifnotbon.is_group:
return

try:
awaitbot(EditBannedRequest(bon.chat_id,sender,BANNED_RIGHTS))
awaitbon.reply("OkBanned!")

exceptException:
awaitbon.reply("Idon'tthinkso!")
return


@bot.on(events.NewMessage(pattern="/kickme$"))
asyncdefkickme(bon):
ifnotbon.is_group:
return
try:
awaitbot.kick_participant(bon.chat_id,bon.sender_id)
awaitbon.reply("Sure!")
exceptException:
awaitbon.reply("Failedtokick!")
return


@bot.on(events.NewMessage(pattern=r"/setdescription([\s\S]*)"))
asyncdefset_group_des(gpic):
input_str=gpic.pattern_match.group(1)
#print(input_str)
ifgpic.is_group:
ifnotawaitcan_change_info(message=gpic):
return
else:
return

try:
awaitbot(
functions.messages.EditChatAboutRequest(peer=gpic.chat_id,about=input_str)
)
awaitgpic.reply("Successfullysetnewgroupdescription.")
exceptBaseException:
awaitgpic.reply("Failedtosetgroupdescription.")


@bot.on(events.NewMessage(pattern="/setsticker$"))
asyncdefset_group_sticker(gpic):
ifgpic.is_group:
ifnotawaitcan_change_info(message=gpic):
return
else:
return

rep_msg=awaitgpic.get_reply_message()
ifnotrep_msg.document:
awaitgpic.reply("Replytoanystickerplox.")
return
stickerset_attr_s=rep_msg.document.attributes
stickerset_attr=find_instance(stickerset_attr_s,DocumentAttributeSticker)
ifnotstickerset_attr.stickerset:
awaitgpic.reply("Stickerdoesnotbelongtoapack.")
return
try:
id=stickerset_attr.stickerset.id
access_hash=stickerset_attr.stickerset.access_hash
print(id)
print(access_hash)
awaitbot(
functions.channels.SetStickersRequest(
channel=gpic.chat_id,
stickerset=types.InputStickerSetID(id=id,access_hash=access_hash),
)
)
awaitgpic.reply("Groupstickerpacksuccessfullyset!")
exceptExceptionase:
print(e)
awaitgpic.reply("Failedtosetgroupstickerpack.")


asyncdefextract_time(message,time_val):
ifany(time_val.endswith(unit)forunitin("m","h","d")):
unit=time_val[-1]
time_num=time_val[:-1]#type:str
ifnottime_num.isdigit():
awaitmessage.reply("Invalidtimeamountspecified.")
return""

ifunit=="m":
bantime=int(time.time()+int(time_num)*60)
elifunit=="h":
bantime=int(time.time()+int(time_num)*60*60)
elifunit=="d":
bantime=int(time.time()+int(time_num)*24*60*60)
else:
return
returnbantime
else:
awaitmessage.reply(
"Invalidtimetypespecified.Expectedm,h,ord,got:{}".format(
time_val[-1]
)
)
return
