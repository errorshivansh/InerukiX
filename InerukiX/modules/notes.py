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

importdifflib
importre
fromcontextlibimportsuppress
fromdatetimeimportdatetime

fromaiogram.dispatcher.filters.builtinimportCommandStart
fromaiogram.types.inline_keyboardimportInlineKeyboardButton,InlineKeyboardMarkup
fromaiogram.utils.deep_linkingimportget_start_link
fromaiogram.utils.exceptionsimport(
BadRequest,
MessageCantBeDeleted,
MessageNotModified,
)
frombabel.datesimportformat_datetime
frompymongoimportReplaceOne
fromtelethon.errors.rpcerrorlistimportMessageDeleteForbiddenError

fromInerukiimportbot
fromIneruki.decoratorimportregister
fromIneruki.services.mongoimportdb
fromIneruki.services.redisimportredis
fromIneruki.services.telethonimporttbot

from.utils.connectionsimportchat_connection,set_connected_command
from.utils.disableimportdisableable_dec
from.utils.languageimportget_string,get_strings_dec
from.utils.messageimportget_arg,need_args_dec
from.utils.notesimport(
ALLOWED_COLUMNS,
BUTTONS,
get_parsed_note_list,
send_note,
t_unparse_note_item,
)
from.utils.user_detailsimportget_user_link

RESTRICTED_SYMBOLS_IN_NOTENAMES=[
":",
"**",
"__",
"`",
"#",
'"',
"[",
"]",
"'",
"$",
"||",
]


asyncdefget_similar_note(chat_id,note_name):
all_notes=[]
asyncfornoteindb.notes.find({"chat_id":chat_id}):
all_notes.extend(note["names"])

iflen(all_notes)>0:
check=difflib.get_close_matches(note_name,all_notes)
iflen(check)>0:
returncheck[0]

returnNone


defclean_notes(func):
asyncdefwrapped_1(*args,**kwargs):
event=args[0]

message=awaitfunc(*args,**kwargs)
ifnotmessage:
return

ifevent.chat.type=="private":
return

chat_id=event.chat.id

data=awaitdb.clean_notes.find_one({"chat_id":chat_id})
ifnotdata:
return

ifdata["enabled"]isnotTrue:
return

if"msgs"indata:
withsuppress(MessageDeleteForbiddenError):
awaittbot.delete_messages(chat_id,data["msgs"])

msgs=[]
ifhasattr(message,"message_id"):
msgs.append(message.message_id)
else:
msgs.append(message.id)

msgs.append(event.message_id)

awaitdb.clean_notes.update_one({"chat_id":chat_id},{"$set":{"msgs":msgs}})

returnwrapped_1


@register(cmds="save",user_admin=True,user_can_change_info=True)
@need_args_dec()
@chat_connection(admin=True)
@get_strings_dec("notes")
asyncdefsave_note(message,chat,strings):
chat_id=chat["chat_id"]
arg=get_arg(message).lower()
ifarg[0]=="#":
arg=arg[1:]

sym=None
ifany((sym:=s)inargforsinRESTRICTED_SYMBOLS_IN_NOTENAMES):
awaitmessage.reply(strings["notename_cant_contain"].format(symbol=sym))
return

note_names=arg.split("|")

note=awaitget_parsed_note_list(message)

note["names"]=note_names
note["chat_id"]=chat_id

if"text"notinnoteand"file"notinnote:
awaitmessage.reply(strings["blank_note"])
return

ifold_note:=awaitdb.notes.find_one(
{"chat_id":chat_id,"names":{"$in":note_names}}
):
text=strings["note_updated"]
if"created_date"inold_note:
note["created_date"]=old_note["created_date"]
note["created_user"]=old_note["created_user"]
note["edited_date"]=datetime.now()
note["edited_user"]=message.from_user.id
else:
text=strings["note_saved"]
note["created_date"]=datetime.now()
note["created_user"]=message.from_user.id

awaitdb.notes.replace_one(
{"_id":old_note["_id"]}ifold_noteelsenote,note,upsert=True
)

text+=strings["you_can_get_note"]
text=text.format(note_name=note_names[0],chat_title=chat["chat_title"])
iflen(note_names)>1:
text+=strings["note_aliases"]
fornotenameinnote_names:
text+=f"<code>#{notename}</code>"

