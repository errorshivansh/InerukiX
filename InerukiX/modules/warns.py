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


importfunctools
importre
fromcontextlibimportsuppress

fromaiogram.typesimportMessage
fromaiogram.types.inline_keyboardimportInlineKeyboardButton,InlineKeyboardMarkup
fromaiogram.utils.deep_linkingimportget_start_link
fromaiogram.utils.exceptionsimportMessageNotModified
frombabel.datesimportformat_timedelta
frombson.objectidimportObjectId

fromInerukiimportBOT_ID,bot
fromIneruki.decoratorimportregister
fromIneruki.services.mongoimportdb
fromIneruki.services.telethonimporttbot

from.miscimportcustomise_reason_finish,customise_reason_start
from.utils.connectionsimportchat_connection
from.utils.languageimportget_strings_dec
from.utils.messageimportInvalidTimeUnit,convert_time
from.utils.restrictionsimportban_user,mute_user
from.utils.user_detailsimport(
get_user_and_text_dec,
get_user_dec,
get_user_link,
is_user_admin,
)


@register(cmds="warn",user_can_restrict_members=True,bot_can_restrict_members=True)
@chat_connection(admin=True,only_groups=True)
@get_user_and_text_dec()
asyncdefwarn_cmd(message,chat,user,text):
awaitwarn_func(message,chat,user,text)


@register(cmds="dwarn",user_can_restrict_members=True,bot_can_restrict_members=True)
@chat_connection(admin=True,only_groups=True)
@get_user_and_text_dec()
asyncdefwarn_cmd(message,chat,user,text):
ifnotmessage.reply_to_message:
awaitmessage.reply(strings["reply_to_msg"])
return
awaitwarn_func(message,chat,user,text)
msgs=[message.message_id,message.reply_to_message.message_id]
awaittbot.delete_messages(message.chat.id,msgs)


@get_strings_dec("warns")
asyncdefwarn_func(message:Message,chat,user,text,strings,filter_action=False):
chat_id=chat["chat_id"]
chat_title=chat["chat_title"]
by_id=BOT_IDiffilter_actionisTrueelsemessage.from_user.id
user_id=user["user_id"]iffilter_actionisFalseelseuser

ifuser_id==BOT_ID:
awaitmessage.reply(strings["warn_sofi"])
return

ifnotfilter_action:
ifuser_id==message.from_user.id:
awaitmessage.reply(strings["warn_self"])
return

ifawaitis_user_admin(chat_id,user_id):
ifnotfilter_action:
awaitmessage.reply(strings["warn_admin"])
return

reason=text
warn_id=str(
(
awaitdb.warns.insert_one(
{
"user_id":user_id,
"chat_id":chat_id,
"reason":str(reason),
"by":by_id,
}
)
).inserted_id
)

admin=awaitget_user_link(by_id)
member=awaitget_user_link(user_id)
text=strings["warn"].format(admin=admin,user=member,chat_name=chat_title)

ifreason:
text+=strings["warn_rsn"].format(reason=reason)

warns_count=awaitdb.warns.count_documents(
{"chat_id":chat_id,"user_id":user_id}
)

buttons=InlineKeyboardMarkup().add(
InlineKeyboardButton(
"⚠️Removewarn",callback_data="remove_warn_{}".format(warn_id)
)
)

ifawaitdb.rules.find_one({"chat_id":chat_id}):
buttons.insert(
InlineKeyboardButton(
"📝Rules",url=awaitget_start_link(f"btn_rules_{chat_id}")
)
)

ifwarn_limit:=awaitdb.warnlimit.find_one({"chat_id":chat_id}):
max_warn=int(warn_limit["num"])
else:
max_warn=3

iffilter_action:
action=functools.partial(bot.send_message,chat_id=chat_id)
elifmessage.reply_to_message:
action=message.reply_to_message.reply
else:
action=functools.partial(message.reply,disable_notification=True)

ifwarns_count>=max_warn:
ifawaitmax_warn_func(chat_id,user_id):
awaitdb.warns.delete_many({"user_id":user_id,"chat_id":chat_id})
data=awaitdb.warnmode.find_one({"chat_id":chat_id})
ifdataisnotNone:
ifdata["mode"]=="tmute":
text=strings["max_warn_exceeded:tmute"].format(
user=member,
time=format_timedelta(
convert_time(data["time"]),
locale=strings["language_info"]["babel"],
),
)
else:
text=strings["max_warn_exceeded"].format(
user=member,
action=strings["banned"]
ifdata["mode"]=="ban"
elsestrings["muted"],
)
returnawaitaction(text=text)
returnawaitaction(
text=strings["max_warn_exceeded"].format(
user=member,action=strings["banned"]
)
)
text+=strings["warn_num"].format(curr_warns=warns_count,max_warns=max_warn)
returnawaitaction(text=text,reply_markup=buttons,disable_web_page_preview=True)


