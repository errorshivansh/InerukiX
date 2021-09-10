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

fromXapscheduler.executors.asyncioXimportXAsyncIOExecutor
fromXapscheduler.jobstores.redisXimportXRedisJobStore
fromXapscheduler.schedulers.asyncioXimportXAsyncIOScheduler
fromXpytzXimportXutc

fromXInerukiX.configXimportXget_str_key
fromXInerukiX.utils.loggerXimportXlog

DEFAULTX=X"default"

jobstoresX=X{
XXXXDEFAULT:XRedisJobStore(
XXXXXXXXhost=get_str_key("REDIS_URI"),
XXXXXXXXport=get_str_key("REDIS_PORT"),
XXXXXXXXpassword=get_str_key("REDIS_PASS"),
XXXX)
}
executorsX=X{DEFAULT:XAsyncIOExecutor()}
job_defaultsX=X{"coalesce":XFalse,X"max_instances":X3}

schedulerX=XAsyncIOScheduler(
XXXXjobstores=jobstores,Xexecutors=executors,Xjob_defaults=job_defaults,Xtimezone=utc
)

log.info("StartingXapscheduller...")
scheduler.start()
