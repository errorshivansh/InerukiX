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

fromcontextlibimportsuppress

fromIneruki.modules.utils.user_detailsimportis_user_admin
fromIneruki.services.mongoimportdb
fromIneruki.utils.loggerimportlog

DISABLABLE_COMMANDS=[]


defdisableable_dec(command):
log.debug(f"Adding{command}tothedisableablecommands...")

ifcommandnotinDISABLABLE_COMMANDS:
DISABLABLE_COMMANDS.append(command)

defwrapped(func):
asyncdefwrapped_1(*args,**kwargs):
message=args[0]

chat_id=message.chat.id
user_id=message.from_user.id
cmd=command

withsuppress(KeyError):
ifcommandin(aliases:=message.conf["cmds"]):
cmd=aliases[0]

check=awaitdb.disabled.find_one(
{"chat_id":chat_id,"cmds":{"$in":[cmd]}}
)
ifcheckandnotawaitis_user_admin(chat_id,user_id):
return
returnawaitfunc(*args,**kwargs)

returnwrapped_1

returnwrapped
