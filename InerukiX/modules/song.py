#XInerukixmusicX(TelegramXbotXprojectX)
#XCopyrightX(C)X2021XXerrorshivansh

#XThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXas
#XpublishedXbyXtheXFreeXSoftwareXFoundation,XeitherXversionX3XofXthe
#XLicense,XorX(atXyourXoption)XanyXlaterXversion.

#XThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.
#
#XYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XalongXwithXthisXprogram.XXIfXnot,XseeX<https://www.gnu.org/licenses/>.


fromX__future__XimportXunicode_literals

importXasyncio
importXos
importXtime
fromXrandomXimportXrandint
fromXurllib.parseXimportXurlparse

importXaiofiles
importXaiohttp
importXwget
importXyoutube_dl
fromXpyrogramXimportXfilters
fromXpyrogram.typesXimportXMessage
fromXyoutube_dlXimportXYoutubeDL
fromXyoutubesearchpythonXimportXSearchVideos

fromXInerukiX.function.inlinehelperXimportXarq
fromXInerukiX.function.pluginhelpersXimportXget_text,Xprogress
fromXInerukiX.services.pyrogramXimportXpbotXasXClient

dl_limitX=X0


@Client.on_message(filters.command(["music",X"song"]))
asyncXdefXytmusic(client,Xmessage:XMessage):
XXXXurlissedX=Xget_text(message)
XXXXifXnotXurlissed:
XXXXXXXXawaitXclient.send_message(
XXXXXXXXXXXXmessage.chat.id,
XXXXXXXXXXXX"InvalidXCommandXSyntax,XPleaseXCheckXHelpXMenuXToXKnowXMore!",
XXXXXXXX)
XXXXXXXXreturn
XXXXglobalXdl_limit
XXXXifXdl_limitX>=X4:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"Ineruki'sXserverXbusyXdueXtoXtooXmanyXdownloads,XtryXagainXafterXsometime."
XXXXXXXX)
XXXXXXXXreturn
XXXXpabloX=XawaitXclient.send_message(
XXXXXXXXmessage.chat.id,Xf"`GettingX{urlissed}XFromXYoutubeXServers.XPleaseXWait.`"
XXXX)
XXXXsearchX=XSearchVideos(f"{urlissed}",Xoffset=1,Xmode="dict",Xmax_results=1)
XXXXtry:
XXXXXXXXmiX=Xsearch.result()
XXXXXXXXmioX=Xmi["search_result"]
XXXXXXXXmoX=Xmio[0]["link"]
XXXXXXXXmio[0]["duration"]
XXXXXXXXthumX=Xmio[0]["title"]
XXXXXXXXfridayzX=Xmio[0]["id"]
XXXXXXXXthumsX=Xmio[0]["channel"]
XXXXXXXXkekmeX=Xf"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
XXXXexcept:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"SorryXIXaccountedXanXerror.\nXUnkownXerrorXraisedXwhileXgettingXsearchXresult"
XXXXXXXX)
XXXXXXXXreturn

XXXXawaitXasyncio.sleep(0.6)
XXXXsedlyfX=Xwget.download(kekme)
XXXXoptsX=X{
XXXXXXXX"format":X"bestaudio",
XXXXXXXX"addmetadata":XTrue,
XXXXXXXX"key":X"FFmpegMetadata",
XXXXXXXX"writethumbnail":XTrue,
XXXXXXXX"prefer_ffmpeg":XTrue,
XXXXXXXX"geo_bypass":XTrue,
XXXXXXXX"nocheckcertificate":XTrue,
XXXXXXXX"postprocessors":X[
XXXXXXXXXXXX{
XXXXXXXXXXXXXXXX"key":X"FFmpegExtractAudio",
XXXXXXXXXXXXXXXX"preferredcodec":X"mp3",
XXXXXXXXXXXXXXXX"preferredquality":X"720",
XXXXXXXXXXXX}
XXXXXXXX],
XXXXXXXX"outtmpl":X"%(id)s.mp3",
XXXXXXXX"quiet":XTrue,
XXXXXXXX"logtostderr":XFalse,
XXXX}
XXXXtry:
XXXXXXXXdl_limitX=Xdl_limitX+X1
XXXXXXXXwithXYoutubeDL(opts)XasXytdl:
XXXXXXXXXXXXytdl_dataX=Xytdl.extract_info(mo,Xdownload=True)

