#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
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

importio
importrandom
importre
fromcontextlibimportsuppress
fromdatetimeimportdatetime
fromtypingimportOptional,Union

fromaiogram.dispatcher.filters.builtinimportCommandStart
fromaiogram.dispatcher.filters.stateimportState,StatesGroup
fromaiogram.typesimportCallbackQuery,ContentType,Message
fromaiogram.types.inline_keyboardimportInlineKeyboardButton,InlineKeyboardMarkup
fromaiogram.types.input_mediaimportInputMediaPhoto
fromaiogram.utils.callback_dataimportCallbackData
fromaiogram.utils.exceptionsimport(
BadRequest,
ChatAdminRequired,
MessageCantBeDeleted,
MessageToDeleteNotFound,
)
fromapscheduler.jobstores.baseimportJobLookupError
frombabel.datesimportformat_timedelta
fromcaptcha.imageimportImageCaptcha
fromtelethon.tl.customimportButton

fromInerukiimportBOT_ID,BOT_USERNAME,bot,dp
fromIneruki.configimportget_str_key
fromIneruki.decoratorimportregister
fromIneruki.services.apschedullerimportscheduler
fromIneruki.services.mongoimportdb
fromIneruki.services.redisimportredis
fromIneruki.services.telethonimporttbot
fromIneruki.stuff.fontsimportALL_FONTS

from..utils.cachedimportcached
from.utils.connectionsimportchat_connection
from.utils.languageimportget_strings_dec
from.utils.messageimportconvert_time,need_args_dec
from.utils.notesimportget_parsed_note_list,send_note,t_unparse_note_item
from.utils.restrictionsimportkick_user,mute_user,restrict_user,unmute_user
from.utils.user_detailsimportcheck_admin_rights,get_user_link,is_user_admin


classWelcomeSecurityState(StatesGroup):
button=State()
captcha=State()
math=State()


@register(cmds="welcome")
@chat_connection(only_groups=True)
@get_strings_dec("greetings")
asyncdefwelcome(message,chat,strings):
chat_id=chat["chat_id"]
send_id=message.chat.id

iflen(args:=message.get_args().split())>0:
no_format=Trueif"no_format"==args[0]or"raw"==args[0]elseFalse
else:
no_format=None

ifnot(db_item:=awaitget_greetings_data(chat_id)):
db_item={}
if"note"notindb_item:
db_item["note"]={"text":strings["default_welcome"]}

ifno_format:
awaitmessage.reply(strings["raw_wlcm_note"])
text,kwargs=awaitt_unparse_note_item(
message,db_item["note"],chat_id,noformat=True
)
awaitsend_note(send_id,text,**kwargs)
return

text=strings["welcome_info"]

text=text.format(
chat_name=chat["chat_title"],
welcomes_status=strings["disabled"]
if"welcome_disabled"indb_itemanddb_item["welcome_disabled"]isTrue
elsestrings["enabled"],
wlcm_security=strings["disabled"]
if"welcome_security"notindb_item
ordb_item["welcome_security"]["enabled"]isFalse
elsestrings["wlcm_security_enabled"].format(
level=db_item["welcome_security"]["level"]
),
wlcm_mutes=strings["disabled"]
if"welcome_mute"notindb_itemordb_item["welcome_mute"]["enabled"]isFalse
elsestrings["wlcm_mutes_enabled"].format(time=db_item["welcome_mute"]["time"]),
clean_welcomes=strings["enabled"]
if"clean_welcome"indb_itemanddb_item["clean_welcome"]["enabled"]isTrue
elsestrings["disabled"],
clean_service=strings["enabled"]
if"clean_service"indb_itemanddb_item["clean_service"]["enabled"]isTrue
elsestrings["disabled"],
)
if"welcome_disabled"notindb_item:
text+=strings["wlcm_note"]
awaitmessage.reply(text)
text,kwargs=awaitt_unparse_note_item(message,db_item["note"],chat_id)
awaitsend_note(send_id,text,**kwargs)
else:
awaitmessage.reply(text)

if"welcome_security"indb_item:
if"security_note"notindb_item:
db_item["security_note"]={"text":strings["default_security_note"]}
awaitmessage.reply(strings["security_note"])
text,kwargs=awaitt_unparse_note_item(
message,db_item["security_note"],chat_id
)
awaitsend_note(send_id,text,**kwargs)


@register(cmds=["setwelcome","savewelcome"],user_admin=True)
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("greetings")
asyncdefset_welcome(message,chat,strings):
chat_id=chat["chat_id"]

iflen(args:=message.get_args().lower().split())<1:
db_item=awaitget_greetings_data(chat_id)

