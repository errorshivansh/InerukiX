#Copyright(C)2021errorshivansh

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


fromgeopy.geocodersimportNominatim
fromtelethonimport*
fromtelethon.tlimport*

fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbotasclient


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):

returnisinstance(
(
awaitclient(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerChat):

ui=awaitclient.get_peer_id(user)
ps=(
awaitclient(functions.messages.GetFullChatRequest(chat.chat_id))
).full_chat.participants.participants
returnisinstance(
next((pforpinpsifp.user_id==ui),None),
(types.ChatParticipantAdmin,types.ChatParticipantCreator),
)
returnNone


GMAPS_LOC="https://maps.googleapis.com/maps/api/geocode/json"


@register(pattern="^/gps(.*)")
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.is_group:
ifnot(awaitis_register_admin(event.input_chat,event.message.sender_id)):
awaitevent.reply(
"YouarenotAdmin.So,Youcan'tusethis.Tryinmyinbox"
)
return

args=event.pattern_match.group(1)

try:
geolocator=Nominatim(user_agent="SkittBot")
location=args
geoloc=geolocator.geocode(location)
longitude=geoloc.longitude
latitude=geoloc.latitude
gm="https://www.google.com/maps/search/{},{}".format(latitude,longitude)
awaitclient.send_file(
event.chat_id,
file=types.InputMediaGeoPoint(
types.InputGeoPoint(float(latitude),float(longitude))
),
)
awaitevent.reply(
"Openwith:[GoogleMaps]({})".format(gm),
link_preview=False,
)
exceptExceptionase:
print(e)
awaitevent.reply("Ican'tfindthat")
