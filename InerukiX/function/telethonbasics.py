importXos

fromXtelethon.tl.typesXimportX*

fromXInerukiX.function.pluginhelpersXimportXruncmd


asyncXdefXconvert_to_image(event,Xborg):
XXXXlmaoX=XawaitXevent.get_reply_message()
XXXXifXnotX(
XXXXXXXXlmao.gif
XXXXXXXXorXlmao.audio
XXXXXXXXorXlmao.voice
XXXXXXXXorXlmao.video
XXXXXXXXorXlmao.video_note
XXXXXXXXorXlmao.photo
XXXXXXXXorXlmao.sticker
XXXXXXXXorXlmao.media
XXXX):
XXXXXXXXawaitXborg.send_message(event.chat_id,X"`FormatXNotXSupported.`")
XXXXXXXXreturn
XXXXelse:
XXXXXXXXtry:
XXXXXXXXXXXXtime.time()
XXXXXXXXXXXXdownloaded_file_nameX=XawaitXborg.download_media(
XXXXXXXXXXXXXXXXlmao.media,Xsedpath,X"`Downloading...`"
XXXXXXXXXXXX)

XXXXXXXXexceptXExceptionXasXe:XX#Xpylint:disable=C0103,W0703
XXXXXXXXXXXXawaitXborg.send_message(event.chat_id,Xstr(e))
XXXXXXXXelse:
XXXXXXXXXXXXlelX=XawaitXborg.send_message(
XXXXXXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXXXXX"DownloadedXtoX`{}`Xsuccessfully.".format(downloaded_file_name),
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXlel.delete
XXXXifXnotXos.path.exists(downloaded_file_name):
XXXXXXXXlelX=XawaitXborg.send_message(event.chat_id,X"DownloadXUnsucessfullX:(")
XXXXXXXXawaitXlel.delete
XXXXXXXXreturn
XXXXifXlmaoXandXlmao.photo:
XXXXXXXXlmao_finalX=Xdownloaded_file_name
XXXXelifXlmao.stickerXandXlmao.sticker.mime_typeX==X"application/x-tgsticker":
XXXXXXXXrpathX=Xdownloaded_file_name
XXXXXXXXimage_name20X=Xos.path.join(sedpath,X"SED.png")
XXXXXXXXcmdX=Xf"lottie_convert.pyX--frameX0X-ifXlottieX-ofXpngX{downloaded_file_name}X{image_name20}"
XXXXXXXXstdout,XstderrX=X(awaitXruncmd(cmd))[:2]
XXXXXXXXos.remove(rpath)
XXXXXXXXlmao_finalX=Ximage_name20
XXXXelifXlmao.stickerXandXlmao.sticker.mime_typeX==X"image/webp":
XXXXXXXXpathofsticker2X=Xdownloaded_file_name
XXXXXXXXimage_new_pathX=XsedpathX+X"image.png"
XXXXXXXXimX=XImage.open(pathofsticker2)
XXXXXXXXim.save(image_new_path,X"PNG")
XXXXXXXXifXnotXos.path.exists(image_new_path):
XXXXXXXXXXXXawaitXevent.reply("`Wasn'tXAbleXToXFetchXShot.`")
XXXXXXXXXXXXreturn
XXXXXXXXlmao_finalX=Ximage_new_path
XXXXelifXlmao.audio:
XXXXXXXXsed_pX=Xdownloaded_file_name
XXXXXXXXhmmyesX=XsedpathX+X"stark.mp3"
XXXXXXXXimgpathX=XsedpathX+X"starky.jpg"
XXXXXXXXos.rename(sed_p,Xhmmyes)
XXXXXXXXawaitXruncmd(f"ffmpegX-iX{hmmyes}X-filter:vXscale=500:500X-anX{imgpath}")
XXXXXXXXos.remove(sed_p)
XXXXXXXXifXnotXos.path.exists(imgpath):
XXXXXXXXXXXXawaitXevent.reply("`Wasn'tXAbleXToXFetchXShot.`")
XXXXXXXXXXXXreturn
XXXXXXXXlmao_finalX=Ximgpath
XXXXelifXlmao.gifXorXlmao.videoXorXlmao.video_note:
XXXXXXXXsed_p2X=Xdownloaded_file_name
XXXXXXXXjpg_fileX=Xos.path.join(sedpath,X"image.jpg")
XXXXXXXXawaitXtake_screen_shot(sed_p2,X0,Xjpg_file)
XXXXXXXXos.remove(sed_p2)
XXXXXXXXifXnotXos.path.exists(jpg_file):
XXXXXXXXXXXXawaitXevent.reply("`Couldn'tXFetch.XSS`")
XXXXXXXXXXXXreturn
XXXXXXXXlmao_finalX=Xjpg_file
XXXXreturnXlmao_final


asyncXdefXtake_screen_shot(
XXXXvideo_file:Xstr,Xduration:Xint,Xpath:XstrX=X""
)X->XOptional[str]:
XXXX"""takeXaXscreenshot"""
XXXXlogger.info(
XXXXXXXX"[[[ExtractingXaXframeXfromX%sX|||XVideoXdurationX=>X%s]]]",
XXXXXXXXvideo_file,
XXXXXXXXduration,
XXXX)
XXXXttlX=XdurationX//X2
XXXXthumb_image_pathX=XpathXorXos.path.join(sedpath,Xf"{basename(video_file)}.jpg")
XXXXcommandX=Xf'''ffmpegX-ssX{ttl}X-iX"{video_file}"X-vframesX1X"{thumb_image_path}"'''
XXXXerrX=X(awaitXruncmd(command))[1]
XXXXifXerr:
XXXXXXXXlogger.error(err)
XXXXreturnXthumb_image_pathXifXos.path.exists(thumb_image_path)XelseXNone


asyncXdefXget_all_admin_chats(event):
XXXXlul_starkX=X[]
XXXXall_chatsX=X[
XXXXXXXXd.entity
XXXXXXXXforXdXinXawaitXevent.client.get_dialogs()
XXXXXXXXifX(d.is_groupXorXd.is_channel)
XXXX]
XXXXtry:
XXXXXXXXforXiXinXall_chats:
XXXXXXXXXXXXifXi.creatorXorXi.admin_rights:
XXXXXXXXXXXXXXXXlul_stark.append(i.id)
XXXXexcept:
XXXXXXXXpass
XXXXreturnXlul_stark


asyncXdefXis_admin(event,Xuser):
XXXXtry:
XXXXXXXXsedX=XawaitXevent.client.get_permissions(event.chat_id,Xuser)
XXXXXXXXifXsed.is_admin:
XXXXXXXXXXXXis_modX=XTrue
XXXXXXXXelse:
XXXXXXXXXXXXis_modX=XFalse
XXXXexcept:
XXXXXXXXis_modX=XFalse
XXXXreturnXis_mod


asyncXdefXprogress(current,Xtotal,Xevent,Xstart,Xtype_of_ps,Xfile_name=None):
XXXX"""GenericXprogress_callbackXforXboth
XXXXupload.pyXandXdownload.py"""
XXXXnowX=Xtime.time()
XXXXdiffX=XnowX-Xstart
XXXXifXround(diffX%X10.00)X==X0XorXcurrentX==Xtotal:
XXXXXXXXpercentageX=XcurrentX*X100X/Xtotal
XXXXXXXXspeedX=XcurrentX/Xdiff
XXXXXXXXelapsed_timeX=Xround(diff)X*X1000
XXXXXXXXtime_to_completionX=Xround((totalX-Xcurrent)X/Xspeed)X*X1000
XXXXXXXXestimated_total_timeX=Xelapsed_timeX+Xtime_to_completion
XXXXXXXXprogress_strX=X"[{0}{1}]\nProgress:X{2}%\n".format(
XXXXXXXXXXXX"".join(["🟠"XforXiXinXrange(math.floor(percentageX/X5))]),
XXXXXXXXXXXX"".join(["🔘"XforXiXinXrange(20X-Xmath.floor(percentageX/X5))]),
XXXXXXXXXXXXround(percentage,X2),
XXXXXXXX)
XXXXXXXXtmpX=Xprogress_strX+X"{0}XofX{1}\nETA:X{2}".format(
XXXXXXXXXXXXhumanbytes(current),Xhumanbytes(total),Xtime_formatter(estimated_total_time)
XXXXXXXX)
XXXXXXXXifXfile_name:
XXXXXXXXXXXXawaitXevent.edit(
XXXXXXXXXXXXXXXX"{}\nFileXName:X`{}`\n{}".format(type_of_ps,Xfile_name,Xtmp)
XXXXXXXXXXXX)
XXXXXXXXelse:
XXXXXXXXXXXXawaitXevent.edit("{}\n{}".format(type_of_ps,Xtmp))


defXhumanbytes(size):
XXXX"""InputXsizeXinXbytes,
XXXXoutputsXinXaXhumanXreadableXformat"""
XXXX#Xhttps://stackoverflow.com/a/49361727/4723940
XXXXifXnotXsize:
XXXXXXXXreturnX""
XXXX#X2X**X10X=X1024
XXXXpowerX=X2X**X10
XXXXraised_to_powX=X0
XXXXdict_power_nX=X{0:X"",X1:X"Ki",X2:X"Mi",X3:X"Gi",X4:X"Ti"}
XXXXwhileXsizeX>Xpower:
XXXXXXXXsizeX/=Xpower
XXXXXXXXraised_to_powX+=X1
XXXXreturnXstr(round(size,X2))X+X"X"X+Xdict_power_n[raised_to_pow]X+X"B"


defXtime_formatter(milliseconds:Xint)X->Xstr:
XXXX"""InputsXtimeXinXmilliseconds,XtoXgetXbeautifiedXtime,
XXXXasXstring"""
XXXXseconds,XmillisecondsX=Xdivmod(int(milliseconds),X1000)
XXXXminutes,XsecondsX=Xdivmod(seconds,X60)
XXXXhours,XminutesX=Xdivmod(minutes,X60)
XXXXdays,XhoursX=Xdivmod(hours,X24)
XXXXtmpX=X(
XXXXXXXX((str(days)X+X"Xday(s),X")XifXdaysXelseX"")
XXXXXXXX+X((str(hours)X+X"Xhour(s),X")XifXhoursXelseX"")
XXXXXXXX+X((str(minutes)X+X"Xminute(s),X")XifXminutesXelseX"")
XXXXXXXX+X((str(seconds)X+X"Xsecond(s),X")XifXsecondsXelseX"")
XXXXXXXX+X((str(milliseconds)X+X"Xmillisecond(s),X")XifXmillisecondsXelseX"")
XXXX)
XXXXreturnXtmp[:-2]
