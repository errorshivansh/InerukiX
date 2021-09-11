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

importtime

importhttpx
importrapidjsonasjson
fromaiogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup
frombs4importBeautifulSoup

fromInerukiimportdecorator
fromIneruki.decoratorimportregister

from.utils.androidimportGetDevice
from.utils.disableimportdisableable_dec
from.utils.messageimportget_arg,get_cmd

MIUI_FIRM="https://raw.githubusercontent.com/iaomiFirmwareUpdater/miui-updates-tracker/master/data/latest.yml"
REALME_FIRM="https://raw.githubusercontent.com/RealmeUpdater/realme-updates-tracker/master/data/latest.yml"


@register(cmds="whatis")
@disableable_dec("whatis")
asyncdefwhatis(message):
device=get_arg(message)
ifnotdevice:
m="Pleasewriteyourcodenameintoit,i.e<code>/whatisraphael</code>"
awaitmessage.reply(m)
return

data=awaitGetDevice(device).get()
ifdata:
name=data["name"]
device=data["device"]
brand=data["brand"]
data["model"]
else:
m="coudn'tfindyourdevice,checkdevice&try!"
awaitmessage.reply(m)
return

m=f"<b>{device}</b>is<code>{brand}{name}</code>\n"
awaitmessage.reply(m)


@decorator.register(cmds=["models","variants"])
@disableable_dec("models")
asyncdefvariants(message):
device=get_arg(message)
ifnotdevice:
m="Pleasewriteyourcodenameintoit,i.e<code>/specsherolte</code>"
awaitmessage.reply(m)
return

data=awaitGetDevice(device).get()
ifdata:
name=data["name"]
device=data["device"]
else:
m="coudn'tfindyourdevice,chackdevice&try!"
awaitmessage.reply(m)
return

asyncwithhttpx.AsyncClient(http2=True)ashttp:
data=awaithttp.get(
"https://raw.githubusercontent.com/androidtrackers/certified-android-devices/master/by_device.json"
)
db=json.loads(data.content)
device=db[device]
m=f"<b>{name}</b>variants:\n\n"

foriindevice:
name=i["name"]
model=i["model"]
m+="<b>Model</b>:<code>{}</code>\n<b>Name:</b><code>{}</code>\n\n".format(
model,name
)

awaithttp.aclose()
awaitmessage.reply(m)


@register(cmds="magisk")
@disableable_dec("magisk")
asyncdefmagisk(message):
url="https://raw.githubusercontent.com/topjohnwu/magisk_files/"
releases="<b>LatestMagiskReleases:</b>\n"
variant=["master/stable","master/beta","canary/canary"]
forvariantsinvariant:
asyncwithhttpx.AsyncClient(http2=True)ashttp:
fetch=awaithttp.get(url+variants+".json")
data=json.loads(fetch.content)
ifvariants=="master/stable":
name="<b>Stable</b>"
cc=0
branch="master"
elifvariants=="master/beta":
name="<b>Beta</b>"
cc=0
branch="master"
elifvariants=="canary/canary":
name="<b>Canary</b>"
cc=1
branch="canary"

ifvariants=="canary/canary":
releases+=f'{name}:<ahref="{url}{branch}/{data["magisk"]["link"]}">v{data["magisk"]["version"]}</a>(<code>{data["magisk"]["versionCode"]}</code>)|'
else:
releases+=f'{name}:<ahref="{data["magisk"]["link"]}">v{data["magisk"]["version"]}</a>(<code>{data["magisk"]["versionCode"]}</code>)|'

ifcc==1:
releases+=(
f'<ahref="{url}{branch}/{data["uninstaller"]["link"]}">Uninstaller</a>|'
f'<ahref="{url}{branch}/{data["magisk"]["note"]}">Changelog</a>\n'
)
else:
releases+=(
f'<ahref="{data["uninstaller"]["link"]}">Uninstaller</a>\n'
f'<ahref="{data["magisk"]["note"]}">Changelog</a>\n'
)

