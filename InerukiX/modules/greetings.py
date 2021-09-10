#XCopyrightX(C)X2018X-X2020XMrYacha.XAllXrightsXreserved.XSourceXcodeXavailableXunderXtheXAGPL.
#XCopyrightX(C)X2021Xerrorshivansh

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

importXio
importXrandom
importXre
fromXcontextlibXimportXsuppress
fromXdatetimeXimportXdatetime
fromXtypingXimportXOptional,XUnion

fromXaiogram.dispatcher.filters.builtinXimportXCommandStart
fromXaiogram.dispatcher.filters.stateXimportXState,XStatesGroup
fromXaiogram.typesXimportXCallbackQuery,XContentType,XMessage
fromXaiogram.types.inline_keyboardXimportXInlineKeyboardButton,XInlineKeyboardMarkup
fromXaiogram.types.input_mediaXimportXInputMediaPhoto
fromXaiogram.utils.callback_dataXimportXCallbackData
fromXaiogram.utils.exceptionsXimportX(
XXXXBadRequest,
XXXXChatAdminRequired,
XXXXMessageCantBeDeleted,
XXXXMessageToDeleteNotFound,
)
fromXapscheduler.jobstores.baseXimportXJobLookupError
fromXbabel.datesXimportXformat_timedelta
fromXcaptcha.imageXimportXImageCaptcha
fromXtelethon.tl.customXimportXButton

fromXInerukiXXimportXBOT_ID,XBOT_USERNAME,Xbot,Xdp
fromXInerukiX.configXimportXget_str_key
fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.apschedullerXimportXscheduler
fromXInerukiX.services.mongoXimportXdb
fromXInerukiX.services.redisXimportXredis
fromXInerukiX.services.telethonXimportXtbot
fromXInerukiX.stuff.fontsXimportXALL_FONTS

fromX..utils.cachedXimportXcached
fromX.utils.connectionsXimportXchat_connection
fromX.utils.languageXimportXget_strings_dec
fromX.utils.messageXimportXconvert_time,Xneed_args_dec
fromX.utils.notesXimportXget_parsed_note_list,Xsend_note,Xt_unparse_note_item
fromX.utils.restrictionsXimportXkick_user,Xmute_user,Xrestrict_user,Xunmute_user
fromX.utils.user_detailsXimportXcheck_admin_rights,Xget_user_link,Xis_user_admin


classXWelcomeSecurityState(StatesGroup):
XXXXbuttonX=XState()
XXXXcaptchaX=XState()
XXXXmathX=XState()


@register(cmds="welcome")
@chat_connection(only_groups=True)
@get_strings_dec("greetings")
asyncXdefXwelcome(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXsend_idX=Xmessage.chat.id

XXXXifXlen(argsX:=Xmessage.get_args().split())X>X0:
XXXXXXXXno_formatX=XTrueXifX"no_format"X==Xargs[0]XorX"raw"X==Xargs[0]XelseXFalse
XXXXelse:
XXXXXXXXno_formatX=XNone

XXXXifXnotX(db_itemX:=XawaitXget_greetings_data(chat_id)):
XXXXXXXXdb_itemX=X{}
XXXXifX"note"XnotXinXdb_item:
XXXXXXXXdb_item["note"]X=X{"text":Xstrings["default_welcome"]}

XXXXifXno_format:
XXXXXXXXawaitXmessage.reply(strings["raw_wlcm_note"])
XXXXXXXXtext,XkwargsX=XawaitXt_unparse_note_item(
XXXXXXXXXXXXmessage,Xdb_item["note"],Xchat_id,Xnoformat=True
XXXXXXXX)
XXXXXXXXawaitXsend_note(send_id,Xtext,X**kwargs)
XXXXXXXXreturn

XXXXtextX=Xstrings["welcome_info"]

XXXXtextX=Xtext.format(
XXXXXXXXchat_name=chat["chat_title"],
XXXXXXXXwelcomes_status=strings["disabled"]
XXXXXXXXifX"welcome_disabled"XinXdb_itemXandXdb_item["welcome_disabled"]XisXTrue
XXXXXXXXelseXstrings["enabled"],
XXXXXXXXwlcm_security=strings["disabled"]
XXXXXXXXifX"welcome_security"XnotXinXdb_item
XXXXXXXXorXdb_item["welcome_security"]["enabled"]XisXFalse
XXXXXXXXelseXstrings["wlcm_security_enabled"].format(
XXXXXXXXXXXXlevel=db_item["welcome_security"]["level"]
XXXXXXXX),
XXXXXXXXwlcm_mutes=strings["disabled"]
XXXXXXXXifX"welcome_mute"XnotXinXdb_itemXorXdb_item["welcome_mute"]["enabled"]XisXFalse
XXXXXXXXelseXstrings["wlcm_mutes_enabled"].format(time=db_item["welcome_mute"]["time"]),
XXXXXXXXclean_welcomes=strings["enabled"]
XXXXXXXXifX"clean_welcome"XinXdb_itemXandXdb_item["clean_welcome"]["enabled"]XisXTrue
XXXXXXXXelseXstrings["disabled"],
XXXXXXXXclean_service=strings["enabled"]
XXXXXXXXifX"clean_service"XinXdb_itemXandXdb_item["clean_service"]["enabled"]XisXTrue
XXXXXXXXelseXstrings["disabled"],
XXXX)
XXXXifX"welcome_disabled"XnotXinXdb_item:
XXXXXXXXtextX+=Xstrings["wlcm_note"]
XXXXXXXXawaitXmessage.reply(text)
XXXXXXXXtext,XkwargsX=XawaitXt_unparse_note_item(message,Xdb_item["note"],Xchat_id)
XXXXXXXXawaitXsend_note(send_id,Xtext,X**kwargs)
XXXXelse:
XXXXXXXXawaitXmessage.reply(text)

XXXXifX"welcome_security"XinXdb_item:
XXXXXXXXifX"security_note"XnotXinXdb_item:
XXXXXXXXXXXXdb_item["security_note"]X=X{"text":Xstrings["default_security_note"]}
XXXXXXXXawaitXmessage.reply(strings["security_note"])
XXXXXXXXtext,XkwargsX=XawaitXt_unparse_note_item(
XXXXXXXXXXXXmessage,Xdb_item["security_note"],Xchat_id
XXXXXXXX)
XXXXXXXXawaitXsend_note(send_id,Xtext,X**kwargs)


@register(cmds=["setwelcome",X"savewelcome"],Xuser_admin=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("greetings")
asyncXdefXset_welcome(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]

XXXXifXlen(argsX:=Xmessage.get_args().lower().split())X<X1:
XXXXXXXXdb_itemX=XawaitXget_greetings_data(chat_id)

XXXXXXXXifX(
XXXXXXXXXXXXdb_item
XXXXXXXXXXXXandX"welcome_disabled"XinXdb_item
XXXXXXXXXXXXandXdb_item["welcome_disabled"]XisXTrue
XXXXXXXX):
XXXXXXXXXXXXstatusX=Xstrings["disabled"]
XXXXXXXXelse:
XXXXXXXXXXXXstatusX=Xstrings["enabled"]

XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["turnwelcome_status"].format(
XXXXXXXXXXXXXXXXstatus=status,Xchat_name=chat["chat_title"]
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturn

XXXXnoX=X["no",X"off",X"0",X"false",X"disable"]

XXXXifXargs[0]XinXno:
XXXXXXXXawaitXdb.greetings.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},
XXXXXXXXXXXX{"$set":X{"chat_id":Xchat_id,X"welcome_disabled":XTrue}},
XXXXXXXXXXXXupsert=True,
XXXXXXXX)
XXXXXXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXXXXXawaitXmessage.reply(strings["turnwelcome_disabled"]X%Xchat["chat_title"])
XXXXXXXXreturn
XXXXelse:
XXXXXXXXnoteX=XawaitXget_parsed_note_list(message,Xsplit_args=-1)

XXXXXXXXifX(
XXXXXXXXXXXXawaitXdb.greetings.update_one(
XXXXXXXXXXXXXXXX{"chat_id":Xchat_id},
XXXXXXXXXXXXXXXX{
XXXXXXXXXXXXXXXXXXXX"$set":X{"chat_id":Xchat_id,X"note":Xnote},
XXXXXXXXXXXXXXXXXXXX"$unset":X{"welcome_disabled":X1},
XXXXXXXXXXXXXXXX},
XXXXXXXXXXXXXXXXupsert=True,
XXXXXXXXXXXX)
XXXXXXXX).modified_countX>X0:
XXXXXXXXXXXXtextX=Xstrings["updated"]
XXXXXXXXelse:
XXXXXXXXXXXXtextX=Xstrings["saved"]

XXXXXXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXXXXXawaitXmessage.reply(textX%Xchat["chat_title"])


@register(cmds="resetwelcome",Xuser_admin=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("greetings")
asyncXdefXreset_welcome(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]

XXXXifX(awaitXdb.greetings.delete_one({"chat_id":Xchat_id})).deleted_countX<X1:
XXXXXXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXXXXXawaitXmessage.reply(strings["not_found"])
XXXXXXXXreturn

XXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXawaitXmessage.reply(strings["deleted"].format(chat=chat["chat_title"]))


@register(cmds="cleanwelcome",Xuser_admin=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("greetings")
asyncXdefXclean_welcome(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]

XXXXifXlen(argsX:=Xmessage.get_args().lower().split())X<X1:
XXXXXXXXdb_itemX=XawaitXget_greetings_data(chat_id)

XXXXXXXXifX(
XXXXXXXXXXXXdb_item
XXXXXXXXXXXXandX"clean_welcome"XinXdb_item
XXXXXXXXXXXXandXdb_item["clean_welcome"]["enabled"]XisXTrue
XXXXXXXX):
XXXXXXXXXXXXstatusX=Xstrings["enabled"]
XXXXXXXXelse:
XXXXXXXXXXXXstatusX=Xstrings["disabled"]

XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["cleanwelcome_status"].format(
XXXXXXXXXXXXXXXXstatus=status,Xchat_name=chat["chat_title"]
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturn

XXXXyesX=X["yes",X"on",X"1",X"true",X"enable"]
XXXXnoX=X["no",X"off",X"0",X"false",X"disable"]

XXXXifXargs[0]XinXyes:
XXXXXXXXawaitXdb.greetings.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},
XXXXXXXXXXXX{"$set":X{"chat_id":Xchat_id,X"clean_welcome":X{"enabled":XTrue}}},
XXXXXXXXXXXXupsert=True,
XXXXXXXX)
XXXXXXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXXXXXawaitXmessage.reply(strings["cleanwelcome_enabled"]X%Xchat["chat_title"])
XXXXelifXargs[0]XinXno:
XXXXXXXXawaitXdb.greetings.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},X{"$unset":X{"clean_welcome":X1}},Xupsert=True
XXXXXXXX)
XXXXXXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXXXXXawaitXmessage.reply(strings["cleanwelcome_disabled"]X%Xchat["chat_title"])
XXXXelse:
XXXXXXXXawaitXmessage.reply(strings["bool_invalid_arg"])


