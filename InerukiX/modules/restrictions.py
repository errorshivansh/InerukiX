#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2021errorshivansh
#Copyright(C)2020InukaAsith

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

importasyncio
importdatetime#noqa:F401
fromcontextlibimportsuppress

fromaiogram.utils.exceptionsimportMessageNotModified
frombabel.datesimportformat_timedelta

fromInerukiimportBOT_ID,bot
fromIneruki.decoratorimportregister
fromIneruki.services.redisimportredis
fromIneruki.services.telethonimporttbot

from.miscimportcustomise_reason_finish,customise_reason_start
from.utils.connectionsimportchat_connection
from.utils.languageimportget_strings_dec
from.utils.messageimportInvalidTimeUnit,convert_time,get_cmd
from.utils.restrictionsimportban_user,kick_user,mute_user,unban_user,unmute_user
from.utils.user_detailsimport(
get_user_and_text_dec,
get_user_dec,
get_user_link,
is_user_admin,
)


@register(
cmds=["kick","skick"],
bot_can_restrict_members=True,
user_can_restrict_members=True,
)
@chat_connection(admin=True,only_groups=True)
@get_user_and_text_dec()
@get_strings_dec("restrictions")
asyncdefkick_user_cmd(message,chat,user,args,strings):
chat_id=chat["chat_id"]
user_id=user["user_id"]

ifuser_id==BOT_ID:
awaitmessage.reply(strings["kick_Ineruki"])
return

elifuser_id==message.from_user.id:
awaitmessage.reply(strings["kick_self"])
return

elifawaitis_user_admin(chat_id,user_id):
awaitmessage.reply(strings["kick_admin"])
return

text=strings["user_kicked"].format(
user=awaitget_user_link(user_id),
admin=awaitget_user_link(message.from_user.id),
chat_name=chat["chat_title"],
)

#Addreason
ifargs:
text+=strings["reason"]%args

#Checkifsilent
silent=False
ifget_cmd(message)=="skick":
silent=True
key="leave_silent:"+str(chat_id)
redis.set(key,user_id)
redis.expire(key,30)
text+=strings["purge"]

awaitkick_user(chat_id,user_id)

msg=awaitmessage.reply(text)

#Delmsgsifsilent
ifsilent:
to_del=[msg.message_id,message.message_id]
if(
"reply_to_message"inmessage
andmessage.reply_to_message.from_user.id==user_id
):
to_del.append(message.reply_to_message.message_id)
awaitasyncio.sleep(5)
awaittbot.delete_messages(chat_id,to_del)


@register(
cmds=["mute","smute","tmute","stmute"],
bot_can_restrict_members=True,
user_can_restrict_members=True,
)
@chat_connection(admin=True,only_groups=True)
@get_user_and_text_dec()
@get_strings_dec("restrictions")
asyncdefmute_user_cmd(message,chat,user,args,strings):
chat_id=chat["chat_id"]
user_id=user["user_id"]

ifuser_id==BOT_ID:
awaitmessage.reply(strings["mute_Ineruki"])
return

elifuser_id==message.from_user.id:
awaitmessage.reply(strings["mute_self"])
return

elifawaitis_user_admin(chat_id,user_id):
awaitmessage.reply(strings["mute_admin"])
return

text=strings["user_muted"].format(
user=awaitget_user_link(user_id),
admin=awaitget_user_link(message.from_user.id),
chat_name=chat["chat_title"],
)

curr_cmd=get_cmd(message)

#Checkiftemprotary
until_date=None
ifcurr_cmdin("tmute","stmute"):
ifargsisnotNoneandlen(args:=args.split())>0:
try:
until_date=convert_time(args[0])
except(InvalidTimeUnit,TypeError,ValueError):
awaitmessage.reply(strings["invalid_time"])
return

text+=strings["on_time"]%format_timedelta(
until_date,locale=strings["language_info"]["babel"]
)

#Addreason
iflen(args)>1:
text+=strings["reason"]%"".join(args[1:])
else:
awaitmessage.reply(strings["enter_time"])
return
else:
#Addreason
ifargsisnotNoneandlen(args:=args.split())>0:
text+=strings["reason"]%"".join(args[0:])

#Checkifsilent
silent=False
ifcurr_cmdin("smute","stmute"):
silent=True
key="leave_silent:"+str(chat_id)
redis.set(key,user_id)
redis.expire(key,30)
text+=strings["purge"]

awaitmute_user(chat_id,user_id,until_date=until_date)

msg=awaitmessage.reply(text)

#Delmsgsifsilent
ifsilent:
to_del=[msg.message_id,message.message_id]
if(
"reply_to_message"inmessage
andmessage.reply_to_message.from_user.id==user_id
):
to_del.append(message.reply_to_message.message_id)
awaitasyncio.sleep(5)
awaittbot.delete_messages(chat_id,to_del)


