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

importpickle
fromdataclassesimportdataclass
fromtypingimportOptional

fromaiogram.dispatcherimportFSMContext
fromaiogram.dispatcher.filters.stateimportState,StatesGroup
fromaiogram.dispatcher.handlerimportCancelHandler
fromaiogram.dispatcher.middlewaresimportBaseMiddleware
fromaiogram.typesimportChatType,InlineKeyboardMarkup
fromaiogram.types.callback_queryimportCallbackQuery
fromaiogram.types.inline_keyboardimportInlineKeyboardButton
fromaiogram.types.messageimportContentType,Message
fromaiogram.utils.callback_dataimportCallbackData
frombabel.datesimportformat_timedelta

fromInerukiimportdp
fromIneruki.decoratorimportregister
fromIneruki.modules.utils.connectionsimportchat_connection
fromIneruki.modules.utils.languageimportget_strings,get_strings_dec
fromIneruki.modules.utils.messageimport(
InvalidTimeUnit,
convert_time,
get_args,
need_args_dec,
)
fromIneruki.modules.utils.restrictionsimportban_user,kick_user,mute_user
fromIneruki.modules.utils.user_detailsimportget_user_link,is_user_admin
fromIneruki.services.mongoimportdb
fromIneruki.services.redisimportbredis,redis
fromIneruki.utils.cachedimportcached
fromIneruki.utils.loggerimportlog

cancel_state=CallbackData("cancel_state","user_id")


classAntiFloodConfigState(StatesGroup):
expiration_proc=State()


classAntiFloodActionState(StatesGroup):
set_time_proc=State()


@dataclass
classCacheModel:
count:int


classAntifloodEnforcer(BaseMiddleware):
state_cache_key="floodstate:{chat_id}"

asyncdefenforcer(self,message:Message,database:dict):
if(not(data:=self.get_flood(message)))orint(
self.get_state(message)
)!=message.from_user.id:
to_set=CacheModel(count=1)
self.insert_flood(to_set,message,database)
self.set_state(message)
returnFalse#weaintbanninganybody

#updatecount
data.count+=1

#checkexceeding
ifdata.count>=database["count"]:
ifawaitself.do_action(message,database):
self.reset_flood(message)
returnTrue

self.insert_flood(data,message,database)
returnFalse

@classmethod
defis_message_valid(cls,message)->bool:
_pre=[ContentType.NEW_CHAT_MEMBERS,ContentType.LEFT_CHAT_MEMBER]
ifmessage.content_typein_pre:
returnFalse
elifmessage.chat.typein(ChatType.PRIVATE,):
returnFalse
returnTrue

defget_flood(self,message)->Optional[CacheModel]:
ifdata:=bredis.get(self.cache_key(message)):
data=pickle.loads(data)
returndata
returnNone

definsert_flood(self,data:CacheModel,message:Message,database:dict):
ex=(
convert_time(database["time"])
ifdatabase.get("time",None)isnotNone
elseNone
)
returnbredis.set(self.cache_key(message),pickle.dumps(data),ex=ex)

defreset_flood(self,message):
returnbredis.delete(self.cache_key(message))

defcheck_flood(self,message):
returnbredis.exists(self.cache_key(message))

defset_state(self,message:Message):
returnbredis.set(
self.state_cache_key.format(chat_id=message.chat.id),message.from_user.id
)

defget_state(self,message:Message):
returnbredis.get(self.state_cache_key.format(chat_id=message.chat.id))

@classmethod
defcache_key(cls,message:Message):
returnf"antiflood:{message.chat.id}:{message.from_user.id}"

@classmethod
asyncdefdo_action(cls,message:Message,database:dict):
action=database["action"]if"action"indatabaseelse"ban"

ifaction=="ban":
returnawaitban_user(message.chat.id,message.from_user.id)
elifaction=="kick":
returnawaitkick_user(message.chat.id,message.from_user.id)
elifaction=="mute":
returnawaitmute_user(message.chat.id,message.from_user.id)
elifaction.startswith("t"):
time=database.get("time",None)
ifnottime:
returnFalse
ifaction=="tmute":
returnawaitmute_user(
message.chat.id,message.from_user.id,until_date=convert_time(time)
)
elifaction=="tban":
returnawaitban_user(
message.chat.id,message.from_user.id,until_date=convert_time(time)
)
else:
returnFalse