@register(
regexp=r"remove_warn_(.*)",
f="cb",
allow_kwargs=True,
user_can_restrict_members=True,
)
@get_strings_dec("warns")
asyncdefrmv_warn_btn(event,strings,regexp=None,**kwargs):
warn_id=ObjectId(re.search(r"remove_warn_(.*)",str(regexp)).group(1)[:-2])
user_id=event.from_user.id
admin_link=awaitget_user_link(user_id)
awaitdb.warns.delete_one({"_id":warn_id})
withsuppress(MessageNotModified):
awaitevent.message.edit_text(
strings["warn_btn_rmvl_success"].format(admin=admin_link)
)


@register(cmds="warns")
@chat_connection(admin=True,only_groups=True)
@get_user_dec(allow_self=True)
@get_strings_dec("warns")
asyncdefwarns(message,chat,user,strings):
chat_id=chat["chat_id"]
user_id=user["user_id"]
text=strings["warns_header"]
user_link=awaitget_user_link(user_id)

count=0
asyncforwarnindb.warns.find({"user_id":user_id,"chat_id":chat_id}):
count+=1
by=awaitget_user_link(warn["by"])
rsn=warn["reason"]
reason=f"<code>{rsn}</code>"
ifnotrsnorrsn=="None":
reason="<i>NoReason</i>"
text+=strings["warns"].format(count=count,reason=reason,admin=by)

ifcount==0:
awaitmessage.reply(strings["no_warns"].format(user=user_link))
return

awaitmessage.reply(text,disable_notification=True)


@register(cmds="warnlimit",user_admin=True)
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("warns")
asyncdefwarnlimit(message,chat,strings):
chat_id=chat["chat_id"]
chat_title=chat["chat_title"]
arg=message.get_args().split()

ifnotarg:
ifcurrent_limit:=awaitdb.warnlimit.find_one({"chat_id":chat_id}):
num=current_limit["num"]
else:
num=3#Defaultvalue
awaitmessage.reply(strings["warn_limit"].format(chat_name=chat_title,num=num))
elifnotarg[0].isdigit():
returnawaitmessage.reply(strings["not_digit"])
else:
ifint(arg[0])<2:
returnawaitmessage.reply(strings["warnlimit_short"])

elifint(arg[0])>10000:#Maxvalue
returnawaitmessage.reply(strings["warnlimit_long"])

new={"chat_id":chat_id,"num":int(arg[0])}

awaitdb.warnlimit.update_one({"chat_id":chat_id},{"$set":new},upsert=True)
awaitmessage.reply(strings["warnlimit_updated"].format(num=int(arg[0])))


@register(cmds=["resetwarns","delwarns"],user_can_restrict_members=True)
@chat_connection(admin=True,only_groups=True)
@get_user_dec()
@get_strings_dec("warns")
asyncdefreset_warn(message,chat,user,strings):
chat_id=chat["chat_id"]
chat_title=chat["chat_title"]
user_id=user["user_id"]
user_link=awaitget_user_link(user_id)
admin_link=awaitget_user_link(message.from_user.id)

ifuser_id==BOT_ID:
awaitmessage.reply(strings["rst_wrn_sofi"])
return

ifawaitdb.warns.find_one({"chat_id":chat_id,"user_id":user_id}):
deleted=awaitdb.warns.delete_many({"chat_id":chat_id,"user_id":user_id})
purged=deleted.deleted_count
awaitmessage.reply(
strings["purged_warns"].format(
admin=admin_link,num=purged,user=user_link,chat_title=chat_title
)
)
else:
awaitmessage.reply(strings["usr_no_wrn"].format(user=user_link))


@register(
cmds=["warnmode","warnaction"],user_admin=True,bot_can_restrict_members=True
)
@chat_connection(admin=True)
@get_strings_dec("warns")
asyncdefwarnmode(message,chat,strings):
chat_id=chat["chat_id"]
acceptable_args=["ban","tmute","mute"]
arg=str(message.get_args()).split()
new={"chat_id":chat_id}

