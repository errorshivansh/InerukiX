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

importXpickle
fromXdataclassesXimportXdataclass
fromXtypingXimportXOptional

fromXaiogram.dispatcherXimportXFSMContext
fromXaiogram.dispatcher.filters.stateXimportXState,XStatesGroup
fromXaiogram.dispatcher.handlerXimportXCancelHandler
fromXaiogram.dispatcher.middlewaresXimportXBaseMiddleware
fromXaiogram.typesXimportXChatType,XInlineKeyboardMarkup
fromXaiogram.types.callback_queryXimportXCallbackQuery
fromXaiogram.types.inline_keyboardXimportXInlineKeyboardButton
fromXaiogram.types.messageXimportXContentType,XMessage
fromXaiogram.utils.callback_dataXimportXCallbackData
fromXbabel.datesXimportXformat_timedelta

fromXInerukiXXimportXdp
fromXInerukiX.decoratorXimportXregister
fromXInerukiX.modules.utils.connectionsXimportXchat_connection
fromXInerukiX.modules.utils.languageXimportXget_strings,Xget_strings_dec
fromXInerukiX.modules.utils.messageXimportX(
XXXXInvalidTimeUnit,
XXXXconvert_time,
XXXXget_args,
XXXXneed_args_dec,
)
fromXInerukiX.modules.utils.restrictionsXimportXban_user,Xkick_user,Xmute_user
fromXInerukiX.modules.utils.user_detailsXimportXget_user_link,Xis_user_admin
fromXInerukiX.services.mongoXimportXdb
fromXInerukiX.services.redisXimportXbredis,Xredis
fromXInerukiX.utils.cachedXimportXcached
fromXInerukiX.utils.loggerXimportXlog

cancel_stateX=XCallbackData("cancel_state",X"user_id")


classXAntiFloodConfigState(StatesGroup):
XXXXexpiration_procX=XState()


classXAntiFloodActionState(StatesGroup):
XXXXset_time_procX=XState()


@dataclass
classXCacheModel:
XXXXcount:Xint


classXAntifloodEnforcer(BaseMiddleware):
XXXXstate_cache_keyX=X"floodstate:{chat_id}"

XXXXasyncXdefXenforcer(self,Xmessage:XMessage,Xdatabase:Xdict):
XXXXXXXXifX(notX(dataX:=Xself.get_flood(message)))XorXint(
XXXXXXXXXXXXself.get_state(message)
XXXXXXXX)X!=Xmessage.from_user.id:
XXXXXXXXXXXXto_setX=XCacheModel(count=1)
XXXXXXXXXXXXself.insert_flood(to_set,Xmessage,Xdatabase)
XXXXXXXXXXXXself.set_state(message)
XXXXXXXXXXXXreturnXFalseXX#XweXaintXbanningXanybody

XXXXXXXX#XupdateXcount
XXXXXXXXdata.countX+=X1

XXXXXXXX#XcheckXexceeding
XXXXXXXXifXdata.countX>=Xdatabase["count"]:
XXXXXXXXXXXXifXawaitXself.do_action(message,Xdatabase):
XXXXXXXXXXXXXXXXself.reset_flood(message)
XXXXXXXXXXXXXXXXreturnXTrue

XXXXXXXXself.insert_flood(data,Xmessage,Xdatabase)
XXXXXXXXreturnXFalse

XXXX@classmethod
XXXXdefXis_message_valid(cls,Xmessage)X->Xbool:
XXXXXXXX_preX=X[ContentType.NEW_CHAT_MEMBERS,XContentType.LEFT_CHAT_MEMBER]
XXXXXXXXifXmessage.content_typeXinX_pre:
XXXXXXXXXXXXreturnXFalse
XXXXXXXXelifXmessage.chat.typeXinX(ChatType.PRIVATE,):
XXXXXXXXXXXXreturnXFalse
XXXXXXXXreturnXTrue

XXXXdefXget_flood(self,Xmessage)X->XOptional[CacheModel]:
XXXXXXXXifXdataX:=Xbredis.get(self.cache_key(message)):
XXXXXXXXXXXXdataX=Xpickle.loads(data)
XXXXXXXXXXXXreturnXdata
XXXXXXXXreturnXNone

