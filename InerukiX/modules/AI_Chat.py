#XCopyrightX(C)X2021XRed-AuraX&XerrorshivanshX&XHamkerCat

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
importXre

importXemoji

urlX=X"https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
importXre

importXaiohttp

#XfromXgoogle_trans_newXimportXgoogle_translator
fromXgoogletransXimportXTranslatorXasXgoogle_translator
fromXpyrogramXimportXfilters

fromXInerukiXXimportXBOT_ID
fromXInerukiX.db.mongo_helpers.aichatXimportXadd_chat,Xget_session,Xremove_chat
fromXInerukiX.function.inlinehelperXimportXarq
fromXInerukiX.function.pluginhelpersXimportXadmins_only,Xedit_or_reply
fromXInerukiX.services.pyrogramXimportXpbotXasXInerukix

translatorX=Xgoogle_translator()


asyncXdefXlunaQuery(query:Xstr,Xuser_id:Xint):
XXXXlunaX=XawaitXarq.luna(query,Xuser_id)
XXXXreturnXluna.result


defXextract_emojis(s):
XXXXreturnX"".join(cXforXcXinXsXifXcXinXemoji.UNICODE_EMOJI)


asyncXdefXfetch(url):
XXXXtry:
XXXXXXXXasyncXwithXaiohttp.Timeout(10.0):
XXXXXXXXXXXXasyncXwithXaiohttp.ClientSession()XasXsession:
XXXXXXXXXXXXXXXXasyncXwithXsession.get(url)XasXresp:
XXXXXXXXXXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXXXXXXXXXdataX=XawaitXresp.json()
XXXXXXXXXXXXXXXXXXXXexcept:
XXXXXXXXXXXXXXXXXXXXXXXXdataX=XawaitXresp.text()
XXXXXXXXXXXXreturnXdata
XXXXexcept:
XXXXXXXXprint("AIXresponseXTimeout")
XXXXXXXXreturn


Ineruki_chatsX=X[]
en_chatsX=X[]
#XAIXChatX(C)X2020-2021XbyX@InukaAsith


@Inerukix.on_message(
XXXXfilters.command("chatbot")X&X~filters.editedX&X~filters.botX&X~filters.private
)
@admins_only
asyncXdefXhmm(_,Xmessage):
XXXXglobalXIneruki_chats
XXXXifXlen(message.command)X!=X2:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"IXonlyXrecognizeX`/chatbotXon`XandX/chatbotX`offXonly`"
XXXXXXXX)
XXXXXXXXmessage.continue_propagation()
XXXXstatusX=Xmessage.text.split(None,X1)[1]
XXXXchat_idX=Xmessage.chat.id
XXXXifXstatusX==X"ON"XorXstatusX==X"on"XorXstatusX==X"On":
XXXXXXXXlelX=XawaitXedit_or_reply(message,X"`Processing...`")
XXXXXXXXlolX=Xadd_chat(int(message.chat.id))
XXXXXXXXifXnotXlol:
XXXXXXXXXXXXawaitXlel.edit("InerukiXAIXAlreadyXActivatedXInXThisXChat")
XXXXXXXXXXXXreturn
XXXXXXXXawaitXlel.edit(
XXXXXXXXXXXXf"InerukiXAIXSuccessfullyXAddedXForXUsersXInXTheXChatX{message.chat.id}"
XXXXXXXX)

XXXXelifXstatusX==X"OFF"XorXstatusX==X"off"XorXstatusX==X"Off":
XXXXXXXXlelX=XawaitXedit_or_reply(message,X"`Processing...`")
XXXXXXXXEscobarX=Xremove_chat(int(message.chat.id))
XXXXXXXXifXnotXEscobar:
XXXXXXXXXXXXawaitXlel.edit("InerukiXAIXWasXNotXActivatedXInXThisXChat")
XXXXXXXXXXXXreturn
XXXXXXXXawaitXlel.edit(
XXXXXXXXXXXXf"InerukiXAIXSuccessfullyXDeactivatedXForXUsersXInXTheXChatX{message.chat.id}"
XXXXXXXX)

XXXXelifXstatusX==X"EN"XorXstatusX==X"en"XorXstatusX==X"english":
XXXXXXXXifXnotXchat_idXinXen_chats:
XXXXXXXXXXXXen_chats.append(chat_id)
XXXXXXXXXXXXawaitXmessage.reply_text("EnglishXAIXchatXEnabled!")
XXXXXXXXXXXXreturn
XXXXXXXXawaitXmessage.reply_text("AIXChatXIsXAlreadyXDisabled.")
XXXXXXXXmessage.continue_propagation()
XXXXelse:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"IXonlyXrecognizeX`/chatbotXon`XandX/chatbotX`offXonly`"
XXXXXXXX)


