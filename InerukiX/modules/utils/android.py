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

importXhttpx
importXrapidjsonXasXjson

#XThisXfileXisXanXadaptationX/XportXfromXtheXGalaxyXHelperXBot.
#XCopyrightX(C)XKassemSYR.XAllXrightsXreserved.


classXGetDevice:
XXXXdefX__init__(self,Xdevice):
XXXXXXXX"""GetXdeviceXinfoXbyXcodenameXorXmodel!"""
XXXXXXXXself.deviceX=Xdevice

XXXXasyncXdefXget(self):
XXXXXXXXifXself.device.lower().startswith("sm-"):
XXXXXXXXXXXXasyncXwithXhttpx.AsyncClient(http2=True)XasXhttp:
XXXXXXXXXXXXXXXXdataX=XawaitXhttp.get(
XXXXXXXXXXXXXXXXXXXX"https://raw.githubusercontent.com/androidtrackers/certified-android-devices/master/by_model.json"
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXdbX=Xjson.loads(data.content)
XXXXXXXXXXXXXXXXawaitXhttp.aclose()
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXnameX=Xdb[self.device.upper()][0]["name"]
XXXXXXXXXXXXXXXXdeviceX=Xdb[self.device.upper()][0]["device"]
XXXXXXXXXXXXXXXXbrandX=Xdb[self.device.upper()][0]["brand"]
XXXXXXXXXXXXXXXXmodelX=Xself.device.lower()
XXXXXXXXXXXXXXXXreturnX{"name":Xname,X"device":Xdevice,X"model":Xmodel,X"brand":Xbrand}
XXXXXXXXXXXXexceptXKeyError:
XXXXXXXXXXXXXXXXreturnXFalse
XXXXXXXXelse:
XXXXXXXXXXXXasyncXwithXhttpx.AsyncClient(http2=True)XasXhttp:
XXXXXXXXXXXXXXXXdataX=XawaitXhttp.get(
XXXXXXXXXXXXXXXXXXXX"https://raw.githubusercontent.com/androidtrackers/certified-android-devices/master/by_device.json"
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXdbX=Xjson.loads(data.content)
XXXXXXXXXXXXXXXXawaitXhttp.aclose()
XXXXXXXXXXXXnewdeviceX=X(
XXXXXXXXXXXXXXXXself.device.strip("lte").lower()
XXXXXXXXXXXXXXXXifXself.device.startswith("beyond")
XXXXXXXXXXXXXXXXelseXself.device.lower()
XXXXXXXXXXXX)
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXnameX=Xdb[newdevice][0]["name"]
XXXXXXXXXXXXXXXXmodelX=Xdb[newdevice][0]["model"]
XXXXXXXXXXXXXXXXbrandX=Xdb[newdevice][0]["brand"]
XXXXXXXXXXXXXXXXdeviceX=Xself.device.lower()
XXXXXXXXXXXXXXXXreturnX{"name":Xname,X"device":Xdevice,X"model":Xmodel,X"brand":Xbrand}
XXXXXXXXXXXXexceptXKeyError:
XXXXXXXXXXXXXXXXreturnXFalse
