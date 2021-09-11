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
importfunctools
importrandom
importre
fromcontextlibimportsuppress
fromstringimportprintable

importregex
fromaiogram.dispatcher.filters.stateimportState,StatesGroup
fromaiogram.typesimportCallbackQuery,Message
fromaiogram.types.inline_keyboardimportInlineKeyboardButton,InlineKeyboardMarkup
fromaiogram.utils.callback_dataimportCallbackData
fromaiogram.utils.exceptionsimportMessageCantBeDeleted,MessageToDeleteNotFound
fromasync_timeoutimporttimeout
frombson.objectidimportObjectId
frompymongoimportUpdateOne

fromInerukiimportbot,loop
fromIneruki.decoratorimportregister
fromIneruki.modulesimportLOADED_MODULES
fromIneruki.services.mongoimportdb
fromIneruki.services.redisimportredis
fromIneruki.utils.loggerimportlog

from.utils.connectionsimportchat_connection,get_connected_chat
from.utils.languageimportget_string,get_strings_dec
from.utils.messageimportget_args_str,need_args_dec
from.utils.user_detailsimportis_chat_creator,is_user_admin

filter_action_cp=CallbackData("filter_action_cp","filter_id")
filter_remove_cp=CallbackData("filter_remove_cp","id")
filter_delall_yes_cb=CallbackData("filter_delall_yes_cb","chat_id")

FILTERS_ACTIONS={}


classNewFilter(StatesGroup):
handler=State()
setup=State()


asyncdefupdate_handlers_cache(chat_id):
redis.delete(f"filters_cache_{chat_id}")
filters=db.filters.find({"chat_id":chat_id})
handlers=[]
asyncforfilterinfilters:
handler=filter["handler"]
ifhandlerinhandlers:
continue

handlers.append(handler)
redis.lpush(f"filters_cache_{chat_id}",handler)

returnhandlers


@register()
asyncdefcheck_msg(message):
log.debug("Runningcheckmsgforfiltersfunction.")
chat=awaitget_connected_chat(message,only_groups=True)
if"err_msg"inchatormessage.chat.type=="private":
return

chat_id=chat["chat_id"]
ifnot(filters:=redis.lrange(f"filters_cache_{chat_id}",0,-1)):
filters=awaitupdate_handlers_cache(chat_id)

iflen(filters)==0:
return

text=message.text

#Workaroundtodisableallfiltersifadminwanttoremovefilter
ifawaitis_user_admin(chat_id,message.from_user.id):
iftext[1:].startswith("addfilter")ortext[1:].startswith("delfilter"):
return

forhandlerinfilters:#type:str
ifhandler.startswith("re:"):
func=functools.partial(
regex.search,handler.replace("re:","",1),text,timeout=0.1
)
else:
#TODO:Removethis(handler.replace(...)).keptforbackwardcompatibility
func=functools.partial(
re.search,
re.escape(handler).replace("(+)","(.*)"),
text,
flags=re.IGNORECASE,
)

try:
asyncwithtimeout(0.1):
matched=awaitloop.run_in_executor(None,func)
except(asyncio.TimeoutError,TimeoutError):
continue

ifmatched:
#Wecanhavefewfilterswithsamehandler,that'swhywecreateanewloop.
filters=db.filters.find({"chat_id":chat_id,"handler":handler})
asyncforfilterinfilters:
action=filter["action"]
awaitFILTERS_ACTIONS[action]["handle"](message,chat,filter)


@register(cmds=["addfilter","newfilter"],is_admin=True,user_can_change_info=True)
@need_args_dec()
@chat_connection(only_groups=True,admin=True)
@get_strings_dec("filters")
asyncdefadd_handler(message,chat,strings):
#filtersdoesn'tsupportanonadmins
ifmessage.from_user.id==1087968824:
returnawaitmessage.reply(strings["anon_detected"])
#ifnotawaitcheck_admin_rights(message,chat_id,message.from_user.id,["can_change_info"]):
#returnawaitmessage.reply("Youcan'tchangeinfoofthisgroup")