awaitmessage.reply(text)


@get_strings_dec("notes")
asyncdefget_note(
message,
strings,
note_name=None,
db_item=None,
chat_id=None,
send_id=None,
rpl_id=None,
noformat=False,
event=None,
user=None,
):
ifnotchat_id:
chat_id=message.chat.id

ifnotsend_id:
send_id=message.chat.id

ifrpl_idisFalse:
rpl_id=None
elifnotrpl_id:
rpl_id=message.message_id

ifnotdb_itemandnot(
db_item:=awaitdb.notes.find_one(
{"chat_id":chat_id,"names":{"$in":[note_name]}}
)
):
awaitbot.send_message(chat_id,strings["no_note"],reply_to_message_id=rpl_id)
return

text,kwargs=awaitt_unparse_note_item(
message,db_item,chat_id,noformat=noformat,event=event,user=user
)
kwargs["reply_to"]=rpl_id

returnawaitsend_note(send_id,text,**kwargs)


@register(cmds="get")
@disableable_dec("get")
@need_args_dec()
@chat_connection(command="get")
@get_strings_dec("notes")
@clean_notes
asyncdefget_note_cmd(message,chat,strings):
chat_id=chat["chat_id"]
chat_name=chat["chat_title"]

note_name=get_arg(message).lower()
ifnote_name[0]=="#":
note_name=note_name[1:]

if"reply_to_message"inmessage:
rpl_id=message.reply_to_message.message_id
user=message.reply_to_message.from_user
else:
rpl_id=message.message_id
user=message.from_user

ifnot(
note:=awaitdb.notes.find_one(
{"chat_id":int(chat_id),"names":{"$in":[note_name]}}
)
):
text=strings["cant_find_note"].format(chat_name=chat_name)
ifalleged_note_name:=awaitget_similar_note(chat_id,note_name):
text+=strings["u_mean"].format(note_name=alleged_note_name)
awaitmessage.reply(text)
return

noformat=False
iflen(args:=message.text.split(""))>2:
arg2=args[2].lower()
noformat=arg2in("noformat","raw")

returnawaitget_note(
message,db_item=note,rpl_id=rpl_id,noformat=noformat,user=user
)


@register(regexp=r"^#([\w-]+)",allow_kwargs=True)
@disableable_dec("get")
@chat_connection(command="get")
@clean_notes
asyncdefget_note_hashtag(message,chat,regexp=None,**kwargs):
chat_id=chat["chat_id"]

note_name=regexp.group(1).lower()
ifnot(
note:=awaitdb.notes.find_one(
{"chat_id":int(chat_id),"names":{"$in":[note_name]}}
)
):
return

if"reply_to_message"inmessage:
rpl_id=message.reply_to_message.message_id
user=message.reply_to_message.from_user
else:
rpl_id=message.message_id
user=message.from_user

returnawaitget_note(message,db_item=note,rpl_id=rpl_id,user=user)


@register(cmds=["notes","saved"])
@disableable_dec("notes")
@chat_connection(command="notes")
@get_strings_dec("notes")
@clean_notes
asyncdefget_notes_list_cmd(message,chat,strings):
if(
awaitdb.privatenotes.find_one({"chat_id":chat["chat_id"]})
andmessage.chat.id==chat["chat_id"]
):#WorkaroundtoavoidsendingPNtoconnectedPM
text=strings["notes_in_private"]
ifnot(keyword:=message.get_args()):
keyword=None
button=InlineKeyboardMarkup().add(
InlineKeyboardButton(
text="Clickhere",
url=awaitget_start_link(f"notes_{chat['chat_id']}_{keyword}"),
)
)
returnawaitmessage.reply(
text,reply_markup=button,disable_web_page_preview=True
)
else:
returnawaitget_notes_list(message,chat=chat)


@get_strings_dec("notes")
asyncdefget_notes_list(message,strings,chat,keyword=None,pm=False):
text=strings["notelist_header"].format(chat_name=chat["chat_title"])

notes=(
awaitdb.notes.find({"chat_id":chat["chat_id"]})
.sort("names",1)
.to_list(length=300)
)
ifnotnotes:
returnawaitmessage.reply(
strings["notelist_no_notes"].format(chat_title=chat["chat_title"])
)