if(
db_item
and"welcome_disabled"indb_item
anddb_item["welcome_disabled"]isTrue
):
status=strings["disabled"]
else:
status=strings["enabled"]

awaitmessage.reply(
strings["turnwelcome_status"].format(
status=status,chat_name=chat["chat_title"]
)
)
return

no=["no","off","0","false","disable"]

ifargs[0]inno:
awaitdb.greetings.update_one(
{"chat_id":chat_id},
{"$set":{"chat_id":chat_id,"welcome_disabled":True}},
upsert=True,
)
awaitget_greetings_data.reset_cache(chat_id)
awaitmessage.reply(strings["turnwelcome_disabled"]%chat["chat_title"])
return
else:
note=awaitget_parsed_note_list(message,split_args=-1)

if(
awaitdb.greetings.update_one(
{"chat_id":chat_id},
{
"$set":{"chat_id":chat_id,"note":note},
"$unset":{"welcome_disabled":1},
},
upsert=True,
)
).modified_count>0:
text=strings["updated"]
else:
text=strings["saved"]

awaitget_greetings_data.reset_cache(chat_id)
awaitmessage.reply(text%chat["chat_title"])


@register(cmds="resetwelcome",user_admin=True)
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("greetings")
asyncdefreset_welcome(message,chat,strings):
chat_id=chat["chat_id"]

if(awaitdb.greetings.delete_one({"chat_id":chat_id})).deleted_count<1:
awaitget_greetings_data.reset_cache(chat_id)
awaitmessage.reply(strings["not_found"])
return

awaitget_greetings_data.reset_cache(chat_id)
awaitmessage.reply(strings["deleted"].format(chat=chat["chat_title"]))


@register(cmds="cleanwelcome",user_admin=True)
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("greetings")
asyncdefclean_welcome(message,chat,strings):
chat_id=chat["chat_id"]

iflen(args:=message.get_args().lower().split())<1:
db_item=awaitget_greetings_data(chat_id)

if(
db_item
and"clean_welcome"indb_item
anddb_item["clean_welcome"]["enabled"]isTrue
):
status=strings["enabled"]
else:
status=strings["disabled"]

awaitmessage.reply(
strings["cleanwelcome_status"].format(
status=status,chat_name=chat["chat_title"]
)
)
return

yes=["yes","on","1","true","enable"]
no=["no","off","0","false","disable"]

ifargs[0]inyes:
awaitdb.greetings.update_one(
{"chat_id":chat_id},
{"$set":{"chat_id":chat_id,"clean_welcome":{"enabled":True}}},
upsert=True,
)
awaitget_greetings_data.reset_cache(chat_id)
awaitmessage.reply(strings["cleanwelcome_enabled"]%chat["chat_title"])
elifargs[0]inno:
awaitdb.greetings.update_one(
{"chat_id":chat_id},{"$unset":{"clean_welcome":1}},upsert=True
)
awaitget_greetings_data.reset_cache(chat_id)
awaitmessage.reply(strings["cleanwelcome_disabled"]%chat["chat_title"])
else:
awaitmessage.reply(strings["bool_invalid_arg"])


@register(cmds="cleanservice",user_admin=True)
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("greetings")
asyncdefclean_service(message,chat,strings):
chat_id=chat["chat_id"]

iflen(args:=message.get_args().lower().split())<1:
db_item=awaitget_greetings_data(chat_id)

if(
db_item
and"clean_service"indb_item
anddb_item["clean_service"]["enabled"]isTrue
):
status=strings["enabled"]
else:
status=strings["disabled"]

awaitmessage.reply(
strings["cleanservice_status"].format(
status=status,chat_name=chat["chat_title"]
)
)
return

yes=["yes","on","1","true","enable"]
no=["no","off","0","false","disable"]

ifargs[0]inyes:
awaitdb.greetings.update_one(
{"chat_id":chat_id},
{"$set":{"chat_id":chat_id,"clean_service":{"enabled":True}}},
upsert=True,
)
awaitget_greetings_data.reset_cache(chat_id)
awaitmessage.reply(strings["cleanservice_enabled"]%chat["chat_title"])
elifargs[0]inno:
awaitdb.greetings.update_one(
{"chat_id":chat_id},{"$unset":{"clean_service":1}},upsert=True
)
awaitget_greetings_data.reset_cache(chat_id)
awaitmessage.reply(strings["cleanservice_disabled"]%chat["chat_title"])
else:
awaitmessage.reply(strings["bool_invalid_arg"])


