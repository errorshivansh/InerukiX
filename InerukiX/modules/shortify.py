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

importjson

importaiohttp
frompyrogramimportfilters

fromIneruki.function.pluginhelpersimportadmins_only,get_text
fromIneruki.services.pyrogramimportpbot


#Usedmyapikeyhere,don'tfuckwithit
@pbot.on_message(
filters.command("short")&~filters.edited&~filters.bot&~filters.private
)
@admins_only
asyncdefshortify(client,message):
lel=awaitclient.send_message(message.chat.id,"`Waitasec....`")
url=get_text(message)
if"."notinurl:
awaitlel.edit("Defuq!.Isitaurl?")
return
header={
"Authorization":"Bearerad39983fa42d0b19e4534f33671629a4940298dc",
"Content-Type":"application/json",
}
payload={"long_url":f"{url}"}
payload=json.dumps(payload)
asyncwithaiohttp.ClientSession()assession:
asyncwithsession.post(
"https://api-ssl.bitly.com/v4/shorten",headers=header,data=payload
)asresp:
data=awaitresp.json()
msg=f"**OriginalUrl:**{url}\n**ShortenedUrl:**{data['link']}"
awaitlel.edit(msg)