asyncdefsearch_notes(request):
nonlocalnotes,text,note,note_name
text+="\n"+strings["notelist_search"].format(request=request)
all_notes=notes
notes=[]
fornoteinall_notes:
fornote_nameinnote["names"]:
ifre.search(request,note_name):
notes.append(note)
iflen(notes)<=0:
returnawaitmessage.reply(strings["no_notes_pattern"]%request)

#Search
ifkeyword:
awaitsearch_notes(keyword)
iflen(keyword:=message.get_args())>0andpmisFalse:
awaitsearch_notes(keyword)

iflen(notes)>0:
fornoteinnotes:
text+="\n-"
fornote_nameinnote["names"]:
text+=f"<code>#{note_name}</code>"
text+=strings["you_can_get_note"]

try:
returnawaitmessage.reply(text)
exceptBadRequest:
awaitmessage.answer(text)


@register(cmds="search")
@chat_connection()
@get_strings_dec("notes")
@clean_notes
asyncdefsearch_in_note(message,chat,strings):
request=message.get_args()
text=strings["search_header"].format(
chat_name=chat["chat_title"],request=request
)

notes=db.notes.find(
{"chat_id":chat["chat_id"],"text":{"$regex":request,"$options":"i"}}
).sort("names",1)
fornotein(check:=awaitnotes.to_list(length=300)):
text+="\n-"
fornote_nameinnote["names"]:
text+=f"<code>#{note_name}</code>"
text+=strings["you_can_get_note"]
ifnotcheck:
returnawaitmessage.reply(
strings["notelist_no_notes"].format(chat_title=chat["chat_title"])
)
returnawaitmessage.reply(text)


@register(cmds=["clear","delnote"],user_admin=True,user_can_change_info=True)
@chat_connection(admin=True)
@need_args_dec()
@get_strings_dec("notes")
asyncdefclear_note(message,chat,strings):
note_names=get_arg(message).lower().split("|")

removed=""
not_removed=""
fornote_nameinnote_names:
ifnote_name[0]=="#":
note_name=note_name[1:]

ifnot(
note:=awaitdb.notes.find_one(
{"chat_id":chat["chat_id"],"names":{"$in":[note_name]}}
)
):
iflen(note_names)<=1:
text=strings["cant_find_note"].format(chat_name=chat["chat_title"])
ifalleged_note_name:=awaitget_similar_note(
chat["chat_id"],note_name
):
text+=strings["u_mean"].format(note_name=alleged_note_name)
awaitmessage.reply(text)
return
else:
not_removed+="#"+note_name
continue

awaitdb.notes.delete_one({"_id":note["_id"]})
removed+="#"+note_name

iflen(note_names)>1:
text=strings["note_removed_multiple"].format(
chat_name=chat["chat_title"],removed=removed
)
ifnot_removed:
text+=strings["not_removed_multiple"].format(not_removed=not_removed)
awaitmessage.reply(text)
else:
awaitmessage.reply(
strings["note_removed"].format(
note_name=note_name,chat_name=chat["chat_title"]
)
)


@register(cmds="clearall",user_admin=True,user_can_change_info=True)
@chat_connection(admin=True)
@get_strings_dec("notes")
asyncdefclear_all_notes(message,chat,strings):
#Ensurenotescount
ifnotawaitdb.notes.find_one({"chat_id":chat["chat_id"]}):
awaitmessage.reply(
strings["notelist_no_notes"].format(chat_title=chat["chat_title"])
)
return

text=strings["clear_all_text"].format(chat_name=chat["chat_title"])
buttons=InlineKeyboardMarkup()
buttons.add(
InlineKeyboardButton(
strings["clearall_btn_yes"],callback_data="clean_all_notes_cb"
)
)
buttons.add(
InlineKeyboardButton(strings["clearall_btn_no"],callback_data="cancel")
)
awaitmessage.reply(text,reply_markup=buttons)


@register(regexp="clean_all_notes_cb",f="cb",is_admin=True,user_can_change_info=True)
@chat_connection(admin=True)
@get_strings_dec("notes")
asyncdefclear_all_notes_cb(event,chat,strings):
num=(awaitdb.notes.delete_many({"chat_id":chat["chat_id"]})).deleted_count

text=strings["clearall_done"].format(num=num,chat_name=chat["chat_title"])
awaitevent.message.edit_text(text)