XXXXexceptXExceptionXasXe:
XXXXXXXXawaitXpablo.edit(f"**FailedXToXDownload**X\n**ErrorX:**X`{str(e)}`")
XXXXXXXX#Xdl_limitX=Xdl_limit-1
XXXXXXXXreturn
XXXXc_timeX=Xtime.time()
XXXXcapyX=Xf"**SongXNameX:**X`{thum}`X\n**RequestedXForX:**X`{urlissed}`X\n**ChannelX:**X`{thums}`X\n**LinkX:**X`{mo}`"
XXXXfile_starkX=Xf"{ytdl_data['id']}.mp3"
XXXXtry:
XXXXXXXXawaitXclient.send_audio(
XXXXXXXXXXXXmessage.chat.id,
XXXXXXXXXXXXaudio=open(file_stark,X"rb"),
XXXXXXXXXXXXduration=int(ytdl_data["duration"]),
XXXXXXXXXXXXtitle=str(ytdl_data["title"]),
XXXXXXXXXXXXperformer=str(ytdl_data["uploader"]),
XXXXXXXXXXXXthumb=sedlyf,
XXXXXXXXXXXXcaption=capy,
XXXXXXXXXXXXprogress=progress,
XXXXXXXXXXXXprogress_args=(
XXXXXXXXXXXXXXXXpablo,
XXXXXXXXXXXXXXXXc_time,
XXXXXXXXXXXXXXXXf"`UploadingX{urlissed}XSongXFromXYouTubeXMusic!`",
XXXXXXXXXXXXXXXXfile_stark,
XXXXXXXXXXXX),
XXXXXXXX)
XXXXXXXXdl_limitX=Xdl_limitX-X1
XXXXexcept:
XXXXXXXXdl_limitX=Xdl_limitX-X1
XXXXXXXXreturn
XXXXawaitXpablo.delete()
XXXXforXfilesXinX(sedlyf,Xfile_stark):
XXXXXXXXifXfilesXandXos.path.exists(files):
XXXXXXXXXXXXos.remove(files)


ydl_optsX=X{
XXXX"format":X"bestaudio/best",
XXXX"writethumbnail":XTrue,
XXXX"postprocessors":X[
XXXXXXXX{
XXXXXXXXXXXX"key":X"FFmpegExtractAudio",
XXXXXXXXXXXX"preferredcodec":X"mp3",
XXXXXXXXXXXX"preferredquality":X"192",
XXXXXXXX}
XXXX],
}


defXget_file_extension_from_url(url):
XXXXurl_pathX=Xurlparse(url).path
XXXXbasenameX=Xos.path.basename(url_path)
XXXXreturnXbasename.split(".")[-1]


#XFuntionXToXDownloadXSong
asyncXdefXdownload_song(url):
XXXXsong_nameX=Xf"{randint(6969,X6999)}.mp3"
XXXXasyncXwithXaiohttp.ClientSession()XasXsession:
XXXXXXXXasyncXwithXsession.get(url)XasXresp:
XXXXXXXXXXXXifXresp.statusX==X200:
XXXXXXXXXXXXXXXXfX=XawaitXaiofiles.open(song_name,Xmode="wb")
XXXXXXXXXXXXXXXXawaitXf.write(awaitXresp.read())
XXXXXXXXXXXXXXXXawaitXf.close()
XXXXreturnXsong_name


is_downloadingX=XFalse


defXtime_to_seconds(time):
XXXXstringtX=Xstr(time)
XXXXreturnXsum(int(x)X*X60X**XiXforXi,XxXinXenumerate(reversed(stringt.split(":"))))