@register(cmds="cleanservice",Xuser_admin=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("greetings")
asyncXdefXclean_service(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]

XXXXifXlen(argsX:=Xmessage.get_args().lower().split())X<X1:
XXXXXXXXdb_itemX=XawaitXget_greetings_data(chat_id)

XXXXXXXXifX(
XXXXXXXXXXXXdb_item
XXXXXXXXXXXXandX"clean_service"XinXdb_item
XXXXXXXXXXXXandXdb_item["clean_service"]["enabled"]XisXTrue
XXXXXXXX):
XXXXXXXXXXXXstatusX=Xstrings["enabled"]
XXXXXXXXelse:
XXXXXXXXXXXXstatusX=Xstrings["disabled"]

XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["cleanservice_status"].format(
XXXXXXXXXXXXXXXXstatus=status,Xchat_name=chat["chat_title"]
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturn

XXXXyesX=X["yes",X"on",X"1",X"true",X"enable"]
XXXXnoX=X["no",X"off",X"0",X"false",X"disable"]

XXXXifXargs[0]XinXyes:
XXXXXXXXawaitXdb.greetings.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},
XXXXXXXXXXXX{"$set":X{"chat_id":Xchat_id,X"clean_service":X{"enabled":XTrue}}},
XXXXXXXXXXXXupsert=True,
XXXXXXXX)
XXXXXXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXXXXXawaitXmessage.reply(strings["cleanservice_enabled"]X%Xchat["chat_title"])
XXXXelifXargs[0]XinXno:
XXXXXXXXawaitXdb.greetings.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},X{"$unset":X{"clean_service":X1}},Xupsert=True
XXXXXXXX)
XXXXXXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXXXXXawaitXmessage.reply(strings["cleanservice_disabled"]X%Xchat["chat_title"])
XXXXelse:
XXXXXXXXawaitXmessage.reply(strings["bool_invalid_arg"])


