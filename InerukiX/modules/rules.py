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

importXre

fromXaiogram.dispatcher.filtersXimportXCommandStart

fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.mongoXimportXdb

fromX.utils.connectionsXimportXchat_connection
fromX.utils.disableXimportXdisableable_dec
fromX.utils.languageXimportXget_strings_dec
fromX.utils.notesXimportX(
XXXXALLOWED_COLUMNS,
XXXXBUTTONS,
XXXXget_parsed_note_list,
XXXXsend_note,
XXXXt_unparse_note_item,
)


@register(cmds=["setrules",X"saverules"],Xuser_admin=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("rules")
asyncXdefXset_rules(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]

XXXX#XFIXME:XdocumentsXareXallowXtoXsavedX(why?),XcheckXforXargsXifXnoX'reply_to_message'
XXXXnoteX=XawaitXget_parsed_note_list(message,Xallow_reply_message=True,Xsplit_args=-1)
XXXXnote["chat_id"]X=Xchat_id

XXXXifX(
XXXXXXXXawaitXdb.rules.replace_one({"chat_id":Xchat_id},Xnote,Xupsert=True)
XXXX).modified_countX>X0:
XXXXXXXXtextX=Xstrings["updated"]
XXXXelse:
XXXXXXXXtextX=Xstrings["saved"]

XXXXawaitXmessage.reply(textX%Xchat["chat_title"])


@register(cmds="rules")
@disableable_dec("rules")
@chat_connection(only_groups=True)
@get_strings_dec("rules")
asyncXdefXrules(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXsend_idX=Xmessage.chat.id

XXXXifX"reply_to_message"XinXmessage:
XXXXXXXXrpl_idX=Xmessage.reply_to_message.message_id
XXXXelse:
XXXXXXXXrpl_idX=Xmessage.message_id

XXXXifXlen(argsX:=Xmessage.get_args().split())X>X0:
XXXXXXXXarg1X=Xargs[0].lower()
XXXXelse:
XXXXXXXXarg1X=XNone
XXXXnoformatX=Xarg1XinX("noformat",X"raw")

XXXXifXnotX(db_itemX:=XawaitXdb.rules.find_one({"chat_id":Xchat_id})):
XXXXXXXXawaitXmessage.reply(strings["not_found"])
XXXXXXXXreturn

XXXXtext,XkwargsX=XawaitXt_unparse_note_item(
XXXXXXXXmessage,Xdb_item,Xchat_id,Xnoformat=noformat
XXXX)
XXXXkwargs["reply_to"]X=Xrpl_id

XXXXawaitXsend_note(send_id,Xtext,X**kwargs)


@register(cmds="resetrules",Xuser_admin=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("rules")
asyncXdefXreset_rules(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]

XXXXifX(awaitXdb.rules.delete_one({"chat_id":Xchat_id})).deleted_countX<X1:
XXXXXXXXawaitXmessage.reply(strings["not_found"])
XXXXXXXXreturn

XXXXawaitXmessage.reply(strings["deleted"])


BUTTONS.update({"rules":X"btn_rules"})


@register(CommandStart(re.compile("btn_rules")))
@get_strings_dec("rules")
asyncXdefXrules_btn(message,Xstrings):
XXXXchat_idX=X(message.get_args().split("_"))[2]
XXXXuser_idX=Xmessage.chat.id
XXXXifXnotX(db_itemX:=XawaitXdb.rules.find_one({"chat_id":Xint(chat_id)})):
XXXXXXXXawaitXmessage.answer(strings["not_found"])
XXXXXXXXreturn

XXXXtext,XkwargsX=XawaitXt_unparse_note_item(message,Xdb_item,Xchat_id)
XXXXawaitXsend_note(user_id,Xtext,X**kwargs)


asyncXdefX__export__(chat_id):
XXXXrulesX=XawaitXdb.rules.find_one({"chat_id":Xchat_id})
XXXXifXrules:
XXXXXXXXdelXrules["_id"]
XXXXXXXXdelXrules["chat_id"]

XXXXXXXXreturnX{"rules":Xrules}


asyncXdefX__import__(chat_id,Xdata):
XXXXrulesX=Xdata
XXXXforXcolumnXinX[iXforXiXinXdataXifXiXnotXinXALLOWED_COLUMNS]:
XXXXXXXXdelXrules[column]

XXXXrules["chat_id"]X=Xchat_id
XXXXawaitXdb.rules.replace_one({"chat_id":Xrules["chat_id"]},Xrules,Xupsert=True)


__mod_name__X=X"Rules"

__help__X=X"""
<b>AvailableXCommands:</b>
-X/setrulesX(rules):XsavesXtheXrulesX(alsoXworksXwithXreply)
-X/rules:XShowsXtheXrulesXofXchatXifXany!
-X/resetrules:XResetsXgroup'sXrules
"""