@register(cmds="welcomemute",user_admin=True)
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("greetings")
asyncdefwelcome_mute(message,chat,strings):
chat_id=chat["chat_id"]

iflen(args:=message.get_args().lower().split())<1:
db_item=awaitget_greetings_data(chat_id)

if(
db_item
and"welcome_mute"indb_item
anddb_item["welcome_mute"]["enabled"]isTrue
):
status=strings["enabled"]
else:
status=strings["disabled"]

awaitmessage.reply(
strings["welcomemute_status"].format(
status=status,chat_name=chat["chat_title"]
)
)
return

no=["no","off","0","false","disable"]

ifargs[0].endswith(("m","h","d")):
awaitdb.greetings.update_one(
{"chat_id":chat_id},
{
"$set":{
"chat_id":chat_id,
"welcome_mute":{"enabled":True,"time":args[0]},
}
},
upsert=True,
)
awaitget_greetings_data.reset_cache(chat_id)
text=strings["welcomemute_enabled"]%chat["chat_title"]
try:
awaitmessage.reply(text)
exceptBadRequest:
awaitmessage.answer(text)
elifargs[0]inno:
text=strings["welcomemute_disabled"]%chat["chat_title"]
awaitdb.greetings.update_one(
{"chat_id":chat_id},{"$unset":{"welcome_mute":1}},upsert=True
)
awaitget_greetings_data.reset_cache(chat_id)
try:
awaitmessage.reply(text)
exceptBadRequest:
awaitmessage.answer(text)
else:
text=strings["welcomemute_invalid_arg"]
try:
awaitmessage.reply(text)
exceptBadRequest:
awaitmessage.answer(text)


#WelcomeSecurity

wlcm_sec_config_proc=CallbackData("wlcm_sec_proc","chat_id","user_id","level")
wlcm_sec_config_cancel=CallbackData("wlcm_sec_cancel","user_id","level")


classWelcomeSecurityConf(StatesGroup):
send_time=State()


@register(cmds="welcomesecurity",user_admin=True)
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("greetings")
asyncdefwelcome_security(message,chat,strings):
chat_id=chat["chat_id"]

iflen(args:=message.get_args().lower().split())<1:
db_item=awaitget_greetings_data(chat_id)

if(
db_item
and"welcome_security"indb_item
anddb_item["welcome_security"]["enabled"]isTrue
):
status=strings["welcomesecurity_enabled_word"].format(
level=db_item["welcome_security"]["level"]
)
else:
status=strings["disabled"]

awaitmessage.reply(
strings["welcomesecurity_status"].format(
status=status,chat_name=chat["chat_title"]
)
)
return

no=["no","off","0","false","disable"]

ifargs[0].lower()in["button","math","captcha"]:
level=args[0].lower()
elifargs[0]inno:
awaitdb.greetings.update_one(
{"chat_id":chat_id},{"$unset":{"welcome_security":1}},upsert=True
)
awaitget_greetings_data.reset_cache(chat_id)
awaitmessage.reply(strings["welcomesecurity_disabled"]%chat["chat_title"])
return
else:
awaitmessage.reply(strings["welcomesecurity_invalid_arg"])
return

awaitdb.greetings.update_one(
{"chat_id":chat_id},
{
"$set":{
"chat_id":chat_id,
"welcome_security":{"enabled":True,"level":level},
}
},
upsert=True,
)
awaitget_greetings_data.reset_cache(chat_id)
buttons=InlineKeyboardMarkup()
buttons.add(
InlineKeyboardButton(
strings["no_btn"],
callback_data=wlcm_sec_config_cancel.new(
user_id=message.from_user.id,level=level
),
),
InlineKeyboardButton(
strings["yes_btn"],
callback_data=wlcm_sec_config_proc.new(
chat_id=chat_id,user_id=message.from_user.id,level=level
),
),
)
awaitmessage.reply(
strings["ask_for_time_customization"].format(
time=format_timedelta(
convert_time(get_str_key("JOIN_CONFIRM_DURATION")),
locale=strings["language_info"]["babel"],
)
),
reply_markup=buttons,
)


@register(wlcm_sec_config_cancel.filter(),f="cb",allow_kwargs=True)
@chat_connection(admin=True)
@get_strings_dec("greetings")
asyncdefwelcome_security_config_cancel(
event:CallbackQuery,chat:dict,strings:dict,callback_data:dict,**_
):
ifint(callback_data["user_id"])==event.from_user.idandis_user_admin(
chat["chat_id"],event.from_user.id
):
awaitevent.message.edit_text(
text=strings["welcomesecurity_enabled"].format(
chat_name=chat["chat_title"],level=callback_data["level"]
)
)