@register(cmds="noteinfo",user_admin=True)
@chat_connection()
@need_args_dec()
@get_strings_dec("notes")
@clean_notes
asyncdefnote_info(message,chat,strings):
note_name=get_arg(message).lower()
ifnote_name[0]=="#":
note_name=note_name[1:]

ifnot(
note:=awaitdb.notes.find_one(
{"chat_id":chat["chat_id"],"names":{"$in":[note_name]}}
)
):
text=strings["cant_find_note"].format(chat_name=chat["chat_title"])
ifalleged_note_name:=awaitget_similar_note(chat["chat_id"],note_name):
text+=strings["u_mean"].format(note_name=alleged_note_name)
returnawaitmessage.reply(text)

text=strings["note_info_title"]

note_names=""
fornote_nameinnote["names"]:
note_names+=f"<code>#{note_name}</code>"

text+=strings["note_info_note"]%note_names
text+=strings["note_info_content"]%(
"text"if"file"notinnoteelsenote["file"]["type"]
)

if"parse_mode"notinnoteornote["parse_mode"]=="md":
parse_mode="Markdown"
elifnote["parse_mode"]=="html":
parse_mode="HTML"
elifnote["parse_mode"]=="none":
parse_mode="None"
else:
raiseTypeError()

text+=strings["note_info_parsing"]%parse_mode

if"created_date"innote:
text+=strings["note_info_created"].format(
date=format_datetime(
note["created_date"],locale=strings["language_info"]["babel"]
),
user=awaitget_user_link(note["created_user"]),
)

if"edited_date"innote:
text+=strings["note_info_updated"].format(
date=format_datetime(
note["edited_date"],locale=strings["language_info"]["babel"]
),
user=awaitget_user_link(note["edited_user"]),
)

returnawaitmessage.reply(text)


BUTTONS.update({"note":"btnnotesm","#":"btnnotesm"})


@register(regexp=r"btnnotesm_(\w+)_(.*)",f="cb",allow_kwargs=True)
@get_strings_dec("notes")
asyncdefnote_btn(event,strings,regexp=None,**kwargs):
chat_id=int(regexp.group(2))
user_id=event.from_user.id
note_name=regexp.group(1).lower()

ifnot(
note:=awaitdb.notes.find_one(
{"chat_id":chat_id,"names":{"$in":[note_name]}}
)
):
awaitevent.answer(strings["no_note"])
return

withsuppress(MessageCantBeDeleted):
awaitevent.message.delete()
awaitget_note(
event.message,
db_item=note,
chat_id=chat_id,
send_id=user_id,
rpl_id=None,
event=event,
)


@register(CommandStart(re.compile(r"btnnotesm")),allow_kwargs=True)
@get_strings_dec("notes")
asyncdefnote_start(message,strings,regexp=None,**kwargs):
#Don'tevenaskwhatitmeans,mostlyitworkaroundtosupportnotenameswith_
args=re.search(r"^([a-zA-Z0-9]+)_(.*?)(-\d+)$",message.get_args())
chat_id=int(args.group(3))
user_id=message.from_user.id
note_name=args.group(2).strip("_")

ifnot(
note:=awaitdb.notes.find_one(
{"chat_id":chat_id,"names":{"$in":[note_name]}}
)
):
awaitmessage.reply(strings["no_note"])
return

awaitget_note(message,db_item=note,chat_id=chat_id,send_id=user_id,rpl_id=None)


@register(cmds="start",only_pm=True)
@get_strings_dec("connections")
asyncdefbtn_note_start_state(message,strings):
key="btn_note_start_state:"+str(message.from_user.id)
ifnot(cached:=redis.hgetall(key)):
return

chat_id=int(cached["chat_id"])
user_id=message.from_user.id
note_name=cached["notename"]

note=awaitdb.notes.find_one({"chat_id":chat_id,"names":{"$in":[note_name]}})
awaitget_note(message,db_item=note,chat_id=chat_id,send_id=user_id,rpl_id=None)

redis.delete(key)


@register(cmds="privatenotes",is_admin=True,user_can_change_info=True)
@chat_connection(admin=True)
@get_strings_dec("notes")
asyncdefprivate_notes_cmd(message,chat,strings):
chat_id=chat["chat_id"]
chat_name=chat["chat_title"]
text=str

try:
(text:="".join(message.text.split()[1]).lower())
exceptIndexError:
pass

