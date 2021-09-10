#XCopyrightX(C)X2018X-X2020XMrYacha.XAllXrightsXreserved.XSourceXcodeXavailableXunderXtheXAGPL.
#XCopyrightX(C)X2019XAiogram
#XCopyrightX(C)X2020XJeepeo
#
#XThisXfileXwasXaXXpartXofXHitsukiX(TelegramXBot)
#XModifiedXbyXerrorshivanshXforXInerukiX


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

importXitertools

fromXaiogram.types.chat_permissionsXimportXChatPermissions

fromXInerukiXXimportXbot
fromXInerukiX.decoratorXimportXregister

fromX.utils.connectionsXimportXchat_connection
fromX.utils.languageXimportXget_strings_dec


@register(cmds=["locks",X"locktypes"],Xuser_admin=True)
@chat_connection(only_groups=True)
@get_strings_dec("locks")
asyncXdefXlock_types(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXchat_titleX=Xchat["chat_title"]
XXXXtextX=Xstrings["locks_header"].format(chat_title=chat_title)

XXXXasyncXforXlock,XstatusXinXlock_parser(chat_id):
XXXXXXXXtextX+=Xf"-X{lock}X=X{status}X\n"
XXXXawaitXmessage.reply(text)


@register(cmds="lock",Xuser_can_restrict_members=True,Xbot_can_restrict_members=True)
@chat_connection(only_groups=True)
@get_strings_dec("locks")
asyncXdefXlock_cmd(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXchat_titleX=Xchat["chat_title"]

XXXXifX(argsX:=Xmessage.get_args().split("X",X1))X==X[""]:
XXXXXXXXawaitXmessage.reply(strings["no_lock_args"])
XXXXXXXXreturn

XXXXasyncXforXlock,XstatusXinXlock_parser(chat_id,Xrev=True):
XXXXXXXXifXargs[0]X==Xlock[0]:
XXXXXXXXXXXXifXstatusXisXTrue:
XXXXXXXXXXXXXXXXawaitXmessage.reply(strings["already_locked"])
XXXXXXXXXXXXXXXXcontinue

XXXXXXXXXXXXto_lockX=X{lock[1]:XFalse}
XXXXXXXXXXXXnew_permX=XChatPermissions(**to_lock)
XXXXXXXXXXXXawaitXbot.set_chat_permissions(chat_id,Xnew_perm)
XXXXXXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXXXXXstrings["locked_successfully"].format(lock=lock[0],Xchat=chat_title)
XXXXXXXXXXXX)


@register(cmds="unlock",Xuser_can_restrict_members=True,Xbot_can_restrict_members=True)
@chat_connection(only_groups=True)
@get_strings_dec("locks")
asyncXdefXunlock_cmd(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXchat_titleX=Xchat["chat_title"]

XXXXifX(argsX:=Xmessage.get_args().split("X",X1))X==X[""]:
XXXXXXXXawaitXmessage.reply(strings["no_unlock_args"])
XXXXXXXXreturn

XXXXasyncXforXlock,XstatusXinXlock_parser(chat_id,Xrev=True):
XXXXXXXXifXargs[0]X==Xlock[0]:
XXXXXXXXXXXXifXstatusXisXFalse:
XXXXXXXXXXXXXXXXawaitXmessage.reply(strings["not_locked"])
XXXXXXXXXXXXXXXXcontinue

XXXXXXXXXXXXto_unlockX=X{lock[1]:XTrue}
XXXXXXXXXXXXnew_permX=XChatPermissions(**to_unlock)
XXXXXXXXXXXXawaitXbot.set_chat_permissions(chat_id,Xnew_perm)
XXXXXXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXXXXXstrings["unlocked_successfully"].format(lock=lock[0],Xchat=chat_title)
XXXXXXXXXXXX)


asyncXdefXlock_parser(chat_id,Xrev=False):
XXXXkeywordsX=X{
XXXXXXXX"all":X"can_send_messages",
XXXXXXXX"media":X"can_send_media_messages",
XXXXXXXX"polls":X"can_send_polls",
XXXXXXXX"others":X"can_send_other_messages",
XXXX}
XXXXcurrent_lockX=X(awaitXbot.get_chat(chat_id)).permissions

XXXXforXlock,XkeywordXinXitertools.zip_longest(
XXXXXXXXdict(current_lock).keys(),Xkeywords.items()
XXXX):
XXXXXXXXifXkeywordXisXnotXNoneXandXlockXinXkeyword:
XXXXXXXXXXXXifXrev:
XXXXXXXXXXXXXXXXlockX=Xlist([keyword[0],Xkeyword[1]])
XXXXXXXXXXXXXXXXstatusX=XnotXcurrent_lock[keyword[1]]
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXstatusX=XnotXcurrent_lock[lock]
XXXXXXXXXXXXXXXXlockX=Xkeyword[0]
XXXXXXXXXXXXyieldXlock,Xstatus


__mod_name__X=X"Locks"

__help__X=X"""
UseXthisXfeatureXtoXblockXusersXfromXsendingXspecificXmessageXtypesXtoXyourXgroup!
<b>AvailableXcommandsXare:</b>
-X/locksXorX/locktypes:XUseXthisXcommandXtoXknowXcurrentXstateXofXyourXlocksXinXyourXgroup!
-X/lockX(locktype):XLocksXaXtypeXofXmessages
-X/unlockX(locktype):XUnlocksXaXtypeXofXmessage
"""
