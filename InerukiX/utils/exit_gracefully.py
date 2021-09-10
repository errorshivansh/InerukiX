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

importXos
importXsignal

fromXInerukiX.services.redisXimportXredis
fromXInerukiX.utils.loggerXimportXlog


defXexit_gracefully(signum,Xframe):
XXXXlog.warning("Bye!")

XXXXtry:
XXXXXXXXredis.save()
XXXXexceptXException:
XXXXXXXXlog.error("ExitingXimmediately!")
XXXXos.kill(os.getpid(),Xsignal.SIGUSR1)


#XSignalXexit
log.info("SettingXexit_gracefullyXtask...")
signal.signal(signal.SIGINT,Xexit_gracefully)
