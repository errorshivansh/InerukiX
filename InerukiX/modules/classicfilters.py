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

importasyncio
importos
importre

fromtelethonimportButton,events,utils
fromtelethon.tlimportfunctions,types

fromIneruki.services.eventsimportregister
fromIneruki.services.sql.filters_sqlimport(
add_filter,
get_all_filters,
remove_all_filters,
remove_filter,
)
fromIneruki.services.telethonimporttbot

DELETE_TIMEOUT=0
TYPE_TET=0
TYPE_PHOTO=1
TYPE_DOCUMENT=2
last_triggered_filters={}


asyncdefcan_change_info(message):
result=awaittbot(
functions.channels.GetParticipantRequest(
channel=message.chat_id,
user_id=message.sender_id,
)
)
p=result.participant
returnisinstance(p,types.ChannelParticipantCreator)or(
isinstance(p,types.ChannelParticipantAdmin)andp.admin_rights.change_info
)


@tbot.on(events.NewMessage(pattern=None))
asyncdefon_snip(event):

globallast_triggered_filters

name=event.raw_text

ifevent.chat_idinlast_triggered_filters:

ifnameinlast_triggered_filters[event.chat_id]:

returnFalse

snips=get_all_filters(event.chat_id)

ifsnips:

forsnipinsnips:

pattern=r"(|^|[^\w])"+re.escape(snip.keyword)+r"(|$|[^\w])"

ifre.search(pattern,name,flags=re.IGNORECASE):

ifsnip.snip_type==TYPE_PHOTO:

media=types.InputPhoto(
int(snip.media_id),
int(snip.media_access_hash),
snip.media_file_reference,
)

elifsnip.snip_type==TYPE_DOCUMENT:

media=types.InputDocument(
int(snip.media_id),
int(snip.media_access_hash),
snip.media_file_reference,
)

else:

media=None

event.message.id

ifevent.reply_to_msg_id:

event.reply_to_msg_id

filter=""
options=""
butto=None

if"|"insnip.reply:
filter,options=snip.reply.split("|")
else:
filter=str(snip.reply)
try:
filter=filter.strip()
button=options.strip()
if"•"inbutton:
mbutton=button.split("•")
lbutton=[]
foriinmbutton:
params=re.findall(r"\'(.*?)\'",i)orre.findall(
r"\"(.*?)\"",i
)
lbutton.append(params)
longbutton=[]
forcinlbutton:
butto=[Button.url(*c)]
longbutton.append(butto)
else:
params=re.findall(r"\'(.*?)\'",button)orre.findall(
r"\"(.*?)\"",button
)
butto=[Button.url(*params)]
exceptBaseException:
filter=filter.strip()
butto=None

try:
awaitevent.reply(filter,buttons=longbutton,file=media)
except:
awaitevent.reply(filter,buttons=butto,file=media)

ifevent.chat_idnotinlast_triggered_filters:

last_triggered_filters[event.chat_id]=[]

last_triggered_filters[event.chat_id].append(name)

awaitasyncio.sleep(DELETE_TIMEOUT)

last_triggered_filters[event.chat_id].remove(name)


@register(pattern="^/cfilter(.*)")
asyncdefon_snip_save(event):
ifevent.is_group:
ifnotawaitcan_change_info(message=event):
return
else:
return

name=event.pattern_match.group(1)
msg=awaitevent.get_reply_message()

ifmsg:

snip={"type":TYPE_TET,"text":msg.messageor""}

ifmsg.media:

media=None

ifisinstance(msg.media,types.MessageMediaPhoto):

media=utils.get_input_photo(msg.media.photo)

snip["type"]=TYPE_PHOTO

elifisinstance(msg.media,types.MessageMediaDocument):

media=utils.get_input_document(msg.media.document)

snip["type"]=TYPE_DOCUMENT

ifmedia:

snip["id"]=media.id

snip["hash"]=media.access_hash

snip["fr"]=media.file_reference

add_filter(
event.chat_id,
name,
snip["text"],
snip["type"],
snip.get("id"),
snip.get("hash"),
snip.get("fr"),
)

awaitevent.reply(
f"ClassicFilter{name}savedsuccessfully.youcangetitwith{name}\nNote:Tryournewfiltersystem/addfilter"
)

else:

awaitevent.reply(
"Usage:Replytousermessagewith/cfilter<text>..\nNotRecomendedusenewfiltersystem/savefilter"
)


@register(pattern="^/stopcfilter(.*)")
asyncdefon_snip_delete(event):
ifevent.is_group:
ifnotawaitcan_change_info(message=event):
return
else:
return
name=event.pattern_match.group(1)

remove_filter(event.chat_id,name)

awaitevent.reply(f"Filter**{name}**deletedsuccessfully")


@register(pattern="^/cfilters$")
asyncdefon_snip_list(event):
ifevent.is_group:
pass
else:
return
all_snips=get_all_filters(event.chat_id)

OUT_STR="AvailableClassicFiltersintheCurrentChat:\n"

iflen(all_snips)>0:

fora_snipinall_snips:

OUT_STR+=f"👉{a_snip.keyword}\n"

else:

OUT_STR="NoClassicFiltersinthischat."

iflen(OUT_STR)>4096:

withio.BytesIO(str.encode(OUT_STR))asout_file:

out_file.name="filters.text"

awaittbot.send_file(
event.chat_id,
out_file,
force_document=True,
allow_cache=False,
caption="AvailableClassicFiltersintheCurrentChat",
reply_to=event,
)

else:

awaitevent.reply(OUT_STR)


@register(pattern="^/stopallcfilters$")
asyncdefon_all_snip_delete(event):
ifevent.is_group:
ifnotawaitcan_change_info(message=event):
return
else:
return
remove_all_filters(event.chat_id)
awaitevent.reply(f"ClassicFilterincurrentchatdeleted!")


file_help=os.path.basename(__file__)
file_help=file_help.replace(".py","")
file_helpo=file_help.replace("_","")
