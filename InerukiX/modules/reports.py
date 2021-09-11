#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2021errorshivansh
#Copyright(C)2020InukaAsith

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

fromIneruki.decoratorimportregister
fromIneruki.services.mongoimportdb

from.utils.connectionsimportchat_connection
from.utils.disableimportdisableable_dec
from.utils.languageimportget_strings_dec
from.utils.user_detailsimportget_admins_rights,get_user_link,is_user_admin


@register(regexp="^@admin$")
@chat_connection(only_groups=True)
@get_strings_dec("reports")
asyncdefreport1_cmd(message,chat,strings):
#Checkingwhetherreportisdisabledinchat!
check=awaitdb.disabled.find_one({"chat_id":chat["chat_id"]})
ifcheck:
if"report"incheck["cmds"]:
return
awaitreport(message,chat,strings)


@register(cmds="report")
@chat_connection(only_groups=True)
@disableable_dec("report")
@get_strings_dec("reports")
asyncdefreport2_cmd(message,chat,strings):
awaitreport(message,chat,strings)


asyncdefreport(message,chat,strings):
user=message.from_user.id

if(awaitis_user_admin(chat["chat_id"],user))isTrue:
returnawaitmessage.reply(strings["user_user_admin"])

if"reply_to_message"notinmessage:
returnawaitmessage.reply(strings["no_user_to_report"])

offender_id=message.reply_to_message.from_user.id
if(awaitis_user_admin(chat["chat_id"],offender_id))isTrue:
returnawaitmessage.reply(strings["report_admin"])

admins=awaitget_admins_rights(chat["chat_id"])

offender=awaitget_user_link(offender_id)
text=strings["reported_user"].format(user=offender)

try:
ifmessage.text.split(None,2)[1]:
reason="".join(message.text.split(None,2)[1:])
text+=strings["reported_reason"].format(reason=reason)
exceptIndexError:
pass

foradmininadmins:
text+=awaitget_user_link(admin,custom_name="​")

awaitmessage.reply(text)


__mod_name__="Reports"

__help__="""
We'reallbusypeoplewhodon'thavetimetomonitorourgroups24/7.Buthowdoyoureactifsomeoneinyourgroupisspamming?

Presentingreports;ifsomeoneinyourgroupthinkssomeoneneedsreporting,theynowhaveaneasywaytocallalladmins.

<b>Availablecommands:</b>
-/report(?text):Reports
-@admins:Sameasabove,butnotaclickable

<b>TIP:</b>Youalwayscandisablereportingbydisablingmodule
"""