awaithttp.aclose()
awaitmessage.reply(releases,disable_web_page_preview=True)


@register(cmds="phh")
@disableable_dec("phh")
asyncdefphh(message):
asyncwithhttpx.AsyncClient(http2=True)ashttp:
fetch=awaithttp.get(
"https://api.github.com/repos/phhusson/treble_experimentations/releases/latest"
)
usr=json.loads(fetch.content)
text="<b>Phh'slatestGSIrelease(s):</b>\n"
foriinrange(len(usr)):
try:
name=usr["assets"][i]["name"]
url=usr["assets"][i]["browser_download_url"]
text+=f"<ahref='{url}'>{name}</a>\n"
exceptIndexError:
continue

awaithttp.aclose()
awaitmessage.reply(text)


@register(cmds="phhmagisk")
@disableable_dec("phhmagisk")
asyncdefphh_magisk(message):
asyncwithhttpx.AsyncClient(http2=True)ashttp:
fetch=awaithttp.get(
"https://api.github.com/repos/expressluke/phh-magisk-builder/releases/latest"
)
usr=json.loads(fetch.content)
text="<b>Phh'slatestMagiskrelease(s):</b>\n"
foriinrange(len(usr)):
try:
usr["assets"][i]["name"]
url=usr["assets"][i]["browser_download_url"]
tag=usr["tag_name"]
size_bytes=usr["assets"][i]["size"]
size=float("{:.2f}".format((size_bytes/1024)/1024))
text+=f"<b>Tag:</b><code>{tag}</code>\n"
text+=f"<b>Size</b>:<code>{size}MB</code>\n\n"
btn="Clickheretodownload!"
button=InlineKeyboardMarkup().add(InlineKeyboardButton(text=btn,url=url))
exceptIndexError:
continue

awaithttp.aclose()
awaitmessage.reply(text,reply_markup=button)
return


@register(cmds="twrp")
@disableable_dec("twrp")
asyncdeftwrp(message):
device=get_arg(message).lower()

ifnotdevice:
m="Typethedevicecodename,example:<code>/twrpj7xelte</code>"
awaitmessage.reply(m)
return

asyncwithhttpx.AsyncClient(http2=True)ashttp:
url=awaithttp.get(f"https://eu.dl.twrp.me/{device}/")
ifurl.status_code==404:
m=f"TWRPisnotavailablefor<code>{device}</code>"
awaitmessage.reply(m)
return

else:
m="<b><u>TeamWinRecovery<i>official</i>release</u></b>\n"
m+=f"<b>Device:</b>{device}\n"
page=BeautifulSoup(url.content,"lxml")
date=page.find("em").text.strip()
m+=f"<b>Updated:</b><code>{date}</code>\n"
trs=page.find("table").find_all("tr")
row=2iftrs[0].find("a").text.endswith("tar")else1

foriinrange(row):
download=trs[i].find("a")
dl_link=f"https://dl.twrp.me{download['href']}"
dl_file=download.text
size=trs[i].find("span",{"class":"filesize"}).text
m+=f"<b>Size:</b><code>{size}</code>\n"
m+=f"<b>File:</b><code>{dl_file.lower()}</code>"
btn="⬇️Download"
button=InlineKeyboardMarkup().add(InlineKeyboardButton(text=btn,url=dl_link))

awaithttp.aclose()
awaitmessage.reply(m,reply_markup=button)


@decorator.register(cmds=["samcheck","samget"])
@disableable_dec("samcheck")
asyncdefcheck(message):
try:
msg_args=message.text.split()
temp=msg_args[1]
csc=msg_args[2]
exceptIndexError:
m=f"Pleasetypeyourdevice<b>MODEL</b>and<b>CSC</b>intoit!\ni.e<code>/{get_cmd(message)}SM-J710MNZTO</code>!"
awaitmessage.reply(m)
return

