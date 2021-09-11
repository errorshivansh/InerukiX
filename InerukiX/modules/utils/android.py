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

importhttpx
importrapidjsonasjson

#Thisfileisanadaptation/portfromtheGalaxyHelperBot.
#Copyright(C)KassemSYR.Allrightsreserved.


classGetDevice:
def__init__(self,device):
"""Getdeviceinfobycodenameormodel!"""
self.device=device

asyncdefget(self):
ifself.device.lower().startswith("sm-"):
asyncwithhttpx.AsyncClient(http2=True)ashttp:
data=awaithttp.get(
"https://raw.githubusercontent.com/androidtrackers/certified-android-devices/master/by_model.json"
)
db=json.loads(data.content)
awaithttp.aclose()
try:
name=db[self.device.upper()][0]["name"]
device=db[self.device.upper()][0]["device"]
brand=db[self.device.upper()][0]["brand"]
model=self.device.lower()
return{"name":name,"device":device,"model":model,"brand":brand}
exceptKeyError:
returnFalse
else:
asyncwithhttpx.AsyncClient(http2=True)ashttp:
data=awaithttp.get(
"https://raw.githubusercontent.com/androidtrackers/certified-android-devices/master/by_device.json"
)
db=json.loads(data.content)
awaithttp.aclose()
newdevice=(
self.device.strip("lte").lower()
ifself.device.startswith("beyond")
elseself.device.lower()
)
try:
name=db[newdevice][0]["name"]
model=db[newdevice][0]["model"]
brand=db[newdevice][0]["brand"]
device=self.device.lower()
return{"name":name,"device":device,"model":model,"brand":brand}
exceptKeyError:
returnFalse
