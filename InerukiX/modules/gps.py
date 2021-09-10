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


fromXgeopy.geocodersXimportXNominatim
fromXtelethonXimportX*
fromXtelethon.tlXimportX*

fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbotXasXclient


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):

XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXclient(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXifXisinstance(chat,Xtypes.InputPeerChat):

XXXXXXXXuiX=XawaitXclient.get_peer_id(user)
XXXXXXXXpsX=X(
XXXXXXXXXXXXawaitXclient(functions.messages.GetFullChatRequest(chat.chat_id))
XXXXXXXX).full_chat.participants.participants
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXXnext((pXforXpXinXpsXifXp.user_idX==Xui),XNone),
XXXXXXXXXXXX(types.ChatParticipantAdmin,Xtypes.ChatParticipantCreator),
XXXXXXXX)
XXXXreturnXNone


GMAPS_LOCX=X"https://maps.googleapis.com/maps/api/geocode/json"


@register(pattern="^/gpsX(.*)")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXnotX(awaitXis_register_admin(event.input_chat,Xevent.message.sender_id)):
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"YouXareXnotXAdmin.XSo,XYouXcan'tXuseXthis.XTryXinXmyXinbox"
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn

XXXXargsX=Xevent.pattern_match.group(1)

XXXXtry:
XXXXXXXXgeolocatorX=XNominatim(user_agent="SkittBot")
XXXXXXXXlocationX=Xargs
XXXXXXXXgeolocX=Xgeolocator.geocode(location)
XXXXXXXXlongitudeX=Xgeoloc.longitude
XXXXXXXXlatitudeX=Xgeoloc.latitude
XXXXXXXXgmX=X"https://www.google.com/maps/search/{},{}".format(latitude,Xlongitude)
XXXXXXXXawaitXclient.send_file(
XXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXfile=types.InputMediaGeoPoint(
XXXXXXXXXXXXXXXXtypes.InputGeoPoint(float(latitude),Xfloat(longitude))
XXXXXXXXXXXX),
XXXXXXXX)
XXXXXXXXawaitXevent.reply(
XXXXXXXXXXXX"OpenXwith:X[GoogleXMaps]({})".format(gm),
XXXXXXXXXXXXlink_preview=False,
XXXXXXXX)
XXXXexceptXExceptionXasXe:
XXXXXXXXprint(e)
XXXXXXXXawaitXevent.reply("IXcan'tXfindXthat")
