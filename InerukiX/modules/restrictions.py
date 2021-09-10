#XCopyrightX(C)X2018X-X2020XMrYacha.XAllXrightsXreserved.XSourceXcodeXavailableXunderXtheXAGPL.
#XCopyrightX(C)X2021Xerrorshivansh
#XCopyrightX(C)X2020XInukaXAsith

#XThisXfileXisXpartXofXInerukiX(TelegramXBot)

#XThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXas
#XpublishedXbyXtheXFreeXSoftwareXFoundation,XeitherXversionX3XofXthe
#XLicense,XorX(atXyourXoption)XanyXlaterXversion.

#XThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.

#XYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XalongXwithXthisXprogram.XXIfXnot,XseeX<http://www.gnu.org/licenses/>.

importXasyncio
importXdatetimeXX#Xnoqa:XF401
fromXcontextlibXimportXsuppress

fromXaiogram.utils.exceptionsXimportXMessageNotModified
fromXbabel.datesXimportXformat_timedelta

fromXInerukiXXimportXBOT_ID,Xbot
fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.redisXimportXredis
fromXInerukiX.services.telethonXimportXtbot

fromX.miscXimportXcustomise_reason_finish,Xcustomise_reason_start
fromX.utils.connectionsXimportXchat_connection
fromX.utils.languageXimportXget_strings_dec
fromX.utils.messageXimportXInvalidTimeUnit,Xconvert_time,Xget_cmd
fromX.utils.restrictionsXimportXban_user,Xkick_user,Xmute_user,Xunban_user,Xunmute_user
fromX.utils.user_detailsXimportX(
XXXXget_user_and_text_dec,
XXXXget_user_dec,
XXXXget_user_link,
XXXXis_user_admin,
)


