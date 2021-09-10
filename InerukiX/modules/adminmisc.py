#XCopyrightX(C)X2021XAlainXX&errorshivansh

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

importXos
fromXtimeXimportXsleep

fromXtelethonXimportX*
fromXtelethonXimportXevents
fromXtelethon.errorsXimportX*
fromXtelethon.errorsXimportXFloodWaitError
fromXtelethon.tlXimportX*
fromXtelethon.tlXimportXfunctions,Xtypes
fromXtelethon.tl.functions.channelsXimportXEditAdminRequest,XEditBannedRequest
fromXtelethon.tl.typesXimportX*
fromXtelethon.tl.typesXimportX(
XXXXChatAdminRights,
XXXXChatBannedRights,
XXXXMessageEntityMentionName,
)

fromXInerukiXXimportXOWNER_ID
fromXInerukiX.services.telethonXimportXtbotXasXbot

#X===================XCONSTANTX===================
PP_TOO_SMOLX=X"**TheXimageXisXtooXsmall**"
PP_ERRORX=X"**FailureXwhileXprocessingXimage**"
NO_ADMINX=X"**IXamXnotXanXadmin**"
NO_PERMX=X"**IXdon'tXhaveXsufficientXpermissions!**"

CHAT_PP_CHANGEDX=X"**ChatXPictureXChanged**"
CHAT_PP_ERRORX=X(
XXXX"**SomeXissueXwithXupdatingXtheXpic,**"
XXXX"**maybeXyouXaren'tXanXadmin,**"
XXXX"**orXdon'tXhaveXtheXdesiredXrights.**"
)
INVALID_MEDIAX=X"InvalidXExtension"
BANNED_RIGHTSX=XChatBannedRights(
XXXXuntil_date=None,
XXXXview_messages=True,
XXXXsend_messages=True,
XXXXsend_media=True,
XXXXsend_stickers=True,
XXXXsend_gifs=True,
XXXXsend_games=True,
XXXXsend_inline=True,
XXXXembed_links=True,
)
UNBAN_RIGHTSX=XChatBannedRights(
XXXXuntil_date=None,
XXXXsend_messages=None,
XXXXsend_media=None,
XXXXsend_stickers=None,
XXXXsend_gifs=None,
XXXXsend_games=None,
XXXXsend_inline=None,
XXXXembed_links=None,
)
KICK_RIGHTSX=XChatBannedRights(until_date=None,Xview_messages=True)
MUTE_RIGHTSX=XChatBannedRights(until_date=None,Xsend_messages=True)
UNMUTE_RIGHTSX=XChatBannedRights(until_date=None,Xsend_messages=False)


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXbot(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXifXisinstance(chat,Xtypes.InputPeerUser):
XXXXXXXXreturnXTrue


asyncXdefXcan_promote_users(message):
XXXXresultX=XawaitXbot(
XXXXXXXXfunctions.channels.GetParticipantRequest(
XXXXXXXXXXXXchannel=message.chat_id,
XXXXXXXXXXXXuser_id=message.sender_id,
XXXXXXXX)
XXXX)
XXXXpX=Xresult.participant
XXXXreturnXisinstance(p,Xtypes.ChannelParticipantCreator)XorX(
XXXXXXXXisinstance(p,Xtypes.ChannelParticipantAdmin)XandXp.admin_rights.ban_users
XXXX)


asyncXdefXcan_ban_users(message):
XXXXresultX=XawaitXbot(
XXXXXXXXfunctions.channels.GetParticipantRequest(
XXXXXXXXXXXXchannel=message.chat_id,
XXXXXXXXXXXXuser_id=message.sender_id,
XXXXXXXX)
XXXX)
XXXXpX=Xresult.participant
XXXXreturnXisinstance(p,Xtypes.ChannelParticipantCreator)XorX(
XXXXXXXXisinstance(p,Xtypes.ChannelParticipantAdmin)XandXp.admin_rights.ban_users
XXXX)


asyncXdefXcan_change_info(message):
XXXXresultX=XawaitXbot(
XXXXXXXXfunctions.channels.GetParticipantRequest(
XXXXXXXXXXXXchannel=message.chat_id,
XXXXXXXXXXXXuser_id=message.sender_id,
XXXXXXXX)
XXXX)
XXXXpX=Xresult.participant
XXXXreturnXisinstance(p,Xtypes.ChannelParticipantCreator)XorX(
XXXXXXXXisinstance(p,Xtypes.ChannelParticipantAdmin)XandXp.admin_rights.change_info
XXXX)


asyncXdefXcan_del(message):
XXXXresultX=XawaitXbot(
XXXXXXXXfunctions.channels.GetParticipantRequest(
XXXXXXXXXXXXchannel=message.chat_id,
XXXXXXXXXXXXuser_id=message.sender_id,
XXXXXXXX)
XXXX)
XXXXpX=Xresult.participant
XXXXreturnXisinstance(p,Xtypes.ChannelParticipantCreator)XorX(
XXXXXXXXisinstance(p,Xtypes.ChannelParticipantAdmin)XandXp.admin_rights.delete_messages
XXXX)


asyncXdefXcan_pin_msg(message):
XXXXresultX=XawaitXbot(
XXXXXXXXfunctions.channels.GetParticipantRequest(
XXXXXXXXXXXXchannel=message.chat_id,
XXXXXXXXXXXXuser_id=message.sender_id,
XXXXXXXX)
XXXX)
XXXXpX=Xresult.participant
XXXXreturnXisinstance(p,Xtypes.ChannelParticipantCreator)XorX(
XXXXXXXXisinstance(p,Xtypes.ChannelParticipantAdmin)XandXp.admin_rights.pin_messages
XXXX)


asyncXdefXget_user_sender_id(user,Xevent):
XXXXifXisinstance(user,Xstr):
XXXXXXXXuserX=Xint(user)

XXXXtry:
XXXXXXXXuser_objX=XawaitXbot.get_entity(user)
XXXXexceptX(TypeError,XValueError)XasXerr:
XXXXXXXXawaitXevent.edit(str(err))
XXXXXXXXreturnXNone

XXXXreturnXuser_obj


asyncXdefXget_user_from_event(event):
XXXX"""GetXtheXuserXfromXargumentXorXrepliedXmessage."""
XXXXifXevent.reply_to_msg_id:
XXXXXXXXprevious_messageX=XawaitXevent.get_reply_message()
XXXXXXXXuser_objX=XawaitXbot.get_entity(previous_message.sender_id)
XXXXelse:
XXXXXXXXuserX=Xevent.pattern_match.group(1)

XXXXXXXXifXuser.isnumeric():
XXXXXXXXXXXXuserX=Xint(user)

XXXXXXXXifXnotXuser:
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"**IXdon'tXknowXwhoXyou'reXtalkingXabout,Xyou'reXgoingXtoXneedXtoXspecifyXaXuser...!**"
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn

XXXXXXXXifXevent.message.entitiesXisXnotXNone:
XXXXXXXXXXXXprobable_user_mention_entityX=Xevent.message.entities[0]

XXXXXXXXXXXXifXisinstance(probable_user_mention_entity,XMessageEntityMentionName):
XXXXXXXXXXXXXXXXuser_idX=Xprobable_user_mention_entity.user_id
XXXXXXXXXXXXXXXXuser_objX=XawaitXbot.get_entity(user_id)
XXXXXXXXXXXXXXXXreturnXuser_obj
XXXXXXXXtry:
XXXXXXXXXXXXuser_objX=XawaitXbot.get_entity(user)
XXXXXXXXexceptX(TypeError,XValueError)XasXerr:
XXXXXXXXXXXXawaitXevent.reply(str(err))
XXXXXXXXXXXXreturnXNone

XXXXreturnXuser_obj


defXfind_instance(items,Xclass_or_tuple):
XXXXforXitemXinXitems:
XXXXXXXXifXisinstance(item,Xclass_or_tuple):
XXXXXXXXXXXXreturnXitem
XXXXreturnXNone


@bot.on(events.NewMessage(pattern="/lowpromoteX?(.*)"))
asyncXdefXlowpromote(promt):
XXXXifXpromt.is_group:
XXXXXXXXifXpromt.sender_idX==XOWNER_ID:
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXifXnotXawaitXcan_promote_users(message=promt):
XXXXXXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXuserX=XawaitXget_user_from_event(promt)
XXXXifXpromt.is_group:
XXXXXXXXifXawaitXis_register_admin(promt.input_chat,Xuser.id):
XXXXXXXXXXXXawaitXpromt.reply("**Well!XiXcantXpromoteXuserXwhoXisXalreadyXanXadmin**")
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXnew_rightsX=XChatAdminRights(
XXXXXXXXadd_admins=False,
XXXXXXXXinvite_users=True,
XXXXXXXXchange_info=False,
XXXXXXXXban_users=False,
XXXXXXXXdelete_messages=True,
XXXXXXXXpin_messages=False,
XXXX)

XXXXifXuser:
XXXXXXXXpass
XXXXelse:
XXXXXXXXreturn
XXXXquewX=Xpromt.pattern_match.group(1)
XXXXifXquew:
XXXXXXXXtitleX=Xquew
XXXXelse:
XXXXXXXXtitleX=X"Moderator"
XXXX#XTryXtoXpromoteXifXcurrentXuserXisXadminXorXcreator
XXXXtry:
XXXXXXXXawaitXbot(EditAdminRequest(promt.chat_id,Xuser.id,Xnew_rights,Xtitle))
XXXXXXXXawaitXpromt.reply("**SuccessfullyXpromoted!**")

XXXX#XIfXTelethonXspitXBadRequestError,Xassume
XXXX#XweXdon'tXhaveXPromoteXpermission
XXXXexceptXException:
XXXXXXXXawaitXpromt.reply("FailedXtoXpromote.")
XXXXXXXXreturn


@bot.on(events.NewMessage(pattern="/midpromoteX?(.*)"))
asyncXdefXmidpromote(promt):
XXXXifXpromt.is_group:
XXXXXXXXifXpromt.sender_idX==XOWNER_ID:
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXifXnotXawaitXcan_promote_users(message=promt):
XXXXXXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXuserX=XawaitXget_user_from_event(promt)
XXXXifXpromt.is_group:
XXXXXXXXifXawaitXis_register_admin(promt.input_chat,Xuser.id):
XXXXXXXXXXXXawaitXpromt.reply("**Well!XiXcantXpromoteXuserXwhoXisXalreadyXanXadmin**")
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXnew_rightsX=XChatAdminRights(
XXXXXXXXadd_admins=False,
XXXXXXXXinvite_users=True,
XXXXXXXXchange_info=True,
XXXXXXXXban_users=False,
XXXXXXXXdelete_messages=True,
XXXXXXXXpin_messages=True,
XXXX)

XXXXifXuser:
XXXXXXXXpass
XXXXelse:
XXXXXXXXreturn
XXXXquewX=Xpromt.pattern_match.group(1)
XXXXifXquew:
XXXXXXXXtitleX=Xquew
XXXXelse:
XXXXXXXXtitleX=X"Admin"
XXXX#XTryXtoXpromoteXifXcurrentXuserXisXadminXorXcreator
XXXXtry:
XXXXXXXXawaitXbot(EditAdminRequest(promt.chat_id,Xuser.id,Xnew_rights,Xtitle))
XXXXXXXXawaitXpromt.reply("**SuccessfullyXpromoted!**")

XXXX#XIfXTelethonXspitXBadRequestError,Xassume
XXXX#XweXdon'tXhaveXPromoteXpermission
XXXXexceptXException:
XXXXXXXXawaitXpromt.reply("FailedXtoXpromote.")
XXXXXXXXreturn


@bot.on(events.NewMessage(pattern="/highpromoteX?(.*)"))
asyncXdefXhighpromote(promt):
XXXXifXpromt.is_group:
XXXXXXXXifXpromt.sender_idX==XOWNER_ID:
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXifXnotXawaitXcan_promote_users(message=promt):
XXXXXXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXuserX=XawaitXget_user_from_event(promt)
XXXXifXpromt.is_group:
XXXXXXXXifXawaitXis_register_admin(promt.input_chat,Xuser.id):
XXXXXXXXXXXXawaitXpromt.reply("**Well!XiXcantXpromoteXuserXwhoXisXalreadyXanXadmin**")
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXnew_rightsX=XChatAdminRights(
XXXXXXXXadd_admins=True,
XXXXXXXXinvite_users=True,
XXXXXXXXchange_info=True,
XXXXXXXXban_users=True,
XXXXXXXXdelete_messages=True,
XXXXXXXXpin_messages=True,
XXXX)

XXXXifXuser:
XXXXXXXXpass
XXXXelse:
XXXXXXXXreturn
XXXXquewX=Xpromt.pattern_match.group(1)
XXXXifXquew:
XXXXXXXXtitleX=Xquew
XXXXelse:
XXXXXXXXtitleX=X"Admin"
XXXX#XTryXtoXpromoteXifXcurrentXuserXisXadminXorXcreator
XXXXtry:
XXXXXXXXawaitXbot(EditAdminRequest(promt.chat_id,Xuser.id,Xnew_rights,Xtitle))
XXXXXXXXawaitXpromt.reply("**SuccessfullyXpromoted!**")

XXXX#XIfXTelethonXspitXBadRequestError,Xassume
XXXX#XweXdon'tXhaveXPromoteXpermission
XXXXexceptXException:
XXXXXXXXawaitXpromt.reply("FailedXtoXpromote.")
XXXXXXXXreturn


@bot.on(events.NewMessage(pattern="/lowdemote(?:X|$)(.*)"))
asyncXdefXlowdemote(dmod):
XXXXifXdmod.is_group:
XXXXXXXXifXnotXawaitXcan_promote_users(message=dmod):
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXuserX=XawaitXget_user_from_event(dmod)
XXXXifXdmod.is_group:
XXXXXXXXifXnotXawaitXis_register_admin(dmod.input_chat,Xuser.id):
XXXXXXXXXXXXawaitXdmod.reply("**Hehe,XiXcantXdemoteXnon-admin**")
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXifXuser:
XXXXXXXXpass
XXXXelse:
XXXXXXXXreturn

XXXX#XNewXrightsXafterXdemotion
XXXXnewrightsX=XChatAdminRights(
XXXXXXXXadd_admins=False,
XXXXXXXXinvite_users=True,
XXXXXXXXchange_info=False,
XXXXXXXXban_users=False,
XXXXXXXXdelete_messages=True,
XXXXXXXXpin_messages=False,
XXXX)
XXXX#XEditXAdminXPermission
XXXXtry:
XXXXXXXXawaitXbot(EditAdminRequest(dmod.chat_id,Xuser.id,Xnewrights,X"Admin"))
XXXXXXXXawaitXdmod.reply("**DemotedXSuccessfully!**")

XXXX#XIfXweXcatchXBadRequestErrorXfromXTelethon
XXXX#XAssumeXweXdon'tXhaveXpermissionXtoXdemote
XXXXexceptXException:
XXXXXXXXawaitXdmod.reply("**FailedXtoXdemote.**")
XXXXXXXXreturn


@bot.on(events.NewMessage(pattern="/middemote(?:X|$)(.*)"))
asyncXdefXmiddemote(dmod):
XXXXifXdmod.is_group:
XXXXXXXXifXnotXawaitXcan_promote_users(message=dmod):
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXuserX=XawaitXget_user_from_event(dmod)
XXXXifXdmod.is_group:
XXXXXXXXifXnotXawaitXis_register_admin(dmod.input_chat,Xuser.id):
XXXXXXXXXXXXawaitXdmod.reply("**Hehe,XiXcantXdemoteXnon-admin**")
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXifXuser:
XXXXXXXXpass
XXXXelse:
XXXXXXXXreturn

XXXX#XNewXrightsXafterXdemotion
XXXXnewrightsX=XChatAdminRights(
XXXXXXXXadd_admins=False,
XXXXXXXXinvite_users=True,
XXXXXXXXchange_info=True,
XXXXXXXXban_users=False,
XXXXXXXXdelete_messages=True,
XXXXXXXXpin_messages=True,
XXXX)
XXXX#XEditXAdminXPermission
XXXXtry:
XXXXXXXXawaitXbot(EditAdminRequest(dmod.chat_id,Xuser.id,Xnewrights,X"Admin"))
XXXXXXXXawaitXdmod.reply("**DemotedXSuccessfully!**")

XXXX#XIfXweXcatchXBadRequestErrorXfromXTelethon
XXXX#XAssumeXweXdon'tXhaveXpermissionXtoXdemote
XXXXexceptXException:
XXXXXXXXawaitXdmod.reply("**FailedXtoXdemote.**")
XXXXXXXXreturn


@bot.on(events.NewMessage(pattern="/users$"))
asyncXdefXget_users(show):
XXXXifXnotXshow.is_group:
XXXXXXXXreturn
XXXXifXshow.is_group:
XXXXXXXXifXnotXawaitXis_register_admin(show.input_chat,Xshow.sender_id):
XXXXXXXXXXXXreturn
XXXXinfoX=XawaitXbot.get_entity(show.chat_id)
XXXXtitleX=Xinfo.titleXifXinfo.titleXelseX"thisXchat"
XXXXmentionsX=X"UsersXinX{}:X\n".format(title)
XXXXasyncXforXuserXinXbot.iter_participants(show.chat_id):
XXXXXXXXifXnotXuser.deleted:
XXXXXXXXXXXXmentionsX+=Xf"\n[{user.first_name}](tg://user?id={user.id})X{user.id}"
XXXXXXXXelse:
XXXXXXXXXXXXmentionsX+=Xf"\nDeletedXAccountX{user.id}"
XXXXfileX=Xopen("userslist.txt",X"w+")
XXXXfile.write(mentions)
XXXXfile.close()
XXXXawaitXbot.send_file(
XXXXXXXXshow.chat_id,
XXXXXXXX"userslist.txt",
XXXXXXXXcaption="UsersXinX{}".format(title),
XXXXXXXXreply_to=show.id,
XXXX)
XXXXos.remove("userslist.txt")


@bot.on(events.NewMessage(pattern="/kickthefools$"))
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn

XXXXifXevent.is_group:
XXXXXXXXifXnotXawaitXcan_ban_users(message=event):
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXX#XHereXlayingXtheXsanityXcheck
XXXXchatX=XawaitXevent.get_chat()
XXXXadminX=Xchat.admin_rights.ban_users
XXXXcreatorX=Xchat.creator

XXXX#XWell
XXXXifXnotXadminXandXnotXcreator:
XXXXXXXXawaitXevent.reply("`IXdon'tXhaveXenoughXpermissions!`")
XXXXXXXXreturn

XXXXcX=X0
XXXXKICK_RIGHTSX=XChatBannedRights(until_date=None,Xview_messages=True)
XXXXdoneX=XawaitXevent.reply("WorkingX...")
XXXXasyncXforXiXinXbot.iter_participants(event.chat_id):

XXXXXXXXifXisinstance(i.status,XUserStatusLastMonth):
XXXXXXXXXXXXstatusX=XawaitXtbot(EditBannedRequest(event.chat_id,Xi,XKICK_RIGHTS))
XXXXXXXXXXXXifXnotXstatus:
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXcX=XcX+X1

XXXXXXXXifXisinstance(i.status,XUserStatusLastWeek):
XXXXXXXXXXXXstatusX=XawaitXtbot(EditBannedRequest(event.chat_id,Xi,XKICK_RIGHTS))
XXXXXXXXXXXXifXnotXstatus:
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXcX=XcX+X1

XXXXifXcX==X0:
XXXXXXXXawaitXdone.edit("GotXnoXoneXtoXkickX😔")
XXXXXXXXreturn

XXXXrequired_stringX=X"SuccessfullyXKickedX**{}**Xusers"
XXXXawaitXevent.reply(required_string.format(c))


@bot.on(events.NewMessage(pattern="/unbanall$"))
asyncXdefX_(event):
XXXXifXnotXevent.is_group:
XXXXXXXXreturn

XXXXifXevent.is_group:
XXXXXXXXifXnotXawaitXcan_ban_users(message=event):
XXXXXXXXXXXXreturn

XXXX#XHereXlayingXtheXsanityXcheck
XXXXchatX=XawaitXevent.get_chat()
XXXXadminX=Xchat.admin_rights.ban_users
XXXXcreatorX=Xchat.creator

XXXX#XWell
XXXXifXnotXadminXandXnotXcreator:
XXXXXXXXawaitXevent.reply("`IXdon'tXhaveXenoughXpermissions!`")
XXXXXXXXreturn

XXXXdoneX=XawaitXevent.reply("SearchingXParticipantXLists.")
XXXXpX=X0
XXXXasyncXforXiXinXbot.iter_participants(
XXXXXXXXevent.chat_id,Xfilter=ChannelParticipantsKicked,Xaggressive=True
XXXX):
XXXXXXXXrightsX=XChatBannedRights(until_date=0,Xview_messages=False)
XXXXXXXXtry:
XXXXXXXXXXXXawaitXbot(functions.channels.EditBannedRequest(event.chat_id,Xi,Xrights))
XXXXXXXXexceptXFloodWaitErrorXasXex:
XXXXXXXXXXXXlogger.warn("sleepingXforX{}Xseconds".format(ex.seconds))
XXXXXXXXXXXXsleep(ex.seconds)
XXXXXXXXexceptXExceptionXasXex:
XXXXXXXXXXXXawaitXevent.reply(str(ex))
XXXXXXXXelse:
XXXXXXXXXXXXpX+=X1

XXXXifXpX==X0:
XXXXXXXXawaitXdone.edit("NoXoneXisXbannedXinXthisXchat")
XXXXXXXXreturn
XXXXrequired_stringX=X"SuccessfullyXunbannedX**{}**Xusers"
XXXXawaitXevent.reply(required_string.format(p))


@bot.on(events.NewMessage(pattern="/unmuteall$"))
asyncXdefX_(event):
XXXXifXnotXevent.is_group:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXnotXawaitXcan_ban_users(message=event):
XXXXXXXXXXXXreturn

XXXX#XHereXlayingXtheXsanityXcheck
XXXXchatX=XawaitXevent.get_chat()
XXXXadminX=Xchat.admin_rights.ban_users
XXXXcreatorX=Xchat.creator

XXXX#XWell
XXXXifXnotXadminXandXnotXcreator:
XXXXXXXXawaitXevent.reply("`IXdon'tXhaveXenoughXpermissions!`")
XXXXXXXXreturn

XXXXdoneX=XawaitXevent.reply("WorkingX...")
XXXXpX=X0
XXXXasyncXforXiXinXbot.iter_participants(
XXXXXXXXevent.chat_id,Xfilter=ChannelParticipantsBanned,Xaggressive=True
XXXX):
XXXXXXXXrightsX=XChatBannedRights(
XXXXXXXXXXXXuntil_date=0,
XXXXXXXXXXXXsend_messages=False,
XXXXXXXX)
XXXXXXXXtry:
XXXXXXXXXXXXawaitXbot(functions.channels.EditBannedRequest(event.chat_id,Xi,Xrights))
XXXXXXXXexceptXFloodWaitErrorXasXex:
XXXXXXXXXXXXlogger.warn("sleepingXforX{}Xseconds".format(ex.seconds))
XXXXXXXXXXXXsleep(ex.seconds)
XXXXXXXXexceptXExceptionXasXex:
XXXXXXXXXXXXawaitXevent.reply(str(ex))
XXXXXXXXelse:
XXXXXXXXXXXXpX+=X1

XXXXifXpX==X0:
XXXXXXXXawaitXdone.edit("NoXoneXisXmutedXinXthisXchat")
XXXXXXXXreturn
XXXXrequired_stringX=X"SuccessfullyXunmutedX**{}**Xusers"
XXXXawaitXevent.reply(required_string.format(p))


@bot.on(events.NewMessage(pattern="/banme$"))
asyncXdefXbanme(bon):
XXXXifXnotXbon.is_group:
XXXXXXXXreturn

XXXXtry:
XXXXXXXXawaitXbot(EditBannedRequest(bon.chat_id,Xsender,XBANNED_RIGHTS))
XXXXXXXXawaitXbon.reply("OkXBannedX!")

XXXXexceptXException:
XXXXXXXXawaitXbon.reply("IXdon'tXthinkXso!")
XXXXXXXXreturn


@bot.on(events.NewMessage(pattern="/kickme$"))
asyncXdefXkickme(bon):
XXXXifXnotXbon.is_group:
XXXXXXXXreturn
XXXXtry:
XXXXXXXXawaitXbot.kick_participant(bon.chat_id,Xbon.sender_id)
XXXXXXXXawaitXbon.reply("Sure!")
XXXXexceptXException:
XXXXXXXXawaitXbon.reply("FailedXtoXkickX!")
XXXXXXXXreturn


@bot.on(events.NewMessage(pattern=r"/setdescriptionX([\s\S]*)"))
asyncXdefXset_group_des(gpic):
XXXXinput_strX=Xgpic.pattern_match.group(1)
XXXX#Xprint(input_str)
XXXXifXgpic.is_group:
XXXXXXXXifXnotXawaitXcan_change_info(message=gpic):
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXtry:
XXXXXXXXawaitXbot(
XXXXXXXXXXXXfunctions.messages.EditChatAboutRequest(peer=gpic.chat_id,Xabout=input_str)
XXXXXXXX)
XXXXXXXXawaitXgpic.reply("SuccessfullyXsetXnewXgroupXdescription.")
XXXXexceptXBaseException:
XXXXXXXXawaitXgpic.reply("FailedXtoXsetXgroupXdescription.")


@bot.on(events.NewMessage(pattern="/setsticker$"))
asyncXdefXset_group_sticker(gpic):
XXXXifXgpic.is_group:
XXXXXXXXifXnotXawaitXcan_change_info(message=gpic):
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXrep_msgX=XawaitXgpic.get_reply_message()
XXXXifXnotXrep_msg.document:
XXXXXXXXawaitXgpic.reply("ReplyXtoXanyXstickerXplox.")
XXXXXXXXreturn
XXXXstickerset_attr_sX=Xrep_msg.document.attributes
XXXXstickerset_attrX=Xfind_instance(stickerset_attr_s,XDocumentAttributeSticker)
XXXXifXnotXstickerset_attr.stickerset:
XXXXXXXXawaitXgpic.reply("StickerXdoesXnotXbelongXtoXaXpack.")
XXXXXXXXreturn
XXXXtry:
XXXXXXXXidX=Xstickerset_attr.stickerset.id
XXXXXXXXaccess_hashX=Xstickerset_attr.stickerset.access_hash
XXXXXXXXprint(id)
XXXXXXXXprint(access_hash)
XXXXXXXXawaitXbot(
XXXXXXXXXXXXfunctions.channels.SetStickersRequest(
XXXXXXXXXXXXXXXXchannel=gpic.chat_id,
XXXXXXXXXXXXXXXXstickerset=types.InputStickerSetID(id=id,Xaccess_hash=access_hash),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXawaitXgpic.reply("GroupXstickerXpackXsuccessfullyXsetX!")
XXXXexceptXExceptionXasXe:
XXXXXXXXprint(e)
XXXXXXXXawaitXgpic.reply("FailedXtoXsetXgroupXstickerXpack.")


asyncXdefXextract_time(message,Xtime_val):
XXXXifXany(time_val.endswith(unit)XforXunitXinX("m",X"h",X"d")):
XXXXXXXXunitX=Xtime_val[-1]
XXXXXXXXtime_numX=Xtime_val[:-1]XX#Xtype:Xstr
XXXXXXXXifXnotXtime_num.isdigit():
XXXXXXXXXXXXawaitXmessage.reply("InvalidXtimeXamountXspecified.")
XXXXXXXXXXXXreturnX""

XXXXXXXXifXunitX==X"m":
XXXXXXXXXXXXbantimeX=Xint(time.time()X+Xint(time_num)X*X60)
XXXXXXXXelifXunitX==X"h":
XXXXXXXXXXXXbantimeX=Xint(time.time()X+Xint(time_num)X*X60X*X60)
XXXXXXXXelifXunitX==X"d":
XXXXXXXXXXXXbantimeX=Xint(time.time()X+Xint(time_num)X*X24X*X60X*X60)
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXXXXXreturnXbantime
XXXXelse:
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXX"InvalidXtimeXtypeXspecified.XExpectedXm,h,XorXd,Xgot:X{}".format(
XXXXXXXXXXXXXXXXtime_val[-1]
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturn
