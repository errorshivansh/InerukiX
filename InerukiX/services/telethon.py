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


fromtelethonimportTelegramClient

fromIneruki.configimportget_int_key,get_str_key

TOKEN=get_str_key("TOKEN",required=True)
NAME=TOKEN.split(":")[0]

tbot=TelegramClient(
NAME,get_int_key("APP_ID",required=True),get_str_key("APP_HASH",required=True)
)

#Telethon
tbot.start(bot_token=TOKEN)
