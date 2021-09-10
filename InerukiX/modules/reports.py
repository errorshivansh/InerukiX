#XCopyrightX(C)X2018X-X2020XMrYacha.XAllXrightsXreserved.XSourceXcodeXavailableXunderXtheXAGPL.
#XCopyrightX(C)X2021Xerrorshivansh
#XCopyrightX(C)X2020XInukaXAsith

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

fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.mongoXimportXdb

fromX.utils.connectionsXimportXchat_connection
fromX.utils.disableXimportXdisableable_dec
fromX.utils.languageXimportXget_strings_dec
fromX.utils.user_detailsXimportXget_admins_rights,Xget_user_link,Xis_user_admin


@register(regexp="^@admin$")
@chat_connection(only_groups=True)
@get_strings_dec("reports")
asyncXdefXreport1_cmd(message,Xchat,Xstrings):
XXXX#XCheckingXwhetherXreportXisXdisabledXinXchat!
XXXXcheckX=XawaitXdb.disabled.find_one({"chat_id":Xchat["chat_id"]})
XXXXifXcheck:
XXXXXXXXifX"report"XinXcheck["cmds"]:
XXXXXXXXXXXXreturn
XXXXawaitXreport(message,Xchat,Xstrings)


@register(cmds="report")
@chat_connection(only_groups=True)
@disableable_dec("report")
@get_strings_dec("reports")
asyncXdefXreport2_cmd(message,Xchat,Xstrings):
XXXXawaitXreport(message,Xchat,Xstrings)


asyncXdefXreport(message,Xchat,Xstrings):
XXXXuserX=Xmessage.from_user.id

XXXXifX(awaitXis_user_admin(chat["chat_id"],Xuser))XisXTrue:
XXXXXXXXreturnXawaitXmessage.reply(strings["user_user_admin"])

XXXXifX"reply_to_message"XnotXinXmessage:
XXXXXXXXreturnXawaitXmessage.reply(strings["no_user_to_report"])

XXXXoffender_idX=Xmessage.reply_to_message.from_user.id
XXXXifX(awaitXis_user_admin(chat["chat_id"],Xoffender_id))XisXTrue:
XXXXXXXXreturnXawaitXmessage.reply(strings["report_admin"])

XXXXadminsX=XawaitXget_admins_rights(chat["chat_id"])

XXXXoffenderX=XawaitXget_user_link(offender_id)
XXXXtextX=Xstrings["reported_user"].format(user=offender)

XXXXtry:
XXXXXXXXifXmessage.text.split(None,X2)[1]:
XXXXXXXXXXXXreasonX=X"X".join(message.text.split(None,X2)[1:])
XXXXXXXXXXXXtextX+=Xstrings["reported_reason"].format(reason=reason)
XXXXexceptXIndexError:
XXXXXXXXpass

XXXXforXadminXinXadmins:
XXXXXXXXtextX+=XawaitXget_user_link(admin,Xcustom_name="​")

XXXXawaitXmessage.reply(text)


__mod_name__X=X"Reports"

__help__X=X"""
We'reXallXbusyXpeopleXwhoXdon'tXhaveXtimeXtoXmonitorXourXgroupsX24/7.XButXhowXdoXyouXreactXifXsomeoneXinXyourXgroupXisXspamming?

PresentingXreports;XifXsomeoneXinXyourXgroupXthinksXsomeoneXneedsXreporting,XtheyXnowXhaveXanXeasyXwayXtoXcallXallXadmins.

<b>AvailableXcommands:</b>
-X/reportX(?text):XReports
-X@admins:XSameXasXabove,XbutXnotXaXclickable

<b>TIP:</b>XYouXalwaysXcanXdisableXreportingXbyXdisablingXmodule
"""