@register(cmds="welcomemute",Xuser_admin=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("greetings")
asyncXdefXwelcome_mute(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]

XXXXifXlen(argsX:=Xmessage.get_args().lower().split())X<X1:
XXXXXXXXdb_itemX=XawaitXget_greetings_data(chat_id)

XXXXXXXXifX(
XXXXXXXXXXXXdb_item
XXXXXXXXXXXXandX"welcome_mute"XinXdb_item
XXXXXXXXXXXXandXdb_item["welcome_mute"]["enabled"]XisXTrue
XXXXXXXX):
XXXXXXXXXXXXstatusX=Xstrings["enabled"]
XXXXXXXXelse:
XXXXXXXXXXXXstatusX=Xstrings["disabled"]

XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["welcomemute_status"].format(
XXXXXXXXXXXXXXXXstatus=status,Xchat_name=chat["chat_title"]
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturn

XXXXnoX=X["no",X"off",X"0",X"false",X"disable"]

XXXXifXargs[0].endswith(("m",X"h",X"d")):
XXXXXXXXawaitXdb.greetings.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},
XXXXXXXXXXXX{
XXXXXXXXXXXXXXXX"$set":X{
XXXXXXXXXXXXXXXXXXXX"chat_id":Xchat_id,
XXXXXXXXXXXXXXXXXXXX"welcome_mute":X{"enabled":XTrue,X"time":Xargs[0]},
XXXXXXXXXXXXXXXX}
XXXXXXXXXXXX},
XXXXXXXXXXXXupsert=True,
XXXXXXXX)
XXXXXXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXXXXXtextX=Xstrings["welcomemute_enabled"]X%Xchat["chat_title"]
XXXXXXXXtry:
XXXXXXXXXXXXawaitXmessage.reply(text)
XXXXXXXXexceptXBadRequest:
XXXXXXXXXXXXawaitXmessage.answer(text)
XXXXelifXargs[0]XinXno:
XXXXXXXXtextX=Xstrings["welcomemute_disabled"]X%Xchat["chat_title"]
XXXXXXXXawaitXdb.greetings.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},X{"$unset":X{"welcome_mute":X1}},Xupsert=True
XXXXXXXX)
XXXXXXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXXXXXtry:
XXXXXXXXXXXXawaitXmessage.reply(text)
XXXXXXXXexceptXBadRequest:
XXXXXXXXXXXXawaitXmessage.answer(text)
XXXXelse:
XXXXXXXXtextX=Xstrings["welcomemute_invalid_arg"]
XXXXXXXXtry:
XXXXXXXXXXXXawaitXmessage.reply(text)
XXXXXXXXexceptXBadRequest:
XXXXXXXXXXXXawaitXmessage.answer(text)


#XWelcomeXSecurity

wlcm_sec_config_procX=XCallbackData("wlcm_sec_proc",X"chat_id",X"user_id",X"level")
wlcm_sec_config_cancelX=XCallbackData("wlcm_sec_cancel",X"user_id",X"level")


classXWelcomeSecurityConf(StatesGroup):
XXXXsend_timeX=XState()


@register(cmds="welcomesecurity",Xuser_admin=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("greetings")
asyncXdefXwelcome_security(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]

XXXXifXlen(argsX:=Xmessage.get_args().lower().split())X<X1:
XXXXXXXXdb_itemX=XawaitXget_greetings_data(chat_id)

XXXXXXXXifX(
XXXXXXXXXXXXdb_item
XXXXXXXXXXXXandX"welcome_security"XinXdb_item
XXXXXXXXXXXXandXdb_item["welcome_security"]["enabled"]XisXTrue
XXXXXXXX):
XXXXXXXXXXXXstatusX=Xstrings["welcomesecurity_enabled_word"].format(
XXXXXXXXXXXXXXXXlevel=db_item["welcome_security"]["level"]
XXXXXXXXXXXX)
XXXXXXXXelse:
XXXXXXXXXXXXstatusX=Xstrings["disabled"]

XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["welcomesecurity_status"].format(
XXXXXXXXXXXXXXXXstatus=status,Xchat_name=chat["chat_title"]
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturn

XXXXnoX=X["no",X"off",X"0",X"false",X"disable"]

XXXXifXargs[0].lower()XinX["button",X"math",X"captcha"]:
XXXXXXXXlevelX=Xargs[0].lower()
XXXXelifXargs[0]XinXno:
XXXXXXXXawaitXdb.greetings.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},X{"$unset":X{"welcome_security":X1}},Xupsert=True
XXXXXXXX)
XXXXXXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXXXXXawaitXmessage.reply(strings["welcomesecurity_disabled"]X%Xchat["chat_title"])
XXXXXXXXreturn
XXXXelse:
XXXXXXXXawaitXmessage.reply(strings["welcomesecurity_invalid_arg"])
XXXXXXXXreturn

XXXXawaitXdb.greetings.update_one(
XXXXXXXX{"chat_id":Xchat_id},
XXXXXXXX{
XXXXXXXXXXXX"$set":X{
XXXXXXXXXXXXXXXX"chat_id":Xchat_id,
XXXXXXXXXXXXXXXX"welcome_security":X{"enabled":XTrue,X"level":Xlevel},
XXXXXXXXXXXX}
XXXXXXXX},
XXXXXXXXupsert=True,
XXXX)
XXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXbuttonsX=XInlineKeyboardMarkup()
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXstrings["no_btn"],
XXXXXXXXXXXXcallback_data=wlcm_sec_config_cancel.new(
XXXXXXXXXXXXXXXXuser_id=message.from_user.id,Xlevel=level
XXXXXXXXXXXX),
XXXXXXXX),
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXstrings["yes_btn"],
XXXXXXXXXXXXcallback_data=wlcm_sec_config_proc.new(
XXXXXXXXXXXXXXXXchat_id=chat_id,Xuser_id=message.from_user.id,Xlevel=level
XXXXXXXXXXXX),
XXXXXXXX),
XXXX)
XXXXawaitXmessage.reply(
XXXXXXXXstrings["ask_for_time_customization"].format(
XXXXXXXXXXXXtime=format_timedelta(
XXXXXXXXXXXXXXXXconvert_time(get_str_key("JOIN_CONFIRM_DURATION")),
XXXXXXXXXXXXXXXXlocale=strings["language_info"]["babel"],
XXXXXXXXXXXX)
XXXXXXXX),
XXXXXXXXreply_markup=buttons,
XXXX)


@register(wlcm_sec_config_cancel.filter(),Xf="cb",Xallow_kwargs=True)
@chat_connection(admin=True)
@get_strings_dec("greetings")
asyncXdefXwelcome_security_config_cancel(
XXXXevent:XCallbackQuery,Xchat:Xdict,Xstrings:Xdict,Xcallback_data:Xdict,X**_
):
XXXXifXint(callback_data["user_id"])X==Xevent.from_user.idXandXis_user_admin(
XXXXXXXXchat["chat_id"],Xevent.from_user.id
XXXX):
XXXXXXXXawaitXevent.message.edit_text(
XXXXXXXXXXXXtext=strings["welcomesecurity_enabled"].format(
XXXXXXXXXXXXXXXXchat_name=chat["chat_title"],Xlevel=callback_data["level"]
XXXXXXXXXXXX)
XXXXXXXX)


