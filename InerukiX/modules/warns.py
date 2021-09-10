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


importXfunctools
importXre
fromXcontextlibXimportXsuppress

fromXaiogram.typesXimportXMessage
fromXaiogram.types.inline_keyboardXimportXInlineKeyboardButton,XInlineKeyboardMarkup
fromXaiogram.utils.deep_linkingXimportXget_start_link
fromXaiogram.utils.exceptionsXimportXMessageNotModified
fromXbabel.datesXimportXformat_timedelta
fromXbson.objectidXimportXObjectId

fromXInerukiXXimportXBOT_ID,Xbot
fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.mongoXimportXdb
fromXInerukiX.services.telethonXimportXtbot

fromX.miscXimportXcustomise_reason_finish,Xcustomise_reason_start
fromX.utils.connectionsXimportXchat_connection
fromX.utils.languageXimportXget_strings_dec
fromX.utils.messageXimportXInvalidTimeUnit,Xconvert_time
fromX.utils.restrictionsXimportXban_user,Xmute_user
fromX.utils.user_detailsXimportX(
XXXXget_user_and_text_dec,
XXXXget_user_dec,
XXXXget_user_link,
XXXXis_user_admin,
)


@register(cmds="warn",Xuser_can_restrict_members=True,Xbot_can_restrict_members=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_user_and_text_dec()
asyncXdefXwarn_cmd(message,Xchat,Xuser,Xtext):
XXXXawaitXwarn_func(message,Xchat,Xuser,Xtext)


@register(cmds="dwarn",Xuser_can_restrict_members=True,Xbot_can_restrict_members=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_user_and_text_dec()
asyncXdefXwarn_cmd(message,Xchat,Xuser,Xtext):
XXXXifXnotXmessage.reply_to_message:
XXXXXXXXawaitXmessage.reply(strings["reply_to_msg"])
XXXXXXXXreturn
XXXXawaitXwarn_func(message,Xchat,Xuser,Xtext)
XXXXmsgsX=X[message.message_id,Xmessage.reply_to_message.message_id]
XXXXawaitXtbot.delete_messages(message.chat.id,Xmsgs)


@get_strings_dec("warns")
asyncXdefXwarn_func(message:XMessage,Xchat,Xuser,Xtext,Xstrings,Xfilter_action=False):
XXXXchat_idX=Xchat["chat_id"]
XXXXchat_titleX=Xchat["chat_title"]
XXXXby_idX=XBOT_IDXifXfilter_actionXisXTrueXelseXmessage.from_user.id
XXXXuser_idX=Xuser["user_id"]XifXfilter_actionXisXFalseXelseXuser

XXXXifXuser_idX==XBOT_ID:
XXXXXXXXawaitXmessage.reply(strings["warn_sofi"])
XXXXXXXXreturn

XXXXifXnotXfilter_action:
XXXXXXXXifXuser_idX==Xmessage.from_user.id:
XXXXXXXXXXXXawaitXmessage.reply(strings["warn_self"])
XXXXXXXXXXXXreturn

XXXXifXawaitXis_user_admin(chat_id,Xuser_id):
XXXXXXXXifXnotXfilter_action:
XXXXXXXXXXXXawaitXmessage.reply(strings["warn_admin"])
XXXXXXXXreturn

XXXXreasonX=Xtext
XXXXwarn_idX=Xstr(
XXXXXXXX(
XXXXXXXXXXXXawaitXdb.warns.insert_one(
XXXXXXXXXXXXXXXX{
XXXXXXXXXXXXXXXXXXXX"user_id":Xuser_id,
XXXXXXXXXXXXXXXXXXXX"chat_id":Xchat_id,
XXXXXXXXXXXXXXXXXXXX"reason":Xstr(reason),
XXXXXXXXXXXXXXXXXXXX"by":Xby_id,
XXXXXXXXXXXXXXXX}
XXXXXXXXXXXX)
XXXXXXXX).inserted_id
XXXX)

XXXXadminX=XawaitXget_user_link(by_id)
XXXXmemberX=XawaitXget_user_link(user_id)
XXXXtextX=Xstrings["warn"].format(admin=admin,Xuser=member,Xchat_name=chat_title)

XXXXifXreason:
XXXXXXXXtextX+=Xstrings["warn_rsn"].format(reason=reason)

XXXXwarns_countX=XawaitXdb.warns.count_documents(
XXXXXXXX{"chat_id":Xchat_id,X"user_id":Xuser_id}
XXXX)

XXXXbuttonsX=XInlineKeyboardMarkup().add(
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXX"⚠️XRemoveXwarn",Xcallback_data="remove_warn_{}".format(warn_id)
XXXXXXXX)
XXXX)

XXXXifXawaitXdb.rules.find_one({"chat_id":Xchat_id}):
XXXXXXXXbuttons.insert(
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXX"📝XRules",Xurl=awaitXget_start_link(f"btn_rules_{chat_id}")
XXXXXXXXXXXX)
XXXXXXXX)