asyncdefon_pre_process_message(self,message:Message,_):
log.debug(
f"Enforcingfloodcontrolon{message.from_user.id}in{message.chat.id}"
)
ifself.is_message_valid(message):
ifawaitis_user_admin(message.chat.id,message.from_user.id):
returnself.set_state(message)
if(database:=awaitget_data(message.chat.id))isNone:
return

ifawaitself.enforcer(message,database):
awaitmessage.delete()
strings=awaitget_strings(message.chat.id,"antiflood")
awaitmessage.answer(
strings["flood_exceeded"].format(
action=(
strings[database["action"]]
if"action"indatabase
else"banned"
).capitalize(),
user=awaitget_user_link(message.from_user.id),
)
)
raiseCancelHandler


@register(
cmds=["setflood"],user_can_restrict_members=True,bot_can_restrict_members=True
)
@need_args_dec()
@chat_connection()
@get_strings_dec("antiflood")
asyncdefsetflood_command(message:Message,chat:dict,strings:dict):
try:
args=int(get_args(message)[0])
exceptValueError:
returnawaitmessage.reply(strings["invalid_args:setflood"])
ifargs>200:
returnawaitmessage.reply(strings["overflowed_count"])

awaitAntiFloodConfigState.expiration_proc.set()
redis.set(f"antiflood_setup:{chat['chat_id']}",args)
awaitmessage.reply(
strings["config_proc_1"],
reply_markup=InlineKeyboardMarkup().add(
InlineKeyboardButton(
text=strings["cancel"],
callback_data=cancel_state.new(user_id=message.from_user.id),
)
),
)


@register(
state=AntiFloodConfigState.expiration_proc,
content_types=ContentType.TET,
allow_kwargs=True,
)
@chat_connection()
@get_strings_dec("antiflood")
asyncdefantiflood_expire_proc(
message:Message,chat:dict,strings:dict,state,**_
):
try:
if(time:=message.text)notin(0,"0"):
parsed_time=convert_time(time)#justcallformakingsureitsvalid
else:
time,parsed_time=None,None
except(TypeError,ValueError):
awaitmessage.reply(strings["invalid_time"])
else:
ifnot(data:=redis.get(f'antiflood_setup:{chat["chat_id"]}')):
awaitmessage.reply(strings["setup_corrupted"])
else:
awaitdb.antiflood.update_one(
{"chat_id":chat["chat_id"]},
{"$set":{"time":time,"count":int(data)}},
upsert=True,
)
awaitget_data.reset_cache(chat["chat_id"])
kw={"count":data}
iftimeisnotNone:
kw.update(
{
"time":format_timedelta(
parsed_time,locale=strings["language_info"]["babel"]
)
}
)
awaitmessage.reply(
strings[
"setup_success"iftimeisnotNoneelse"setup_success:no_exp"
].format(**kw)
)
finally:
awaitstate.finish()


@register(cmds=["antiflood","flood"],is_admin=True)
@chat_connection(admin=True)
@get_strings_dec("antiflood")
asyncdefantiflood(message:Message,chat:dict,strings:dict):
ifnot(data:=awaitget_data(chat["chat_id"])):
returnawaitmessage.reply(strings["not_configured"])

ifmessage.get_args().lower()in("off","0","no"):
awaitdb.antiflood.delete_one({"chat_id":chat["chat_id"]})
awaitget_data.reset_cache(chat["chat_id"])
returnawaitmessage.reply(
strings["turned_off"].format(chat_title=chat["chat_title"])
)

ifdata["time"]isNone:
returnawaitmessage.reply(
strings["configuration_info"].format(
action=strings[data["action"]]if"action"indataelsestrings["ban"],
count=data["count"],
)
)
returnawaitmessage.reply(
strings["configuration_info:with_time"].format(
action=strings[data["action"]]if"action"indataelsestrings["ban"],
count=data["count"],
time=format_timedelta(
convert_time(data["time"]),locale=strings["language_info"]["babel"]
),
)
)


