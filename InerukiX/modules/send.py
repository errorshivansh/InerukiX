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

frompyrogramimportfilters

fromIneruki.function.pluginhelpersimportadmins_only,get_text
fromIneruki.services.pyrogramimportpbot


@pbot.on_message(
filters.command("send")&~filters.edited&~filters.bot&~filters.private
)
@admins_only
asyncdefsend(client,message):
args=get_text(message)
awaitclient.send_message(message.chat.id,text=args)