handler=get_args_str(message)

ifhandler.startswith("re:"):
pattern=handler
random_text_str="".join(random.choice(printable)foriinrange(50))
try:
regex.match(pattern,random_text_str,timeout=0.2)
exceptTimeoutError:
awaitmessage.reply(strings["regex_too_slow"])
return
else:
handler=handler.lower()

text=strings["adding_filter"].format(
handler=handler,chat_name=chat["chat_title"]
)

buttons=InlineKeyboardMarkup(row_width=2)
foractioninFILTERS_ACTIONS.items():
filter_id=action[0]
data=action[1]

buttons.insert(
InlineKeyboardButton(
awaitget_string(
chat["chat_id"],data["title"]["module"],data["title"]["string"]
),
callback_data=filter_action_cp.new(filter_id=filter_id),
)
)
buttons.add(InlineKeyboardButton(strings["cancel_btn"],callback_data="cancel"))

user_id=message.from_user.id
chat_id=chat["chat_id"]
redis.set(f"add_filter:{user_id}:{chat_id}",handler)
ifhandlerisnotNone:
awaitmessage.reply(text,reply_markup=buttons)


asyncdefsave_filter(message,data,strings):
ifawaitdb.filters.find_one(data):
#preventsavingduplicatefilter
awaitmessage.reply("Duplicatefilter!")
return

awaitdb.filters.insert_one(data)
awaitupdate_handlers_cache(data["chat_id"])
awaitmessage.reply(strings["saved"])


@register(filter_action_cp.filter(),f="cb",allow_kwargs=True)
@chat_connection(only_groups=True,admin=True)
@get_strings_dec("filters")
asyncdefregister_action(
event,chat,strings,callback_data=None,state=None,**kwargs
):
ifnotawaitis_user_admin(event.message.chat.id,event.from_user.id):
returnawaitevent.answer("Youarenotadmintodothis")
filter_id=callback_data["filter_id"]
action=FILTERS_ACTIONS[filter_id]

user_id=event.from_user.id
chat_id=chat["chat_id"]

handler=redis.get(f"add_filter:{user_id}:{chat_id}")

ifnothandler:
returnawaitevent.answer(
"Somethingwentwrong!Pleasetryagain!",show_alert=True
)

data={"chat_id":chat_id,"handler":handler,"action":filter_id}

if"setup"inaction:
awaitNewFilter.setup.set()
setup_co=len(action["setup"])-1iftype(action["setup"])islistelse0
asyncwithstate.proxy()asproxy:
proxy["data"]=data
proxy["filter_id"]=filter_id
proxy["setup_co"]=setup_co
proxy["setup_done"]=0
proxy["msg_id"]=event.message.message_id

ifsetup_co>0:
awaitaction["setup"][0]["start"](event.message)
else:
awaitaction["setup"]["start"](event.message)
return

awaitsave_filter(event.message,data,strings)


@register(state=NewFilter.setup,f="any",is_admin=True,allow_kwargs=True)
@chat_connection(only_groups=True,admin=True)
@get_strings_dec("filters")
asyncdefsetup_end(message,chat,strings,state=None,**kwargs):
asyncwithstate.proxy()asproxy:
data=proxy["data"]
filter_id=proxy["filter_id"]
setup_co=proxy["setup_co"]
curr_step=proxy["setup_done"]
withsuppress(MessageCantBeDeleted,MessageToDeleteNotFound):
awaitbot.delete_message(message.chat.id,proxy["msg_id"])

action=FILTERS_ACTIONS[filter_id]

func=(
action["setup"][curr_step]["finish"]
iftype(action["setup"])islist
elseaction["setup"]["finish"]
)
ifnotbool(a:=awaitfunc(message,data)):
awaitstate.finish()
return

data.update(a)

ifsetup_co>0:
awaitaction["setup"][curr_step+1]["start"](message)
asyncwithstate.proxy()asproxy:
proxy["data"]=data
proxy["setup_co"]-=1
proxy["setup_done"]+=1
return

