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

importXtime

importXhttpx
importXrapidjsonXasXjson
fromXaiogram.typesXimportXInlineKeyboardButton,XInlineKeyboardMarkup
fromXbs4XimportXBeautifulSoup

fromXInerukiXXimportXdecorator
fromXInerukiX.decoratorXimportXregister

fromX.utils.androidXimportXGetDevice
fromX.utils.disableXimportXdisableable_dec
fromX.utils.messageXimportXget_arg,Xget_cmd

MIUI_FIRMX=X"https://raw.githubusercontent.com/XiaomiFirmwareUpdater/miui-updates-tracker/master/data/latest.yml"
REALME_FIRMX=X"https://raw.githubusercontent.com/RealmeUpdater/realme-updates-tracker/master/data/latest.yml"


@register(cmds="whatis")
@disableable_dec("whatis")
asyncXdefXwhatis(message):
XXXXdeviceX=Xget_arg(message)
XXXXifXnotXdevice:
XXXXXXXXmX=X"PleaseXwriteXyourXcodenameXintoXit,Xi.eX<code>/whatisXraphael</code>"
XXXXXXXXawaitXmessage.reply(m)
XXXXXXXXreturn

XXXXdataX=XawaitXGetDevice(device).get()
XXXXifXdata:
XXXXXXXXnameX=Xdata["name"]
XXXXXXXXdeviceX=Xdata["device"]
XXXXXXXXbrandX=Xdata["brand"]
XXXXXXXXdata["model"]
XXXXelse:
XXXXXXXXmX=X"coudn'tXfindXyourXdevice,XcheckXdeviceX&Xtry!"
XXXXXXXXawaitXmessage.reply(m)
XXXXXXXXreturn

XXXXmX=Xf"<b>{device}</b>XisX<code>{brand}X{name}</code>\n"
XXXXawaitXmessage.reply(m)


@decorator.register(cmds=["models",X"variants"])
@disableable_dec("models")
asyncXdefXvariants(message):
XXXXdeviceX=Xget_arg(message)
XXXXifXnotXdevice:
XXXXXXXXmX=X"PleaseXwriteXyourXcodenameXintoXit,Xi.eX<code>/specsXherolte</code>"
XXXXXXXXawaitXmessage.reply(m)
XXXXXXXXreturn

XXXXdataX=XawaitXGetDevice(device).get()
XXXXifXdata:
XXXXXXXXnameX=Xdata["name"]
XXXXXXXXdeviceX=Xdata["device"]
XXXXelse:
XXXXXXXXmX=X"coudn'tXfindXyourXdevice,XchackXdeviceX&Xtry!"
XXXXXXXXawaitXmessage.reply(m)
XXXXXXXXreturn

XXXXasyncXwithXhttpx.AsyncClient(http2=True)XasXhttp:
XXXXXXXXdataX=XawaitXhttp.get(
XXXXXXXXXXXX"https://raw.githubusercontent.com/androidtrackers/certified-android-devices/master/by_device.json"
XXXXXXXX)
XXXXXXXXdbX=Xjson.loads(data.content)
XXXXdeviceX=Xdb[device]
XXXXmX=Xf"<b>{name}</b>Xvariants:\n\n"

XXXXforXiXinXdevice:
XXXXXXXXnameX=Xi["name"]
XXXXXXXXmodelX=Xi["model"]
XXXXXXXXmX+=X"<b>Model</b>:X<code>{}</code>X\n<b>Name:</b>X<code>{}</code>\n\n".format(
XXXXXXXXXXXXmodel,Xname
XXXXXXXX)

XXXXawaitXhttp.aclose()
XXXXawaitXmessage.reply(m)


