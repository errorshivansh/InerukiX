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
fromaiogram.utils.exceptionsimportUnauthorized

fromIneruki.modules.utils.user_detailsimportis_user_admin
fromIneruki.services.mongoimportdb
fromIneruki.services.redisimportredis
fromIneruki.utils.cachedimportcached


asyncdefget_connected_chat(
message,admin=False,only_groups=False,from_id=None,command=None
):
#admin-Requireadminrightsinconnectedchat
#only_in_groups-disablecommandwhenbot'spmnotconnectedtoanychat
real_chat_id=message.chat.id
user_id=from_idormessage.from_user.id
key="connection_cache_"+str(user_id)

ifnotmessage.chat.type=="private":
_chat=awaitdb.chat_list.find_one({"chat_id":real_chat_id})
chat_title=_chat["chat_title"]if_chatisnotNoneelsemessage.chat.title
#OnsomestrangecasessuchasDatabaseisfreshornew;itdoesn'tcontainchatdata
#Onlyto"handle"theerror,wedotheaboveworkaround-gettingchattitlefromtheupdate
return{"status":"chat","chat_id":real_chat_id,"chat_title":chat_title}

#Cached
ifcached:=redis.hgetall(key):
cached["status"]=True
cached["chat_id"]=int(cached["chat_id"])
#returncached

#ifpmandnotconnected
if(
not(connected:=awaitget_connection_data(user_id))
or"chat_id"notinconnected
):
ifonly_groups:
return{"status":None,"err_msg":"usage_only_in_groups"}
else:
return{"status":"private","chat_id":user_id,"chat_title":"Localchat"}

chat_id=connected["chat_id"]

#Getchatswhereuserwasdetectedandcheckifuserinconnectedchat
#TODO:Reallygettheuserandcheckonbanned
user_chats=(awaitdb.user_list.find_one({"user_id":user_id}))["chats"]
ifchat_idnotinuser_chats:
return{"status":None,"err_msg":"not_in_chat"}

chat_title=(awaitdb.chat_list.find_one({"chat_id":chat_id}))["chat_title"]

#Adminrightscheckifadmin=True
try:
user_admin=awaitis_user_admin(chat_id,user_id)
exceptUnauthorized:
return{"status":None,"err_msg":"bot_not_in_chat,please/disconnect"}

ifadmin:
ifnotuser_admin:
return{"status":None,"err_msg":"u_should_be_admin"}

if"command"inconnected:
ifcommandinconnected["command"]:
return{"status":True,"chat_id":chat_id,"chat_title":chat_title}
else:
#Returnlocalchatifuserisaccessingnonconnectedcommand
return{"status":"private","chat_id":user_id,"chat_title":"Localchat"}

#Checkon/allowusersconnectenabled
ifsettings:=awaitdb.chat_connection_settings.find_one({"chat_id":chat_id}):
if(
"allow_users_connect"insettings
andsettings["allow_users_connect"]isFalse
andnotuser_admin
):
return{"status":None,"err_msg":"conn_not_allowed"}

data={"status":True,"chat_id":chat_id,"chat_title":chat_title}

#Cacheconnectionstatusfor15minutes
cached=data
cached["status"]=1
redis.hmset(key,cached)
redis.expire(key,900)

returndata


defchat_connection(**dec_kwargs):
defwrapped(func):
asyncdefwrapped_1(*args,**kwargs):

message=args[0]
from_id=None
ifhasattr(message,"message"):
from_id=message.from_user.id
message=message.message

if(
check:=awaitget_connected_chat(
message,from_id=from_id,**dec_kwargs
)
)["status"]isNone:
awaitmessage.reply(check["err_msg"])
return
else:
returnawaitfunc(*args,check,**kwargs)

returnwrapped_1

returnwrapped


asyncdefset_connected_chat(user_id,chat_id):
key=f"connection_cache_{user_id}"
redis.delete(key)
ifnotchat_id:
awaitdb.connections.update_one(
{"user_id":user_id},{"$unset":{"chat_id":1,"command":1}},upsert=True
)
awaitget_connection_data.reset_cache(user_id)
return

awaitdb.connections.update_one(
{"user_id":user_id},
{
"$set":{"user_id":user_id,"chat_id":chat_id},
"$unset":{"command":1},
"$addToSet":{"history":{"$each":[chat_id]}},
},
upsert=True,
)
returnawaitget_connection_data.reset_cache(user_id)


asyncdefset_connected_command(user_id,chat_id,command):
command.append("disconnect")
awaitdb.connections.update_one(
{"user_id":user_id},
{"$set":{"user_id":user_id,"chat_id":chat_id,"command":list(command)}},
upsert=True,
)
returnawaitget_connection_data.reset_cache(user_id)


@cached()
asyncdefget_connection_data(user_id:int)->dict:
returnawaitdb.connections.find_one({"user_id":user_id})