@register(wlcm_sec_config_proc.filter(),f="cb",allow_kwargs=True)
@chat_connection(admin=True)
@get_strings_dec("greetings")
asyncdefwelcome_security_config_proc(
event:CallbackQuery,chat:dict,strings:dict,callback_data:dict,**_
):
ifint(callback_data["user_id"])!=event.from_user.idandis_user_admin(
chat["chat_id"],event.from_user.id
):
return

awaitWelcomeSecurityConf.send_time.set()
asyncwithdp.get_current().current_state().proxy()asdata:
data["level"]=callback_data["level"]
awaitevent.message.edit_text(strings["send_time"])


@register(
state=WelcomeSecurityConf.send_time,
content_types=ContentType.TET,
allow_kwargs=True,
)
@chat_connection(admin=True)
@get_strings_dec("greetings")
asyncdefwlcm_sec_time_state(message:Message,chat:dict,strings:dict,state,**_):
asyncwithstate.proxy()asdata:
level=data["level"]
try:
con_time=convert_time(message.text)
except(ValueError,TypeError):
awaitmessage.reply(strings["invalid_time"])
else:
awaitdb.greetings.update_one(
{"chat_id":chat["chat_id"]},
{"$set":{"welcome_security.expire":message.text}},
)
awaitget_greetings_data.reset_cache(chat["chat_id"])
awaitmessage.reply(
strings["welcomesecurity_enabled:customized_time"].format(
chat_name=chat["chat_title"],
level=level,
time=format_timedelta(
con_time,locale=strings["language_info"]["babel"]
),
)
)
finally:
awaitstate.finish()


@register(cmds=["setsecuritynote","sevesecuritynote"],user_admin=True)
@need_args_dec()
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("greetings")
asyncdefset_security_note(message,chat,strings):
chat_id=chat["chat_id"]

ifmessage.get_args().lower().split()[0]in["raw","noformat"]:
db_item=awaitget_greetings_data(chat_id)
if"security_note"notindb_item:
db_item={"security_note":{}}
db_item["security_note"]["text"]=strings["default_security_note"]
db_item["security_note"]["parse_mode"]="md"

text,kwargs=awaitt_unparse_note_item(
message,db_item["security_note"],chat_id,noformat=True
)
kwargs["reply_to"]=message.message_id

awaitsend_note(chat_id,text,**kwargs)
return

note=awaitget_parsed_note_list(message,split_args=-1)

if(
awaitdb.greetings.update_one(
{"chat_id":chat_id},
{"$set":{"chat_id":chat_id,"security_note":note}},
upsert=True,
)
).modified_count>0:
awaitget_greetings_data.reset_cache(chat_id)
text=strings["security_note_updated"]
else:
text=strings["security_note_saved"]

awaitmessage.reply(text%chat["chat_title"])


@register(cmds="delsecuritynote",user_admin=True)
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("greetings")
asyncdefreset_security_note(message,chat,strings):
chat_id=chat["chat_id"]

if(
awaitdb.greetings.update_one(
{"chat_id":chat_id},{"$unset":{"security_note":1}},upsert=True
)
).modified_count>0:
awaitget_greetings_data.reset_cache(chat_id)
text=strings["security_note_updated"]
else:
text=strings["del_security_note_ok"]

awaitmessage.reply(text%chat["chat_title"])


@register(only_groups=True,f="welcome")
@get_strings_dec("greetings")
asyncdefwelcome_security_handler(message:Message,strings):
iflen(message.new_chat_members)>1:
#FIME:AllMightRobotdoesntsupportaddingmultipleuserscurrently
return

new_user=message.new_chat_members[0]
chat_id=message.chat.id
user_id=new_user.id

ifuser_id==BOT_ID:
return

db_item=awaitget_greetings_data(message.chat.id)
ifnotdb_itemor"welcome_security"notindb_item:
return

ifnotawaitcheck_admin_rights(message,chat_id,BOT_ID,["can_restrict_members"]):
awaitmessage.reply(strings["not_admin_ws"])
return

user=awaitmessage.chat.get_member(user_id)
#Checkifuserwasmutedbefore
ifuser["status"]=="restricted":
ifuser["can_send_messages"]isFalse:
return

#CheckonOPsandchatowner
ifawaitis_user_admin(chat_id,user_id):
return

#checkifuseraddedisabot
ifnew_user.is_botandawaitis_user_admin(chat_id,message.from_user.id):
return

if"security_note"notindb_item:
db_item["security_note"]={}
db_item["security_note"]["text"]=strings["default_security_note"]
db_item["security_note"]["parse_mode"]="md"