XXXXdefXinsert_flood(self,Xdata:XCacheModel,Xmessage:XMessage,Xdatabase:Xdict):
XXXXXXXXexX=X(
XXXXXXXXXXXXconvert_time(database["time"])
XXXXXXXXXXXXifXdatabase.get("time",XNone)XisXnotXNone
XXXXXXXXXXXXelseXNone
XXXXXXXX)
XXXXXXXXreturnXbredis.set(self.cache_key(message),Xpickle.dumps(data),Xex=ex)

XXXXdefXreset_flood(self,Xmessage):
XXXXXXXXreturnXbredis.delete(self.cache_key(message))

XXXXdefXcheck_flood(self,Xmessage):
XXXXXXXXreturnXbredis.exists(self.cache_key(message))

XXXXdefXset_state(self,Xmessage:XMessage):
XXXXXXXXreturnXbredis.set(
XXXXXXXXXXXXself.state_cache_key.format(chat_id=message.chat.id),Xmessage.from_user.id
XXXXXXXX)

XXXXdefXget_state(self,Xmessage:XMessage):
XXXXXXXXreturnXbredis.get(self.state_cache_key.format(chat_id=message.chat.id))

XXXX@classmethod
XXXXdefXcache_key(cls,Xmessage:XMessage):
XXXXXXXXreturnXf"antiflood:{message.chat.id}:{message.from_user.id}"

XXXX@classmethod
XXXXasyncXdefXdo_action(cls,Xmessage:XMessage,Xdatabase:Xdict):
XXXXXXXXactionX=Xdatabase["action"]XifX"action"XinXdatabaseXelseX"ban"

