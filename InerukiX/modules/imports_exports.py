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
importXio
fromXdatetimeXimportXdatetime,Xtimedelta

importXrapidjson
fromXaiogramXimportXtypes
fromXaiogram.dispatcher.filters.stateXimportXState,XStatesGroup
fromXaiogram.types.input_fileXimportXInputFile
fromXbabel.datesXimportXformat_timedelta

fromXInerukiXXimportXOPERATORS,Xbot
fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.redisXimportXredis

fromX.XimportXLOADED_MODULES
fromX.utils.connectionsXimportXchat_connection
fromX.utils.languageXimportXget_strings_dec

VERSIONX=X5


#XWaitingXforXimportXfileXstate
classXImportFileWait(StatesGroup):
XXXXwaitingX=XState()


@register(cmds="export",Xuser_admin=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("imports_exports")
asyncXdefXexport_chat_data(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXkeyX=X"export_lock:"X+Xstr(chat_id)
XXXXifXredis.get(key)XandXmessage.from_user.idXnotXinXOPERATORS:
XXXXXXXXttlX=Xformat_timedelta(
XXXXXXXXXXXXtimedelta(seconds=redis.ttl(key)),Xstrings["language_info"]["babel"]
XXXXXXXX)
XXXXXXXXawaitXmessage.reply(strings["exports_locked"]X%Xttl)
XXXXXXXXreturn

XXXXredis.set(key,X1)
XXXXredis.expire(key,X7200)

XXXXmsgX=XawaitXmessage.reply(strings["started_exporting"])
XXXXdataX=X{
XXXXXXXX"general":X{
XXXXXXXXXXXX"chat_name":Xchat["chat_title"],
XXXXXXXXXXXX"chat_id":Xchat_id,
XXXXXXXXXXXX"date":Xdatetime.now().strftime("%Y-%m-%dX%H:%M:%S"),
XXXXXXXXXXXX"version":XVERSION,
XXXXXXXX}
XXXX}

XXXXforXmoduleXinX[mXforXmXinXLOADED_MODULESXifXhasattr(m,X"__export__")]:
XXXXXXXXawaitXasyncio.sleep(0)XX#XSwitchXtoXotherXeventsXbeforeXcontinue
XXXXXXXXifXkX:=XawaitXmodule.__export__(chat_id):
XXXXXXXXXXXXdata.update(k)

XXXXjfileX=XInputFile(
XXXXXXXXio.StringIO(rapidjson.dumps(data,Xindent=2)),Xfilename=f"{chat_id}_export.json"
XXXX)
XXXXtextX=Xstrings["export_done"].format(chat_name=chat["chat_title"])
XXXXawaitXmessage.answer_document(jfile,Xtext,Xreply=message.message_id)
XXXXawaitXmsg.delete()


@register(cmds="import",Xuser_admin=True)
@get_strings_dec("imports_exports")
asyncXdefXimport_reply(message,Xstrings):
XXXXifX"document"XinXmessage:
XXXXXXXXdocumentX=Xmessage.document
XXXXelse:
XXXXXXXXifX"reply_to_message"XnotXinXmessage:
XXXXXXXXXXXXawaitXImportFileWait.waiting.set()
XXXXXXXXXXXXawaitXmessage.reply(strings["send_import_file"])
XXXXXXXXXXXXreturn

XXXXXXXXelifX"document"XnotXinXmessage.reply_to_message:
XXXXXXXXXXXXawaitXmessage.reply(strings["rpl_to_file"])
XXXXXXXXXXXXreturn
XXXXXXXXdocumentX=Xmessage.reply_to_message.document

XXXXawaitXimport_fun(message,Xdocument)


@register(
XXXXstate=ImportFileWait.waiting,
XXXXcontent_types=types.ContentTypes.DOCUMENT,
XXXXallow_kwargs=True,
)
asyncXdefXimport_state(message,Xstate=None,X**kwargs):
XXXXawaitXimport_fun(message,Xmessage.document)
XXXXawaitXstate.finish()


@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("imports_exports")
asyncXdefXimport_fun(message,Xdocument,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXkeyX=X"import_lock:"X+Xstr(chat_id)
XXXXifXredis.get(key)XandXmessage.from_user.idXnotXinXOPERATORS:
XXXXXXXXttlX=Xformat_timedelta(
XXXXXXXXXXXXtimedelta(seconds=redis.ttl(key)),Xstrings["language_info"]["babel"]
XXXXXXXX)
XXXXXXXXawaitXmessage.reply(strings["imports_locked"]X%Xttl)
XXXXXXXXreturn

XXXXredis.set(key,X1)
XXXXredis.expire(key,X7200)

XXXXmsgX=XawaitXmessage.reply(strings["started_importing"])
XXXXifXdocument["file_size"]X>X52428800:
XXXXXXXXawaitXmessage.reply(strings["big_file"])
XXXXXXXXreturn
XXXXdataX=XawaitXbot.download_file_by_id(document.file_id,Xio.BytesIO())
XXXXtry:
XXXXXXXXdataX=Xrapidjson.load(data)
XXXXexceptXValueError:
XXXXXXXXreturnXawaitXmessage.reply(strings["invalid_file"])

XXXXifX"general"XnotXinXdata:
XXXXXXXXawaitXmessage.reply(strings["bad_file"])
XXXXXXXXreturn

XXXXfile_versionX=Xdata["general"]["version"]

XXXXifXfile_versionX>XVERSION:
XXXXXXXXawaitXmessage.reply(strings["file_version_so_new"])
XXXXXXXXreturn

XXXXimportedX=X[]
XXXXforXmoduleXinX[mXforXmXinXLOADED_MODULESXifXhasattr(m,X"__import__")]:
XXXXXXXXmodule_nameX=Xmodule.__name__.replace("InerukiX.modules.",X"")
XXXXXXXXifXmodule_nameXnotXinXdata:
XXXXXXXXXXXXcontinue
XXXXXXXXifXnotXdata[module_name]:
XXXXXXXXXXXXcontinue

XXXXXXXXimported.append(module_name)
XXXXXXXXawaitXasyncio.sleep(0)XX#XSwitchXtoXotherXeventsXbeforeXcontinue
XXXXXXXXawaitXmodule.__import__(chat_id,Xdata[module_name])

XXXXawaitXmsg.edit_text(strings["import_done"])


__mod_name__X=X"Backups"

__help__X=X"""
SometimesXyouXwantXtoXseeXallXofXyourXdataXinXyourXchatsXorXyouXwantXtoXcopyXyourXdataXtoXanotherXchatsXorXyouXevenXwantXtoXswiftXbots,XinXallXtheseXcasesXimports/exportsXforXyou!

<b>AvailableXcommands:</b>
-X/export:XExportXchat'sXdataXtoXJSONXfile
-X/import:XImportXJSONXfileXtoXchat

<b>Notes:</b>XExportingX/XimportingXavaibleXeveryX2XhoursXtoXpreventXflooding.
"""
