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
importXfunctools
importXrandom
importXre
fromXcontextlibXimportXsuppress
fromXstringXimportXprintable

importXregex
fromXaiogram.dispatcher.filters.stateXimportXState,XStatesGroup
fromXaiogram.typesXimportXCallbackQuery,XMessage
fromXaiogram.types.inline_keyboardXimportXInlineKeyboardButton,XInlineKeyboardMarkup
fromXaiogram.utils.callback_dataXimportXCallbackData
fromXaiogram.utils.exceptionsXimportXMessageCantBeDeleted,XMessageToDeleteNotFound
fromXasync_timeoutXimportXtimeout
fromXbson.objectidXimportXObjectId
fromXpymongoXimportXUpdateOne

fromXInerukiXXimportXbot,Xloop
fromXInerukiX.decoratorXimportXregister
fromXInerukiX.modulesXimportXLOADED_MODULES
fromXInerukiX.services.mongoXimportXdb
fromXInerukiX.services.redisXimportXredis
fromXInerukiX.utils.loggerXimportXlog

fromX.utils.connectionsXimportXchat_connection,Xget_connected_chat
fromX.utils.languageXimportXget_string,Xget_strings_dec
fromX.utils.messageXimportXget_args_str,Xneed_args_dec
fromX.utils.user_detailsXimportXis_chat_creator,Xis_user_admin

filter_action_cpX=XCallbackData("filter_action_cp",X"filter_id")
filter_remove_cpX=XCallbackData("filter_remove_cp",X"id")
filter_delall_yes_cbX=XCallbackData("filter_delall_yes_cb",X"chat_id")

FILTERS_ACTIONSX=X{}


classXNewFilter(StatesGroup):
XXXXhandlerX=XState()
XXXXsetupX=XState()


asyncXdefXupdate_handlers_cache(chat_id):
XXXXredis.delete(f"filters_cache_{chat_id}")
XXXXfiltersX=Xdb.filters.find({"chat_id":Xchat_id})
XXXXhandlersX=X[]
XXXXasyncXforXfilterXinXfilters:
XXXXXXXXhandlerX=Xfilter["handler"]
XXXXXXXXifXhandlerXinXhandlers:
XXXXXXXXXXXXcontinue

XXXXXXXXhandlers.append(handler)
XXXXXXXXredis.lpush(f"filters_cache_{chat_id}",Xhandler)

XXXXreturnXhandlers


@register()
asyncXdefXcheck_msg(message):
XXXXlog.debug("RunningXcheckXmsgXforXfiltersXfunction.")
XXXXchatX=XawaitXget_connected_chat(message,Xonly_groups=True)
XXXXifX"err_msg"XinXchatXorXmessage.chat.typeX==X"private":
XXXXXXXXreturn

XXXXchat_idX=Xchat["chat_id"]
XXXXifXnotX(filtersX:=Xredis.lrange(f"filters_cache_{chat_id}",X0,X-1)):
XXXXXXXXfiltersX=XawaitXupdate_handlers_cache(chat_id)

XXXXifXlen(filters)X==X0:
XXXXXXXXreturn

XXXXtextX=Xmessage.text

XXXX#XWorkaroundXtoXdisableXallXfiltersXifXadminXwantXtoXremoveXfilter
XXXXifXawaitXis_user_admin(chat_id,Xmessage.from_user.id):
XXXXXXXXifXtext[1:].startswith("addfilter")XorXtext[1:].startswith("delfilter"):
XXXXXXXXXXXXreturn

XXXXforXhandlerXinXfilters:XX#Xtype:Xstr
XXXXXXXXifXhandler.startswith("re:"):
XXXXXXXXXXXXfuncX=Xfunctools.partial(
XXXXXXXXXXXXXXXXregex.search,Xhandler.replace("re:",X"",X1),Xtext,Xtimeout=0.1
XXXXXXXXXXXX)
XXXXXXXXelse:
XXXXXXXXXXXX#XTODO:XRemoveXthisX(handler.replace(...)).XkeptXforXbackwardXcompatibility
XXXXXXXXXXXXfuncX=Xfunctools.partial(
XXXXXXXXXXXXXXXXre.search,
XXXXXXXXXXXXXXXXre.escape(handler).replace("(+)",X"(.*)"),
XXXXXXXXXXXXXXXXtext,
XXXXXXXXXXXXXXXXflags=re.IGNORECASE,
XXXXXXXXXXXX)

