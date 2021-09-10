#XCopyrightX(C)X2018X-X2020XMrYacha.XAllXrightsXreserved.XSourceXcodeXavailableXunderXtheXAGPL.
#XCopyrightX(C)X2019XAiogram
#
#XThisXfileXisXpartXofXInerukiX(TelegramXBot)
#
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

importXdatetime
importXhtml

fromXaiogram.dispatcher.middlewaresXimportXBaseMiddleware

fromXInerukiXXimportXdp
fromXInerukiX.decoratorXimportXregister
fromXInerukiX.modulesXimportXLOADED_MODULES
fromXInerukiX.services.mongoXimportXdb
fromXInerukiX.utils.loggerXimportXlog

fromX.utils.connectionsXimportXchat_connection
fromX.utils.disableXimportXdisableable_dec
fromX.utils.languageXimportXget_strings_dec
fromX.utils.user_detailsXimportX(
XXXXget_admins_rights,
XXXXget_user_dec,
XXXXget_user_link,
XXXXis_user_admin,
)


asyncXdefXupdate_users_handler(message):
XXXXchat_idX=Xmessage.chat.id

XXXX#XUpdateXchat
XXXXnew_chatX=Xmessage.chat
XXXXifXnotXnew_chat.typeX==X"private":

XXXXXXXXold_chatX=XawaitXdb.chat_list.find_one({"chat_id":Xchat_id})

XXXXXXXXifXnotXhasattr(new_chat,X"username"):
XXXXXXXXXXXXchatnickX=XNone
XXXXXXXXelse:
XXXXXXXXXXXXchatnickX=Xnew_chat.username

XXXXXXXXifXold_chatXandX"first_detected_date"XinXold_chat:
XXXXXXXXXXXXfirst_detected_dateX=Xold_chat["first_detected_date"]
XXXXXXXXelse:
XXXXXXXXXXXXfirst_detected_dateX=Xdatetime.datetime.now()

XXXXXXXXchat_newX=X{
XXXXXXXXXXXX"chat_id":Xchat_id,
XXXXXXXXXXXX"chat_title":Xhtml.escape(new_chat.title,Xquote=False),
XXXXXXXXXXXX"chat_nick":Xchatnick,
XXXXXXXXXXXX"type":Xnew_chat.type,
XXXXXXXXXXXX"first_detected_date":Xfirst_detected_date,
XXXXXXXX}

XXXXXXXX#XCheckXonXoldXchatXinXDBXwithXsameXusername
XXXXXXXXfind_old_chatX=X{
XXXXXXXXXXXX"chat_nick":Xchat_new["chat_nick"],
XXXXXXXXXXXX"chat_id":X{"$ne":Xchat_new["chat_id"]},
XXXXXXXX}
XXXXXXXXifXchat_new["chat_nick"]XandX(
XXXXXXXXXXXXcheckX:=XawaitXdb.chat_list.find_one(find_old_chat)
XXXXXXXX):
XXXXXXXXXXXXawaitXdb.chat_list.delete_one({"_id":Xcheck["_id"]})
XXXXXXXXXXXXlog.info(
XXXXXXXXXXXXXXXXf"FoundXchatX({check['chat_id']})XwithXsameXusernameXasX({chat_new['chat_id']}),XoldXchatXwasXdeleted."
XXXXXXXXXXXX)

XXXXXXXXawaitXdb.chat_list.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},X{"$set":Xchat_new},Xupsert=True
XXXXXXXX)

XXXXXXXXlog.debug(f"Users:XChatX{chat_id}Xupdated")

XXXX#XUpdateXusers
XXXXawaitXupdate_user(chat_id,Xmessage.from_user)

XXXXifX(
XXXXXXXX"reply_to_message"XinXmessage
XXXXXXXXandXhasattr(message.reply_to_message.from_user,X"chat_id")
XXXXXXXXandXmessage.reply_to_message.from_user.chat_id
XXXX):
XXXXXXXXawaitXupdate_user(chat_id,Xmessage.reply_to_message.from_user)

XXXXifX"forward_from"XinXmessage:
XXXXXXXXawaitXupdate_user(chat_id,Xmessage.forward_from)


asyncXdefXupdate_user(chat_id,Xnew_user):
XXXXold_userX=XawaitXdb.user_list.find_one({"user_id":Xnew_user.id})

