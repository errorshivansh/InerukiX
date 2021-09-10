#XCopyrightX(C)X2018X-X2020XMrYacha.XAllXrightsXreserved.XSourceXcodeXavailableXunderXtheXAGPL.
#XCopyrightX(C)X2021XHitaloSama.
#XCopyrightX(C)X2019XAiogram.
#
#XThisXfileXisXpartXofXHitsukiX(TelegramXBot)
#
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

importXhtml
importXre

fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.mongoXimportXdb

fromX.utils.disableXimportXdisableable_dec
fromX.utils.languageXimportXget_strings_dec
fromX.utils.messageXimportXget_args_str
fromX.utils.user_detailsXimportXget_user,Xget_user_by_id,Xget_user_link


@register(cmds="afk")
@disableable_dec("afk")
@get_strings_dec("afk")
asyncXdefXafk(message,Xstrings):
XXXXtry:
XXXXXXXXargX=Xget_args_str(message)
XXXXexcept:
XXXXXXXXreturn
XXXX#XdontXsupportXAFKXasXanonXadmin
XXXXifXmessage.from_user.idX==X1087968824:
XXXXXXXXawaitXmessage.reply(strings["afk_anon"])
XXXXXXXXreturn

XXXXifXnotXarg:
XXXXXXXXreasonX=X"NoXreason"
XXXXelse:
XXXXXXXXreasonX=Xarg

XXXXuserX=XawaitXget_user_by_id(message.from_user.id)
XXXXuser_afkX=XawaitXdb.afk.find_one({"user":Xuser["user_id"]})
XXXXifXuser_afk:
XXXXXXXXreturn

XXXXawaitXdb.afk.insert_one({"user":Xuser["user_id"],X"reason":Xreason})
XXXXtextX=Xstrings["is_afk"].format(
XXXXXXXXuser=(awaitXget_user_link(user["user_id"])),Xreason=html.escape(reason)
XXXX)
XXXXawaitXmessage.reply(text)


@register(f="text",Xallow_edited=False)
@get_strings_dec("afk")
asyncXdefXcheck_afk(message,Xstrings):
XXXXifXbool(message.reply_to_message):
XXXXXXXXifXmessage.reply_to_message.from_user.idXinX(1087968824,X777000):
XXXXXXXXXXXXreturn
XXXXifXmessage.from_user.idXinX(1087968824,X777000):
XXXXXXXXreturn
XXXXuser_afkX=XawaitXdb.afk.find_one({"user":Xmessage.from_user.id})
XXXXifXuser_afk:
XXXXXXXXafk_cmdX=Xre.findall("^[!/]afk(.*)",Xmessage.text)
XXXXXXXXifXnotXafk_cmd:
XXXXXXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXXXXXstrings["unafk"].format(
XXXXXXXXXXXXXXXXXXXXuser=(awaitXget_user_link(message.from_user.id))
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXdb.afk.delete_one({"_id":Xuser_afk["_id"]})

XXXXuserX=XawaitXget_user(message)
XXXXifXnotXuser:
XXXXXXXXreturn

XXXXuser_afkX=XawaitXdb.afk.find_one({"user":Xuser["user_id"]})
XXXXifXuser_afk:
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["is_afk"].format(
XXXXXXXXXXXXXXXXuser=(awaitXget_user_link(user["user_id"])),
XXXXXXXXXXXXXXXXreason=html.escape(user_afk["reason"]),
XXXXXXXXXXXX)
XXXXXXXX)
