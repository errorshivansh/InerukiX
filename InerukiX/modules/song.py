#Inerukixmusic(Telegrambotproject)
#Copyright(C)2021errorshivansh

#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseas
#publishedbytheFreeSoftwareFoundation,eitherversion3ofthe
#License,or(atyouroption)anylaterversion.

#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.
#
#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<https://www.gnu.org/licenses/>.


from__future__importunicode_literals

importasyncio
importos
importtime
fromrandomimportrandint
fromurllib.parseimporturlparse

importaiofiles
importaiohttp
importwget
importyoutube_dl
frompyrogramimportfilters
frompyrogram.typesimportMessage
fromyoutube_dlimportYoutubeDL
fromyoutubesearchpythonimportSearchVideos

fromIneruki.function.inlinehelperimportarq
fromIneruki.function.pluginhelpersimportget_text,progress
fromIneruki.services.pyrogramimportpbotasClient

dl_limit=0


@Client.on_message(filters.command(["music","song"]))
asyncdefytmusic(client,message:Message):
urlissed=get_text(message)
ifnoturlissed:
awaitclient.send_message(
message.chat.id,
"InvalidCommandSyntax,PleaseCheckHelpMenuToKnowMore!",
)
return
globaldl_limit
ifdl_limit>=4:
awaitmessage.reply_text(
"Ineruki'sserverbusyduetotoomanydownloads,tryagainaftersometime."
)
return
pablo=awaitclient.send_message(
message.chat.id,f"`Getting{urlissed}FromYoutubeServers.PleaseWait.`"
)
search=SearchVideos(f"{urlissed}",offset=1,mode="dict",max_results=1)
try:
mi=search.result()
mio=mi["search_result"]
mo=mio[0]["link"]
mio[0]["duration"]
thum=mio[0]["title"]
fridayz=mio[0]["id"]
thums=mio[0]["channel"]
kekme=f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
except:
awaitmessage.reply_text(
"SorryIaccountedanerror.\nUnkownerrorraisedwhilegettingsearchresult"
)
return

awaitasyncio.sleep(0.6)
sedlyf=wget.download(kekme)
opts={
"format":"bestaudio",
"addmetadata":True,
"key":"FFmpegMetadata",
"writethumbnail":True,
"prefer_ffmpeg":True,
"geo_bypass":True,
"nocheckcertificate":True,
"postprocessors":[
{
"key":"FFmpegExtractAudio",
"preferredcodec":"mp3",
"preferredquality":"720",
}
],
"outtmpl":"%(id)s.mp3",
"quiet":True,
"logtostderr":False,
}
try:
dl_limit=dl_limit+1
withYoutubeDL(opts)asytdl:
ytdl_data=ytdl.extract_info(mo,download=True)

exceptExceptionase:
awaitpablo.edit(f"**FailedToDownload**\n**Error:**`{str(e)}`")
#dl_limit=dl_limit-1
return
c_time=time.time()
capy=f"**SongName:**`{thum}`\n**RequestedFor:**`{urlissed}`\n**Channel:**`{thums}`\n**Link:**`{mo}`"
file_stark=f"{ytdl_data['id']}.mp3"
try:
awaitclient.send_audio(
message.chat.id,
audio=open(file_stark,"rb"),
duration=int(ytdl_data["duration"]),
title=str(ytdl_data["title"]),
performer=str(ytdl_data["uploader"]),
thumb=sedlyf,
caption=capy,
progress=progress,
progress_args=(
pablo,
c_time,
f"`Uploading{urlissed}SongFromYouTubeMusic!`",
file_stark,
),
)
dl_limit=dl_limit-1
except:
dl_limit=dl_limit-1
return
awaitpablo.delete()
forfilesin(sedlyf,file_stark):
iffilesandos.path.exists(files):
os.remove(files)


ydl_opts={
"format":"bestaudio/best",
"writethumbnail":True,
"postprocessors":[
{
"key":"FFmpegExtractAudio",
"preferredcodec":"mp3",
"preferredquality":"192",
}
],
}


defget_file_extension_from_url(url):
url_path=urlparse(url).path
basename=os.path.basename(url_path)
returnbasename.split(".")[-1]


#FuntionToDownloadSong
asyncdefdownload_song(url):
song_name=f"{randint(6969,6999)}.mp3"
asyncwithaiohttp.ClientSession()assession:
asyncwithsession.get(url)asresp:
ifresp.status==200:
f=awaitaiofiles.open(song_name,mode="wb")
awaitf.write(awaitresp.read())
awaitf.close()
returnsong_name


is_downloading=False


deftime_to_seconds(time):
stringt=str(time)
returnsum(int(x)*60**ifori,xinenumerate(reversed(stringt.split(":"))))


