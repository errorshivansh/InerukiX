#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2019Aiogram
#
#ThisfileispartofAllMightBot.
#
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

importhtml
importre
importsys
fromdatetimeimportdatetime

fromaiogram.typesimportMessage
fromaiogram.types.inline_keyboardimportInlineKeyboardButton,InlineKeyboardMarkup
fromaiogram.utilsimportmarkdown
frombabel.datesimportformat_date,format_datetime,format_time
fromtelethon.errorsimport(
BadRequestError,
ButtonUrlInvalidError,
MediaEmptyError,
MessageEmptyError,
RPCError,
)
fromtelethon.errors.rpcerrorlistimportChatWriteForbiddenError
fromtelethon.tl.customimportButton

importIneruki.modules.utils.tmarkdownastmarkdown
fromInerukiimportBOT_USERNAME
fromIneruki.services.telethonimporttbot

from...utils.loggerimportlog
from.languageimportget_chat_lang
from.messageimportget_args
from.tmarkdownimporttbold,tcode,titalic,tlink,tpre,tstrikethrough,tunderline
from.user_detailsimportget_user_link

BUTTONS={}

ALLOWED_COLUMNS=["parse_mode","file","text","preview"]


deftparse_ent(ent,text,as_html=True):
ifnottext:
returntext

etype=ent.type
offset=ent.offset
length=ent.length

ifsys.maxunicode==0xFFFF:
returntext[offset:offset+length]

ifnotisinstance(text,bytes):
entity_text=text.encode("utf-16-le")
else:
entity_text=text

entity_text=entity_text[offset*2:(offset+length)*2].decode("utf-16-le")

ifetype=="bold":
method=markdown.hboldifas_htmlelsetbold
returnmethod(entity_text)
ifetype=="italic":
method=markdown.hitalicifas_htmlelsetitalic
returnmethod(entity_text)
ifetype=="pre":
method=markdown.hpreifas_htmlelsetpre
returnmethod(entity_text)
ifetype=="code":
method=markdown.hcodeifas_htmlelsetcode
returnmethod(entity_text)
ifetype=="strikethrough":
method=markdown.hstrikethroughifas_htmlelsetstrikethrough
returnmethod(entity_text)
ifetype=="underline":
method=markdown.hunderlineifas_htmlelsetunderline
returnmethod(entity_text)
ifetype=="url":
returnentity_text
ifetype=="text_link":
method=markdown.hlinkifas_htmlelsetlink
returnmethod(entity_text,ent.url)
ifetype=="text_mention"andent.user:
returnent.user.get_mention(entity_text,as_html=as_html)

returnentity_text


defget_parsed_msg(message):
ifnotmessage.textandnotmessage.caption:
return"","md"

text=message.captionormessage.text

mode=get_msg_parse(text)
ifmode=="html":
as_html=True
else:
as_html=False

entities=message.caption_entitiesormessage.entities

ifnotentities:
returntext,mode

ifnotsys.maxunicode==0xFFFF:
text=text.encode("utf-16-le")

result=""
offset=0

forentityinsorted(entities,key=lambdaitem:item.offset):
entity_text=tparse_ent(entity,text,as_html=as_html)

ifsys.maxunicode==0xFFFF:
part=text[offset:entity.offset]
result+=part+entity_text
else:
part=text[offset*2:entity.offset*2].decode("utf-16-le")
result+=part+entity_text

offset=entity.offset+entity.length

ifsys.maxunicode==0xFFFF:
result+=text[offset:]
else:
result+=text[offset*2:].decode("utf-16-le")

result=re.sub(r"\[format:(\w+)\]","",result)
result=re.sub(r"%PARSEMODE_(\w+)","",result)

ifnotresult:
result=""

returnresult,mode


defget_msg_parse(text,default_md=True):
if"[format:html]"intextor"%PARSEMODE_HTML"intext:
return"html"
elif"[format:none]"intextor"%PARSEMODE_NONE"intext:
return"none"
elif"[format:md]"intextor"%PARSEMODE_MD"intext:
return"md"
else:
ifnotdefault_md:
returnNone
return"md"


defparse_button(data,name):
raw_button=data.split("_")
raw_btn_type=raw_button[0]

pattern=re.match(r"btn(.+)(sm|cb|start)",raw_btn_type)
ifnotpattern:
return""

action=pattern.group(1)
args=raw_button[1]

ifactioninBUTTONS:
text=f"\n[{name}](btn{action}:{args}*!repl!*)"
else:
ifargs:
text=f"\n[{name}].(btn{action}:{args})"
else:
text=f"\n[{name}].(btn{action})"

returntext


defget_reply_msg_btns_text(message):
text=""
forcolumninmessage.reply_markup.inline_keyboard:
btn_num=0
forbtnincolumn:
btn_num+=1
name=btn["text"]