@register(wlcm_sec_config_proc.filter(),Xf="cb",Xallow_kwargs=True)
@chat_connection(admin=True)
@get_strings_dec("greetings")
asyncXdefXwelcome_security_config_proc(
XXXXevent:XCallbackQuery,Xchat:Xdict,Xstrings:Xdict,Xcallback_data:Xdict,X**_
):
XXXXifXint(callback_data["user_id"])X!=Xevent.from_user.idXandXis_user_admin(
XXXXXXXXchat["chat_id"],Xevent.from_user.id
XXXX):
XXXXXXXXreturn

XXXXawaitXWelcomeSecurityConf.send_time.set()
XXXXasyncXwithXdp.get_current().current_state().proxy()XasXdata:
XXXXXXXXdata["level"]X=Xcallback_data["level"]
XXXXawaitXevent.message.edit_text(strings["send_time"])


@register(
XXXXstate=WelcomeSecurityConf.send_time,
XXXXcontent_types=ContentType.TEXT,
XXXXallow_kwargs=True,
)
@chat_connection(admin=True)
@get_strings_dec("greetings")
asyncXdefXwlcm_sec_time_state(message:XMessage,Xchat:Xdict,Xstrings:Xdict,Xstate,X**_):
XXXXasyncXwithXstate.proxy()XasXdata:
XXXXXXXXlevelX=Xdata["level"]
XXXXtry:
XXXXXXXXcon_timeX=Xconvert_time(message.text)
XXXXexceptX(ValueError,XTypeError):
XXXXXXXXawaitXmessage.reply(strings["invalid_time"])
XXXXelse:
XXXXXXXXawaitXdb.greetings.update_one(
XXXXXXXXXXXX{"chat_id":Xchat["chat_id"]},
XXXXXXXXXXXX{"$set":X{"welcome_security.expire":Xmessage.text}},
XXXXXXXX)
XXXXXXXXawaitXget_greetings_data.reset_cache(chat["chat_id"])
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["welcomesecurity_enabled:customized_time"].format(
XXXXXXXXXXXXXXXXchat_name=chat["chat_title"],
XXXXXXXXXXXXXXXXlevel=level,
XXXXXXXXXXXXXXXXtime=format_timedelta(
XXXXXXXXXXXXXXXXXXXXcon_time,Xlocale=strings["language_info"]["babel"]
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXfinally:
XXXXXXXXawaitXstate.finish()


@register(cmds=["setsecuritynote",X"sevesecuritynote"],Xuser_admin=True)
@need_args_dec()
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("greetings")
asyncXdefXset_security_note(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]

XXXXifXmessage.get_args().lower().split()[0]XinX["raw",X"noformat"]:
XXXXXXXXdb_itemX=XawaitXget_greetings_data(chat_id)
XXXXXXXXifX"security_note"XnotXinXdb_item:
XXXXXXXXXXXXdb_itemX=X{"security_note":X{}}
XXXXXXXXXXXXdb_item["security_note"]["text"]X=Xstrings["default_security_note"]
XXXXXXXXXXXXdb_item["security_note"]["parse_mode"]X=X"md"

XXXXXXXXtext,XkwargsX=XawaitXt_unparse_note_item(
XXXXXXXXXXXXmessage,Xdb_item["security_note"],Xchat_id,Xnoformat=True
XXXXXXXX)
XXXXXXXXkwargs["reply_to"]X=Xmessage.message_id

XXXXXXXXawaitXsend_note(chat_id,Xtext,X**kwargs)
XXXXXXXXreturn

XXXXnoteX=XawaitXget_parsed_note_list(message,Xsplit_args=-1)

XXXXifX(
XXXXXXXXawaitXdb.greetings.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},
XXXXXXXXXXXX{"$set":X{"chat_id":Xchat_id,X"security_note":Xnote}},
XXXXXXXXXXXXupsert=True,
XXXXXXXX)
XXXX).modified_countX>X0:
XXXXXXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXXXXXtextX=Xstrings["security_note_updated"]
XXXXelse:
XXXXXXXXtextX=Xstrings["security_note_saved"]

XXXXawaitXmessage.reply(textX%Xchat["chat_title"])


@register(cmds="delsecuritynote",Xuser_admin=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("greetings")
asyncXdefXreset_security_note(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]

XXXXifX(
XXXXXXXXawaitXdb.greetings.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},X{"$unset":X{"security_note":X1}},Xupsert=True
XXXXXXXX)
XXXX).modified_countX>X0:
XXXXXXXXawaitXget_greetings_data.reset_cache(chat_id)
XXXXXXXXtextX=Xstrings["security_note_updated"]
XXXXelse:
XXXXXXXXtextX=Xstrings["del_security_note_ok"]

XXXXawaitXmessage.reply(textX%Xchat["chat_title"])


@register(only_groups=True,Xf="welcome")
@get_strings_dec("greetings")
asyncXdefXwelcome_security_handler(message:XMessage,Xstrings):
XXXXifXlen(message.new_chat_members)X>X1:
XXXXXXXX#XFIXME:XAllMightRobotXdoesntXsupportXaddingXmultipleXusersXcurrently
XXXXXXXXreturn

XXXXnew_userX=Xmessage.new_chat_members[0]
XXXXchat_idX=Xmessage.chat.id
XXXXuser_idX=Xnew_user.id

XXXXifXuser_idX==XBOT_ID:
XXXXXXXXreturn

XXXXdb_itemX=XawaitXget_greetings_data(message.chat.id)
XXXXifXnotXdb_itemXorX"welcome_security"XnotXinXdb_item:
XXXXXXXXreturn

XXXXifXnotXawaitXcheck_admin_rights(message,Xchat_id,XBOT_ID,X["can_restrict_members"]):
XXXXXXXXawaitXmessage.reply(strings["not_admin_ws"])
XXXXXXXXreturn

XXXXuserX=XawaitXmessage.chat.get_member(user_id)
XXXX#XCheckXifXuserXwasXmutedXbefore
XXXXifXuser["status"]X==X"restricted":
XXXXXXXXifXuser["can_send_messages"]XisXFalse:
XXXXXXXXXXXXreturn

XXXX#XCheckXonXOPsXandXchatXowner
XXXXifXawaitXis_user_admin(chat_id,Xuser_id):
XXXXXXXXreturn

XXXX#XcheckXifXuserXaddedXisXaXbot
XXXXifXnew_user.is_botXandXawaitXis_user_admin(chat_id,Xmessage.from_user.id):
XXXXXXXXreturn

XXXXifX"security_note"XnotXinXdb_item:
XXXXXXXXdb_item["security_note"]X=X{}
XXXXXXXXdb_item["security_note"]["text"]X=Xstrings["default_security_note"]
XXXXXXXXdb_item["security_note"]["parse_mode"]X=X"md"

XXXXtext,XkwargsX=XawaitXt_unparse_note_item(message,Xdb_item["security_note"],Xchat_id)

XXXXkwargs["reply_to"]X=X(
XXXXXXXXNone
XXXXXXXXifX"clean_service"XinXdb_itemXandXdb_item["clean_service"]["enabled"]XisXTrue
XXXXXXXXelseXmessage.message_id
XXXX)