@register(cmds="magisk")
@disableable_dec("magisk")
asyncXdefXmagisk(message):
XXXXurlX=X"https://raw.githubusercontent.com/topjohnwu/magisk_files/"
XXXXreleasesX=X"<b>LatestXMagiskXReleases:</b>\n"
XXXXvariantX=X["master/stable",X"master/beta",X"canary/canary"]
XXXXforXvariantsXinXvariant:
XXXXXXXXasyncXwithXhttpx.AsyncClient(http2=True)XasXhttp:
XXXXXXXXXXXXfetchX=XawaitXhttp.get(urlX+XvariantsX+X".json")
XXXXXXXXXXXXdataX=Xjson.loads(fetch.content)
XXXXXXXXifXvariantsX==X"master/stable":
XXXXXXXXXXXXnameX=X"<b>Stable</b>"
XXXXXXXXXXXXccX=X0
XXXXXXXXXXXXbranchX=X"master"
XXXXXXXXelifXvariantsX==X"master/beta":
XXXXXXXXXXXXnameX=X"<b>Beta</b>"
XXXXXXXXXXXXccX=X0
XXXXXXXXXXXXbranchX=X"master"
XXXXXXXXelifXvariantsX==X"canary/canary":
XXXXXXXXXXXXnameX=X"<b>Canary</b>"
XXXXXXXXXXXXccX=X1
XXXXXXXXXXXXbranchX=X"canary"

XXXXXXXXifXvariantsX==X"canary/canary":
XXXXXXXXXXXXreleasesX+=Xf'{name}:X<aXhref="{url}{branch}/{data["magisk"]["link"]}">v{data["magisk"]["version"]}</a>X(<code>{data["magisk"]["versionCode"]}</code>)X|X'
XXXXXXXXelse:
XXXXXXXXXXXXreleasesX+=Xf'{name}:X<aXhref="{data["magisk"]["link"]}">v{data["magisk"]["version"]}</a>X(<code>{data["magisk"]["versionCode"]}</code>)X|X'

XXXXXXXXifXccX==X1:
XXXXXXXXXXXXreleasesX+=X(
XXXXXXXXXXXXXXXXf'<aXhref="{url}{branch}/{data["uninstaller"]["link"]}">Uninstaller</a>X|X'
XXXXXXXXXXXXXXXXf'<aXhref="{url}{branch}/{data["magisk"]["note"]}">Changelog</a>\n'
XXXXXXXXXXXX)
XXXXXXXXelse:
XXXXXXXXXXXXreleasesX+=X(
XXXXXXXXXXXXXXXXf'<aXhref="{data["uninstaller"]["link"]}">Uninstaller</a>\n'
XXXXXXXXXXXXXXXXf'<aXhref="{data["magisk"]["note"]}">Changelog</a>\n'
XXXXXXXXXXXX)

XXXXawaitXhttp.aclose()
XXXXawaitXmessage.reply(releases,Xdisable_web_page_preview=True)


@register(cmds="phh")
@disableable_dec("phh")
asyncXdefXphh(message):
XXXXasyncXwithXhttpx.AsyncClient(http2=True)XasXhttp:
XXXXXXXXfetchX=XawaitXhttp.get(
XXXXXXXXXXXX"https://api.github.com/repos/phhusson/treble_experimentations/releases/latest"
XXXXXXXX)
XXXXXXXXusrX=Xjson.loads(fetch.content)
XXXXtextX=X"<b>Phh'sXlatestXGSIXrelease(s):</b>\n"
XXXXforXiXinXrange(len(usr)):
XXXXXXXXtry:
XXXXXXXXXXXXnameX=Xusr["assets"][i]["name"]
XXXXXXXXXXXXurlX=Xusr["assets"][i]["browser_download_url"]
XXXXXXXXXXXXtextX+=Xf"<aXhref='{url}'>{name}</a>\n"
XXXXXXXXexceptXIndexError:
XXXXXXXXXXXXcontinue

XXXXawaitXhttp.aclose()
XXXXawaitXmessage.reply(text)


@register(cmds="phhmagisk")
@disableable_dec("phhmagisk")
asyncXdefXphh_magisk(message):
XXXXasyncXwithXhttpx.AsyncClient(http2=True)XasXhttp:
XXXXXXXXfetchX=XawaitXhttp.get(
XXXXXXXXXXXX"https://api.github.com/repos/expressluke/phh-magisk-builder/releases/latest"
XXXXXXXX)
XXXXXXXXusrX=Xjson.loads(fetch.content)
XXXXtextX=X"<b>Phh'sXlatestXMagiskXrelease(s):</b>\n"
XXXXforXiXinXrange(len(usr)):
XXXXXXXXtry:
XXXXXXXXXXXXusr["assets"][i]["name"]
XXXXXXXXXXXXurlX=Xusr["assets"][i]["browser_download_url"]
XXXXXXXXXXXXtagX=Xusr["tag_name"]
XXXXXXXXXXXXsize_bytesX=Xusr["assets"][i]["size"]
XXXXXXXXXXXXsizeX=Xfloat("{:.2f}".format((size_bytesX/X1024)X/X1024))
XXXXXXXXXXXXtextX+=Xf"<b>Tag:</b>X<code>{tag}</code>\n"
XXXXXXXXXXXXtextX+=Xf"<b>Size</b>:X<code>{size}XMB</code>\n\n"
XXXXXXXXXXXXbtnX=X"ClickXhereXtoXdownload!"
XXXXXXXXXXXXbuttonX=XInlineKeyboardMarkup().add(InlineKeyboardButton(text=btn,Xurl=url))
XXXXXXXXexceptXIndexError:
XXXXXXXXXXXXcontinue