awaitstate.finish()
awaitsave_filter(message,data,strings)


@register(cmds=["filters","listfilters"])
@chat_connection(only_groups=True)
@get_strings_dec("filters")
asyncdeflist_filters(message,chat,strings):
text=strings["list_filters"].format(chat_name=chat["chat_title"])

filters=db.filters.find({"chat_id":chat["chat_id"]})
filters_text=""
asyncforfilterinfilters:
filters_text+=f"-{filter['handler']}:{filter['action']}\n"

ifnotfilters_text:
awaitmessage.reply(
strings["no_filters_found"].format(chat_name=chat["chat_title"])
)
return

awaitmessage.reply(text+filters_text)


@register(cmds="delfilter",is_admin=True,user_can_change_info=True)
@need_args_dec()
@chat_connection(only_groups=True,admin=True)
@get_strings_dec("filters")
asyncdefdel_filter(message,chat,strings):
handler=get_args_str(message)
chat_id=chat["chat_id"]
filters=awaitdb.filters.find({"chat_id":chat_id,"handler":handler}).to_list(
9999
)
ifnotfilters:
awaitmessage.reply(
strings["no_such_filter"].format(chat_name=chat["chat_title"])
)
return

#Removefilterincaseifwefoundonly1filterwithsameheader
filter=filters[0]
iflen(filters)==1:
awaitdb.filters.delete_one({"_id":filter["_id"]})
awaitupdate_handlers_cache(chat_id)
awaitmessage.reply(strings["del_filter"].format(handler=filter["handler"]))
return

#Buildkeyboardrowforselectwhichexactlyfilteruserwanttoremove
buttons=InlineKeyboardMarkup(row_width=1)
text=strings["select_filter_to_remove"].format(handler=handler)
forfilterinfilters:
action=FILTERS_ACTIONS[filter["action"]]
buttons.add(
InlineKeyboardButton(
#Ifmodule'sfiltersupportcustomdelbtnnameselsejustshowactionname
""+action["del_btn_name"](message,filter)
if"del_btn_name"inaction
elsefilter["action"],
callback_data=filter_remove_cp.new(id=str(filter["_id"])),
)
)

awaitmessage.reply(text,reply_markup=buttons)


@register(filter_remove_cp.filter(),f="cb",allow_kwargs=True)
@chat_connection(only_groups=True,admin=True)
@get_strings_dec("filters")
asyncdefdel_filter_cb(event,chat,strings,callback_data=None,**kwargs):
ifnotawaitis_user_admin(event.message.chat.id,event.from_user.id):
returnawaitevent.answer("Youarenotadmintodothis")
filter_id=ObjectId(callback_data["id"])
filter=awaitdb.filters.find_one({"_id":filter_id})
awaitdb.filters.delete_one({"_id":filter_id})
awaitupdate_handlers_cache(chat["chat_id"])
awaitevent.message.edit_text(
strings["del_filter"].format(handler=filter["handler"])
)
return


@register(cmds=["delfilters","delallfilters"])
@get_strings_dec("filters")
asyncdefdelall_filters(message:Message,strings:dict):
ifnotawaitis_chat_creator(message,message.chat.id,message.from_user.id):
returnawaitmessage.reply(strings["not_chat_creator"])
buttons=InlineKeyboardMarkup()
buttons.add(
*[
InlineKeyboardButton(
strings["confirm_yes"],
callback_data=filter_delall_yes_cb.new(chat_id=message.chat.id),
),
InlineKeyboardButton(
strings["confirm_no"],callback_data="filter_delall_no_cb"
),
]
)
returnawaitmessage.reply(strings["delall_header"],reply_markup=buttons)


@register(filter_delall_yes_cb.filter(),f="cb",allow_kwargs=True)
@get_strings_dec("filters")
asyncdefdelall_filters_yes(
event:CallbackQuery,strings:dict,callback_data:dict,**_
):
ifnotawaitis_chat_creator(
event,chat_id:=int(callback_data["chat_id"]),event.from_user.id
):
returnFalse
result=awaitdb.filters.delete_many({"chat_id":chat_id})
awaitupdate_handlers_cache(chat_id)
returnawaitevent.message.edit_text(
strings["delall_success"].format(count=result.deleted_count)
)


