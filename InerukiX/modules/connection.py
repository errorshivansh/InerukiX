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

importXre

fromXaiogram.dispatcher.filters.builtinXimportXCommandStart
fromXaiogram.typesXimportXCallbackQuery
fromXaiogram.types.inline_keyboardXimportXInlineKeyboardButton,XInlineKeyboardMarkup
fromXaiogram.utils.callback_dataXimportXCallbackData
fromXaiogram.utils.deep_linkingXimportXget_start_link
fromXaiogram.utils.exceptionsXimportXBotBlocked,XCantInitiateConversation

fromXInerukiXXimportXbot
fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.mongoXimportXdb
fromXInerukiX.services.redisXimportXredis

fromX.utils.connectionsXimportXchat_connection,Xget_connection_data,Xset_connected_chat
fromX.utils.languageXimportXget_strings_dec
fromX.utils.messageXimportXget_arg
fromX.utils.notesXimportXBUTTONS
fromX.utils.user_detailsXimportXget_chat_dec,Xis_user_admin

connect_to_chat_cbX=XCallbackData("connect_to_chat_cb",X"chat_id")


@get_strings_dec("connections")
asyncXdefXdef_connect_chat(message,Xuser_id,Xchat_id,Xchat_title,Xstrings,Xedit=False):
XXXXawaitXset_connected_chat(user_id,Xchat_id)

XXXXtextX=Xstrings["pm_connected"].format(chat_name=chat_title)
XXXXifXedit:
XXXXXXXXawaitXmessage.edit_text(text)
XXXXelse:
XXXXXXXXawaitXmessage.reply(text)


#XInXchatX-XconnectXdirectlyXtoXchat
@register(cmds="connect",Xonly_groups=True,Xno_args=True)
@get_strings_dec("connections")
asyncXdefXconnect_to_chat_direct(message,Xstrings):
XXXXuser_idX=Xmessage.from_user.id
XXXXchat_idX=Xmessage.chat.id

XXXXifXuser_idX==X1087968824:
XXXXXXXX#XjustXwarnXtheXuserXthatXconnectionsXwithXadminXrightsXdoesn'tXwork
XXXXXXXXreturnXawaitXmessage.reply(
XXXXXXXXXXXXstrings["anon_admin_conn"],
XXXXXXXXXXXXreply_markup=InlineKeyboardMarkup().add(
XXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXstrings["click_here"],Xcallback_data="anon_conn_cb"
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXX),
XXXXXXXX)

XXXXchatX=XawaitXdb.chat_list.find_one({"chat_id":Xchat_id})
XXXXchat_titleX=Xchat["chat_title"]XifXchatXisXnotXNoneXelseXmessage.chat.title
XXXXtextX=Xstrings["pm_connected"].format(chat_name=chat_title)

XXXXtry:
XXXXXXXXawaitXbot.send_message(user_id,Xtext)
XXXXXXXXawaitXdef_connect_chat(message,Xuser_id,Xchat_id,Xchat_title)
XXXXexceptX(BotBlocked,XCantInitiateConversation):
XXXXXXXXawaitXmessage.reply(strings["connected_pm_to_me"].format(chat_name=chat_title))
XXXXXXXXredis.set("InerukiX_connected_start_state:"X+Xstr(user_id),X1)


#XInXpmXwithoutXargsX-XshowXlastXconnectedXchats
@register(cmds="connect",Xno_args=True,Xonly_pm=True)
@get_strings_dec("connections")
@chat_connection()
asyncXdefXconnect_chat_keyboard(message,Xstrings,Xchat):
XXXXconnected_dataX=XawaitXget_connection_data(message.from_user.id)
XXXXifXnotXconnected_data:
XXXXXXXXreturnXawaitXmessage.reply(strings["u_wasnt_connected"])

XXXXifXchat["status"]X!=X"private":
XXXXXXXXtextX=Xstrings["connected_chat"].format(chat_name=chat["chat_title"])
XXXXelifX"command"XinXconnected_data:
XXXXXXXXifXchatX:=XawaitXdb.chat_list.find_one({"chat_id":Xconnected_data["chat_id"]}):
XXXXXXXXXXXXchat_titleX=Xchat["chat_title"]
XXXXXXXXelse:
XXXXXXXXXXXXchat_titleX=Xconnected_data["chat_id"]
XXXXXXXXtextX=Xstrings["connected_chat:cmds"].format(
XXXXXXXXXXXXchat_name=chat_title,
XXXXXXXXXXXX#XdisconnectXisXbuiltinXcommand,XshouldXnotXbeXshown
XXXXXXXXXXXXcommands=",X".join(
XXXXXXXXXXXXXXXXf"<code>/{cmd}</code>"
XXXXXXXXXXXXXXXXforXcmdXinXconnected_data["command"]
XXXXXXXXXXXXXXXXifXcmdX!=X"disconnect"
XXXXXXXXXXXX),
XXXXXXXX)
XXXXelse:
XXXXXXXXtextX=X""

