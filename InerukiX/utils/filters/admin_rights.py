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

fromXdataclassesXimportXdataclass

fromXaiogram.dispatcher.filtersXimportXFilter
fromXaiogram.types.callback_queryXimportXCallbackQuery
fromXaiogram.utils.exceptionsXimportXBadRequest

fromXInerukiXXimportXBOT_ID,Xdp
fromXInerukiX.modules.utils.languageXimportXget_strings
fromXInerukiX.modules.utils.user_detailsXimportXcheck_admin_rights


@dataclass
classXUserRestricting(Filter):
XXXXadmin:XboolX=XFalse
XXXXcan_post_messages:XboolX=XFalse
XXXXcan_edit_messages:XboolX=XFalse
XXXXcan_delete_messages:XboolX=XFalse
XXXXcan_restrict_members:XboolX=XFalse
XXXXcan_promote_members:XboolX=XFalse
XXXXcan_change_info:XboolX=XFalse
XXXXcan_invite_users:XboolX=XFalse
XXXXcan_pin_messages:XboolX=XFalse

XXXXARGUMENTSX=X{
XXXXXXXX"user_admin":X"admin",
XXXXXXXX"user_can_post_messages":X"can_post_messages",
XXXXXXXX"user_can_edit_messages":X"can_edit_messages",
XXXXXXXX"user_can_delete_messages":X"can_delete_messages",
XXXXXXXX"user_can_restrict_members":X"can_restrict_members",
XXXXXXXX"user_can_promote_members":X"can_promote_members",
XXXXXXXX"user_can_change_info":X"can_change_info",
XXXXXXXX"user_can_invite_users":X"can_invite_users",
XXXXXXXX"user_can_pin_messages":X"can_pin_messages",
XXXX}
XXXXPAYLOAD_ARGUMENT_NAMEX=X"user_member"

XXXXdefX__post_init__(self):
XXXXXXXXself.required_permissionsX=X{
XXXXXXXXXXXXarg:XTrueXforXargXinXself.ARGUMENTS.values()XifXgetattr(self,Xarg)
XXXXXXXX}

XXXX@classmethod
XXXXdefXvalidate(cls,Xfull_config):
XXXXXXXXconfigX=X{}
XXXXXXXXforXalias,XargumentXinXcls.ARGUMENTS.items():
XXXXXXXXXXXXifXaliasXinXfull_config:
XXXXXXXXXXXXXXXXconfig[argument]X=Xfull_config.pop(alias)
XXXXXXXXreturnXconfig

XXXXasyncXdefXcheck(self,Xevent):
XXXXXXXXuser_idX=XawaitXself.get_target_id(event)
XXXXXXXXmessageX=Xevent.messageXifXhasattr(event,X"message")XelseXevent
XXXXXXXX#XIfXpmXskipXchecks
XXXXXXXXifXmessage.chat.typeX==X"private":
XXXXXXXXXXXXreturnXTrue

XXXXXXXXcheckX=XawaitXcheck_admin_rights(
XXXXXXXXXXXXmessage,Xmessage.chat.id,Xuser_id,Xself.required_permissions.keys()
XXXXXXXX)
XXXXXXXXifXcheckXisXnotXTrue:
XXXXXXXXXXXX#XcheckX=XmissingXpermissionXinXthisXscope
XXXXXXXXXXXXawaitXself.no_rights_msg(event,Xcheck)
XXXXXXXXXXXXreturnXFalse

XXXXXXXXreturnXTrue

XXXXasyncXdefXget_target_id(self,Xmessage):
XXXXXXXXreturnXmessage.from_user.id

XXXXasyncXdefXno_rights_msg(self,Xmessage,Xrequired_permissions):
XXXXXXXXstringsX=XawaitXget_strings(
XXXXXXXXXXXXmessage.message.chat.idXifXhasattr(message,X"message")XelseXmessage.chat.id,
XXXXXXXXXXXX"global",
XXXXXXXX)
XXXXXXXXtaskX=Xmessage.answerXifXhasattr(message,X"message")XelseXmessage.reply
XXXXXXXXifXnotXisinstance(
XXXXXXXXXXXXrequired_permissions,Xbool
XXXXXXXX):XX#XCheckXifXcheck_admin_rightsXfuncXreturnedXmissingXperm
XXXXXXXXXXXXrequired_permissionsX=X"X".join(
XXXXXXXXXXXXXXXXrequired_permissions.strip("can_").split("_")
XXXXXXXXXXXX)
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXtask(
XXXXXXXXXXXXXXXXXXXXstrings["user_no_right"].format(permission=required_permissions)
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXBadRequestXasXerror:
XXXXXXXXXXXXXXXXifXerror.argsX==X"ReplyXmessageXnotXfound":
XXXXXXXXXXXXXXXXXXXXreturnXawaitXmessage.answer(strings["user_no_right"])
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXtask(strings["user_no_right:not_admin"])
XXXXXXXXXXXXexceptXBadRequestXasXerror:
XXXXXXXXXXXXXXXXifXerror.argsX==X"ReplyXmessageXnotXfound":
XXXXXXXXXXXXXXXXXXXXreturnXawaitXmessage.answer(strings["user_no_right:not_admin"])


classXBotHasPermissions(UserRestricting):
XXXXARGUMENTSX=X{
XXXXXXXX"bot_admin":X"admin",
XXXXXXXX"bot_can_post_messages":X"can_post_messages",
XXXXXXXX"bot_can_edit_messages":X"can_edit_messages",
XXXXXXXX"bot_can_delete_messages":X"can_delete_messages",
XXXXXXXX"bot_can_restrict_members":X"can_restrict_members",
XXXXXXXX"bot_can_promote_members":X"can_promote_members",
XXXXXXXX"bot_can_change_info":X"can_change_info",
XXXXXXXX"bot_can_invite_users":X"can_invite_users",
XXXXXXXX"bot_can_pin_messages":X"can_pin_messages",
XXXX}
XXXXPAYLOAD_ARGUMENT_NAMEX=X"bot_member"

XXXXasyncXdefXget_target_id(self,Xmessage):
XXXXXXXXreturnXBOT_ID

XXXXasyncXdefXno_rights_msg(self,Xmessage,Xrequired_permissions):
XXXXXXXXmessageX=Xmessage.messageXifXisinstance(message,XCallbackQuery)XelseXmessage
XXXXXXXXstringsX=XawaitXget_strings(message.chat.id,X"global")
XXXXXXXXifXnotXisinstance(required_permissions,Xbool):
XXXXXXXXXXXXrequired_permissionsX=X"X".join(
XXXXXXXXXXXXXXXXrequired_permissions.strip("can_").split("_")
XXXXXXXXXXXX)
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXXXXXXXXXstrings["bot_no_right"].format(permission=required_permissions)
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXBadRequestXasXerror:
XXXXXXXXXXXXXXXXifXerror.argsX==X"ReplyXmessageXnotXfound":
XXXXXXXXXXXXXXXXXXXXreturnXawaitXmessage.answer(strings["bot_no_right"])
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply(strings["bot_no_right:not_admin"])
XXXXXXXXXXXXexceptXBadRequestXasXerror:
XXXXXXXXXXXXXXXXifXerror.argsX==X"ReplyXmessageXnotXfound":
XXXXXXXXXXXXXXXXXXXXreturnXawaitXmessage.answer(strings["bot_no_right:not_admin"])


dp.filters_factory.bind(UserRestricting)
dp.filters_factory.bind(BotHasPermissions)
