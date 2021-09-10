#XCopyrightX(C)X2018X-X2020XMrYacha.XAllXrightsXreserved.XSourceXcodeXavailableXunderXtheXAGPL.
#XCopyrightX(C)X2021Xerrorshivansh
#XCopyrightX(C)X2020XInukaXAsith

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

fromXInerukiX.utils.loggerXimportXlog

LOADED_MODULESX=X[]
MOD_HELPX=X{}


defXlist_all_modules()X->Xlist:
XXXXmodules_directoryX=X"InerukiX/modules"

XXXXall_modulesX=X[]
XXXXforXmodule_nameXinXos.listdir(modules_directory):
XXXXXXXXpathX=Xmodules_directoryX+X"/"X+Xmodule_name

XXXXXXXXifX"__init__"XinXpathXorX"__pycache__"XinXpath:
XXXXXXXXXXXXcontinue

XXXXXXXXifXpathXinXall_modules:
XXXXXXXXXXXXlog.path("ModulesXwithXsameXnameXcan'tXexists!")
XXXXXXXXXXXXsys.exit(5)

XXXXXXXX#XOneXfileXmoduleXtype
XXXXXXXXifXpath.endswith(".py"):
XXXXXXXXXXXX#XTODO:Xremovesuffix
XXXXXXXXXXXXall_modules.append(module_name.split(".py")[0])

XXXXXXXX#XModuleXdirectory
XXXXXXXXifXos.path.isdir(path)XandXos.path.exists(pathX+X"/__init__.py"):
XXXXXXXXXXXXall_modules.append(module_name)

XXXXreturnXall_modules


ALL_MODULESX=Xsorted(list_all_modules())
__all__X=XALL_MODULESX+X["ALL_MODULES"]