XXXXtextX+=Xstrings["select_chat_to_connect"]
XXXXmarkupX=XInlineKeyboardMarkup(row_width=1)
XXXXforXchat_idXinXreversed(connected_data["history"][-3:]):
XXXXXXXXchatX=XawaitXdb.chat_list.find_one({"chat_id":Xchat_id})
XXXXXXXXmarkup.insert(
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXchat["chat_title"],
XXXXXXXXXXXXXXXXcallback_data=connect_to_chat_cb.new(chat_id=chat_id),
XXXXXXXXXXXX)
XXXXXXXX)

XXXXawaitXmessage.reply(text,Xreply_markup=markup)


#XCallbackXforXprev.Xfunction
@register(connect_to_chat_cb.filter(),Xf="cb",Xallow_kwargs=True)
asyncXdefXconnect_chat_keyboard_cb(message,Xcallback_data=False,X**kwargs):
XXXXchat_idX=Xint(callback_data["chat_id"])
XXXXchatX=XawaitXdb.chat_list.find_one({"chat_id":Xchat_id})
XXXXawaitXdef_connect_chat(
XXXXXXXXmessage.message,Xmessage.from_user.id,Xchat_id,Xchat["chat_title"],Xedit=True
XXXX)


#XInXpmXwithXargsX-XconnectXtoXchatXbyXarg
@register(cmds="connect",Xhas_args=True,Xonly_pm=True)
@get_chat_dec()
@get_strings_dec("connections")
asyncXdefXconnect_to_chat_from_arg(message,Xchat,Xstrings):
XXXXuser_idX=Xmessage.from_user.id
XXXXchat_idX=Xchat["chat_id"]

XXXXargX=Xget_arg(message)
XXXXifXarg.startswith("-"):
XXXXXXXXchat_idX=Xint(arg)

XXXXifXnotXchat_id:
XXXXXXXXawaitXmessage.reply(strings["cant_find_chat_use_id"])
XXXXXXXXreturn

XXXXawaitXdef_connect_chat(message,Xuser_id,Xchat_id,Xchat["chat_title"])


@register(cmds="disconnect",Xonly_pm=True)
@get_strings_dec("connections")
asyncXdefXdisconnect_from_chat_direct(message,Xstrings):
XXXXifX(dataX:=XawaitXget_connection_data(message.from_user.id))XandX"chat_id"XinXdata:
XXXXXXXXchatX=XawaitXdb.chat_list.find_one({"chat_id":Xdata["chat_id"]})
XXXXXXXXuser_idX=Xmessage.from_user.id
XXXXXXXXawaitXset_connected_chat(user_id,XNone)
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["disconnected"].format(chat_name=chat["chat_title"])
XXXXXXXX)


@register(cmds="allowusersconnect")
@get_strings_dec("connections")
@chat_connection(admin=True,Xonly_groups=True)
asyncXdefXallow_users_to_connect(message,Xstrings,Xchat):
XXXXchat_idX=Xchat["chat_id"]
XXXXargX=Xget_arg(message).lower()
XXXXifXnotXarg:
XXXXXXXXstatusX=Xstrings["enabled"]
XXXXXXXXdataX=XawaitXdb.chat_connection_settings.find_one({"chat_id":Xchat_id})
XXXXXXXXifX(
XXXXXXXXXXXXdata
XXXXXXXXXXXXandX"allow_users_connect"XinXdata
XXXXXXXXXXXXandXdata["allow_users_connect"]XisXFalse
XXXXXXXX):
XXXXXXXXXXXXstatusX=Xstrings["disabled"]
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["chat_users_connections_info"].format(
XXXXXXXXXXXXXXXXstatus=status,Xchat_name=chat["chat_title"]
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturn
XXXXenableX=X("enable",X"on",X"ok",X"yes")
XXXXdisableX=X("disable",X"off",X"no")
XXXXifXargXinXenable:
XXXXXXXXr_boolX=XTrue
XXXXXXXXstatusX=Xstrings["enabled"]
XXXXelifXargXinXdisable:
XXXXXXXXr_boolX=XFalse
XXXXXXXXstatusX=Xstrings["disabled"]
XXXXelse:
XXXXXXXXawaitXmessage.reply(strings["bad_arg_bool"])
XXXXXXXXreturn

XXXXawaitXdb.chat_connection_settings.update_one(
XXXXXXXX{"chat_id":Xchat_id},X{"$set":X{"allow_users_connect":Xr_bool}},Xupsert=True
XXXX)
XXXXawaitXmessage.reply(
XXXXXXXXstrings["chat_users_connections_cng"].format(
XXXXXXXXXXXXstatus=status,Xchat_name=chat["chat_title"]
XXXXXXXX)
XXXX)


@register(cmds="start",Xonly_pm=True)
@get_strings_dec("connections")
@chat_connection()
asyncXdefXconnected_start_state(message,Xstrings,Xchat):
XXXXkeyX=X"InerukiX_connected_start_state:"X+Xstr(message.from_user.id)
XXXXifXredis.get(key):
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["pm_connected"].format(chat_name=chat["chat_title"])
XXXXXXXX)
XXXXXXXXredis.delete(key)


