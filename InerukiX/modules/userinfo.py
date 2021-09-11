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

fromdatetimeimportdatetime

frompyrogramimportfilters
frompyrogram.errorsimportPeerIdInvalid
frompyrogram.typesimportMessage,User

fromIneruki.services.pyrogramimportpbot


defReplyCheck(message:Message):
reply_id=None

ifmessage.reply_to_message:
reply_id=message.reply_to_message.message_id

elifnotmessage.from_user.is_self:
reply_id=message.message_id

returnreply_id


infotext=(
"**[{full_name}](tg://user?id={user_id})**\n"
"*UserID:`{user_id}`\n"
"*FirstName:`{first_name}`\n"
"*LastName:`{last_name}`\n"
"*Username:`{username}`\n"
"*LastOnline:`{last_online}`\n"
"*Bio:{bio}"
)


defLastOnline(user:User):
ifuser.is_bot:
return""
elifuser.status=="recently":
return"Recently"
elifuser.status=="within_week":
return"Withinthelastweek"
elifuser.status=="within_month":
return"Withinthelastmonth"
elifuser.status=="long_time_ago":
return"Alongtimeago:("
elifuser.status=="online":
return"CurrentlyOnline"
elifuser.status=="offline":
returndatetime.fromtimestamp(user.status.date).strftime(
"%a,%d%b%Y,%H:%M:%S"
)


defFullName(user:User):
returnuser.first_name+""+user.last_nameifuser.last_nameelseuser.first_name


@pbot.on_message(filters.command("whois")&~filters.edited&~filters.bot)
asyncdefwhois(client,message):
cmd=message.command
ifnotmessage.reply_to_messageandlen(cmd)==1:
get_user=message.from_user.id
eliflen(cmd)==1:
get_user=message.reply_to_message.from_user.id
eliflen(cmd)>1:
get_user=cmd[1]
try:
get_user=int(cmd[1])
exceptValueError:
pass
try:
user=awaitclient.get_users(get_user)
exceptPeerIdInvalid:
awaitmessage.reply("Idon'tknowthatUser.")
return
desc=awaitclient.get_chat(get_user)
desc=desc.description
awaitmessage.reply_text(
infotext.format(
full_name=FullName(user),
user_id=user.id,
user_dc=user.dc_id,
first_name=user.first_name,
last_name=user.last_nameifuser.last_nameelse"",
username=user.usernameifuser.usernameelse"",
last_online=LastOnline(user),
bio=descifdescelse"`Nobiosetup.`",
),
disable_web_page_preview=True,
)
