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

importXio

fromXtelethonXimportXtypes
fromXtelethon.tlXimportXfunctions,Xtypes
fromXtelethon.tl.typesXimportX*

fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbotXasXborg


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):

XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXborg(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXifXisinstance(chat,Xtypes.InputPeerChat):

XXXXXXXXuiX=XawaitXborg.get_peer_id(user)
XXXXXXXXpsX=X(
XXXXXXXXXXXXawaitXborg(functions.messages.GetFullChatRequest(chat.chat_id))
XXXXXXXX).full_chat.participants.participants
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXXnext((pXforXpXinXpsXifXp.user_idX==Xui),XNone),
XXXXXXXXXXXX(types.ChatParticipantAdmin,Xtypes.ChatParticipantCreator),
XXXXXXXX)
XXXXreturnXNone


@register(pattern="^/json$")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelifXevent.chat_idX==XiidXandXevent.sender_idX==Xuserss:
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXthe_real_messageX=XNone
XXXXreply_to_idX=XNone
XXXXifXevent.reply_to_msg_id:
XXXXXXXXprevious_messageX=XawaitXevent.get_reply_message()
XXXXXXXXthe_real_messageX=Xprevious_message.stringify()
XXXXXXXXreply_to_idX=Xevent.reply_to_msg_id
XXXXelse:
XXXXXXXXthe_real_messageX=Xevent.stringify()
XXXXXXXXreply_to_idX=Xevent.message.id
XXXXifXlen(the_real_message)X>X4095:
XXXXXXXXwithXio.BytesIO(str.encode(the_real_message))XasXout_file:
XXXXXXXXXXXXout_file.nameX=X"json.text"
XXXXXXXXXXXXawaitXborg.send_file(
XXXXXXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXXXXXout_file,
XXXXXXXXXXXXXXXXforce_document=True,
XXXXXXXXXXXXXXXXallow_cache=False,
XXXXXXXXXXXXXXXXreply_to=reply_to_id,
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXevent.delete()
XXXXelse:
XXXXXXXXawaitXevent.reply("`{}`".format(the_real_message))