text,kwargs=awaitt_unparse_note_item(message,db_item["security_note"],chat_id)

kwargs["reply_to"]=(
None
if"clean_service"indb_itemanddb_item["clean_service"]["enabled"]isTrue
elsemessage.message_id
)

kwargs["buttons"]=[]ifnotkwargs["buttons"]elsekwargs["buttons"]
kwargs["buttons"]+=[
Button.inline(strings["click_here"],f"ws_{chat_id}_{user_id}")
]

#FIME:Betterworkaround
ifnot(msg:=awaitsend_note(chat_id,text,**kwargs)):
#Wasn'tabletosentmessage
return

#Muteuser
try:
awaitmute_user(chat_id,user_id)
exceptBadRequestaserror:
#TODO:Deletethe"sent"message^
returnawaitmessage.reply(f"welcomesecurityfaileddueto{error.args[0]}")

redis.set(f"welcome_security_users:{user_id}:{chat_id}",msg.id)

ifraw_time:=db_item["welcome_security"].get("expire",None):
time=convert_time(raw_time)
else:
time=convert_time(get_str_key("JOIN_CONFIRM_DURATION"))

scheduler.add_job(
join_expired,
"date",
id=f"wc_expire:{chat_id}:{user_id}",
run_date=datetime.utcnow()+time,
kwargs={
"chat_id":chat_id,
"user_id":user_id,
"message_id":msg.id,
"wlkm_msg_id":message.message_id,
},
replace_existing=True,
)


asyncdefjoin_expired(chat_id,user_id,message_id,wlkm_msg_id):
user=awaitbot.get_chat_member(chat_id,user_id)
ifuser.status!="restricted":
return

bot_user=awaitbot.get_chat_member(chat_id,BOT_ID)
if(
"can_restrict_members"notinbot_user
orbot_user["can_restrict_members"]isFalse
):
return

key="leave_silent:"+str(chat_id)
redis.set(key,user_id)

awaitunmute_user(chat_id,user_id)
awaitkick_user(chat_id,user_id)
awaittbot.delete_messages(chat_id,[message_id,wlkm_msg_id])


@register(regexp=re.compile(r"ws_"),f="cb")
@get_strings_dec("greetings")
asyncdefws_redirecter(message,strings):
payload=message.data.split("_")[1:]
chat_id=int(payload[0])
real_user_id=int(payload[1])
called_user_id=message.from_user.id

url=f"https://t.me/{BOT_USERNAME}?start=ws_{chat_id}_{called_user_id}_{message.message.message_id}"
ifnotcalled_user_id==real_user_id:
#Thepersonswhicharemutedbeforewonthavetheirsignaturesregisteredoncache
ifnotredis.exists(f"welcome_security_users:{called_user_id}:{chat_id}"):
awaitmessage.answer(strings["not_allowed"],show_alert=True)
return
else:
#Forthosewholosttheirbuttons
url=f"https://t.me/{BOT_USERNAME}?start=ws_{chat_id}_{called_user_id}_{message.message.message_id}_0"
awaitmessage.answer(url=url)


@register(CommandStart(re.compile(r"ws_")),allow_kwargs=True)
@get_strings_dec("greetings")
asyncdefwelcome_security_handler_pm(
message:Message,strings,regexp=None,state=None,**kwargs
):
args=message.get_args().split("_")
chat_id=int(args[1])

asyncwithstate.proxy()asdata:
data["chat_id"]=chat_id
data["msg_id"]=int(args[3])
data["to_delete"]=bool(int(args[4]))iflen(args)>4elseTrue

db_item=awaitget_greetings_data(chat_id)

level=db_item["welcome_security"]["level"]

iflevel=="button":
awaitWelcomeSecurityState.button.set()
awaitsend_button(message,state)

eliflevel=="math":
awaitWelcomeSecurityState.math.set()
awaitsend_btn_math(message,state)

eliflevel=="captcha":
awaitWelcomeSecurityState.captcha.set()
awaitsend_captcha(message,state)


@get_strings_dec("greetings")
asyncdefsend_button(message,state,strings):
text=strings["btn_button_text"]
buttons=InlineKeyboardMarkup().add(
InlineKeyboardButton(strings["click_here"],callback_data="wc_button_btn")
)
verify_msg_id=(awaitmessage.reply(text,reply_markup=buttons)).message_id
asyncwithstate.proxy()asdata:
data["verify_msg_id"]=verify_msg_id