@Inerukix.on_message(
XXXXfilters.text
XXXX&Xfilters.reply
XXXX&X~filters.bot
XXXX&X~filters.edited
XXXX&X~filters.via_bot
XXXX&X~filters.forwarded,
XXXXgroup=2,
)
asyncXdefXhmm(client,Xmessage):
XXXXifXnotXget_session(int(message.chat.id)):
XXXXXXXXreturn
XXXXifXnotXmessage.reply_to_message:
XXXXXXXXreturn
XXXXtry:
XXXXXXXXsenderrX=Xmessage.reply_to_message.from_user.id
XXXXexcept:
XXXXXXXXreturn
XXXXifXsenderrX!=XBOT_ID:
XXXXXXXXreturn
XXXXmsgX=Xmessage.text
XXXXchat_idX=Xmessage.chat.id
XXXXifXmsg.startswith("/")XorXmsg.startswith("@"):
XXXXXXXXmessage.continue_propagation()
XXXXifXchat_idXinXen_chats:
XXXXXXXXtestX=Xmsg
XXXXXXXXtestX=Xtest.replace("Ineruki",X"Aco")
XXXXXXXXtestX=Xtest.replace("Ineruki",X"Aco")
XXXXXXXXresponseX=XawaitXlunaQuery(
XXXXXXXXXXXXtest,Xmessage.from_user.idXifXmessage.from_userXelseX0
XXXXXXXX)
XXXXXXXXresponseX=Xresponse.replace("Aco",X"Ineruki")
XXXXXXXXresponseX=Xresponse.replace("aco",X"Ineruki")

XXXXXXXXproX=Xresponse
XXXXXXXXtry:
XXXXXXXXXXXXawaitXInerukix.send_chat_action(message.chat.id,X"typing")
XXXXXXXXXXXXawaitXmessage.reply_text(pro)
XXXXXXXXexceptXCFError:
XXXXXXXXXXXXreturn

XXXXelse:
XXXXXXXXuX=Xmsg.split()
XXXXXXXXemjX=Xextract_emojis(msg)
XXXXXXXXmsgX=Xmsg.replace(emj,X"")
XXXXXXXXifX(
XXXXXXXXXXXX[(k)XforXkXinXuXifXk.startswith("@")]
XXXXXXXXXXXXandX[(k)XforXkXinXuXifXk.startswith("#")]
XXXXXXXXXXXXandX[(k)XforXkXinXuXifXk.startswith("/")]
XXXXXXXXXXXXandXre.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)",Xmsg)X!=X[]
XXXXXXXX):

XXXXXXXXXXXXhX=X"X".join(filter(lambdaXx:Xx[0]X!=X"@",Xu))
XXXXXXXXXXXXkmX=Xre.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)",Xr"",Xh)
XXXXXXXXXXXXtmX=Xkm.split()
XXXXXXXXXXXXjmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"#",Xtm))
XXXXXXXXXXXXhmX=Xjm.split()
XXXXXXXXXXXXrmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"/",Xhm))
XXXXXXXXelifX[(k)XforXkXinXuXifXk.startswith("@")]:

XXXXXXXXXXXXrmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"@",Xu))
XXXXXXXXelifX[(k)XforXkXinXuXifXk.startswith("#")]:
XXXXXXXXXXXXrmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"#",Xu))
XXXXXXXXelifX[(k)XforXkXinXuXifXk.startswith("/")]:
XXXXXXXXXXXXrmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"/",Xu))
XXXXXXXXelifXre.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)",Xmsg)X!=X[]:
XXXXXXXXXXXXrmX=Xre.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)",Xr"",Xmsg)
XXXXXXXXelse:
XXXXXXXXXXXXrmX=Xmsg
XXXXXXXXXXXX#XprintX(rm)
XXXXXXXXtry:
XXXXXXXXXXXXlanX=Xtranslator.detect(rm)
XXXXXXXXXXXXlanX=Xlan.lang
XXXXXXXXexcept:
XXXXXXXXXXXXreturn
XXXXXXXXtestX=Xrm
XXXXXXXXifXnotX"en"XinXlanXandXnotXlanX==X"":
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXtestX=Xtranslator.translate(test,Xdest="en")
XXXXXXXXXXXXXXXXtestX=Xtest.text
XXXXXXXXXXXXexcept:
XXXXXXXXXXXXXXXXreturn
XXXXXXXX#XtestX=Xemoji.demojize(test.strip())

