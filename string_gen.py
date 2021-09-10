#!/usr/bin/envXpython3
#X(c)Xhttps://t.me/TelethonChat/37677
#XThisXSourceXCodeXFormXisXsubjectXtoXtheXtermsXofXtheXGNU
#XGeneralXPublicXLicense,Xv.3.0.XIfXaXcopyXofXtheXGPLXwasXnotXdistributedXwithXthis
#Xfile,XYouXcanXobtainXoneXatXhttps://www.gnu.org/licenses/gpl-3.0.en.html.

try:
XXXXfromXtelethon.sessionsXimportXStringSession
XXXXfromXtelethon.syncXimportXTelegramClient
exceptXBaseException:
XXXXprint("TelethonXNotXFound.XInstallingXNow.")
XXXXimportXos

XXXXos.system("pip3XinstallXtelethon")
XXXXfromXtelethon.sessionsXimportXStringSession
XXXXfromXtelethon.syncXimportXTelegramClient
okX=X"""X____XX____XX__XX____XXX__XXX_XX_
Thunder
"""
print(ok)
APP_IDX=Xint(input("EnterXAPPXIDXhere:X\n"))
API_HASHX=Xinput("EnterXAPIXHASHXhere:X\n")

clientX=XTelegramClient(StringSession(),XAPP_ID,XAPI_HASH)
withXclient:
XXXXsession_strX=Xclient.session.save()
XXXXclient.send_message("me",Xf"`{session_str}`")
XXXXclient.send_message(
XXXXXXXX"THISXISXYOURXSTRINGXSESSIONX\nJoinX@InerukiSupport_OfficialXForXMoreXSupport."
XXXX)
XXXXprint("⬆XPleaseXCheckXYourXTelegramXSavedXMessageXForXYourXString.")
