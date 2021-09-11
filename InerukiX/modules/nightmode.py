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


fromapscheduler.schedulers.asyncioimportAsyncIOScheduler
fromtelethonimportevents,functions
fromtelethon.tl.typesimportChatBannedRights

fromInerukiimportBOT_ID
fromIneruki.function.telethonbasicsimportis_admin
fromIneruki.services.sql.night_mode_sqlimport(
add_nightmode,
get_all_chat_id,
is_nightmode_indb,
rmnightmode,
)
fromIneruki.services.telethonimporttbot

CLEAN_GROUPS=False
hehes=ChatBannedRights(
until_date=None,
send_messages=True,
send_media=True,
send_stickers=True,
send_gifs=True,
send_games=True,
send_inline=True,
send_polls=True,
invite_users=True,
pin_messages=True,
change_info=True,
)
openhehe=ChatBannedRights(
until_date=None,
send_messages=False,
send_media=False,
send_stickers=False,
send_gifs=False,
send_games=False,
send_inline=False,
send_polls=False,
invite_users=True,
pin_messages=True,
change_info=True,
)


@tbot.on(events.NewMessage(pattern="/nightmode(.*)"))
asyncdefclose_ws(event):

ifnotevent.is_group:
awaitevent.reply("YouCanOnlyNsfwWatchinGroups.")
return
input_str=event.pattern_match.group(1)
ifnotawaitis_admin(event,BOT_ID):
awaitevent.reply("`IShouldBeAdminToDoThis!`")
return
ifawaitis_admin(event,event.message.sender_id):
if(
input_str=="on"
orinput_str=="On"
orinput_str=="ON"
orinput_str=="enable"
):
ifis_nightmode_indb(str(event.chat_id)):
awaitevent.reply("ThisChatisHasAlreadyEnabledNightMode.")
return
add_nightmode(str(event.chat_id))
awaitevent.reply(
f"**AddedChat{event.chat.title}WithId{event.chat_id}ToDatabase.ThisGroupWillBeClosedOn12Am(IST)AndWillOpenedOn06Am(IST)**"
)
elif(
input_str=="off"
orinput_str=="Off"
orinput_str=="OFF"
orinput_str=="disable"
):

ifnotis_nightmode_indb(str(event.chat_id)):
awaitevent.reply("ThisChatisHasNotEnabledNightMode.")
return
rmnightmode(str(event.chat_id))
awaitevent.reply(
f"**RemovedChat{event.chat.title}WithId{event.chat_id}FromDatabase.ThisGroupWillBeNoLongerClosedOn12Am(IST)AndWillOpenedOn06Am(IST)**"
)
else:
awaitevent.reply("Iundestand`/nightmodeon`and`/nightmodeoff`only")
else:
awaitevent.reply("`YouShouldBeAdminToDoThis!`")
return


asyncdefjob_close():
ws_chats=get_all_chat_id()
iflen(ws_chats)==0:
return
forwarnerinws_chats:
try:
awaittbot.send_message(
int(warner.chat_id),
"`12:00Am,GroupIsClosingTill6Am.NightModeStarted!`\n**PoweredBy@Inerukibot**",
)
awaittbot(
functions.messages.EditChatDefaultBannedRightsRequest(
peer=int(warner.chat_id),banned_rights=hehes
)
)
ifCLEAN_GROUPS:
asyncforuserintbot.iter_participants(int(warner.chat_id)):
ifuser.deleted:
awaittbot.edit_permissions(
int(warner.chat_id),user.id,view_messages=False
)
exceptExceptionase:
print(f"UnableToCloseGroup{warner}-{e}")


scheduler=AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_close,trigger="cron",hour=23,minute=55)
scheduler.start()


asyncdefjob_open():
ws_chats=get_all_chat_id()
iflen(ws_chats)==0:
return
forwarnerinws_chats:
try:
awaittbot.send_message(
int(warner.chat_id),
"`06:00Am,GroupIsOpening.`\n**PoweredBy@InerukiBot**",
)
awaittbot(
functions.messages.EditChatDefaultBannedRightsRequest(
peer=int(warner.chat_id),banned_rights=openhehe
)
)
exceptExceptionase:
print(f"UnableToOpenGroup{warner.chat_id}-{e}")


#Runeverydayat06
scheduler=AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_open,trigger="cron",hour=6,minute=10)
scheduler.start()

__mod_name__="NightMode"

__help__="""
<b>TheNightmode</b>
Closeyourgroupat12.00a.m.andopenbackat6.00a.m.(IST)
<i>Onlyavailableforasiancountries(IndiaStandardtime)</i>

-/nightmode[ON/OFF]:Enable/DisableNightMode.

"""