XXXXkwargs["buttons"]X=X[]XifXnotXkwargs["buttons"]XelseXkwargs["buttons"]
XXXXkwargs["buttons"]X+=X[
XXXXXXXXButton.inline(strings["click_here"],Xf"ws_{chat_id}_{user_id}")
XXXX]

XXXX#XFIXME:XBetterXworkaround
XXXXifXnotX(msgX:=XawaitXsend_note(chat_id,Xtext,X**kwargs)):
XXXXXXXX#XWasn'tXableXtoXsentXmessage
XXXXXXXXreturn

XXXX#XMuteXuser
XXXXtry:
XXXXXXXXawaitXmute_user(chat_id,Xuser_id)
XXXXexceptXBadRequestXasXerror:
XXXXXXXX#XTODO:XDeleteXtheX"sent"XmessageX^
XXXXXXXXreturnXawaitXmessage.reply(f"welcomeXsecurityXfailedXdueXtoX{error.args[0]}")

XXXXredis.set(f"welcome_security_users:{user_id}:{chat_id}",Xmsg.id)

XXXXifXraw_timeX:=Xdb_item["welcome_security"].get("expire",XNone):
XXXXXXXXtimeX=Xconvert_time(raw_time)
XXXXelse:
XXXXXXXXtimeX=Xconvert_time(get_str_key("JOIN_CONFIRM_DURATION"))

XXXXscheduler.add_job(
XXXXXXXXjoin_expired,
XXXXXXXX"date",
XXXXXXXXid=f"wc_expire:{chat_id}:{user_id}",
XXXXXXXXrun_date=datetime.utcnow()X+Xtime,
XXXXXXXXkwargs={
XXXXXXXXXXXX"chat_id":Xchat_id,
XXXXXXXXXXXX"user_id":Xuser_id,
XXXXXXXXXXXX"message_id":Xmsg.id,
XXXXXXXXXXXX"wlkm_msg_id":Xmessage.message_id,
XXXXXXXX},
XXXXXXXXreplace_existing=True,
XXXX)


asyncXdefXjoin_expired(chat_id,Xuser_id,Xmessage_id,Xwlkm_msg_id):
XXXXuserX=XawaitXbot.get_chat_member(chat_id,Xuser_id)
XXXXifXuser.statusX!=X"restricted":
XXXXXXXXreturn

XXXXbot_userX=XawaitXbot.get_chat_member(chat_id,XBOT_ID)
XXXXifX(
XXXXXXXX"can_restrict_members"XnotXinXbot_user
XXXXXXXXorXbot_user["can_restrict_members"]XisXFalse
XXXX):
XXXXXXXXreturn

XXXXkeyX=X"leave_silent:"X+Xstr(chat_id)
XXXXredis.set(key,Xuser_id)

XXXXawaitXunmute_user(chat_id,Xuser_id)
XXXXawaitXkick_user(chat_id,Xuser_id)
XXXXawaitXtbot.delete_messages(chat_id,X[message_id,Xwlkm_msg_id])


@register(regexp=re.compile(r"ws_"),Xf="cb")
@get_strings_dec("greetings")
asyncXdefXws_redirecter(message,Xstrings):
XXXXpayloadX=Xmessage.data.split("_")[1:]
XXXXchat_idX=Xint(payload[0])
XXXXreal_user_idX=Xint(payload[1])
XXXXcalled_user_idX=Xmessage.from_user.id

XXXXurlX=Xf"https://t.me/{BOT_USERNAME}?start=ws_{chat_id}_{called_user_id}_{message.message.message_id}"
XXXXifXnotXcalled_user_idX==Xreal_user_id:
XXXXXXXX#XTheXpersonsXwhichXareXmutedXbeforeXwontXhaveXtheirXsignaturesXregisteredXonXcache
XXXXXXXXifXnotXredis.exists(f"welcome_security_users:{called_user_id}:{chat_id}"):
XXXXXXXXXXXXawaitXmessage.answer(strings["not_allowed"],Xshow_alert=True)
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXX#XForXthoseXwhoXlostXtheirXbuttons
XXXXXXXXXXXXurlX=Xf"https://t.me/{BOT_USERNAME}?start=ws_{chat_id}_{called_user_id}_{message.message.message_id}_0"
XXXXawaitXmessage.answer(url=url)


@register(CommandStart(re.compile(r"ws_")),Xallow_kwargs=True)
@get_strings_dec("greetings")
asyncXdefXwelcome_security_handler_pm(
XXXXmessage:XMessage,Xstrings,Xregexp=None,Xstate=None,X**kwargs
):
XXXXargsX=Xmessage.get_args().split("_")
XXXXchat_idX=Xint(args[1])

XXXXasyncXwithXstate.proxy()XasXdata:
XXXXXXXXdata["chat_id"]X=Xchat_id
XXXXXXXXdata["msg_id"]X=Xint(args[3])
XXXXXXXXdata["to_delete"]X=Xbool(int(args[4]))XifXlen(args)X>X4XelseXTrue

XXXXdb_itemX=XawaitXget_greetings_data(chat_id)

XXXXlevelX=Xdb_item["welcome_security"]["level"]

XXXXifXlevelX==X"button":
XXXXXXXXawaitXWelcomeSecurityState.button.set()
XXXXXXXXawaitXsend_button(message,Xstate)

XXXXelifXlevelX==X"math":
XXXXXXXXawaitXWelcomeSecurityState.math.set()
XXXXXXXXawaitXsend_btn_math(message,Xstate)

XXXXelifXlevelX==X"captcha":
XXXXXXXXawaitXWelcomeSecurityState.captcha.set()
XXXXXXXXawaitXsend_captcha(message,Xstate)


@get_strings_dec("greetings")
asyncXdefXsend_button(message,Xstate,Xstrings):
XXXXtextX=Xstrings["btn_button_text"]
XXXXbuttonsX=XInlineKeyboardMarkup().add(
XXXXXXXXInlineKeyboardButton(strings["click_here"],Xcallback_data="wc_button_btn")
XXXX)
XXXXverify_msg_idX=X(awaitXmessage.reply(text,Xreply_markup=buttons)).message_id
XXXXasyncXwithXstate.proxy()XasXdata:
XXXXXXXXdata["verify_msg_id"]X=Xverify_msg_id


@register(
XXXXregexp="wc_button_btn",Xf="cb",Xstate=WelcomeSecurityState.button,Xallow_kwargs=True
)
asyncXdefXwc_button_btn_cb(event,Xstate=None,X**kwargs):
XXXXawaitXwelcome_security_passed(event,Xstate)


defXgenerate_captcha(number=None):
XXXXifXnotXnumber:
XXXXXXXXnumberX=Xstr(random.randint(10001,X99999))
XXXXcaptchaX=XImageCaptcha(fonts=ALL_FONTS,Xwidth=200,Xheight=100).generate_image(
XXXXXXXXnumber
XXXX)
XXXXimgX=Xio.BytesIO()
XXXXcaptcha.save(img,X"PNG")
XXXXimg.seek(0)
XXXXreturnXimg,Xnumber


