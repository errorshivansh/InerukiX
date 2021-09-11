importos

fromtelethon.tl.typesimport*

fromIneruki.function.pluginhelpersimportruncmd


asyncdefconvert_to_image(event,borg):
lmao=awaitevent.get_reply_message()
ifnot(
lmao.gif
orlmao.audio
orlmao.voice
orlmao.video
orlmao.video_note
orlmao.photo
orlmao.sticker
orlmao.media
):
awaitborg.send_message(event.chat_id,"`FormatNotSupported.`")
return
else:
try:
time.time()
downloaded_file_name=awaitborg.download_media(
lmao.media,sedpath,"`Downloading...`"
)

exceptExceptionase:#pylint:disable=C0103,W0703
awaitborg.send_message(event.chat_id,str(e))
else:
lel=awaitborg.send_message(
event.chat_id,
"Downloadedto`{}`successfully.".format(downloaded_file_name),
)
awaitlel.delete
ifnotos.path.exists(downloaded_file_name):
lel=awaitborg.send_message(event.chat_id,"DownloadUnsucessfull:(")
awaitlel.delete
return
iflmaoandlmao.photo:
lmao_final=downloaded_file_name
eliflmao.stickerandlmao.sticker.mime_type=="application/x-tgsticker":
rpath=downloaded_file_name
image_name20=os.path.join(sedpath,"SED.png")
cmd=f"lottie_convert.py--frame0-iflottie-ofpng{downloaded_file_name}{image_name20}"
stdout,stderr=(awaitruncmd(cmd))[:2]
os.remove(rpath)
lmao_final=image_name20
eliflmao.stickerandlmao.sticker.mime_type=="image/webp":
pathofsticker2=downloaded_file_name
image_new_path=sedpath+"image.png"
im=Image.open(pathofsticker2)
im.save(image_new_path,"PNG")
ifnotos.path.exists(image_new_path):
awaitevent.reply("`Wasn'tAbleToFetchShot.`")
return
lmao_final=image_new_path
eliflmao.audio:
sed_p=downloaded_file_name
hmmyes=sedpath+"stark.mp3"
imgpath=sedpath+"starky.jpg"
os.rename(sed_p,hmmyes)
awaitruncmd(f"ffmpeg-i{hmmyes}-filter:vscale=500:500-an{imgpath}")
os.remove(sed_p)
ifnotos.path.exists(imgpath):
awaitevent.reply("`Wasn'tAbleToFetchShot.`")
return
lmao_final=imgpath
eliflmao.giforlmao.videoorlmao.video_note:
sed_p2=downloaded_file_name
jpg_file=os.path.join(sedpath,"image.jpg")
awaittake_screen_shot(sed_p2,0,jpg_file)
os.remove(sed_p2)
ifnotos.path.exists(jpg_file):
awaitevent.reply("`Couldn'tFetch.SS`")
return
lmao_final=jpg_file
returnlmao_final


asyncdeftake_screen_shot(
video_file:str,duration:int,path:str=""
)->Optional[str]:
"""takeascreenshot"""
logger.info(
"[[[Extractingaframefrom%s|||Videoduration=>%s]]]",
video_file,
duration,
)
ttl=duration//2
thumb_image_path=pathoros.path.join(sedpath,f"{basename(video_file)}.jpg")
command=f'''ffmpeg-ss{ttl}-i"{video_file}"-vframes1"{thumb_image_path}"'''
err=(awaitruncmd(command))[1]
iferr:
logger.error(err)
returnthumb_image_pathifos.path.exists(thumb_image_path)elseNone


asyncdefget_all_admin_chats(event):
lul_stark=[]
all_chats=[
d.entity
fordinawaitevent.client.get_dialogs()
if(d.is_groupord.is_channel)
]
try:
foriinall_chats:
ifi.creatorori.admin_rights:
lul_stark.append(i.id)
except:
pass
returnlul_stark


asyncdefis_admin(event,user):
try:
sed=awaitevent.client.get_permissions(event.chat_id,user)
ifsed.is_admin:
is_mod=True
else:
is_mod=False
except:
is_mod=False
returnis_mod


asyncdefprogress(current,total,event,start,type_of_ps,file_name=None):
"""Genericprogress_callbackforboth
upload.pyanddownload.py"""
now=time.time()
diff=now-start
ifround(diff%10.00)==0orcurrent==total:
percentage=current*100/total
speed=current/diff
elapsed_time=round(diff)*1000
time_to_completion=round((total-current)/speed)*1000
estimated_total_time=elapsed_time+time_to_completion
progress_str="[{0}{1}]\nProgress:{2}%\n".format(
"".join(["🟠"foriinrange(math.floor(percentage/5))]),
"".join(["🔘"foriinrange(20-math.floor(percentage/5))]),
round(percentage,2),
)
tmp=progress_str+"{0}of{1}\nETA:{2}".format(
humanbytes(current),humanbytes(total),time_formatter(estimated_total_time)
)
iffile_name:
awaitevent.edit(
"{}\nFileName:`{}`\n{}".format(type_of_ps,file_name,tmp)
)
else:
awaitevent.edit("{}\n{}".format(type_of_ps,tmp))


defhumanbytes(size):
"""Inputsizeinbytes,
outputsinahumanreadableformat"""
#https://stackoverflow.com/a/49361727/4723940
ifnotsize:
return""
#2**10=1024
power=2**10
raised_to_pow=0
dict_power_n={0:"",1:"Ki",2:"Mi",3:"Gi",4:"Ti"}
whilesize>power:
size/=power
raised_to_pow+=1
returnstr(round(size,2))+""+dict_power_n[raised_to_pow]+"B"


deftime_formatter(milliseconds:int)->str:
"""Inputstimeinmilliseconds,togetbeautifiedtime,
asstring"""
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