@Client.on_message(filters.command("saavn")X&X~filters.edited)
asyncXdefXjssong(_,Xmessage):
XXXXglobalXis_downloading
XXXXglobalXdl_limit
XXXXifXlen(message.command)X<X2:
XXXXXXXXawaitXmessage.reply_text("/saavnXrequiresXanXargument.")
XXXXXXXXreturn
XXXXifXdl_limitX>=X3:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"Ineruki'sXserverXbusyXdueXtoXtooXmanyXdownloads,XtryXagainXafterXsometime."
XXXXXXXX)
XXXXXXXXreturn
XXXXifXis_downloading:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"AnotherXdownloadXisXinXprogress,XtryXagainXafterXsometime."
XXXXXXXX)
XXXXXXXXreturn
XXXXis_downloadingX=XTrue
XXXXtextX=Xmessage.text.split(None,X1)[1]
XXXXqueryX=Xtext.replace("X",X"%20")
XXXXmX=XawaitXmessage.reply_text("Searching...")
XXXXtry:
XXXXXXXXsongsX=XawaitXarq.saavn(query)
XXXXXXXXifXnotXsongs.ok:
XXXXXXXXXXXXawaitXmessage.reply_text(songs.result)
XXXXXXXXXXXXreturn
XXXXXXXXsnameX=Xsongs.result[0].song
XXXXXXXXslinkX=Xsongs.result[0].media_url
XXXXXXXXssingersX=Xsongs.result[0].singers
XXXXXXXXawaitXm.edit("Downloading")
XXXXXXXXsongX=XawaitXdownload_song(slink)
XXXXXXXXawaitXm.edit("Uploading")
XXXXXXXXawaitXmessage.reply_audio(audio=song,Xtitle=sname,Xperformer=ssingers)
XXXXXXXXos.remove(song)
XXXXXXXXawaitXm.delete()
XXXXexceptXExceptionXasXe:
XXXXXXXXis_downloadingX=XFalse
XXXXXXXXawaitXm.edit(str(e))
XXXXXXXXreturn
XXXXis_downloadingX=XFalse


#XDeezerXMusic


@Client.on_message(filters.command("deezer")X&X~filters.edited)
asyncXdefXdeezsong(_,Xmessage):
XXXXglobalXis_downloading
XXXXifXlen(message.command)X<X2:
XXXXXXXXawaitXmessage.reply_text("/deezerXrequiresXanXargument.")
XXXXXXXXreturn
XXXXifXis_downloading:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"AnotherXdownloadXisXinXprogress,XtryXagainXafterXsometime."
XXXXXXXX)
XXXXXXXXreturn
XXXXifXdl_limitX>=X3:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"Ineruki'sXserverXbusyXdueXtoXtooXmanyXdownloads,XtryXagainXafterXsometime."
XXXXXXXX)
XXXXXXXXreturn
XXXXis_downloadingX=XTrue
XXXXtextX=Xmessage.text.split(None,X1)[1]
XXXXqueryX=Xtext.replace("X",X"%20")
XXXXmX=XawaitXmessage.reply_text("Searching...")
XXXXtry:
XXXXXXXXsongsX=XawaitXarq.deezer(query,X1)
XXXXXXXXifXnotXsongs.ok:
XXXXXXXXXXXXawaitXmessage.reply_text(songs.result)
XXXXXXXXXXXXreturn
XXXXXXXXtitleX=Xsongs.result[0].title
XXXXXXXXurlX=Xsongs.result[0].url
XXXXXXXXartistX=Xsongs.result[0].artist
XXXXXXXXawaitXm.edit("Downloading")
XXXXXXXXsongX=XawaitXdownload_song(url)
XXXXXXXXawaitXm.edit("Uploading")
XXXXXXXXawaitXmessage.reply_audio(audio=song,Xtitle=title,Xperformer=artist)
XXXXXXXXos.remove(song)
XXXXXXXXawaitXm.delete()
XXXXexceptXExceptionXasXe:
XXXXXXXXis_downloadingX=XFalse
XXXXXXXXawaitXm.edit(str(e))
XXXXXXXXreturn
XXXXis_downloadingX=XFalse


@Client.on_message(filters.command(["vsong",X"video"]))
asyncXdefXytmusic(client,Xmessage:XMessage):
XXXXglobalXis_downloading
XXXXifXis_downloading:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"AnotherXdownloadXisXinXprogress,XtryXagainXafterXsometime."
XXXXXXXX)
XXXXXXXXreturn
XXXXglobalXdl_limit
XXXXifXdl_limitX>=X4:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"InerukiXsXserverXbusyXdueXtoXtooXmanyXdownloads,XtryXagainXafterXsometime."
XXXXXXXX)
XXXXXXXXreturn
XXXXurlissedX=Xget_text(message)

