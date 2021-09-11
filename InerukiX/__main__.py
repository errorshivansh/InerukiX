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
importos
fromimportlibimportimport_module

fromaiogramimportexecutor
fromaiogram.contrib.middlewares.loggingimportLoggingMiddleware

fromInerukiimportTOKEN,bot,dp
fromIneruki.configimportget_bool_key,get_list_key
fromIneruki.modulesimportALL_MODULES,LOADED_MODULES,MOD_HELP
fromIneruki.utils.loggerimportlog

ifget_bool_key("DEBUG_MODE"):
log.debug("Enablingloggingmiddleware.")
dp.middleware.setup(LoggingMiddleware())

LOAD=get_list_key("LOAD")
DONT_LOAD=get_list_key("DONT_LOAD")

ifget_bool_key("LOAD_MODULES"):
iflen(LOAD)>0:
modules=LOAD
else:
modules=ALL_MODULES

modules=[xforxinmodulesifxnotinDONT_LOAD]

log.info("Modulestoload:%s",str(modules))
formodule_nameinmodules:
#Loadpm_menuatlast
ifmodule_name=="pm_menu":
continue
log.debug(f"Importing<d><n>{module_name}</></>")
imported_module=import_module("Ineruki.modules."+module_name)
ifhasattr(imported_module,"__help__"):
ifhasattr(imported_module,"__mod_name__"):
MOD_HELP[imported_module.__mod_name__]=imported_module.__help__
else:
MOD_HELP[imported_module.__name__]=imported_module.__help__
LOADED_MODULES.append(imported_module)
log.info("Modulesloaded!")
else:
log.warning("Notimportingmodules!")

loop=asyncio.get_event_loop()

import_module("Ineruki.modules.pm_menu")
#Importmiscstuff
import_module("Ineruki.utils.exit_gracefully")
ifnotget_bool_key("DEBUG_MODE"):
import_module("Ineruki.utils.sentry")


asyncdefbefore_srv_task(loop):
formodulein[mforminLOADED_MODULESifhasattr(m,"__before_serving__")]:
log.debug("Beforeserving:"+module.__name__)
loop.create_task(module.__before_serving__(loop))


asyncdefstart(_):
log.debug("Startingbeforeservingtaskforallmodules...")
loop.create_task(before_srv_task(loop))

ifnotget_bool_key("DEBUG_MODE"):
log.debug("Waiting2seconds...")
awaitasyncio.sleep(2)


asyncdefstart_webhooks(_):
url=os.getenv("WEBHOOK_URL")+f"/{TOKEN}"
awaitbot.set_webhook(url)
returnawaitstart(_)


log.info("Startingloop..")
log.info("Aiogram:Usingpollingmethod")

ifos.getenv("WEBHOOKS",False):
port=os.getenv("WEBHOOKS_PORT",8080)
executor.start_webhook(dp,f"/{TOKEN}",on_startup=start_webhooks,port=port)
else:
executor.start_polling(
dp,
loop=loop,
on_startup=start,
timeout=15,
relax=0.1,
fast=True,
skip_updates=True,
)
