#!/usr/bin/envpython3
#(c)https://t.me/TelethonChat/37677
#ThisSourceCodeFormissubjecttothetermsoftheGNU
#GeneralPublicLicense,v.3.0.IfacopyoftheGPLwasnotdistributedwiththis
#file,Youcanobtainoneathttps://www.gnu.org/licenses/gpl-3.0.en.html.

try:
fromtelethon.sessionsimportStringSession
fromtelethon.syncimportTelegramClient
exceptBaseException:
print("TelethonNotFound.InstallingNow.")
importos

os.system("pip3installtelethon")
fromtelethon.sessionsimportStringSession
fromtelethon.syncimportTelegramClient
ok="""__________________
Thunder
"""
print(ok)
APP_ID=int(input("EnterAPPIDhere:\n"))
API_HASH=input("EnterAPIHASHhere:\n")

client=TelegramClient(StringSession(),APP_ID,API_HASH)
withclient:
session_str=client.session.save()
client.send_message("me",f"`{session_str}`")
client.send_message(
"THISISYOURSTRINGSESSION\nJoin@InerukiSupport_OfficialForMoreSupport."
)
print("⬆PleaseCheckYourTelegramSavedMessageForYourString.")
