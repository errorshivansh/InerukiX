#ThisfileispartofUtah(TelegramBot)

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

importredisasredis_lib

fromInerukiimportlog
fromIneruki.configimportget_str_key

#InitRedis
redis=redis_lib.Redis(
host=get_str_key("REDIS_URI"),
port=get_str_key("REDIS_PORT"),
password=get_str_key("REDIS_PASS"),
decode_responses=True,
)

bredis=redis_lib.Redis(
host=get_str_key("REDIS_URI"),
port=get_str_key("REDIS_PORT"),
password=get_str_key("REDIS_PASS"),
)

try:
redis.ping()
exceptredis_lib.ConnectionError:
sys.exit(log.critical("Can'tconnecttoRedisDB!Exiting..."))
