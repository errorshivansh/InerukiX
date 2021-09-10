#XCopyrightX(C)X2021Xerrorshivansh


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

fromXpyrogramXimportXfilters

fromXInerukiX.function.pluginhelpersXimportXadmins_only
fromXInerukiX.services.pyrogramXimportXpbot

__HELP__X=X"""
ClassicXfiltersXareXjustXlikeXmarie'sXfilterXsystem.XIfXyouXstillXlikeXthatXkindXofXfilterXsystem
**AdminXOnly**
X-X/cfilterX<word>X<message>:XEveryXtimeXsomeoneXsaysX"word",XtheXbotXwillXreplyXwithX"message"
YouXcanXalsoXincludeXbuttonsXinXfilters,XexampleXsendX`/savefilterXgoogle`XinXreplyXtoX`ClickXHereXToXOpenXGoogleX|X[Button.url('Google',X'google.com')]`
X-X/stopcfilterX<word>:XStopXthatXfilter.
X-X/stopallcfilters:XDeleteXallXfiltersXinXtheXcurrentXchat.
**Admin+Non-Admin**
X-X/cfilters:XListXallXactiveXfiltersXinXtheXchat
X
X**PleaseXnoteXclassicXfiltersXcanXbeXunstable.XWeXrecommendXyouXtoXuseX/addfilter**
"""


@pbot.on_message(
XXXXfilters.command("invitelink")X&X~filters.editedX&X~filters.botX&X~filters.private
)
@admins_only
asyncXdefXinvitelink(client,Xmessage):
XXXXchidX=Xmessage.chat.id
XXXXtry:
XXXXXXXXinvitelinkX=XawaitXclient.export_chat_invite_link(chid)
XXXXexcept:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"AddXmeXasXadminXofXyorXgroupXfirst",
XXXXXXXX)
XXXXXXXXreturn
XXXXawaitXmessage.reply_text(f"InviteXlinkXgeneratedXsuccessfullyX\n\nX{invitelink}")


@pbot.on_message(filters.command("cfilterhelp")X&X~filters.privateX&X~filters.edited)
@admins_only
asyncXdefXfiltersghelp(client,Xmessage):
XXXXawaitXclient.send_message(message.chat.id,Xtext=__HELP__)
