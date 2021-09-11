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

fromapscheduler.executors.asyncioimportAsyncIOExecutor
fromapscheduler.jobstores.redisimportRedisJobStore
fromapscheduler.schedulers.asyncioimportAsyncIOScheduler
frompytzimportutc

fromIneruki.configimportget_str_key
fromIneruki.utils.loggerimportlog

DEFAULT="default"

jobstores={
DEFAULT:RedisJobStore(
host=get_str_key("REDIS_URI"),
port=get_str_key("REDIS_PORT"),
password=get_str_key("REDIS_PASS"),
)
}
executors={DEFAULT:AsyncIOExecutor()}
job_defaults={"coalesce":False,"max_instances":3}

scheduler=AsyncIOScheduler(
jobstores=jobstores,executors=executors,job_defaults=job_defaults,timezone=utc
)

log.info("Startingapscheduller...")
scheduler.start()
