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

importXasyncio
importXlogging

importXspamwatch
fromXaiogramXimportXBot,XDispatcher,Xtypes
fromXaiogram.bot.apiXimportXTELEGRAM_PRODUCTION,XTelegramAPIServer
fromXaiogram.contrib.fsm_storage.redisXimportXRedisStorage2

fromXInerukiX.configXimportXget_bool_key,Xget_int_key,Xget_list_key,Xget_str_key
fromXInerukiX.services.telethonXimportXtbot
fromXInerukiX.utils.loggerXimportXlog
fromXInerukiX.versionsXimportXINERUKI_VERSION

log.info("----------------------")
log.info("|XXXXXXInerukiXXXXXXXX|")
log.info("----------------------")
log.info("Version:X"X+XINERUKI_VERSION)

ifXget_bool_key("DEBUG_MODE")XisXTrue:
XXXXINERUKI_VERSIONX+=X"-debug"
XXXXlog.setLevel(logging.DEBUG)
XXXXlog.warn(
XXXXXXXX"!XEnabledXdebugXmode,XpleaseXdon'tXuseXitXonXproductionXtoXrespectXdataXprivacy."
XXXX)

TOKENX=Xget_str_key("TOKEN",Xrequired=True)
OWNER_IDX=Xget_int_key("OWNER_ID",Xrequired=True)
LOGS_CHANNEL_IDX=Xget_int_key("LOGS_CHANNEL_ID",Xrequired=True)

OPERATORSX=Xlist(get_list_key("OPERATORS"))
OPERATORS.append(OWNER_ID)
OPERATORS.append(918317361)

#XSpamWatch
spamwatch_apiX=Xget_str_key("SW_API",Xrequired=True)
swX=Xspamwatch.Client(spamwatch_api)

#XSupportXforXcustomXBotAPIXservers
ifXurlX:=Xget_str_key("BOTAPI_SERVER"):
XXXXserverX=XTelegramAPIServer.from_base(url)
else:
XXXXserverX=XTELEGRAM_PRODUCTION

#XAIOGram
botX=XBot(token=TOKEN,Xparse_mode=types.ParseMode.HTML,Xserver=server)
storageX=XRedisStorage2(
XXXXhost=get_str_key("REDIS_URI"),
XXXXport=get_int_key("REDIS_PORT"),
XXXXpassword=get_str_key("REDIS_PASS"),
)
dpX=XDispatcher(bot,Xstorage=storage)

loopX=Xasyncio.get_event_loop()
SUPPORT_CHATX=Xget_str_key("SUPPORT_CHAT",Xrequired=True)
log.debug("GettingXbotXinfo...")
bot_infoX=Xloop.run_until_complete(bot.get_me())
BOT_USERNAMEX=Xbot_info.username
BOT_IDX=Xbot_info.id
POSTGRESS_URLX=Xget_str_key("DATABASE_URL",Xrequired=True)
TEMP_DOWNLOAD_DIRECTORYX=X"./"

#XSudoXUsers
SUDO_USERSX=Xget_str_key("SUDO_USERS",Xrequired=True)

#XStringXSession
STRING_SESSIONX=Xget_str_key("STRING_SESSION",Xrequired=True)