@get_strings_dec("greetings")
asyncXdefXsend_captcha(message,Xstate,Xstrings):
XXXXimg,XnumX=Xgenerate_captcha()
XXXXasyncXwithXstate.proxy()XasXdata:
XXXXXXXXdata["captcha_num"]X=Xnum
XXXXtextX=Xstrings["ws_captcha_text"].format(
XXXXXXXXuser=awaitXget_user_link(message.from_user.id)
XXXX)

XXXXbuttonsX=XInlineKeyboardMarkup().add(
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXstrings["regen_captcha_btn"],Xcallback_data="regen_captcha"
XXXXXXXX)
XXXX)

XXXXverify_msg_idX=X(
XXXXXXXXawaitXmessage.answer_photo(img,Xcaption=text,Xreply_markup=buttons)
XXXX).message_id
XXXXasyncXwithXstate.proxy()XasXdata:
XXXXXXXXdata["verify_msg_id"]X=Xverify_msg_id


@register(
XXXXregexp="regen_captcha",
XXXXf="cb",
XXXXstate=WelcomeSecurityState.captcha,
XXXXallow_kwargs=True,
)
@get_strings_dec("greetings")
asyncXdefXchange_captcha(event,Xstrings,Xstate=None,X**kwargs):
XXXXmessageX=Xevent.message
XXXXasyncXwithXstate.proxy()XasXdata:
XXXXXXXXdata["regen_num"]X=X1XifX"regen_num"XnotXinXdataXelseXdata["regen_num"]X+X1
XXXXXXXXregen_numX=Xdata["regen_num"]

XXXXXXXXifXregen_numX>X3:
XXXXXXXXXXXXimg,XnumX=Xgenerate_captcha(number=data["captcha_num"])
XXXXXXXXXXXXtextX=Xstrings["last_chance"]
XXXXXXXXXXXXawaitXmessage.edit_media(InputMediaPhoto(img,Xcaption=text))
XXXXXXXXXXXXreturn

XXXXXXXXimg,XnumX=Xgenerate_captcha()
XXXXXXXXdata["captcha_num"]X=Xnum

XXXXtextX=Xstrings["ws_captcha_text"].format(
XXXXXXXXuser=awaitXget_user_link(event.from_user.id)
XXXX)

XXXXbuttonsX=XInlineKeyboardMarkup().add(
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXstrings["regen_captcha_btn"],Xcallback_data="regen_captcha"
XXXXXXXX)
XXXX)

XXXXawaitXmessage.edit_media(InputMediaPhoto(img,Xcaption=text),Xreply_markup=buttons)


@register(f="text",Xstate=WelcomeSecurityState.captcha,Xallow_kwargs=True)
@get_strings_dec("greetings")
asyncXdefXcheck_captcha_text(message,Xstrings,Xstate=None,X**kwargs):
XXXXnumX=Xmessage.text.split("X")[0]

XXXXifXnotXnum.isdigit():
XXXXXXXXawaitXmessage.reply(strings["num_is_not_digit"])
XXXXXXXXreturn

XXXXasyncXwithXstate.proxy()XasXdata:
XXXXXXXXcaptcha_numX=Xdata["captcha_num"]

XXXXifXnotXint(num)X==Xint(captcha_num):
XXXXXXXXawaitXmessage.reply(strings["bad_num"])
XXXXXXXXreturn

XXXXawaitXwelcome_security_passed(message,Xstate)


#XBtns


defXgen_expression():
XXXXaX=Xrandom.randint(1,X10)
XXXXbX=Xrandom.randint(1,X10)
XXXXifXrandom.getrandbits(1):
XXXXXXXXwhileXaX<Xb:
XXXXXXXXXXXXbX=Xrandom.randint(1,X10)
XXXXXXXXanswrX=XaX-Xb
XXXXXXXXexprX=Xf"{a}X-X{b}"
XXXXelse:
XXXXXXXXbX=Xrandom.randint(1,X10)

XXXXXXXXanswrX=XaX+Xb
XXXXXXXXexprX=Xf"{a}X+X{b}"

XXXXreturnXexpr,Xanswr


defXgen_int_btns(answer):
XXXXbuttonsX=X[]

XXXXforXaXinX[random.randint(1,X20)XforX_XinXrange(3)]:
XXXXXXXXwhileXaX==Xanswer:
XXXXXXXXXXXXaX=Xrandom.randint(1,X20)
XXXXXXXXbuttons.append(Button.inline(str(a),Xdata="wc_int_btn:"X+Xstr(a)))

XXXXbuttons.insert(
XXXXXXXXrandom.randint(0,X3),
XXXXXXXXButton.inline(str(answer),Xdata="wc_int_btn:"X+Xstr(answer)),
XXXX)

XXXXreturnXbuttons


@get_strings_dec("greetings")
asyncXdefXsend_btn_math(message,Xstate,Xstrings,Xmsg_id=False):
XXXXchat_idX=Xmessage.chat.id
XXXXexpr,XanswerX=Xgen_expression()

XXXXasyncXwithXstate.proxy()XasXdata:
XXXXXXXXdata["num"]X=Xanswer

XXXXbtnsX=Xgen_int_btns(answer)

XXXXifXmsg_id:
XXXXXXXXasyncXwithXstate.proxy()XasXdata:
XXXXXXXXXXXXdata["last"]X=XTrue
XXXXXXXXtextX=Xstrings["math_wc_rtr_text"]X+Xstrings["btn_wc_text"]X%Xexpr
XXXXelse:
XXXXXXXXtextX=Xstrings["btn_wc_text"]X%Xexpr
XXXXXXXXmsg_idX=X(awaitXmessage.reply(text)).message_id

XXXXasyncXwithXstate.proxy()XasXdata:
XXXXXXXXdata["verify_msg_id"]X=Xmsg_id

XXXXawaitXtbot.edit_message(
XXXXXXXXchat_id,Xmsg_id,Xtext,Xbuttons=btns
XXXX)XX#XTODO:XchangeXtoXaiogram


@register(
XXXXregexp="wc_int_btn:",Xf="cb",Xstate=WelcomeSecurityState.math,Xallow_kwargs=True
)
@get_strings_dec("greetings")
asyncXdefXwc_math_check_cb(event,Xstrings,Xstate=None,X**kwargs):
XXXXnumX=Xint(event.data.split(":")[1])

XXXXasyncXwithXstate.proxy()XasXdata:
XXXXXXXXanswerX=Xdata["num"]
XXXXXXXXifX"last"XinXdata:
XXXXXXXXXXXXawaitXstate.finish()
XXXXXXXXXXXXawaitXevent.answer(strings["math_wc_sry"],Xshow_alert=True)
XXXXXXXXXXXXawaitXevent.message.delete()
XXXXXXXXXXXXreturn

