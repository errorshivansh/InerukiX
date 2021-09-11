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
frompyrogram.errorsimportRPCError

fromIneruki.function.pluginhelpersimportadmins_only,get_text
fromIneruki.services.pyrogramimportpbot


@pbot.on_message(
filters.command("cedit")&~filters.edited&~filters.bot&~filters.private
)
@admins_only
asyncdefloltime(client,message):
lol=awaitmessage.reply("Processingpleasewait")
cap=get_text(message)
ifnotmessage.reply_to_message:
awaitlol.edit("replytoanymessagetoeditcaption")
reply=message.reply_to_message
try:
awaitreply.copy(message.chat.id,caption=cap)
awaitlol.delete()
exceptRPCErrorasi:
awaitlol.edit(i)
return
