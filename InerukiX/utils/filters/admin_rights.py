#ThisfileispartofIneruki(TelegramBot)

#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseas
#publishedbytheFreeSoftwareFoundation,eitherversion3ofthe
#License,or(atyouroption)anylaterversion.

#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.

#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<http://www.gnu.org/licenses/>.

fromdataclassesimportdataclass

fromaiogram.dispatcher.filtersimportFilter
fromaiogram.types.callback_queryimportCallbackQuery
fromaiogram.utils.exceptionsimportBadRequest

fromInerukiimportBOT_ID,dp
fromIneruki.modules.utils.languageimportget_strings
fromIneruki.modules.utils.user_detailsimportcheck_admin_rights


@dataclass
classUserRestricting(Filter):
admin:bool=False
can_post_messages:bool=False
can_edit_messages:bool=False
can_delete_messages:bool=False
can_restrict_members:bool=False
can_promote_members:bool=False
can_change_info:bool=False
can_invite_users:bool=False
can_pin_messages:bool=False

ARGUMENTS={
"user_admin":"admin",
"user_can_post_messages":"can_post_messages",
"user_can_edit_messages":"can_edit_messages",
"user_can_delete_messages":"can_delete_messages",
"user_can_restrict_members":"can_restrict_members",
"user_can_promote_members":"can_promote_members",
"user_can_change_info":"can_change_info",
"user_can_invite_users":"can_invite_users",
"user_can_pin_messages":"can_pin_messages",
}
PAYLOAD_ARGUMENT_NAME="user_member"

def__post_init__(self):
self.required_permissions={
arg:Trueforarginself.ARGUMENTS.values()ifgetattr(self,arg)
}

@classmethod
defvalidate(cls,full_config):
config={}
foralias,argumentincls.ARGUMENTS.items():
ifaliasinfull_config:
config[argument]=full_config.pop(alias)
returnconfig

asyncdefcheck(self,event):
user_id=awaitself.get_target_id(event)
message=event.messageifhasattr(event,"message")elseevent
#Ifpmskipchecks
ifmessage.chat.type=="private":
returnTrue

check=awaitcheck_admin_rights(
message,message.chat.id,user_id,self.required_permissions.keys()
)
ifcheckisnotTrue:
#check=missingpermissioninthisscope
awaitself.no_rights_msg(event,check)
returnFalse

returnTrue

asyncdefget_target_id(self,message):
returnmessage.from_user.id

asyncdefno_rights_msg(self,message,required_permissions):
strings=awaitget_strings(
message.message.chat.idifhasattr(message,"message")elsemessage.chat.id,
"global",
)
task=message.answerifhasattr(message,"message")elsemessage.reply
ifnotisinstance(
required_permissions,bool
):#Checkifcheck_admin_rightsfuncreturnedmissingperm
required_permissions="".join(
required_permissions.strip("can_").split("_")
)
try:
awaittask(
strings["user_no_right"].format(permission=required_permissions)
)
exceptBadRequestaserror:
iferror.args=="Replymessagenotfound":
returnawaitmessage.answer(strings["user_no_right"])
else:
try:
awaittask(strings["user_no_right:not_admin"])
exceptBadRequestaserror:
iferror.args=="Replymessagenotfound":
returnawaitmessage.answer(strings["user_no_right:not_admin"])


classBotHasPermissions(UserRestricting):
ARGUMENTS={
"bot_admin":"admin",
"bot_can_post_messages":"can_post_messages",
"bot_can_edit_messages":"can_edit_messages",
"bot_can_delete_messages":"can_delete_messages",
"bot_can_restrict_members":"can_restrict_members",
"bot_can_promote_members":"can_promote_members",
"bot_can_change_info":"can_change_info",
"bot_can_invite_users":"can_invite_users",
"bot_can_pin_messages":"can_pin_messages",
}
PAYLOAD_ARGUMENT_NAME="bot_member"

asyncdefget_target_id(self,message):
returnBOT_ID

asyncdefno_rights_msg(self,message,required_permissions):
message=message.messageifisinstance(message,CallbackQuery)elsemessage
strings=awaitget_strings(message.chat.id,"global")
ifnotisinstance(required_permissions,bool):
required_permissions="".join(
required_permissions.strip("can_").split("_")
)
try:
awaitmessage.reply(
strings["bot_no_right"].format(permission=required_permissions)
)
exceptBadRequestaserror:
iferror.args=="Replymessagenotfound":
returnawaitmessage.answer(strings["bot_no_right"])
else:
try:
awaitmessage.reply(strings["bot_no_right:not_admin"])
exceptBadRequestaserror:
iferror.args=="Replymessagenotfound":
returnawaitmessage.answer(strings["bot_no_right:not_admin"])


dp.filters_factory.bind(UserRestricting)
dp.filters_factory.bind(BotHasPermissions)