enabling=["true","enable","on"]
disabling=["false","disable","off"]
ifdatabase:=awaitdb.privatenotes.find_one({"chat_id":chat_id}):
iftextinenabling:
awaitmessage.reply(strings["already_enabled"]%chat_name)
return
iftextinenabling:
awaitdb.privatenotes.insert_one({"chat_id":chat_id})
awaitmessage.reply(strings["enabled_successfully"]%chat_name)
eliftextindisabling:
ifnotdatabase:
awaitmessage.reply(strings["not_enabled"])
return
awaitdb.privatenotes.delete_one({"_id":database["_id"]})
awaitmessage.reply(strings["disabled_successfully"]%chat_name)
else:
#Assumeadminaskedforcurrentstate
ifdatabase:
state=strings["enabled"]
else:
state=strings["disabled"]
awaitmessage.reply(
strings["current_state_info"].format(state=state,chat=chat_name)
)


@register(cmds="cleannotes",is_admin=True,user_can_change_info=True)
@chat_connection(admin=True)
@get_strings_dec("notes")
asyncdefclean_notes(message,chat,strings):
disable=["no","off","0","false","disable"]
enable=["yes","on","1","true","enable"]

chat_id=chat["chat_id"]

arg=get_arg(message)
ifargandarg.lower()inenable:
awaitdb.clean_notes.update_one(
{"chat_id":chat_id},{"$set":{"enabled":True}},upsert=True
)
text=strings["clean_notes_enable"].format(chat_name=chat["chat_title"])
elifargandarg.lower()indisable:
awaitdb.clean_notes.update_one(
{"chat_id":chat_id},{"$set":{"enabled":False}},upsert=True
)
text=strings["clean_notes_disable"].format(chat_name=chat["chat_title"])
else:
data=awaitdb.clean_notes.find_one({"chat_id":chat_id})
ifdataanddata["enabled"]isTrue:
text=strings["clean_notes_enabled"].format(chat_name=chat["chat_title"])
else:
text=strings["clean_notes_disabled"].format(chat_name=chat["chat_title"])

awaitmessage.reply(text)


@register(CommandStart(re.compile("notes")))
@get_strings_dec("notes")
asyncdefprivate_notes_func(message,strings):
args=message.get_args().split("_")
chat_id=args[1]
keyword=args[2]ifargs[2]!="None"elseNone
awaitset_connected_command(message.from_user.id,int(chat_id),["get","notes"])
chat=awaitdb.chat_list.find_one({"chat_id":int(chat_id)})
awaitmessage.answer(strings["privatenotes_notif"].format(chat=chat["chat_title"]))
awaitget_notes_list(message,chat=chat,keyword=keyword,pm=True)


asyncdef__stats__():
text="*<code>{}</code>totalnotes\n".format(awaitdb.notes.count_documents({}))
returntext


asyncdef__export__(chat_id):
data=[]
notes=(
awaitdb.notes.find({"chat_id":chat_id}).sort("names",1).to_list(length=300)
)
fornoteinnotes:
delnote["_id"]
delnote["chat_id"]
note["created_date"]=str(note["created_date"])
if"edited_date"innote:
note["edited_date"]=str(note["edited_date"])
data.append(note)

return{"notes":data}


ALLOWED_COLUMNS_NOTES=ALLOWED_COLUMNS+[
"names",
"created_date",
"created_user",
"edited_date",
"edited_user",
]


asyncdef__import__(chat_id,data):
ifnotdata:
return

new=[]
fornoteindata:

#Filever1to2
if"name"innote:
note["names"]=[note["name"]]
delnote["name"]

foritemin[iforiinnoteifinotinALLOWED_COLUMNS_NOTES]:
delnote[item]

note["chat_id"]=chat_id
note["created_date"]=datetime.fromisoformat(note["created_date"])
if"edited_date"innote:
note["edited_date"]=datetime.fromisoformat(note["edited_date"])
new.append(
ReplaceOne(
{"chat_id":note["chat_id"],"names":{"$in":[note["names"][0]]}},
note,
upsert=True,
)
)

awaitdb.notes.bulk_write(new)


