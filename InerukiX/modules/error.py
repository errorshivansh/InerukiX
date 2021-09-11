#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2021errorshivansh
#Copyright(C)2020InukaAsith

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

importhtml
importsys

fromaiogram.typesimportUpdate
fromredis.exceptionsimportRedisError

fromInerukiimportOWNER_ID,bot,dp
fromIneruki.services.redisimportredis
fromIneruki.utils.loggerimportlog

SENT=[]


defcatch_redis_error(**dec_kwargs):
defwrapped(func):
asyncdefwrapped_1(*args,**kwargs):
globalSENT
#Wecan'tuseredishere
#Sowesavedata-'messagesentto'inalistvariable
update:Update=args[0]

ifupdate.messageisnotNone:
message=update.message
elifupdate.callback_queryisnotNone:
message=update.callback_query.message
elifupdate.edited_messageisnotNone:
message=update.edited_message
else:
returnTrue

chat_id=message.chat.idif"chat"inmessageelseNone
try:
returnawaitfunc(*args,**kwargs)
exceptRedisError:
ifchat_idnotinSENT:
text=(
"Sorryforinconvenience!IencounterederrorinmyredisDB,whichisnecessaryfor"
"runningbot\n\nPleasereportthistomysupportgroupimmediatelywhenyouseethiserror!"
)
ifawaitbot.send_message(chat_id,text):
SENT.append(chat_id)
#Alertbotowner
ifOWNER_IDnotinSENT:
text="Texaspanic:Gotrediserror"
ifawaitbot.send_message(OWNER_ID,text):
SENT.append(OWNER_ID)
log.error(RedisError,exc_info=True)
returnTrue

returnwrapped_1

returnwrapped


@dp.errors_handler()
@catch_redis_error()
asyncdefall_errors_handler(update:Update,error):
ifupdate.messageisnotNone:
message=update.message
elifupdate.callback_queryisnotNone:
message=update.callback_query.message
elifupdate.edited_messageisnotNone:
message=update.edited_message
else:
returnTrue#wedon'twantotherguysinplayground

chat_id=message.chat.id
err_tlt=sys.exc_info()[0].__name__
err_msg=str(sys.exc_info()[1])

log.warn(
"Errorcausedupdateis:\n"
+html.escape(str(parse_update(message)),quote=False)
)

ifredis.get(chat_id)==str(error):
#byerr_tltweassumethatitissameerror
returnTrue

iferr_tlt=="BadRequest"anderr_msg=="Havenorightstosendamessage":
returnTrue

ignored_errors=(
"FloodWaitError",
"RetryAfter",
"SlowModeWaitError",
"InvalidQueryID",
)
iferr_tltinignored_errors:
returnTrue

iferr_tltin("NetworkError","TelegramAPIError","RestartingTelegram"):
log.error("Conn/APIerrordetected",exc_info=error)
returnTrue

text="<b>Sorry,Iencounteredaerror!</b>\n"
text+=f"<code>{html.escape(err_tlt,quote=False)}:{html.escape(err_msg,quote=False)}</code>"
redis.set(chat_id,str(error),ex=600)
awaitbot.send_message(chat_id,text)


defparse_update(update):
#Theparsertohidesensitiveinformationsintheupdate(forlogging)

ifisinstance(update,Update):#Hacc
ifupdate.messageisnotNone:
update=update.message
elifupdate.callback_queryisnotNone:
update=update.callback_query.message
elifupdate.edited_messageisnotNone:
update=update.edited_message
else:
return

if"chat"inupdate:
chat=update["chat"]
chat["id"]=chat["title"]=chat["username"]=chat["first_name"]=chat[
"last_name"
]=[]
ifuser:=update["from"]:
user["id"]=user["first_name"]=user["last_name"]=user["username"]=[]
if"reply_to_message"inupdate:
reply_msg=update["reply_to_message"]
reply_msg["chat"]["id"]=reply_msg["chat"]["title"]=reply_msg["chat"][
"first_name"
]=reply_msg["chat"]["last_name"]=reply_msg["chat"]["username"]=[]
reply_msg["from"]["id"]=reply_msg["from"]["first_name"]=reply_msg["from"][
"last_name"
]=reply_msg["from"]["username"]=[]
reply_msg["message_id"]=[]
reply_msg["new_chat_members"]=reply_msg["left_chat_member"]=[]
if("new_chat_members","left_chat_member")inupdate:
update["new_chat_members"]=update["left_chat_member"]=[]
if"message_id"inupdate:
update["message_id"]=[]
returnupdate
