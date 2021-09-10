#XCopyrightX(C)X2021Xerrorshivansh


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

fromXasyncioXimportXsleep

fromXtelethonXimportXevents
fromXtelethon.errorsXimportXChatAdminRequiredError,XUserAdminInvalidError
fromXtelethon.tl.functions.channelsXimportXEditBannedRequest
fromXtelethon.tl.typesXimportXChatBannedRights

fromXInerukiXXimportXOWNER_ID
fromXInerukiX.services.telethonXimportXtbotXasXclient

#X===================XCONSTANTX===================

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

OFFICERSX=XOWNER_ID

#XCheckXifXuserXhasXadminXrights
asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):

XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXtbot(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXifXisinstance(chat,Xtypes.InputPeerChat):

XXXXXXXXuiX=XawaitXtbot.get_peer_id(user)
XXXXXXXXpsX=X(
XXXXXXXXXXXXawaitXtbot(functions.messages.GetFullChatRequest(chat.chat_id))
XXXXXXXX).full_chat.participants.participants
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXXnext((pXforXpXinXpsXifXp.user_idX==Xui),XNone),
XXXXXXXXXXXX(types.ChatParticipantAdmin,Xtypes.ChatParticipantCreator),
XXXXXXXX)
XXXXreturnXNone


@client.on(events.NewMessage(pattern=f"^[!/]zombiesX?(.*)"))
asyncXdefXzombies(event):
XXXX"""ForX.zombiesXcommand,XlistXallXtheXzombiesXinXaXchat."""
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXconX=Xevent.pattern_match.group(1).lower()
XXXXdel_uX=X0
XXXXdel_statusX=X"NoXDeletedXAccountsXFound,XGroupXIsXClean."

XXXXifXconX!=X"clean":
XXXXXXXXfind_zombiesX=XawaitXevent.respond("SearchingXForXZombies...")
XXXXXXXXasyncXforXuserXinXevent.client.iter_participants(event.chat_id):

XXXXXXXXXXXXifXuser.deleted:
XXXXXXXXXXXXXXXXdel_uX+=X1
XXXXXXXXXXXXXXXXawaitXsleep(1)
XXXXXXXXifXdel_uX>X0:
XXXXXXXXXXXXdel_statusX=Xf"FoundX**{del_u}**XZombiesXInXThisXGroup.\
XXXXXXXXXXXX\nCleanXThemXByXUsingX-X`/zombiesXclean`"
XXXXXXXXawaitXfind_zombies.edit(del_status)
XXXXXXXXreturn

XXXX#XHereXlayingXtheXsanityXcheck
XXXXchatX=XawaitXevent.get_chat()
XXXXchat.admin_rights
XXXXchat.creator

XXXX#XWell

XXXXcleaning_zombiesX=XawaitXevent.respond("CleaningXZombies...")
XXXXdel_uX=X0
XXXXdel_aX=X0

XXXXasyncXforXuserXinXevent.client.iter_participants(event.chat_id):
XXXXXXXXifXuser.deleted:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXevent.client(
XXXXXXXXXXXXXXXXXXXXEditBannedRequest(event.chat_id,Xuser.id,XBANNED_RIGHTS)
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXChatAdminRequiredError:
XXXXXXXXXXXXXXXXawaitXcleaning_zombies.edit("IXDon'tXHaveXBanXRightsXInXThisXGroup.")
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXexceptXUserAdminInvalidError:
XXXXXXXXXXXXXXXXdel_uX-=X1
XXXXXXXXXXXXXXXXdel_aX+=X1
XXXXXXXXXXXXawaitXevent.client(EditBannedRequest(event.chat_id,Xuser.id,XUNBAN_RIGHTS))
XXXXXXXXXXXXdel_uX+=X1

XXXXifXdel_uX>X0:
XXXXXXXXdel_statusX=Xf"CleanedX`{del_u}`XZombies"

XXXXifXdel_aX>X0:
XXXXXXXXdel_statusX=Xf"CleanedX`{del_u}`XZombiesX\
XXXXXXXX\n`{del_a}`XZombieXAdminXAccountsXAreXNotXRemoved!"

XXXXawaitXcleaning_zombies.edit(del_status)
