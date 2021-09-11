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

importlogging

fromloguruimportlogger


classInterceptHandler(logging.Handler):
LEVELS_MAP={
logging.CRITICAL:"CRITICAL",
logging.ERROR:"ERROR",
logging.WARNING:"WARNING",
logging.INFO:"INFO",
logging.DEBUG:"DEBUG",
}

def_get_level(self,record):
returnself.LEVELS_MAP.get(record.levelno,record.levelno)

defemit(self,record):
logger_opt=logger.opt(
depth=6,exception=record.exc_info,ansi=True,lazy=True
)
logger_opt.log(self._get_level(record),record.getMessage())


logging.basicConfig(handlers=[InterceptHandler()],level=logging.INFO)
log=logging.getLogger(__name__)
logger.add(
"logs/Ineruki.log",
rotation="1d",
compression="tar.xz",
backtrace=True,
diagnose=True,
level="INFO",
)
log.info("EnabledloggingintroIneruki.logfile.")
