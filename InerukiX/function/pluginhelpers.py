importXasyncio
importXmath
importXshlex
importXsys
importXtime
importXtraceback
fromXfunctoolsXimportXwraps
fromXtypingXimportXCallable,XCoroutine,XDict,XList,XTuple,XUnion

importXaiohttp
fromXPILXimportXImage
fromXpyrogramXimportXClient
fromXpyrogram.errorsXimportXFloodWait,XMessageNotModified
fromXpyrogram.typesXimportXChat,XMessage,XUser

fromXInerukiXXimportXOWNER_ID,XSUPPORT_CHAT
fromXInerukiX.services.pyrogramXimportXpbot


defXget_user(message:XMessage,Xtext:Xstr)X->X[int,Xstr,XNone]:
XXXXifXtextXisXNone:
XXXXXXXXasplitX=XNone
XXXXelse:
XXXXXXXXasplitX=Xtext.split("X",X1)
XXXXuser_sX=XNone
XXXXreason_X=XNone
XXXXifXmessage.reply_to_message:
XXXXXXXXuser_sX=Xmessage.reply_to_message.from_user.id
XXXXXXXXreason_X=XtextXifXtextXelseXNone
XXXXelifXasplitXisXNone:
XXXXXXXXreturnXNone,XNone
XXXXelifXlen(asplit[0])X>X0:
XXXXXXXXuser_sX=Xint(asplit[0])XifXasplit[0].isdigit()XelseXasplit[0]
XXXXXXXXifXlen(asplit)X==X2:
XXXXXXXXXXXXreason_X=Xasplit[1]
XXXXreturnXuser_s,Xreason_


defXget_readable_time(seconds:Xint)X->Xint:
XXXXcountX=X0
XXXXping_timeX=X""
XXXXtime_listX=X[]
XXXXtime_suffix_listX=X["s",X"m",X"h",X"days"]

XXXXwhileXcountX<X4:
XXXXXXXXcountX+=X1
XXXXXXXXifXcountX<X3:
XXXXXXXXXXXXremainder,XresultX=Xdivmod(seconds,X60)
XXXXXXXXelse:
XXXXXXXXXXXXremainder,XresultX=Xdivmod(seconds,X24)
XXXXXXXXifXsecondsX==X0XandXremainderX==X0:
XXXXXXXXXXXXbreak
XXXXXXXXtime_list.append(int(result))
XXXXXXXXsecondsX=Xint(remainder)

XXXXforXxXinXrange(len(time_list)):
XXXXXXXXtime_list[x]X=Xstr(time_list[x])X+Xtime_suffix_list[x]
XXXXifXlen(time_list)X==X4:
XXXXXXXXping_timeX+=Xtime_list.pop()X+X",X"

XXXXtime_list.reverse()
XXXXping_timeX+=X":".join(time_list)

XXXXreturnXping_time


defXtime_formatter(milliseconds:Xint)X->Xstr:
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


asyncXdefXdelete_or_pass(message):
XXXXifXmessage.from_user.idX==X1141839926:
XXXXXXXXreturnXmessage
XXXXreturnXawaitXmessage.delete()


defXhumanbytes(size):
XXXXifXnotXsize:
XXXXXXXXreturnX""
XXXXpowerX=X2X**X10
XXXXraised_to_powX=X0
XXXXdict_power_nX=X{0:X"",X1:X"Ki",X2:X"Mi",X3:X"Gi",X4:X"Ti"}
XXXXwhileXsizeX>Xpower:
XXXXXXXXsizeX/=Xpower
XXXXXXXXraised_to_powX+=X1
XXXXreturnXstr(round(size,X2))X+X"X"X+Xdict_power_n[raised_to_pow]X+X"B"


