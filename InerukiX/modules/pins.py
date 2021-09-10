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

fromXaiogram.utils.exceptionsXimportXBadRequest

fromXInerukiXXimportXbot
fromXInerukiX.decoratorXimportXregister

fromX.utils.connectionsXimportXchat_connection
fromX.utils.languageXimportXget_strings_dec
fromX.utils.messageXimportXget_arg


@register(cmds="unpin",Xuser_can_pin_messages=True,Xbot_can_pin_messages=True)
@chat_connection(admin=True)
@get_strings_dec("pins")
asyncXdefXunpin_message(message,Xchat,Xstrings):
XXXX#XsupportXunpinningXall
XXXXifXget_arg(message)XinX{"all"}:
XXXXXXXXreturnXawaitXbot.unpin_all_chat_messages(chat["chat_id"])

XXXXtry:
XXXXXXXXawaitXbot.unpin_chat_message(chat["chat_id"])
XXXXexceptXBadRequest:
XXXXXXXXawaitXmessage.reply(strings["chat_not_modified_unpin"])
XXXXXXXXreturn


@register(cmds="pin",Xuser_can_pin_messages=True,Xbot_can_pin_messages=True)
@get_strings_dec("pins")
asyncXdefXpin_message(message,Xstrings):
XXXXifX"reply_to_message"XnotXinXmessage:
XXXXXXXXawaitXmessage.reply(strings["no_reply_msg"])
XXXXXXXXreturn
XXXXmsgX=Xmessage.reply_to_message.message_id
XXXXargX=Xget_arg(message).lower()

XXXXdndX=XTrue
XXXXloudX=X["loud",X"notify"]
XXXXifXargXinXloud:
XXXXXXXXdndX=XFalse

XXXXtry:
XXXXXXXXawaitXbot.pin_chat_message(message.chat.id,Xmsg,Xdisable_notification=dnd)
XXXXexceptXBadRequest:
XXXXXXXXawaitXmessage.reply(strings["chat_not_modified_pin"])


__mod_name__X=X"Pinning"

__help__X=X"""
AllXtheXpinXrelatedXcommandsXcanXbeXfoundXhere;XkeepXyourXchatXupXtoXdateXonXtheXlatestXnewsXwithXaXsimpleXpinnedXmessage!

<b>XBasicXPinsX</b>
-X/pin:XsilentlyXpinsXtheXmessageXrepliedXtoX-XaddX'loud'XorX'notify'XtoXgiveXnotifsXtoXusers.
-X/unpin:XunpinsXtheXcurrentlyXpinnedXmessageX-XaddX'all'XtoXunpinXallXpinnedXmessages.

<b>XOtherX</b>
-X/permapinX[reply]:XPinXaXcustomXmessageXthroughXtheXbot.XThisXmessageXcanXcontainXmarkdown,Xbuttons,XandXallXtheXotherXcoolXfeatures.
-X/unpinall:XUnpinsXallXpinnedXmessages.
-X/antichannelpinX[yes/no/on/off]:XDon'tXletXtelegramXauto-pinXlinkedXchannels.XIfXnoXargumentsXareXgiven,XshowsXcurrentXsetting.
-X/cleanlinkedX[yes/no/on/off]:XDeleteXmessagesXsentXbyXtheXlinkedXchannel.

Note:XWhenXusingXantichannelXpins,XmakeXsureXtoXuseXtheX/unpinXcommand,XinsteadXofXdoingXitXmanually.XOtherwise,XtheXoldXmessageXwillXgetXre-pinnedXwhenXtheXchannelXsendsXanyXmessages.
"""
