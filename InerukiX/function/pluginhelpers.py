importasyncio
importmath
importshlex
importsys
importtime
importtraceback
fromfunctoolsimportwraps
fromtypingimportCallable,Coroutine,Dict,List,Tuple,Union

importaiohttp
fromPILimportImage
frompyrogramimportClient
frompyrogram.errorsimportFloodWait,MessageNotModified
frompyrogram.typesimportChat,Message,User

fromInerukiimportOWNER_ID,SUPPORT_CHAT
fromIneruki.services.pyrogramimportpbot


defget_user(message:Message,text:str)->[int,str,None]:
iftextisNone:
asplit=None
else:
asplit=text.split("",1)
user_s=None
reason_=None
ifmessage.reply_to_message:
user_s=message.reply_to_message.from_user.id
reason_=textiftextelseNone
elifasplitisNone:
returnNone,None
eliflen(asplit[0])>0:
user_s=int(asplit[0])ifasplit[0].isdigit()elseasplit[0]
iflen(asplit)==2:
reason_=asplit[1]
returnuser_s,reason_


defget_readable_time(seconds:int)->int:
count=0
ping_time=""
time_list=[]
time_suffix_list=["s","m","h","days"]

whilecount<4:
count+=1
ifcount<3:
remainder,result=divmod(seconds,60)
else:
remainder,result=divmod(seconds,24)
ifseconds==0andremainder==0:
break
time_list.append(int(result))
seconds=int(remainder)

forxinrange(len(time_list)):
time_list[x]=str(time_list[x])+time_suffix_list[x]
iflen(time_list)==4:
ping_time+=time_list.pop()+","

time_list.reverse()
ping_time+=":".join(time_list)

returnping_time


deftime_formatter(milliseconds:int)->str:
seconds,milliseconds=divmod(int(milliseconds),1000)
minutes,seconds=divmod(seconds,60)
hours,minutes=divmod(minutes,60)
days,hours=divmod(hours,24)
tmp=(
((str(days)+"day(s),")ifdayselse"")
+((str(hours)+"hour(s),")ifhourselse"")
+((str(minutes)+"minute(s),")ifminuteselse"")
+((str(seconds)+"second(s),")ifsecondselse"")
+((str(milliseconds)+"millisecond(s),")ifmillisecondselse"")
)
returntmp[:-2]


asyncdefdelete_or_pass(message):
ifmessage.from_user.id==1141839926:
returnmessage
returnawaitmessage.delete()


defhumanbytes(size):
ifnotsize:
return""
power=2**10
raised_to_pow=0
dict_power_n={0:"",1:"Ki",2:"Mi",3:"Gi",4:"Ti"}
whilesize>power:
size/=power
raised_to_pow+=1
returnstr(round(size,2))+""+dict_power_n[raised_to_pow]+"B"


asyncdefprogress(current,total,message,start,type_of_ps,file_name=None):
now=time.time()
diff=now-start
ifround(diff%10.00)==0orcurrent==total:
percentage=current*100/total
speed=current/diff
elapsed_time=round(diff)*1000
ifelapsed_time==0:
return
time_to_completion=round((total-current)/speed)*1000
estimated_total_time=elapsed_time+time_to_completion
progress_str="{0}{1}{2}%\n".format(
"".join(["🔴"foriinrange(math.floor(percentage/10))]),
"".join(["🔘"foriinrange(10-math.floor(percentage/10))]),
round(percentage,2),
)
tmp=progress_str+"{0}of{1}\nETA:{2}".format(
humanbytes(current),humanbytes(total),time_formatter(estimated_total_time)
)
iffile_name:
try:
awaitmessage.edit(
"{}\n**FileName:**`{}`\n{}".format(type_of_ps,file_name,tmp)
)
exceptFloodWaitase:
awaitasyncio.sleep(e.x)
exceptMessageNotModified:
pass
else:
try:
awaitmessage.edit("{}\n{}".format(type_of_ps,tmp))
exceptFloodWaitase:
awaitasyncio.sleep(e.x)
exceptMessageNotModified:
pass


defget_text(message:Message)->[None,str]:
text_to_return=message.text
ifmessage.textisNone:
returnNone
if""intext_to_return:
try:
returnmessage.text.split(None,1)[1]
exceptIndexError:
returnNone
else:
returnNone


asyncdefiter_chats(client):
chats=[]
asyncfordialoginclient.iter_dialogs():
ifdialog.chat.typein["supergroup","channel"]:
chats.append(dialog.chat.id)
returnchats