XXXXifXwarn_limitX:=XawaitXdb.warnlimit.find_one({"chat_id":Xchat_id}):
XXXXXXXXmax_warnX=Xint(warn_limit["num"])
XXXXelse:
XXXXXXXXmax_warnX=X3

XXXXifXfilter_action:
XXXXXXXXactionX=Xfunctools.partial(bot.send_message,Xchat_id=chat_id)
XXXXelifXmessage.reply_to_message:
XXXXXXXXactionX=Xmessage.reply_to_message.reply
XXXXelse:
XXXXXXXXactionX=Xfunctools.partial(message.reply,Xdisable_notification=True)

XXXXifXwarns_countX>=Xmax_warn:
XXXXXXXXifXawaitXmax_warn_func(chat_id,Xuser_id):
XXXXXXXXXXXXawaitXdb.warns.delete_many({"user_id":Xuser_id,X"chat_id":Xchat_id})
XXXXXXXXXXXXdataX=XawaitXdb.warnmode.find_one({"chat_id":Xchat_id})
XXXXXXXXXXXXifXdataXisXnotXNone:
XXXXXXXXXXXXXXXXifXdata["mode"]X==X"tmute":
XXXXXXXXXXXXXXXXXXXXtextX=Xstrings["max_warn_exceeded:tmute"].format(
XXXXXXXXXXXXXXXXXXXXXXXXuser=member,
XXXXXXXXXXXXXXXXXXXXXXXXtime=format_timedelta(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXconvert_time(data["time"]),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXlocale=strings["language_info"]["babel"],
XXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXtextX=Xstrings["max_warn_exceeded"].format(
XXXXXXXXXXXXXXXXXXXXXXXXuser=member,
XXXXXXXXXXXXXXXXXXXXXXXXaction=strings["banned"]
XXXXXXXXXXXXXXXXXXXXXXXXifXdata["mode"]X==X"ban"
XXXXXXXXXXXXXXXXXXXXXXXXelseXstrings["muted"],
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXreturnXawaitXaction(text=text)
XXXXXXXXXXXXreturnXawaitXaction(
XXXXXXXXXXXXXXXXtext=strings["max_warn_exceeded"].format(
XXXXXXXXXXXXXXXXXXXXuser=member,Xaction=strings["banned"]
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXX)
XXXXtextX+=Xstrings["warn_num"].format(curr_warns=warns_count,Xmax_warns=max_warn)
XXXXreturnXawaitXaction(text=text,Xreply_markup=buttons,Xdisable_web_page_preview=True)


@register(
XXXXregexp=r"remove_warn_(.*)",
XXXXf="cb",
XXXXallow_kwargs=True,
XXXXuser_can_restrict_members=True,
)
@get_strings_dec("warns")
asyncXdefXrmv_warn_btn(event,Xstrings,Xregexp=None,X**kwargs):
XXXXwarn_idX=XObjectId(re.search(r"remove_warn_(.*)",Xstr(regexp)).group(1)[:-2])
XXXXuser_idX=Xevent.from_user.id
XXXXadmin_linkX=XawaitXget_user_link(user_id)
XXXXawaitXdb.warns.delete_one({"_id":Xwarn_id})
XXXXwithXsuppress(MessageNotModified):
XXXXXXXXawaitXevent.message.edit_text(
XXXXXXXXXXXXstrings["warn_btn_rmvl_success"].format(admin=admin_link)
XXXXXXXX)


@register(cmds="warns")
@chat_connection(admin=True,Xonly_groups=True)
@get_user_dec(allow_self=True)
@get_strings_dec("warns")
asyncXdefXwarns(message,Xchat,Xuser,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXuser_idX=Xuser["user_id"]
XXXXtextX=Xstrings["warns_header"]
XXXXuser_linkX=XawaitXget_user_link(user_id)

XXXXcountX=X0
XXXXasyncXforXwarnXinXdb.warns.find({"user_id":Xuser_id,X"chat_id":Xchat_id}):
XXXXXXXXcountX+=X1
XXXXXXXXbyX=XawaitXget_user_link(warn["by"])
XXXXXXXXrsnX=Xwarn["reason"]
XXXXXXXXreasonX=Xf"<code>{rsn}</code>"
XXXXXXXXifXnotXrsnXorXrsnX==X"None":
XXXXXXXXXXXXreasonX=X"<i>NoXReason</i>"
XXXXXXXXtextX+=Xstrings["warns"].format(count=count,Xreason=reason,Xadmin=by)

XXXXifXcountX==X0:
XXXXXXXXawaitXmessage.reply(strings["no_warns"].format(user=user_link))
XXXXXXXXreturn

XXXXawaitXmessage.reply(text,Xdisable_notification=True)


@register(cmds="warnlimit",Xuser_admin=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("warns")
asyncXdefXwarnlimit(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXchat_titleX=Xchat["chat_title"]
XXXXargX=Xmessage.get_args().split()

XXXXifXnotXarg:
XXXXXXXXifXcurrent_limitX:=XawaitXdb.warnlimit.find_one({"chat_id":Xchat_id}):
XXXXXXXXXXXXnumX=Xcurrent_limit["num"]
XXXXXXXXelse:
XXXXXXXXXXXXnumX=X3XX#XDefaultXvalue
XXXXXXXXawaitXmessage.reply(strings["warn_limit"].format(chat_name=chat_title,Xnum=num))
XXXXelifXnotXarg[0].isdigit():
XXXXXXXXreturnXawaitXmessage.reply(strings["not_digit"])
XXXXelse:
XXXXXXXXifXint(arg[0])X<X2:
XXXXXXXXXXXXreturnXawaitXmessage.reply(strings["warnlimit_short"])

XXXXXXXXelifXint(arg[0])X>X10000:XX#XMaxXvalue
XXXXXXXXXXXXreturnXawaitXmessage.reply(strings["warnlimit_long"])

XXXXXXXXnewX=X{"chat_id":Xchat_id,X"num":Xint(arg[0])}

XXXXXXXXawaitXdb.warnlimit.update_one({"chat_id":Xchat_id},X{"$set":Xnew},Xupsert=True)
XXXXXXXXawaitXmessage.reply(strings["warnlimit_updated"].format(num=int(arg[0])))


@register(cmds=["resetwarns",X"delwarns"],Xuser_can_restrict_members=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_user_dec()
@get_strings_dec("warns")
asyncXdefXreset_warn(message,Xchat,Xuser,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXchat_titleX=Xchat["chat_title"]
XXXXuser_idX=Xuser["user_id"]
XXXXuser_linkX=XawaitXget_user_link(user_id)
XXXXadmin_linkX=XawaitXget_user_link(message.from_user.id)

XXXXifXuser_idX==XBOT_ID:
XXXXXXXXawaitXmessage.reply(strings["rst_wrn_sofi"])
XXXXXXXXreturn

XXXXifXawaitXdb.warns.find_one({"chat_id":Xchat_id,X"user_id":Xuser_id}):
XXXXXXXXdeletedX=XawaitXdb.warns.delete_many({"chat_id":Xchat_id,X"user_id":Xuser_id})
XXXXXXXXpurgedX=Xdeleted.deleted_count
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["purged_warns"].format(
XXXXXXXXXXXXXXXXadmin=admin_link,Xnum=purged,Xuser=user_link,Xchat_title=chat_title
XXXXXXXXXXXX)
XXXXXXXX)
XXXXelse:
XXXXXXXXawaitXmessage.reply(strings["usr_no_wrn"].format(user=user_link))


@register(
XXXXcmds=["warnmode",X"warnaction"],Xuser_admin=True,Xbot_can_restrict_members=True
)
@chat_connection(admin=True)
@get_strings_dec("warns")
asyncXdefXwarnmode(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXacceptable_argsX=X["ban",X"tmute",X"mute"]
XXXXargX=Xstr(message.get_args()).split()
XXXXnewX=X{"chat_id":Xchat_id}

XXXXifXargXandXarg[0]XinXacceptable_args:
XXXXXXXXoptionX=X"".join(arg[0])
XXXXXXXXifX(
XXXXXXXXXXXXdataX:=XawaitXdb.warnmode.find_one({"chat_id":Xchat_id})
XXXXXXXX)XisXnotXNoneXandXdata["mode"]X==Xoption:
XXXXXXXXXXXXreturnXawaitXmessage.reply(strings["same_mode"])
XXXXXXXXifXarg[0]X==Xacceptable_args[0]:
XXXXXXXXXXXXnew["mode"]X=Xoption
XXXXXXXXXXXXawaitXdb.warnmode.update_one(
XXXXXXXXXXXXXXXX{"chat_id":Xchat_id},X{"$set":Xnew},Xupsert=True
XXXXXXXXXXXX)
XXXXXXXXelifXarg[0]X==Xacceptable_args[1]:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXtimeX=Xarg[1]
XXXXXXXXXXXXexceptXIndexError:
XXXXXXXXXXXXXXXXreturnXawaitXmessage.reply(strings["no_time"])
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXXXXX#XTODO:XForXbetterXUXXweXhaveXtoXshowXuntilXtimeXofXtmuteXwhenXactionXisXdone.
XXXXXXXXXXXXXXXXXXXX#XWeXcan'tXstoreXtimedeltaXclassXinXmongodb;XHereXweXcheckXvalidityXofXgivenXtime.
XXXXXXXXXXXXXXXXXXXXconvert_time(time)
XXXXXXXXXXXXXXXXexceptX(InvalidTimeUnit,XTypeError,XValueError):
XXXXXXXXXXXXXXXXXXXXreturnXawaitXmessage.reply(strings["invalid_time"])
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXnew.update(mode=option,Xtime=time)
XXXXXXXXXXXXXXXXXXXXawaitXdb.warnmode.update_one(
XXXXXXXXXXXXXXXXXXXXXXXX{"chat_id":Xchat_id},X{"$set":Xnew},Xupsert=True
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXelifXarg[0]X==Xacceptable_args[2]:
XXXXXXXXXXXXnew["mode"]X=Xoption
XXXXXXXXXXXXawaitXdb.warnmode.update_one(
XXXXXXXXXXXXXXXX{"chat_id":Xchat_id},X{"$set":Xnew},Xupsert=True
XXXXXXXXXXXX)
XXXXXXXXawaitXmessage.reply(strings["warnmode_success"]X%X(chat["chat_title"],Xoption))
XXXXelse:
XXXXXXXXtextX=X""
XXXXXXXXifX(curr_modeX:=XawaitXdb.warnmode.find_one({"chat_id":Xchat_id}))XisXnotXNone:
XXXXXXXXXXXXmodeX=Xcurr_mode["mode"]
XXXXXXXXXXXXtextX+=Xstrings["mode_info"]X%Xmode
XXXXXXXXtextX+=Xstrings["wrng_args"]
XXXXXXXXtextX+=X"\n".join([f"-X{i}"XforXiXinXacceptable_args])
XXXXXXXXawaitXmessage.reply(text)


asyncXdefXmax_warn_func(chat_id,Xuser_id):
XXXXifX(dataX:=XawaitXdb.warnmode.find_one({"chat_id":Xchat_id}))XisXnotXNone:
XXXXXXXXifXdata["mode"]X==X"ban":
XXXXXXXXXXXXreturnXawaitXban_user(chat_id,Xuser_id)
XXXXXXXXelifXdata["mode"]X==X"tmute":
XXXXXXXXXXXXtimeX=Xconvert_time(data["time"])
XXXXXXXXXXXXreturnXawaitXmute_user(chat_id,Xuser_id,Xtime)
XXXXXXXXelifXdata["mode"]X==X"mute":
XXXXXXXXXXXXreturnXawaitXmute_user(chat_id,Xuser_id)
XXXXelse:XX#XDefault
XXXXXXXXreturnXawaitXban_user(chat_id,Xuser_id)


asyncXdefX__export__(chat_id):
XXXXifXdataX:=XawaitXdb.warnlimit.find_one({"chat_id":Xchat_id}):
XXXXXXXXnumberX=Xdata["num"]
XXXXelse:
XXXXXXXXnumberX=X3

XXXXifXwarnmode_dataX:=XawaitXdb.warnmode.find_one({"chat_id":Xchat_id}):
XXXXXXXXdelXwarnmode_data["chat_id"],Xwarnmode_data["_id"]
XXXXelse:
XXXXXXXXwarnmode_dataX=XNone

XXXXreturnX{"warns":X{"warns_limit":Xnumber,X"warn_mode":Xwarnmode_data}}


asyncXdefX__import__(chat_id,Xdata):
XXXXifX"warns_limit"XinXdata:
XXXXXXXXnumberX=Xdata["warns_limit"]
XXXXXXXXifXnumberX<X2:
XXXXXXXXXXXXreturn

XXXXXXXXelifXnumberX>X10000:XX#XMaxXvalue
XXXXXXXXXXXXreturn

XXXXXXXXawaitXdb.warnlimit.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},X{"$set":X{"num":Xnumber}},Xupsert=True
XXXXXXXX)

XXXXifX(dataX:=Xdata["warn_mode"])XisXnotXNone:
XXXXXXXXawaitXdb.warnmode.update_one({"chat_id":Xchat_id},X{"$set":Xdata},Xupsert=True)


@get_strings_dec("warns")
asyncXdefXfilter_handle(message,Xchat,Xdata,Xstring=None):
XXXXifXawaitXis_user_admin(chat["chat_id"],Xmessage.from_user.id):
XXXXXXXXreturn
XXXXtarget_userX=Xmessage.from_user.id
XXXXtextX=Xdata.get("reason",XNone)XorXstring["filter_handle_rsn"]
XXXXawaitXwarn_func(message,Xchat,Xtarget_user,Xtext,Xfilter_action=True)


__filters__X=X{
XXXX"warn_user":X{
XXXXXXXX"title":X{"module":X"warns",X"string":X"filters_title"},
XXXXXXXX"setup":X{"start":Xcustomise_reason_start,X"finish":Xcustomise_reason_finish},
XXXXXXXX"handle":Xfilter_handle,
XXXX}
}


__mod_name__X=X"Warnings"

__help__X=X"""
YouXcanXkeepXyourXmembersXfromXgettingXoutXofXcontrolXusingXthisXfeature!

<b>AvailableXcommands:</b>
<b>GeneralX(Admins):</b>
-X/warnX(?user)X(?reason):XUseXthisXcommandXtoXwarnXtheXuser!XyouXcanXmentionXorXreplyXtoXtheXoffendedXuserXandXaddXreasonXifXneeded
-X/delwarnsXorX/resetwarns:XThisXcommandXisXusedXtoXdeleteXallXtheXwarnsXuserXgotXsoXfarXinXtheXchat
-X/dwarnX[reply]:XDeleteXtheXrepliedXmessageXandXwarnXhim
<b>WarnlimtX(Admins):</b>
-X/warnlimitX(newXlimit):XSetsXaXwarnlimit
NotXallXchatsXwantXtoXgiveXsameXmaximumXwarnsXtoXtheXuser,Xright?XThisXcommandXwillXhelpXyouXtoXmodifyXdefaultXmaximumXwarns.XDefaultXisX3

TheXwarnlimitXshouldXbeXgreaterXthanX<code>1</code>XandXlessXthanX<code>10,000</code>

<b>WarnactionX(Admins):</b>
/warnactionX(mode)X(?time)
WellXagain,XnotXallXchatsXwantXtoXbanX(default)XusersXwhenXexceedXmaximumXwarnsXsoXthisXcommandXwillXableXtoXmodifyXthat.
CurrentXsupportedXactionsXareX<code>ban</code>X(defaultXone),X<code>mute</code>,X<code>tmute</code>.XTheXtmuteXmodeXrequireX<code>time</code>XargumentXasXyouXguessed.

<b>AvailableXforXallXusers:</b>
/warnsX(?user)
UseXthisXcommandXtoXknowXnumberXofXwarnsXandXinformationXaboutXwarnsXyouXgotXsoXfarXinXtheXchat.XToXuseXyourselfXyouXdoesn'tXrequireXuserXargument.
"""