@register(regexp="filter_delall_no_cb",f="cb")
@get_strings_dec("filters")
asyncdefdelall_filters_no(event:CallbackQuery,strings:dict):
ifnotawaitis_chat_creator(event,event.message.chat.id,event.from_user.id):
returnFalse
awaitevent.message.delete()


asyncdef__before_serving__(loop):
log.debug("Addingfiltersactions")
formoduleinLOADED_MODULES:
ifnotgetattr(module,"__filters__",None):
continue

module_name=module.__name__.split(".")[-1]
log.debug(f"Addingfilteractionfrom{module_name}module")
fordatainmodule.__filters__.items():
FILTERS_ACTIONS[data[0]]=data[1]


asyncdef__export__(chat_id):
data=[]
filters=db.filters.find({"chat_id":chat_id})
asyncforfilterinfilters:
delfilter["_id"],filter["chat_id"]
if"time"infilter:
filter["time"]=str(filter["time"])
data.append(filter)

return{"filters":data}


asyncdef__import__(chat_id,data):
new=[]
forfilterindata:
new.append(
UpdateOne(
{
"chat_id":chat_id,
"handler":filter["handler"],
"action":filter["action"],
},
{"$set":filter},
upsert=True,
)
)
awaitdb.filters.bulk_write(new)
awaitupdate_handlers_cache(chat_id)


__mod_name__="Filters"

__help__="""
<b>GENERALFILTERS</b>
Filtermoduleisgreatforeverything!filterinhereisusedtofilterwordsorsentencesinyourchat-sendnotes,warn,banthose!
<i>General(Admins):</i>
-/addfilter(word/sentence):Thisisusedtoaddfilters.
-/delfilter(word/sentence):Usethiscommandtoremoveaspecificfilter.
-/delallfilters:Asincommandthisisusedtoremoveallfiltersofgroup.

<i>Asofnow,thereis6actionsthatyoucando:</i>
-<code>Sendanote</code>
-<code>Warntheuser</code>
-<code>Bantheuser</code>
-<code>Mutetheuser</code>
-<code>tBantheuser</code>
-<code>tMutetheuser</code>

<i>Afiltercansupportmultipleactions!</i>

Ahifyoudon'tunderstandwhatthisactionsarefor?Actionssaysbotwhattodowhenthegiven<code>word/sentence</code>istriggered.
Youcanalsouseregexandbuttonsforfilters.Check/buttonshelptoknowmore.

<i>Availableforallusers:</i>
-/filtersor/listfilters

Youwanttoknowallfilterofyourchat/chatyoujoined?Usethiscommand.Itwilllistallfiltersalongwithspecifiedactions!

<b>TETFILTERS</b>
Textfiltersareforshortandtextreplies
<i>Commandsavailable</i>
-/filter[KEYWORD][REPLYTOMESSAGE]:Filterstherepliedmessagewithgivenkeyword.
-/stop[KEYWORD]:Stopsthegivenfilter.


<i>Differencebetweentextfilterandfilter</i>
*Ifyoufilteredword"hi"with/addfilteritfiltersallwordsincludinghi.
Futureexplained:
-Whenafilteraddedtohias"hello"whenusersentamessagelike"Itwasahit"botrepliesas"Hello"aswordcontainhi
**Youcanuseregextoremovethisifyoulike
<i>Textfilterswon'treplylikethat.Itonlyrepliesifword="hi"(Accordingtoexampletaken)</i>
Textfilterscanfilter
-<code>Asingleword</code>
-<code>Asentence</code>
-<code>Asticker</code>

<b>CLASSICFILTERS</b>
Classicfiltersarejustlikemarie'sfiltersystem.Ifyoustilllikethatkindoffiltersystem.Use/cfilterhelptoknowmore

⚠️READFROMTOP
"""
