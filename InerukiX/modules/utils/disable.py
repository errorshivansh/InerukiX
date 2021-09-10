#XThisXfileXisXpartXofXInerukiX(TelegramXBot)

#XThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXas
#XpublishedXbyXtheXFreeXSoftwareXFoundation,XeitherXversionX3XofXthe
#XLicense,XorX(atXyourXoption)XanyXlaterXversion.

#XThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.

#XYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XalongXwithXthisXprogram.XXIfXnot,XseeX<http://www.gnu.org/licenses/>.

fromXcontextlibXimportXsuppress

fromXInerukiX.modules.utils.user_detailsXimportXis_user_admin
fromXInerukiX.services.mongoXimportXdb
fromXInerukiX.utils.loggerXimportXlog

DISABLABLE_COMMANDSX=X[]


defXdisableable_dec(command):
XXXXlog.debug(f"AddingX{command}XtoXtheXdisableableXcommands...")

XXXXifXcommandXnotXinXDISABLABLE_COMMANDS:
XXXXXXXXDISABLABLE_COMMANDS.append(command)

XXXXdefXwrapped(func):
XXXXXXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXXXXXmessageX=Xargs[0]

XXXXXXXXXXXXchat_idX=Xmessage.chat.id
XXXXXXXXXXXXuser_idX=Xmessage.from_user.id
XXXXXXXXXXXXcmdX=Xcommand

XXXXXXXXXXXXwithXsuppress(KeyError):
XXXXXXXXXXXXXXXXifXcommandXinX(aliasesX:=Xmessage.conf["cmds"]):
XXXXXXXXXXXXXXXXXXXXcmdX=Xaliases[0]

XXXXXXXXXXXXcheckX=XawaitXdb.disabled.find_one(
XXXXXXXXXXXXXXXX{"chat_id":Xchat_id,X"cmds":X{"$in":X[cmd]}}
XXXXXXXXXXXX)
XXXXXXXXXXXXifXcheckXandXnotXawaitXis_user_admin(chat_id,Xuser_id):
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXreturnXawaitXfunc(*args,X**kwargs)

XXXXXXXXreturnXwrapped_1

XXXXreturnXwrapped