@register(
regexp="wc_button_btn",f="cb",state=WelcomeSecurityState.button,allow_kwargs=True
)
asyncdefwc_button_btn_cb(event,state=None,**kwargs):
awaitwelcome_security_passed(event,state)


defgenerate_captcha(number=None):
ifnotnumber:
number=str(random.randint(10001,99999))
captcha=ImageCaptcha(fonts=ALL_FONTS,width=200,height=100).generate_image(
number
)
img=io.BytesIO()
captcha.save(img,"PNG")
img.seek(0)
returnimg,number


@get_strings_dec("greetings")
asyncdefsend_captcha(message,state,strings):
img,num=generate_captcha()
asyncwithstate.proxy()asdata:
data["captcha_num"]=num
text=strings["ws_captcha_text"].format(
user=awaitget_user_link(message.from_user.id)
)

buttons=InlineKeyboardMarkup().add(
InlineKeyboardButton(
strings["regen_captcha_btn"],callback_data="regen_captcha"
)
)

verify_msg_id=(
awaitmessage.answer_photo(img,caption=text,reply_markup=buttons)
).message_id
asyncwithstate.proxy()asdata:
data["verify_msg_id"]=verify_msg_id


@register(
regexp="regen_captcha",
f="cb",
state=WelcomeSecurityState.captcha,
allow_kwargs=True,
)
@get_strings_dec("greetings")
asyncdefchange_captcha(event,strings,state=None,**kwargs):
message=event.message
asyncwithstate.proxy()asdata:
data["regen_num"]=1if"regen_num"notindataelsedata["regen_num"]+1
regen_num=data["regen_num"]

ifregen_num>3:
img,num=generate_captcha(number=data["captcha_num"])
text=strings["last_chance"]
awaitmessage.edit_media(InputMediaPhoto(img,caption=text))
return

img,num=generate_captcha()
data["captcha_num"]=num

text=strings["ws_captcha_text"].format(
user=awaitget_user_link(event.from_user.id)
)

buttons=InlineKeyboardMarkup().add(
InlineKeyboardButton(
strings["regen_captcha_btn"],callback_data="regen_captcha"
)
)

awaitmessage.edit_media(InputMediaPhoto(img,caption=text),reply_markup=buttons)


@register(f="text",state=WelcomeSecurityState.captcha,allow_kwargs=True)
@get_strings_dec("greetings")
asyncdefcheck_captcha_text(message,strings,state=None,**kwargs):
num=message.text.split("")[0]

ifnotnum.isdigit():
awaitmessage.reply(strings["num_is_not_digit"])
return

asyncwithstate.proxy()asdata:
captcha_num=data["captcha_num"]

ifnotint(num)==int(captcha_num):
awaitmessage.reply(strings["bad_num"])
return

awaitwelcome_security_passed(message,state)


#Btns


defgen_expression():
a=random.randint(1,10)
b=random.randint(1,10)
ifrandom.getrandbits(1):
whilea<b:
b=random.randint(1,10)
answr=a-b
expr=f"{a}-{b}"
else:
b=random.randint(1,10)

answr=a+b
expr=f"{a}+{b}"

returnexpr,answr


defgen_int_btns(answer):
buttons=[]

forain[random.randint(1,20)for_inrange(3)]:
whilea==answer:
a=random.randint(1,20)
buttons.append(Button.inline(str(a),data="wc_int_btn:"+str(a)))

buttons.insert(
random.randint(0,3),
Button.inline(str(answer),data="wc_int_btn:"+str(answer)),
)

returnbuttons


@get_strings_dec("greetings")
asyncdefsend_btn_math(message,state,strings,msg_id=False):
chat_id=message.chat.id
expr,answer=gen_expression()

asyncwithstate.proxy()asdata:
data["num"]=answer

btns=gen_int_btns(answer)

ifmsg_id:
asyncwithstate.proxy()asdata:
data["last"]=True
text=strings["math_wc_rtr_text"]+strings["btn_wc_text"]%expr
else:
text=strings["btn_wc_text"]%expr
msg_id=(awaitmessage.reply(text)).message_id

asyncwithstate.proxy()asdata:
data["verify_msg_id"]=msg_id

awaittbot.edit_message(
chat_id,msg_id,text,buttons=btns
)#TODO:changetoaiogram


@register(
regexp="wc_int_btn:",f="cb",state=WelcomeSecurityState.math,allow_kwargs=True
)
@get_strings_dec("greetings")
asyncdefwc_math_check_cb(event,strings,state=None,**kwargs):
num=int(event.data.split(":")[1])

asyncwithstate.proxy()asdata:
answer=data["num"]
if"last"indata:
awaitstate.finish()
awaitevent.answer(strings["math_wc_sry"],show_alert=True)
awaitevent.message.delete()
return