XXXXpabloX=XawaitXclient.send_message(
XXXXXXXXmessage.chat.id,Xf"`GettingX{urlissed}XFromXYoutubeXServers.XPleaseXWait.`"
XXXX)
XXXXifXnotXurlissed:
XXXXXXXXawaitXpablo.edit("InvalidXCommandXSyntax,XPleaseXCheckXHelpXMenuXToXKnowXMore!")
XXXXXXXXreturn

XXXXsearchX=XSearchVideos(f"{urlissed}",Xoffset=1,Xmode="dict",Xmax_results=1)
XXXXtry:
XXXXXXXXmiX=Xsearch.result()
XXXXXXXXmioX=Xmi["search_result"]
XXXXXXXXmoX=Xmio[0]["link"]
XXXXXXXXthumX=Xmio[0]["title"]
XXXXXXXXfridayzX=Xmio[0]["id"]
XXXXXXXXthumsX=Xmio[0]["channel"]
XXXXXXXXkekmeX=Xf"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
XXXXexcept:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"UnknownXerrorXraisedXwhileXgettingXresultXfromXyoutube"
XXXXXXXX)
XXXXXXXXreturn
XXXXawaitXasyncio.sleep(0.6)
XXXXurlX=Xmo
XXXXsedlyfX=Xwget.download(kekme)
XXXXoptsX=X{
XXXXXXXX"format":X"best",
XXXXXXXX"addmetadata":XTrue,
XXXXXXXX"key":X"FFmpegMetadata",
XXXXXXXX"prefer_ffmpeg":XTrue,
XXXXXXXX"geo_bypass":XTrue,
XXXXXXXX"nocheckcertificate":XTrue,
XXXXXXXX"postprocessors":X[{"key":X"FFmpegVideoConvertor",X"preferedformat":X"mp4"}],
XXXXXXXX"outtmpl":X"%(id)s.mp4",
XXXXXXXX"logtostderr":XFalse,
XXXXXXXX"quiet":XTrue,
XXXX}
XXXXtry:
XXXXXXXXis_downloadingX=XTrue
XXXXXXXXwithXyoutube_dl.YoutubeDL(opts)XasXytdl:
XXXXXXXXXXXXinfooX=Xytdl.extract_info(url,XFalse)
XXXXXXXXXXXXdurationX=Xround(infoo["duration"]X/X60)

XXXXXXXXXXXXifXdurationX>X8:
XXXXXXXXXXXXXXXXawaitXpablo.edit(
XXXXXXXXXXXXXXXXXXXXf"❌XVideosXlongerXthanX8Xminute(s)XarenXtXallowed,XtheXprovidedXvideoXisX{duration}Xminute(s)"
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXis_downloadingX=XFalse
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXytdl_dataX=Xytdl.extract_info(url,Xdownload=True)

XXXXexceptXException:
XXXXXXXX#XawaitXpablo.edit(event,Xf"**FailedXToXDownload**X\n**ErrorX:**X`{str(e)}`")
XXXXXXXXis_downloadingX=XFalse
XXXXXXXXreturn

XXXXc_timeX=Xtime.time()
XXXXfile_starkX=Xf"{ytdl_data['id']}.mp4"
XXXXcapyX=Xf"**VideoXNameX➠**X`{thum}`X\n**RequestedXForX:**X`{urlissed}`X\n**ChannelX:**X`{thums}`X\n**LinkX:**X`{mo}`"
XXXXawaitXclient.send_video(
XXXXXXXXmessage.chat.id,
XXXXXXXXvideo=open(file_stark,X"rb"),
XXXXXXXXduration=int(ytdl_data["duration"]),
XXXXXXXXfile_name=str(ytdl_data["title"]),
XXXXXXXXthumb=sedlyf,
XXXXXXXXcaption=capy,
XXXXXXXXsupports_streaming=True,
XXXXXXXXprogress=progress,
XXXXXXXXprogress_args=(
XXXXXXXXXXXXpablo,
XXXXXXXXXXXXc_time,
XXXXXXXXXXXXf"`UploadingX{urlissed}XSongXFromXYouTubeXMusic!`",
XXXXXXXXXXXXfile_stark,
XXXXXXXX),
XXXX)
XXXXawaitXpablo.delete()
XXXXis_downloadingX=XFalse
XXXXforXfilesXinX(sedlyf,Xfile_stark):
XXXXXXXXifXfilesXandXos.path.exists(files):
XXXXXXXXXXXXos.remove(files)
