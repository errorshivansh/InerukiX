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

importasyncio

frompyrogramimportfilters
frompyrogram.errorsimportRPCError

fromInerukiimportBOT_ID
fromIneruki.db.mongo_helpers.lockurlimportadd_chat,get_session,remove_chat
fromIneruki.function.pluginhelpersimport(
admins_only,
edit_or_reply,
get_url,
member_permissions,
)
fromIneruki.services.pyrogramimportpbot


@pbot.on_message(
filters.command("urllock")&~filters.edited&~filters.bot&~filters.private
)
@admins_only
asyncdefhmm(_,message):
globalIneruki_chats
try:
user_id=message.from_user.id
except:
return
ifnot"can_change_info"in(awaitmember_permissions(message.chat.id,user_id)):
awaitmessage.reply_text("**Youdon'thaveenoughpermissions**")
return
iflen(message.command)!=2:
awaitmessage.reply_text(
"Ionlyrecognize`/urllockon`and/urllock`offonly`"
)
return
status=message.text.split(None,1)[1]
message.chat.id
ifstatus=="ON"orstatus=="on"orstatus=="On":
lel=awaitedit_or_reply(message,"`Processing...`")
lol=add_chat(int(message.chat.id))
ifnotlol:
awaitlel.edit("URLBlockAlreadyActivatedInThisChat")
return
awaitlel.edit(
f"URLBlockSuccessfullyAddedForUsersInTheChat{message.chat.id}"
)

elifstatus=="OFF"orstatus=="off"orstatus=="Off":
lel=awaitedit_or_reply(message,"`Processing...`")
Escobar=remove_chat(int(message.chat.id))
ifnotEscobar:
awaitlel.edit("URLBlockWasNotActivatedInThisChat")
return
awaitlel.edit(
f"URLBlockSuccessfullyDeactivatedForUsersInTheChat{message.chat.id}"
)
else:
awaitmessage.reply_text(
"Ionlyrecognize`/urllockon`and/urllock`offonly`"
)


@pbot.on_message(
filters.incoming&filters.text&~filters.private&~filters.channel&~filters.bot
)
asyncdefhi(client,message):
ifnotget_session(int(message.chat.id)):
message.continue_propagation()
try:
user_id=message.from_user.id
except:
return
try:
ifnotlen(awaitmember_permissions(message.chat.id,user_id))<1:
message.continue_propagation()
iflen(awaitmember_permissions(message.chat.id,BOT_ID))<1:
message.continue_propagation()
ifnot"can_delete_messages"in(
awaitmember_permissions(message.chat.id,BOT_ID)
):
message.continue_propagation()
exceptRPCError:
return
try:

lel=get_url(message)
except:
return

iflel:
try:
awaitmessage.delete()
sender=message.from_user.mention()
lol=awaitclient.send_message(
message.chat.id,
f"{sender},Yourmessagewasdeletedasitcontainalink(s).\n❗️Linksarenotallowedhere",
)
awaitasyncio.sleep(10)
awaitlol.delete()
except:
message.continue_propagation()
else:
message.continue_propagation()