ifnotnum==answer:
awaitsend_btn_math(event.message,state,msg_id=event.message.message_id)
awaitevent.answer(strings["math_wc_wrong"],show_alert=True)
return

awaitwelcome_security_passed(event,state)


@get_strings_dec("greetings")
asyncdefwelcome_security_passed(
message:Union[CallbackQuery,Message],state,strings
):
user_id=message.from_user.id
asyncwithstate.proxy()asdata:
chat_id=data["chat_id"]
msg_id=data["msg_id"]
verify_msg_id=data["verify_msg_id"]
to_delete=data["to_delete"]

withsuppress(ChatAdminRequired):
awaitunmute_user(chat_id,user_id)

withsuppress(MessageToDeleteNotFound,MessageCantBeDeleted):
ifto_delete:
awaitbot.delete_message(chat_id,msg_id)
awaitbot.delete_message(user_id,verify_msg_id)
awaitstate.finish()

withsuppress(MessageToDeleteNotFound,MessageCantBeDeleted):
message_id=redis.get(f"welcome_security_users:{user_id}:{chat_id}")
#Deletetheperson'srealsecuritybuttonifexists!
ifmessage_id:
awaitbot.delete_message(chat_id,message_id)

redis.delete(f"welcome_security_users:{user_id}:{chat_id}")

withsuppress(JobLookupError):
scheduler.remove_job(f"wc_expire:{chat_id}:{user_id}")

title=(awaitdb.chat_list.find_one({"chat_id":chat_id}))["chat_title"]

if"data"inmessage:
awaitmessage.answer(strings["passed_no_frm"]%title,show_alert=True)
else:
awaitmessage.reply(strings["passed"]%title)

db_item=awaitget_greetings_data(chat_id)

if"message"inmessage:
message=message.message

#Welcome
if"note"indb_itemandnotdb_item.get("welcome_disabled",False):
text,kwargs=awaitt_unparse_note_item(
message.reply_to_message
ifmessage.reply_to_messageisnotNone
elsemessage,
db_item["note"],
chat_id,
)
awaitsend_note(user_id,text,**kwargs)

#Welcomemute
if"welcome_mute"indb_itemanddb_item["welcome_mute"]["enabled"]isnotFalse:
user=awaitbot.get_chat_member(chat_id,user_id)
if"can_send_messages"notinuseroruser["can_send_messages"]isTrue:
awaitrestrict_user(
chat_id,
user_id,
until_date=convert_time(db_item["welcome_mute"]["time"]),
)

chat=awaitdb.chat_list.find_one({"chat_id":chat_id})

buttons=None
ifchat_nick:=chat["chat_nick"]ifchat.get("chat_nick",None)elseNone:
buttons=InlineKeyboardMarkup().add(
InlineKeyboardButton(text=strings["click_here"],url=f"t.me/{chat_nick}")
)

awaitbot.send_message(user_id,strings["verification_done"],reply_markup=buttons)


#EndWelcomeSecurity

#Welcomes
@register(only_groups=True,f="welcome")
@get_strings_dec("greetings")
asyncdefwelcome_trigger(message:Message,strings):
iflen(message.new_chat_members)>1:
#FIME:AllMightRobotdoesntsupportaddingmultipleuserscurrently
return

chat_id=message.chat.id
user_id=message.new_chat_members[0].id

ifuser_id==BOT_ID:
return

ifnot(db_item:=awaitget_greetings_data(message.chat.id)):
db_item={}

if"welcome_disabled"indb_itemanddb_item["welcome_disabled"]isTrue:
return

if"welcome_security"indb_itemanddb_item["welcome_security"]["enabled"]:
return

#Welcome
if"note"notindb_item:
db_item["note"]={"text":strings["default_welcome"],"parse_mode":"md"}
reply_to=(
message.message_id
if"clean_welcome"indb_item
anddb_item["clean_welcome"]["enabled"]isnotFalse
elseNone
)
text,kwargs=awaitt_unparse_note_item(message,db_item["note"],chat_id)
msg=awaitsend_note(chat_id,text,reply_to=reply_to,**kwargs)
#Cleanwelcome
if"clean_welcome"indb_itemanddb_item["clean_welcome"]["enabled"]isnotFalse:
if"last_msg"indb_item["clean_welcome"]:
withsuppress(MessageToDeleteNotFound,MessageCantBeDeleted):
ifvalue:=redis.get(_clean_welcome.format(chat=chat_id)):
awaitbot.delete_message(chat_id,value)
redis.set(_clean_welcome.format(chat=chat_id),msg.id)

