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
fromXaiogram.utils.exceptionsXimportXUnauthorized

fromXInerukiX.modules.utils.user_detailsXimportXis_user_admin
fromXInerukiX.services.mongoXimportXdb
fromXInerukiX.services.redisXimportXredis
fromXInerukiX.utils.cachedXimportXcached


asyncXdefXget_connected_chat(
XXXXmessage,Xadmin=False,Xonly_groups=False,Xfrom_id=None,Xcommand=None
):
XXXX#XadminX-XRequireXadminXrightsXinXconnectedXchat
XXXX#Xonly_in_groupsX-XdisableXcommandXwhenXbot'sXpmXnotXconnectedXtoXanyXchat
XXXXreal_chat_idX=Xmessage.chat.id
XXXXuser_idX=Xfrom_idXorXmessage.from_user.id
XXXXkeyX=X"connection_cache_"X+Xstr(user_id)

XXXXifXnotXmessage.chat.typeX==X"private":
XXXXXXXX_chatX=XawaitXdb.chat_list.find_one({"chat_id":Xreal_chat_id})
XXXXXXXXchat_titleX=X_chat["chat_title"]XifX_chatXisXnotXNoneXelseXmessage.chat.title
XXXXXXXX#XOnXsomeXstrangeXcasesXsuchXasXDatabaseXisXfreshXorXnewX;XitXdoesn'tXcontainXchatXdata
XXXXXXXX#XOnlyXtoX"handle"XtheXerror,XweXdoXtheXaboveXworkaroundX-XgettingXchatXtitleXfromXtheXupdate
XXXXXXXXreturnX{"status":X"chat",X"chat_id":Xreal_chat_id,X"chat_title":Xchat_title}

XXXX#XCached
XXXXifXcachedX:=Xredis.hgetall(key):
XXXXXXXXcached["status"]X=XTrue
XXXXXXXXcached["chat_id"]X=Xint(cached["chat_id"])
XXXXXXXX#XreturnXcached

XXXX#XifXpmXandXnotXconnected
XXXXifX(
XXXXXXXXnotX(connectedX:=XawaitXget_connection_data(user_id))
XXXXXXXXorX"chat_id"XnotXinXconnected
XXXX):
XXXXXXXXifXonly_groups:
XXXXXXXXXXXXreturnX{"status":XNone,X"err_msg":X"usage_only_in_groups"}
XXXXXXXXelse:
XXXXXXXXXXXXreturnX{"status":X"private",X"chat_id":Xuser_id,X"chat_title":X"LocalXchat"}

XXXXchat_idX=Xconnected["chat_id"]

XXXX#XGetXchatsXwhereXuserXwasXdetectedXandXcheckXifXuserXinXconnectedXchat
XXXX#XTODO:XReallyXgetXtheXuserXandXcheckXonXbanned
XXXXuser_chatsX=X(awaitXdb.user_list.find_one({"user_id":Xuser_id}))["chats"]
XXXXifXchat_idXnotXinXuser_chats:
XXXXXXXXreturnX{"status":XNone,X"err_msg":X"not_in_chat"}

XXXXchat_titleX=X(awaitXdb.chat_list.find_one({"chat_id":Xchat_id}))["chat_title"]

XXXX#XAdminXrightsXcheckXifXadmin=True
XXXXtry:
XXXXXXXXuser_adminX=XawaitXis_user_admin(chat_id,Xuser_id)
XXXXexceptXUnauthorized:
XXXXXXXXreturnX{"status":XNone,X"err_msg":X"bot_not_in_chat,XpleaseX/disconnect"}

XXXXifXadmin:
XXXXXXXXifXnotXuser_admin:
XXXXXXXXXXXXreturnX{"status":XNone,X"err_msg":X"u_should_be_admin"}

XXXXifX"command"XinXconnected:
XXXXXXXXifXcommandXinXconnected["command"]:
XXXXXXXXXXXXreturnX{"status":XTrue,X"chat_id":Xchat_id,X"chat_title":Xchat_title}
XXXXXXXXelse:
XXXXXXXXXXXX#XReturnXlocalXchatXifXuserXisXaccessingXnonXconnectedXcommand
XXXXXXXXXXXXreturnX{"status":X"private",X"chat_id":Xuser_id,X"chat_title":X"LocalXchat"}