model="sm-"+tempifnottemp.upper().startswith("SM-")elsetemp
asyncwithhttpx.AsyncClient(http2=True)ashttp:
fota=awaithttp.get(
f"http://fota-cloud-dn.ospserver.net/firmware/{csc.upper()}/{model.upper()}/version.xml"
)
test=awaithttp.get(
f"http://fota-cloud-dn.ospserver.net/firmware/{csc.upper()}/{model.upper()}/version.test.xml"
)
awaithttp.aclose()
iftest.status_code!=200:
m=f"Couldn'tfindanyfirmwaresfor{temp.upper()}-{csc.upper()},pleaserefineyoursearchortryagainlater!"
awaitmessage.reply(m)
return

page1=BeautifulSoup(fota.content,"lxml")
page2=BeautifulSoup(test.content,"lxml")
os1=page1.find("latest").get("o")
os2=page2.find("latest").get("o")
ifpage1.find("latest").text.strip():
pda1,csc1,phone1=page1.find("latest").text.strip().split("/")
m=f"<b>MODEL:</b><code>{model.upper()}</code>\n<b>CSC:</b><code>{csc.upper()}</code>\n\n"
m+="<b>Latestavailablefirmware:</b>\n"
m+=f"•PDA:<code>{pda1}</code>\n•CSC:<code>{csc1}</code>\n"
ifphone1:
m+=f"•Phone:<code>{phone1}</code>\n"
ifos1:
m+=f"•Android:<code>{os1}</code>\n"
m+="\n"
else:
m=f"<b>Nopublicreleasefoundfor{model.upper()}and{csc.upper()}.</b>\n\n"
m+="<b>Latesttestfirmware:</b>\n"
iflen(page2.find("latest").text.strip().split("/"))==3:
pda2,csc2,phone2=page2.find("latest").text.strip().split("/")
m+=f"•PDA:<code>{pda2}</code>\n•CSC:<code>{csc2}</code>\n"
ifphone2:
m+=f"•Phone:<code>{phone2}</code>\n"
ifos2:
m+=f"•Android:<code>{os2}</code>\n"
else:
md5=page2.find("latest").text.strip()
m+=f"•Hash:<code>{md5}</code>\n•Android:<code>{os2}</code>\n"

ifget_cmd(message)=="samcheck":
awaitmessage.reply(m)

elifget_cmd(message)=="samget":
m+="\n<b>Downloadfrombelow:</b>\n"
buttons=InlineKeyboardMarkup()
buttons.add(
InlineKeyboardButton(
"SamMobile",
url="https://www.sammobile.com/samsung/firmware/{}/{}/".format(
model.upper(),csc.upper()
),
),
InlineKeyboardButton(
"SamFw",
url="https://samfw.com/firmware/{}/{}/".format(
model.upper(),csc.upper()
),
),
InlineKeyboardButton(
"SamFrew",
url="https://samfrew.com/model/{}/region/{}/".format(
model.upper(),csc.upper()
),
),
)

awaitmessage.reply(m,reply_markup=buttons)


@decorator.register(cmds=["ofox","of"])
@disableable_dec("ofox")
asyncdeforangefox(message):
API_HOST="https://api.orangefox.download/v3/"
try:
args=message.text.split()
codename=args[1].lower()
exceptBaseException:
codename=""
try:
build_type=args[2].lower()
exceptBaseException:
build_type=""

ifbuild_type=="":
build_type="stable"

ifcodename=="devices"orcodename=="":
reply_text=(
f"<b>OrangeFoxRecovery<i>{build_type}</i>iscurrentlyavaiblefor:</b>"
)

asyncwithhttpx.AsyncClient(http2=True)ashttp:
data=awaithttp.get(
API_HOST+f"devices/?release_type={build_type}&sort=device_name_asc"
)
devices=json.loads(data.text)
awaithttp.aclose()
try:
fordeviceindevices["data"]:
reply_text+=(
f"\n-{device['full_name']}(<code>{device['codename']}</code>)"
)
exceptBaseException:
awaitmessage.reply(
f"'<b>{build_type}</b>'isnotatypeofbuildavailable,thetypesarejust'<b>beta</b>'or'<b>stable</b>'."
)
return

