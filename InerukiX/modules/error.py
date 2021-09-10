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

importXhtml
importXsys

fromXaiogram.typesXimportXUpdate
fromXredis.exceptionsXimportXRedisError

fromXInerukiXXimportXOWNER_ID,Xbot,Xdp
fromXInerukiX.services.redisXimportXredis
fromXInerukiX.utils.loggerXimportXlog

SENTX=X[]


defXcatch_redis_error(**dec_kwargs):
XXXXdefXwrapped(func):
XXXXXXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXXXXXglobalXSENT
XXXXXXXXXXXX#XWeXcan'tXuseXredisXhere
XXXXXXXXXXXX#XSoXweXsaveXdataX-X'messageXsentXto'XinXaXlistXvariable
XXXXXXXXXXXXupdate:XUpdateX=Xargs[0]

XXXXXXXXXXXXifXupdate.messageXisXnotXNone:
XXXXXXXXXXXXXXXXmessageX=Xupdate.message
XXXXXXXXXXXXelifXupdate.callback_queryXisXnotXNone:
XXXXXXXXXXXXXXXXmessageX=Xupdate.callback_query.message
XXXXXXXXXXXXelifXupdate.edited_messageXisXnotXNone:
XXXXXXXXXXXXXXXXmessageX=Xupdate.edited_message
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXreturnXTrue

