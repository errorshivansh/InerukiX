#XCopyrightX(C)X2021Xerrorshivansh


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

fromXcountryinfoXimportXCountryInfo

fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbotXasXborg


@register(pattern="^/countryX(.*)")
asyncXdefXmsg(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXinput_strX=Xevent.pattern_match.group(1)
XXXXlolX=Xinput_str
XXXXcountryX=XCountryInfo(lol)
XXXXtry:
XXXXXXXXaX=Xcountry.info()
XXXXexcept:
XXXXXXXXawaitXevent.reply("CountryXNotXAvaiableXCurrently")
XXXXnameX=Xa.get("name")
XXXXbbX=Xa.get("altSpellings")
XXXXhuX=X""
XXXXforXpXinXbb:
XXXXXXXXhuX+=XpX+X",XX"

XXXXareaX=Xa.get("area")
XXXXbordersX=X""
XXXXhellX=Xa.get("borders")
XXXXforXfkXinXhell:
XXXXXXXXbordersX+=XfkX+X",XX"

XXXXcallX=X""
XXXXWhAtX=Xa.get("callingCodes")
XXXXforXwhatXinXWhAt:
XXXXXXXXcallX+=XwhatX+X"XX"

XXXXcapitalX=Xa.get("capital")
XXXXcurrenciesX=X""
XXXXfkerX=Xa.get("currencies")
XXXXforXFKerXinXfker:
XXXXXXXXcurrenciesX+=XFKerX+X",XX"

XXXXHmMX=Xa.get("demonym")
XXXXgeoX=Xa.get("geoJSON")
XXXXpabloX=Xgeo.get("features")
XXXXPabloX=Xpablo[0]
XXXXPAbloX=XPablo.get("geometry")
XXXXEsCoBaRX=XPAblo.get("type")
XXXXisoX=X""
XXXXiSoX=Xa.get("ISO")
XXXXforXhitlerXinXiSo:
XXXXXXXXpoX=XiSo.get(hitler)
XXXXXXXXisoX+=XpoX+X",XX"
XXXXflaX=XiSo.get("alpha2")
XXXXfla.upper()

XXXXlanguagesX=Xa.get("languages")
XXXXlMAOX=X""
XXXXforXlmaoXinXlanguages:
XXXXXXXXlMAOX+=XlmaoX+X",XX"

XXXXnoniveX=Xa.get("nativeName")
XXXXwasteX=Xa.get("population")
XXXXregX=Xa.get("region")
XXXXsubX=Xa.get("subregion")
XXXXtikX=Xa.get("timezones")
XXXXtomX=X""
XXXXforXjerryXinXtik:
XXXXXXXXtomX+=XjerryX+X",XXX"

XXXXGOTX=Xa.get("tld")
XXXXlanesterX=X""
XXXXforXtargaryenXinXGOT:
XXXXXXXXlanesterX+=XtargaryenX+X",XXX"

XXXXwikiX=Xa.get("wiki")

XXXXcaptionX=Xf"""<b><u>InformationXGatheredXSuccessfully</b></u>
<b>
CountryXName:-X{name}
AlternativeXSpellings:-X{hu}
CountryXArea:-X{area}XsquareXkilometers
Borders:-X{borders}
CallingXCodes:-X{call}
Country'sXCapital:-X{capital}
Country'sXcurrency:-X{currencies}
Demonym:-X{HmM}
CountryXType:-X{EsCoBaR}
ISOXNames:-X{iso}
Languages:-X{lMAO}
NativeXName:-X{nonive}
population:-X{waste}
Region:-X{reg}
SubXRegion:-X{sub}
TimeXZones:-X{tom}
TopXLevelXDomain:-X{lanester}
wikipedia:-X{wiki}</b>
GatheredXByXInerukiXX.</b>
"""

XXXXawaitXborg.send_message(
XXXXXXXXevent.chat_id,
XXXXXXXXcaption,
XXXXXXXXparse_mode="HTML",
XXXX)
