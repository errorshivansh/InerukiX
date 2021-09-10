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

importXrequests
fromXtelethonXimportXtypes
fromXtelethon.tlXimportXfunctions

fromXInerukiX.configXimportXget_str_key
fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbot

CASH_API_KEYX=Xget_str_key("CASH_API_KEY",Xrequired=False)


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


@register(pattern="^/cash")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXX"""thisXmethodXofXapproveXsystemXisXmadeXbyX@AyushChatterjee,XgodXwillXcurseXyourXfamilyXifXyouXkangXitXmotherfucker"""
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn

XXXXcmdX=Xevent.text

XXXXargsX=Xcmd.split("X")

XXXXifXlen(args)X==X4:
XXXXXXXXtry:
XXXXXXXXXXXXorig_cur_amountX=Xfloat(args[1])

XXXXXXXXexceptXValueError:
XXXXXXXXXXXXawaitXevent.reply("InvalidXAmountXOfXCurrency")
XXXXXXXXXXXXreturn

XXXXXXXXorig_curX=Xargs[2].upper()

XXXXXXXXnew_curX=Xargs[3].upper()

XXXXXXXXrequest_urlX=X(
XXXXXXXXXXXXf"https://www.alphavantage.co/query"
XXXXXXXXXXXXf"?function=CURRENCY_EXCHANGE_RATE"
XXXXXXXXXXXXf"&from_currency={orig_cur}"
XXXXXXXXXXXXf"&to_currency={new_cur}"
XXXXXXXXXXXXf"&apikey={CASH_API_KEY}"
XXXXXXXX)
XXXXXXXXresponseX=Xrequests.get(request_url).json()
XXXXXXXXtry:
XXXXXXXXXXXXcurrent_rateX=Xfloat(
XXXXXXXXXXXXXXXXresponse["RealtimeXCurrencyXExchangeXRate"]["5.XExchangeXRate"]
XXXXXXXXXXXX)
XXXXXXXXexceptXKeyError:
XXXXXXXXXXXXawaitXevent.reply("CurrencyXNotXSupported.")
XXXXXXXXXXXXreturn
XXXXXXXXnew_cur_amountX=Xround(orig_cur_amountX*Xcurrent_rate,X5)
XXXXXXXXawaitXevent.reply(f"{orig_cur_amount}X{orig_cur}X=X{new_cur_amount}X{new_cur}")

XXXXelifXlen(args)X==X1:
XXXXXXXXawaitXevent.reply(__help__)

XXXXelse:
XXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXf"**InvalidXArgs!!:**XRequiredX3XButXPassedX{len(args)X-1}",
XXXXXXXX)
