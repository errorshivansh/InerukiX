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
importXcsv
importXhtml
importXio
importXos
importXre
importXtime
importXuuid
fromXcontextlibXimportXsuppress
fromXdatetimeXimportXdatetime,Xtimedelta
fromXtypingXimportXOptional

importXbabel
importXrapidjson
fromXaiogramXimportXtypes
fromXaiogram.dispatcher.filters.stateXimportXState,XStatesGroup
fromXaiogram.typesXimportXInputFile,XMessage
fromXaiogram.types.inline_keyboardXimportXInlineKeyboardButton,XInlineKeyboardMarkup
fromXaiogram.utils.callback_dataXimportXCallbackData
fromXaiogram.utils.exceptionsXimportX(
XXXXChatNotFound,
XXXXNeedAdministratorRightsInTheChannel,
XXXXUnauthorized,
)
fromXbabel.datesXimportXformat_timedelta
fromXpymongoXimportXDeleteMany,XInsertOne

fromXInerukiXXimportXBOT_ID,XOPERATORS,XOWNER_ID,Xbot,Xdecorator
fromXInerukiX.services.mongoXimportXdb
fromXInerukiX.services.redisXimportXredis
fromXInerukiX.services.telethonXimportXtbot

fromX..utils.cachedXimportXcached
fromX.utils.connectionsXimportXchat_connection,Xget_connected_chat
fromX.utils.languageXimportXget_string,Xget_strings,Xget_strings_dec
fromX.utils.messageXimportXget_cmd,Xneed_args_dec
fromX.utils.restrictionsXimportXban_user,Xunban_user
fromX.utils.user_detailsXimportX(
XXXXcheck_admin_rights,
XXXXget_chat_dec,
XXXXget_user_and_text,
XXXXget_user_link,
XXXXis_chat_creator,
XXXXis_user_admin,
)


classXImportFbansFileWait(StatesGroup):
XXXXwaitingX=XState()


delfed_cbX=XCallbackData("delfed_cb",X"fed_id",X"creator_id")


#Xfunctions


asyncXdefXget_fed_f(message):
XXXXchatX=XawaitXget_connected_chat(message,Xadmin=True)
XXXXifX"err_msg"XnotXinXchat:
XXXXXXXXifXchat["status"]X==X"private":
XXXXXXXXXXXX#XreturnXfedXwhichXuserXisXcreated
XXXXXXXXXXXXfedX=XawaitXget_fed_by_creator(chat["chat_id"])
XXXXXXXXelse:
XXXXXXXXXXXXfedX=XawaitXdb.feds.find_one({"chats":X{"$in":X[chat["chat_id"]]}})
XXXXXXXXifXnotXfed:
XXXXXXXXXXXXreturnXFalse
XXXXXXXXreturnXfed


asyncXdefXfed_post_log(fed,Xtext):
XXXXifX"log_chat_id"XnotXinXfed:
XXXXXXXXreturn
XXXXchat_idX=Xfed["log_chat_id"]
XXXXwithXsuppress(Unauthorized,XNeedAdministratorRightsInTheChannel,XChatNotFound):
XXXXXXXXawaitXbot.send_message(chat_id,Xtext)


#Xdecorators


defXget_current_chat_fed(func):
XXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXmessageX=Xargs[0]
XXXXXXXXreal_chat_idX=Xmessage.chat.id
XXXXXXXXifXnotX(fedX:=XawaitXget_fed_f(message)):
XXXXXXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXXXXXawaitXget_string(real_chat_id,X"feds",X"chat_not_in_fed")
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn

XXXXXXXXreturnXawaitXfunc(*args,Xfed,X**kwargs)

XXXXreturnXwrapped_1


defXget_fed_user_text(skip_no_fed=False,Xself=False):
XXXXdefXwrapped(func):
XXXXXXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXXXXXfedX=XNone
XXXXXXXXXXXXmessageX=Xargs[0]
XXXXXXXXXXXXreal_chat_idX=Xmessage.chat.id
XXXXXXXXXXXXuser,XtextX=XawaitXget_user_and_text(message)
XXXXXXXXXXXXstringsX=XawaitXget_strings(real_chat_id,X"feds")

