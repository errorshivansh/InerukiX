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

importXasyncio

fromXtelethon.errors.rpcerrorlistXimportXMessageDeleteForbiddenError

fromXInerukiXXimportXbot
fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.telethonXimportXtbot

fromX.utils.languageXimportXget_strings_dec
fromX.utils.notesXimportXBUTTONS


@register(cmds="del",Xbot_can_delete_messages=True,Xuser_can_delete_messages=True)
@get_strings_dec("msg_deleting")
asyncXdefXdel_message(message,Xstrings):
XXXXifXnotXmessage.reply_to_message:
XXXXXXXXawaitXmessage.reply(strings["reply_to_msg"])
XXXXXXXXreturn
XXXXmsgsX=X[message.message_id,Xmessage.reply_to_message.message_id]
XXXXawaitXtbot.delete_messages(message.chat.id,Xmsgs)


@register(
XXXXcmds="purge",
XXXXno_args=True,
XXXXbot_can_delete_messages=True,
XXXXuser_can_delete_messages=True,
)
@get_strings_dec("msg_deleting")
asyncXdefXfast_purge(message,Xstrings):
XXXXifXnotXmessage.reply_to_message:
XXXXXXXXawaitXmessage.reply(strings["reply_to_msg"])
XXXXXXXXreturn
XXXXmsg_idX=Xmessage.reply_to_message.message_id
XXXXdelete_toX=Xmessage.message_id

XXXXchat_idX=Xmessage.chat.id
XXXXmsgsX=X[]
XXXXforXm_idXinXrange(int(delete_to),Xmsg_idX-X1,X-1):
XXXXXXXXmsgs.append(m_id)
XXXXXXXXifXlen(msgs)X==X100:
XXXXXXXXXXXXawaitXtbot.delete_messages(chat_id,Xmsgs)
XXXXXXXXXXXXmsgsX=X[]

XXXXtry:
XXXXXXXXawaitXtbot.delete_messages(chat_id,Xmsgs)
XXXXexceptXMessageDeleteForbiddenError:
XXXXXXXXawaitXmessage.reply(strings["purge_error"])
XXXXXXXXreturn

XXXXmsgX=XawaitXbot.send_message(chat_id,Xstrings["fast_purge_done"])
XXXXawaitXasyncio.sleep(5)
XXXXawaitXmsg.delete()


BUTTONS.update({"delmsg":X"btn_deletemsg_cb"})


@register(regexp=r"btn_deletemsg:(\w+)",Xf="cb",Xallow_kwargs=True)
asyncXdefXdelmsg_btn(event,Xregexp=None,X**kwargs):
XXXXawaitXevent.message.delete()


__mod_name__X=X"Purges"

__help__X=X"""
NeedXtoXdeleteXlotsXofXmessages?XThat'sXwhatXpurgesXareXfor!

<b>AvailableXcommands:</b>
-X/purge:XDeletesXallXmessagesXfromXtheXmessageXyouXrepliedXto,XtoXtheXcurrentXmessage.
-X/del:XDeletesXtheXmessageXyouXrepliedXtoXandXyourX"<code>/del</code>"XcommandXmessage.
"""