XXXX#XCheckXonX/allowusersconnectXenabled
XXXXifXsettingsX:=XawaitXdb.chat_connection_settings.find_one({"chat_id":Xchat_id}):
XXXXXXXXifX(
XXXXXXXXXXXX"allow_users_connect"XinXsettings
XXXXXXXXXXXXandXsettings["allow_users_connect"]XisXFalse
XXXXXXXXXXXXandXnotXuser_admin
XXXXXXXX):
XXXXXXXXXXXXreturnX{"status":XNone,X"err_msg":X"conn_not_allowed"}

XXXXdataX=X{"status":XTrue,X"chat_id":Xchat_id,X"chat_title":Xchat_title}

XXXX#XCacheXconnectionXstatusXforX15Xminutes
XXXXcachedX=Xdata
XXXXcached["status"]X=X1
XXXXredis.hmset(key,Xcached)
XXXXredis.expire(key,X900)

XXXXreturnXdata


defXchat_connection(**dec_kwargs):
XXXXdefXwrapped(func):
XXXXXXXXasyncXdefXwrapped_1(*args,X**kwargs):

XXXXXXXXXXXXmessageX=Xargs[0]
XXXXXXXXXXXXfrom_idX=XNone
XXXXXXXXXXXXifXhasattr(message,X"message"):
XXXXXXXXXXXXXXXXfrom_idX=Xmessage.from_user.id
XXXXXXXXXXXXXXXXmessageX=Xmessage.message

XXXXXXXXXXXXifX(
XXXXXXXXXXXXXXXXcheckX:=XawaitXget_connected_chat(
XXXXXXXXXXXXXXXXXXXXmessage,Xfrom_id=from_id,X**dec_kwargs
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXX)["status"]XisXNone:
XXXXXXXXXXXXXXXXawaitXmessage.reply(check["err_msg"])
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXreturnXawaitXfunc(*args,Xcheck,X**kwargs)

XXXXXXXXreturnXwrapped_1

XXXXreturnXwrapped


asyncXdefXset_connected_chat(user_id,Xchat_id):
XXXXkeyX=Xf"connection_cache_{user_id}"
XXXXredis.delete(key)
XXXXifXnotXchat_id:
XXXXXXXXawaitXdb.connections.update_one(
XXXXXXXXXXXX{"user_id":Xuser_id},X{"$unset":X{"chat_id":X1,X"command":X1}},Xupsert=True
XXXXXXXX)
XXXXXXXXawaitXget_connection_data.reset_cache(user_id)
XXXXXXXXreturn

XXXXawaitXdb.connections.update_one(
XXXXXXXX{"user_id":Xuser_id},
XXXXXXXX{
XXXXXXXXXXXX"$set":X{"user_id":Xuser_id,X"chat_id":Xchat_id},
XXXXXXXXXXXX"$unset":X{"command":X1},
XXXXXXXXXXXX"$addToSet":X{"history":X{"$each":X[chat_id]}},
XXXXXXXX},
XXXXXXXXupsert=True,
XXXX)
XXXXreturnXawaitXget_connection_data.reset_cache(user_id)


asyncXdefXset_connected_command(user_id,Xchat_id,Xcommand):
XXXXcommand.append("disconnect")
XXXXawaitXdb.connections.update_one(
XXXXXXXX{"user_id":Xuser_id},
XXXXXXXX{"$set":X{"user_id":Xuser_id,X"chat_id":Xchat_id,X"command":Xlist(command)}},
XXXXXXXXupsert=True,
XXXX)
XXXXreturnXawaitXget_connection_data.reset_cache(user_id)


@cached()
asyncXdefXget_connection_data(user_id:Xint)X->Xdict:
XXXXreturnXawaitXdb.connections.find_one({"user_id":Xuser_id})
