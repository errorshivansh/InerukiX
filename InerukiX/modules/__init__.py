#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2021errorshivansh
#Copyright(C)2020InukaAsith

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

fromIneruki.utils.loggerimportlog

LOADED_MODULES=[]
MOD_HELP={}


deflist_all_modules()->list:
modules_directory="Ineruki/modules"

all_modules=[]
formodule_nameinos.listdir(modules_directory):
path=modules_directory+"/"+module_name

if"__init__"inpathor"__pycache__"inpath:
continue

ifpathinall_modules:
log.path("Moduleswithsamenamecan'texists!")
sys.exit(5)

#Onefilemoduletype
ifpath.endswith(".py"):
#TODO:removesuffix
all_modules.append(module_name.split(".py")[0])

#Moduledirectory
ifos.path.isdir(path)andos.path.exists(path+"/__init__.py"):
all_modules.append(module_name)

returnall_modules


ALL_MODULES=sorted(list_all_modules())
__all__=ALL_MODULES+["ALL_MODULES"]