if"url"inbtn:
url=btn["url"]
if"?start="inurl:
raw_btn=url.split("?start=")[1]
text+=parse_button(raw_btn,name)
else:
text+=f"\n[{btn['text']}](btnurl:{btn['url']}*!repl!*)"
elif"callback_data"inbtn:
text+=parse_button(btn["callback_data"],name)

ifbtn_num>1:
text=text.replace("*!repl!*",":same")
else:
text=text.replace("*!repl!*","")
returntext


asyncdefget_msg_file(message):
message_id=message.message_id

tmsg=awaittbot.get_messages(message.chat.id,ids=message_id)

file_types=[
"sticker",
"photo",
"document",
"video",
"audio",
"video_note",
"voice",
]
forfile_typeinfile_types:
iffile_typenotinmessage:
continue
return{"id":tmsg.file.id,"type":file_type}
returnNone


asyncdefget_parsed_note_list(message,allow_reply_message=True,split_args=1):
note={}
if"reply_to_message"inmessageandallow_reply_message:
#Getparsedreplymsgtext
text,note["parse_mode"]=get_parsed_msg(message.reply_to_message)
#Getparsedoriginmsgtext
text+=""
to_split="".join([""+qforqinget_args(message)[:split_args]])
ifnotto_split:
to_split=""
text+=get_parsed_msg(message)[0].partition(message.get_command()+to_split)[
2
][1:]
#Setparse_modeiforiginmsgoverrideit
ifmode:=get_msg_parse(message.text,default_md=False):
note["parse_mode"]=mode

#Getmessagekeyboard
if(
"reply_markup"inmessage.reply_to_message
and"inline_keyboard"inmessage.reply_to_message.reply_markup
):
text+=get_reply_msg_btns_text(message.reply_to_message)

#Checkonattachment
ifmsg_file:=awaitget_msg_file(message.reply_to_message):
note["file"]=msg_file
else:
text,note["parse_mode"]=get_parsed_msg(message)
ifmessage.get_command()andmessage.get_args():
#Removecmdandargfrommessage'stext
text=re.sub(message.get_command()+r"\s?","",text,1)
ifsplit_args>0:
text=re.sub(re.escape(get_args(message)[0])+r"\s?","",text,1)
#Checkonattachment
ifmsg_file:=awaitget_msg_file(message):
note["file"]=msg_file

iftext.replace("",""):
note["text"]=text

#Preview
if"text"innoteandre.search(r"[$|%]PREVIEW",note["text"]):
note["text"]=re.sub(r"[$|%]PREVIEW","",note["text"])
note["preview"]=True

returnnote


asyncdeft_unparse_note_item(
message,db_item,chat_id,noformat=None,event=None,user=None
):
text=db_item["text"]if"text"indb_itemelse""

file_id=None
preview=None

ifnotuser:
user=message.from_user

if"file"indb_item:
file_id=db_item["file"]["id"]

ifnoformat:
markup=None
if"parse_mode"notindb_itemordb_item["parse_mode"]=="none":
text+="\n%PARSEMODE_NONE"
elifdb_item["parse_mode"]=="html":
text+="\n%PARSEMODE_HTML"

if"preview"indb_itemanddb_item["preview"]:
text+="\n%PREVIEW"

db_item["parse_mode"]=None

else:
pm=Trueifmessage.chat.type=="private"elseFalse
text,markup=button_parser(chat_id,text,pm=pm)

ifnottextandnotfile_id:
text=("#"+db_item["names"][0])if"names"indb_itemelse"404"

if"parse_mode"notindb_itemordb_item["parse_mode"]=="none":
db_item["parse_mode"]=None
elifdb_item["parse_mode"]=="md":
text=awaitvars_parser(
text,message,chat_id,md=True,event=event,user=user
)
elifdb_item["parse_mode"]=="html":
text=awaitvars_parser(
text,message,chat_id,md=False,event=event,user=user
)

if"preview"indb_itemanddb_item["preview"]:
preview=True

returntext,{
"buttons":markup,
"parse_mode":db_item["parse_mode"],
"file":file_id,
"link_preview":preview,
}


asyncdefsend_note(send_id,text,**kwargs):
iftext:
text=text[:4090]

if"parse_mode"inkwargsandkwargs["parse_mode"]=="md":
kwargs["parse_mode"]=tmarkdown

try:
returnawaittbot.send_message(send_id,text,**kwargs)

except(ButtonUrlInvalidError,MessageEmptyError,MediaEmptyError):
returnawaittbot.send_message(
send_id,"Ifoundthisnoteinvalid!Pleaseupdateit(readhelp)."
)
exceptRPCError:
log.error("SendNoteErrorbotisKicked/Mutedinchat[IGNORE]")
return
exceptChatWriteForbiddenError:
log.error("SendNoteErrorbotisKicked/Mutedinchat[IGNORE]")
return
exceptBadRequestError:#ifreplymessagedeleted
delkwargs["reply_to"]
returnawaittbot.send_message(send_id,text,**kwargs)
exceptExceptionaserr:
log.error("Somethinghappenedonsendingnote",exc_info=err)