XXXXawaitXhttp.aclose()
XXXXawaitXmessage.reply(text,Xreply_markup=button)
XXXXreturn


@register(cmds="twrp")
@disableable_dec("twrp")
asyncXdefXtwrp(message):
XXXXdeviceX=Xget_arg(message).lower()

XXXXifXnotXdevice:
XXXXXXXXmX=X"TypeXtheXdeviceXcodename,Xexample:X<code>/twrpXj7xelte</code>"
XXXXXXXXawaitXmessage.reply(m)
XXXXXXXXreturn

XXXXasyncXwithXhttpx.AsyncClient(http2=True)XasXhttp:
XXXXXXXXurlX=XawaitXhttp.get(f"https://eu.dl.twrp.me/{device}/")
XXXXifXurl.status_codeX==X404:
XXXXXXXXmX=Xf"TWRPXisXnotXavailableXforX<code>{device}</code>"
XXXXXXXXawaitXmessage.reply(m)
XXXXXXXXreturn

XXXXelse:
XXXXXXXXmX=X"<b><u>TeamWinXRecoveryX<i>official</i>Xrelease</u></b>\n"
XXXXXXXXmX+=Xf"XX<b>Device:</b>X{device}\n"
XXXXXXXXpageX=XBeautifulSoup(url.content,X"lxml")
XXXXXXXXdateX=Xpage.find("em").text.strip()
XXXXXXXXmX+=Xf"XX<b>Updated:</b>X<code>{date}</code>\n"
XXXXXXXXtrsX=Xpage.find("table").find_all("tr")
XXXXXXXXrowX=X2XifXtrs[0].find("a").text.endswith("tar")XelseX1

XXXXXXXXforXiXinXrange(row):
XXXXXXXXXXXXdownloadX=Xtrs[i].find("a")
XXXXXXXXXXXXdl_linkX=Xf"https://dl.twrp.me{download['href']}"
XXXXXXXXXXXXdl_fileX=Xdownload.text
XXXXXXXXXXXXsizeX=Xtrs[i].find("span",X{"class":X"filesize"}).text
XXXXXXXXmX+=Xf"XX<b>Size:</b>X<code>{size}</code>\n"
XXXXXXXXmX+=Xf"XX<b>File:</b>X<code>{dl_file.lower()}</code>"
XXXXXXXXbtnX=X"⬇️XDownload"
XXXXXXXXbuttonX=XInlineKeyboardMarkup().add(InlineKeyboardButton(text=btn,Xurl=dl_link))

XXXXXXXXawaitXhttp.aclose()
XXXXXXXXawaitXmessage.reply(m,Xreply_markup=button)


@decorator.register(cmds=["samcheck",X"samget"])
@disableable_dec("samcheck")
asyncXdefXcheck(message):
XXXXtry:
XXXXXXXXmsg_argsX=Xmessage.text.split()
XXXXXXXXtempX=Xmsg_args[1]
XXXXXXXXcscX=Xmsg_args[2]
XXXXexceptXIndexError:
XXXXXXXXmX=Xf"PleaseXtypeXyourXdeviceX<b>MODEL</b>XandX<b>CSC</b>XintoXit!\ni.eX<code>/{get_cmd(message)}XSM-J710MNXZTO</code>!"
XXXXXXXXawaitXmessage.reply(m)
XXXXXXXXreturn