@register(
XXXXcmds=["kick",X"skick"],
XXXXbot_can_restrict_members=True,
XXXXuser_can_restrict_members=True,
)
@chat_connection(admin=True,Xonly_groups=True)
@get_user_and_text_dec()
@get_strings_dec("restrictions")
asyncXdefXkick_user_cmd(message,Xchat,Xuser,Xargs,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXuser_idX=Xuser["user_id"]

XXXXifXuser_idX==XBOT_ID:
XXXXXXXXawaitXmessage.reply(strings["kick_InerukiX"])
XXXXXXXXreturn

XXXXelifXuser_idX==Xmessage.from_user.id:
XXXXXXXXawaitXmessage.reply(strings["kick_self"])
XXXXXXXXreturn

XXXXelifXawaitXis_user_admin(chat_id,Xuser_id):
XXXXXXXXawaitXmessage.reply(strings["kick_admin"])
XXXXXXXXreturn

XXXXtextX=Xstrings["user_kicked"].format(
XXXXXXXXuser=awaitXget_user_link(user_id),
XXXXXXXXadmin=awaitXget_user_link(message.from_user.id),
XXXXXXXXchat_name=chat["chat_title"],
XXXX)

XXXX#XAddXreason
XXXXifXargs:
XXXXXXXXtextX+=Xstrings["reason"]X%Xargs

XXXX#XCheckXifXsilent
XXXXsilentX=XFalse
XXXXifXget_cmd(message)X==X"skick":
XXXXXXXXsilentX=XTrue
XXXXXXXXkeyX=X"leave_silent:"X+Xstr(chat_id)
XXXXXXXXredis.set(key,Xuser_id)
XXXXXXXXredis.expire(key,X30)
XXXXXXXXtextX+=Xstrings["purge"]

XXXXawaitXkick_user(chat_id,Xuser_id)

XXXXmsgX=XawaitXmessage.reply(text)

XXXX#XDelXmsgsXifXsilent
XXXXifXsilent:
XXXXXXXXto_delX=X[msg.message_id,Xmessage.message_id]
XXXXXXXXifX(
XXXXXXXXXXXX"reply_to_message"XinXmessage
XXXXXXXXXXXXandXmessage.reply_to_message.from_user.idX==Xuser_id
XXXXXXXX):
XXXXXXXXXXXXto_del.append(message.reply_to_message.message_id)
XXXXXXXXawaitXasyncio.sleep(5)
XXXXXXXXawaitXtbot.delete_messages(chat_id,Xto_del)


@register(
XXXXcmds=["mute",X"smute",X"tmute",X"stmute"],
XXXXbot_can_restrict_members=True,
XXXXuser_can_restrict_members=True,
)
@chat_connection(admin=True,Xonly_groups=True)
@get_user_and_text_dec()
@get_strings_dec("restrictions")
asyncXdefXmute_user_cmd(message,Xchat,Xuser,Xargs,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXuser_idX=Xuser["user_id"]

XXXXifXuser_idX==XBOT_ID:
XXXXXXXXawaitXmessage.reply(strings["mute_InerukiX"])
XXXXXXXXreturn

XXXXelifXuser_idX==Xmessage.from_user.id:
XXXXXXXXawaitXmessage.reply(strings["mute_self"])
XXXXXXXXreturn

XXXXelifXawaitXis_user_admin(chat_id,Xuser_id):
XXXXXXXXawaitXmessage.reply(strings["mute_admin"])
XXXXXXXXreturn

XXXXtextX=Xstrings["user_muted"].format(
XXXXXXXXuser=awaitXget_user_link(user_id),
XXXXXXXXadmin=awaitXget_user_link(message.from_user.id),
XXXXXXXXchat_name=chat["chat_title"],
XXXX)

XXXXcurr_cmdX=Xget_cmd(message)

XXXX#XCheckXifXtemprotary
XXXXuntil_dateX=XNone
XXXXifXcurr_cmdXinX("tmute",X"stmute"):
XXXXXXXXifXargsXisXnotXNoneXandXlen(argsX:=Xargs.split())X>X0:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXuntil_dateX=Xconvert_time(args[0])
XXXXXXXXXXXXexceptX(InvalidTimeUnit,XTypeError,XValueError):
XXXXXXXXXXXXXXXXawaitXmessage.reply(strings["invalid_time"])
XXXXXXXXXXXXXXXXreturn

XXXXXXXXXXXXtextX+=Xstrings["on_time"]X%Xformat_timedelta(
XXXXXXXXXXXXXXXXuntil_date,Xlocale=strings["language_info"]["babel"]
XXXXXXXXXXXX)

XXXXXXXXXXXX#XAddXreason
XXXXXXXXXXXXifXlen(args)X>X1:
XXXXXXXXXXXXXXXXtextX+=Xstrings["reason"]X%X"X".join(args[1:])
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply(strings["enter_time"])
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXX#XAddXreason
XXXXXXXXifXargsXisXnotXNoneXandXlen(argsX:=Xargs.split())X>X0:
XXXXXXXXXXXXtextX+=Xstrings["reason"]X%X"X".join(args[0:])

XXXX#XCheckXifXsilent
XXXXsilentX=XFalse
XXXXifXcurr_cmdXinX("smute",X"stmute"):
XXXXXXXXsilentX=XTrue
XXXXXXXXkeyX=X"leave_silent:"X+Xstr(chat_id)
XXXXXXXXredis.set(key,Xuser_id)
XXXXXXXXredis.expire(key,X30)
XXXXXXXXtextX+=Xstrings["purge"]

XXXXawaitXmute_user(chat_id,Xuser_id,Xuntil_date=until_date)

XXXXmsgX=XawaitXmessage.reply(text)

XXXX#XDelXmsgsXifXsilent
XXXXifXsilent:
XXXXXXXXto_delX=X[msg.message_id,Xmessage.message_id]
XXXXXXXXifX(
XXXXXXXXXXXX"reply_to_message"XinXmessage
XXXXXXXXXXXXandXmessage.reply_to_message.from_user.idX==Xuser_id
XXXXXXXX):
XXXXXXXXXXXXto_del.append(message.reply_to_message.message_id)
XXXXXXXXawaitXasyncio.sleep(5)
XXXXXXXXawaitXtbot.delete_messages(chat_id,Xto_del)


@register(cmds="unmute",Xbot_can_restrict_members=True,Xuser_can_restrict_members=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_user_dec()
@get_strings_dec("restrictions")
asyncXdefXunmute_user_cmd(message,Xchat,Xuser,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXuser_idX=Xuser["user_id"]

XXXXifXuser_idX==XBOT_ID:
XXXXXXXXawaitXmessage.reply(strings["unmute_InerukiX"])
XXXXXXXXreturn

XXXXelifXuser_idX==Xmessage.from_user.id:
XXXXXXXXawaitXmessage.reply(strings["unmute_self"])
XXXXXXXXreturn

XXXXelifXawaitXis_user_admin(chat_id,Xuser_id):
XXXXXXXXawaitXmessage.reply(strings["unmute_admin"])
XXXXXXXXreturn

XXXXawaitXunmute_user(chat_id,Xuser_id)

XXXXtextX=Xstrings["user_unmuted"].format(
XXXXXXXXuser=awaitXget_user_link(user_id),
XXXXXXXXadmin=awaitXget_user_link(message.from_user.id),
XXXXXXXXchat_name=chat["chat_title"],
XXXX)

XXXXawaitXmessage.reply(text)


@register(
XXXXcmds=["ban",X"sban",X"tban",X"stban"],
XXXXbot_can_restrict_members=True,
XXXXuser_can_restrict_members=True,
)
@chat_connection(admin=True,Xonly_groups=True)
@get_user_and_text_dec()
@get_strings_dec("restrictions")
asyncXdefXban_user_cmd(message,Xchat,Xuser,Xargs,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXuser_idX=Xuser["user_id"]

XXXXifXuser_idX==XBOT_ID:
XXXXXXXXawaitXmessage.reply(strings["ban_InerukiX"])
XXXXXXXXreturn

XXXXelifXuser_idX==Xmessage.from_user.id:
XXXXXXXXawaitXmessage.reply(strings["ban_self"])
XXXXXXXXreturn

XXXXelifXawaitXis_user_admin(chat_id,Xuser_id):
XXXXXXXXawaitXmessage.reply(strings["ban_admin"])
XXXXXXXXreturn

XXXXtextX=Xstrings["user_banned"].format(
XXXXXXXXuser=awaitXget_user_link(user_id),
XXXXXXXXadmin=awaitXget_user_link(message.from_user.id),
XXXXXXXXchat_name=chat["chat_title"],
XXXX)

XXXXcurr_cmdX=Xget_cmd(message)

XXXX#XCheckXifXtemprotary
XXXXuntil_dateX=XNone
XXXXifXcurr_cmdXinX("tban",X"stban"):
XXXXXXXXifXargsXisXnotXNoneXandXlen(argsX:=Xargs.split())X>X0:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXuntil_dateX=Xconvert_time(args[0])
XXXXXXXXXXXXexceptX(InvalidTimeUnit,XTypeError,XValueError):
XXXXXXXXXXXXXXXXawaitXmessage.reply(strings["invalid_time"])
XXXXXXXXXXXXXXXXreturn

XXXXXXXXXXXXtextX+=Xstrings["on_time"]X%Xformat_timedelta(
XXXXXXXXXXXXXXXXuntil_date,Xlocale=strings["language_info"]["babel"]
XXXXXXXXXXXX)

XXXXXXXXXXXX#XAddXreason
XXXXXXXXXXXXifXlen(args)X>X1:
XXXXXXXXXXXXXXXXtextX+=Xstrings["reason"]X%X"X".join(args[1:])
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply(strings["enter_time"])
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXX#XAddXreason
XXXXXXXXifXargsXisXnotXNoneXandXlen(argsX:=Xargs.split())X>X0:
XXXXXXXXXXXXtextX+=Xstrings["reason"]X%X"X".join(args[0:])

XXXX#XCheckXifXsilent
XXXXsilentX=XFalse
XXXXifXcurr_cmdXinX("sban",X"stban"):
XXXXXXXXsilentX=XTrue
XXXXXXXXkeyX=X"leave_silent:"X+Xstr(chat_id)
XXXXXXXXredis.set(key,Xuser_id)
XXXXXXXXredis.expire(key,X30)
XXXXXXXXtextX+=Xstrings["purge"]

XXXXawaitXban_user(chat_id,Xuser_id,Xuntil_date=until_date)

XXXXmsgX=XawaitXmessage.reply(text)

XXXX#XDelXmsgsXifXsilent
XXXXifXsilent:
XXXXXXXXto_delX=X[msg.message_id,Xmessage.message_id]
XXXXXXXXifX(
XXXXXXXXXXXX"reply_to_message"XinXmessage
XXXXXXXXXXXXandXmessage.reply_to_message.from_user.idX==Xuser_id
XXXXXXXX):
XXXXXXXXXXXXto_del.append(message.reply_to_message.message_id)
XXXXXXXXawaitXasyncio.sleep(5)
XXXXXXXXawaitXtbot.delete_messages(chat_id,Xto_del)


@register(cmds="unban",Xbot_can_restrict_members=True,Xuser_can_restrict_members=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_user_dec()
@get_strings_dec("restrictions")
asyncXdefXunban_user_cmd(message,Xchat,Xuser,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXuser_idX=Xuser["user_id"]

XXXXifXuser_idX==XBOT_ID:
XXXXXXXXawaitXmessage.reply(strings["unban_InerukiX"])
XXXXXXXXreturn

XXXXelifXuser_idX==Xmessage.from_user.id:
XXXXXXXXawaitXmessage.reply(strings["unban_self"])
XXXXXXXXreturn

XXXXelifXawaitXis_user_admin(chat_id,Xuser_id):
XXXXXXXXawaitXmessage.reply(strings["unban_admin"])
XXXXXXXXreturn

XXXXawaitXunban_user(chat_id,Xuser_id)

XXXXtextX=Xstrings["user_unband"].format(
XXXXXXXXuser=awaitXget_user_link(user_id),
XXXXXXXXadmin=awaitXget_user_link(message.from_user.id),
XXXXXXXXchat_name=chat["chat_title"],
XXXX)

XXXXawaitXmessage.reply(text)


@register(f="leave")
asyncXdefXleave_silent(message):
XXXXifXnotXmessage.from_user.idX==XBOT_ID:
XXXXXXXXreturn

XXXXifXredis.get("leave_silent:"X+Xstr(message.chat.id))X==Xmessage.left_chat_member.id:
XXXXXXXXawaitXmessage.delete()


@get_strings_dec("restrictions")
asyncXdefXfilter_handle_ban(message,Xchat,Xdata:Xdict,Xstrings=None):
XXXXifXawaitXis_user_admin(chat["chat_id"],Xmessage.from_user.id):
XXXXXXXXreturn
XXXXifXawaitXban_user(chat["chat_id"],Xmessage.from_user.id):
XXXXXXXXreasonX=Xdata.get("reason",XNone)XorXstrings["filter_action_rsn"]
XXXXXXXXtextX=Xstrings["filtr_ban_success"]X%X(
XXXXXXXXXXXXawaitXget_user_link(BOT_ID),
XXXXXXXXXXXXawaitXget_user_link(message.from_user.id),
XXXXXXXXXXXXreason,
XXXXXXXX)
XXXXXXXXawaitXbot.send_message(chat["chat_id"],Xtext)


@get_strings_dec("restrictions")
asyncXdefXfilter_handle_mute(message,Xchat,Xdata,Xstrings=None):
XXXXifXawaitXis_user_admin(chat["chat_id"],Xmessage.from_user.id):
XXXXXXXXreturn
XXXXifXawaitXmute_user(chat["chat_id"],Xmessage.from_user.id):
XXXXXXXXreasonX=Xdata.get("reason",XNone)XorXstrings["filter_action_rsn"]
XXXXXXXXtextX=Xstrings["filtr_mute_success"]X%X(
XXXXXXXXXXXXawaitXget_user_link(BOT_ID),
XXXXXXXXXXXXawaitXget_user_link(message.from_user.id),
XXXXXXXXXXXXreason,
XXXXXXXX)
XXXXXXXXawaitXbot.send_message(chat["chat_id"],Xtext)


@get_strings_dec("restrictions")
asyncXdefXfilter_handle_tmute(message,Xchat,Xdata,Xstrings=None):
XXXXifXawaitXis_user_admin(chat["chat_id"],Xmessage.from_user.id):
XXXXXXXXreturn
XXXXifXawaitXmute_user(
XXXXXXXXchat["chat_id"],Xmessage.from_user.id,Xuntil_date=eval(data["time"])
XXXX):
XXXXXXXXreasonX=Xdata.get("reason",XNone)XorXstrings["filter_action_rsn"]
XXXXXXXXtimeX=Xformat_timedelta(
XXXXXXXXXXXXeval(data["time"]),Xlocale=strings["language_info"]["babel"]
XXXXXXXX)
XXXXXXXXtextX=Xstrings["filtr_tmute_success"]X%X(
XXXXXXXXXXXXawaitXget_user_link(BOT_ID),
XXXXXXXXXXXXawaitXget_user_link(message.from_user.id),
XXXXXXXXXXXXtime,
XXXXXXXXXXXXreason,
XXXXXXXX)
XXXXXXXXawaitXbot.send_message(chat["chat_id"],Xtext)


@get_strings_dec("restrictions")
asyncXdefXfilter_handle_tban(message,Xchat,Xdata,Xstrings=None):
XXXXifXawaitXis_user_admin(chat["chat_id"],Xmessage.from_user.id):
XXXXXXXXreturn
XXXXifXawaitXban_user(
XXXXXXXXchat["chat_id"],Xmessage.from_user.id,Xuntil_date=eval(data["time"])
XXXX):
XXXXXXXXreasonX=Xdata.get("reason",XNone)XorXstrings["filter_action_rsn"]
XXXXXXXXtimeX=Xformat_timedelta(
XXXXXXXXXXXXeval(data["time"]),Xlocale=strings["language_info"]["babel"]
XXXXXXXX)
XXXXXXXXtextX=Xstrings["filtr_tban_success"]X%X(
XXXXXXXXXXXXawaitXget_user_link(BOT_ID),
XXXXXXXXXXXXawaitXget_user_link(message.from_user.id),
XXXXXXXXXXXXtime,
XXXXXXXXXXXXreason,
XXXXXXXX)
XXXXXXXXawaitXbot.send_message(chat["chat_id"],Xtext)


@get_strings_dec("restrictions")
asyncXdefXtime_setup_start(message,Xstrings):
XXXXwithXsuppress(MessageNotModified):
XXXXXXXXawaitXmessage.edit_text(strings["time_setup_start"])


@get_strings_dec("restrictions")
asyncXdefXtime_setup_finish(message,Xdata,Xstrings):
XXXXtry:
XXXXXXXXtimeX=Xconvert_time(message.text)
XXXXexceptX(InvalidTimeUnit,XTypeError,XValueError):
XXXXXXXXawaitXmessage.reply(strings["invalid_time"])
XXXXXXXXreturnXNone
XXXXelse:
XXXXXXXXreturnX{"time":Xrepr(time)}


@get_strings_dec("restrictions")
asyncXdefXfilter_handle_kick(message,Xchat,Xdata,Xstrings=None):
XXXXifXawaitXis_user_admin(chat["chat_id"],Xmessage.from_user.id):
XXXXXXXXreturn
XXXXifXawaitXkick_user(chat["chat_id"],Xmessage.from_user.id):
XXXXXXXXawaitXbot.send_message(
XXXXXXXXXXXXchat["chat_id"],
XXXXXXXXXXXXstrings["user_kicked"].format(
XXXXXXXXXXXXXXXXuser=awaitXget_user_link(message.from_user.id),
XXXXXXXXXXXXXXXXadmin=awaitXget_user_link(BOT_ID),
XXXXXXXXXXXXXXXXchat_name=chat["chat_title"],
XXXXXXXXXXXX),
XXXXXXXX)


__filters__X=X{
XXXX"ban_user":X{
XXXXXXXX"title":X{"module":X"restrictions",X"string":X"filter_title_ban"},
XXXXXXXX"setup":X{"start":Xcustomise_reason_start,X"finish":Xcustomise_reason_finish},
XXXXXXXX"handle":Xfilter_handle_ban,
XXXX},
XXXX"mute_user":X{
XXXXXXXX"title":X{"module":X"restrictions",X"string":X"filter_title_mute"},
XXXXXXXX"setup":X{"start":Xcustomise_reason_start,X"finish":Xcustomise_reason_finish},
XXXXXXXX"handle":Xfilter_handle_mute,
XXXX},
XXXX"tmute_user":X{
XXXXXXXX"title":X{"module":X"restrictions",X"string":X"filter_title_tmute"},
XXXXXXXX"handle":Xfilter_handle_tmute,
XXXXXXXX"setup":X[
XXXXXXXXXXXX{"start":Xtime_setup_start,X"finish":Xtime_setup_finish},
XXXXXXXXXXXX{"start":Xcustomise_reason_start,X"finish":Xcustomise_reason_finish},
XXXXXXXX],
XXXX},
XXXX"tban_user":X{
XXXXXXXX"title":X{"module":X"restrictions",X"string":X"filter_title_tban"},
XXXXXXXX"handle":Xfilter_handle_tban,
XXXXXXXX"setup":X[
XXXXXXXXXXXX{"start":Xtime_setup_start,X"finish":Xtime_setup_finish},
XXXXXXXXXXXX{"start":Xcustomise_reason_start,X"finish":Xcustomise_reason_finish},
XXXXXXXX],
XXXX},
XXXX"kick_user":X{
XXXXXXXX"title":X{"module":X"restrictions",X"string":X"filter_title_kick"},
XXXXXXXX"handle":Xfilter_handle_kick,
XXXX},
}


__mod_name__X=X"Restrictions"

__help__X=X"""
GeneralXadmin'sXrightsXisXrestrictXusersXandXcontrolXtheirXrulesXwithXthisXmoduleXyouXcanXeaselyXdoXit.

<b>AvailableXcommands:</b>
<b>Kicks:</b>
-X/kick:XKicksXaXuser
-X/skick:XSilentlyXkicks

<b>Mutes:</b>
-X/mute:XMutesXaXuser
-X/smute:XSilentlyXmutes
-X/tmuteX(time):XTemprotaryXmuteXaXuser
-X/stmuteX(time):XSilentlyXtemprotaryXmuteXaXuser
-X/unmute:XUnmutesXtheXuser

<b>Bans:</b>
-X/ban:XBansXaXuser
-X/sban:XSilentlyXbans
-X/tbanX(time):XTemprotaryXbanXaXuser
-/stbanX(time):XSilentlyXtemprotaryXbanXaXuser
-X/unban:XUnbansXtheXuser

<b>Examples:</b>
<code>-XMuteXaXuserXforXtwoXhours.
->X/tmuteX@usernameX2h</code>


"""
