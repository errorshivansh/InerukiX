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

importdatetime
fromtypingimportList

importrequests
fromtelethonimporttypes
fromtelethon.tlimportfunctions

fromIneruki.configimportget_str_key
fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbot

TIME_API_KEY=get_str_key("TIME_API_KEY",required=False)


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):
returnisinstance(
(
awaittbot(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerUser):
returnTrue


defgenerate_time(to_find:str,findtype:List[str])->str:
data=requests.get(
f"http://api.timezonedb.com/v2.1/list-time-zone"
f"?key={TIME_API_KEY}"
f"&format=json"
f"&fields=countryCode,countryName,zoneName,gmtOffset,timestamp,dst"
).json()

forzoneindata["zones"]:
foreachtypeinfindtype:
ifto_findinzone[eachtype].lower():
country_name=zone["countryName"]
country_zone=zone["zoneName"]
country_code=zone["countryCode"]

ifzone["dst"]==1:
daylight_saving="Yes"
else:
daylight_saving="No"

date_fmt=r"%d-%m-%Y"
time_fmt=r"%H:%M:%S"
day_fmt=r"%A"
gmt_offset=zone["gmtOffset"]
timestamp=datetime.datetime.now(
datetime.timezone.utc
)+datetime.timedelta(seconds=gmt_offset)
current_date=timestamp.strftime(date_fmt)
current_time=timestamp.strftime(time_fmt)
current_day=timestamp.strftime(day_fmt)

break

try:
result=(
f"<b>🌍Country:</b><code>{country_name}</code>\n"
f"<b>⏳ZoneName:</b><code>{country_zone}</code>\n"
f"<b>🗺CountryCode:</b><code>{country_code}</code>\n"
f"<b>🌞Daylightsaving:</b><code>{daylight_saving}</code>\n"
f"<b>🌅Day:</b><code>{current_day}</code>\n"
f"<b>⌚CurrentTime:</b><code>{current_time}</code>\n"
f"<b>📆CurrentDate:</b><code>{current_date}</code>"
)
exceptBaseException:
result=None

returnresult


@register(pattern="^/datetime?(.*)")
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
else:
return

gay=event.pattern_match.group(1)

try:
query=gay
exceptBaseException:
awaitevent.reply("Provideacountryname/abbreviation/timezonetofind.")
return

send_message=awaitevent.reply(
f"Findingtimezoneinfofor<b>{query}</b>",parse_mode="html"
)

query_timezone=query.lower()
iflen(query_timezone)==2:
result=generate_time(query_timezone,["countryCode"])
else:
result=generate_time(query_timezone,["zoneName","countryName"])

ifnotresult:
awaitsend_message.edit(
f"Timezoneinfonotavailablefor<b>{query}</b>",parse_mode="html"
)
return

awaitsend_message.edit(result,parse_mode="html")


_mod_name_="DateTime"
_help_="""
-/datetime[timezone]:Getthepresentdateandtimeinformation
**Youcancheckoutthis[link](https://timezonedb.com/time-zones)fortheavailabletimezones**
"""
