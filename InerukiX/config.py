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

importos
importsys

importyaml
fromenvparseimportenv

fromIneruki.utils.loggerimportlog

DEFAULTS={
"LOAD_MODULES":True,
"DEBUG_MODE":True,
"REDIS_HOST":"localhost",
"REDIS_PORT":6379,
"REDIS_DB_FSM":1,
"MONGODB_URI":"localhost",
"MONGO_DB":"Ineruki",
"API_PORT":8080,
"JOIN_CONFIRM_DURATION":"30m",
}

CONFIG_PATH="data/bot_conf.yaml"
ifos.name=="nt":
log.debug("DetectedWindows,changingconfigpath...")
CONFIG_PATH=os.getcwd()+"\\data\\bot_conf.yaml"

ifos.path.isfile(CONFIG_PATH):
log.info(CONFIG_PATH)
foritemin(
data:=yaml.load(open("data/bot_conf.yaml","r"),Loader=yaml.CLoader)
):
DEFAULTS[item.upper()]=data[item]
else:
log.info("Usingenvvars")


defget_str_key(name,required=False):
ifnameinDEFAULTS:
default=DEFAULTS[name]
else:
default=None
ifnot(data:=env.str(name,default=default))andnotrequired:
log.warn("Nostrkey:"+name)
returnNone
elifnotdata:
log.critical("Nostrkey:"+name)
sys.exit(2)
else:
returndata


defget_int_key(name,required=False):
ifnameinDEFAULTS:
default=DEFAULTS[name]
else:
default=None
ifnot(data:=env.int(name,default=default))andnotrequired:
log.warn("Nointkey:"+name)
returnNone
elifnotdata:
log.critical("Nointkey:"+name)
sys.exit(2)
else:
returndata


defget_list_key(name,required=False):
ifnameinDEFAULTS:
default=DEFAULTS[name]
else:
default=None
ifnot(data:=env.list(name,default=default))andnotrequired:
log.warn("Nolistkey:"+name)
return[]
elifnotdata:
log.critical("Nolistkey:"+name)
sys.exit(2)
else:
returndata


defget_bool_key(name,required=False):
ifnameinDEFAULTS:
default=DEFAULTS[name]
else:
default=None
ifnot(data:=env.bool(name,default=default))andnotrequired:
log.warn("Noboolkey:"+name)
returnFalse
elifnotdata:
log.critical("Noboolkey:"+name)
sys.exit(2)
else:
returndata
