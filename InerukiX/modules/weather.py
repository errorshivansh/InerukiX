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

importio
importtime

importaiohttp
fromtelethon.tlimportfunctions,types
fromtelethon.tl.typesimport*

fromIneruki.configimportget_str_key

OPENWEATHERMAP_ID=get_str_key("OPENWEATHERMAP_ID","")
fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbot


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):
returnisinstance(
(
awaittbot(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerChat):
ui=awaittbot.get_peer_id(user)
ps=(
awaittbot(functions.messages.GetFullChatRequest(chat.chat_id))
).full_chat.participants.participants
returnisinstance(
next((pforpinpsifp.user_id==ui),None),
(types.ChatParticipantAdmin,types.ChatParticipantCreator),
)
ifisinstance(chat,types.InputPeerUser):
returnTrue


@register(pattern="^/weather(.*)")
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
elifevent.chat_id==iidandevent.sender_id==userss:
pass
else:
return
sample_url=(
"https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
)
input_str=event.pattern_match.group(1)
asyncwithaiohttp.ClientSession()assession:
response_api_zero=awaitsession.get(
sample_url.format(input_str,OPENWEATHERMAP_ID)
)
response_api=awaitresponse_api_zero.json()
ifresponse_api["cod"]==200:
country_code=response_api["sys"]["country"]
country_time_zone=int(response_api["timezone"])
sun_rise_time=int(response_api["sys"]["sunrise"])+country_time_zone
sun_set_time=int(response_api["sys"]["sunset"])+country_time_zone
awaitevent.reply(
"""**Location**:{}
**Temperature☀️**:{}°С
__minimium__:{}°С
__maximum__:{}°С
**Humidity🌤**:{}%
**Wind**💨:{}m/s
**Clouds**☁️:{}hpa
**Sunrise**🌤:{}{}
**Sunset**🌝:{}{}""".format(
input_str,
response_api["main"]["temp"],
response_api["main"]["temp_min"],
response_api["main"]["temp_max"],
response_api["main"]["humidity"],
response_api["wind"]["speed"],
response_api["clouds"]["all"],
#response_api["main"]["pressure"],
time.strftime("%Y-%m-%d%H:%M:%S",time.gmtime(sun_rise_time)),
country_code,
time.strftime("%Y-%m-%d%H:%M:%S",time.gmtime(sun_set_time)),
country_code,
)
)
else:
awaitevent.reply(response_api["message"])


@register(pattern="^/weatherimg(.*)")
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
elifevent.chat_id==iidandevent.sender_id==userss:
pass
else:
return
sample_url="https://wttr.in/{}.png"
#logger.info(sample_url)
input_str=event.pattern_match.group(1)
asyncwithaiohttp.ClientSession()assession:
response_api_zero=awaitsession.get(sample_url.format(input_str))
#logger.info(response_api_zero)
response_api=awaitresponse_api_zero.read()
withio.BytesIO(response_api)asout_file:
awaitevent.reply(file=out_file)