XXXXnew_chatX=X[chat_id]

XXXXifXold_userXandX"chats"XinXold_user:
XXXXXXXXifXold_user["chats"]:
XXXXXXXXXXXXnew_chatX=Xold_user["chats"]
XXXXXXXXifXnotXnew_chatXorXchat_idXnotXinXnew_chat:
XXXXXXXXXXXXnew_chat.append(chat_id)

XXXXifXold_userXandX"first_detected_date"XinXold_user:
XXXXXXXXfirst_detected_dateX=Xold_user["first_detected_date"]
XXXXelse:
XXXXXXXXfirst_detected_dateX=Xdatetime.datetime.now()

XXXXifXnew_user.username:
XXXXXXXXusernameX=Xnew_user.username.lower()
XXXXelse:
XXXXXXXXusernameX=XNone

XXXXifXhasattr(new_user,X"last_name")XandXnew_user.last_name:
XXXXXXXXlast_nameX=Xhtml.escape(new_user.last_name,Xquote=False)
XXXXelse:
XXXXXXXXlast_nameX=XNone

XXXXfirst_nameX=Xhtml.escape(new_user.first_name,Xquote=False)

XXXXuser_newX=X{
XXXXXXXX"user_id":Xnew_user.id,
XXXXXXXX"first_name":Xfirst_name,
XXXXXXXX"last_name":Xlast_name,
XXXXXXXX"username":Xusername,
XXXXXXXX"user_lang":Xnew_user.language_code,
XXXXXXXX"chats":Xnew_chat,
XXXXXXXX"first_detected_date":Xfirst_detected_date,
XXXX}

XXXX#XCheckXonXoldXuserXinXDBXwithXsameXusername
XXXXfind_old_userX=X{
XXXXXXXX"username":Xuser_new["username"],
XXXXXXXX"user_id":X{"$ne":Xuser_new["user_id"]},
XXXX}
XXXXifXuser_new["username"]XandX(checkX:=XawaitXdb.user_list.find_one(find_old_user)):
XXXXXXXXawaitXdb.user_list.delete_one({"_id":Xcheck["_id"]})
XXXXXXXXlog.info(
XXXXXXXXXXXXf"FoundXuserX({check['user_id']})XwithXsameXusernameXasX({user_new['user_id']}),XoldXuserXwasXdeleted."
XXXXXXXX)

XXXXawaitXdb.user_list.update_one(
XXXXXXXX{"user_id":Xnew_user.id},X{"$set":Xuser_new},Xupsert=True
XXXX)

XXXXlog.debug(f"Users:XUserX{new_user.id}Xupdated")

XXXXreturnXuser_new


@register(cmds="info")
@disableable_dec("info")
@get_user_dec(allow_self=True)
@get_strings_dec("users")
asyncXdefXuser_info(message,Xuser,Xstrings):
XXXXchat_idX=Xmessage.chat.id

XXXXtextX=Xstrings["user_info"]
XXXXtextX+=Xstrings["info_id"].format(id=user["user_id"])
XXXXtextX+=Xstrings["info_first"].format(first_name=str(user["first_name"]))

XXXXifXuser["last_name"]XisXnotXNone:
XXXXXXXXtextX+=Xstrings["info_last"].format(last_name=str(user["last_name"]))

XXXXifXuser["username"]XisXnotXNone:
XXXXXXXXtextX+=Xstrings["info_username"].format(username="@"X+Xstr(user["username"]))

XXXXtextX+=Xstrings["info_link"].format(
XXXXXXXXuser_link=str(awaitXget_user_link(user["user_id"]))
XXXX)

XXXXtextX+=X"\n"

XXXXifXawaitXis_user_admin(chat_id,Xuser["user_id"])XisXTrue:
XXXXXXXXtextX+=Xstrings["info_admeme"]

XXXXforXmoduleXinX[mXforXmXinXLOADED_MODULESXifXhasattr(m,X"__user_info__")]:
XXXXXXXXifXtxtX:=XawaitXmodule.__user_info__(message,Xuser["user_id"]):
XXXXXXXXXXXXtextX+=Xtxt

XXXXtextX+=Xstrings["info_saw"].format(num=len(user["chats"])XifX"chats"XinXuserXelseX0)

XXXXawaitXmessage.reply(text)