XXXXmodelX=X"sm-"X+XtempXifXnotXtemp.upper().startswith("SM-")XelseXtemp
XXXXasyncXwithXhttpx.AsyncClient(http2=True)XasXhttp:
XXXXXXXXfotaX=XawaitXhttp.get(
XXXXXXXXXXXXf"http://fota-cloud-dn.ospserver.net/firmware/{csc.upper()}/{model.upper()}/version.xml"
XXXXXXXX)
XXXXXXXXtestX=XawaitXhttp.get(
XXXXXXXXXXXXf"http://fota-cloud-dn.ospserver.net/firmware/{csc.upper()}/{model.upper()}/version.test.xml"
XXXXXXXX)
XXXXawaitXhttp.aclose()
XXXXifXtest.status_codeX!=X200:
XXXXXXXXmX=Xf"Couldn'tXfindXanyXfirmwaresXforX{temp.upper()}X-X{csc.upper()},XpleaseXrefineXyourXsearchXorXtryXagainXlater!"
XXXXXXXXawaitXmessage.reply(m)
XXXXXXXXreturn

XXXXpage1X=XBeautifulSoup(fota.content,X"lxml")
XXXXpage2X=XBeautifulSoup(test.content,X"lxml")
XXXXos1X=Xpage1.find("latest").get("o")
XXXXos2X=Xpage2.find("latest").get("o")
XXXXifXpage1.find("latest").text.strip():
XXXXXXXXpda1,Xcsc1,Xphone1X=Xpage1.find("latest").text.strip().split("/")
XXXXXXXXmX=Xf"<b>MODEL:</b>X<code>{model.upper()}</code>\n<b>CSC:</b>X<code>{csc.upper()}</code>\n\n"
XXXXXXXXmX+=X"<b>LatestXavailableXfirmware:</b>\n"
XXXXXXXXmX+=Xf"•XPDA:X<code>{pda1}</code>\n•XCSC:X<code>{csc1}</code>\n"
XXXXXXXXifXphone1:
XXXXXXXXXXXXmX+=Xf"•XPhone:X<code>{phone1}</code>\n"
XXXXXXXXifXos1:
XXXXXXXXXXXXmX+=Xf"•XAndroid:X<code>{os1}</code>\n"
XXXXXXXXmX+=X"\n"
XXXXelse:
XXXXXXXXmX=Xf"<b>NoXpublicXreleaseXfoundXforX{model.upper()}XandX{csc.upper()}.</b>\n\n"
XXXXmX+=X"<b>LatestXtestXfirmware:</b>\n"
XXXXifXlen(page2.find("latest").text.strip().split("/"))X==X3:
XXXXXXXXpda2,Xcsc2,Xphone2X=Xpage2.find("latest").text.strip().split("/")
XXXXXXXXmX+=Xf"•XPDA:X<code>{pda2}</code>\n•XCSC:X<code>{csc2}</code>\n"
XXXXXXXXifXphone2:
XXXXXXXXXXXXmX+=Xf"•XPhone:X<code>{phone2}</code>\n"
XXXXXXXXifXos2:
XXXXXXXXXXXXmX+=Xf"•XAndroid:X<code>{os2}</code>\n"
XXXXelse:
XXXXXXXXmd5X=Xpage2.find("latest").text.strip()
XXXXXXXXmX+=Xf"•XHash:X<code>{md5}</code>\n•XAndroid:X<code>{os2}</code>\n"

XXXXifXget_cmd(message)X==X"samcheck":
XXXXXXXXawaitXmessage.reply(m)

XXXXelifXget_cmd(message)X==X"samget":
XXXXXXXXmX+=X"\n<b>DownloadXfromXbelow:</b>\n"
XXXXXXXXbuttonsX=XInlineKeyboardMarkup()
XXXXXXXXbuttons.add(
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXX"SamMobile",
XXXXXXXXXXXXXXXXurl="https://www.sammobile.com/samsung/firmware/{}/{}/".format(
XXXXXXXXXXXXXXXXXXXXmodel.upper(),Xcsc.upper()
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX),
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXX"SamFw",
XXXXXXXXXXXXXXXXurl="https://samfw.com/firmware/{}/{}/".format(
XXXXXXXXXXXXXXXXXXXXmodel.upper(),Xcsc.upper()
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX),
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXX"SamFrew",
XXXXXXXXXXXXXXXXurl="https://samfrew.com/model/{}/region/{}/".format(
XXXXXXXXXXXXXXXXXXXXmodel.upper(),Xcsc.upper()
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX),
XXXXXXXX)