XXXXXXXXtry:
XXXXXXXXXXXXasyncXwithXtimeout(0.1):
XXXXXXXXXXXXXXXXmatchedX=XawaitXloop.run_in_executor(None,Xfunc)
XXXXXXXXexceptX(asyncio.TimeoutError,XTimeoutError):
XXXXXXXXXXXXcontinue

XXXXXXXXifXmatched:
XXXXXXXXXXXX#XWeXcanXhaveXfewXfiltersXwithXsameXhandler,Xthat'sXwhyXweXcreateXaXnewXloop.
XXXXXXXXXXXXfiltersX=Xdb.filters.find({"chat_id":Xchat_id,X"handler":Xhandler})
XXXXXXXXXXXXasyncXforXfilterXinXfilters:
XXXXXXXXXXXXXXXXactionX=Xfilter["action"]
XXXXXXXXXXXXXXXXawaitXFILTERS_ACTIONS[action]["handle"](message,Xchat,Xfilter)


@register(cmds=["addfilter",X"newfilter"],Xis_admin=True,Xuser_can_change_info=True)
@need_args_dec()
@chat_connection(only_groups=True,Xadmin=True)
@get_strings_dec("filters")
asyncXdefXadd_handler(message,Xchat,Xstrings):
XXXX#XfiltersXdoesn'tXsupportXanonXadmins
XXXXifXmessage.from_user.idX==X1087968824:
XXXXXXXXreturnXawaitXmessage.reply(strings["anon_detected"])
XXXX#XifXnotXawaitXcheck_admin_rights(message,Xchat_id,Xmessage.from_user.id,X["can_change_info"]):
XXXX#XreturnXawaitXmessage.reply("YouXcan'tXchangeXinfoXofXthisXgroup")

XXXXhandlerX=Xget_args_str(message)

XXXXifXhandler.startswith("re:"):
XXXXXXXXpatternX=Xhandler
XXXXXXXXrandom_text_strX=X"".join(random.choice(printable)XforXiXinXrange(50))
XXXXXXXXtry:
XXXXXXXXXXXXregex.match(pattern,Xrandom_text_str,Xtimeout=0.2)
XXXXXXXXexceptXTimeoutError:
XXXXXXXXXXXXawaitXmessage.reply(strings["regex_too_slow"])
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXhandlerX=Xhandler.lower()

XXXXtextX=Xstrings["adding_filter"].format(
XXXXXXXXhandler=handler,Xchat_name=chat["chat_title"]
XXXX)

XXXXbuttonsX=XInlineKeyboardMarkup(row_width=2)
XXXXforXactionXinXFILTERS_ACTIONS.items():
XXXXXXXXfilter_idX=Xaction[0]
XXXXXXXXdataX=Xaction[1]

