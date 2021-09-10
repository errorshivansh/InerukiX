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

fromXasyncioXimportXsleep
fromXdatetimeXimportXdatetime

importXaiohttp
fromXpyrogramXimportXfilters
fromXpyrogram.errorsXimportXPeerIdInvalid

fromXInerukiX.services.pyrogramXimportXpbot


classXAioHttp:
XXXX@staticmethod
XXXXasyncXdefXget_json(link):
XXXXXXXXasyncXwithXaiohttp.ClientSession()XasXsession:
XXXXXXXXXXXXasyncXwithXsession.get(link)XasXresp:
XXXXXXXXXXXXXXXXreturnXawaitXresp.json()

XXXX@staticmethod
XXXXasyncXdefXget_text(link):
XXXXXXXXasyncXwithXaiohttp.ClientSession()XasXsession:
XXXXXXXXXXXXasyncXwithXsession.get(link)XasXresp:
XXXXXXXXXXXXXXXXreturnXawaitXresp.text()

XXXX@staticmethod
XXXXasyncXdefXget_raw(link):
XXXXXXXXasyncXwithXaiohttp.ClientSession()XasXsession:
XXXXXXXXXXXXasyncXwithXsession.get(link)XasXresp:
XXXXXXXXXXXXXXXXreturnXawaitXresp.read()


@pbot.on_message(filters.command("spwinfo")X&X~filters.editedX&X~filters.bot)
asyncXdefXlookup(client,Xmessage):
XXXXcmdX=Xmessage.command
XXXXifXnotXmessage.reply_to_messageXandXlen(cmd)X==X1:
XXXXXXXXget_userX=Xmessage.from_user.id
XXXXelifXlen(cmd)X==X1:
XXXXXXXXifXmessage.reply_to_message.forward_from:
XXXXXXXXXXXXget_userX=Xmessage.reply_to_message.forward_from.id
XXXXXXXXelse:
XXXXXXXXXXXXget_userX=Xmessage.reply_to_message.from_user.id
XXXXelifXlen(cmd)X>X1:
XXXXXXXXget_userX=Xcmd[1]
XXXXXXXXtry:
XXXXXXXXXXXXget_userX=Xint(cmd[1])
XXXXXXXXexceptXValueError:
XXXXXXXXXXXXpass
XXXXtry:
XXXXXXXXuserX=XawaitXclient.get_chat(get_user)
XXXXexceptXPeerIdInvalid:
XXXXXXXXawaitXmessage.reply_text("IXdon'tXknowXthatXUser.")
XXXXXXXXsleep(2)
XXXXXXXXreturn
XXXXurlX=Xf"https://api.intellivoid.net/spamprotection/v1/lookup?query={user.id}"
XXXXaX=XawaitXAioHttp().get_json(url)
XXXXresponseX=Xa["success"]
XXXXifXresponseXisXTrue:
XXXXXXXXdateX=Xa["results"]["last_updated"]
XXXXXXXXstatsX=Xf"**◢XIntellivoid•XSpamProtectionXInfo**:\n"
XXXXXXXXstatsX+=Xf'X•X**UpdatedXon**:X`{datetime.fromtimestamp(date).strftime("%Y-%m-%dX%I:%M:%SX%p")}`\n'
XXXXXXXXstatsX+=X(
XXXXXXXXXXXXf"X•X**ChatXInfo**:X[Link](t.me/SpamProtectionBot/?start=00_{user.id})\n"
XXXXXXXX)

XXXXXXXXifXa["results"]["attributes"]["is_potential_spammer"]XisXTrue:
XXXXXXXXXXXXstatsX+=Xf"X•X**User**:X`USERxSPAM`\n"
XXXXXXXXelifXa["results"]["attributes"]["is_operator"]XisXTrue:
XXXXXXXXXXXXstatsX+=Xf"X•X**User**:X`USERxOPERATOR`\n"
XXXXXXXXelifXa["results"]["attributes"]["is_agent"]XisXTrue:
XXXXXXXXXXXXstatsX+=Xf"X•X**User**:X`USERxAGENT`\n"
XXXXXXXXelifXa["results"]["attributes"]["is_whitelisted"]XisXTrue:
XXXXXXXXXXXXstatsX+=Xf"X•X**User**:X`USERxWHITELISTED`\n"

XXXXXXXXstatsX+=Xf'X•X**Type**:X`{a["results"]["entity_type"]}`\n'
XXXXXXXXstatsX+=X(
XXXXXXXXXXXXf'X•X**Language**:X`{a["results"]["language_prediction"]["language"]}`\n'
XXXXXXXX)
XXXXXXXXstatsX+=Xf'X•X**LanguageXProbability**:X`{a["results"]["language_prediction"]["probability"]}`\n'
XXXXXXXXstatsX+=Xf"**SpamXPrediction**:\n"
XXXXXXXXstatsX+=Xf'X•X**HamXPrediction**:X`{a["results"]["spam_prediction"]["ham_prediction"]}`\n'
XXXXXXXXstatsX+=Xf'X•X**SpamXPrediction**:X`{a["results"]["spam_prediction"]["spam_prediction"]}`\n'
XXXXXXXXstatsX+=Xf'**Blacklisted**:X`{a["results"]["attributes"]["is_blacklisted"]}`\n'
XXXXXXXXifXa["results"]["attributes"]["is_blacklisted"]XisXTrue:
XXXXXXXXXXXXstatsX+=X(
XXXXXXXXXXXXXXXXf'X•X**Reason**:X`{a["results"]["attributes"]["blacklist_reason"]}`\n'
XXXXXXXXXXXX)
XXXXXXXXXXXXstatsX+=Xf'X•X**Flag**:X`{a["results"]["attributes"]["blacklist_flag"]}`\n'
XXXXXXXXstatsX+=Xf'**PTID**:\n`{a["results"]["private_telegram_id"]}`\n'
XXXXXXXXawaitXmessage.reply_text(stats,Xdisable_web_page_preview=True)
XXXXelse:
XXXXXXXXawaitXmessage.reply_text("`CannotXreachXSpamProtectionXAPI`")
XXXXXXXXawaitXsleep(3)
