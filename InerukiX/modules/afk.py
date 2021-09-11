#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2021HitaloSama.
#Copyright(C)2019Aiogram.
#
#ThisfileispartofHitsuki(TelegramBot)
#
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

importhtml
importre

fromIneruki.decoratorimportregister
fromIneruki.services.mongoimportdb

from.utils.disableimportdisableable_dec
from.utils.languageimportget_strings_dec
from.utils.messageimportget_args_str
from.utils.user_detailsimportget_user,get_user_by_id,get_user_link


@register(cmds="afk")
@disableable_dec("afk")
@get_strings_dec("afk")
asyncdefafk(message,strings):
try:
arg=get_args_str(message)
except:
return
#dontsupportAFKasanonadmin
ifmessage.from_user.id==1087968824:
awaitmessage.reply(strings["afk_anon"])
return

ifnotarg:
reason="Noreason"
else:
reason=arg

user=awaitget_user_by_id(message.from_user.id)
user_afk=awaitdb.afk.find_one({"user":user["user_id"]})
ifuser_afk:
return

awaitdb.afk.insert_one({"user":user["user_id"],"reason":reason})
text=strings["is_afk"].format(
user=(awaitget_user_link(user["user_id"])),reason=html.escape(reason)
)
awaitmessage.reply(text)


@register(f="text",allow_edited=False)
@get_strings_dec("afk")
asyncdefcheck_afk(message,strings):
ifbool(message.reply_to_message):
ifmessage.reply_to_message.from_user.idin(1087968824,777000):
return
ifmessage.from_user.idin(1087968824,777000):
return
user_afk=awaitdb.afk.find_one({"user":message.from_user.id})
ifuser_afk:
afk_cmd=re.findall("^[!/]afk(.*)",message.text)
ifnotafk_cmd:
awaitmessage.reply(
strings["unafk"].format(
user=(awaitget_user_link(message.from_user.id))
)
)
awaitdb.afk.delete_one({"_id":user_afk["_id"]})

user=awaitget_user(message)
ifnotuser:
return

user_afk=awaitdb.afk.find_one({"user":user["user_id"]})
ifuser_afk:
awaitmessage.reply(
strings["is_afk"].format(
user=(awaitget_user_link(user["user_id"])),
reason=html.escape(user_afk["reason"]),
)
)
