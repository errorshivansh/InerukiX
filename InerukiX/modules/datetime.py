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

importXdatetime
fromXtypingXimportXList

importXrequests
fromXtelethonXimportXtypes
fromXtelethon.tlXimportXfunctions

fromXInerukiX.configXimportXget_str_key
fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbot

TIME_API_KEYX=Xget_str_key("TIME_API_KEY",Xrequired=False)


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXtbot(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXifXisinstance(chat,Xtypes.InputPeerUser):
XXXXXXXXreturnXTrue


defXgenerate_time(to_find:Xstr,Xfindtype:XList[str])X->Xstr:
XXXXdataX=Xrequests.get(
XXXXXXXXf"http://api.timezonedb.com/v2.1/list-time-zone"
XXXXXXXXf"?key={TIME_API_KEY}"
XXXXXXXXf"&format=json"
XXXXXXXXf"&fields=countryCode,countryName,zoneName,gmtOffset,timestamp,dst"
XXXX).json()

XXXXforXzoneXinXdata["zones"]:
XXXXXXXXforXeachtypeXinXfindtype:
XXXXXXXXXXXXifXto_findXinXzone[eachtype].lower():
XXXXXXXXXXXXXXXXcountry_nameX=Xzone["countryName"]
XXXXXXXXXXXXXXXXcountry_zoneX=Xzone["zoneName"]
XXXXXXXXXXXXXXXXcountry_codeX=Xzone["countryCode"]

XXXXXXXXXXXXXXXXifXzone["dst"]X==X1:
XXXXXXXXXXXXXXXXXXXXdaylight_savingX=X"Yes"
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXdaylight_savingX=X"No"

XXXXXXXXXXXXXXXXdate_fmtX=Xr"%d-%m-%Y"
XXXXXXXXXXXXXXXXtime_fmtX=Xr"%H:%M:%S"
XXXXXXXXXXXXXXXXday_fmtX=Xr"%A"
XXXXXXXXXXXXXXXXgmt_offsetX=Xzone["gmtOffset"]
XXXXXXXXXXXXXXXXtimestampX=Xdatetime.datetime.now(
XXXXXXXXXXXXXXXXXXXXdatetime.timezone.utc
XXXXXXXXXXXXXXXX)X+Xdatetime.timedelta(seconds=gmt_offset)
XXXXXXXXXXXXXXXXcurrent_dateX=Xtimestamp.strftime(date_fmt)
XXXXXXXXXXXXXXXXcurrent_timeX=Xtimestamp.strftime(time_fmt)
XXXXXXXXXXXXXXXXcurrent_dayX=Xtimestamp.strftime(day_fmt)

XXXXXXXXXXXXXXXXbreak

XXXXtry:
XXXXXXXXresultX=X(
XXXXXXXXXXXXf"<b>🌍CountryX:</b>X<code>{country_name}</code>\n"
XXXXXXXXXXXXf"<b>⏳ZoneXNameX:</b>X<code>{country_zone}</code>\n"
XXXXXXXXXXXXf"<b>🗺CountryXCodeX:</b>X<code>{country_code}</code>\n"
XXXXXXXXXXXXf"<b>🌞DaylightXsavingX:</b>X<code>{daylight_saving}</code>\n"
XXXXXXXXXXXXf"<b>🌅DayX:</b>X<code>{current_day}</code>\n"
XXXXXXXXXXXXf"<b>⌚CurrentXTimeX:</b>X<code>{current_time}</code>\n"
XXXXXXXXXXXXf"<b>📆CurrentXDateX:</b>X<code>{current_date}</code>"
XXXXXXXX)
XXXXexceptXBaseException:
XXXXXXXXresultX=XNone

XXXXreturnXresult


@register(pattern="^/datetimeX?(.*)")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn

XXXXgayX=Xevent.pattern_match.group(1)

XXXXtry:
XXXXXXXXqueryX=Xgay
XXXXexceptXBaseException:
XXXXXXXXawaitXevent.reply("ProvideXaXcountryXname/abbreviation/timezoneXtoXfind.")
XXXXXXXXreturn

XXXXsend_messageX=XawaitXevent.reply(
XXXXXXXXf"FindingXtimezoneXinfoXforX<b>{query}</b>",Xparse_mode="html"
XXXX)

XXXXquery_timezoneX=Xquery.lower()
XXXXifXlen(query_timezone)X==X2:
XXXXXXXXresultX=Xgenerate_time(query_timezone,X["countryCode"])
XXXXelse:
XXXXXXXXresultX=Xgenerate_time(query_timezone,X["zoneName",X"countryName"])

XXXXifXnotXresult:
XXXXXXXXawaitXsend_message.edit(
XXXXXXXXXXXXf"TimezoneXinfoXnotXavailableXforX<b>{query}</b>",Xparse_mode="html"
XXXXXXXX)
XXXXXXXXreturn

XXXXawaitXsend_message.edit(result,Xparse_mode="html")


_mod_name_X=X"DateXTime"
_help_X=X"""
X-X/datetimeX[timezone]:XGetXtheXpresentXdateXandXtimeXinformation
**YouXcanXcheckXoutXthisX[link](https://timezonedb.com/time-zones)XforXtheXavailableXtimezones**
"""