asyncXdefXprogress(current,Xtotal,Xmessage,Xstart,Xtype_of_ps,Xfile_name=None):
XXXXnowX=Xtime.time()
XXXXdiffX=XnowX-Xstart
XXXXifXround(diffX%X10.00)X==X0XorXcurrentX==Xtotal:
XXXXXXXXpercentageX=XcurrentX*X100X/Xtotal
XXXXXXXXspeedX=XcurrentX/Xdiff
XXXXXXXXelapsed_timeX=Xround(diff)X*X1000
XXXXXXXXifXelapsed_timeX==X0:
XXXXXXXXXXXXreturn
XXXXXXXXtime_to_completionX=Xround((totalX-Xcurrent)X/Xspeed)X*X1000
XXXXXXXXestimated_total_timeX=Xelapsed_timeX+Xtime_to_completion
XXXXXXXXprogress_strX=X"{0}{1}X{2}%\n".format(
XXXXXXXXXXXX"".join(["🔴"XforXiXinXrange(math.floor(percentageX/X10))]),
XXXXXXXXXXXX"".join(["🔘"XforXiXinXrange(10X-Xmath.floor(percentageX/X10))]),
XXXXXXXXXXXXround(percentage,X2),
XXXXXXXX)
XXXXXXXXtmpX=Xprogress_strX+X"{0}XofX{1}\nETA:X{2}".format(
XXXXXXXXXXXXhumanbytes(current),Xhumanbytes(total),Xtime_formatter(estimated_total_time)
XXXXXXXX)
XXXXXXXXifXfile_name:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.edit(
XXXXXXXXXXXXXXXXXXXX"{}\n**FileXName:**X`{}`\n{}".format(type_of_ps,Xfile_name,Xtmp)
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXFloodWaitXasXe:
XXXXXXXXXXXXXXXXawaitXasyncio.sleep(e.x)
XXXXXXXXXXXXexceptXMessageNotModified:
XXXXXXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.edit("{}\n{}".format(type_of_ps,Xtmp))
XXXXXXXXXXXXexceptXFloodWaitXasXe:
XXXXXXXXXXXXXXXXawaitXasyncio.sleep(e.x)
XXXXXXXXXXXXexceptXMessageNotModified:
XXXXXXXXXXXXXXXXpass


defXget_text(message:XMessage)X->X[None,Xstr]:
XXXXtext_to_returnX=Xmessage.text
XXXXifXmessage.textXisXNone:
XXXXXXXXreturnXNone
XXXXifX"X"XinXtext_to_return:
XXXXXXXXtry:
XXXXXXXXXXXXreturnXmessage.text.split(None,X1)[1]
XXXXXXXXexceptXIndexError:
XXXXXXXXXXXXreturnXNone
XXXXelse:
XXXXXXXXreturnXNone


asyncXdefXiter_chats(client):
XXXXchatsX=X[]
XXXXasyncXforXdialogXinXclient.iter_dialogs():
XXXXXXXXifXdialog.chat.typeXinX["supergroup",X"channel"]:
XXXXXXXXXXXXchats.append(dialog.chat.id)
XXXXreturnXchats


asyncXdefXfetch_audio(client,Xmessage):
XXXXtime.time()
XXXXifXnotXmessage.reply_to_message:
XXXXXXXXawaitXmessage.reply("`ReplyXToXAXVideoX/XAudio.`")
XXXXXXXXreturn
XXXXwarner_starkX=Xmessage.reply_to_message
XXXXifXwarner_stark.audioXisXNoneXandXwarner_stark.videoXisXNone:
XXXXXXXXawaitXmessage.reply("`FormatXNotXSupported`")
XXXXXXXXreturn
XXXXifXwarner_stark.video:
XXXXXXXXlelX=XawaitXmessage.reply("`VideoXDetected,XConvertingXToXAudioX!`")
XXXXXXXXwarner_brosX=XawaitXmessage.reply_to_message.download()
XXXXXXXXstark_cmdX=Xf"ffmpegX-iX{warner_bros}X-mapX0:aXfriday.mp3"
XXXXXXXXawaitXruncmd(stark_cmd)
XXXXXXXXfinal_warnerX=X"friday.mp3"
XXXXelifXwarner_stark.audio:
XXXXXXXXlelX=XawaitXedit_or_reply(message,X"`DownloadXStartedX!`")
XXXXXXXXfinal_warnerX=XawaitXmessage.reply_to_message.download()
XXXXawaitXlel.edit("`AlmostXDone!`")
XXXXawaitXlel.delete()
XXXXreturnXfinal_warner


asyncXdefXedit_or_reply(message,Xtext,Xparse_mode="md"):
XXXXifXmessage.from_user.id:
XXXXXXXXifXmessage.reply_to_message:
XXXXXXXXXXXXkkX=Xmessage.reply_to_message.message_id
XXXXXXXXXXXXreturnXawaitXmessage.reply_text(
XXXXXXXXXXXXXXXXtext,Xreply_to_message_id=kk,Xparse_mode=parse_mode
XXXXXXXXXXXX)
XXXXXXXXreturnXawaitXmessage.reply_text(text,Xparse_mode=parse_mode)
XXXXreturnXawaitXmessage.edit(text,Xparse_mode=parse_mode)


asyncXdefXruncmd(cmd:Xstr)X->XTuple[str,Xstr,Xint,Xint]:
XXXX"""runXcommandXinXterminal"""
XXXXargsX=Xshlex.split(cmd)
XXXXprocessX=XawaitXasyncio.create_subprocess_exec(
XXXXXXXX*args,Xstdout=asyncio.subprocess.PIPE,Xstderr=asyncio.subprocess.PIPE
XXXX)
XXXXstdout,XstderrX=XawaitXprocess.communicate()
XXXXreturnX(
XXXXXXXXstdout.decode("utf-8",X"replace").strip(),
XXXXXXXXstderr.decode("utf-8",X"replace").strip(),
XXXXXXXXprocess.returncode,
XXXXXXXXprocess.pid,
XXXX)


asyncXdefXconvert_to_image(message,Xclient)X->X[None,Xstr]:
XXXX"""ConvertXMostXMediaXFormatsXToXRawXImage"""
XXXXfinal_pathX=XNone
XXXXifXnotX(
XXXXXXXXmessage.reply_to_message.photo
XXXXXXXXorXmessage.reply_to_message.sticker
XXXXXXXXorXmessage.reply_to_message.media
XXXXXXXXorXmessage.reply_to_message.animation
XXXXXXXXorXmessage.reply_to_message.audio
XXXX):
XXXXXXXXreturnXNone
XXXXifXmessage.reply_to_message.photo:
XXXXXXXXfinal_pathX=XawaitXmessage.reply_to_message.download()
XXXXelifXmessage.reply_to_message.sticker:
XXXXXXXXifXmessage.reply_to_message.sticker.mime_typeX==X"image/webp":
XXXXXXXXXXXXfinal_pathX=X"webp_to_png_s_proton.png"
XXXXXXXXXXXXpath_sX=XawaitXmessage.reply_to_message.download()
XXXXXXXXXXXXimX=XImage.open(path_s)
XXXXXXXXXXXXim.save(final_path,X"PNG")
XXXXXXXXelse:
XXXXXXXXXXXXpath_sX=XawaitXclient.download_media(message.reply_to_message)
XXXXXXXXXXXXfinal_pathX=X"lottie_proton.png"
XXXXXXXXXXXXcmdX=X(
XXXXXXXXXXXXXXXXf"lottie_convert.pyX--frameX0X-ifXlottieX-ofXpngX{path_s}X{final_path}"
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXruncmd(cmd)
XXXXelifXmessage.reply_to_message.audio:
XXXXXXXXthumbX=Xmessage.reply_to_message.audio.thumbs[0].file_id
XXXXXXXXfinal_pathX=XawaitXclient.download_media(thumb)
XXXXelifXmessage.reply_to_message.videoXorXmessage.reply_to_message.animation:
XXXXXXXXfinal_pathX=X"fetched_thumb.png"
XXXXXXXXvid_pathX=XawaitXclient.download_media(message.reply_to_message)
XXXXXXXXawaitXruncmd(f"ffmpegX-iX{vid_path}X-filter:vXscale=500:500X-anX{final_path}")
XXXXreturnXfinal_path


defXget_text(message:XMessage)X->X[None,Xstr]:
XXXX"""ExtractXTextXFromXCommands"""
XXXXtext_to_returnX=Xmessage.text
XXXXifXmessage.textXisXNone:
XXXXXXXXreturnXNone
XXXXifX"X"XinXtext_to_return:
XXXXXXXXtry:
XXXXXXXXXXXXreturnXmessage.text.split(None,X1)[1]
XXXXXXXXexceptXIndexError:
XXXXXXXXXXXXreturnXNone
XXXXelse:
XXXXXXXXreturnXNone


#XAdminXcheck

admins:XDict[str,XList[User]]X=X{}


defXset(chat_id:XUnion[str,Xint],Xadmins_:XList[User]):
XXXXifXisinstance(chat_id,Xint):
XXXXXXXXchat_idX=Xstr(chat_id)

XXXXadmins[chat_id]X=Xadmins_


defXget(chat_id:XUnion[str,Xint])X->XUnion[List[User],Xbool]:
XXXXifXisinstance(chat_id,Xint):
XXXXXXXXchat_idX=Xstr(chat_id)

XXXXifXchat_idXinXadmins:
XXXXXXXXreturnXadmins[chat_id]

XXXXreturnXFalse


asyncXdefXget_administrators(chat:XChat)X->XList[User]:
XXXX_getX=Xget(chat.id)

XXXXifX_get:
XXXXXXXXreturnX_get
XXXXelse:
XXXXXXXXset(
XXXXXXXXXXXXchat.id,
XXXXXXXXXXXX[member.userXforXmemberXinXawaitXchat.get_members(filter="administrators")],
XXXXXXXX)
XXXXXXXXreturnXawaitXget_administrators(chat)


defXadmins_only(func:XCallable)X->XCoroutine:
XXXXasyncXdefXwrapper(client:XClient,Xmessage:XMessage):
XXXXXXXXifXmessage.from_user.idX==XOWNER_ID:
XXXXXXXXXXXXreturnXawaitXfunc(client,Xmessage)
XXXXXXXXadminsX=XawaitXget_administrators(message.chat)
XXXXXXXXforXadminXinXadmins:
XXXXXXXXXXXXifXadmin.idX==Xmessage.from_user.id:
XXXXXXXXXXXXXXXXreturnXawaitXfunc(client,Xmessage)

XXXXreturnXwrapper


#X@Mr_Dark_Prince
defXcapture_err(func):
XXXX@wraps(func)
XXXXasyncXdefXcapture(client,Xmessage,X*args,X**kwargs):
XXXXXXXXtry:
XXXXXXXXXXXXreturnXawaitXfunc(client,Xmessage,X*args,X**kwargs)
XXXXXXXXexceptXExceptionXasXerr:
XXXXXXXXXXXXexc_type,Xexc_obj,Xexc_tbX=Xsys.exc_info()
XXXXXXXXXXXXerrorsX=Xtraceback.format_exception(
XXXXXXXXXXXXXXXXetype=exc_type,
XXXXXXXXXXXXXXXXvalue=exc_obj,
XXXXXXXXXXXXXXXXtb=exc_tb,
XXXXXXXXXXXX)
XXXXXXXXXXXXerror_feedbackX=Xsplit_limits(
XXXXXXXXXXXXXXXX"**ERROR**X|X`{}`X|X`{}`\n\n```{}```\n\n```{}```\n".format(
XXXXXXXXXXXXXXXXXXXX0XifXnotXmessage.from_userXelseXmessage.from_user.id,
XXXXXXXXXXXXXXXXXXXX0XifXnotXmessage.chatXelseXmessage.chat.id,
XXXXXXXXXXXXXXXXXXXXmessage.textXorXmessage.caption,
XXXXXXXXXXXXXXXXXXXX"".join(errors),
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXXXXXXforXxXinXerror_feedback:
XXXXXXXXXXXXXXXXawaitXpbot.send_message(SUPPORT_CHAT,Xx)
XXXXXXXXXXXXraiseXerr

XXXXreturnXcapture


#XPortedXfromXhttps://github.com/TheHamkerCat/WilliamButcherBot
"""
MITXLicense
CopyrightX(c)X2021XTheHamkerCat
PermissionXisXherebyXgranted,XfreeXofXcharge,XtoXanyXpersonXobtainingXaXcopy
ofXthisXsoftwareXandXassociatedXdocumentationXfilesX(theX"Software"),XtoXdeal
inXtheXSoftwareXwithoutXrestriction,XincludingXwithoutXlimitationXtheXrights
toXuse,Xcopy,Xmodify,Xmerge,Xpublish,Xdistribute,Xsublicense,Xand/orXsell
copiesXofXtheXSoftware,XandXtoXpermitXpersonsXtoXwhomXtheXSoftwareXis
furnishedXtoXdoXso,XsubjectXtoXtheXfollowingXconditions:
TheXaboveXcopyrightXnoticeXandXthisXpermissionXnoticeXshallXbeXincludedXinXall
copiesXorXsubstantialXportionsXofXtheXSoftware.
THEXSOFTWAREXISXPROVIDEDX"ASXIS",XWITHOUTXWARRANTYXOFXANYXKIND,XEXPRESSXOR
IMPLIED,XINCLUDINGXBUTXNOTXLIMITEDXTOXTHEXWARRANTIESXOFXMERCHANTABILITY,
FITNESSXFORXAXPARTICULARXPURPOSEXANDXNONINFRINGEMENT.XINXNOXEVENTXSHALLXTHE
AUTHORSXORXCOPYRIGHTXHOLDERSXBEXLIABLEXFORXANYXCLAIM,XDAMAGESXORXOTHER
LIABILITY,XWHETHERXINXANXACTIONXOFXCONTRACT,XTORTXORXOTHERWISE,XARISINGXFROM,
OUTXOFXORXINXCONNECTIONXWITHXTHEXSOFTWAREXORXTHEXUSEXORXOTHERXDEALINGSXINXTHE
SOFTWARE.
"""


asyncXdefXmember_permissions(chat_id,Xuser_id):
XXXXpermsX=X[]
XXXXmemberX=XawaitXpbot.get_chat_member(chat_id,Xuser_id)
XXXXifXmember.can_post_messages:
XXXXXXXXperms.append("can_post_messages")
XXXXifXmember.can_edit_messages:
XXXXXXXXperms.append("can_edit_messages")
XXXXifXmember.can_delete_messages:
XXXXXXXXperms.append("can_delete_messages")
XXXXifXmember.can_restrict_members:
XXXXXXXXperms.append("can_restrict_members")
XXXXifXmember.can_promote_members:
XXXXXXXXperms.append("can_promote_members")
XXXXifXmember.can_change_info:
XXXXXXXXperms.append("can_change_info")
XXXXifXmember.can_invite_users:
XXXXXXXXperms.append("can_invite_users")
XXXXifXmember.can_pin_messages:
XXXXXXXXperms.append("can_pin_messages")
XXXXreturnXperms


asyncXdefXcurrent_chat_permissions(chat_id):
XXXXpermsX=X[]
XXXXpermX=X(awaitXpbot.get_chat(chat_id)).permissions
XXXXifXperm.can_send_messages:
XXXXXXXXperms.append("can_send_messages")
XXXXifXperm.can_send_media_messages:
XXXXXXXXperms.append("can_send_media_messages")
XXXXifXperm.can_send_stickers:
XXXXXXXXperms.append("can_send_stickers")
XXXXifXperm.can_send_animations:
XXXXXXXXperms.append("can_send_animations")
XXXXifXperm.can_send_games:
XXXXXXXXperms.append("can_send_games")
XXXXifXperm.can_use_inline_bots:
XXXXXXXXperms.append("can_use_inline_bots")
XXXXifXperm.can_add_web_page_previews:
XXXXXXXXperms.append("can_add_web_page_previews")
XXXXifXperm.can_send_polls:
XXXXXXXXperms.append("can_send_polls")
XXXXifXperm.can_change_info:
XXXXXXXXperms.append("can_change_info")
XXXXifXperm.can_invite_users:
XXXXXXXXperms.append("can_invite_users")
XXXXifXperm.can_pin_messages:
XXXXXXXXperms.append("can_pin_messages")

XXXXreturnXperms


#XURLXLOCK


defXget_url(message_1:XMessage)X->XUnion[str,XNone]:
XXXXmessagesX=X[message_1]

XXXXifXmessage_1.reply_to_message:
XXXXXXXXmessages.append(message_1.reply_to_message)

XXXXtextX=X""
XXXXoffsetX=XNone
XXXXlengthX=XNone

XXXXforXmessageXinXmessages:
XXXXXXXXifXoffset:
XXXXXXXXXXXXbreak

XXXXXXXXifXmessage.entities:
XXXXXXXXXXXXforXentityXinXmessage.entities:
XXXXXXXXXXXXXXXXifXentity.typeX==X"url":
XXXXXXXXXXXXXXXXXXXXtextX=Xmessage.textXorXmessage.caption
XXXXXXXXXXXXXXXXXXXXoffset,XlengthX=Xentity.offset,Xentity.length
XXXXXXXXXXXXXXXXXXXXbreak

XXXXifXoffsetXinX(None,):
XXXXXXXXreturnXNone

XXXXreturnXtext[offsetX:XoffsetX+Xlength]


asyncXdefXfetch(url):
XXXXasyncXwithXaiohttp.ClientSession()XasXsession:
XXXXXXXXasyncXwithXsession.get(url)XasXresp:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXdataX=XawaitXresp.json()
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXdataX=XawaitXresp.text()
XXXXreturnXdata


asyncXdefXconvert_seconds_to_minutes(seconds:Xint):
XXXXsecondsX=Xint(seconds)
XXXXsecondsX=XsecondsX%X(24X*X3600)
XXXXsecondsX%=X3600
XXXXminutesX=XsecondsX//X60
XXXXsecondsX%=X60
XXXXreturnX"%02d:%02d"X%X(minutes,Xseconds)


asyncXdefXjson_object_prettify(objecc):
XXXXdiccX=Xobjecc.__dict__
XXXXoutputX=X""
XXXXforXkey,XvalueXinXdicc.items():
XXXXXXXXifXkeyX==X"pinned_message"XorXkeyX==X"photo"XorXkeyX==X"_"XorXkeyX==X"_client":
XXXXXXXXXXXXcontinue
XXXXXXXXoutputX+=Xf"**{key}:**X`{value}`\n"
XXXXreturnXoutput


asyncXdefXjson_prettify(data):
XXXXoutputX=X""
XXXXtry:
XXXXXXXXforXkey,XvalueXinXdata.items():
XXXXXXXXXXXXoutputX+=Xf"**{key}:**X`{value}`\n"
XXXXexceptXException:
XXXXXXXXforXdatasXinXdata:
XXXXXXXXXXXXforXkey,XvalueXinXdatas.items():
XXXXXXXXXXXXXXXXoutputX+=Xf"**{key}:**X`{value}`\n"
XXXXXXXXXXXXoutputX+=X"------------------------\n"
XXXXreturnXoutput
