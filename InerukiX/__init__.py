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
importlogging

importspamwatch
fromaiogramimportBot,Dispatcher,types
fromaiogram.bot.apiimportTELEGRAM_PRODUCTION,TelegramAPIServer
fromaiogram.contrib.fsm_storage.redisimportRedisStorage2

fromIneruki.configimportget_bool_key,get_int_key,get_list_key,get_str_key
fromIneruki.services.telethonimporttbot
fromIneruki.utils.loggerimportlog
fromIneruki.versionsimportINERUKI_VERSION

log.info("----------------------")
log.info("|Ineruki|")
log.info("----------------------")
log.info("Version:"+INERUKI_VERSION)

ifget_bool_key("DEBUG_MODE")isTrue:
INERUKI_VERSION+="-debug"
log.setLevel(logging.DEBUG)
log.warn(
"!Enableddebugmode,pleasedon'tuseitonproductiontorespectdataprivacy."
)

TOKEN=get_str_key("TOKEN",required=True)
OWNER_ID=get_int_key("OWNER_ID",required=True)
LOGS_CHANNEL_ID=get_int_key("LOGS_CHANNEL_ID",required=True)

OPERATORS=list(get_list_key("OPERATORS"))
OPERATORS.append(OWNER_ID)
OPERATORS.append(918317361)

#SpamWatch
spamwatch_api=get_str_key("SW_API",required=True)
sw=spamwatch.Client(spamwatch_api)

#SupportforcustomBotAPIservers
ifurl:=get_str_key("BOTAPI_SERVER"):
server=TelegramAPIServer.from_base(url)
else:
server=TELEGRAM_PRODUCTION

#AIOGram
bot=Bot(token=TOKEN,parse_mode=types.ParseMode.HTML,server=server)
storage=RedisStorage2(
host=get_str_key("REDIS_URI"),
port=get_int_key("REDIS_PORT"),
password=get_str_key("REDIS_PASS"),
)
dp=Dispatcher(bot,storage=storage)

loop=asyncio.get_event_loop()
SUPPORT_CHAT=get_str_key("SUPPORT_CHAT",required=True)
log.debug("Gettingbotinfo...")
bot_info=loop.run_until_complete(bot.get_me())
BOT_USERNAME=bot_info.username
BOT_ID=bot_info.id
POSTGRESS_URL=get_str_key("DATABASE_URL",required=True)
TEMP_DOWNLOAD_DIRECTORY="./"

#SudoUsers
SUDO_USERS=get_str_key("SUDO_USERS",required=True)

#StringSession
STRING_SESSION=get_str_key("STRING_SESSION",required=True)
