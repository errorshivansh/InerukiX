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

fromXaiogram.utils.exceptionsXimportXChatAdminRequired
fromXtelethon.errorsXimportXAdminRankEmojiNotAllowedError

fromXInerukiXXimportXBOT_ID,Xbot
fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.telethonXimportXtbot

fromX.utils.connectionsXimportXchat_connection
fromX.utils.languageXimportXget_strings_dec
fromX.utils.user_detailsXimportX(
XXXXget_admins_rights,
XXXXget_user_and_text_dec,
XXXXget_user_dec,
XXXXget_user_link,
)


@register(cmds="promote",Xbot_can_promote_members=True,Xuser_can_promote_members=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_user_and_text_dec()
@get_strings_dec("promotes")
asyncXdefXpromote(message,Xchat,Xuser,Xargs,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXtextX=Xstrings["promote_success"].format(
XXXXXXXXuser=awaitXget_user_link(user["user_id"]),Xchat_name=chat["chat_title"]
XXXX)

XXXXifXuser["user_id"]X==XBOT_ID:
XXXXXXXXreturn

XXXXifXuser["user_id"]X==Xmessage.from_user.id:
XXXXXXXXreturnXawaitXmessage.reply(strings["cant_promote_yourself"])

XXXXtitleX=XNone

XXXXifXargs:
XXXXXXXXifXlen(args)X>X16:
XXXXXXXXXXXXawaitXmessage.reply(strings["rank_to_loong"])
XXXXXXXXXXXXreturn
XXXXXXXXtitleX=Xargs
XXXXXXXXtextX+=Xstrings["promote_title"].format(role=html.escape(title,Xquote=False))

XXXXtry:
XXXXXXXXawaitXtbot.edit_admin(
XXXXXXXXXXXXchat_id,
XXXXXXXXXXXXuser["user_id"],
XXXXXXXXXXXXinvite_users=True,
XXXXXXXXXXXXchange_info=True,
XXXXXXXXXXXXban_users=True,
XXXXXXXXXXXXdelete_messages=True,
XXXXXXXXXXXXpin_messages=True,
XXXXXXXXXXXXtitle=title,
XXXXXXXX)
XXXXexceptXValueError:
XXXXXXXXreturnXawaitXmessage.reply(strings["cant_get_user"])
XXXXexceptXAdminRankEmojiNotAllowedError:
XXXXXXXXreturnXawaitXmessage.reply(strings["emoji_not_allowed"])
XXXXawaitXget_admins_rights(chat_id,Xforce_update=True)XX#XResetXaXcache
XXXXawaitXmessage.reply(text)


@register(cmds="demote",Xbot_can_promote_members=True,Xuser_can_promote_members=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_user_dec()
@get_strings_dec("promotes")
asyncXdefXdemote(message,Xchat,Xuser,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXifXuser["user_id"]X==XBOT_ID:
XXXXXXXXreturn

XXXXtry:
XXXXXXXXawaitXbot.promote_chat_member(chat_id,Xuser["user_id"])
XXXXexceptXChatAdminRequired:
XXXXXXXXreturnXawaitXmessage.reply(strings["demote_failed"])

XXXXawaitXget_admins_rights(chat_id,Xforce_update=True)XX#XResetXaXcache
XXXXawaitXmessage.reply(
XXXXXXXXstrings["demote_success"].format(
XXXXXXXXXXXXuser=awaitXget_user_link(user["user_id"]),Xchat_name=chat["chat_title"]
XXXXXXXX)
XXXX)