asyncdeffetch_audio(client,message):
time.time()
ifnotmessage.reply_to_message:
awaitmessage.reply("`ReplyToAVideo/Audio.`")
return
warner_stark=message.reply_to_message
ifwarner_stark.audioisNoneandwarner_stark.videoisNone:
awaitmessage.reply("`FormatNotSupported`")
return
ifwarner_stark.video:
lel=awaitmessage.reply("`VideoDetected,ConvertingToAudio!`")
warner_bros=awaitmessage.reply_to_message.download()
stark_cmd=f"ffmpeg-i{warner_bros}-map0:afriday.mp3"
awaitruncmd(stark_cmd)
final_warner="friday.mp3"
elifwarner_stark.audio:
lel=awaitedit_or_reply(message,"`DownloadStarted!`")
final_warner=awaitmessage.reply_to_message.download()
awaitlel.edit("`AlmostDone!`")
awaitlel.delete()
returnfinal_warner


asyncdefedit_or_reply(message,text,parse_mode="md"):
ifmessage.from_user.id:
ifmessage.reply_to_message:
kk=message.reply_to_message.message_id
returnawaitmessage.reply_text(
text,reply_to_message_id=kk,parse_mode=parse_mode
)
returnawaitmessage.reply_text(text,parse_mode=parse_mode)
returnawaitmessage.edit(text,parse_mode=parse_mode)


asyncdefruncmd(cmd:str)->Tuple[str,str,int,int]:
"""runcommandinterminal"""
args=shlex.split(cmd)
process=awaitasyncio.create_subprocess_exec(
*args,stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE
)
stdout,stderr=awaitprocess.communicate()
return(
stdout.decode("utf-8","replace").strip(),
stderr.decode("utf-8","replace").strip(),
process.returncode,
process.pid,
)


asyncdefconvert_to_image(message,client)->[None,str]:
"""ConvertMostMediaFormatsToRawImage"""
final_path=None
ifnot(
message.reply_to_message.photo
ormessage.reply_to_message.sticker
ormessage.reply_to_message.media
ormessage.reply_to_message.animation
ormessage.reply_to_message.audio
):
returnNone
ifmessage.reply_to_message.photo:
final_path=awaitmessage.reply_to_message.download()
elifmessage.reply_to_message.sticker:
ifmessage.reply_to_message.sticker.mime_type=="image/webp":
final_path="webp_to_png_s_proton.png"
path_s=awaitmessage.reply_to_message.download()
im=Image.open(path_s)
im.save(final_path,"PNG")
else:
path_s=awaitclient.download_media(message.reply_to_message)
final_path="lottie_proton.png"
cmd=(
f"lottie_convert.py--frame0-iflottie-ofpng{path_s}{final_path}"
)
awaitruncmd(cmd)
elifmessage.reply_to_message.audio:
thumb=message.reply_to_message.audio.thumbs[0].file_id
final_path=awaitclient.download_media(thumb)
elifmessage.reply_to_message.videoormessage.reply_to_message.animation:
final_path="fetched_thumb.png"
vid_path=awaitclient.download_media(message.reply_to_message)
awaitruncmd(f"ffmpeg-i{vid_path}-filter:vscale=500:500-an{final_path}")
returnfinal_path


defget_text(message:Message)->[None,str]:
"""ExtractTextFromCommands"""
text_to_return=message.text
ifmessage.textisNone:
returnNone
if""intext_to_return:
try:
returnmessage.text.split(None,1)[1]
exceptIndexError:
returnNone
else:
returnNone


#Admincheck

admins:Dict[str,List[User]]={}


defset(chat_id:Union[str,int],admins_:List[User]):
ifisinstance(chat_id,int):
chat_id=str(chat_id)

admins[chat_id]=admins_


defget(chat_id:Union[str,int])->Union[List[User],bool]:
ifisinstance(chat_id,int):
chat_id=str(chat_id)

ifchat_idinadmins:
returnadmins[chat_id]

returnFalse


asyncdefget_administrators(chat:Chat)->List[User]:
_get=get(chat.id)

if_get:
return_get
else:
set(
chat.id,
[member.userformemberinawaitchat.get_members(filter="administrators")],
)
returnawaitget_administrators(chat)


defadmins_only(func:Callable)->Coroutine:
asyncdefwrapper(client:Client,message:Message):
ifmessage.from_user.id==OWNER_ID:
returnawaitfunc(client,message)
admins=awaitget_administrators(message.chat)
foradmininadmins:
ifadmin.id==message.from_user.id:
returnawaitfunc(client,message)

returnwrapper


#@Mr_Dark_Prince
defcapture_err(func):
@wraps(func)
asyncdefcapture(client,message,*args,**kwargs):
try:
returnawaitfunc(client,message,*args,**kwargs)
exceptExceptionaserr:
exc_type,exc_obj,exc_tb=sys.exc_info()
errors=traceback.format_exception(
etype=exc_type,
value=exc_obj,
tb=exc_tb,
)
error_feedback=split_limits(
"**ERROR**|`{}`|`{}`\n\n```{}```\n\n```{}```\n".format(
0ifnotmessage.from_userelsemessage.from_user.id,
0ifnotmessage.chatelsemessage.chat.id,
message.textormessage.caption,
"".join(errors),
),
)
forxinerror_feedback:
awaitpbot.send_message(SUPPORT_CHAT,x)
raiseerr

