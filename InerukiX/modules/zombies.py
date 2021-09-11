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

fromasyncioimportsleep

fromtelethonimportevents
fromtelethon.errorsimportChatAdminRequiredError,UserAdminInvalidError
fromtelethon.tl.functions.channelsimportEditBannedRequest
fromtelethon.tl.typesimportChatBannedRights

fromInerukiimportOWNER_ID
fromIneruki.services.telethonimporttbotasclient

#===================CONSTANT===================

BANNED_RIGHTS=ChatBannedRights(
until_date=None,
view_messages=True,
send_messages=True,
send_media=True,
send_stickers=True,
send_gifs=True,
send_games=True,
send_inline=True,
embed_links=True,
)


UNBAN_RIGHTS=ChatBannedRights(
until_date=None,
send_messages=None,
send_media=None,
send_stickers=None,
send_gifs=None,
send_games=None,
send_inline=None,
embed_links=None,
)

OFFICERS=OWNER_ID

#Checkifuserhasadminrights
asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):

returnisinstance(
(
awaittbot(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerChat):

ui=awaittbot.get_peer_id(user)
ps=(
awaittbot(functions.messages.GetFullChatRequest(chat.chat_id))
).full_chat.participants.participants
returnisinstance(
next((pforpinpsifp.user_id==ui),None),
(types.ChatParticipantAdmin,types.ChatParticipantCreator),
)
returnNone


@client.on(events.NewMessage(pattern=f"^[!/]zombies?(.*)"))
asyncdefzombies(event):
"""For.zombiescommand,listallthezombiesinachat."""
ifevent.fwd_from:
return
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
else:
return
con=event.pattern_match.group(1).lower()
del_u=0
del_status="NoDeletedAccountsFound,GroupIsClean."

ifcon!="clean":
find_zombies=awaitevent.respond("SearchingForZombies...")
asyncforuserinevent.client.iter_participants(event.chat_id):

ifuser.deleted:
del_u+=1
awaitsleep(1)
ifdel_u>0:
del_status=f"Found**{del_u}**ZombiesInThisGroup.\
\nCleanThemByUsing-`/zombiesclean`"
awaitfind_zombies.edit(del_status)
return

#Herelayingthesanitycheck
chat=awaitevent.get_chat()
chat.admin_rights
chat.creator

#Well

cleaning_zombies=awaitevent.respond("CleaningZombies...")
del_u=0
del_a=0

asyncforuserinevent.client.iter_participants(event.chat_id):
ifuser.deleted:
try:
awaitevent.client(
EditBannedRequest(event.chat_id,user.id,BANNED_RIGHTS)
)
exceptChatAdminRequiredError:
awaitcleaning_zombies.edit("IDon'tHaveBanRightsInThisGroup.")
return
exceptUserAdminInvalidError:
del_u-=1
del_a+=1
awaitevent.client(EditBannedRequest(event.chat_id,user.id,UNBAN_RIGHTS))
del_u+=1

ifdel_u>0:
del_status=f"Cleaned`{del_u}`Zombies"

ifdel_a>0:
del_status=f"Cleaned`{del_u}`Zombies\
\n`{del_a}`ZombieAdminAccountsAreNotRemoved!"

awaitcleaning_zombies.edit(del_status)