XXXXXXXXtestX=Xtest.replace("Ineruki",X"Aco")
XXXXXXXXtestX=Xtest.replace("Ineruki",X"Aco")
XXXXXXXXresponseX=XawaitXlunaQuery(
XXXXXXXXXXXXtest,Xmessage.from_user.idXifXmessage.from_userXelseX0
XXXXXXXX)
XXXXXXXXresponseX=Xresponse.replace("Aco",X"Ineruki")
XXXXXXXXresponseX=Xresponse.replace("aco",X"Ineruki")
XXXXXXXXresponseX=Xresponse.replace("Luna",X"Ineruki")
XXXXXXXXresponseX=Xresponse.replace("luna",X"Ineruki")
XXXXXXXXproX=Xresponse
XXXXXXXXifXnotX"en"XinXlanXandXnotXlanX==X"":
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXproX=Xtranslator.translate(pro,Xdest=lan)
XXXXXXXXXXXXXXXXproX=Xpro.text
XXXXXXXXXXXXexcept:
XXXXXXXXXXXXXXXXreturn
XXXXXXXXtry:
XXXXXXXXXXXXawaitXInerukix.send_chat_action(message.chat.id,X"typing")
XXXXXXXXXXXXawaitXmessage.reply_text(pro)
XXXXXXXXexceptXCFError:
XXXXXXXXXXXXreturn


@Inerukix.on_message(
XXXXfilters.textX&Xfilters.privateX&X~filters.editedX&Xfilters.replyX&X~filters.bot
)
asyncXdefXinuka(client,Xmessage):
XXXXmsgX=Xmessage.text
XXXXifXmsg.startswith("/")XorXmsg.startswith("@"):
XXXXXXXXmessage.continue_propagation()
XXXXuX=Xmsg.split()
XXXXemjX=Xextract_emojis(msg)
XXXXmsgX=Xmsg.replace(emj,X"")
XXXXifX(
XXXXXXXX[(k)XforXkXinXuXifXk.startswith("@")]
XXXXXXXXandX[(k)XforXkXinXuXifXk.startswith("#")]
XXXXXXXXandX[(k)XforXkXinXuXifXk.startswith("/")]
XXXXXXXXandXre.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)",Xmsg)X!=X[]
XXXX):

XXXXXXXXhX=X"X".join(filter(lambdaXx:Xx[0]X!=X"@",Xu))
XXXXXXXXkmX=Xre.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)",Xr"",Xh)
XXXXXXXXtmX=Xkm.split()
XXXXXXXXjmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"#",Xtm))
XXXXXXXXhmX=Xjm.split()
XXXXXXXXrmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"/",Xhm))
XXXXelifX[(k)XforXkXinXuXifXk.startswith("@")]:

XXXXXXXXrmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"@",Xu))
XXXXelifX[(k)XforXkXinXuXifXk.startswith("#")]:
XXXXXXXXrmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"#",Xu))
XXXXelifX[(k)XforXkXinXuXifXk.startswith("/")]:
XXXXXXXXrmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"/",Xu))
XXXXelifXre.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)",Xmsg)X!=X[]:
XXXXXXXXrmX=Xre.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)",Xr"",Xmsg)
XXXXelse:
XXXXXXXXrmX=Xmsg
XXXXXXXX#XprintX(rm)
XXXXtry:
XXXXXXXXlanX=Xtranslator.detect(rm)
XXXXXXXXlanX=Xlan.lang
XXXXexcept:
XXXXXXXXreturn
XXXXtestX=Xrm
XXXXifXnotX"en"XinXlanXandXnotXlanX==X"":
XXXXXXXXtry:
XXXXXXXXXXXXtestX=Xtranslator.translate(test,Xdest="en")
XXXXXXXXXXXXtestX=Xtest.text
XXXXXXXXexcept:
XXXXXXXXXXXXreturn

XXXX#XtestX=Xemoji.demojize(test.strip())

XXXX#XKangXwithXtheXcreditsXbitchesX@InukaASiTH
XXXXtestX=Xtest.replace("Ineruki",X"Aco")
XXXXtestX=Xtest.replace("Ineruki",X"Aco")

XXXXresponseX=XawaitXlunaQuery(test,Xmessage.from_user.idXifXmessage.from_userXelseX0)
XXXXresponseX=Xresponse.replace("Aco",X"Ineruki")
XXXXresponseX=Xresponse.replace("aco",X"Ineruki")

XXXXproX=Xresponse
XXXXifXnotX"en"XinXlanXandXnotXlanX==X"":
XXXXXXXXproX=Xtranslator.translate(pro,Xdest=lan)
XXXXXXXXproX=Xpro.text
XXXXtry:
XXXXXXXXawaitXInerukix.send_chat_action(message.chat.id,X"typing")
XXXXXXXXawaitXmessage.reply_text(pro)
XXXXexceptXCFError:
XXXXXXXXreturn