XXXXXXXXawaitXmessage.reply(m,Xreply_markup=buttons)


@decorator.register(cmds=["ofox",X"of"])
@disableable_dec("ofox")
asyncXdefXorangefox(message):
XXXXAPI_HOSTX=X"https://api.orangefox.download/v3/"
XXXXtry:
XXXXXXXXargsX=Xmessage.text.split()
XXXXXXXXcodenameX=Xargs[1].lower()
XXXXexceptXBaseException:
XXXXXXXXcodenameX=X""
XXXXtry:
XXXXXXXXbuild_typeX=Xargs[2].lower()
XXXXexceptXBaseException:
XXXXXXXXbuild_typeX=X""

XXXXifXbuild_typeX==X"":
XXXXXXXXbuild_typeX=X"stable"

XXXXifXcodenameX==X"devices"XorXcodenameX==X"":
XXXXXXXXreply_textX=X(
XXXXXXXXXXXXf"<b>OrangeFoxXRecoveryX<i>{build_type}</i>XisXcurrentlyXavaibleXfor:</b>"
XXXXXXXX)

XXXXXXXXasyncXwithXhttpx.AsyncClient(http2=True)XasXhttp:
XXXXXXXXXXXXdataX=XawaitXhttp.get(
XXXXXXXXXXXXXXXXAPI_HOSTX+Xf"devices/?release_type={build_type}&sort=device_name_asc"
XXXXXXXXXXXX)
XXXXXXXXXXXXdevicesX=Xjson.loads(data.text)
XXXXXXXXXXXXawaitXhttp.aclose()
XXXXXXXXtry:
XXXXXXXXXXXXforXdeviceXinXdevices["data"]:
XXXXXXXXXXXXXXXXreply_textX+=X(
XXXXXXXXXXXXXXXXXXXXf"\nX-X{device['full_name']}X(<code>{device['codename']}</code>)"
XXXXXXXXXXXXXXXX)
XXXXXXXXexceptXBaseException:
XXXXXXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXXXXXf"'<b>{build_type}</b>'XisXnotXaXtypeXofXbuildXavailable,XtheXtypesXareXjustX'<b>beta</b>'XorX'<b>stable</b>'."
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn

XXXXXXXXifXbuild_typeX==X"stable":
XXXXXXXXXXXXreply_textX+=X(
XXXXXXXXXXXXXXXX"\n\n"
XXXXXXXXXXXXXXXX+Xf"ToXgetXtheXlatestXStableXreleaseXuseX<code>/ofoxX(codename)</code>,XforXexample:X<code>/ofoxXraphael</code>"
XXXXXXXXXXXX)
XXXXXXXXelifXbuild_typeX==X"beta":
XXXXXXXXXXXXreply_textX+=X(
XXXXXXXXXXXXXXXX"\n\n"
XXXXXXXXXXXXXXXX+Xf"ToXgetXtheXlatestXBetaXreleaseXuseX<code>/ofoxX(codename)Xbeta</code>,XforXexample:X<code>/ofoxXraphaelXbeta</code>"
XXXXXXXXXXXX)
XXXXXXXXawaitXmessage.reply(reply_text)
XXXXXXXXreturn

XXXXasyncXwithXhttpx.AsyncClient(http2=True)XasXhttp:
XXXXXXXXdataX=XawaitXhttp.get(API_HOSTX+Xf"devices/get?codename={codename}")
XXXXXXXXdeviceX=Xjson.loads(data.text)
XXXXXXXXawaitXhttp.aclose()
XXXXifXdata.status_codeX==X404:
XXXXXXXXawaitXmessage.reply("DeviceXisXnotXfound!")
XXXXXXXXreturn