asyncdeffilter_handle(message,chat,data):
chat_id=chat["chat_id"]
read_chat_id=message.chat.id
note_name=data["note_name"]
note=awaitdb.notes.find_one({"chat_id":chat_id,"names":{"$in":[note_name]}})
awaitget_note(
message,db_item=note,chat_id=chat_id,send_id=read_chat_id,rpl_id=None
)


asyncdefsetup_start(message):
text=awaitget_string(message.chat.id,"notes","filters_setup_start")
withsuppress(MessageNotModified):
awaitmessage.edit_text(text)


asyncdefsetup_finish(message,data):
note_name=message.text.split("",1)[0].split()[0]

ifnot(awaitdb.notes.find_one({"chat_id":data["chat_id"],"names":note_name})):
awaitmessage.reply("nosuchnote!")
return

return{"note_name":note_name}


__filters__={
"get_note":{
"title":{"module":"notes","string":"filters_title"},
"handle":filter_handle,
"setup":{"start":setup_start,"finish":setup_finish},
"del_btn_name":lambdamsg,data:f"Getnote:{data['note_name']}",
}
}


__mod_name__="Notes"

__help__="""
Sometimesyouneedtosavesomedata,liketextorpictures.Withnotes,youcansaveanytypesofTelegram'sdatainyourchats.
AlsonotesperfectlyworkinginPMwithIneruki.

<b>Availablecommands:</b>
-/save(name)(data):Savesthenote.
-#(name)or/get(name):Getthenoteregisteredtothatword.
-/clear(name):deletesthenote.
-/notesor/saved:Listsallnotes.
-/noteinfo(name):Showsdetailedinfoaboutthenote.
-/search(searchpattern):Searchtextinnotes
-/clearall:Clearsallnotes

<b>Onlyingroups:</b>
-/privatenotes(on/off):RedirectuserinPMtoseenotes
-/cleannotes(on/off):Willcleanoldnotesmessages

<b>Examples:</b>
Anexampleofhowtosaveanotewouldbevia:
<code>/savedataThisisexamplenote!</code>
Now,anyoneusing<code>/getdata</code>,or<code>#data</code>willberepliedtowithThisisexamplenote!.

<b>Savingpicturesandothernon-textdata:</b>
Ifyouwanttosaveanimage,gif,orsticker,oranyotherdata,dothefollowing:
<code>/saveword</code>whilereplyingtoastickerorwhateverdatayou'dlike.Now,thenoteat<code>#word</code>containsastickerwhichwillbesentasareply.

<b>Removingmanynotesperonerequest:</b>
Toremovemanynotesyoucanusethe/clearcommand,justplaceallnotenameswhichyouwanttoremoveasargumentofthecommand,use|asseprator,forexample:
<code>/clearnote1|note2|note3</code>

<b>Notesaliases:</b>
Youcansavenotewithmanynames,example:
<code>/savename1|name2|name3</code>
Thatwillsaveanotewith3differentnames,byanyyoucan/getnote,thatcanbeusefulifusersinyourchattryingtogetnoteswhichexitsbyothernames.

<b>Notesbuttonsandvariables:</b>
Notessupportinlinebuttons,send/buttonshelptogetstartedwithusingit.
Variablesarespecialwordswhichwillbereplacedbyactualinfolikeifyouadd<code>{id}</code>inyournoteitwillbereplacedbyuserIDwhichaskednote.Send/variableshelptogetstartedwithusingit.

<b>Notesformattingandsettings:</b>
Everynotecancontainspecialsettings,forexampleyoucanchangeformattingmethodtoHTMLby<code>%PARSEMODE_HTML</code>andfullydisableitby<code>%PARSEMODE_NONE</code>(BydefaultformattingisMarkdownorthesameformattingTelegramsupports)

<code>%PARSEMODE_(HTML,NONE)</code>:Changethenoteformatting
<code>%PREVIEW</code>:Enablesthelinkspreviewinsavednote

<b>SavingnotesfromotherMariestylebots:</b>
Inerukicansavenotesfromotherbots,justreply/saveonthesavedmessagefromanotherbot,savingpicturesandbuttonssupportedaswell.

<b>Retrievingnoteswithouttheformatting:</b>
Toretrieveanotewithouttheformatting,use<code>/get(name)raw</code>or<code>/get(name)noformat</code>
Thiswillretrievethenoteandsenditwithoutformattingit;gettingyoutherawnote,allowingyoutomakeeasyedits.
"""