XXXXifXnotXnumX==Xanswer:
XXXXXXXXawaitXsend_btn_math(event.message,Xstate,Xmsg_id=event.message.message_id)
XXXXXXXXawaitXevent.answer(strings["math_wc_wrong"],Xshow_alert=True)
XXXXXXXXreturn

XXXXawaitXwelcome_security_passed(event,Xstate)


@get_strings_dec("greetings")
asyncXdefXwelcome_security_passed(
XXXXmessage:XUnion[CallbackQuery,XMessage],Xstate,Xstrings
):
XXXXuser_idX=Xmessage.from_user.id
XXXXasyncXwithXstate.proxy()XasXdata:
XXXXXXXXchat_idX=Xdata["chat_id"]
XXXXXXXXmsg_idX=Xdata["msg_id"]
XXXXXXXXverify_msg_idX=Xdata["verify_msg_id"]
XXXXXXXXto_deleteX=Xdata["to_delete"]

XXXXwithXsuppress(ChatAdminRequired):
XXXXXXXXawaitXunmute_user(chat_id,Xuser_id)

XXXXwithXsuppress(MessageToDeleteNotFound,XMessageCantBeDeleted):
XXXXXXXXifXto_delete:
XXXXXXXXXXXXawaitXbot.delete_message(chat_id,Xmsg_id)
XXXXXXXXawaitXbot.delete_message(user_id,Xverify_msg_id)
XXXXawaitXstate.finish()

XXXXwithXsuppress(MessageToDeleteNotFound,XMessageCantBeDeleted):
XXXXXXXXmessage_idX=Xredis.get(f"welcome_security_users:{user_id}:{chat_id}")
XXXXXXXX#XDeleteXtheXperson'sXrealXsecurityXbuttonXifXexists!
XXXXXXXXifXmessage_id:
XXXXXXXXXXXXawaitXbot.delete_message(chat_id,Xmessage_id)

XXXXredis.delete(f"welcome_security_users:{user_id}:{chat_id}")

XXXXwithXsuppress(JobLookupError):
XXXXXXXXscheduler.remove_job(f"wc_expire:{chat_id}:{user_id}")

XXXXtitleX=X(awaitXdb.chat_list.find_one({"chat_id":Xchat_id}))["chat_title"]

XXXXifX"data"XinXmessage:
XXXXXXXXawaitXmessage.answer(strings["passed_no_frm"]X%Xtitle,Xshow_alert=True)
XXXXelse:
XXXXXXXXawaitXmessage.reply(strings["passed"]X%Xtitle)

XXXXdb_itemX=XawaitXget_greetings_data(chat_id)

XXXXifX"message"XinXmessage:
XXXXXXXXmessageX=Xmessage.message

XXXX#XWelcome
XXXXifX"note"XinXdb_itemXandXnotXdb_item.get("welcome_disabled",XFalse):
XXXXXXXXtext,XkwargsX=XawaitXt_unparse_note_item(
XXXXXXXXXXXXmessage.reply_to_message
XXXXXXXXXXXXifXmessage.reply_to_messageXisXnotXNone
XXXXXXXXXXXXelseXmessage,
XXXXXXXXXXXXdb_item["note"],
XXXXXXXXXXXXchat_id,
XXXXXXXX)
XXXXXXXXawaitXsend_note(user_id,Xtext,X**kwargs)

XXXX#XWelcomeXmute
XXXXifX"welcome_mute"XinXdb_itemXandXdb_item["welcome_mute"]["enabled"]XisXnotXFalse:
XXXXXXXXuserX=XawaitXbot.get_chat_member(chat_id,Xuser_id)
XXXXXXXXifX"can_send_messages"XnotXinXuserXorXuser["can_send_messages"]XisXTrue:
XXXXXXXXXXXXawaitXrestrict_user(
XXXXXXXXXXXXXXXXchat_id,
XXXXXXXXXXXXXXXXuser_id,
XXXXXXXXXXXXXXXXuntil_date=convert_time(db_item["welcome_mute"]["time"]),
XXXXXXXXXXXX)

XXXXchatX=XawaitXdb.chat_list.find_one({"chat_id":Xchat_id})

XXXXbuttonsX=XNone
XXXXifXchat_nickX:=Xchat["chat_nick"]XifXchat.get("chat_nick",XNone)XelseXNone:
XXXXXXXXbuttonsX=XInlineKeyboardMarkup().add(
XXXXXXXXXXXXInlineKeyboardButton(text=strings["click_here"],Xurl=f"t.me/{chat_nick}")
XXXXXXXX)

XXXXawaitXbot.send_message(user_id,Xstrings["verification_done"],Xreply_markup=buttons)


#XEndXWelcomeXSecurity

#XWelcomes
@register(only_groups=True,Xf="welcome")
@get_strings_dec("greetings")
asyncXdefXwelcome_trigger(message:XMessage,Xstrings):
XXXXifXlen(message.new_chat_members)X>X1:
XXXXXXXX#XFIXME:XAllMightRobotXdoesntXsupportXaddingXmultipleXusersXcurrently
XXXXXXXXreturn

XXXXchat_idX=Xmessage.chat.id
XXXXuser_idX=Xmessage.new_chat_members[0].id

XXXXifXuser_idX==XBOT_ID:
XXXXXXXXreturn

XXXXifXnotX(db_itemX:=XawaitXget_greetings_data(message.chat.id)):
XXXXXXXXdb_itemX=X{}

XXXXifX"welcome_disabled"XinXdb_itemXandXdb_item["welcome_disabled"]XisXTrue:
XXXXXXXXreturn

XXXXifX"welcome_security"XinXdb_itemXandXdb_item["welcome_security"]["enabled"]:
XXXXXXXXreturn

XXXX#XWelcome
XXXXifX"note"XnotXinXdb_item:
XXXXXXXXdb_item["note"]X=X{"text":Xstrings["default_welcome"],X"parse_mode":X"md"}
XXXXreply_toX=X(
XXXXXXXXmessage.message_id
XXXXXXXXifX"clean_welcome"XinXdb_item
XXXXXXXXandXdb_item["clean_welcome"]["enabled"]XisXnotXFalse
XXXXXXXXelseXNone
XXXX)
XXXXtext,XkwargsX=XawaitXt_unparse_note_item(message,Xdb_item["note"],Xchat_id)
XXXXmsgX=XawaitXsend_note(chat_id,Xtext,Xreply_to=reply_to,X**kwargs)
XXXX#XCleanXwelcome
XXXXifX"clean_welcome"XinXdb_itemXandXdb_item["clean_welcome"]["enabled"]XisXnotXFalse:
XXXXXXXXifX"last_msg"XinXdb_item["clean_welcome"]:
XXXXXXXXXXXXwithXsuppress(MessageToDeleteNotFound,XMessageCantBeDeleted):
XXXXXXXXXXXXXXXXifXvalueX:=Xredis.get(_clean_welcome.format(chat=chat_id)):
XXXXXXXXXXXXXXXXXXXXawaitXbot.delete_message(chat_id,Xvalue)
XXXXXXXXredis.set(_clean_welcome.format(chat=chat_id),Xmsg.id)

