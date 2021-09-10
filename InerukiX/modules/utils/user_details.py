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

importXpickle
importXre
fromXcontextlibXimportXsuppress
fromXtypingXimportXUnion

fromXaiogram.dispatcher.handlerXimportXSkipHandler
fromXaiogram.typesXimportXCallbackQuery,XMessage
fromXaiogram.utils.exceptionsXimportXBadRequest,XChatNotFound,XUnauthorized
fromXtelethon.tl.functions.usersXimportXGetFullUserRequest

fromXInerukiXXimportXOPERATORS,Xbot
fromXInerukiX.services.mongoXimportXdb
fromXInerukiX.services.redisXimportXbredis
fromXInerukiX.services.telethonXimportXtbot

fromX.languageXimportXget_string
fromX.messageXimportXget_arg


asyncXdefXadd_user_to_db(user):
XXXXifXhasattr(user,X"user"):
XXXXXXXXuserX=Xuser.user

XXXXnew_userX=X{
XXXXXXXX"user_id":Xuser.id,
XXXXXXXX"first_name":Xuser.first_name,
XXXXXXXX"last_name":Xuser.last_name,
XXXXXXXX"username":Xuser.username,
XXXX}

XXXXuserX=XawaitXdb.user_list.find_one({"user_id":Xnew_user["user_id"]})
XXXXifXnotXuserXorXuserXisXNone:
XXXXXXXXuserX=Xnew_user

XXXXifX"chats"XnotXinXuser:
XXXXXXXXnew_user["chats"]X=X[]
XXXXifX"user_lang"XnotXinXuser:
XXXXXXXXnew_user["user_lang"]X=X"en"
XXXXXXXXifXhasattr(user,X"user_lang"):
XXXXXXXXXXXXnew_user["user_lang"]X=Xuser.user_lang

XXXXawaitXdb.user_list.update_one(
XXXXXXXX{"user_id":Xuser["user_id"]},X{"$set":Xnew_user},Xupsert=True
XXXX)

XXXXreturnXnew_user


asyncXdefXget_user_by_id(user_id:Xint):
XXXXifXnotXuser_idX<=X2147483647:
XXXXXXXXreturnXNone

XXXXuserX=XawaitXdb.user_list.find_one({"user_id":Xuser_id})
XXXXifXnotXuser:
XXXXXXXXtry:
XXXXXXXXXXXXuserX=XawaitXadd_user_to_db(awaitXtbot(GetFullUserRequest(user_id)))
XXXXXXXXexceptX(ValueError,XTypeError):
XXXXXXXXXXXXuserX=XNone

XXXXreturnXuser


asyncXdefXget_id_by_nick(data):
XXXX#XCheckXifXdataXisXuser_id
XXXXuserX=XawaitXdb.user_list.find_one({"username":Xdata.replace("@",X"")})
XXXXifXuser:
XXXXXXXXreturnXuser["user_id"]

XXXXuserX=XawaitXtbot(GetFullUserRequest(data))
XXXXreturnXuser


asyncXdefXget_user_by_username(username):
XXXX#XSearchXusernameXinXdatabase
XXXXifX"@"XinXusername:
XXXXXXXX#XRemoveX'@'
XXXXXXXXusernameX=Xusername[1:]

XXXXuserX=XawaitXdb.user_list.find_one({"username":Xusername.lower()})

XXXX#XOhnu,XweXdon'tXhaveXthisXuserXinXDB
XXXXifXnotXuser:
XXXXXXXXtry:
XXXXXXXXXXXXuserX=XawaitXadd_user_to_db(awaitXtbot(GetFullUserRequest(username)))
XXXXXXXXexceptX(ValueError,XTypeError):
XXXXXXXXXXXXuserX=XNone

XXXXreturnXuser


asyncXdefXget_user_link(user_id,Xcustom_name=None,Xmd=False):
XXXXuserX=XawaitXdb.user_list.find_one({"user_id":Xuser_id})