@register(cmds=["setfloodaction"],user_can_restrict_members=True)
@need_args_dec()
@chat_connection(admin=True)
@get_strings_dec("antiflood")
asyncdefsetfloodaction(message:Message,chat:dict,strings:dict):
SUPPORTED_ACTIONS=["kick","ban","mute","tmute","tban"]#noqa
if(action:=message.get_args().lower())notinSUPPORTED_ACTIONS:
returnawaitmessage.reply(
strings["invalid_args"].format(
supported_actions=",".join(SUPPORTED_ACTIONS)
)
)

ifaction.startswith("t"):
awaitmessage.reply(
"Sendatimefortaction",allow_sending_without_reply=True
)
redis.set(f"floodactionstate:{chat['chat_id']}",action)
returnawaitAntiFloodActionState.set_time_proc.set()

awaitdb.antiflood.update_one(
{"chat_id":chat["chat_id"]},{"$set":{"action":action}},upsert=True
)
awaitget_data.reset_cache(message.chat.id)
returnawaitmessage.reply(strings["setfloodaction_success"].format(action=action))


@register(
state=AntiFloodActionState.set_time_proc,
user_can_restrict_members=True,
allow_kwargs=True,
)
@chat_connection(admin=True)
@get_strings_dec("antiflood")
asyncdefset_time_config(
message:Message,chat:dict,strings:dict,state:FSMContext,**_
):
ifnot(action:=redis.get(f"floodactionstate:{chat['chat_id']}")):
awaitmessage.reply("setup_corrupted",allow_sending_without_reply=True)
returnawaitstate.finish()
try:
parsed_time=convert_time(
time:=message.text.lower()
)#justcallformakingsureitsvalid
except(TypeError,ValueError,InvalidTimeUnit):
awaitmessage.reply("Invalidtime")
else:
awaitdb.antiflood.update_one(
{"chat_id":chat["chat_id"]},
{"$set":{"action":action,"time":time}},
upsert=True,
)
awaitget_data.reset_cache(chat["chat_id"])
text=strings["setfloodaction_success"].format(action=action)
text+=f"({format_timedelta(parsed_time,locale=strings['language_info']['babel'])})"
awaitmessage.reply(text,allow_sending_without_reply=True)
finally:
awaitstate.finish()


asyncdef__before_serving__(_):
dp.middleware.setup(AntifloodEnforcer())


@register(cancel_state.filter(),f="cb")
asyncdefcancel_state_cb(event:CallbackQuery):
awaitevent.message.delete()


@cached()
asyncdefget_data(chat_id:int):
returnawaitdb.antiflood.find_one({"chat_id":chat_id})


asyncdef__export__(chat_id:int):
data=awaitget_data(chat_id)
ifnotdata:
return

deldata["_id"],data["chat_id"]
returndata


asyncdef__import__(chat_id:int,data:dict):#noqa
awaitdb.antiflood.update_one({"chat_id":chat_id},{"$set":data})


__mod_name__="AntiFlood"

__help__="""
Youknowhowsometimes,peoplejoin,send100messages,andruinyourchat?Withantiflood,thathappensnomore!

Antifloodallowsyoutotakeactiononusersthatsendmorethanxmessagesinarow.

<b>Adminsonly:</b>
-/antiflood:Givesyoucurrentconfigurationofantifloodinthechat
-/antifloodoff:DisablesAntiflood
-/setflood(limit):Setsfloodlimit

Replace(limit)withanyinteger,shouldbelessthan200.Whensettingup,Inerukiwouldaskyoutosendexpirationtime,ifyoudontunderstandwhatthisexpirationtimefor?UserwhosendsspecifiedlimitofmessagesconsecutivelywithinthisTIME,wouldbekicked,bannedwhatevertheactionis.ifyoudontwantthisTIME,wantstotakeactionagainstthosewhoexceedsspecifiedlimitwithoutmatteringTIMEINTERVALbetweenthemessages.youcanreplytoquestionwith0

<b>Configuringthetime:</b>
<code>2m</code>=2minutes
<code>2h</code>=2hours
<code>2d</code>=2days

<b>Example:</b>
Me:<code>/setflood10</code>
Ineruki:<code>Pleasesendexpirationtime[...]</code>
Me:<code>5m</code>(5minutes)
DONE!

-/setfloodaction(action):Setstheactiontotakenwhenuserexceedsfloodlimit

<b>Currentlysupportedactions:</b>
<code>ban</code>
<code>mute</code>
<code>kick</code>
<i>Moresoon™</i>
"""