ifargandarg[0]inacceptable_args:
option="".join(arg[0])
if(
data:=awaitdb.warnmode.find_one({"chat_id":chat_id})
)isnotNoneanddata["mode"]==option:
returnawaitmessage.reply(strings["same_mode"])
ifarg[0]==acceptable_args[0]:
new["mode"]=option
awaitdb.warnmode.update_one(
{"chat_id":chat_id},{"$set":new},upsert=True
)
elifarg[0]==acceptable_args[1]:
try:
time=arg[1]
exceptIndexError:
returnawaitmessage.reply(strings["no_time"])
else:
try:
#TODO:ForbetterUwehavetoshowuntiltimeoftmutewhenactionisdone.
#Wecan'tstoretimedeltaclassinmongodb;Herewecheckvalidityofgiventime.
convert_time(time)
except(InvalidTimeUnit,TypeError,ValueError):
returnawaitmessage.reply(strings["invalid_time"])
else:
new.update(mode=option,time=time)
awaitdb.warnmode.update_one(
{"chat_id":chat_id},{"$set":new},upsert=True
)
elifarg[0]==acceptable_args[2]:
new["mode"]=option
awaitdb.warnmode.update_one(
{"chat_id":chat_id},{"$set":new},upsert=True
)
awaitmessage.reply(strings["warnmode_success"]%(chat["chat_title"],option))
else:
text=""
if(curr_mode:=awaitdb.warnmode.find_one({"chat_id":chat_id}))isnotNone:
mode=curr_mode["mode"]
text+=strings["mode_info"]%mode
text+=strings["wrng_args"]
text+="\n".join([f"-{i}"foriinacceptable_args])
awaitmessage.reply(text)


asyncdefmax_warn_func(chat_id,user_id):
if(data:=awaitdb.warnmode.find_one({"chat_id":chat_id}))isnotNone:
ifdata["mode"]=="ban":
returnawaitban_user(chat_id,user_id)
elifdata["mode"]=="tmute":
time=convert_time(data["time"])
returnawaitmute_user(chat_id,user_id,time)
elifdata["mode"]=="mute":
returnawaitmute_user(chat_id,user_id)
else:#Default
returnawaitban_user(chat_id,user_id)


asyncdef__export__(chat_id):
ifdata:=awaitdb.warnlimit.find_one({"chat_id":chat_id}):
number=data["num"]
else:
number=3

ifwarnmode_data:=awaitdb.warnmode.find_one({"chat_id":chat_id}):
delwarnmode_data["chat_id"],warnmode_data["_id"]
else:
warnmode_data=None

return{"warns":{"warns_limit":number,"warn_mode":warnmode_data}}


asyncdef__import__(chat_id,data):
if"warns_limit"indata:
number=data["warns_limit"]
ifnumber<2:
return

elifnumber>10000:#Maxvalue
return

awaitdb.warnlimit.update_one(
{"chat_id":chat_id},{"$set":{"num":number}},upsert=True
)

if(data:=data["warn_mode"])isnotNone:
awaitdb.warnmode.update_one({"chat_id":chat_id},{"$set":data},upsert=True)


@get_strings_dec("warns")
asyncdeffilter_handle(message,chat,data,string=None):
ifawaitis_user_admin(chat["chat_id"],message.from_user.id):
return
target_user=message.from_user.id
text=data.get("reason",None)orstring["filter_handle_rsn"]
awaitwarn_func(message,chat,target_user,text,filter_action=True)


__filters__={
"warn_user":{
"title":{"module":"warns","string":"filters_title"},
"setup":{"start":customise_reason_start,"finish":customise_reason_finish},
"handle":filter_handle,
}
}


__mod_name__="Warnings"

__help__="""
Youcankeepyourmembersfromgettingoutofcontrolusingthisfeature!

<b>Availablecommands:</b>
<b>General(Admins):</b>
-/warn(?user)(?reason):Usethiscommandtowarntheuser!youcanmentionorreplytotheoffendeduserandaddreasonifneeded
-/delwarnsor/resetwarns:Thiscommandisusedtodeleteallthewarnsusergotsofarinthechat
-/dwarn[reply]:Deletetherepliedmessageandwarnhim
<b>Warnlimt(Admins):</b>
-/warnlimit(newlimit):Setsawarnlimit
Notallchatswanttogivesamemaximumwarnstotheuser,right?Thiscommandwillhelpyoutomodifydefaultmaximumwarns.Defaultis3

Thewarnlimitshouldbegreaterthan<code>1</code>andlessthan<code>10,000</code>

<b>Warnaction(Admins):</b>
/warnaction(mode)(?time)
Wellagain,notallchatswanttoban(default)userswhenexceedmaximumwarnssothiscommandwillabletomodifythat.
Currentsupportedactionsare<code>ban</code>(defaultone),<code>mute</code>,<code>tmute</code>.Thetmutemoderequire<code>time</code>argumentasyouguessed.

<b>Availableforallusers:</b>
/warns(?user)
Usethiscommandtoknownumberofwarnsandinformationaboutwarnsyougotsofarinthechat.Touseyourselfyoudoesn'trequireuserargument.
"""
