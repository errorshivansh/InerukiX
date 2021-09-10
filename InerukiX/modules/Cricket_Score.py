#XXXXCopyrightX(C)X@chsaiujwalX2020-2021
#XXXXEditedXbyXerrorshivansh
#XXXXThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XXXXitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXasXpublishedXby
#XXXXtheXFreeXSoftwareXFoundation,XeitherXversionX3XofXtheXLicense,Xor
#
#XXXXThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XXXXbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XXXXMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XXXXGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.
#
#XXXXYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XXXXalongXwithXthisXprogram.XXIfXnot,XseeX<https://www.gnu.org/licenses/>.


importXurllib.request

fromXbs4XimportXBeautifulSoup
fromXtelethonXimportXevents
fromXtelethon.tlXimportXfunctions,Xtypes

fromXInerukiX.services.telethonXimportXtbot


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


@tbot.on(events.NewMessage(pattern="/cs$"))
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXscore_pageX=X"http://static.cricinfo.com/rss/livescores.xml"
XXXXpageX=Xurllib.request.urlopen(score_page)
XXXXsoupX=XBeautifulSoup(page,X"html.parser")
XXXXresultX=Xsoup.find_all("description")
XXXXSedX=X""
XXXXforXmatchXinXresult:
XXXXXXXXSedX+=Xmatch.get_text()X+X"\n\n"
XXXXawaitXevent.reply(
XXXXXXXXf"<b><u>MatchXinformationXgatheredXsuccessful</b></u>\n\n\n<code>{Sed}</code>",
XXXXXXXXparse_mode="HTML",
XXXX)
