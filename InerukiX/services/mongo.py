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

importasyncio
importsys

frommotorimportmotor_asyncio
fromodmanticimportAIOEngine
frompymongoimportMongoClient
frompymongo.errorsimportServerSelectionTimeoutError

fromInerukiimportlog
fromIneruki.configimportget_int_key,get_str_key

MONGO_URI=get_str_key("MONGO_URI")
MONGO_PORT=get_int_key("MONGO_PORT")
MONGO_DB=get_str_key("MONGO_DB")

#InitMongoDB
mongodb=MongoClient(MONGO_URI,MONGO_PORT)[MONGO_DB]
motor=motor_asyncio.AsyncIOMotorClient(MONGO_URI,MONGO_PORT)
db=motor[MONGO_DB]

engine=AIOEngine(motor,MONGO_DB)

try:
asyncio.get_event_loop().run_until_complete(motor.server_info())
exceptServerSelectionTimeoutError:
sys.exit(log.critical("Can'tconnecttomongodb!Exiting..."))
