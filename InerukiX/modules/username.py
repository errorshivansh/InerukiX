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

fromXtelethon.errors.rpcerrorlistXimportXYouBlockedUserError
fromXtelethon.tlXimportXfunctions,Xtypes

fromXInerukiX.services.eventsXimportXregisterXasXIneruki
fromXInerukiX.services.telethonXimportXtbot
fromXInerukiX.services.telethonuserbotXimportXubot


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


asyncXdefXsilently_send_message(conv,Xtext):
XXXXawaitXconv.send_message(text)
XXXXresponseX=XawaitXconv.get_response()
XXXXawaitXconv.mark_read(message=response)
XXXXreturnXresponse


@Ineruki(pattern="^/namehistoryX?(.*)")
asyncXdefX_(event):

XXXXifXevent.fwd_from:

XXXXXXXXreturn

XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXifXnotXevent.reply_to_msg_id:

XXXXXXXXawaitXevent.reply("```ReplyXtoXanyXuserXmessage.```")

XXXXXXXXreturn

XXXXreply_messageX=XawaitXevent.get_reply_message()

XXXXifXnotXreply_message.text:

XXXXXXXXawaitXevent.reply("```replyXtoXtextXmessage```")

XXXXXXXXreturn

XXXXchatX=X"@DetectiveInfoBot"
XXXXuidX=Xreply_message.sender_id
XXXXreply_message.sender

XXXXifXreply_message.sender.bot:

XXXXXXXXawaitXevent.edit("```ReplyXtoXactualXusersXmessage.```")

XXXXXXXXreturn

XXXXlolX=XawaitXevent.reply("```Processing```")

XXXXasyncXwithXubot.conversation(chat)XasXconv:

XXXXXXXXtry:

XXXXXXXXXXXX#XresponseX=Xconv.wait_event(
XXXXXXXXXXXX#XXXevents.NewMessage(incoming=True,Xfrom_users=1706537835)
XXXXXXXXXXXX#X)

XXXXXXXXXXXXawaitXsilently_send_message(conv,Xf"/detect_idX{uid}")

XXXXXXXXXXXX#XresponseX=XawaitXresponse
XXXXXXXXXXXXresponsesX=XawaitXsilently_send_message(conv,Xf"/detect_idX{uid}")
XXXXXXXXexceptXYouBlockedUserError:

XXXXXXXXXXXXawaitXevent.reply("```PleaseXunblockX@DetectiveInfoBotXandXtryXagain```")

XXXXXXXXXXXXreturn
XXXXXXXXawaitXlol.edit(f"{responses.text}")
XXXXXXXX#XawaitXlol.edit(f"{response.message.message}")
