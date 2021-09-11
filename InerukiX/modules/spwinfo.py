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
fromdatetimeimportdatetime

importaiohttp
frompyrogramimportfilters
frompyrogram.errorsimportPeerIdInvalid

fromIneruki.services.pyrogramimportpbot


classAioHttp:
@staticmethod
asyncdefget_json(link):
asyncwithaiohttp.ClientSession()assession:
asyncwithsession.get(link)asresp:
returnawaitresp.json()

@staticmethod
asyncdefget_text(link):
asyncwithaiohttp.ClientSession()assession:
asyncwithsession.get(link)asresp:
returnawaitresp.text()

@staticmethod
asyncdefget_raw(link):
asyncwithaiohttp.ClientSession()assession:
asyncwithsession.get(link)asresp:
returnawaitresp.read()


@pbot.on_message(filters.command("spwinfo")&~filters.edited&~filters.bot)
asyncdeflookup(client,message):
cmd=message.command
ifnotmessage.reply_to_messageandlen(cmd)==1:
get_user=message.from_user.id
eliflen(cmd)==1:
ifmessage.reply_to_message.forward_from:
get_user=message.reply_to_message.forward_from.id
else:
get_user=message.reply_to_message.from_user.id
eliflen(cmd)>1:
get_user=cmd[1]
try:
get_user=int(cmd[1])
exceptValueError:
pass
try:
user=awaitclient.get_chat(get_user)
exceptPeerIdInvalid:
awaitmessage.reply_text("Idon'tknowthatUser.")
sleep(2)
return
url=f"https://api.intellivoid.net/spamprotection/v1/lookup?query={user.id}"
a=awaitAioHttp().get_json(url)
response=a["success"]
ifresponseisTrue:
date=a["results"]["last_updated"]
stats=f"**◢Intellivoid•SpamProtectionInfo**:\n"
stats+=f'•**Updatedon**:`{datetime.fromtimestamp(date).strftime("%Y-%m-%d%I:%M:%S%p")}`\n'
stats+=(
f"•**ChatInfo**:[Link](t.me/SpamProtectionBot/?start=00_{user.id})\n"
)

ifa["results"]["attributes"]["is_potential_spammer"]isTrue:
stats+=f"•**User**:`USERxSPAM`\n"
elifa["results"]["attributes"]["is_operator"]isTrue:
stats+=f"•**User**:`USERxOPERATOR`\n"
elifa["results"]["attributes"]["is_agent"]isTrue:
stats+=f"•**User**:`USERxAGENT`\n"
elifa["results"]["attributes"]["is_whitelisted"]isTrue:
stats+=f"•**User**:`USERxWHITELISTED`\n"

stats+=f'•**Type**:`{a["results"]["entity_type"]}`\n'
stats+=(
f'•**Language**:`{a["results"]["language_prediction"]["language"]}`\n'
)
stats+=f'•**LanguageProbability**:`{a["results"]["language_prediction"]["probability"]}`\n'
stats+=f"**SpamPrediction**:\n"
stats+=f'•**HamPrediction**:`{a["results"]["spam_prediction"]["ham_prediction"]}`\n'
stats+=f'•**SpamPrediction**:`{a["results"]["spam_prediction"]["spam_prediction"]}`\n'
stats+=f'**Blacklisted**:`{a["results"]["attributes"]["is_blacklisted"]}`\n'
ifa["results"]["attributes"]["is_blacklisted"]isTrue:
stats+=(
f'•**Reason**:`{a["results"]["attributes"]["blacklist_reason"]}`\n'
)
stats+=f'•**Flag**:`{a["results"]["attributes"]["blacklist_flag"]}`\n'
stats+=f'**PTID**:\n`{a["results"]["private_telegram_id"]}`\n'
awaitmessage.reply_text(stats,disable_web_page_preview=True)
else:
awaitmessage.reply_text("`CannotreachSpamProtectionAPI`")
awaitsleep(3)
