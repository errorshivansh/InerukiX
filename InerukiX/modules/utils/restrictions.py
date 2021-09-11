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

fromaiogram.types.chat_permissionsimportChatPermissions
fromaiogram.utils.exceptionsimportBadRequest,MigrateToChat,Unauthorized

fromInerukiimportbot


asyncdefban_user(chat_id,user_id,until_date=None):
try:
awaitbot.kick_chat_member(chat_id,user_id,until_date=until_date)
except(BadRequest,MigrateToChat,Unauthorized):
returnFalse
returnTrue


asyncdefkick_user(chat_id,user_id):
awaitbot.unban_chat_member(chat_id,user_id)
returnTrue


asyncdefmute_user(chat_id,user_id,until_date=None):
awaitbot.restrict_chat_member(
chat_id,
user_id,
permissions=ChatPermissions(can_send_messages=False,until_date=until_date),
until_date=until_date,
)
returnTrue


asyncdefrestrict_user(chat_id,user_id,until_date=None):
awaitbot.restrict_chat_member(
chat_id,
user_id,
permissions=ChatPermissions(
can_send_messages=True,
can_send_media_messages=False,
can_send_other_messages=False,
can_add_web_page_previews=False,
until_date=until_date,
),
until_date=until_date,
)
returnTrue


asyncdefunmute_user(chat_id,user_id):
awaitbot.restrict_chat_member(
chat_id,
user_id,
can_send_messages=True,
can_send_media_messages=True,
can_send_other_messages=True,
can_add_web_page_previews=True,
)
returnTrue


asyncdefunban_user(chat_id,user_id):
try:
returnawaitbot.unban_chat_member(chat_id,user_id,only_if_banned=True)
except(BadRequest,Unauthorized):
returnFalse