@Client.on_message(filters.command("saavn")&~filters.edited)
asyncdefjssong(_,message):
globalis_downloading
globaldl_limit
iflen(message.command)<2:
awaitmessage.reply_text("/saavnrequiresanargument.")
return
ifdl_limit>=3:
awaitmessage.reply_text(
"Ineruki'sserverbusyduetotoomanydownloads,tryagainaftersometime."
)
return
ifis_downloading:
awaitmessage.reply_text(
"Anotherdownloadisinprogress,tryagainaftersometime."
)
return
is_downloading=True
text=message.text.split(None,1)[1]
query=text.replace("","%20")
m=awaitmessage.reply_text("Searching...")
try:
songs=awaitarq.saavn(query)
ifnotsongs.ok:
awaitmessage.reply_text(songs.result)
return
sname=songs.result[0].song
slink=songs.result[0].media_url
ssingers=songs.result[0].singers
awaitm.edit("Downloading")
song=awaitdownload_song(slink)
awaitm.edit("Uploading")
awaitmessage.reply_audio(audio=song,title=sname,performer=ssingers)
os.remove(song)
awaitm.delete()
exceptExceptionase:
is_downloading=False
awaitm.edit(str(e))
return
is_downloading=False


#DeezerMusic


@Client.on_message(filters.command("deezer")&~filters.edited)
asyncdefdeezsong(_,message):
globalis_downloading
iflen(message.command)<2:
awaitmessage.reply_text("/deezerrequiresanargument.")
return
ifis_downloading:
awaitmessage.reply_text(
"Anotherdownloadisinprogress,tryagainaftersometime."
)
return
ifdl_limit>=3:
awaitmessage.reply_text(
"Ineruki'sserverbusyduetotoomanydownloads,tryagainaftersometime."
)
return
is_downloading=True
text=message.text.split(None,1)[1]
query=text.replace("","%20")
m=awaitmessage.reply_text("Searching...")
try:
songs=awaitarq.deezer(query,1)
ifnotsongs.ok:
awaitmessage.reply_text(songs.result)
return
title=songs.result[0].title
url=songs.result[0].url
artist=songs.result[0].artist
awaitm.edit("Downloading")
song=awaitdownload_song(url)
awaitm.edit("Uploading")
awaitmessage.reply_audio(audio=song,title=title,performer=artist)
os.remove(song)
awaitm.delete()
exceptExceptionase:
is_downloading=False
awaitm.edit(str(e))
return
is_downloading=False


@Client.on_message(filters.command(["vsong","video"]))
asyncdefytmusic(client,message:Message):
globalis_downloading
ifis_downloading:
awaitmessage.reply_text(
"Anotherdownloadisinprogress,tryagainaftersometime."
)
return
globaldl_limit
ifdl_limit>=4:
awaitmessage.reply_text(
"Inerukisserverbusyduetotoomanydownloads,tryagainaftersometime."
)
return
urlissed=get_text(message)

pablo=awaitclient.send_message(
message.chat.id,f"`Getting{urlissed}FromYoutubeServers.PleaseWait.`"
)
ifnoturlissed:
awaitpablo.edit("InvalidCommandSyntax,PleaseCheckHelpMenuToKnowMore!")
return

search=SearchVideos(f"{urlissed}",offset=1,mode="dict",max_results=1)
try:
mi=search.result()
mio=mi["search_result"]
mo=mio[0]["link"]
thum=mio[0]["title"]
fridayz=mio[0]["id"]
thums=mio[0]["channel"]
kekme=f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
except:
awaitmessage.reply_text(
"Unknownerrorraisedwhilegettingresultfromyoutube"
)
return
awaitasyncio.sleep(0.6)
url=mo
sedlyf=wget.download(kekme)
opts={
"format":"best",
"addmetadata":True,
"key":"FFmpegMetadata",
"prefer_ffmpeg":True,
"geo_bypass":True,
"nocheckcertificate":True,
"postprocessors":[{"key":"FFmpegVideoConvertor","preferedformat":"mp4"}],
"outtmpl":"%(id)s.mp4",
"logtostderr":False,
"quiet":True,
}
try:
is_downloading=True
withyoutube_dl.YoutubeDL(opts)asytdl:
infoo=ytdl.extract_info(url,False)
duration=round(infoo["duration"]/60)

ifduration>8:
awaitpablo.edit(
f"❌Videoslongerthan8minute(s)arentallowed,theprovidedvideois{duration}minute(s)"
)
is_downloading=False
return
ytdl_data=ytdl.extract_info(url,download=True)

exceptException:
#awaitpablo.edit(event,f"**FailedToDownload**\n**Error:**`{str(e)}`")
is_downloading=False
return

c_time=time.time()
file_stark=f"{ytdl_data['id']}.mp4"
capy=f"**VideoName➠**`{thum}`\n**RequestedFor:**`{urlissed}`\n**Channel:**`{thums}`\n**Link:**`{mo}`"
awaitclient.send_video(
message.chat.id,
video=open(file_stark,"rb"),
duration=int(ytdl_data["duration"]),
file_name=str(ytdl_data["title"]),
thumb=sedlyf,
caption=capy,
supports_streaming=True,
progress=progress,
progress_args=(
pablo,
c_time,
f"`Uploading{urlissed}SongFromYouTubeMusic!`",
file_stark,
),
)
awaitpablo.delete()
is_downloading=False
forfilesin(sedlyf,file_stark):
iffilesandos.path.exists(files):
os.remove(files)