XXXXifXuser:
XXXXXXXXuser_nameX=Xuser["first_name"]
XXXXelse:
XXXXXXXXtry:
XXXXXXXXXXXXuserX=XawaitXadd_user_to_db(awaitXtbot(GetFullUserRequest(int(user_id))))
XXXXXXXXexceptX(ValueError,XTypeError):
XXXXXXXXXXXXuser_nameX=Xstr(user_id)
XXXXXXXXelse:
XXXXXXXXXXXXuser_nameX=Xuser["first_name"]

XXXXifXcustom_name:
XXXXXXXXuser_nameX=Xcustom_name

XXXXifXmd:
XXXXXXXXreturnX"[{name}](tg://user?id={id})".format(name=user_name,Xid=user_id)
XXXXelse:
XXXXXXXXreturnX'<aXhref="tg://user?id={id}">{name}</a>'.format(
XXXXXXXXXXXXname=user_name,Xid=user_id
XXXXXXXX)


asyncXdefXget_admins_rights(chat_id,Xforce_update=False):
XXXXkeyX=X"admin_cache:"X+Xstr(chat_id)
XXXXifX(alistX:=Xbredis.get(key))XandXnotXforce_update:
XXXXXXXXreturnXpickle.loads(alist)
XXXXelse:
XXXXXXXXalistX=X{}
XXXXXXXXadminsX=XawaitXbot.get_chat_administrators(chat_id)
XXXXXXXXforXadminXinXadmins:
XXXXXXXXXXXXuser_idX=Xadmin["user"]["id"]
XXXXXXXXXXXXalist[user_id]X=X{
XXXXXXXXXXXXXXXX"status":Xadmin["status"],
XXXXXXXXXXXXXXXX"admin":XTrue,
XXXXXXXXXXXXXXXX"title":Xadmin["custom_title"],
XXXXXXXXXXXXXXXX"anonymous":Xadmin["is_anonymous"],
XXXXXXXXXXXXXXXX"can_change_info":Xadmin["can_change_info"],
XXXXXXXXXXXXXXXX"can_delete_messages":Xadmin["can_delete_messages"],
XXXXXXXXXXXXXXXX"can_invite_users":Xadmin["can_invite_users"],
XXXXXXXXXXXXXXXX"can_restrict_members":Xadmin["can_restrict_members"],
XXXXXXXXXXXXXXXX"can_pin_messages":Xadmin["can_pin_messages"],
XXXXXXXXXXXXXXXX"can_promote_members":Xadmin["can_promote_members"],
XXXXXXXXXXXX}

XXXXXXXXXXXXwithXsuppress(KeyError):XX#XOptionalXpermissions
XXXXXXXXXXXXXXXXalist[user_id]["can_post_messages"]X=Xadmin["can_post_messages"]

XXXXXXXXbredis.set(key,Xpickle.dumps(alist))
XXXXXXXXbredis.expire(key,X900)
XXXXreturnXalist


asyncXdefXis_user_admin(chat_id,Xuser_id):
XXXX#XUser'sXpmXshouldXhaveXadminXrights
XXXXifXchat_idX==Xuser_id:
XXXXXXXXreturnXTrue

XXXXifXuser_idXinXOPERATORS:
XXXXXXXXreturnXTrue

XXXX#XWorkaroundXtoXsupportXanonymousXadmins
XXXXifXuser_idX==X1087968824:
XXXXXXXXreturnXTrue

XXXXtry:
XXXXXXXXadminsX=XawaitXget_admins_rights(chat_id)
XXXXexceptXBadRequest:
XXXXXXXXreturnXFalse
XXXXelse:
XXXXXXXXifXuser_idXinXadmins:
XXXXXXXXXXXXreturnXTrue
XXXXXXXXelse:
XXXXXXXXXXXXreturnXFalse


asyncXdefXcheck_admin_rights(
XXXXevent:XUnion[Message,XCallbackQuery],Xchat_id,Xuser_id,Xrights
):
XXXX#XUser'sXpmXshouldXhaveXadminXrights
XXXXifXchat_idX==Xuser_id:
XXXXXXXXreturnXTrue

XXXXifXuser_idXinXOPERATORS:
XXXXXXXXreturnXTrue