XXXXXXXXifXactionX==X"ban":
XXXXXXXXXXXXreturnXawaitXban_user(message.chat.id,Xmessage.from_user.id)
XXXXXXXXelifXactionX==X"kick":
XXXXXXXXXXXXreturnXawaitXkick_user(message.chat.id,Xmessage.from_user.id)
XXXXXXXXelifXactionX==X"mute":
XXXXXXXXXXXXreturnXawaitXmute_user(message.chat.id,Xmessage.from_user.id)
XXXXXXXXelifXaction.startswith("t"):
XXXXXXXXXXXXtimeX=Xdatabase.get("time",XNone)
XXXXXXXXXXXXifXnotXtime:
XXXXXXXXXXXXXXXXreturnXFalse
XXXXXXXXXXXXifXactionX==X"tmute":
XXXXXXXXXXXXXXXXreturnXawaitXmute_user(
XXXXXXXXXXXXXXXXXXXXmessage.chat.id,Xmessage.from_user.id,Xuntil_date=convert_time(time)
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXelifXactionX==X"tban":
XXXXXXXXXXXXXXXXreturnXawaitXban_user(
XXXXXXXXXXXXXXXXXXXXmessage.chat.id,Xmessage.from_user.id,Xuntil_date=convert_time(time)
XXXXXXXXXXXXXXXX)
XXXXXXXXelse:
XXXXXXXXXXXXreturnXFalse

XXXXasyncXdefXon_pre_process_message(self,Xmessage:XMessage,X_):
XXXXXXXXlog.debug(
XXXXXXXXXXXXf"EnforcingXfloodXcontrolXonX{message.from_user.id}XinX{message.chat.id}"
XXXXXXXX)
XXXXXXXXifXself.is_message_valid(message):
XXXXXXXXXXXXifXawaitXis_user_admin(message.chat.id,Xmessage.from_user.id):
XXXXXXXXXXXXXXXXreturnXself.set_state(message)
XXXXXXXXXXXXifX(databaseX:=XawaitXget_data(message.chat.id))XisXNone:
XXXXXXXXXXXXXXXXreturn

XXXXXXXXXXXXifXawaitXself.enforcer(message,Xdatabase):
XXXXXXXXXXXXXXXXawaitXmessage.delete()
XXXXXXXXXXXXXXXXstringsX=XawaitXget_strings(message.chat.id,X"antiflood")
XXXXXXXXXXXXXXXXawaitXmessage.answer(
XXXXXXXXXXXXXXXXXXXXstrings["flood_exceeded"].format(
XXXXXXXXXXXXXXXXXXXXXXXXaction=(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXstrings[database["action"]]
XXXXXXXXXXXXXXXXXXXXXXXXXXXXifX"action"XinXdatabase
XXXXXXXXXXXXXXXXXXXXXXXXXXXXelseX"banned"
XXXXXXXXXXXXXXXXXXXXXXXX).capitalize(),
XXXXXXXXXXXXXXXXXXXXXXXXuser=awaitXget_user_link(message.from_user.id),
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXraiseXCancelHandler


@register(
XXXXcmds=["setflood"],Xuser_can_restrict_members=True,Xbot_can_restrict_members=True
)
@need_args_dec()
@chat_connection()
@get_strings_dec("antiflood")
asyncXdefXsetflood_command(message:XMessage,Xchat:Xdict,Xstrings:Xdict):
XXXXtry:
XXXXXXXXargsX=Xint(get_args(message)[0])
XXXXexceptXValueError:
XXXXXXXXreturnXawaitXmessage.reply(strings["invalid_args:setflood"])
XXXXifXargsX>X200:
XXXXXXXXreturnXawaitXmessage.reply(strings["overflowed_count"])

XXXXawaitXAntiFloodConfigState.expiration_proc.set()
XXXXredis.set(f"antiflood_setup:{chat['chat_id']}",Xargs)
XXXXawaitXmessage.reply(
XXXXXXXXstrings["config_proc_1"],
XXXXXXXXreply_markup=InlineKeyboardMarkup().add(
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXtext=strings["cancel"],
XXXXXXXXXXXXXXXXcallback_data=cancel_state.new(user_id=message.from_user.id),
XXXXXXXXXXXX)
XXXXXXXX),
XXXX)


@register(
XXXXstate=AntiFloodConfigState.expiration_proc,
XXXXcontent_types=ContentType.TEXT,
XXXXallow_kwargs=True,
)
@chat_connection()
@get_strings_dec("antiflood")
asyncXdefXantiflood_expire_proc(
XXXXmessage:XMessage,Xchat:Xdict,Xstrings:Xdict,Xstate,X**_
):
XXXXtry:
XXXXXXXXifX(timeX:=Xmessage.text)XnotXinX(0,X"0"):
XXXXXXXXXXXXparsed_timeX=Xconvert_time(time)XX#XjustXcallXforXmakingXsureXitsXvalid
XXXXXXXXelse:
XXXXXXXXXXXXtime,Xparsed_timeX=XNone,XNone
XXXXexceptX(TypeError,XValueError):
XXXXXXXXawaitXmessage.reply(strings["invalid_time"])
XXXXelse:
XXXXXXXXifXnotX(dataX:=Xredis.get(f'antiflood_setup:{chat["chat_id"]}')):
XXXXXXXXXXXXawaitXmessage.reply(strings["setup_corrupted"])
XXXXXXXXelse:
XXXXXXXXXXXXawaitXdb.antiflood.update_one(
XXXXXXXXXXXXXXXX{"chat_id":Xchat["chat_id"]},
XXXXXXXXXXXXXXXX{"$set":X{"time":Xtime,X"count":Xint(data)}},
XXXXXXXXXXXXXXXXupsert=True,
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXget_data.reset_cache(chat["chat_id"])
XXXXXXXXXXXXkwX=X{"count":Xdata}
XXXXXXXXXXXXifXtimeXisXnotXNone:
XXXXXXXXXXXXXXXXkw.update(
XXXXXXXXXXXXXXXXXXXX{
XXXXXXXXXXXXXXXXXXXXXXXX"time":Xformat_timedelta(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXparsed_time,Xlocale=strings["language_info"]["babel"]
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXX}
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXXXXXstrings[
XXXXXXXXXXXXXXXXXXXX"setup_success"XifXtimeXisXnotXNoneXelseX"setup_success:no_exp"
XXXXXXXXXXXXXXXX].format(**kw)
XXXXXXXXXXXX)
XXXXfinally:
XXXXXXXXawaitXstate.finish()


@register(cmds=["antiflood",X"flood"],Xis_admin=True)
@chat_connection(admin=True)
@get_strings_dec("antiflood")
asyncXdefXantiflood(message:XMessage,Xchat:Xdict,Xstrings:Xdict):
XXXXifXnotX(dataX:=XawaitXget_data(chat["chat_id"])):
XXXXXXXXreturnXawaitXmessage.reply(strings["not_configured"])

XXXXifXmessage.get_args().lower()XinX("off",X"0",X"no"):
XXXXXXXXawaitXdb.antiflood.delete_one({"chat_id":Xchat["chat_id"]})
XXXXXXXXawaitXget_data.reset_cache(chat["chat_id"])
XXXXXXXXreturnXawaitXmessage.reply(
XXXXXXXXXXXXstrings["turned_off"].format(chat_title=chat["chat_title"])
XXXXXXXX)

XXXXifXdata["time"]XisXNone:
XXXXXXXXreturnXawaitXmessage.reply(
XXXXXXXXXXXXstrings["configuration_info"].format(
XXXXXXXXXXXXXXXXaction=strings[data["action"]]XifX"action"XinXdataXelseXstrings["ban"],
XXXXXXXXXXXXXXXXcount=data["count"],
XXXXXXXXXXXX)
XXXXXXXX)
XXXXreturnXawaitXmessage.reply(
XXXXXXXXstrings["configuration_info:with_time"].format(
XXXXXXXXXXXXaction=strings[data["action"]]XifX"action"XinXdataXelseXstrings["ban"],
XXXXXXXXXXXXcount=data["count"],
XXXXXXXXXXXXtime=format_timedelta(
XXXXXXXXXXXXXXXXconvert_time(data["time"]),Xlocale=strings["language_info"]["babel"]
XXXXXXXXXXXX),
XXXXXXXX)
XXXX)


@register(cmds=["setfloodaction"],Xuser_can_restrict_members=True)
@need_args_dec()
@chat_connection(admin=True)
@get_strings_dec("antiflood")
asyncXdefXsetfloodaction(message:XMessage,Xchat:Xdict,Xstrings:Xdict):
XXXXSUPPORTED_ACTIONSX=X["kick",X"ban",X"mute",X"tmute",X"tban"]XX#Xnoqa
XXXXifX(actionX:=Xmessage.get_args().lower())XnotXinXSUPPORTED_ACTIONS:
XXXXXXXXreturnXawaitXmessage.reply(
XXXXXXXXXXXXstrings["invalid_args"].format(
XXXXXXXXXXXXXXXXsupported_actions=",X".join(SUPPORTED_ACTIONS)
XXXXXXXXXXXX)
XXXXXXXX)

XXXXifXaction.startswith("t"):
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXX"SendXaXtimeXforXtXaction",Xallow_sending_without_reply=True
XXXXXXXX)
XXXXXXXXredis.set(f"floodactionstate:{chat['chat_id']}",Xaction)
XXXXXXXXreturnXawaitXAntiFloodActionState.set_time_proc.set()

XXXXawaitXdb.antiflood.update_one(
XXXXXXXX{"chat_id":Xchat["chat_id"]},X{"$set":X{"action":Xaction}},Xupsert=True
XXXX)
XXXXawaitXget_data.reset_cache(message.chat.id)
XXXXreturnXawaitXmessage.reply(strings["setfloodaction_success"].format(action=action))


@register(
XXXXstate=AntiFloodActionState.set_time_proc,
XXXXuser_can_restrict_members=True,
XXXXallow_kwargs=True,
)
@chat_connection(admin=True)
@get_strings_dec("antiflood")
asyncXdefXset_time_config(
XXXXmessage:XMessage,Xchat:Xdict,Xstrings:Xdict,Xstate:XFSMContext,X**_
):
XXXXifXnotX(actionX:=Xredis.get(f"floodactionstate:{chat['chat_id']}")):
XXXXXXXXawaitXmessage.reply("setup_corrupted",Xallow_sending_without_reply=True)
XXXXXXXXreturnXawaitXstate.finish()
XXXXtry:
XXXXXXXXparsed_timeX=Xconvert_time(
XXXXXXXXXXXXtimeX:=Xmessage.text.lower()
XXXXXXXX)XX#XjustXcallXforXmakingXsureXitsXvalid
XXXXexceptX(TypeError,XValueError,XInvalidTimeUnit):
XXXXXXXXawaitXmessage.reply("InvalidXtime")
XXXXelse:
XXXXXXXXawaitXdb.antiflood.update_one(
XXXXXXXXXXXX{"chat_id":Xchat["chat_id"]},
XXXXXXXXXXXX{"$set":X{"action":Xaction,X"time":Xtime}},
XXXXXXXXXXXXupsert=True,
XXXXXXXX)
XXXXXXXXawaitXget_data.reset_cache(chat["chat_id"])
XXXXXXXXtextX=Xstrings["setfloodaction_success"].format(action=action)
XXXXXXXXtextX+=Xf"X({format_timedelta(parsed_time,Xlocale=strings['language_info']['babel'])})"
XXXXXXXXawaitXmessage.reply(text,Xallow_sending_without_reply=True)
XXXXfinally:
XXXXXXXXawaitXstate.finish()


asyncXdefX__before_serving__(_):
XXXXdp.middleware.setup(AntifloodEnforcer())


@register(cancel_state.filter(),Xf="cb")
asyncXdefXcancel_state_cb(event:XCallbackQuery):
XXXXawaitXevent.message.delete()


@cached()
asyncXdefXget_data(chat_id:Xint):
XXXXreturnXawaitXdb.antiflood.find_one({"chat_id":Xchat_id})


asyncXdefX__export__(chat_id:Xint):
XXXXdataX=XawaitXget_data(chat_id)
XXXXifXnotXdata:
XXXXXXXXreturn

XXXXdelXdata["_id"],Xdata["chat_id"]
XXXXreturnXdata


asyncXdefX__import__(chat_id:Xint,Xdata:Xdict):XX#Xnoqa
XXXXawaitXdb.antiflood.update_one({"chat_id":Xchat_id},X{"$set":Xdata})


__mod_name__X=X"AntiFlood"

__help__X=X"""
YouXknowXhowXsometimes,XpeopleXjoin,XsendX100Xmessages,XandXruinXyourXchat?XWithXantiflood,XthatXhappensXnoXmore!

AntifloodXallowsXyouXtoXtakeXactionXonXusersXthatXsendXmoreXthanXxXmessagesXinXaXrow.

<b>AdminsXonly:</b>
-X/antiflood:XGivesXyouXcurrentXconfigurationXofXantifloodXinXtheXchat
-X/antifloodXoff:XDisablesXAntiflood
-X/setfloodX(limit):XSetsXfloodXlimit

ReplaceX(limit)XwithXanyXinteger,XshouldXbeXlessXthanX200.XWhenXsettingXup,XInerukiXwouldXaskXyouXtoXsendXexpirationXtime,XifXyouXdontXunderstandXwhatXthisXexpirationXtimeXfor?XUserXwhoXsendsXspecifiedXlimitXofXmessagesXconsecutivelyXwithinXthisXTIME,XwouldXbeXkicked,XbannedXwhateverXtheXactionXis.XifXyouXdontXwantXthisXTIME,XwantsXtoXtakeXactionXagainstXthoseXwhoXexceedsXspecifiedXlimitXwithoutXmatteringXTIMEXINTERVALXbetweenXtheXmessages.XyouXcanXreplyXtoXquestionXwithX0

<b>ConfiguringXtheXtime:</b>
<code>2m</code>X=X2Xminutes
<code>2h</code>X=X2Xhours
<code>2d</code>X=X2Xdays

<b>Example:</b>
Me:X<code>/setfloodX10</code>
Ineruki:X<code>PleaseXsendXexpirationXtimeX[...]</code>
Me:X<code>5m</code>X(5Xminutes)
DONE!

-X/setfloodactionX(action):XSetsXtheXactionXtoXtakenXwhenXuserXexceedsXfloodXlimit

<b>CurrentlyXsupportedXactions:</b>
<code>ban</code>
<code>mute</code>
<code>kick</code>
<i>MoreXsoon™</i>
"""
