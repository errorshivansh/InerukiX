#Copyright(C)2021TheHamkerCat
#Editedbyerrorshivansh

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

frompyrogramimportfilters

fromIneruki.function.pluginhelpersimportfetch,json_prettify
fromIneruki.services.pyrogramimportpbotasapp


@app.on_message(filters.command("covid")&~filters.edited)
asyncdefcovid(_,message):
iflen(message.command)==1:
data=awaitfetch("https://corona.lmao.ninja/v2/all")
data=awaitjson_prettify(data)
awaitapp.send_message(message.chat.id,text=data)
return
iflen(message.command)!=1:
country=message.text.split(None,1)[1].strip()
country=country.replace("","")
data=awaitfetch(f"https://corona.lmao.ninja/v2/countries/{country}")
data=awaitjson_prettify(data)
awaitapp.send_message(message.chat.id,text=data)
return