XXXX#XWorkaroundXtoXsupportXanonymousXadmins
XXXXifXuser_idX==X1087968824:
XXXXXXXXifXnotXisinstance(event,XMessage):
XXXXXXXXXXXXraiseXValueError(
XXXXXXXXXXXXXXXXf"CannotXextractXsignuatureXofXanonymousXadminXfromX{type(event)}"
XXXXXXXXXXXX)

XXXXXXXXifXnotXevent.author_signature:
XXXXXXXXXXXXreturnXTrue

XXXXXXXXforXadminXinX(awaitXget_admins_rights(chat_id)).values():
XXXXXXXXXXXXifX"title"XinXadminXandXadmin["title"]X==Xevent.author_signature:
XXXXXXXXXXXXXXXXforXpermissionXinXrights:
XXXXXXXXXXXXXXXXXXXXifXnotXadmin[permission]:
XXXXXXXXXXXXXXXXXXXXXXXXreturnXpermission
XXXXXXXXreturnXTrue

XXXXadmin_rightsX=XawaitXget_admins_rights(chat_id)
XXXXifXuser_idXnotXinXadmin_rights:
XXXXXXXXreturnXFalse

XXXXifXadmin_rights[user_id]["status"]X==X"creator":
XXXXXXXXreturnXTrue

XXXXforXpermissionXinXrights:
XXXXXXXXifXnotXadmin_rights[user_id][permission]:
XXXXXXXXXXXXreturnXpermission

XXXXreturnXTrue


asyncXdefXcheck_group_admin(event,Xuser_id,Xno_msg=False):
XXXXifXhasattr(event,X"chat_id"):
XXXXXXXXchat_idX=Xevent.chat_id
XXXXelifXhasattr(event,X"chat"):
XXXXXXXXchat_idX=Xevent.chat.id
XXXXifXawaitXis_user_admin(chat_id,Xuser_id)XisXTrue:
XXXXXXXXreturnXTrue
XXXXelse:
XXXXXXXXifXno_msgXisXFalse:
XXXXXXXXXXXXawaitXevent.reply("YouXshouldXbeXaXadminXtoXdoXit!")
XXXXXXXXreturnXFalse


asyncXdefXis_chat_creator(event:XUnion[Message,XCallbackQuery],Xchat_id,Xuser_id):
XXXXadmin_rightsX=XawaitXget_admins_rights(chat_id)

XXXXifXuser_idX==X1087968824:
XXXXXXXX_co,Xpossible_creatorX=X0,XNone
XXXXXXXXforXadminXinXadmin_rights.values():
XXXXXXXXXXXXifXadmin["title"]X==Xevent.author_signature:
XXXXXXXXXXXXXXXX_coX+=X1
XXXXXXXXXXXXXXXXpossible_creatorX=Xadmin

XXXXXXXXifX_coX>X1:
XXXXXXXXXXXXawaitXevent.answer(
XXXXXXXXXXXXXXXXawaitXget_string(chat_id,X"global",X"unable_identify_creator")
XXXXXXXXXXXX)
XXXXXXXXXXXXraiseXSkipHandler

XXXXXXXXifXpossible_creator["status"]X==X"creator":
XXXXXXXXXXXXreturnXTrue
XXXXXXXXreturnXFalse

XXXXifXuser_idXnotXinXadmin_rights:
XXXXXXXXreturnXFalse

XXXXifXadmin_rights[user_id]["status"]X==X"creator":
XXXXXXXXreturnXTrue

XXXXreturnXFalse


asyncXdefXget_user_by_text(message,Xtext:Xstr):
XXXX#XGetXallXentities
XXXXentitiesX=Xfilter(
XXXXXXXXlambdaXent:Xent["type"]X==X"text_mention"XorXent["type"]X==X"mention",
XXXXXXXXmessage.entities,
XXXX)
XXXXforXentityXinXentities:
XXXXXXXX#XIfXusernameXmatchesXentity'sXtext
XXXXXXXXifXtextXinXentity.get_text(message.text):
XXXXXXXXXXXXifXentity.typeX==X"mention":
XXXXXXXXXXXXXXXX#XThisXoneXentityXisXcomesXwithXmentionXbyXusername,XlikeX@rInerukiBot
XXXXXXXXXXXXXXXXreturnXawaitXget_user_by_username(text)
XXXXXXXXXXXXelifXentity.typeX==X"text_mention":
XXXXXXXXXXXXXXXX#XThisXoneXisXlinkXmention,XmostlyXusedXforXusersXwithoutXanXusername
XXXXXXXXXXXXXXXXreturnXawaitXget_user_by_id(entity.user.id)