XXXXXXXXXXXX#XCheckXnonXexitsXuser
XXXXXXXXXXXXdataX=Xmessage.get_args().split("X")
XXXXXXXXXXXXifX(
XXXXXXXXXXXXXXXXnotXuser
XXXXXXXXXXXXXXXXandXlen(data)X>X0
XXXXXXXXXXXXXXXXandXdata[0].isdigit()
XXXXXXXXXXXXXXXXandXint(data[0])X<=X2147483647
XXXXXXXXXXXX):
XXXXXXXXXXXXXXXXuserX=X{"user_id":Xint(data[0])}
XXXXXXXXXXXXXXXXtextX=X"X".join(data[1:])XifXlen(data)X>X1XelseXNone
XXXXXXXXXXXXelifXnotXuser:
XXXXXXXXXXXXXXXXifXselfXisXTrue:
XXXXXXXXXXXXXXXXXXXXuserX=XawaitXdb.user_list.find_one(
XXXXXXXXXXXXXXXXXXXXXXXX{"user_id":Xmessage.from_user.id}
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXawaitXmessage.reply(strings["cant_get_user"])
XXXXXXXXXXXXXXXXXXXX#XPassingX'None'XuserXwillXthrowXerr
XXXXXXXXXXXXXXXXXXXXreturn

XXXXXXXXXXXX#XCheckXfed_idXinXargs
XXXXXXXXXXXXifXtext:
XXXXXXXXXXXXXXXXtext_argsX=Xtext.split("X",X1)
XXXXXXXXXXXXXXXXifXlen(text_args)X>=X1:
XXXXXXXXXXXXXXXXXXXXifXtext_args[0].count("-")X==X4:
XXXXXXXXXXXXXXXXXXXXXXXXtextX=Xtext_args[1]XifXlen(text_args)X>X1XelseX""
XXXXXXXXXXXXXXXXXXXXXXXXifXnotX(fedX:=XawaitXget_fed_by_id(text_args[0])):
XXXXXXXXXXXXXXXXXXXXXXXXXXXXawaitXmessage.reply(strings["fed_id_invalid"])
XXXXXXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXXXXXtextX=X"X".join(text_args)

XXXXXXXXXXXXifXnotXfed:
XXXXXXXXXXXXXXXXifXnotX(fedX:=XawaitXget_fed_f(message)):
XXXXXXXXXXXXXXXXXXXXifXnotXskip_no_fed:
XXXXXXXXXXXXXXXXXXXXXXXXawaitXmessage.reply(strings["chat_not_in_fed"])
XXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXXXXXfedX=XNone

XXXXXXXXXXXXreturnXawaitXfunc(*args,Xfed,Xuser,Xtext,X**kwargs)

XXXXXXXXreturnXwrapped_1

XXXXreturnXwrapped


defXget_fed_dec(func):
XXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXfedX=XNone
XXXXXXXXmessageX=Xargs[0]
XXXXXXXXreal_chat_idX=Xmessage.chat.id

XXXXXXXXifXmessage.text:
XXXXXXXXXXXXtext_argsX=Xmessage.text.split("X",X2)
XXXXXXXXXXXXifXnotXlen(text_args)X<X2XandXtext_args[1].count("-")X==X4:
XXXXXXXXXXXXXXXXifXnotX(fedX:=XawaitXget_fed_by_id(text_args[1])):
XXXXXXXXXXXXXXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXXXXXXXXXXXXXawaitXget_string(real_chat_id,X"feds",X"fed_id_invalid")
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXreturn

XXXXXXXX#XCheckXwhetherXfedXisXstillXNone;XThisXwillXallowXaboveXfedXvariableXtoXbeXpassed
XXXXXXXX#XTODO(BetterXhandling?)
XXXXXXXXifXfedXisXNone:
XXXXXXXXXXXXifXnotX(fedX:=XawaitXget_fed_f(message)):
XXXXXXXXXXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXXXXXXXXXawaitXget_string(real_chat_id,X"feds",X"chat_not_in_fed")
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXreturn

XXXXXXXXreturnXawaitXfunc(*args,Xfed,X**kwargs)

XXXXreturnXwrapped_1


defXis_fed_owner(func):
XXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXmessageX=Xargs[0]
XXXXXXXXfedX=Xargs[1]
XXXXXXXXuser_idX=Xmessage.from_user.id

XXXXXXXX#XcheckXonXanon
XXXXXXXXifXuser_idXinX[1087968824,X777000]:
XXXXXXXXXXXXreturn

XXXXXXXXifXnotXuser_idX==Xfed["creator"]XandXuser_idX!=XOWNER_ID:
XXXXXXXXXXXXtextX=X(awaitXget_string(message.chat.id,X"feds",X"need_fed_admin")).format(
XXXXXXXXXXXXXXXXname=html.escape(fed["fed_name"],XFalse)
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmessage.reply(text)
XXXXXXXXXXXXreturn

XXXXXXXXreturnXawaitXfunc(*args,X**kwargs)

XXXXreturnXwrapped_1


defXis_fed_admin(func):
XXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXmessageX=Xargs[0]
XXXXXXXXfedX=Xargs[1]
XXXXXXXXuser_idX=Xmessage.from_user.id

XXXXXXXX#XcheckXonXanon
XXXXXXXXifXuser_idXinX[1087968824,X777000]:
XXXXXXXXXXXXreturn

XXXXXXXXifXnotXuser_idX==Xfed["creator"]XandXuser_idX!=XOWNER_ID:
XXXXXXXXXXXXifX"admins"XnotXinXfedXorXuser_idXnotXinXfed["admins"]:
XXXXXXXXXXXXXXXXtextX=X(
XXXXXXXXXXXXXXXXXXXXawaitXget_string(message.chat.id,X"feds",X"need_fed_admin")
XXXXXXXXXXXXXXXX).format(name=html.escape(fed["fed_name"],XFalse))
XXXXXXXXXXXXXXXXreturnXawaitXmessage.reply(text)

XXXXXXXXreturnXawaitXfunc(*args,X**kwargs)

XXXXreturnXwrapped_1


#Xcmds


@decorator.register(cmds=["newfed",X"fnew"])
@need_args_dec()
@get_strings_dec("feds")
asyncXdefXnew_fed(message,Xstrings):
XXXXfed_nameX=Xhtml.escape(message.get_args())
XXXXuser_idX=Xmessage.from_user.id
XXXX#XdontXsupportXcreationXofXnewfedXasXanonXadmin
XXXXifXuser_idX==X1087968824:
XXXXXXXXreturnXawaitXmessage.reply(strings["disallow_anon"])

XXXXifXnotXfed_name:
XXXXXXXXawaitXmessage.reply(strings["no_args"])

XXXXifXlen(fed_name)X>X60:
XXXXXXXXawaitXmessage.reply(strings["fed_name_long"])
XXXXXXXXreturn

XXXXifXawaitXget_fed_by_creator(user_id)XandXnotXuser_idX==XOWNER_ID:
XXXXXXXXawaitXmessage.reply(strings["can_only_1_fed"])
XXXXXXXXreturn

XXXXifXawaitXdb.feds.find_one({"fed_name":Xfed_name}):
XXXXXXXXawaitXmessage.reply(strings["name_not_avaible"].format(name=fed_name))
XXXXXXXXreturn

XXXXdataX=X{"fed_name":Xfed_name,X"fed_id":Xstr(uuid.uuid4()),X"creator":Xuser_id}
XXXXawaitXdb.feds.insert_one(data)
XXXXawaitXget_fed_by_id.reset_cache(data["fed_id"])
XXXXawaitXget_fed_by_creator.reset_cache(data["creator"])
XXXXawaitXmessage.reply(
XXXXXXXXstrings["created_fed"].format(
XXXXXXXXXXXXname=fed_name,Xid=data["fed_id"],Xcreator=awaitXget_user_link(user_id)
XXXXXXXX)
XXXX)


@decorator.register(cmds=["joinfed",X"fjoin"])
@need_args_dec()
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("feds")
asyncXdefXjoin_fed(message,Xchat,Xstrings):
XXXXfed_idX=Xmessage.get_args().split("X")[0]
XXXXuser_idX=Xmessage.from_user.id
XXXXchat_idX=Xchat["chat_id"]

XXXXifXnotXawaitXis_chat_creator(message,Xchat_id,Xuser_id):
XXXXXXXXawaitXmessage.reply(strings["only_creators"])
XXXXXXXXreturn

XXXX#XAssumeXFedXIDXinvalid
XXXXifXnotX(fedX:=XawaitXget_fed_by_id(fed_id)):
XXXXXXXXawaitXmessage.reply(strings["fed_id_invalid"])
XXXXXXXXreturn

XXXX#XAssumeXchatXalreadyXjoinedXthis/otherXfed
XXXXifX"chats"XinXfedXandXchat_idXinXfed["chats"]:
XXXXXXXXawaitXmessage.reply(strings["joined_fed_already"])
XXXXXXXXreturn

XXXXawaitXdb.feds.update_one(
XXXXXXXX{"_id":Xfed["_id"]},X{"$addToSet":X{"chats":X{"$each":X[chat_id]}}}
XXXX)
XXXXawaitXget_fed_by_id.reset_cache(fed["fed_id"])
XXXXawaitXmessage.reply(
XXXXXXXXstrings["join_fed_success"].format(
XXXXXXXXXXXXchat=chat["chat_title"],Xfed=html.escape(fed["fed_name"],XFalse)
XXXXXXXX)
XXXX)
XXXXawaitXfed_post_log(
XXXXXXXXfed,
XXXXXXXXstrings["join_chat_fed_log"].format(
XXXXXXXXXXXXfed_name=fed["fed_name"],
XXXXXXXXXXXXfed_id=fed["fed_id"],
XXXXXXXXXXXXchat_name=chat["chat_title"],
XXXXXXXXXXXXchat_id=chat_id,
XXXXXXXX),
XXXX)


@decorator.register(cmds=["leavefed",X"fleave"])
@chat_connection(admin=True,Xonly_groups=True)
@get_current_chat_fed
@get_strings_dec("feds")
asyncXdefXleave_fed_comm(message,Xchat,Xfed,Xstrings):
XXXXuser_idX=Xmessage.from_user.id
XXXXifXnotXawaitXis_chat_creator(message,Xchat["chat_id"],Xuser_id):
XXXXXXXXawaitXmessage.reply(strings["only_creators"])
XXXXXXXXreturn

XXXXawaitXdb.feds.update_one({"_id":Xfed["_id"]},X{"$pull":X{"chats":Xchat["chat_id"]}})
XXXXawaitXget_fed_by_id.reset_cache(fed["fed_id"])
XXXXawaitXmessage.reply(
XXXXXXXXstrings["leave_fed_success"].format(
XXXXXXXXXXXXchat=chat["chat_title"],Xfed=html.escape(fed["fed_name"],XFalse)
XXXXXXXX)
XXXX)

XXXXawaitXfed_post_log(
XXXXXXXXfed,
XXXXXXXXstrings["leave_chat_fed_log"].format(
XXXXXXXXXXXXfed_name=html.escape(fed["fed_name"],XFalse),
XXXXXXXXXXXXfed_id=fed["fed_id"],
XXXXXXXXXXXXchat_name=chat["chat_title"],
XXXXXXXXXXXXchat_id=chat["chat_id"],
XXXXXXXX),
XXXX)


@decorator.register(cmds="fsub")
@need_args_dec()
@get_current_chat_fed
@is_fed_owner
@get_strings_dec("feds")
asyncXdefXfed_sub(message,Xfed,Xstrings):
XXXXfed_idX=Xmessage.get_args().split("X")[0]

XXXX#XAssumeXFedXIDXisXvalid
XXXXifXnotX(fed2X:=XawaitXget_fed_by_id(fed_id)):
XXXXXXXXawaitXmessage.reply(strings["fed_id_invalid"])
XXXXXXXXreturn

XXXX#XAssumeXchatXalreadyXjoinedXthis/otherXfed
XXXXifX"subscribed"XinXfedXandXfed_idXinXfed["subscribed"]:
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["already_subsed"].format(
XXXXXXXXXXXXXXXXname=html.escape(fed["fed_name"],XFalse),
XXXXXXXXXXXXXXXXname2=html.escape(fed2["fed_name"],XFalse),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturn

XXXXawaitXdb.feds.update_one(
XXXXXXXX{"_id":Xfed["_id"]},X{"$addToSet":X{"subscribed":X{"$each":X[fed_id]}}}
XXXX)
XXXXawaitXget_fed_by_id.reset_cache(fed["fed_id"])
XXXXawaitXmessage.reply(
XXXXXXXXstrings["subsed_success"].format(
XXXXXXXXXXXXname=html.escape(fed["fed_name"],XFalse),
XXXXXXXXXXXXname2=html.escape(fed2["fed_name"],XFalse),
XXXXXXXX)
XXXX)


@decorator.register(cmds="funsub")
@need_args_dec()
@get_current_chat_fed
@is_fed_owner
@get_strings_dec("feds")
asyncXdefXfed_unsub(message,Xfed,Xstrings):
XXXXfed_idX=Xmessage.get_args().split("X")[0]

XXXXifXnotX(fed2X:=XawaitXget_fed_by_id(fed_id)):
XXXXXXXXawaitXmessage.reply(strings["fed_id_invalid"])
XXXXXXXXreturn

XXXXifX"subscribed"XinXfedXandXfed_idXnotXinXfed["subscribed"]:
XXXXXXXXmessage.reply(
XXXXXXXXXXXXstrings["not_subsed"].format(
XXXXXXXXXXXXXXXXname=html.escape(fed["fed_name"],XFalse),Xname2=fed2["fed_name"]
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturn

XXXXawaitXdb.feds.update_one(
XXXXXXXX{"_id":Xfed["_id"]},X{"$pull":X{"subscribed":Xstr(fed_id)}}
XXXX)
XXXXawaitXget_fed_by_id.reset_cache(fed["fed_id"])
XXXXawaitXmessage.reply(
XXXXXXXXstrings["unsubsed_success"].format(
XXXXXXXXXXXXname=html.escape(fed["fed_name"],XFalse),
XXXXXXXXXXXXname2=html.escape(fed2["fed_name"],XFalse),
XXXXXXXX)
XXXX)


@decorator.register(cmds="fpromote")
@get_fed_user_text()
@is_fed_owner
@get_strings_dec("feds")
asyncXdefXpromote_to_fed(message,Xfed,Xuser,Xtext,Xstrings):
XXXXrestricted_idsX=X[1087968824,X777000]
XXXXifXuser["user_id"]XinXrestricted_ids:
XXXXXXXXreturnXawaitXmessage.reply(strings["restricted_user:promote"])
XXXXawaitXdb.feds.update_one(
XXXXXXXX{"_id":Xfed["_id"]},X{"$addToSet":X{"admins":X{"$each":X[user["user_id"]]}}}
XXXX)
XXXXawaitXget_fed_by_id.reset_cache(fed["fed_id"])
XXXXawaitXmessage.reply(
XXXXXXXXstrings["admin_added_to_fed"].format(
XXXXXXXXXXXXuser=awaitXget_user_link(user["user_id"]),
XXXXXXXXXXXXname=html.escape(fed["fed_name"],XFalse),
XXXXXXXX)
XXXX)

XXXXawaitXfed_post_log(
XXXXXXXXfed,
XXXXXXXXstrings["promote_user_fed_log"].format(
XXXXXXXXXXXXfed_name=html.escape(fed["fed_name"],XFalse),
XXXXXXXXXXXXfed_id=fed["fed_id"],
XXXXXXXXXXXXuser=awaitXget_user_link(user["user_id"]),
XXXXXXXXXXXXuser_id=user["user_id"],
XXXXXXXX),
XXXX)


@decorator.register(cmds="fdemote")
@get_fed_user_text()
@is_fed_owner
@get_strings_dec("feds")
asyncXdefXdemote_from_fed(message,Xfed,Xuser,Xtext,Xstrings):
XXXXawaitXdb.feds.update_one(
XXXXXXXX{"_id":Xfed["_id"]},X{"$pull":X{"admins":Xuser["user_id"]}}
XXXX)
XXXXawaitXget_fed_by_id.reset_cache(fed["fed_id"])

XXXXawaitXmessage.reply(
XXXXXXXXstrings["admin_demoted_from_fed"].format(
XXXXXXXXXXXXuser=awaitXget_user_link(user["user_id"]),
XXXXXXXXXXXXname=html.escape(fed["fed_name"],XFalse),
XXXXXXXX)
XXXX)

XXXXawaitXfed_post_log(
XXXXXXXXfed,
XXXXXXXXstrings["demote_user_fed_log"].format(
XXXXXXXXXXXXfed_name=html.escape(fed["fed_name"],XFalse),
XXXXXXXXXXXXfed_id=fed["fed_id"],
XXXXXXXXXXXXuser=awaitXget_user_link(user["user_id"]),
XXXXXXXXXXXXuser_id=user["user_id"],
XXXXXXXX),
XXXX)


@decorator.register(cmds=["fsetlog",X"setfedlog"],Xonly_groups=True)
@get_fed_dec
@get_chat_dec(allow_self=True,Xfed=True)
@is_fed_owner
@get_strings_dec("feds")
asyncXdefXset_fed_log_chat(message,Xfed,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]XifX"chat_id"XinXchatXelseXchat["id"]
XXXXifXchat["type"]X==X"channel":
XXXXXXXXifX(
XXXXXXXXXXXXawaitXcheck_admin_rights(message,Xchat_id,XBOT_ID,X["can_post_messages"])
XXXXXXXXXXXXisXnotXTrue
XXXXXXXX):
XXXXXXXXXXXXreturnXawaitXmessage.reply(strings["no_right_to_post"])

XXXXifX"log_chat_id"XinXfedXandXfed["log_chat_id"]:
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["already_have_chatlog"].format(
XXXXXXXXXXXXXXXXname=html.escape(fed["fed_name"],XFalse)
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturn

XXXXawaitXdb.feds.update_one({"_id":Xfed["_id"]},X{"$set":X{"log_chat_id":Xchat_id}})
XXXXawaitXget_fed_by_id.reset_cache(fed["fed_id"])

XXXXtextX=Xstrings["set_chat_log"].format(name=html.escape(fed["fed_name"],XFalse))
XXXXawaitXmessage.reply(text)

XXXX#XCurrentXfedXvariableXisXnotXupdated
XXXXawaitXfed_post_log(
XXXXXXXXawaitXget_fed_by_id(fed["fed_id"]),
XXXXXXXXstrings["set_log_fed_log"].format(
XXXXXXXXXXXXfed_name=html.escape(fed["fed_name"],XFalse),Xfed_id=fed["fed_id"]
XXXXXXXX),
XXXX)


@decorator.register(cmds=["funsetlog",X"unsetfedlog"],Xonly_groups=True)
@get_fed_dec
@is_fed_owner
@get_strings_dec("feds")
asyncXdefXunset_fed_log_chat(message,Xfed,Xstrings):
XXXXifX"log_chat_id"XnotXinXfedXorXnotXfed["log_chat_id"]:
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["already_have_chatlog"].format(
XXXXXXXXXXXXXXXXname=html.escape(fed["fed_name"],XFalse)
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturn

XXXXawaitXdb.feds.update_one({"_id":Xfed["_id"]},X{"$unset":X{"log_chat_id":X1}})
XXXXawaitXget_fed_by_id.reset_cache(fed["fed_id"])

XXXXtextX=Xstrings["logging_removed"].format(name=html.escape(fed["fed_name"],XFalse))
XXXXawaitXmessage.reply(text)

XXXXawaitXfed_post_log(
XXXXXXXXfed,
XXXXXXXXstrings["unset_log_fed_log"].format(
XXXXXXXXXXXXfed_name=html.escape(fed["fed_name"],XFalse),Xfed_id=fed["fed_id"]
XXXXXXXX),
XXXX)


@decorator.register(cmds=["fchatlist",X"fchats"])
@get_fed_dec
@is_fed_admin
@get_strings_dec("feds")
asyncXdefXfed_chat_list(message,Xfed,Xstrings):
XXXXtextX=Xstrings["chats_in_fed"].format(name=html.escape(fed["fed_name"],XFalse))
XXXXifX"chats"XnotXinXfed:
XXXXXXXXreturnXawaitXmessage.reply(
XXXXXXXXXXXXstrings["no_chats"].format(name=html.escape(fed["fed_name"],XFalse))
XXXXXXXX)

XXXXforXchat_idXinXfed["chats"]:
XXXXXXXXchatX=XawaitXdb.chat_list.find_one({"chat_id":Xchat_id})
XXXXXXXXtextX+=X"*X{}X(<code>{}</code>)\n".format(chat["chat_title"],Xchat_id)
XXXXifXlen(text)X>X4096:
XXXXXXXXawaitXmessage.answer_document(
XXXXXXXXXXXXInputFile(io.StringIO(text),Xfilename="chatlist.txt"),
XXXXXXXXXXXXstrings["too_large"],
XXXXXXXXXXXXreply=message.message_id,
XXXXXXXX)
XXXXXXXXreturn
XXXXawaitXmessage.reply(text)


@decorator.register(cmds=["fadminlist",X"fadmins"])
@get_fed_dec
@is_fed_admin
@get_strings_dec("feds")
asyncXdefXfed_admins_list(message,Xfed,Xstrings):
XXXXtextX=Xstrings["fadmins_header"].format(
XXXXXXXXfed_name=html.escape(fed["fed_name"],XFalse)
XXXX)
XXXXtextX+=X"*X{}X(<code>{}</code>)\n".format(
XXXXXXXXawaitXget_user_link(fed["creator"]),Xfed["creator"]
XXXX)
XXXXifX"admins"XinXfed:
XXXXXXXXforXuser_idXinXfed["admins"]:
XXXXXXXXXXXXtextX+=X"*X{}X(<code>{}</code>)\n".format(
XXXXXXXXXXXXXXXXawaitXget_user_link(user_id),Xuser_id
XXXXXXXXXXXX)
XXXXawaitXmessage.reply(text,Xdisable_notification=True)


@decorator.register(cmds=["finfo",X"fedinfo"])
@get_fed_dec
@get_strings_dec("feds")
asyncXdefXfed_info(message,Xfed,Xstrings):
XXXXtextX=Xstrings["finfo_text"]
XXXXbanned_numX=XawaitXdb.fed_bans.count_documents({"fed_id":Xfed["fed_id"]})
XXXXtextX=Xtext.format(
XXXXXXXXname=html.escape(fed["fed_name"],XFalse),
XXXXXXXXfed_id=fed["fed_id"],
XXXXXXXXcreator=awaitXget_user_link(fed["creator"]),
XXXXXXXXchats=len(fed["chats"]XifX"chats"XinXfedXelseX[]),
XXXXXXXXfbanned=banned_num,
XXXX)

XXXXifX"subscribed"XinXfedXandXlen(fed["subscribed"])X>X0:
XXXXXXXXtextX+=Xstrings["finfo_subs_title"]
XXXXXXXXforXsfedXinXfed["subscribed"]:
XXXXXXXXXXXXsfedX=XawaitXget_fed_by_id(sfed)
XXXXXXXXXXXXtextX+=Xf"*X{sfed['fed_name']}X(<code>{sfed['fed_id']}</code>)\n"

XXXXawaitXmessage.reply(text,Xdisable_notification=True)


asyncXdefXget_all_subs_feds_r(fed_id,Xnew):
XXXXnew.append(fed_id)

XXXXfedX=XawaitXget_fed_by_id(fed_id)
XXXXasyncXforXitemXinXdb.feds.find({"subscribed":X{"$in":X[fed["fed_id"]]}}):
XXXXXXXXifXitem["fed_id"]XinXnew:
XXXXXXXXXXXXcontinue
XXXXXXXXnewX=XawaitXget_all_subs_feds_r(item["fed_id"],Xnew)

XXXXreturnXnew


@decorator.register(cmds=["fban",X"sfban"])
@get_fed_user_text()
@is_fed_admin
@get_strings_dec("feds")
asyncXdefXfed_ban_user(message,Xfed,Xuser,Xreason,Xstrings):
XXXXuser_idX=Xuser["user_id"]

XXXX#XChecks
XXXXifXuser_idXinXOPERATORS:
XXXXXXXXawaitXmessage.reply(strings["user_wl"])
XXXXXXXXreturn

XXXXelifXuser_idX==Xmessage.from_user.id:
XXXXXXXXawaitXmessage.reply(strings["fban_self"])
XXXXXXXXreturn

XXXXelifXuser_idX==XBOT_ID:
XXXXXXXXawaitXmessage.reply(strings["fban_self"])
XXXXXXXXreturn

XXXXelifXuser_idX==Xfed["creator"]:
XXXXXXXXawaitXmessage.reply(strings["fban_creator"])
XXXXXXXXreturn

XXXXelifX"admins"XinXfedXandXuser_idXinXfed["admins"]:
XXXXXXXXawaitXmessage.reply(strings["fban_fed_admin"])
XXXXXXXXreturn

XXXXelifXdataX:=XawaitXdb.fed_bans.find_one(
XXXXXXXX{"fed_id":Xfed["fed_id"],X"user_id":Xuser_id}
XXXX):
XXXXXXXXifX"reason"XnotXinXdataXorXdata["reason"]X!=Xreason:
XXXXXXXXXXXXoperationX=X"$set"XifXreasonXelseX"$unset"
XXXXXXXXXXXXawaitXdb.fed_bans.update_one(
XXXXXXXXXXXXXXXX{"_id":Xdata["_id"]},X{operation:X{"reason":Xreason}}
XXXXXXXXXXXX)
XXXXXXXXXXXXreturnXawaitXmessage.reply(strings["update_fban"].format(reason=reason))
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["already_fbanned"].format(user=awaitXget_user_link(user_id))
XXXXXXXX)
XXXXXXXXreturn

XXXXtextX=Xstrings["fbanned_header"]
XXXXtextX+=Xstrings["fban_info"].format(
XXXXXXXXfed=html.escape(fed["fed_name"],XFalse),
XXXXXXXXfadmin=awaitXget_user_link(message.from_user.id),
XXXXXXXXuser=awaitXget_user_link(user_id),
XXXXXXXXuser_id=user["user_id"],
XXXX)
XXXXifXreason:
XXXXXXXXtextX+=Xstrings["fbanned_reason"].format(reason=reason)

XXXX#XfbanXprocessingXmsg
XXXXnumX=Xlen(fed["chats"])XifX"chats"XinXfedXelseX0
XXXXmsgX=XawaitXmessage.reply(textX+Xstrings["fbanned_process"].format(num=num))

XXXXuserX=XawaitXdb.user_list.find_one({"user_id":Xuser_id})

XXXXbanned_chatsX=X[]

XXXXifX"chats"XinXfed:
XXXXXXXXforXchat_idXinXfed["chats"]:
XXXXXXXXXXXX#XWeXnotXfoundXtheXuserXorXuserXwasn'tXdetected
XXXXXXXXXXXXifXnotXuserXorX"chats"XnotXinXuser:
XXXXXXXXXXXXXXXXcontinue

XXXXXXXXXXXXifXchat_idXinXuser["chats"]:
XXXXXXXXXXXXXXXXawaitXasyncio.sleep(0)XX#XDoXnotXslowXdownXotherXupdates
XXXXXXXXXXXXXXXXifXawaitXban_user(chat_id,Xuser_id):
XXXXXXXXXXXXXXXXXXXXbanned_chats.append(chat_id)

XXXXnewX=X{
XXXXXXXX"fed_id":Xfed["fed_id"],
XXXXXXXX"user_id":Xuser_id,
XXXXXXXX"banned_chats":Xbanned_chats,
XXXXXXXX"time":Xdatetime.now(),
XXXXXXXX"by":Xmessage.from_user.id,
XXXX}

XXXXifXreason:
XXXXXXXXnew["reason"]X=Xreason

XXXXawaitXdb.fed_bans.insert_one(new)

XXXXchannel_textX=Xstrings["fban_log_fed_log"].format(
XXXXXXXXfed_name=html.escape(fed["fed_name"],XFalse),
XXXXXXXXfed_id=fed["fed_id"],
XXXXXXXXuser=awaitXget_user_link(user_id),
XXXXXXXXuser_id=user_id,
XXXXXXXXby=awaitXget_user_link(message.from_user.id),
XXXXXXXXchat_count=len(banned_chats),
XXXXXXXXall_chats=num,
XXXX)

XXXXifXreason:
XXXXXXXXchannel_textX+=Xstrings["fban_reason_fed_log"].format(reason=reason)

XXXX#XCheckXifXsilent
XXXXsilentX=XFalse
XXXXifXget_cmd(message)X==X"sfban":
XXXXXXXXsilentX=XTrue
XXXXXXXXkeyX=X"leave_silent:"X+Xstr(message.chat.id)
XXXXXXXXredis.set(key,Xuser_id)
XXXXXXXXredis.expire(key,X30)
XXXXXXXXtextX+=Xstrings["fbanned_silence"]

XXXX#XSubsFedsXprocess
XXXXifXlen(sfeds_listX:=XawaitXget_all_subs_feds_r(fed["fed_id"],X[]))X>X1:
XXXXXXXXsfeds_list.remove(fed["fed_id"])
XXXXXXXXthis_fed_banned_countX=Xlen(banned_chats)

XXXXXXXXawaitXmsg.edit_text(
XXXXXXXXXXXXtextX+Xstrings["fbanned_subs_process"].format(feds=len(sfeds_list))
XXXXXXXX)

XXXXXXXXall_banned_chats_countX=X0
XXXXXXXXforXs_fed_idXinXsfeds_list:
XXXXXXXXXXXXifX(
XXXXXXXXXXXXXXXXawaitXdb.fed_bans.find_one({"fed_id":Xs_fed_id,X"user_id":Xuser_id})
XXXXXXXXXXXXXXXXisXnotXNone
XXXXXXXXXXXX):
XXXXXXXXXXXXXXXX#XuserXisXalreadyXbannedXinXsubscribedXfederation,Xskip
XXXXXXXXXXXXXXXXcontinue
XXXXXXXXXXXXs_fedX=XawaitXget_fed_by_id(s_fed_id)
XXXXXXXXXXXXbanned_chatsX=X[]
XXXXXXXXXXXXnewX=X{
XXXXXXXXXXXXXXXX"fed_id":Xs_fed_id,
XXXXXXXXXXXXXXXX"user_id":Xuser_id,
XXXXXXXXXXXXXXXX"banned_chats":Xbanned_chats,
XXXXXXXXXXXXXXXX"time":Xdatetime.now(),
XXXXXXXXXXXXXXXX"origin_fed":Xfed["fed_id"],
XXXXXXXXXXXXXXXX"by":Xmessage.from_user.id,
XXXXXXXXXXXX}
XXXXXXXXXXXXforXchat_idXinXs_fed["chats"]:
XXXXXXXXXXXXXXXXifXnotXuser:
XXXXXXXXXXXXXXXXXXXXcontinue

XXXXXXXXXXXXXXXXelifXchat_idX==Xuser["user_id"]:
XXXXXXXXXXXXXXXXXXXXcontinue

XXXXXXXXXXXXXXXXelifX"chats"XnotXinXuser:
XXXXXXXXXXXXXXXXXXXXcontinue

XXXXXXXXXXXXXXXXelifXchat_idXnotXinXuser["chats"]:
XXXXXXXXXXXXXXXXXXXXcontinue

XXXXXXXXXXXXXXXX#XDoXnotXslowXdownXotherXupdates
XXXXXXXXXXXXXXXXawaitXasyncio.sleep(0.2)

XXXXXXXXXXXXXXXXifXawaitXban_user(chat_id,Xuser_id):
XXXXXXXXXXXXXXXXXXXXbanned_chats.append(chat_id)
XXXXXXXXXXXXXXXXXXXXall_banned_chats_countX+=X1

XXXXXXXXXXXXXXXXXXXXifXreason:
XXXXXXXXXXXXXXXXXXXXXXXXnew["reason"]X=Xreason

XXXXXXXXXXXXawaitXdb.fed_bans.insert_one(new)

XXXXXXXXawaitXmsg.edit_text(
XXXXXXXXXXXXtext
XXXXXXXXXXXX+Xstrings["fbanned_subs_done"].format(
XXXXXXXXXXXXXXXXchats=this_fed_banned_count,
XXXXXXXXXXXXXXXXsubs_chats=all_banned_chats_count,
XXXXXXXXXXXXXXXXfeds=len(sfeds_list),
XXXXXXXXXXXX)
XXXXXXXX)

XXXXXXXXchannel_textX+=Xstrings["fban_subs_fed_log"].format(
XXXXXXXXXXXXsubs_chats=all_banned_chats_count,Xfeds=len(sfeds_list)
XXXXXXXX)

XXXXelse:
XXXXXXXXawaitXmsg.edit_text(
XXXXXXXXXXXXtextX+Xstrings["fbanned_done"].format(num=len(banned_chats))
XXXXXXXX)

XXXXawaitXfed_post_log(fed,Xchannel_text)

XXXXifXsilent:
XXXXXXXXto_delX=X[msg.message_id,Xmessage.message_id]
XXXXXXXXifX(
XXXXXXXXXXXX"reply_to_message"XinXmessage
XXXXXXXXXXXXandXmessage.reply_to_message.from_user.idX==Xuser_id
XXXXXXXX):
XXXXXXXXXXXXto_del.append(message.reply_to_message.message_id)
XXXXXXXXawaitXasyncio.sleep(5)
XXXXXXXXawaitXtbot.delete_messages(message.chat.id,Xto_del)


@decorator.register(cmds=["unfban",X"funban"])
@get_fed_user_text()
@is_fed_admin
@get_strings_dec("feds")
asyncXdefXunfed_ban_user(message,Xfed,Xuser,Xtext,Xstrings):
XXXXuser_idX=Xuser["user_id"]

XXXXifXuserX==XBOT_ID:
XXXXXXXXawaitXmessage.reply(strings["unfban_self"])
XXXXXXXXreturn

XXXXelifXnotX(
XXXXXXXXbannedX:=XawaitXdb.fed_bans.find_one(
XXXXXXXXXXXX{"fed_id":Xfed["fed_id"],X"user_id":Xuser_id}
XXXXXXXX)
XXXX):
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["user_not_fbanned"].format(user=awaitXget_user_link(user_id))
XXXXXXXX)
XXXXXXXXreturn

XXXXtextX=Xstrings["un_fbanned_header"]
XXXXtextX+=Xstrings["fban_info"].format(
XXXXXXXXfed=html.escape(fed["fed_name"],XFalse),
XXXXXXXXfadmin=awaitXget_user_link(message.from_user.id),
XXXXXXXXuser=awaitXget_user_link(user["user_id"]),
XXXXXXXXuser_id=user["user_id"],
XXXX)

XXXXbanned_chatsX=X[]
XXXXifX"banned_chats"XinXbanned:
XXXXXXXXbanned_chatsX=Xbanned["banned_chats"]

XXXX#XunfbanXprocessingXmsg
XXXXmsgX=XawaitXmessage.reply(
XXXXXXXXtextX+Xstrings["un_fbanned_process"].format(num=len(banned_chats))
XXXX)

XXXXcounterX=X0
XXXXforXchat_idXinXbanned_chats:
XXXXXXXXawaitXasyncio.sleep(0)XX#XDoXnotXslowXdownXotherXupdates
XXXXXXXXifXawaitXunban_user(chat_id,Xuser_id):
XXXXXXXXXXXXcounterX+=X1

XXXXawaitXdb.fed_bans.delete_one({"fed_id":Xfed["fed_id"],X"user_id":Xuser_id})

XXXXchannel_textX=Xstrings["un_fban_log_fed_log"].format(
XXXXXXXXfed_name=html.escape(fed["fed_name"],XFalse),
XXXXXXXXfed_id=fed["fed_id"],
XXXXXXXXuser=awaitXget_user_link(user["user_id"]),
XXXXXXXXuser_id=user["user_id"],
XXXXXXXXby=awaitXget_user_link(message.from_user.id),
XXXXXXXXchat_count=len(banned_chats),
XXXXXXXXall_chats=len(fed["chats"])XifX"chats"XinXfedXelseX0,
XXXX)

XXXX#XSubsXfeds
XXXXifXlen(sfeds_listX:=XawaitXget_all_subs_feds_r(fed["fed_id"],X[]))X>X1:
XXXXXXXXsfeds_list.remove(fed["fed_id"])
XXXXXXXXthis_fed_unbanned_countX=Xcounter

XXXXXXXXawaitXmsg.edit_text(
XXXXXXXXXXXXtextX+Xstrings["un_fbanned_subs_process"].format(feds=len(sfeds_list))
XXXXXXXX)

XXXXXXXXall_unbanned_chats_countX=X0
XXXXXXXXforXsfed_idXinXsfeds_list:
XXXXXXXXXXXX#XrevisionX19/10/2020:XunfbansXonlyXthoseXwhoXgotXbannedXbyX`this`Xfed
XXXXXXXXXXXXbanX=XawaitXdb.fed_bans.find_one(
XXXXXXXXXXXXXXXX{"fed_id":Xsfed_id,X"origin_fed":Xfed["fed_id"],X"user_id":Xuser_id}
XXXXXXXXXXXX)
XXXXXXXXXXXXifXbanXisXNone:
XXXXXXXXXXXXXXXX#XprobablyXoldXfban
XXXXXXXXXXXXXXXXbanX=XawaitXdb.fed_bans.find_one(
XXXXXXXXXXXXXXXXXXXX{"fed_id":Xsfed_id,X"user_id":Xuser_id}
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXX#XifXban['time']X>X`replaceXhereXwithXdatetimeXofXreleaseXofXv2.2`:
XXXXXXXXXXXXXXXX#XXXXcontinue
XXXXXXXXXXXXbanned_chatsX=X[]
XXXXXXXXXXXXifXbanXisXnotXNoneXandX"banned_chats"XinXban:
XXXXXXXXXXXXXXXXbanned_chatsX=Xban["banned_chats"]

XXXXXXXXXXXXforXchat_idXinXbanned_chats:
XXXXXXXXXXXXXXXXawaitXasyncio.sleep(0.2)XX#XDoXnotXslowXdownXotherXupdates
XXXXXXXXXXXXXXXXifXawaitXunban_user(chat_id,Xuser_id):
XXXXXXXXXXXXXXXXXXXXall_unbanned_chats_countX+=X1

XXXXXXXXXXXXXXXXXXXXawaitXdb.fed_bans.delete_one(
XXXXXXXXXXXXXXXXXXXXXXXX{"fed_id":Xsfed_id,X"user_id":Xuser_id}
XXXXXXXXXXXXXXXXXXXX)

XXXXXXXXawaitXmsg.edit_text(
XXXXXXXXXXXXtext
XXXXXXXXXXXX+Xstrings["un_fbanned_subs_done"].format(
XXXXXXXXXXXXXXXXchats=this_fed_unbanned_count,
XXXXXXXXXXXXXXXXsubs_chats=all_unbanned_chats_count,
XXXXXXXXXXXXXXXXfeds=len(sfeds_list),
XXXXXXXXXXXX)
XXXXXXXX)

XXXXXXXXchannel_textX+=Xstrings["fban_subs_fed_log"].format(
XXXXXXXXXXXXsubs_chats=all_unbanned_chats_count,Xfeds=len(sfeds_list)
XXXXXXXX)
XXXXelse:
XXXXXXXXawaitXmsg.edit_text(textX+Xstrings["un_fbanned_done"].format(num=counter))

XXXXawaitXfed_post_log(fed,Xchannel_text)


@decorator.register(cmds=["delfed",X"fdel"])
@get_fed_dec
@is_fed_owner
@get_strings_dec("feds")
asyncXdefXdel_fed_cmd(message,Xfed,Xstrings):
XXXXfed_nameX=Xhtml.escape(fed["fed_name"],XFalse)
XXXXfed_idX=Xfed["fed_id"]
XXXXfed_ownerX=Xfed["creator"]

XXXXbuttonsX=XInlineKeyboardMarkup()
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXtext=strings["delfed_btn_yes"],
XXXXXXXXXXXXcallback_data=delfed_cb.new(fed_id=fed_id,Xcreator_id=fed_owner),
XXXXXXXX)
XXXX)
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXtext=strings["delfed_btn_no"],Xcallback_data=f"cancel_{fed_owner}"
XXXXXXXX)
XXXX)

XXXXawaitXmessage.reply(strings["delfed"]X%Xfed_name,Xreply_markup=buttons)


@decorator.register(delfed_cb.filter(),Xf="cb",Xallow_kwargs=True)
@get_strings_dec("feds")
asyncXdefXdel_fed_func(event,Xstrings,Xcallback_data=None,X**kwargs):
XXXXfed_idX=Xcallback_data["fed_id"]
XXXXfed_ownerX=Xcallback_data["creator_id"]

XXXXifXevent.from_user.idX!=Xint(fed_owner):
XXXXXXXXreturn

XXXXawaitXdb.feds.delete_one({"fed_id":Xfed_id})
XXXXawaitXget_fed_by_id.reset_cache(fed_id)
XXXXawaitXget_fed_by_creator.reset_cache(int(fed_owner))
XXXXasyncXforXsubscribed_fedXinXdb.feds.find({"subscribed":Xfed_id}):
XXXXXXXXawaitXdb.feds.update_one(
XXXXXXXXXXXX{"_id":Xsubscribed_fed["_id"]},X{"$pull":X{"subscribed":Xfed_id}}
XXXXXXXX)
XXXXXXXXawaitXget_fed_by_id.reset_cache(subscribed_fed["fed_id"])

XXXX#XdeleteXallXfbansXofXit
XXXXawaitXdb.fed_bans.delete_many({"fed_id":Xfed_id})

XXXXawaitXevent.message.edit_text(strings["delfed_success"])


@decorator.register(regexp="cancel_(.*)",Xf="cb")
asyncXdefXcancel(event):
XXXXifXevent.from_user.idX!=Xint((re.search(r"cancel_(.*)",Xevent.data)).group(1)):
XXXXXXXXreturn
XXXXawaitXevent.message.delete()


@decorator.register(cmds="frename")
@need_args_dec()
@get_fed_dec
@is_fed_owner
@get_strings_dec("feds")
asyncXdefXfed_rename(message,Xfed,Xstrings):
XXXX#XCheckXwhetherXfirstXargXisXfedXIDX|XTODO:XRemoveXthis
XXXXargsX=Xmessage.get_args().split("X",X2)
XXXXifXlen(args)X>X1XandXargs[0].count("-")X==X4:
XXXXXXXXnew_nameX=X"X".join(args[1:])
XXXXelse:
XXXXXXXXnew_nameX=X"X".join(args[0:])

XXXXifXnew_nameX==Xfed["fed_name"]:
XXXXXXXXawaitXmessage.reply(strings["frename_same_name"])
XXXXXXXXreturn

XXXXawaitXdb.feds.update_one({"_id":Xfed["_id"]},X{"$set":X{"fed_name":Xnew_name}})
XXXXawaitXget_fed_by_id.reset_cache(fed["fed_id"])
XXXXawaitXmessage.reply(
XXXXXXXXstrings["frename_success"].format(
XXXXXXXXXXXXold_name=html.escape(fed["fed_name"],XFalse),
XXXXXXXXXXXXnew_name=html.escape(new_name,XFalse),
XXXXXXXX)
XXXX)


@decorator.register(cmds=["fbanlist",X"exportfbans",X"fexport"])
@get_fed_dec
@is_fed_admin
@get_strings_dec("feds")
asyncXdefXfban_export(message,Xfed,Xstrings):
XXXXfed_idX=Xfed["fed_id"]
XXXXkeyX=X"fbanlist_lock:"X+Xstr(fed_id)
XXXXifXredis.get(key)XandXmessage.from_user.idXnotXinXOPERATORS:
XXXXXXXXttlX=Xformat_timedelta(
XXXXXXXXXXXXtimedelta(seconds=redis.ttl(key)),Xstrings["language_info"]["babel"]
XXXXXXXX)
XXXXXXXXawaitXmessage.reply(strings["fbanlist_locked"]X%Xttl)
XXXXXXXXreturn

XXXXredis.set(key,X1)
XXXXredis.expire(key,X600)

XXXXmsgX=XawaitXmessage.reply(strings["creating_fbanlist"])
XXXXfieldsX=X["user_id",X"reason",X"by",X"time",X"banned_chats"]
XXXXwithXio.StringIO()XasXf:
XXXXXXXXwriterX=Xcsv.DictWriter(f,Xfields)
XXXXXXXXwriter.writeheader()
XXXXXXXXasyncXforXbanned_dataXinXdb.fed_bans.find({"fed_id":Xfed_id}):
XXXXXXXXXXXXawaitXasyncio.sleep(0)

XXXXXXXXXXXXdataX=X{"user_id":Xbanned_data["user_id"]}

XXXXXXXXXXXXifX"reason"XinXbanned_data:
XXXXXXXXXXXXXXXXdata["reason"]X=Xbanned_data["reason"]

XXXXXXXXXXXXifX"time"XinXbanned_data:
XXXXXXXXXXXXXXXXdata["time"]X=Xint(time.mktime(banned_data["time"].timetuple()))

XXXXXXXXXXXXifX"by"XinXbanned_data:
XXXXXXXXXXXXXXXXdata["by"]X=Xbanned_data["by"]

XXXXXXXXXXXXifX"banned_chats"XinXbanned_data:
XXXXXXXXXXXXXXXXdata["banned_chats"]X=Xbanned_data["banned_chats"]

XXXXXXXXXXXXwriter.writerow(data)

XXXXXXXXtextX=Xstrings["fbanlist_done"]X%Xhtml.escape(fed["fed_name"],XFalse)
XXXXXXXXf.seek(0)
XXXXXXXXawaitXmessage.answer_document(InputFile(f,Xfilename="fban_export.csv"),Xtext)
XXXXawaitXmsg.delete()


@decorator.register(cmds=["importfbans",X"fimport"])
@get_fed_dec
@is_fed_admin
@get_strings_dec("feds")
asyncXdefXimportfbans_cmd(message,Xfed,Xstrings):
XXXXfed_idX=Xfed["fed_id"]
XXXXkeyX=X"importfbans_lock:"X+Xstr(fed_id)
XXXXifXredis.get(key)XandXmessage.from_user.idXnotXinXOPERATORS:
XXXXXXXXttlX=Xformat_timedelta(
XXXXXXXXXXXXtimedelta(seconds=redis.ttl(key)),Xstrings["language_info"]["babel"]
XXXXXXXX)
XXXXXXXXawaitXmessage.reply(strings["importfbans_locked"]X%Xttl)
XXXXXXXXreturn

XXXXredis.set(key,X1)
XXXXredis.expire(key,X600)

XXXXifX"document"XinXmessage:
XXXXXXXXdocumentX=Xmessage.document
XXXXelse:
XXXXXXXXifX"reply_to_message"XnotXinXmessage:
XXXXXXXXXXXXawaitXImportFbansFileWait.waiting.set()
XXXXXXXXXXXXawaitXmessage.reply(strings["send_import_file"])
XXXXXXXXXXXXreturn

XXXXXXXXelifX"document"XnotXinXmessage.reply_to_message:
XXXXXXXXXXXXawaitXmessage.reply(strings["rpl_to_file"])
XXXXXXXXXXXXreturn
XXXXXXXXdocumentX=Xmessage.reply_to_message.document

XXXXawaitXimportfbans_func(message,Xfed,Xdocument=document)


@get_strings_dec("feds")
asyncXdefXimportfbans_func(message,Xfed,Xstrings,Xdocument=None):
XXXXglobalXuser_id
XXXXfile_typeX=Xos.path.splitext(document["file_name"])[1][1:]

XXXXifXfile_typeX==X"json":
XXXXXXXXifXdocument["file_size"]X>X1000000:
XXXXXXXXXXXXawaitXmessage.reply(strings["big_file_json"].format(num="1"))
XXXXXXXXXXXXreturn
XXXXelifXfile_typeX==X"csv":
XXXXXXXXifXdocument["file_size"]X>X52428800:
XXXXXXXXXXXXawaitXmessage.reply(strings["big_file_csv"].format(num="50"))
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXawaitXmessage.reply(strings["wrong_file_ext"])
XXXXXXXXreturn

XXXXfX=XawaitXbot.download_file_by_id(document.file_id,Xio.BytesIO())
XXXXmsgX=XawaitXmessage.reply(strings["importing_process"])

XXXXdataX=XNone
XXXXifXfile_typeX==X"json":
XXXXXXXXtry:
XXXXXXXXXXXXdataX=Xrapidjson.load(f).items()
XXXXXXXXexceptXValueError:
XXXXXXXXXXXXreturnXawaitXmessage.reply(strings["invalid_file"])
XXXXelifXfile_typeX==X"csv":
XXXXXXXXdataX=Xcsv.DictReader(io.TextIOWrapper(f))

XXXXreal_counterX=X0

XXXXqueue_delX=X[]
XXXXqueue_insertX=X[]
XXXXcurrent_timeX=Xdatetime.now()
XXXXforXrowXinXdata:
XXXXXXXXifXfile_typeX==X"json":
XXXXXXXXXXXXuser_idX=Xrow[0]
XXXXXXXXXXXXdataX=Xrow[1]
XXXXXXXXelifXfile_typeX==X"csv":
XXXXXXXXXXXXifX"user_id"XinXrow:
XXXXXXXXXXXXXXXXuser_idX=Xint(row["user_id"])
XXXXXXXXXXXXelifX"id"XinXrow:
XXXXXXXXXXXXXXXXuser_idX=Xint(row["id"])
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXcontinue
XXXXXXXXelse:
XXXXXXXXXXXXraiseXNotImplementedError

XXXXXXXXnewX=X{"fed_id":Xfed["fed_id"],X"user_id":Xuser_id}

XXXXXXXXifX"reason"XinXrow:
XXXXXXXXXXXXnew["reason"]X=Xrow["reason"]

XXXXXXXXifX"by"XinXrow:
XXXXXXXXXXXXnew["by"]X=Xint(row["by"])
XXXXXXXXelse:
XXXXXXXXXXXXnew["by"]X=Xmessage.from_user.id

XXXXXXXXifX"time"XinXrow:
XXXXXXXXXXXXnew["time"]X=Xdatetime.fromtimestamp(int(row["time"]))
XXXXXXXXelse:
XXXXXXXXXXXXnew["time"]X=Xcurrent_time

XXXXXXXXifX"banned_chats"XinXrowXandXtype(row["banned_chats"])XisXlist:
XXXXXXXXXXXXnew["banned_chats"]X=Xrow["banned_chats"]

XXXXXXXXqueue_del.append(DeleteMany({"fed_id":Xfed["fed_id"],X"user_id":Xuser_id}))
XXXXXXXXqueue_insert.append(InsertOne(new))

XXXXXXXXifXlen(queue_insert)X==X1000:
XXXXXXXXXXXXreal_counterX+=Xlen(queue_insert)

XXXXXXXXXXXX#XMakeXdeleteXoperationXorderedXbeforeXinserting.
XXXXXXXXXXXXifXqueue_del:
XXXXXXXXXXXXXXXXawaitXdb.fed_bans.bulk_write(queue_del,Xordered=False)
XXXXXXXXXXXXawaitXdb.fed_bans.bulk_write(queue_insert,Xordered=False)

XXXXXXXXXXXXqueue_delX=X[]
XXXXXXXXXXXXqueue_insertX=X[]

XXXX#XProcessXlastXbans
XXXXreal_counterX+=Xlen(queue_insert)
XXXXifXqueue_del:
XXXXXXXXawaitXdb.fed_bans.bulk_write(queue_del,Xordered=False)
XXXXifXqueue_insert:
XXXXXXXXawaitXdb.fed_bans.bulk_write(queue_insert,Xordered=False)

XXXXawaitXmsg.edit_text(strings["import_done"].format(num=real_counter))


@decorator.register(
XXXXstate=ImportFbansFileWait.waiting,
XXXXcontent_types=types.ContentTypes.DOCUMENT,
XXXXallow_kwargs=True,
)
@get_fed_dec
@is_fed_admin
asyncXdefXimport_state(message,Xfed,Xstate=None,X**kwargs):
XXXXawaitXimportfbans_func(message,Xfed,Xdocument=message.document)
XXXXawaitXstate.finish()


@decorator.register(only_groups=True)
@chat_connection(only_groups=True)
@get_strings_dec("feds")
asyncXdefXcheck_fbanned(message:XMessage,Xchat,Xstrings):
XXXXifXmessage.sender_chat:
XXXXXXXX#XshouldXbeXchannel/anon
XXXXXXXXreturn

XXXXuser_idX=Xmessage.from_user.id
XXXXchat_idX=Xchat["chat_id"]

XXXXifXnotX(fedX:=XawaitXget_fed_f(message)):
XXXXXXXXreturn

XXXXelifXawaitXis_user_admin(chat_id,Xuser_id):
XXXXXXXXreturn

XXXXfeds_listX=X[fed["fed_id"]]

XXXXifX"subscribed"XinXfed:
XXXXXXXXfeds_list.extend(fed["subscribed"])

XXXXifXbanX:=XawaitXdb.fed_bans.find_one(
XXXXXXXX{"fed_id":X{"$in":Xfeds_list},X"user_id":Xuser_id}
XXXX):

XXXXXXXX#XcheckXwhetherXbannedXfed_idXisXchat'sXfedXidXelse
XXXXXXXX#XuserXisXbannedXinXsubXfed
XXXXXXXXifXfed["fed_id"]X==Xban["fed_id"]XandX"origin_fed"XnotXinXban:
XXXXXXXXXXXXtextX=Xstrings["automatic_ban"].format(
XXXXXXXXXXXXXXXXuser=awaitXget_user_link(user_id),
XXXXXXXXXXXXXXXXfed_name=html.escape(fed["fed_name"],XFalse),
XXXXXXXXXXXX)
XXXXXXXXelse:
XXXXXXXXXXXXs_fedX=XawaitXget_fed_by_id(
XXXXXXXXXXXXXXXXban["fed_id"]XifX"origin_fed"XnotXinXbanXelseXban["origin_fed"]
XXXXXXXXXXXX)
XXXXXXXXXXXXifXs_fedXisXNone:
XXXXXXXXXXXXXXXXreturn

XXXXXXXXXXXXtextX=Xstrings["automatic_ban_sfed"].format(
XXXXXXXXXXXXXXXXuser=awaitXget_user_link(user_id),Xfed_name=s_fed["fed_name"]
XXXXXXXXXXXX)

XXXXXXXXifX"reason"XinXban:
XXXXXXXXXXXXtextX+=Xstrings["automatic_ban_reason"].format(text=ban["reason"])

XXXXXXXXifXnotXawaitXban_user(chat_id,Xuser_id):
XXXXXXXXXXXXreturn

XXXXXXXXawaitXmessage.reply(text)

XXXXXXXXawaitXdb.fed_bans.update_one(
XXXXXXXXXXXX{"_id":Xban["_id"]},X{"$addToSet":X{"banned_chats":Xchat_id}}
XXXXXXXX)


@decorator.register(cmds=["fcheck",X"fbanstat"])
@get_fed_user_text(skip_no_fed=True,Xself=True)
@get_strings_dec("feds")
asyncXdefXfedban_check(message,Xfed,Xuser,X_,Xstrings):
XXXXfbanned_fedX=XFalseXX#XAXvariableXtoXfindXifXuserXisXbannedXinXcurrentXfedXofXchat
XXXXfban_dataX=XNone

XXXXtotal_countX=XawaitXdb.fed_bans.count_documents({"user_id":Xuser["user_id"]})
XXXXifXfed:
XXXXXXXXfed_listX=X[fed["fed_id"]]
XXXXXXXX#XcheckXfbannedXinXsubscribed
XXXXXXXXifX"subscribed"XinXfed:
XXXXXXXXXXXXfed_list.extend(fed["subscribed"])

XXXXXXXXifXfban_dataX:=XawaitXdb.fed_bans.find_one(
XXXXXXXXXXXX{"user_id":Xuser["user_id"],X"fed_id":X{"$in":Xfed_list}}
XXXXXXXX):
XXXXXXXXXXXXfbanned_fedX=XTrue

XXXXXXXXXXXX#Xre-assignXfedXifXuserXisXbannedXinXsub-fed
XXXXXXXXXXXXifXfban_data["fed_id"]X!=Xfed["fed_id"]XorX"origin_fed"XinXfban_data:
XXXXXXXXXXXXXXXXfedX=XawaitXget_fed_by_id(
XXXXXXXXXXXXXXXXXXXXfban_data[
XXXXXXXXXXXXXXXXXXXXXXXX"fed_id"XifX"origin_fed"XnotXinXfban_dataXelseX"origin_fed"
XXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXX)

XXXX#XcreateXtext
XXXXtextX=Xstrings["fcheck_header"]
XXXXifXmessage.chat.typeX==X"private"XandXmessage.from_user.idX==Xuser["user_id"]:
XXXXXXXXifXbool(fed):
XXXXXXXXXXXXifXbool(fban_data):
XXXXXXXXXXXXXXXXifX"reason"XnotXinXfban_data:
XXXXXXXXXXXXXXXXXXXXtextX+=Xstrings["fban_info:fcheck"].format(
XXXXXXXXXXXXXXXXXXXXXXXXfed=html.escape(fed["fed_name"],XFalse),
XXXXXXXXXXXXXXXXXXXXXXXXdate=babel.dates.format_date(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXfban_data["time"],
XXXXXXXXXXXXXXXXXXXXXXXXXXXX"long",
XXXXXXXXXXXXXXXXXXXXXXXXXXXXlocale=strings["language_info"]["babel"],
XXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXtextX+=Xstrings["fban_info:fcheck:reason"].format(
XXXXXXXXXXXXXXXXXXXXXXXXfed=html.escape(fed["fed_name"],XFalse),
XXXXXXXXXXXXXXXXXXXXXXXXdate=babel.dates.format_date(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXfban_data["time"],
XXXXXXXXXXXXXXXXXXXXXXXXXXXX"long",
XXXXXXXXXXXXXXXXXXXXXXXXXXXXlocale=strings["language_info"]["babel"],
XXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXXreason=fban_data["reason"],
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXreturnXawaitXmessage.reply(strings["didnt_fbanned"])
XXXXXXXXelse:
XXXXXXXXXXXXtextX+=Xstrings["fbanned_count_pm"].format(count=total_count)
XXXXXXXXXXXXifXtotal_countX>X0:
XXXXXXXXXXXXXXXXcountX=X0
XXXXXXXXXXXXXXXXasyncXforXfbanXinXdb.fed_bans.find({"user_id":Xuser["user_id"]}):
XXXXXXXXXXXXXXXXXXXXcountX+=X1
XXXXXXXXXXXXXXXXXXXX_fedX=XawaitXget_fed_by_id(fban["fed_id"])
XXXXXXXXXXXXXXXXXXXXifX_fed:
XXXXXXXXXXXXXXXXXXXXXXXXfed_nameX=X_fed["fed_name"]
XXXXXXXXXXXXXXXXXXXXXXXXtextX+=Xf'{count}:X<code>{fban["fed_id"]}</code>:X{fed_name}\n'
XXXXelse:
XXXXXXXXifXtotal_countX>X0:
XXXXXXXXXXXXtextX+=Xstrings["fbanned_data"].format(
XXXXXXXXXXXXXXXXuser=awaitXget_user_link(user["user_id"]),Xcount=total_count
XXXXXXXXXXXX)
XXXXXXXXelse:
XXXXXXXXXXXXtextX+=Xstrings["fbanned_nowhere"].format(
XXXXXXXXXXXXXXXXuser=awaitXget_user_link(user["user_id"])
XXXXXXXXXXXX)

XXXXXXXXifXfbanned_fedXisXTrue:
XXXXXXXXXXXXifX"reason"XinXfban_data:
XXXXXXXXXXXXXXXXtextX+=Xstrings["fbanned_in_fed:reason"].format(
XXXXXXXXXXXXXXXXXXXXfed=html.escape(fed["fed_name"],XFalse),Xreason=fban_data["reason"]
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXtextX+=Xstrings["fbanned_in_fed"].format(
XXXXXXXXXXXXXXXXXXXXfed=html.escape(fed["fed_name"],XFalse)
XXXXXXXXXXXXXXXX)
XXXXXXXXelifXfedXisXnotXNone:
XXXXXXXXXXXXtextX+=Xstrings["not_fbanned_in_fed"].format(
XXXXXXXXXXXXXXXXfed_name=html.escape(fed["fed_name"],Xquote=False)
XXXXXXXXXXXX)

XXXXXXXXifXtotal_countX>X0:
XXXXXXXXXXXXifXmessage.from_user.idX==Xuser["user_id"]:
XXXXXXXXXXXXXXXXtextX+=Xstrings["contact_in_pm"]
XXXXifXlen(text)X>X4096:
XXXXXXXXreturnXawaitXmessage.answer_document(
XXXXXXXXXXXXInputFile(io.StringIO(text),Xfilename="fban_info.txt"),
XXXXXXXXXXXXstrings["too_long_fbaninfo"],
XXXXXXXXXXXXreply=message.message_id,
XXXXXXXX)
XXXXawaitXmessage.reply(text)


@cached()
asyncXdefXget_fed_by_id(fed_id:Xstr)X->XOptional[dict]:
XXXXreturnXawaitXdb.feds.find_one({"fed_id":Xfed_id})


@cached()
asyncXdefXget_fed_by_creator(creator:Xint)X->XOptional[dict]:
XXXXreturnXawaitXdb.feds.find_one({"creator":Xcreator})


asyncXdefX__export__(chat_id):
XXXXifXchat_fedX:=XawaitXdb.feds.find_one({"chats":X[chat_id]}):
XXXXXXXXreturnX{"feds":X{"fed_id":Xchat_fed["fed_id"]}}


asyncXdefX__import__(chat_id,Xdata):
XXXXifXfed_idX:=Xdata["fed_id"]:
XXXXXXXXifXcurrent_fedX:=XawaitXdb.feds.find_one({"chats":X[int(chat_id)]}):
XXXXXXXXXXXXawaitXdb.feds.update_one(
XXXXXXXXXXXXXXXX{"_id":Xcurrent_fed["_id"]},X{"$pull":X{"chats":Xchat_id}}
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXget_fed_by_id.reset_cache(current_fed["fed_id"])
XXXXXXXXawaitXdb.feds.update_one({"fed_id":Xfed_id},X{"$addToSet":X{"chats":Xchat_id}})
XXXXXXXXawaitXget_fed_by_id.reset_cache(fed_id)


__mod_name__X=X"Federations"

__help__X=X"""
WellXbasicallyXthereXisX2XreasonsXtoXuseXFederations:
1.XYouXhaveXmanyXchatsXandXwantXtoXbanXusersXinXallXofXthemXwithX1Xcommand
2.XYouXwantXtoXsubscribeXtoXanyXofXtheXantispamXFederationsXtoXhaveXyourXchat(s)Xprotected.
InXbothXcasesXInerukiXwillXhelpXyou.
<b>ArgumentsXtypesXhelp:</b>
<code>()</code>:XrequiredXargument
<code>(user)</code>:XrequiredXbutXyouXcanXreplyXonXanyXuser'sXmessageXinstead
<code>(file)</code>:XrequiredXfile,XifXfileXisn'tXprovidedXyouXwillXbeXenteredXinXfileXstate,XthisXmeansXInerukiXwillXwaitXfileXmessageXfromXyou.XTypeX/cancelXtoXleaveXfromXit.
<code>(?X)</code>:XadditionalXargument
<b>OnlyXFederationXowner:</b>
-X/fnewX(name)XorX/newfedX(name):XCreatesXaXnewXFederation
-X/frenameX(?FedXID)X(newXname):XRenamesXyourXfederation
-X/fdelX(?FedXID)XorX/delfedX(?FedXID):XRemovesXyourXFederation
-X/fpromoteX(user)X(?FedXID):XPromotesXaXuserXtoXtheXyourXFederation
-X/fdemoteX(user)X(?FedXID):XDemotesXaXuserXfromXtheXyourXFederation
-X/fsubX(FedXID):XSubscibesXyourXFederationXoverXprovided
-X/funsubX(FedXID):XunsubscibesXyourXFederationXfromXprovided
-X/fsetlogX(?XFedXID)X(?Xchat/channelXid)XorX/setfedlogX(?XFedXID)X(?Xchat/channelXid):XSet'sXaXlogXchat/channelXforXyourXFederation
-X/funsetlogX(?FedXID)XorX/unsetfedlogX(?FedXID):XUnsetsXaXFederationXlogXchat\channel
-X/fexportX(?FedXID):XExportsXFederationXbans
-X/fimportX(?FedXID)X(file):XImportsXFederationXbans
<b>OnlyXChatXowner:</b>
-X/fjoinX(FedXID)XorX/joinfedX(FedXID):XJoinsXcurrentXchatXtoXprovidedXFederation
-X/fleaveXorX/leavefed:XLeavesXcurrentXchatXfromXtheXfed
<b>AvaibleXforXFederationXadminsXandXowners:</b>
-X/fchatlistX(?FedXID)XorX/fchatsX(?FedXID):XShowsXaXlistXofXchatsXinXtheXyourXFederationXlist
-X/fbanX(user)X(?FedXID)X(?reason):XBansXuserXinXtheXFedXandXFedsXwhichXsubscribedXonXthisXFed
-X/sfbanX(user)X(?FedXID)X(?reason):XAsXabove,XbutXsilentlyX-XmeansXtheXmessagesXaboutXfbanningXandXrepliedXmessageX(ifXwasXprovided)XwillXbeXremoved
-X/unfbanX(user)X(?FedXID)X(?reason):XUnbansXaXuserXfromXaXFederation
<b>AvaibleXforXallXusers:</b>
-X/fcheckX(?user):XCheckXuser'sXfederationXbanXinfo
-X/finfoX(?FedXID):XInfoXaboutXFederation
"""
