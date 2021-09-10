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
importXos
fromXimportlibXimportXimport_module

fromXaiogramXimportXexecutor
fromXaiogram.contrib.middlewares.loggingXimportXLoggingMiddleware

fromXInerukiXXimportXTOKEN,Xbot,Xdp
fromXInerukiX.configXimportXget_bool_key,Xget_list_key
fromXInerukiX.modulesXimportXALL_MODULES,XLOADED_MODULES,XMOD_HELP
fromXInerukiX.utils.loggerXimportXlog

ifXget_bool_key("DEBUG_MODE"):
XXXXlog.debug("EnablingXloggingXmiddleware.")
XXXXdp.middleware.setup(LoggingMiddleware())

LOADX=Xget_list_key("LOAD")
DONT_LOADX=Xget_list_key("DONT_LOAD")

ifXget_bool_key("LOAD_MODULES"):
XXXXifXlen(LOAD)X>X0:
XXXXXXXXmodulesX=XLOAD
XXXXelse:
XXXXXXXXmodulesX=XALL_MODULES

XXXXmodulesX=X[xXforXxXinXmodulesXifXxXnotXinXDONT_LOAD]

XXXXlog.info("ModulesXtoXload:X%s",Xstr(modules))
XXXXforXmodule_nameXinXmodules:
XXXXXXXX#XLoadXpm_menuXatXlast
XXXXXXXXifXmodule_nameX==X"pm_menu":
XXXXXXXXXXXXcontinue
XXXXXXXXlog.debug(f"ImportingX<d><n>{module_name}</></>")
XXXXXXXXimported_moduleX=Ximport_module("InerukiX.modules."X+Xmodule_name)
XXXXXXXXifXhasattr(imported_module,X"__help__"):
XXXXXXXXXXXXifXhasattr(imported_module,X"__mod_name__"):
XXXXXXXXXXXXXXXXMOD_HELP[imported_module.__mod_name__]X=Ximported_module.__help__
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXMOD_HELP[imported_module.__name__]X=Ximported_module.__help__
XXXXXXXXLOADED_MODULES.append(imported_module)
XXXXlog.info("ModulesXloaded!")
else:
XXXXlog.warning("NotXimportingXmodules!")

loopX=Xasyncio.get_event_loop()

import_module("InerukiX.modules.pm_menu")
#XImportXmiscXstuff
import_module("InerukiX.utils.exit_gracefully")
ifXnotXget_bool_key("DEBUG_MODE"):
XXXXimport_module("InerukiX.utils.sentry")


asyncXdefXbefore_srv_task(loop):
XXXXforXmoduleXinX[mXforXmXinXLOADED_MODULESXifXhasattr(m,X"__before_serving__")]:
XXXXXXXXlog.debug("BeforeXserving:X"X+Xmodule.__name__)
XXXXXXXXloop.create_task(module.__before_serving__(loop))


asyncXdefXstart(_):
XXXXlog.debug("StartingXbeforeXservingXtaskXforXallXmodules...")
XXXXloop.create_task(before_srv_task(loop))

XXXXifXnotXget_bool_key("DEBUG_MODE"):
XXXXXXXXlog.debug("WaitingX2Xseconds...")
XXXXXXXXawaitXasyncio.sleep(2)


asyncXdefXstart_webhooks(_):
XXXXurlX=Xos.getenv("WEBHOOK_URL")X+Xf"/{TOKEN}"
XXXXawaitXbot.set_webhook(url)
XXXXreturnXawaitXstart(_)


log.info("StartingXloop..")
log.info("Aiogram:XUsingXpollingXmethod")

ifXos.getenv("WEBHOOKS",XFalse):
XXXXportX=Xos.getenv("WEBHOOKS_PORT",X8080)
XXXXexecutor.start_webhook(dp,Xf"/{TOKEN}",Xon_startup=start_webhooks,Xport=port)
else:
XXXXexecutor.start_polling(
XXXXXXXXdp,
XXXXXXXXloop=loop,
XXXXXXXXon_startup=start,
XXXXXXXXtimeout=15,
XXXXXXXXrelax=0.1,
XXXXXXXXfast=True,
XXXXXXXXskip_updates=True,
XXXX)
