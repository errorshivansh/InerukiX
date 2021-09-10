#XThisXfileXisXpartXofXUtahX(TelegramXBot)

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

importXsys

importXredisXasXredis_lib

fromXInerukiXXimportXlog
fromXInerukiX.configXimportXget_str_key

#XInitXRedis
redisX=Xredis_lib.Redis(
XXXXhost=get_str_key("REDIS_URI"),
XXXXport=get_str_key("REDIS_PORT"),
XXXXpassword=get_str_key("REDIS_PASS"),
XXXXdecode_responses=True,
)

bredisX=Xredis_lib.Redis(
XXXXhost=get_str_key("REDIS_URI"),
XXXXport=get_str_key("REDIS_PORT"),
XXXXpassword=get_str_key("REDIS_PASS"),
)

try:
XXXXredis.ping()
exceptXredis_lib.ConnectionError:
XXXXsys.exit(log.critical("Can'tXconnectXtoXRedisDB!XExiting..."))