@Inerukix.on_message(
XXXXfilters.regex("Ineruki|Ineruki|InerukiX|Inerukix|Inerukix")
XXXX&X~filters.bot
XXXX&X~filters.via_bot
XXXX&X~filters.forwarded
XXXX&X~filters.reply
XXXX&X~filters.channel
XXXX&X~filters.edited
)
asyncXdefXinuka(client,Xmessage):
XXXXmsgX=Xmessage.text
XXXXifXmsg.startswith("/")XorXmsg.startswith("@"):
XXXXXXXXmessage.continue_propagation()
XXXXuX=Xmsg.split()
XXXXemjX=Xextract_emojis(msg)
XXXXmsgX=Xmsg.replace(emj,X"")
XXXXifX(
XXXXXXXX[(k)XforXkXinXuXifXk.startswith("@")]
XXXXXXXXandX[(k)XforXkXinXuXifXk.startswith("#")]
XXXXXXXXandX[(k)XforXkXinXuXifXk.startswith("/")]
XXXXXXXXandXre.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)",Xmsg)X!=X[]
XXXX):

XXXXXXXXhX=X"X".join(filter(lambdaXx:Xx[0]X!=X"@",Xu))
XXXXXXXXkmX=Xre.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)",Xr"",Xh)
XXXXXXXXtmX=Xkm.split()
XXXXXXXXjmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"#",Xtm))
XXXXXXXXhmX=Xjm.split()
XXXXXXXXrmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"/",Xhm))
XXXXelifX[(k)XforXkXinXuXifXk.startswith("@")]:

XXXXXXXXrmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"@",Xu))
XXXXelifX[(k)XforXkXinXuXifXk.startswith("#")]:
XXXXXXXXrmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"#",Xu))
XXXXelifX[(k)XforXkXinXuXifXk.startswith("/")]:
XXXXXXXXrmX=X"X".join(filter(lambdaXx:Xx[0]X!=X"/",Xu))
XXXXelifXre.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)",Xmsg)X!=X[]:
XXXXXXXXrmX=Xre.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)",Xr"",Xmsg)
XXXXelse:
XXXXXXXXrmX=Xmsg
XXXXXXXX#XprintX(rm)
XXXXtry:
XXXXXXXXlanX=Xtranslator.detect(rm)
XXXXXXXXlanX=Xlan.lang
XXXXexcept:
XXXXXXXXreturn
XXXXtestX=Xrm
XXXXifXnotX"en"XinXlanXandXnotXlanX==X"":
XXXXXXXXtry:
XXXXXXXXXXXXtestX=Xtranslator.translate(test,Xdest="en")
XXXXXXXXXXXXtestX=Xtest.text
XXXXXXXXexcept:
XXXXXXXXXXXXreturn

XXXX#XtestX=Xemoji.demojize(test.strip())

XXXXtestX=Xtest.replace("Ineruki",X"Aco")
XXXXtestX=Xtest.replace("Ineruki",X"Aco")
XXXXresponseX=XawaitXlunaQuery(test,Xmessage.from_user.idXifXmessage.from_userXelseX0)
XXXXresponseX=Xresponse.replace("Aco",X"Ineruki")
XXXXresponseX=Xresponse.replace("aco",X"Ineruki")

XXXXproX=Xresponse
XXXXifXnotX"en"XinXlanXandXnotXlanX==X"":
XXXXXXXXtry:
XXXXXXXXXXXXproX=Xtranslator.translate(pro,Xdest=lan)
XXXXXXXXXXXXproX=Xpro.text
XXXXXXXXexceptXException:
XXXXXXXXXXXXreturn
XXXXtry:
XXXXXXXXawaitXInerukix.send_chat_action(message.chat.id,X"typing")
XXXXXXXXawaitXmessage.reply_text(pro)
XXXXexceptXCFError:
XXXXXXXXreturn


__help__X=X"""
<b>XChatbotX</b>
INERUKIXAIX3.0XISXTHEXONLYXAIXSYSTEMXWHICHXCANXDETECTX&XREPLYXUPTOX200XLANGUAGES

X-X/chatbotX[ON/OFF]:XEnablesXandXdisablesXAIXChatXmodeX(EXCLUSIVE)
X-X/chatbotXENX:XEnablesXEnglishXonlyXchatbot
X
X
<b>XAssistantX</b>
X-X/askX[question]:XAskXquestionXfromXIneruki
X-X/askX[replyXtoXvoiceXnote]:XGetXvoiceXreply
X
"""

__mod_name__X=X"AIXAssistant"