@register(cmds="unmute",bot_can_restrict_members=True,user_can_restrict_members=True)
@chat_connection(admin=True,only_groups=True)
@get_user_dec()
@get_strings_dec("restrictions")
asyncdefunmute_user_cmd(message,chat,user,strings):
chat_id=chat["chat_id"]
user_id=user["user_id"]

ifuser_id==BOT_ID:
awaitmessage.reply(strings["unmute_Ineruki"])
return

elifuser_id==message.from_user.id:
awaitmessage.reply(strings["unmute_self"])
return

elifawaitis_user_admin(chat_id,user_id):
awaitmessage.reply(strings["unmute_admin"])
return

awaitunmute_user(chat_id,user_id)

text=strings["user_unmuted"].format(
user=awaitget_user_link(user_id),
admin=awaitget_user_link(message.from_user.id),
chat_name=chat["chat_title"],
)

awaitmessage.reply(text)


@register(
cmds=["ban","sban","tban","stban"],
bot_can_restrict_members=True,
user_can_restrict_members=True,
)
@chat_connection(admin=True,only_groups=True)
@get_user_and_text_dec()
@get_strings_dec("restrictions")
asyncdefban_user_cmd(message,chat,user,args,strings):
chat_id=chat["chat_id"]
user_id=user["user_id"]

ifuser_id==BOT_ID:
awaitmessage.reply(strings["ban_Ineruki"])
return

elifuser_id==message.from_user.id:
awaitmessage.reply(strings["ban_self"])
return

elifawaitis_user_admin(chat_id,user_id):
awaitmessage.reply(strings["ban_admin"])
return

text=strings["user_banned"].format(
user=awaitget_user_link(user_id),
admin=awaitget_user_link(message.from_user.id),
chat_name=chat["chat_title"],
)

curr_cmd=get_cmd(message)

#Checkiftemprotary
until_date=None
ifcurr_cmdin("tban","stban"):
ifargsisnotNoneandlen(args:=args.split())>0:
try:
until_date=convert_time(args[0])
except(InvalidTimeUnit,TypeError,ValueError):
awaitmessage.reply(strings["invalid_time"])
return

text+=strings["on_time"]%format_timedelta(
until_date,locale=strings["language_info"]["babel"]
)

#Addreason
iflen(args)>1:
text+=strings["reason"]%"".join(args[1:])
else:
awaitmessage.reply(strings["enter_time"])
return
else:
#Addreason
ifargsisnotNoneandlen(args:=args.split())>0:
text+=strings["reason"]%"".join(args[0:])

#Checkifsilent
silent=False
ifcurr_cmdin("sban","stban"):
silent=True
key="leave_silent:"+str(chat_id)
redis.set(key,user_id)
redis.expire(key,30)
text+=strings["purge"]

awaitban_user(chat_id,user_id,until_date=until_date)

msg=awaitmessage.reply(text)

#Delmsgsifsilent
ifsilent:
to_del=[msg.message_id,message.message_id]
if(
"reply_to_message"inmessage
andmessage.reply_to_message.from_user.id==user_id
):
to_del.append(message.reply_to_message.message_id)
awaitasyncio.sleep(5)
awaittbot.delete_messages(chat_id,to_del)


@register(cmds="unban",bot_can_restrict_members=True,user_can_restrict_members=True)
@chat_connection(admin=True,only_groups=True)
@get_user_dec()
@get_strings_dec("restrictions")
asyncdefunban_user_cmd(message,chat,user,strings):
chat_id=chat["chat_id"]
user_id=user["user_id"]

ifuser_id==BOT_ID:
awaitmessage.reply(strings["unban_Ineruki"])
return

elifuser_id==message.from_user.id:
awaitmessage.reply(strings["unban_self"])
return

elifawaitis_user_admin(chat_id,user_id):
awaitmessage.reply(strings["unban_admin"])
return

awaitunban_user(chat_id,user_id)

text=strings["user_unband"].format(
user=awaitget_user_link(user_id),
admin=awaitget_user_link(message.from_user.id),
chat_name=chat["chat_title"],
)

awaitmessage.reply(text)


@register(f="leave")
asyncdefleave_silent(message):
ifnotmessage.from_user.id==BOT_ID:
return

ifredis.get("leave_silent:"+str(message.chat.id))==message.left_chat_member.id:
awaitmessage.delete()


@get_strings_dec("restrictions")
asyncdeffilter_handle_ban(message,chat,data:dict,strings=None):
ifawaitis_user_admin(chat["chat_id"],message.from_user.id):
return
ifawaitban_user(chat["chat_id"],message.from_user.id):
reason=data.get("reason",None)orstrings["filter_action_rsn"]
text=strings["filtr_ban_success"]%(
awaitget_user_link(BOT_ID),
awaitget_user_link(message.from_user.id),
reason,
)
awaitbot.send_message(chat["chat_id"],text)


