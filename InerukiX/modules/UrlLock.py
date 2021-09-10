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

importXasyncio

fromXpyrogramXimportXfilters
fromXpyrogram.errorsXimportXRPCError

fromXInerukiXXimportXBOT_ID
fromXInerukiX.db.mongo_helpers.lockurlXimportXadd_chat,Xget_session,Xremove_chat
fromXInerukiX.function.pluginhelpersXimportX(
XXXXadmins_only,
XXXXedit_or_reply,
XXXXget_url,
XXXXmember_permissions,
)
fromXInerukiX.services.pyrogramXimportXpbot


@pbot.on_message(
XXXXfilters.command("urllock")X&X~filters.editedX&X~filters.botX&X~filters.private
)
@admins_only
asyncXdefXhmm(_,Xmessage):
XXXXglobalXIneruki_chats
XXXXtry:
XXXXXXXXuser_idX=Xmessage.from_user.id
XXXXexcept:
XXXXXXXXreturn
XXXXifXnotX"can_change_info"XinX(awaitXmember_permissions(message.chat.id,Xuser_id)):
XXXXXXXXawaitXmessage.reply_text("**YouXdon'tXhaveXenoughXpermissions**")
XXXXXXXXreturn
XXXXifXlen(message.command)X!=X2:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"IXonlyXrecognizeX`/urllockXon`XandX/urllockX`offXonly`"
XXXXXXXX)
XXXXXXXXreturn
XXXXstatusX=Xmessage.text.split(None,X1)[1]
XXXXmessage.chat.id
XXXXifXstatusX==X"ON"XorXstatusX==X"on"XorXstatusX==X"On":
XXXXXXXXlelX=XawaitXedit_or_reply(message,X"`Processing...`")
XXXXXXXXlolX=Xadd_chat(int(message.chat.id))
XXXXXXXXifXnotXlol:
XXXXXXXXXXXXawaitXlel.edit("URLXBlockXAlreadyXActivatedXInXThisXChat")
XXXXXXXXXXXXreturn
XXXXXXXXawaitXlel.edit(
XXXXXXXXXXXXf"URLXBlockXSuccessfullyXAddedXForXUsersXInXTheXChatX{message.chat.id}"
XXXXXXXX)

XXXXelifXstatusX==X"OFF"XorXstatusX==X"off"XorXstatusX==X"Off":
XXXXXXXXlelX=XawaitXedit_or_reply(message,X"`Processing...`")
XXXXXXXXEscobarX=Xremove_chat(int(message.chat.id))
XXXXXXXXifXnotXEscobar:
XXXXXXXXXXXXawaitXlel.edit("URLXBlockXWasXNotXActivatedXInXThisXChat")
XXXXXXXXXXXXreturn
XXXXXXXXawaitXlel.edit(
XXXXXXXXXXXXf"URLXBlockXSuccessfullyXDeactivatedXForXUsersXInXTheXChatX{message.chat.id}"
XXXXXXXX)
XXXXelse:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"IXonlyXrecognizeX`/urllockXon`XandX/urllockX`offXonly`"
XXXXXXXX)


@pbot.on_message(
XXXXfilters.incomingX&Xfilters.textX&X~filters.privateX&X~filters.channelX&X~filters.bot
)
asyncXdefXhi(client,Xmessage):
XXXXifXnotXget_session(int(message.chat.id)):
XXXXXXXXmessage.continue_propagation()
XXXXtry:
XXXXXXXXuser_idX=Xmessage.from_user.id
XXXXexcept:
XXXXXXXXreturn
XXXXtry:
XXXXXXXXifXnotXlen(awaitXmember_permissions(message.chat.id,Xuser_id))X<X1:
XXXXXXXXXXXXmessage.continue_propagation()
XXXXXXXXifXlen(awaitXmember_permissions(message.chat.id,XBOT_ID))X<X1:
XXXXXXXXXXXXmessage.continue_propagation()
XXXXXXXXifXnotX"can_delete_messages"XinX(
XXXXXXXXXXXXawaitXmember_permissions(message.chat.id,XBOT_ID)
XXXXXXXX):
XXXXXXXXXXXXmessage.continue_propagation()
XXXXexceptXRPCError:
XXXXXXXXreturn
XXXXtry:

XXXXXXXXlelX=Xget_url(message)
XXXXexcept:
XXXXXXXXreturn

XXXXifXlel:
XXXXXXXXtry:
XXXXXXXXXXXXawaitXmessage.delete()
XXXXXXXXXXXXsenderX=Xmessage.from_user.mention()
XXXXXXXXXXXXlolX=XawaitXclient.send_message(
XXXXXXXXXXXXXXXXmessage.chat.id,
XXXXXXXXXXXXXXXXf"{sender},XYourXmessageXwasXdeletedXasXitXcontainXaXlink(s).X\nX❗️XLinksXareXnotXallowedXhere",
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXasyncio.sleep(10)
XXXXXXXXXXXXawaitXlol.delete()
XXXXXXXXexcept:
XXXXXXXXXXXXmessage.continue_propagation()
XXXXelse:
XXXXXXXXmessage.continue_propagation()