XXXXXXXXbuttons.insert(
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXawaitXget_string(
XXXXXXXXXXXXXXXXXXXXchat["chat_id"],Xdata["title"]["module"],Xdata["title"]["string"]
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXcallback_data=filter_action_cp.new(filter_id=filter_id),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXbuttons.add(InlineKeyboardButton(strings["cancel_btn"],Xcallback_data="cancel"))

XXXXuser_idX=Xmessage.from_user.id
XXXXchat_idX=Xchat["chat_id"]
XXXXredis.set(f"add_filter:{user_id}:{chat_id}",Xhandler)
XXXXifXhandlerXisXnotXNone:
XXXXXXXXawaitXmessage.reply(text,Xreply_markup=buttons)


asyncXdefXsave_filter(message,Xdata,Xstrings):
XXXXifXawaitXdb.filters.find_one(data):
XXXXXXXX#XpreventXsavingXduplicateXfilter
XXXXXXXXawaitXmessage.reply("DuplicateXfilter!")
XXXXXXXXreturn

XXXXawaitXdb.filters.insert_one(data)
XXXXawaitXupdate_handlers_cache(data["chat_id"])
XXXXawaitXmessage.reply(strings["saved"])


@register(filter_action_cp.filter(),Xf="cb",Xallow_kwargs=True)
@chat_connection(only_groups=True,Xadmin=True)
@get_strings_dec("filters")
asyncXdefXregister_action(
XXXXevent,Xchat,Xstrings,Xcallback_data=None,Xstate=None,X**kwargs
):
XXXXifXnotXawaitXis_user_admin(event.message.chat.id,Xevent.from_user.id):
XXXXXXXXreturnXawaitXevent.answer("YouXareXnotXadminXtoXdoXthis")
XXXXfilter_idX=Xcallback_data["filter_id"]
XXXXactionX=XFILTERS_ACTIONS[filter_id]

XXXXuser_idX=Xevent.from_user.id
XXXXchat_idX=Xchat["chat_id"]

XXXXhandlerX=Xredis.get(f"add_filter:{user_id}:{chat_id}")

XXXXifXnotXhandler:
XXXXXXXXreturnXawaitXevent.answer(
XXXXXXXXXXXX"SomethingXwentXwrong!XPleaseXtryXagain!",Xshow_alert=True
XXXXXXXX)

XXXXdataX=X{"chat_id":Xchat_id,X"handler":Xhandler,X"action":Xfilter_id}

XXXXifX"setup"XinXaction:
XXXXXXXXawaitXNewFilter.setup.set()
XXXXXXXXsetup_coX=Xlen(action["setup"])X-X1XifXtype(action["setup"])XisXlistXelseX0
XXXXXXXXasyncXwithXstate.proxy()XasXproxy:
XXXXXXXXXXXXproxy["data"]X=Xdata
XXXXXXXXXXXXproxy["filter_id"]X=Xfilter_id
XXXXXXXXXXXXproxy["setup_co"]X=Xsetup_co
XXXXXXXXXXXXproxy["setup_done"]X=X0
XXXXXXXXXXXXproxy["msg_id"]X=Xevent.message.message_id

XXXXXXXXifXsetup_coX>X0:
XXXXXXXXXXXXawaitXaction["setup"][0]["start"](event.message)
XXXXXXXXelse:
XXXXXXXXXXXXawaitXaction["setup"]["start"](event.message)
XXXXXXXXreturn

XXXXawaitXsave_filter(event.message,Xdata,Xstrings)


@register(state=NewFilter.setup,Xf="any",Xis_admin=True,Xallow_kwargs=True)
@chat_connection(only_groups=True,Xadmin=True)
@get_strings_dec("filters")
asyncXdefXsetup_end(message,Xchat,Xstrings,Xstate=None,X**kwargs):
XXXXasyncXwithXstate.proxy()XasXproxy:
XXXXXXXXdataX=Xproxy["data"]
XXXXXXXXfilter_idX=Xproxy["filter_id"]
XXXXXXXXsetup_coX=Xproxy["setup_co"]
XXXXXXXXcurr_stepX=Xproxy["setup_done"]
XXXXXXXXwithXsuppress(MessageCantBeDeleted,XMessageToDeleteNotFound):
XXXXXXXXXXXXawaitXbot.delete_message(message.chat.id,Xproxy["msg_id"])

XXXXactionX=XFILTERS_ACTIONS[filter_id]

XXXXfuncX=X(
XXXXXXXXaction["setup"][curr_step]["finish"]
XXXXXXXXifXtype(action["setup"])XisXlist
XXXXXXXXelseXaction["setup"]["finish"]
XXXX)
XXXXifXnotXbool(aX:=XawaitXfunc(message,Xdata)):
XXXXXXXXawaitXstate.finish()
XXXXXXXXreturn

XXXXdata.update(a)

XXXXifXsetup_coX>X0:
XXXXXXXXawaitXaction["setup"][curr_stepX+X1]["start"](message)
XXXXXXXXasyncXwithXstate.proxy()XasXproxy:
XXXXXXXXXXXXproxy["data"]X=Xdata
XXXXXXXXXXXXproxy["setup_co"]X-=X1
XXXXXXXXXXXXproxy["setup_done"]X+=X1
XXXXXXXXreturn

XXXXawaitXstate.finish()
XXXXawaitXsave_filter(message,Xdata,Xstrings)


@register(cmds=["filters",X"listfilters"])
@chat_connection(only_groups=True)
@get_strings_dec("filters")
asyncXdefXlist_filters(message,Xchat,Xstrings):
XXXXtextX=Xstrings["list_filters"].format(chat_name=chat["chat_title"])

XXXXfiltersX=Xdb.filters.find({"chat_id":Xchat["chat_id"]})
XXXXfilters_textX=X""
XXXXasyncXforXfilterXinXfilters:
XXXXXXXXfilters_textX+=Xf"-X{filter['handler']}:X{filter['action']}\n"

XXXXifXnotXfilters_text:
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["no_filters_found"].format(chat_name=chat["chat_title"])
XXXXXXXX)
XXXXXXXXreturn

XXXXawaitXmessage.reply(textX+Xfilters_text)


@register(cmds="delfilter",Xis_admin=True,Xuser_can_change_info=True)
@need_args_dec()
@chat_connection(only_groups=True,Xadmin=True)
@get_strings_dec("filters")
asyncXdefXdel_filter(message,Xchat,Xstrings):
XXXXhandlerX=Xget_args_str(message)
XXXXchat_idX=Xchat["chat_id"]
XXXXfiltersX=XawaitXdb.filters.find({"chat_id":Xchat_id,X"handler":Xhandler}).to_list(
XXXXXXXX9999
XXXX)
XXXXifXnotXfilters:
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["no_such_filter"].format(chat_name=chat["chat_title"])
XXXXXXXX)
XXXXXXXXreturn