XXXXXXXXXXXXchat_idX=Xmessage.chat.idXifX"chat"XinXmessageXelseXNone
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXreturnXawaitXfunc(*args,X**kwargs)
XXXXXXXXXXXXexceptXRedisError:
XXXXXXXXXXXXXXXXifXchat_idXnotXinXSENT:
XXXXXXXXXXXXXXXXXXXXtextX=X(
XXXXXXXXXXXXXXXXXXXXXXXX"SorryXforXinconvenience!XIXencounteredXerrorXinXmyXredisXDB,XwhichXisXnecessaryXforXX"
XXXXXXXXXXXXXXXXXXXXXXXX"runningXbotX\n\nPleaseXreportXthisXtoXmyXsupportXgroupXimmediatelyXwhenXyouXseeXthisXerror!"
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXifXawaitXbot.send_message(chat_id,Xtext):
XXXXXXXXXXXXXXXXXXXXXXXXSENT.append(chat_id)
XXXXXXXXXXXXXXXX#XAlertXbotXowner
XXXXXXXXXXXXXXXXifXOWNER_IDXnotXinXSENT:
XXXXXXXXXXXXXXXXXXXXtextX=X"TexasXpanic:XGotXredisXerror"
XXXXXXXXXXXXXXXXXXXXifXawaitXbot.send_message(OWNER_ID,Xtext):
XXXXXXXXXXXXXXXXXXXXXXXXSENT.append(OWNER_ID)
XXXXXXXXXXXXXXXXlog.error(RedisError,Xexc_info=True)
XXXXXXXXXXXXXXXXreturnXTrue

XXXXXXXXreturnXwrapped_1

XXXXreturnXwrapped


@dp.errors_handler()
@catch_redis_error()
asyncXdefXall_errors_handler(update:XUpdate,Xerror):
XXXXifXupdate.messageXisXnotXNone:
XXXXXXXXmessageX=Xupdate.message
XXXXelifXupdate.callback_queryXisXnotXNone:
XXXXXXXXmessageX=Xupdate.callback_query.message
XXXXelifXupdate.edited_messageXisXnotXNone:
XXXXXXXXmessageX=Xupdate.edited_message
XXXXelse:
XXXXXXXXreturnXTrueXX#XweXdon'tXwantXotherXguysXinXplayground

XXXXchat_idX=Xmessage.chat.id
XXXXerr_tltX=Xsys.exc_info()[0].__name__
XXXXerr_msgX=Xstr(sys.exc_info()[1])

XXXXlog.warn(
XXXXXXXX"ErrorXcausedXupdateXis:X\n"
XXXXXXXX+Xhtml.escape(str(parse_update(message)),Xquote=False)
XXXX)

XXXXifXredis.get(chat_id)X==Xstr(error):
XXXXXXXX#XbyXerr_tltXweXassumeXthatXitXisXsameXerror
XXXXXXXXreturnXTrue

XXXXifXerr_tltX==X"BadRequest"XandXerr_msgX==X"HaveXnoXrightsXtoXsendXaXmessage":
XXXXXXXXreturnXTrue

XXXXignored_errorsX=X(
XXXXXXXX"FloodWaitError",
XXXXXXXX"RetryAfter",
XXXXXXXX"SlowModeWaitError",
XXXXXXXX"InvalidQueryID",
XXXX)
XXXXifXerr_tltXinXignored_errors:
XXXXXXXXreturnXTrue

XXXXifXerr_tltXinX("NetworkError",X"TelegramAPIError",X"RestartingTelegram"):
XXXXXXXXlog.error("Conn/APIXerrorXdetected",Xexc_info=error)
XXXXXXXXreturnXTrue

XXXXtextX=X"<b>Sorry,XIXencounteredXaXerror!</b>\n"
XXXXtextX+=Xf"<code>{html.escape(err_tlt,Xquote=False)}:X{html.escape(err_msg,Xquote=False)}</code>"
XXXXredis.set(chat_id,Xstr(error),Xex=600)
XXXXawaitXbot.send_message(chat_id,Xtext)


defXparse_update(update):
XXXX#XTheXparserXtoXhideXsensitiveXinformationsXinXtheXupdateX(forXlogging)

XXXXifXisinstance(update,XUpdate):XX#XHacc
XXXXXXXXifXupdate.messageXisXnotXNone:
XXXXXXXXXXXXupdateX=Xupdate.message
XXXXXXXXelifXupdate.callback_queryXisXnotXNone:
XXXXXXXXXXXXupdateX=Xupdate.callback_query.message
XXXXXXXXelifXupdate.edited_messageXisXnotXNone:
XXXXXXXXXXXXupdateX=Xupdate.edited_message
XXXXXXXXelse:
XXXXXXXXXXXXreturn

XXXXifX"chat"XinXupdate:
XXXXXXXXchatX=Xupdate["chat"]
XXXXXXXXchat["id"]X=Xchat["title"]X=Xchat["username"]X=Xchat["first_name"]X=Xchat[
XXXXXXXXXXXX"last_name"
XXXXXXXX]X=X[]
XXXXifXuserX:=Xupdate["from"]:
XXXXXXXXuser["id"]X=Xuser["first_name"]X=Xuser["last_name"]X=Xuser["username"]X=X[]
XXXXifX"reply_to_message"XinXupdate:
XXXXXXXXreply_msgX=Xupdate["reply_to_message"]
XXXXXXXXreply_msg["chat"]["id"]X=Xreply_msg["chat"]["title"]X=Xreply_msg["chat"][
XXXXXXXXXXXX"first_name"
XXXXXXXX]X=Xreply_msg["chat"]["last_name"]X=Xreply_msg["chat"]["username"]X=X[]
XXXXXXXXreply_msg["from"]["id"]X=Xreply_msg["from"]["first_name"]X=Xreply_msg["from"][
XXXXXXXXXXXX"last_name"
XXXXXXXX]X=Xreply_msg["from"]["username"]X=X[]
XXXXXXXXreply_msg["message_id"]X=X[]
XXXXXXXXreply_msg["new_chat_members"]X=Xreply_msg["left_chat_member"]X=X[]
XXXXifX("new_chat_members",X"left_chat_member")XinXupdate:
XXXXXXXXupdate["new_chat_members"]X=Xupdate["left_chat_member"]X=X[]
XXXXifX"message_id"XinXupdate:
XXXXXXXXupdate["message_id"]X=X[]
XXXXreturnXupdate