ifbuild_type=="stable":
reply_text+=(
"\n\n"
+f"TogetthelatestStablereleaseuse<code>/ofox(codename)</code>,forexample:<code>/ofoxraphael</code>"
)
elifbuild_type=="beta":
reply_text+=(
"\n\n"
+f"TogetthelatestBetareleaseuse<code>/ofox(codename)beta</code>,forexample:<code>/ofoxraphaelbeta</code>"
)
awaitmessage.reply(reply_text)
return

asyncwithhttpx.AsyncClient(http2=True)ashttp:
data=awaithttp.get(API_HOST+f"devices/get?codename={codename}")
device=json.loads(data.text)
awaithttp.aclose()
ifdata.status_code==404:
awaitmessage.reply("Deviceisnotfound!")
return

asyncwithhttpx.AsyncClient(http2=True)ashttp:
data=awaithttp.get(
API_HOST
+f"releases/?codename={codename}&type={build_type}&sort=date_desc&limit=1"
)
ifdata.status_code==404:
btn="Device'spage"
url=f"https://orangefox.download/device/{device['codename']}"
button=InlineKeyboardMarkup().add(InlineKeyboardButton(text=btn,url=url))
awaitmessage.reply(
f"⚠️Thereisno'<b>{build_type}</b>'releasesfor<b>{device['full_name']}</b>.",
reply_markup=button,
disable_web_page_preview=True,
)
return
find_id=json.loads(data.text)
awaithttp.aclose()
forbuildinfind_id["data"]:
file_id=build["_id"]

asyncwithhttpx.AsyncClient(http2=True)ashttp:
data=awaithttp.get(API_HOST+f"releases/get?_id={file_id}")
release=json.loads(data.text)
awaithttp.aclose()
ifdata.status_code==404:
awaitmessage.reply("Releaseisnotfound!")
return

reply_text=f"<u><b>OrangeFoxRecovery<i>{build_type}</i>release</b></u>\n"
reply_text+=("<b>Device:</b>{fullname}(<code>{codename}</code>)\n").format(
fullname=device["full_name"],codename=device["codename"]
)
reply_text+=("<b>Version:</b>{}\n").format(release["version"])
reply_text+=("<b>Releasedate:</b>{}\n").format(
time.strftime("%d/%m/%Y",time.localtime(release["date"]))
)

reply_text+=("<b>Maintainer:</b>{name}\n").format(
name=device["maintainer"]["name"]
)
changelog=release["changelog"]
try:
reply_text+="<u><b>Changelog:</b></u>\n"
forentry_numinrange(len(changelog)):
ifentry_num==10:
break
reply_text+=f"-{changelog[entry_num]}\n"
exceptBaseException:
pass

btn="⬇️Download"
url=release["mirrors"]["DL"]
button=InlineKeyboardMarkup().add(InlineKeyboardButton(text=btn,url=url))
awaitmessage.reply(reply_text,reply_markup=button,disable_web_page_preview=True)
return


__mod_name__="Android"

__help__="""
ModulespeciallymadeforAndroidusers.

<b>GSI</b>
-/phh:GetthelatestPHHAOSPGSIs.
-/phhmagisk:GetthelatestPHHMagisk.

<b>Devicefirmware:</b>
-/samcheck(model)(csc):Samsungonly-showsthelatestfirmwareinfoforthegivendevice,takenfromsamsungservers.
-/samget(model)(csc):Similartothe<code>/samcheck</code>commandbuthavingdownloadbuttons.

<b>Misc</b>
-/magisk:GetlatestMagiskreleases.
-/twrp(codename):GetslatestTWRPfortheandroiddeviceusingthecodename.
-/ofox(codename):GetslatestOFRPfortheandroiddeviceusingthecodename.
-/ofoxdevices:SendsthelistofdeviceswithstablereleasessupportedbyOFRP.
-/models(codename):SearchforAndroiddevicemodelsusingcodename.
-/whatis(codename):Findoutwhichsmartphoneisusingthecodename.
"""