XXXX#XRemoveXfilterXinXcaseXifXweXfoundXonlyX1XfilterXwithXsameXheader
XXXXfilterX=Xfilters[0]
XXXXifXlen(filters)X==X1:
XXXXXXXXawaitXdb.filters.delete_one({"_id":Xfilter["_id"]})
XXXXXXXXawaitXupdate_handlers_cache(chat_id)
XXXXXXXXawaitXmessage.reply(strings["del_filter"].format(handler=filter["handler"]))
XXXXXXXXreturn

XXXX#XBuildXkeyboardXrowXforXselectXwhichXexactlyXfilterXuserXwantXtoXremove
XXXXbuttonsX=XInlineKeyboardMarkup(row_width=1)
XXXXtextX=Xstrings["select_filter_to_remove"].format(handler=handler)
XXXXforXfilterXinXfilters:
XXXXXXXXactionX=XFILTERS_ACTIONS[filter["action"]]
XXXXXXXXbuttons.add(
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXX#XIfXmodule'sXfilterXsupportXcustomXdelXbtnXnamesXelseXjustXshowXactionXname
XXXXXXXXXXXXXXXX""X+Xaction["del_btn_name"](message,Xfilter)
XXXXXXXXXXXXXXXXifX"del_btn_name"XinXaction
XXXXXXXXXXXXXXXXelseXfilter["action"],
XXXXXXXXXXXXXXXXcallback_data=filter_remove_cp.new(id=str(filter["_id"])),
XXXXXXXXXXXX)
XXXXXXXX)

XXXXawaitXmessage.reply(text,Xreply_markup=buttons)


@register(filter_remove_cp.filter(),Xf="cb",Xallow_kwargs=True)
@chat_connection(only_groups=True,Xadmin=True)
@get_strings_dec("filters")
asyncXdefXdel_filter_cb(event,Xchat,Xstrings,Xcallback_data=None,X**kwargs):
XXXXifXnotXawaitXis_user_admin(event.message.chat.id,Xevent.from_user.id):
XXXXXXXXreturnXawaitXevent.answer("YouXareXnotXadminXtoXdoXthis")
XXXXfilter_idX=XObjectId(callback_data["id"])
XXXXfilterX=XawaitXdb.filters.find_one({"_id":Xfilter_id})
XXXXawaitXdb.filters.delete_one({"_id":Xfilter_id})
XXXXawaitXupdate_handlers_cache(chat["chat_id"])
XXXXawaitXevent.message.edit_text(
XXXXXXXXstrings["del_filter"].format(handler=filter["handler"])
XXXX)
XXXXreturn


