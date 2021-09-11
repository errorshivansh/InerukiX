#Copyright(C)@chsaiujwal2020-2021
#Editedbyerrorshivansh
#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseaspublishedby
#theFreeSoftwareFoundation,eitherversion3oftheLicense,or
#
#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.
#
#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<https://www.gnu.org/licenses/>.


importurllib.request

frombs4importBeautifulSoup
fromtelethonimportevents
fromtelethon.tlimportfunctions,types

fromIneruki.services.telethonimporttbot


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


@tbot.on(events.NewMessage(pattern="/cs$"))
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
else:
return
score_page="http://static.cricinfo.com/rss/livescores.xml"
page=urllib.request.urlopen(score_page)
soup=BeautifulSoup(page,"html.parser")
result=soup.find_all("description")
Sed=""
formatchinresult:
Sed+=match.get_text()+"\n\n"
awaitevent.reply(
f"<b><u>Matchinformationgatheredsuccessful</b></u>\n\n\n<code>{Sed}</code>",
parse_mode="HTML",
)