#Welcomemute
ifuser_id==BOT_ID:
return
if"welcome_mute"indb_itemanddb_item["welcome_mute"]["enabled"]isnotFalse:
user=awaitbot.get_chat_member(chat_id,user_id)
if"can_send_messages"notinuseroruser["can_send_messages"]isTrue:
ifnotawaitcheck_admin_rights(
message,chat_id,BOT_ID,["can_restrict_members"]
):
awaitmessage.reply(strings["not_admin_wm"])
return

awaitrestrict_user(
chat_id,
user_id,
until_date=convert_time(db_item["welcome_mute"]["time"]),
)


#Cleanservicetrigger
@register(only_groups=True,f="service")
@get_strings_dec("greetings")
asyncdefclean_service_trigger(message,strings):
chat_id=message.chat.id

ifmessage.new_chat_members[0].id==BOT_ID:
return

ifnot(db_item:=awaitget_greetings_data(chat_id)):
return

if"clean_service"notindb_itemordb_item["clean_service"]["enabled"]isFalse:
return

ifnotawaitcheck_admin_rights(message,chat_id,BOT_ID,["can_delete_messages"]):
awaitbot.send_message(chat_id,strings["not_admin_wsr"])
return

withsuppress(MessageToDeleteNotFound,MessageCantBeDeleted):
awaitmessage.delete()


_clean_welcome="cleanwelcome:{chat}"


@cached()
asyncdefget_greetings_data(chat:int)->Optional[dict]:
returnawaitdb.greetings.find_one({"chat_id":chat})


asyncdef__export__(chat_id):
ifgreetings:=awaitget_greetings_data(chat_id):
delgreetings["_id"]
delgreetings["chat_id"]

return{"greetings":greetings}


asyncdef__import__(chat_id,data):
awaitdb.greetings.update_one({"chat_id":chat_id},{"$set":data},upsert=True)
awaitget_greetings_data.reset_cache(chat_id)


__mod_name__="Greetings"

__help__="""
<b>Availablecommands:</b>
<b>General:</b>
-/setwelcomeor/savewelcome:Setwelcome
-/setwelcome(on/off):Disable/enabledwelcomesinyourchat
-/welcome:Showscurrentwelcomessettingsandwelcometext
-/resetwelcome:Resetwelcomessettings
<b>Welcomesecurity:</b>
-/welcomesecurity(level)
Turnsonwelcomesecuritywithspecifiedlevel,eitherbuttonorcaptcha.
Settingupwelcomesecuritywillgiveyouachoicetocustomizejoinexpirationtimeakaminimumtimegiventousertoverifythemselvesnotabot,userswhodonotverifywithinthistimewouldbekicked!
-/welcomesecurity(off/no/0):Disablewelcomesecurity
-/setsecuritynote:Customisethe"Pleasepressbuttonbelowtoverifythemselfashuman!"text
-/delsecuritynote:Resetsecuritytexttodefaults
<b>Availablelevels:</b>
-<code>button</code>:Askusertopress"I'mnotabot"button
-<code>math</code>:Askingtosolvesimplemathquery,fewbuttonswithanswerswillbeprovided,onlyonewillhaverightanswer
-<code>captcha</code>:Askusertoentercaptcha
<b>Welcomemutes:</b>
-/welcomemute(time):Setwelcomemute(nomedia)fortime
-/welcomemute(off/no):Disablewelcomemute
<b>Purges:</b>
-/cleanwelcome(on/off):Deletesoldwelcomemessagesandlastoneafter45mintes
-/cleanservice(on/off):Cleansservicemessages(userjoined)
Ifwelcomesecurityisenabled,userwillbewelcomedwithsecuritytext,ifusersuccessfullyverifyselfasuser,he/shewillbewelcomedalsowithwelcometextinhisPM(topreventspamminginchat).
Ifuserdidn'tverifiedselffor24hourshe/shewillbekickedfromchat.
<b>Addingsbuttonsandvariablestowelcomesorsecuritytext:</b>
Buttonsandvariablessyntaxissameasnotesbuttonsandvariables.
Send/buttonshelpand/variableshelptogetstartedwithusingit.
<b>Settingsimages,gifs,videosorstickersaswelcome:</b>
Savingattachmentsonwelcomeissameassavingnoteswithit,readthenoteshelpaboutit.Butkeepinmindwhatyouhavetoreplace/saveto/setwelcome
<b>Examples:</b>
<code>-Getthewelcomemessagewithoutanyformatting
->/welcomeraw</code>
"""