defbutton_parser(chat_id,texts,pm=False,aio=False,row_width=None):
buttons=InlineKeyboardMarkup(row_width=row_width)ifaioelse[]
pattern=r"\[(.+?)\]\((button|btn|#)(.+?)(:.+?|)(:same|)\)(\n|)"
raw_buttons=re.findall(pattern,texts)
text=re.sub(pattern,"",texts)
btn=None
forraw_buttoninraw_buttons:
name=raw_button[0]
action=(
raw_button[1]ifraw_button[1]notin("button","btn")elseraw_button[2]
)

ifraw_button[3]:
argument=raw_button[3][1:].lower().replace("`","")
elifactionin("#"):
argument=raw_button[2]
print(raw_button[2])
else:
argument=""

ifactioninBUTTONS.keys():
cb=BUTTONS[action]
string=f"{cb}_{argument}_{chat_id}"ifargumentelsef"{cb}_{chat_id}"
ifaio:
start_btn=InlineKeyboardButton(
name,url=f"https://t.me/{BOT_USERNAME}?start="+string
)
cb_btn=InlineKeyboardButton(name,callback_data=string)
else:
start_btn=Button.url(
name,f"https://t.me/{BOT_USERNAME}?start="+string
)
cb_btn=Button.inline(name,string)

ifcb.endswith("sm"):
btn=cb_btnifpmelsestart_btn
elifcb.endswith("cb"):
btn=cb_btn
elifcb.endswith("start"):
btn=start_btn
elifcb.startswith("url"):
#WorkaroundtomakeURLscase-sensitiveTODO:makebetter
argument=raw_button[3][1:].replace("`","")ifraw_button[3]else""
btn=Button.url(name,argument)
elifcb.endswith("rules"):
btn=start_btn
elifaction=="url":
argument=raw_button[3][1:].replace("`","")ifraw_button[3]else""
ifargument[0]=="/"andargument[1]=="/":
argument=argument[2:]
btn=(
InlineKeyboardButton(name,url=argument)
ifaio
elseButton.url(name,argument)
)
else:
#Ifbtnnotregistred
btn=None
ifargument:
text+=f"\n[{name}].(btn{action}:{argument})"
else:
text+=f"\n[{name}].(btn{action})"
continue

ifbtn:
ifaio:
buttons.insert(btn)ifraw_button[4]elsebuttons.add(btn)
else:
iflen(buttons)<1andraw_button[4]:
buttons.add(btn)ifaioelsebuttons.append([btn])
else:
buttons[-1].append(btn)ifraw_button[4]elsebuttons.append([btn])

ifnotaioandlen(buttons)==0:
buttons=None

ifnottextortext.isspace():#TODO:Sometimeswecanreturntext==''
text=None

returntext,buttons


asyncdefvars_parser(
text,message,chat_id,md=False,event:Message=None,user=None
):
ifeventisNone:
event=message

ifnottext:
returntext

language_code=awaitget_chat_lang(chat_id)
current_datetime=datetime.now()

first_name=html.escape(user.first_name,quote=False)
last_name=html.escape(user.last_nameor"",quote=False)
user_id=(
[user.idforuserinevent.new_chat_members][0]
if"new_chat_members"ineventandevent.new_chat_members!=[]
elseuser.id
)
mention=awaitget_user_link(user_id,md=md)

if(
hasattr(event,"new_chat_members")
andevent.new_chat_members
andevent.new_chat_members[0].username
):
username="@"+event.new_chat_members[0].username
elifuser.username:
username="@"+user.username
else:
username=mention

chat_id=message.chat.id
chat_name=html.escape(message.chat.titleor"Local",quote=False)
chat_nick=message.chat.usernameorchat_name

current_date=html.escape(
format_date(date=current_datetime,locale=language_code),quote=False
)
current_time=html.escape(
format_time(time=current_datetime,locale=language_code),quote=False
)
current_timedate=html.escape(
format_datetime(datetime=current_datetime,locale=language_code),quote=False
)

text=(
text.replace("{first}",first_name)
.replace("{last}",last_name)
.replace("{fullname}",first_name+""+last_name)
.replace("{id}",str(user_id).replace("{userid}",str(user_id)))
.replace("{mention}",mention)
.replace("{username}",username)
.replace("{chatid}",str(chat_id))
.replace("{chatname}",str(chat_name))
.replace("{chatnick}",str(chat_nick))
.replace("{date}",str(current_date))
.replace("{time}",str(current_time))
.replace("{timedate}",str(current_timedate))
)
returntext
