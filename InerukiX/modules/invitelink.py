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

fromIneruki.function.pluginhelpersimportadmins_only
fromIneruki.services.pyrogramimportpbot

__HELP__="""
Classicfiltersarejustlikemarie'sfiltersystem.Ifyoustilllikethatkindoffiltersystem
**AdminOnly**
-/cfilter<word><message>:Everytimesomeonesays"word",thebotwillreplywith"message"
Youcanalsoincludebuttonsinfilters,examplesend`/savefiltergoogle`inreplyto`ClickHereToOpenGoogle|[Button.url('Google','google.com')]`
-/stopcfilter<word>:Stopthatfilter.
-/stopallcfilters:Deleteallfiltersinthecurrentchat.
**Admin+Non-Admin**
-/cfilters:Listallactivefiltersinthechat

**Pleasenoteclassicfilterscanbeunstable.Werecommendyoutouse/addfilter**
"""


@pbot.on_message(
filters.command("invitelink")&~filters.edited&~filters.bot&~filters.private
)
@admins_only
asyncdefinvitelink(client,message):
chid=message.chat.id
try:
invitelink=awaitclient.export_chat_invite_link(chid)
except:
awaitmessage.reply_text(
"Addmeasadminofyorgroupfirst",
)
return
awaitmessage.reply_text(f"Invitelinkgeneratedsuccessfully\n\n{invitelink}")


@pbot.on_message(filters.command("cfilterhelp")&~filters.private&~filters.edited)
@admins_only
asyncdeffiltersghelp(client,message):
awaitclient.send_message(message.chat.id,text=__HELP__)
