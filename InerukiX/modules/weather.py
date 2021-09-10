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
importXtime

importXaiohttp
fromXtelethon.tlXimportXfunctions,Xtypes
fromXtelethon.tl.typesXimportX*

fromXInerukiX.configXimportXget_str_key

OPENWEATHERMAP_IDX=Xget_str_key("OPENWEATHERMAP_ID",X"")
fromXInerukiX.services.eventsXimportXregister
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
XXXXifXisinstance(chat,Xtypes.InputPeerUser):
XXXXXXXXreturnXTrue


@register(pattern="^/weatherX(.*)")
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
XXXXsample_urlX=X(
XXXXXXXX"https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
XXXX)
XXXXinput_strX=Xevent.pattern_match.group(1)
XXXXasyncXwithXaiohttp.ClientSession()XasXsession:
XXXXXXXXresponse_api_zeroX=XawaitXsession.get(
XXXXXXXXXXXXsample_url.format(input_str,XOPENWEATHERMAP_ID)
XXXXXXXX)
XXXXresponse_apiX=XawaitXresponse_api_zero.json()
XXXXifXresponse_api["cod"]X==X200:
XXXXXXXXcountry_codeX=Xresponse_api["sys"]["country"]
XXXXXXXXcountry_time_zoneX=Xint(response_api["timezone"])
XXXXXXXXsun_rise_timeX=Xint(response_api["sys"]["sunrise"])X+Xcountry_time_zone
XXXXXXXXsun_set_timeX=Xint(response_api["sys"]["sunset"])X+Xcountry_time_zone
XXXXXXXXawaitXevent.reply(
XXXXXXXXXXXX"""**Location**:X{}
**TemperatureX☀️**:X{}°С
XXXX__minimium__:X{}°С
XXXX__maximum__X:X{}°С
**HumidityX🌤**:X{}%
**Wind**X💨:X{}m/s
**Clouds**X☁️:X{}hpa
**Sunrise**X🌤:X{}X{}
**Sunset**X🌝:X{}X{}""".format(
XXXXXXXXXXXXXXXXinput_str,
XXXXXXXXXXXXXXXXresponse_api["main"]["temp"],
XXXXXXXXXXXXXXXXresponse_api["main"]["temp_min"],
XXXXXXXXXXXXXXXXresponse_api["main"]["temp_max"],
XXXXXXXXXXXXXXXXresponse_api["main"]["humidity"],
XXXXXXXXXXXXXXXXresponse_api["wind"]["speed"],
XXXXXXXXXXXXXXXXresponse_api["clouds"]["all"],
XXXXXXXXXXXXXXXX#Xresponse_api["main"]["pressure"],
XXXXXXXXXXXXXXXXtime.strftime("%Y-%m-%dX%H:%M:%S",Xtime.gmtime(sun_rise_time)),
XXXXXXXXXXXXXXXXcountry_code,
XXXXXXXXXXXXXXXXtime.strftime("%Y-%m-%dX%H:%M:%S",Xtime.gmtime(sun_set_time)),
XXXXXXXXXXXXXXXXcountry_code,
XXXXXXXXXXXX)
XXXXXXXX)
XXXXelse:
XXXXXXXXawaitXevent.reply(response_api["message"])


@register(pattern="^/weatherimgX(.*)")
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
XXXXsample_urlX=X"https://wttr.in/{}.png"
XXXX#Xlogger.info(sample_url)
XXXXinput_strX=Xevent.pattern_match.group(1)
XXXXasyncXwithXaiohttp.ClientSession()XasXsession:
XXXXXXXXresponse_api_zeroX=XawaitXsession.get(sample_url.format(input_str))
XXXXXXXX#Xlogger.info(response_api_zero)
XXXXXXXXresponse_apiX=XawaitXresponse_api_zero.read()
XXXXXXXXwithXio.BytesIO(response_api)XasXout_file:
XXXXXXXXXXXXawaitXevent.reply(file=out_file)