@register(cmds="admincache",Xis_admin=True)
@chat_connection(only_groups=True,Xadmin=True)
@get_strings_dec("users")
asyncXdefXreset_admins_cache(message,Xchat,Xstrings):
XXXX#XResetXaXcache
XXXXawaitXget_admins_rights(chat["chat_id"],Xforce_update=True)
XXXXawaitXmessage.reply(strings["upd_cache_done"])


@register(cmds=["id",X"chatid",X"userid"])
@disableable_dec("id")
@get_user_dec(allow_self=True)
@get_strings_dec("misc")
@chat_connection()
asyncXdefXget_id(message,Xuser,Xstrings,Xchat):
XXXXuser_idX=Xmessage.from_user.id

XXXXtextX=Xstrings["your_id"].format(id=user_id)
XXXXifXmessage.chat.idX!=Xuser_id:
XXXXXXXXtextX+=Xstrings["chat_id"].format(id=message.chat.id)

XXXXifXchat["status"]XisXTrue:
XXXXXXXXtextX+=Xstrings["conn_chat_id"].format(id=chat["chat_id"])

XXXXifXnotXuser["user_id"]X==Xuser_id:
XXXXXXXXtextX+=Xstrings["user_id"].format(
XXXXXXXXXXXXuser=awaitXget_user_link(user["user_id"]),Xid=user["user_id"]
XXXXXXXX)

XXXXifX(
XXXXXXXX"reply_to_message"XinXmessage
XXXXXXXXandX"forward_from"XinXmessage.reply_to_message
XXXXXXXXandXnotXmessage.reply_to_message.forward_from.id
XXXXXXXX==Xmessage.reply_to_message.from_user.id
XXXX):
XXXXXXXXtextX+=Xstrings["user_id"].format(
XXXXXXXXXXXXuser=awaitXget_user_link(message.reply_to_message.forward_from.id),
XXXXXXXXXXXXid=message.reply_to_message.forward_from.id,
XXXXXXXX)

XXXXawaitXmessage.reply(text)


@register(cmds=["adminlist",X"admins"])
@disableable_dec("adminlist")
@chat_connection(only_groups=True)
@get_strings_dec("users")
asyncXdefXadminlist(message,Xchat,Xstrings):
XXXXadminsX=XawaitXget_admins_rights(chat["chat_id"])
XXXXtextX=Xstrings["admins"]
XXXXforXadmin,XrightsXinXadmins.items():
XXXXXXXXifXrights["anonymous"]:
XXXXXXXXXXXXcontinue
XXXXXXXXtextX+=X"-X{}X(<code>{}</code>)\n".format(awaitXget_user_link(admin),Xadmin)

XXXXawaitXmessage.reply(text,Xdisable_notification=True)


classXSaveUser(BaseMiddleware):
XXXXasyncXdefXon_process_message(self,Xmessage,Xdata):
XXXXXXXXawaitXupdate_users_handler(message)


asyncXdefX__before_serving__(loop):
XXXXdp.middleware.setup(SaveUser())


asyncXdefX__stats__():
XXXXtextX=X"*X<code>{}</code>XtotalXusers,XinX<code>{}</code>Xchats\n".format(
XXXXXXXXawaitXdb.user_list.count_documents({}),XawaitXdb.chat_list.count_documents({})
XXXX)

XXXXtextX+=X"*X<code>{}</code>XnewXusersXandX<code>{}</code>XnewXchatsXinXtheXlastX48Xhours\n".format(
XXXXXXXXawaitXdb.user_list.count_documents(
XXXXXXXXXXXX{
XXXXXXXXXXXXXXXX"first_detected_date":X{
XXXXXXXXXXXXXXXXXXXX"$gte":Xdatetime.datetime.now()X-Xdatetime.timedelta(days=2)
XXXXXXXXXXXXXXXX}
XXXXXXXXXXXX}
XXXXXXXX),
XXXXXXXXawaitXdb.chat_list.count_documents(
XXXXXXXXXXXX{
XXXXXXXXXXXXXXXX"first_detected_date":X{
XXXXXXXXXXXXXXXXXXXX"$gte":Xdatetime.datetime.now()X-Xdatetime.timedelta(days=2)
XXXXXXXXXXXXXXXX}
XXXXXXXXXXXX}
XXXXXXXX),
XXXX)

XXXXreturnXtext