XXXX#XWelcomeXmute
XXXXifXuser_idX==XBOT_ID:
XXXXXXXXreturn
XXXXifX"welcome_mute"XinXdb_itemXandXdb_item["welcome_mute"]["enabled"]XisXnotXFalse:
XXXXXXXXuserX=XawaitXbot.get_chat_member(chat_id,Xuser_id)
XXXXXXXXifX"can_send_messages"XnotXinXuserXorXuser["can_send_messages"]XisXTrue:
XXXXXXXXXXXXifXnotXawaitXcheck_admin_rights(
XXXXXXXXXXXXXXXXmessage,Xchat_id,XBOT_ID,X["can_restrict_members"]
XXXXXXXXXXXX):
XXXXXXXXXXXXXXXXawaitXmessage.reply(strings["not_admin_wm"])
XXXXXXXXXXXXXXXXreturn

XXXXXXXXXXXXawaitXrestrict_user(
XXXXXXXXXXXXXXXXchat_id,
XXXXXXXXXXXXXXXXuser_id,
XXXXXXXXXXXXXXXXuntil_date=convert_time(db_item["welcome_mute"]["time"]),
XXXXXXXXXXXX)


#XCleanXserviceXtrigger
@register(only_groups=True,Xf="service")
@get_strings_dec("greetings")
asyncXdefXclean_service_trigger(message,Xstrings):
XXXXchat_idX=Xmessage.chat.id

XXXXifXmessage.new_chat_members[0].idX==XBOT_ID:
XXXXXXXXreturn

XXXXifXnotX(db_itemX:=XawaitXget_greetings_data(chat_id)):
XXXXXXXXreturn

XXXXifX"clean_service"XnotXinXdb_itemXorXdb_item["clean_service"]["enabled"]XisXFalse:
XXXXXXXXreturn

XXXXifXnotXawaitXcheck_admin_rights(message,Xchat_id,XBOT_ID,X["can_delete_messages"]):
XXXXXXXXawaitXbot.send_message(chat_id,Xstrings["not_admin_wsr"])
XXXXXXXXreturn

XXXXwithXsuppress(MessageToDeleteNotFound,XMessageCantBeDeleted):
XXXXXXXXawaitXmessage.delete()


_clean_welcomeX=X"cleanwelcome:{chat}"


@cached()
asyncXdefXget_greetings_data(chat:Xint)X->XOptional[dict]:
XXXXreturnXawaitXdb.greetings.find_one({"chat_id":Xchat})


asyncXdefX__export__(chat_id):
XXXXifXgreetingsX:=XawaitXget_greetings_data(chat_id):
XXXXXXXXdelXgreetings["_id"]
XXXXXXXXdelXgreetings["chat_id"]

XXXXXXXXreturnX{"greetings":Xgreetings}


asyncXdefX__import__(chat_id,Xdata):
XXXXawaitXdb.greetings.update_one({"chat_id":Xchat_id},X{"$set":Xdata},Xupsert=True)
XXXXawaitXget_greetings_data.reset_cache(chat_id)


__mod_name__X=X"Greetings"

__help__X=X"""
<b>AvailableXcommands:</b>
<b>General:</b>
-X/setwelcomeXorX/savewelcome:XSetXwelcome
-X/setwelcomeX(on/off):XDisable/enabledXwelcomesXinXyourXchat
-X/welcome:XShowsXcurrentXwelcomesXsettingsXandXwelcomeXtext
-X/resetwelcome:XResetXwelcomesXsettings
<b>WelcomeXsecurity:</b>
-X/welcomesecurityX(level)
TurnsXonXwelcomeXsecurityXwithXspecifiedXlevel,XeitherXbuttonXorXcaptcha.
SettingXupXwelcomeXsecurityXwillXgiveXyouXaXchoiceXtoXcustomizeXjoinXexpirationXtimeXakaXminimumXtimeXgivenXtoXuserXtoXverifyXthemselvesXnotXaXbot,XusersXwhoXdoXnotXverifyXwithinXthisXtimeXwouldXbeXkicked!
-X/welcomesecurityX(off/no/0):XDisableXwelcomeXsecurity
-X/setsecuritynote:XCustomiseXtheX"PleaseXpressXbuttonXbelowXtoXverifyXthemselfXasXhuman!"Xtext
-X/delsecuritynote:XResetXsecurityXtextXtoXdefaults
<b>AvailableXlevels:</b>
-X<code>button</code>:XAskXuserXtoXpressX"I'mXnotXaXbot"Xbutton
-X<code>math</code>:XAskingXtoXsolveXsimpleXmathXquery,XfewXbuttonsXwithXanswersXwillXbeXprovided,XonlyXoneXwillXhaveXrightXanswer
-X<code>captcha</code>:XAskXuserXtoXenterXcaptcha
<b>WelcomeXmutes:</b>
-X/welcomemuteX(time):XSetXwelcomeXmuteX(noXmedia)XforXXXtime
-X/welcomemuteX(off/no):XDisableXwelcomeXmute
<b>Purges:</b>
-X/cleanwelcomeX(on/off):XDeletesXoldXwelcomeXmessagesXandXlastXoneXafterX45Xmintes
-X/cleanserviceX(on/off):XCleansXserviceXmessagesX(userXXXjoined)
IfXwelcomeXsecurityXisXenabled,XuserXwillXbeXwelcomedXwithXsecurityXtext,XifXuserXsuccessfullyXverifyXselfXasXuser,Xhe/sheXwillXbeXwelcomedXalsoXwithXwelcomeXtextXinXhisXPMX(toXpreventXspammingXinXchat).
IfXuserXdidn'tXverifiedXselfXforX24XhoursXhe/sheXwillXbeXkickedXfromXchat.
<b>AddingsXbuttonsXandXvariablesXtoXwelcomesXorXsecurityXtext:</b>
ButtonsXandXvariablesXsyntaxXisXsameXasXnotesXbuttonsXandXvariables.
SendX/buttonshelpXandX/variableshelpXtoXgetXstartedXwithXusingXit.
<b>SettingsXimages,Xgifs,XvideosXorXstickersXasXwelcome:</b>
SavingXattachmentsXonXwelcomeXisXsameXasXsavingXnotesXwithXit,XreadXtheXnotesXhelpXaboutXit.XButXkeepXinXmindXwhatXyouXhaveXtoXreplaceX/saveXtoX/setwelcome
<b>Examples:</b>
<code>-XGetXtheXwelcomeXmessageXwithoutXanyXformatting
->X/welcomeXraw</code>
"""
