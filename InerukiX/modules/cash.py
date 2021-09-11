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

importrequests
fromtelethonimporttypes
fromtelethon.tlimportfunctions

fromIneruki.configimportget_str_key
fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbot

CASH_API_KEY=get_str_key("CASH_API_KEY",required=False)


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


@register(pattern="^/cash")
asyncdef_(event):
ifevent.fwd_from:
return
"""thismethodofapprovesystemismadeby@AyushChatterjee,godwillcurseyourfamilyifyoukangitmotherfucker"""
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
else:
return

cmd=event.text

args=cmd.split("")

iflen(args)==4:
try:
orig_cur_amount=float(args[1])

exceptValueError:
awaitevent.reply("InvalidAmountOfCurrency")
return

orig_cur=args[2].upper()

new_cur=args[3].upper()

request_url=(
f"https://www.alphavantage.co/query"
f"?function=CURRENCY_ECHANGE_RATE"
f"&from_currency={orig_cur}"
f"&to_currency={new_cur}"
f"&apikey={CASH_API_KEY}"
)
response=requests.get(request_url).json()
try:
current_rate=float(
response["RealtimeCurrencyExchangeRate"]["5.ExchangeRate"]
)
exceptKeyError:
awaitevent.reply("CurrencyNotSupported.")
return
new_cur_amount=round(orig_cur_amount*current_rate,5)
awaitevent.reply(f"{orig_cur_amount}{orig_cur}={new_cur_amount}{new_cur}")

eliflen(args)==1:
awaitevent.reply(__help__)

else:
awaitevent.reply(
f"**InvalidArgs!!:**Required3ButPassed{len(args)-1}",
)