XXXX#XNowXlet'sXtryXgetXuserXwithXuser_id
XXXX#XWeXtryingXthisXnotXfirstXbecauseXuserXlinkXmentionXalsoXcanXhaveXnumbers
XXXXifXtext.isdigit():
XXXXXXXXuser_idX=Xint(text)
XXXXXXXXifXuserX:=XawaitXget_user_by_id(user_id):
XXXXXXXXXXXXreturnXuser

XXXX#XNotXfoundXanythingX😞
XXXXreturnXNone


asyncXdefXget_user(message,Xallow_self=False):
XXXXargsX=Xmessage.text.split(None,X2)
XXXXuserX=XNone

XXXX#XOnlyX1Xway
XXXXifXlen(args)X<X2XandX"reply_to_message"XinXmessage:
XXXXXXXXreturnXawaitXget_user_by_id(message.reply_to_message.from_user.id)

XXXX#XUseXdefaultXfunctionXtoXgetXuser
XXXXifXlen(args)X>X1:
XXXXXXXXuserX=XawaitXget_user_by_text(message,Xargs[1])

XXXXifXnotXuserXandXbool(message.reply_to_message):
XXXXXXXXuserX=XawaitXget_user_by_id(message.reply_to_message.from_user.id)

XXXXifXnotXuserXandXallow_self:
XXXXXXXX#XTODO:XFetchXuserXfromXmessageXinsteadXofXdb?!XlessXoverhead
XXXXXXXXreturnXawaitXget_user_by_id(message.from_user.id)

XXXX#XNoXargsXandXnoXwayXtoXgetXuser
XXXXifXnotXuserXandXlen(args)X<X2:
XXXXXXXXreturnXNone

XXXXreturnXuser


asyncXdefXget_user_and_text(message,X**kwargs):
XXXXargsX=Xmessage.text.split("X",X2)
XXXXuserX=XawaitXget_user(message,X**kwargs)

XXXXifXlen(args)X>X1:
XXXXXXXXifX(test_userX:=XawaitXget_user_by_text(message,Xargs[1]))X==Xuser:
XXXXXXXXXXXXifXtest_user:
XXXXXXXXXXXXXXXXprint(len(args))
XXXXXXXXXXXXXXXXifXlen(args)X>X2:
XXXXXXXXXXXXXXXXXXXXreturnXuser,Xargs[2]
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXreturnXuser,X""

XXXXifXlen(args)X>X1:
XXXXXXXXreturnXuser,Xmessage.text.split("X",X1)[1]
XXXXelse:
XXXXXXXXreturnXuser,X""


asyncXdefXget_users(message):
XXXXargsX=Xmessage.text.split(None,X2)
XXXXtextX=Xargs[1]
XXXXusersX=X[]

XXXXforXtextXinXtext.split("|"):
XXXXXXXXifXuserX:=XawaitXget_user_by_text(message,Xtext):
XXXXXXXXXXXXusers.append(user)

XXXXreturnXusers


asyncXdefXget_users_and_text(message):
XXXXusersX=XawaitXget_users(message)
XXXXargsX=Xmessage.text.split(None,X2)

XXXXifXlen(args)X>X1:
XXXXXXXXreturnXusers,Xargs[1]
XXXXelse:
XXXXXXXXreturnXusers,X""


defXget_user_and_text_dec(**dec_kwargs):
XXXXdefXwrapped(func):
XXXXXXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXXXXXmessageX=Xargs[0]
XXXXXXXXXXXXifXhasattr(message,X"message"):
XXXXXXXXXXXXXXXXmessageX=Xmessage.message