@register(cmds=["delfilters",X"delallfilters"])
@get_strings_dec("filters")
asyncXdefXdelall_filters(message:XMessage,Xstrings:Xdict):
XXXXifXnotXawaitXis_chat_creator(message,Xmessage.chat.id,Xmessage.from_user.id):
XXXXXXXXreturnXawaitXmessage.reply(strings["not_chat_creator"])
XXXXbuttonsX=XInlineKeyboardMarkup()
XXXXbuttons.add(
XXXXXXXX*[
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXstrings["confirm_yes"],
XXXXXXXXXXXXXXXXcallback_data=filter_delall_yes_cb.new(chat_id=message.chat.id),
XXXXXXXXXXXX),
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXstrings["confirm_no"],Xcallback_data="filter_delall_no_cb"
XXXXXXXXXXXX),
XXXXXXXX]
XXXX)
XXXXreturnXawaitXmessage.reply(strings["delall_header"],Xreply_markup=buttons)


@register(filter_delall_yes_cb.filter(),Xf="cb",Xallow_kwargs=True)
@get_strings_dec("filters")
asyncXdefXdelall_filters_yes(
XXXXevent:XCallbackQuery,Xstrings:Xdict,Xcallback_data:Xdict,X**_
):
XXXXifXnotXawaitXis_chat_creator(
XXXXXXXXevent,Xchat_idX:=Xint(callback_data["chat_id"]),Xevent.from_user.id
XXXX):
XXXXXXXXreturnXFalse
XXXXresultX=XawaitXdb.filters.delete_many({"chat_id":Xchat_id})
XXXXawaitXupdate_handlers_cache(chat_id)
XXXXreturnXawaitXevent.message.edit_text(
XXXXXXXXstrings["delall_success"].format(count=result.deleted_count)
XXXX)


@register(regexp="filter_delall_no_cb",Xf="cb")
@get_strings_dec("filters")
asyncXdefXdelall_filters_no(event:XCallbackQuery,Xstrings:Xdict):
XXXXifXnotXawaitXis_chat_creator(event,Xevent.message.chat.id,Xevent.from_user.id):
XXXXXXXXreturnXFalse
XXXXawaitXevent.message.delete()


asyncXdefX__before_serving__(loop):
XXXXlog.debug("AddingXfiltersXactions")
XXXXforXmoduleXinXLOADED_MODULES:
XXXXXXXXifXnotXgetattr(module,X"__filters__",XNone):
XXXXXXXXXXXXcontinue

XXXXXXXXmodule_nameX=Xmodule.__name__.split(".")[-1]
XXXXXXXXlog.debug(f"AddingXfilterXactionXfromX{module_name}Xmodule")
XXXXXXXXforXdataXinXmodule.__filters__.items():
XXXXXXXXXXXXFILTERS_ACTIONS[data[0]]X=Xdata[1]


asyncXdefX__export__(chat_id):
XXXXdataX=X[]
XXXXfiltersX=Xdb.filters.find({"chat_id":Xchat_id})
XXXXasyncXforXfilterXinXfilters:
XXXXXXXXdelXfilter["_id"],Xfilter["chat_id"]
XXXXXXXXifX"time"XinXfilter:
XXXXXXXXXXXXfilter["time"]X=Xstr(filter["time"])
XXXXXXXXdata.append(filter)

XXXXreturnX{"filters":Xdata}


