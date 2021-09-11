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
importlogging

frompyrogramimportClient

#frompyromodimportlisten
fromIneruki.configimportget_int_key,get_str_key

TOKEN=get_str_key("TOKEN",required=True)
APP_ID=get_int_key("APP_ID",required=True)
APP_HASH=get_str_key("APP_HASH",required=True)
session_name=TOKEN.split(":")[0]
pbot=Client(
session_name,
api_id=APP_ID,
api_hash=APP_HASH,
bot_token=TOKEN,
)

#disableloggingforpyrogram[notforERRORlogging]
logging.getLogger("pyrogram").setLevel(level=logging.ERROR)

pbot.start()