BUTTONS.update({"connect":X"btn_connect_start"})


@register(CommandStart(re.compile(r"btn_connect_start")),Xallow_kwargs=True)
@get_strings_dec("connections")
asyncXdefXconnect_start(message,Xstrings,Xregexp=None,X**kwargs):
XXXXargsX=Xmessage.get_args().split("_")

XXXX#XInXcaseXifXbuttonXhaveXargXitXwillXbeXused.X#XTODO:XCheckXchat_id,XparseXchatXnickname.
XXXXargX=Xargs[3]

XXXXifXarg.startswith("-")XorXarg.isdigit():
XXXXXXXXchatX=XawaitXdb.chat_list.find_one({"chat_id":Xint(arg)})
XXXXelifXarg.startswith("@"):
XXXXXXXXchatX=XawaitXdb.chat_list.find_one({"chat_nick":Xarg.lower()})
XXXXelse:
XXXXXXXXawaitXmessage.reply(strings["cant_find_chat_use_id"])
XXXXXXXXreturn

XXXXawaitXdef_connect_chat(
XXXXXXXXmessage,Xmessage.from_user.id,Xchat["chat_id"],Xchat["chat_title"]
XXXX)


@register(regexp="anon_conn_cb",Xf="cb")
asyncXdefXconnect_anon_admins(event:XCallbackQuery):
XXXXifXnotXawaitXis_user_admin(event.message.chat.id,Xevent.from_user.id):
XXXXXXXXreturn

XXXXifX(
XXXXXXXXevent.message.chat.id
XXXXXXXXnotXinX(dataX:=XawaitXdb.user_list.find_one({"user_id":Xevent.from_user.id}))[
XXXXXXXXXXXX"chats"
XXXXXXXX]
XXXX):
XXXXXXXXawaitXdb.user_list.update_one(
XXXXXXXXXXXX{"_id":Xdata["_id"]},X{"$addToSet":X{"chats":Xevent.message.chat.id}}
XXXXXXXX)
XXXXreturnXawaitXevent.answer(
XXXXXXXXurl=awaitXget_start_link(f"btn_connect_start_{event.message.chat.id}")
XXXX)


__mod_name__X=X"Connections"

__help__X=X"""
SometimesXyouXneedXchangeXsomethingXinXyourXchat,XlikeXnotes,XbutXyouXdon'tXwantXtoXspamXinXit,XtryXconnections,XthisXallowXyouXchangeXchatXsettingsXandXmanageXchat'sXcontentXinXpersonalXmessageXwithXIneruki.

<b>AvailableXcommandsXare:</b>
<b>AvaibleXonlyXinXPM:</b>
-X/connect:XShowXlastXconnectedXchatsXbuttonXforXfastXconnection
-X/connectX(chatXIDXorXchatXnickname):XConnectXtoXchatXbyXargumentXwhichXyouXprovided
-X/reconnect:XConnectXtoXlastXconnectedXchatXbefore
-X/disconnect:XDisconnectXfrom

<b>AvaibleXonlyXinXgroups:</b>
-X/connect:XDirectXconnectXtoXthisXgroup

<b>OtherXcommands:</b>
-X/allowusersconnectX(on/offXenable/disable):XEnableXorXdisableXconnectionXfeatureXforXregularXusers,XforXadminsXconnectionsXwillXbeXworksXalways
"""
