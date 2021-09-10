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
importXsys

importXyaml
fromXenvparseXimportXenv

fromXInerukiX.utils.loggerXimportXlog

DEFAULTSX=X{
XXXX"LOAD_MODULES":XTrue,
XXXX"DEBUG_MODE":XTrue,
XXXX"REDIS_HOST":X"localhost",
XXXX"REDIS_PORT":X6379,
XXXX"REDIS_DB_FSM":X1,
XXXX"MONGODB_URI":X"localhost",
XXXX"MONGO_DB":X"InerukiX",
XXXX"API_PORT":X8080,
XXXX"JOIN_CONFIRM_DURATION":X"30m",
}

CONFIG_PATHX=X"data/bot_conf.yaml"
ifXos.nameX==X"nt":
XXXXlog.debug("DetectedXWindows,XchangingXconfigXpath...")
XXXXCONFIG_PATHX=Xos.getcwd()X+X"\\data\\bot_conf.yaml"

ifXos.path.isfile(CONFIG_PATH):
XXXXlog.info(CONFIG_PATH)
XXXXforXitemXinX(
XXXXXXXXdataX:=Xyaml.load(open("data/bot_conf.yaml",X"r"),XLoader=yaml.CLoader)
XXXX):
XXXXXXXXDEFAULTS[item.upper()]X=Xdata[item]
else:
XXXXlog.info("UsingXenvXvars")


defXget_str_key(name,Xrequired=False):
XXXXifXnameXinXDEFAULTS:
XXXXXXXXdefaultX=XDEFAULTS[name]
XXXXelse:
XXXXXXXXdefaultX=XNone
XXXXifXnotX(dataX:=Xenv.str(name,Xdefault=default))XandXnotXrequired:
XXXXXXXXlog.warn("NoXstrXkey:X"X+Xname)
XXXXXXXXreturnXNone
XXXXelifXnotXdata:
XXXXXXXXlog.critical("NoXstrXkey:X"X+Xname)
XXXXXXXXsys.exit(2)
XXXXelse:
XXXXXXXXreturnXdata


defXget_int_key(name,Xrequired=False):
XXXXifXnameXinXDEFAULTS:
XXXXXXXXdefaultX=XDEFAULTS[name]
XXXXelse:
XXXXXXXXdefaultX=XNone
XXXXifXnotX(dataX:=Xenv.int(name,Xdefault=default))XandXnotXrequired:
XXXXXXXXlog.warn("NoXintXkey:X"X+Xname)
XXXXXXXXreturnXNone
XXXXelifXnotXdata:
XXXXXXXXlog.critical("NoXintXkey:X"X+Xname)
XXXXXXXXsys.exit(2)
XXXXelse:
XXXXXXXXreturnXdata


defXget_list_key(name,Xrequired=False):
XXXXifXnameXinXDEFAULTS:
XXXXXXXXdefaultX=XDEFAULTS[name]
XXXXelse:
XXXXXXXXdefaultX=XNone
XXXXifXnotX(dataX:=Xenv.list(name,Xdefault=default))XandXnotXrequired:
XXXXXXXXlog.warn("NoXlistXkey:X"X+Xname)
XXXXXXXXreturnX[]
XXXXelifXnotXdata:
XXXXXXXXlog.critical("NoXlistXkey:X"X+Xname)
XXXXXXXXsys.exit(2)
XXXXelse:
XXXXXXXXreturnXdata


defXget_bool_key(name,Xrequired=False):
XXXXifXnameXinXDEFAULTS:
XXXXXXXXdefaultX=XDEFAULTS[name]
XXXXelse:
XXXXXXXXdefaultX=XNone
XXXXifXnotX(dataX:=Xenv.bool(name,Xdefault=default))XandXnotXrequired:
XXXXXXXXlog.warn("NoXboolXkey:X"X+Xname)
XXXXXXXXreturnXFalse
XXXXelifXnotXdata:
XXXXXXXXlog.critical("NoXboolXkey:X"X+Xname)
XXXXXXXXsys.exit(2)
XXXXelse:
XXXXXXXXreturnXdata
