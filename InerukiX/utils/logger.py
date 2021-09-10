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

importXlogging

fromXloguruXimportXlogger


classXInterceptHandler(logging.Handler):
XXXXLEVELS_MAPX=X{
XXXXXXXXlogging.CRITICAL:X"CRITICAL",
XXXXXXXXlogging.ERROR:X"ERROR",
XXXXXXXXlogging.WARNING:X"WARNING",
XXXXXXXXlogging.INFO:X"INFO",
XXXXXXXXlogging.DEBUG:X"DEBUG",
XXXX}

XXXXdefX_get_level(self,Xrecord):
XXXXXXXXreturnXself.LEVELS_MAP.get(record.levelno,Xrecord.levelno)

XXXXdefXemit(self,Xrecord):
XXXXXXXXlogger_optX=Xlogger.opt(
XXXXXXXXXXXXdepth=6,Xexception=record.exc_info,Xansi=True,Xlazy=True
XXXXXXXX)
XXXXXXXXlogger_opt.log(self._get_level(record),Xrecord.getMessage())


logging.basicConfig(handlers=[InterceptHandler()],Xlevel=logging.INFO)
logX=Xlogging.getLogger(__name__)
logger.add(
XXXX"logs/Ineruki.log",
XXXXrotation="1Xd",
XXXXcompression="tar.xz",
XXXXbacktrace=True,
XXXXdiagnose=True,
XXXXlevel="INFO",
)
log.info("EnabledXloggingXintroXIneruki.logXfile.")