XXXXasyncXwithXhttpx.AsyncClient(http2=True)XasXhttp:
XXXXXXXXdataX=XawaitXhttp.get(
XXXXXXXXXXXXAPI_HOST
XXXXXXXXXXXX+Xf"releases/?codename={codename}&type={build_type}&sort=date_desc&limit=1"
XXXXXXXX)
XXXXXXXXifXdata.status_codeX==X404:
XXXXXXXXXXXXbtnX=X"Device'sXpage"
XXXXXXXXXXXXurlX=Xf"https://orangefox.download/device/{device['codename']}"
XXXXXXXXXXXXbuttonX=XInlineKeyboardMarkup().add(InlineKeyboardButton(text=btn,Xurl=url))
XXXXXXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXXXXXf"⚠️XThereXisXnoX'<b>{build_type}</b>'XreleasesXforX<b>{device['full_name']}</b>.",
XXXXXXXXXXXXXXXXreply_markup=button,
XXXXXXXXXXXXXXXXdisable_web_page_preview=True,
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn
XXXXXXXXfind_idX=Xjson.loads(data.text)
XXXXXXXXawaitXhttp.aclose()
XXXXXXXXforXbuildXinXfind_id["data"]:
XXXXXXXXXXXXfile_idX=Xbuild["_id"]

XXXXasyncXwithXhttpx.AsyncClient(http2=True)XasXhttp:
XXXXXXXXdataX=XawaitXhttp.get(API_HOSTX+Xf"releases/get?_id={file_id}")
XXXXXXXXreleaseX=Xjson.loads(data.text)
XXXXXXXXawaitXhttp.aclose()
XXXXifXdata.status_codeX==X404:
XXXXXXXXawaitXmessage.reply("ReleaseXisXnotXfound!")
XXXXXXXXreturn

XXXXreply_textX=Xf"<u><b>OrangeFoxXRecoveryX<i>{build_type}</i>Xrelease</b></u>\n"
XXXXreply_textX+=X("XX<b>Device:</b>X{fullname}X(<code>{codename}</code>)\n").format(
XXXXXXXXfullname=device["full_name"],Xcodename=device["codename"]
XXXX)
XXXXreply_textX+=X("XX<b>Version:</b>X{}\n").format(release["version"])
XXXXreply_textX+=X("XX<b>ReleaseXdate:</b>X{}\n").format(
XXXXXXXXtime.strftime("%d/%m/%Y",Xtime.localtime(release["date"]))
XXXX)

XXXXreply_textX+=X("XX<b>Maintainer:</b>X{name}\n").format(
XXXXXXXXname=device["maintainer"]["name"]
XXXX)
XXXXchangelogX=Xrelease["changelog"]
XXXXtry:
XXXXXXXXreply_textX+=X"XX<u><b>Changelog:</b></u>\n"
XXXXXXXXforXentry_numXinXrange(len(changelog)):
XXXXXXXXXXXXifXentry_numX==X10:
XXXXXXXXXXXXXXXXbreak
XXXXXXXXXXXXreply_textX+=Xf"XXXX-X{changelog[entry_num]}\n"
XXXXexceptXBaseException:
XXXXXXXXpass

XXXXbtnX=X"⬇️XDownload"
XXXXurlX=Xrelease["mirrors"]["DL"]
XXXXbuttonX=XInlineKeyboardMarkup().add(InlineKeyboardButton(text=btn,Xurl=url))
XXXXawaitXmessage.reply(reply_text,Xreply_markup=button,Xdisable_web_page_preview=True)
XXXXreturn


__mod_name__X=X"Android"

__help__X=X"""
ModuleXspeciallyXmadeXforXAndroidXusers.

<b>GSI</b>
-X/phh:XGetXtheXlatestXPHHXAOSPXGSIs.
-X/phhmagisk:XGetXtheXlatestXPHHXMagisk.

<b>DeviceXfirmware:</b>
-X/samcheckX(model)X(csc):XSamsungXonlyX-XshowsXtheXlatestXfirmwareXinfoXforXtheXgivenXdevice,XtakenXfromXsamsungXservers.
-X/samgetX(model)X(csc):XSimilarXtoXtheX<code>/samcheck</code>XcommandXbutXhavingXdownloadXbuttons.

<b>Misc</b>
-X/magisk:XGetXlatestXMagiskXreleases.
-X/twrpX(codename):XGetsXlatestXTWRPXforXtheXandroidXdeviceXusingXtheXcodename.
-X/ofoxX(codename):XGetsXlatestXOFRPXforXtheXandroidXdeviceXusingXtheXcodename.
-X/ofoxXdevices:XSendsXtheXlistXofXdevicesXwithXstableXreleasesXsupportedXbyXOFRP.
-X/modelsX(codename):XSearchXforXAndroidXdeviceXmodelsXusingXcodename.
-X/whatisX(codename):XFindXoutXwhichXsmartphoneXisXusingXtheXcodename.
"""
