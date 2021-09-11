#ThisfileispartofInerukiBot(TelegramBot)

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

importsys

fromtelethonimportTelegramClient
fromtelethon.sessionsimportStringSession

fromIneruki.configimportget_int_key,get_str_key

STRING_SESSION=get_str_key("STRING_SESSION",required=True)
API_ID=get_int_key("APP_ID",required=True)
API_HASH=get_str_key("APP_HASH",required=True)

ubot=TelegramClient(StringSession(STRING_SESSION),API_ID,API_HASH)
try:
ubot.start()
exceptBaseException:
print("UserbotError!HaveyouaddedaSTRING_SESSIONindeploying??")
sys.exit(1)