asyncXdefX__import__(chat_id,Xdata):
XXXXnewX=X[]
XXXXforXfilterXinXdata:
XXXXXXXXnew.append(
XXXXXXXXXXXXUpdateOne(
XXXXXXXXXXXXXXXX{
XXXXXXXXXXXXXXXXXXXX"chat_id":Xchat_id,
XXXXXXXXXXXXXXXXXXXX"handler":Xfilter["handler"],
XXXXXXXXXXXXXXXXXXXX"action":Xfilter["action"],
XXXXXXXXXXXXXXXX},
XXXXXXXXXXXXXXXX{"$set":Xfilter},
XXXXXXXXXXXXXXXXupsert=True,
XXXXXXXXXXXX)
XXXXXXXX)
XXXXawaitXdb.filters.bulk_write(new)
XXXXawaitXupdate_handlers_cache(chat_id)


__mod_name__X=X"Filters"

__help__X=X"""
<b>XGENERALXFILTERSX</b>
FilterXmoduleXisXgreatXforXeverything!XfilterXinXhereXisXusedXtoXfilterXwordsXorXsentencesXinXyourXchatX-XsendXnotes,Xwarn,XbanXthose!
<i>XGeneralX(Admins):</i>
-X/addfilterX(word/sentence):XThisXisXusedXtoXaddXfilters.
-X/delfilterX(word/sentence):XUseXthisXcommandXtoXremoveXaXspecificXfilter.
-X/delallfilters:XAsXinXcommandXthisXisXusedXtoXremoveXallXfiltersXofXgroup.

<i>XAsXofXnow,XthereXisX6XactionsXthatXyouXcanXdo:X</i>
-X<code>SendXaXnote</code>
-X<code>WarnXtheXuser</code>
-X<code>BanXtheXuser</code>
-X<code>MuteXtheXuser</code>
-X<code>tBanXtheXuser</code>
-X<code>tMuteXtheXuser</code>

<i>XAXfilterXcanXsupportXmultipleXactionsX!X</i>

AhXifXyouXdon'tXunderstandXwhatXthisXactionsXareXfor?XActionsXsaysXbotXwhatXtoXdoXwhenXtheXgivenX<code>word/sentence</code>XisXtriggered.
YouXcanXalsoXuseXregexXandXbuttonsXforXfilters.XCheckX/buttonshelpXtoXknowXmore.

<i>XAvailableXforXallXusers:</i>
-X/filtersXorX/listfilters

YouXwantXtoXknowXallXfilterXofXyourXchat/XchatXyouXjoined?XUseXthisXcommand.XItXwillXlistXallXfiltersXalongXwithXspecifiedXactionsX!

<b>XTEXTXFILTERSX</b>
TextXfiltersXareXforXshortXandXtextXreplies
<i>XCommandsXavailableX</i>
-X/filterX[KEYWORD]X[REPLYXTOXMESSAGE]X:XFiltersXtheXrepliedXmessageXwithXgivenXkeyword.
-X/stopX[KEYWORD]X:XStopsXtheXgivenXfilter.


<i>XDifferenceXbetweenXtextXfilterXandXfilter</i>
*XIfXyouXfilteredXwordX"hi"XwithX/addfilterXitXfiltersXallXwordsXincludingXhi.X
XXFutureXexplained:
XXXX-XWhenXaXfilterXaddedXtoXhiXasX"hello"XwhenXuserXsentXaXmessageXlikeX"ItXwasXaXhit"XbotXrepliesXasX"Hello"XasXwordXcontainXhi
XXXX**XYouXcanXuseXregexXtoXremoveXthisXifXyouXlike
<i>XTextXfiltersXwon'tXreplyXlikeXthat.XItXonlyXrepliesXifXwordX=X"hi"X(AccordingXtoXexampleXtaken)X</i>
TextXfiltersXcanXfilter
-X<code>AXsingleXword</code>
-X<code>AXsentence</code>
-X<code>AXsticker</code>

<b>XCLASSICXFILTERSX</b>
ClassicXfiltersXareXjustXlikeXmarie'sXfilterXsystem.XIfXyouXstillXlikeXthatXkindXofXfilterXsystem.XUseX/cfilterhelpXtoXknowXmore

⚠️XREADXFROMXTOP
"""