returncapture


#Portedfromhttps://github.com/TheHamkerCat/WilliamButcherBot
"""
MITLicense
Copyright(c)2021TheHamkerCat
Permissionisherebygranted,freeofcharge,toanypersonobtainingacopy
ofthissoftwareandassociateddocumentationfiles(the"Software"),todeal
intheSoftwarewithoutrestriction,includingwithoutlimitationtherights
touse,copy,modify,merge,publish,distribute,sublicense,and/orsell
copiesoftheSoftware,andtopermitpersonstowhomtheSoftwareis
furnishedtodoso,subjecttothefollowingconditions:
Theabovecopyrightnoticeandthispermissionnoticeshallbeincludedinall
copiesorsubstantialportionsoftheSoftware.
THESOFTWAREISPROVIDED"ASIS",WITHOUTWARRANTYOFANYKIND,EPRESSOR
IMPLIED,INCLUDINGBUTNOTLIMITEDTOTHEWARRANTIESOFMERCHANTABILITY,
FITNESSFORAPARTICULARPURPOSEANDNONINFRINGEMENT.INNOEVENTSHALLTHE
AUTHORSORCOPYRIGHTHOLDERSBELIABLEFORANYCLAIM,DAMAGESOROTHER
LIABILITY,WHETHERINANACTIONOFCONTRACT,TORTOROTHERWISE,ARISINGFROM,
OUTOFORINCONNECTIONWITHTHESOFTWAREORTHEUSEOROTHERDEALINGSINTHE
SOFTWARE.
"""


asyncdefmember_permissions(chat_id,user_id):
perms=[]
member=awaitpbot.get_chat_member(chat_id,user_id)
ifmember.can_post_messages:
perms.append("can_post_messages")
ifmember.can_edit_messages:
perms.append("can_edit_messages")
ifmember.can_delete_messages:
perms.append("can_delete_messages")
ifmember.can_restrict_members:
perms.append("can_restrict_members")
ifmember.can_promote_members:
perms.append("can_promote_members")
ifmember.can_change_info:
perms.append("can_change_info")
ifmember.can_invite_users:
perms.append("can_invite_users")
ifmember.can_pin_messages:
perms.append("can_pin_messages")
returnperms


asyncdefcurrent_chat_permissions(chat_id):
perms=[]
perm=(awaitpbot.get_chat(chat_id)).permissions
ifperm.can_send_messages:
perms.append("can_send_messages")
ifperm.can_send_media_messages:
perms.append("can_send_media_messages")
ifperm.can_send_stickers:
perms.append("can_send_stickers")
ifperm.can_send_animations:
perms.append("can_send_animations")
ifperm.can_send_games:
perms.append("can_send_games")
ifperm.can_use_inline_bots:
perms.append("can_use_inline_bots")
ifperm.can_add_web_page_previews:
perms.append("can_add_web_page_previews")
ifperm.can_send_polls:
perms.append("can_send_polls")
ifperm.can_change_info:
perms.append("can_change_info")
ifperm.can_invite_users:
perms.append("can_invite_users")
ifperm.can_pin_messages:
perms.append("can_pin_messages")

returnperms


#URLLOCK


defget_url(message_1:Message)->Union[str,None]:
messages=[message_1]

ifmessage_1.reply_to_message:
messages.append(message_1.reply_to_message)

text=""
offset=None
length=None

formessageinmessages:
ifoffset:
break

ifmessage.entities:
forentityinmessage.entities:
ifentity.type=="url":
text=message.textormessage.caption
offset,length=entity.offset,entity.length
break

ifoffsetin(None,):
returnNone

returntext[offset:offset+length]


asyncdeffetch(url):
asyncwithaiohttp.ClientSession()assession:
asyncwithsession.get(url)asresp:
try:
data=awaitresp.json()
exceptException:
data=awaitresp.text()
returndata


asyncdefconvert_seconds_to_minutes(seconds:int):
seconds=int(seconds)
seconds=seconds%(24*3600)
seconds%=3600
minutes=seconds//60
seconds%=60
return"%02d:%02d"%(minutes,seconds)


asyncdefjson_object_prettify(objecc):
dicc=objecc.__dict__
output=""
forkey,valueindicc.items():
ifkey=="pinned_message"orkey=="photo"orkey=="_"orkey=="_client":
continue
output+=f"**{key}:**`{value}`\n"
returnoutput


asyncdefjson_prettify(data):
output=""
try:
forkey,valueindata.items():
output+=f"**{key}:**`{value}`\n"
exceptException:
fordatasindata:
forkey,valueindatas.items():
output+=f"**{key}:**`{value}`\n"
output+="------------------------\n"
returnoutput
