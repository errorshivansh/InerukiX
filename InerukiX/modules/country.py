#Copyright(C)2021errorshivansh


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

fromcountryinfoimportCountryInfo

fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbotasborg


@register(pattern="^/country(.*)")
asyncdefmsg(event):
ifevent.fwd_from:
return
input_str=event.pattern_match.group(1)
lol=input_str
country=CountryInfo(lol)
try:
a=country.info()
except:
awaitevent.reply("CountryNotAvaiableCurrently")
name=a.get("name")
bb=a.get("altSpellings")
hu=""
forpinbb:
hu+=p+","

area=a.get("area")
borders=""
hell=a.get("borders")
forfkinhell:
borders+=fk+","

call=""
WhAt=a.get("callingCodes")
forwhatinWhAt:
call+=what+""

capital=a.get("capital")
currencies=""
fker=a.get("currencies")
forFKerinfker:
currencies+=FKer+","

HmM=a.get("demonym")
geo=a.get("geoJSON")
pablo=geo.get("features")
Pablo=pablo[0]
PAblo=Pablo.get("geometry")
EsCoBaR=PAblo.get("type")
iso=""
iSo=a.get("ISO")
forhitleriniSo:
po=iSo.get(hitler)
iso+=po+","
fla=iSo.get("alpha2")
fla.upper()

languages=a.get("languages")
lMAO=""
forlmaoinlanguages:
lMAO+=lmao+","

nonive=a.get("nativeName")
waste=a.get("population")
reg=a.get("region")
sub=a.get("subregion")
tik=a.get("timezones")
tom=""
forjerryintik:
tom+=jerry+","

GOT=a.get("tld")
lanester=""
fortargaryeninGOT:
lanester+=targaryen+","

wiki=a.get("wiki")

caption=f"""<b><u>InformationGatheredSuccessfully</b></u>
<b>
CountryName:-{name}
AlternativeSpellings:-{hu}
CountryArea:-{area}squarekilometers
Borders:-{borders}
CallingCodes:-{call}
Country'sCapital:-{capital}
Country'scurrency:-{currencies}
Demonym:-{HmM}
CountryType:-{EsCoBaR}
ISONames:-{iso}
Languages:-{lMAO}
NativeName:-{nonive}
population:-{waste}
Region:-{reg}
SubRegion:-{sub}
TimeZones:-{tom}
TopLevelDomain:-{lanester}
wikipedia:-{wiki}</b>
GatheredByIneruki.</b>
"""

awaitborg.send_message(
event.chat_id,
caption,
parse_mode="HTML",
)