XXXXXXXXXXXXuser,XtextX=XawaitXget_user_and_text(message,X**dec_kwargs)
XXXXXXXXXXXXifXnotXuser:
XXXXXXXXXXXXXXXXawaitXmessage.reply("IXcan'tXgetXtheXuser!")
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXreturnXawaitXfunc(*args,Xuser,Xtext,X**kwargs)

XXXXXXXXreturnXwrapped_1

XXXXreturnXwrapped


defXget_user_dec(**dec_kwargs):
XXXXdefXwrapped(func):
XXXXXXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXXXXXmessageX=Xargs[0]
XXXXXXXXXXXXifXhasattr(message,X"message"):
XXXXXXXXXXXXXXXXmessageX=Xmessage.message

XXXXXXXXXXXXuser,XtextX=XawaitXget_user_and_text(message,X**dec_kwargs)
XXXXXXXXXXXXifXnotXbool(user):
XXXXXXXXXXXXXXXXawaitXmessage.reply("IXcan'tXgetXtheXuser!")
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXreturnXawaitXfunc(*args,Xuser,X**kwargs)

XXXXXXXXreturnXwrapped_1

XXXXreturnXwrapped


defXget_chat_dec(allow_self=False,Xfed=False):
XXXXdefXwrapped(func):
XXXXXXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXXXXXmessageX=Xargs[0]
XXXXXXXXXXXXifXhasattr(message,X"message"):
XXXXXXXXXXXXXXXXmessageX=Xmessage.message

XXXXXXXXXXXXargX=Xget_arg(message)
XXXXXXXXXXXXifXfedXisXTrue:
XXXXXXXXXXXXXXXXifXlen(textX:=Xmessage.get_args().split())X>X1:
XXXXXXXXXXXXXXXXXXXXifXtext[0].count("-")X==X4:
XXXXXXXXXXXXXXXXXXXXXXXXargX=Xtext[1]
XXXXXXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXXXXXargX=Xtext[0]

XXXXXXXXXXXXifXarg.startswith("-")XorXarg.isdigit():
XXXXXXXXXXXXXXXXchatX=XawaitXdb.chat_list.find_one({"chat_id":Xint(arg)})
XXXXXXXXXXXXXXXXifXnotXchat:
XXXXXXXXXXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXXXXXXXXXchatX=XawaitXbot.get_chat(arg)
XXXXXXXXXXXXXXXXXXXXexceptXChatNotFound:
XXXXXXXXXXXXXXXXXXXXXXXXreturnXawaitXmessage.reply(
XXXXXXXXXXXXXXXXXXXXXXXXXXXX"IXcouldn'tXfindXtheXchat/channel!XMaybeXIXamXnotXthere!"
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXexceptXUnauthorized:
XXXXXXXXXXXXXXXXXXXXXXXXreturnXawaitXmessage.reply(
XXXXXXXXXXXXXXXXXXXXXXXXXXXX"IXcouldn'tXaccessXchat/channel!XMaybeXIXwasXkickedXfromXthere!"
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXelifXarg.startswith("@"):
XXXXXXXXXXXXXXXXchatX=XawaitXdb.chat_list.find_one(
XXXXXXXXXXXXXXXXXXXX{"chat_nick":Xre.compile(arg.strip("@"),Xre.IGNORECASE)}
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXelifXallow_selfXisXTrue:
XXXXXXXXXXXXXXXXchatX=XawaitXdb.chat_list.find_one({"chat_id":Xmessage.chat.id})
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXawaitXmessage.reply("PleaseXgiveXmeXvalidXchatXID/username")
XXXXXXXXXXXXXXXXreturn

XXXXXXXXXXXXifXnotXchat:
XXXXXXXXXXXXXXXXawaitXmessage.reply("IXcan'tXfindXanyXchatsXonXgivenXinformation!")
XXXXXXXXXXXXXXXXreturn

XXXXXXXXXXXXreturnXawaitXfunc(*args,Xchat,X**kwargs)

XXXXXXXXreturnXwrapped_1

XXXXreturnXwrapped