@get_strings_dec("restrictions")
asyncdeffilter_handle_mute(message,chat,data,strings=None):
ifawaitis_user_admin(chat["chat_id"],message.from_user.id):
return
ifawaitmute_user(chat["chat_id"],message.from_user.id):
reason=data.get("reason",None)orstrings["filter_action_rsn"]
text=strings["filtr_mute_success"]%(
awaitget_user_link(BOT_ID),
awaitget_user_link(message.from_user.id),
reason,
)
awaitbot.send_message(chat["chat_id"],text)


@get_strings_dec("restrictions")
asyncdeffilter_handle_tmute(message,chat,data,strings=None):
ifawaitis_user_admin(chat["chat_id"],message.from_user.id):
return
ifawaitmute_user(
chat["chat_id"],message.from_user.id,until_date=eval(data["time"])
):
reason=data.get("reason",None)orstrings["filter_action_rsn"]
time=format_timedelta(
eval(data["time"]),locale=strings["language_info"]["babel"]
)
text=strings["filtr_tmute_success"]%(
awaitget_user_link(BOT_ID),
awaitget_user_link(message.from_user.id),
time,
reason,
)
awaitbot.send_message(chat["chat_id"],text)


@get_strings_dec("restrictions")
asyncdeffilter_handle_tban(message,chat,data,strings=None):
ifawaitis_user_admin(chat["chat_id"],message.from_user.id):
return
ifawaitban_user(
chat["chat_id"],message.from_user.id,until_date=eval(data["time"])
):
reason=data.get("reason",None)orstrings["filter_action_rsn"]
time=format_timedelta(
eval(data["time"]),locale=strings["language_info"]["babel"]
)
text=strings["filtr_tban_success"]%(
awaitget_user_link(BOT_ID),
awaitget_user_link(message.from_user.id),
time,
reason,
)
awaitbot.send_message(chat["chat_id"],text)


@get_strings_dec("restrictions")
asyncdeftime_setup_start(message,strings):
withsuppress(MessageNotModified):
awaitmessage.edit_text(strings["time_setup_start"])


@get_strings_dec("restrictions")
asyncdeftime_setup_finish(message,data,strings):
try:
time=convert_time(message.text)
except(InvalidTimeUnit,TypeError,ValueError):
awaitmessage.reply(strings["invalid_time"])
returnNone
else:
return{"time":repr(time)}


@get_strings_dec("restrictions")
asyncdeffilter_handle_kick(message,chat,data,strings=None):
ifawaitis_user_admin(chat["chat_id"],message.from_user.id):
return
ifawaitkick_user(chat["chat_id"],message.from_user.id):
awaitbot.send_message(
chat["chat_id"],
strings["user_kicked"].format(
user=awaitget_user_link(message.from_user.id),
admin=awaitget_user_link(BOT_ID),
chat_name=chat["chat_title"],
),
)


__filters__={
"ban_user":{
"title":{"module":"restrictions","string":"filter_title_ban"},
"setup":{"start":customise_reason_start,"finish":customise_reason_finish},
"handle":filter_handle_ban,
},
"mute_user":{
"title":{"module":"restrictions","string":"filter_title_mute"},
"setup":{"start":customise_reason_start,"finish":customise_reason_finish},
"handle":filter_handle_mute,
},
"tmute_user":{
"title":{"module":"restrictions","string":"filter_title_tmute"},
"handle":filter_handle_tmute,
"setup":[
{"start":time_setup_start,"finish":time_setup_finish},
{"start":customise_reason_start,"finish":customise_reason_finish},
],
},
"tban_user":{
"title":{"module":"restrictions","string":"filter_title_tban"},
"handle":filter_handle_tban,
"setup":[
{"start":time_setup_start,"finish":time_setup_finish},
{"start":customise_reason_start,"finish":customise_reason_finish},
],
},
"kick_user":{
"title":{"module":"restrictions","string":"filter_title_kick"},
"handle":filter_handle_kick,
},
}


__mod_name__="Restrictions"

__help__="""
Generaladmin'srightsisrestrictusersandcontroltheirruleswiththismoduleyoucaneaselydoit.

<b>Availablecommands:</b>
<b>Kicks:</b>
-/kick:Kicksauser
-/skick:Silentlykicks

<b>Mutes:</b>
-/mute:Mutesauser
-/smute:Silentlymutes
-/tmute(time):Temprotarymuteauser
-/stmute(time):Silentlytemprotarymuteauser
-/unmute:Unmutestheuser

<b>Bans:</b>
-/ban:Bansauser
-/sban:Silentlybans
-/tban(time):Temprotarybanauser
-/stban(time):Silentlytemprotarybanauser
-/unban:Unbanstheuser

<b>Examples:</b>
<code>-Muteauserfortwohours.
->/tmute@username2h</code>


"""
