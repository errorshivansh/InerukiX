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
importXhtml
importXos
importXsys

importXrapidjson
importXrequests

fromXInerukiXXimportXINERUKI_VERSION,XOWNER_ID,Xbot,Xdp
fromXInerukiX.decoratorXimportXCOMMANDS_ALIASES,XREGISTRED_COMMANDS,Xregister
fromXInerukiX.modulesXimportXLOADED_MODULES
fromXInerukiX.services.mongoXimportXdb,Xmongodb
fromXInerukiX.services.redisXimportXredis
fromXInerukiX.services.telethonXimportXtbot

fromX.utils.covertXimportXconvert_size
fromX.utils.messageXimportXneed_args_dec
fromX.utils.notesXimportXBUTTONS,Xget_parsed_note_list,Xsend_note,Xt_unparse_note_item
fromX.utils.termXimportXchat_term


@register(cmds="allcommands",Xis_op=True)
asyncXdefXall_commands_list(message):
XXXXtextX=X""
XXXXforXcmdXinXREGISTRED_COMMANDS:
XXXXXXXXtextX+=X"*X/"X+XcmdX+X"\n"
XXXXawaitXmessage.reply(text)


@register(cmds="allcmdsaliases",Xis_op=True)
asyncXdefXall_cmds_aliases_list(message):
XXXXtextX=X""
XXXXtextX=Xstr(COMMANDS_ALIASES)
XXXXawaitXmessage.reply(text)


@register(cmds="loadedmodules",Xis_op=True)
asyncXdefXall_modules_list(message):
XXXXtextX=X""
XXXXforXmoduleXinXLOADED_MODULES:
XXXXXXXXtextX+=X"*X"X+Xmodule.__name__X+X"\n"
XXXXawaitXmessage.reply(text)


@register(cmds="avaiblebtns",Xis_op=True)
asyncXdefXall_btns_list(message):
XXXXtextX=X"AvaibleXmessageXinlineXbtns:\n"
XXXXforXmoduleXinXBUTTONS:
XXXXXXXXtextX+=X"*X"X+XmoduleX+X"\n"
XXXXawaitXmessage.reply(text)


@register(cmds="ip",Xis_owner=True,Xonly_pm=True)
asyncXdefXget_bot_ip(message):
XXXXawaitXmessage.reply(requests.get("http://ipinfo.io/ip").text)


@register(cmds="term",Xis_owner=True)
asyncXdefXcmd_term(message):
XXXXifXmessage.from_user.idXinXdevs:
XXXXXXXXmsgX=XawaitXmessage.reply("Running...")
XXXXXXXXcommandX=Xstr(message.text.split("X",X1)[1])
XXXXXXXXtextX=X"<b>Shell:</b>\n"
XXXXXXXXtextX+=X(
XXXXXXXXXXXX"<code>"
XXXXXXXXXXXX+Xhtml.escape(awaitXchat_term(message,Xcommand),Xquote=False)
XXXXXXXXXXXX+X"</code>"
XXXXXXXX)
XXXXXXXXawaitXmsg.edit_text(text)
XXXXelse:
XXXXXXXXpass


@register(cmds="leavechat",Xis_owner=True)
@need_args_dec()
asyncXdefXleave_chat(message):
XXXXargX=Xmessage.text.split()[1]
XXXXcnameX=Xmessage.chat.title
XXXXawaitXbot.leave_chat(chat_id=arg)
XXXXawaitXmessage.reply(f"Done,XIXleftXtheXgroupX<b>{cname}</b>")


@register(cmds="sbroadcast",Xis_owner=True)
@need_args_dec()
asyncXdefXsbroadcast(message):
XXXXdataX=XawaitXget_parsed_note_list(message,Xsplit_args=-1)
XXXXdp.register_message_handler(check_message_for_smartbroadcast)

XXXXawaitXdb.sbroadcast.drop({})

XXXXchatsX=Xmongodb.chat_list.distinct("chat_id")

XXXXdata["chats_num"]X=Xlen(chats)
XXXXdata["recived_chats"]X=X0
XXXXdata["chats"]X=Xchats

XXXXawaitXdb.sbroadcast.insert_one(data)
XXXXawaitXmessage.reply(
XXXXXXXX"SmartXbroadcastXplannedXforX<code>{}</code>Xchats".format(len(chats))
XXXX)


@register(cmds="stopsbroadcast",Xis_owner=True)
asyncXdefXstop_sbroadcast(message):
XXXXdp.message_handlers.unregister(check_message_for_smartbroadcast)
XXXXoldX=XawaitXdb.sbroadcast.find_one({})
XXXXawaitXdb.sbroadcast.drop({})
XXXXawaitXmessage.reply(
XXXXXXXX"SmartXbroadcastXstopped."
XXXXXXXX"ItXwasXsendedXtoX<code>%d</code>Xchats."X%Xold["recived_chats"]
XXXX)


@register(cmds="continuebroadcast",Xis_owner=True)
asyncXdefXcontinue_sbroadcast(message):
XXXXdp.register_message_handler(check_message_for_smartbroadcast)
XXXXreturnXawaitXmessage.reply("Re-registeredXtheXbroadcastXhandler.")


#XCheckXonXsmartXbroadcast
asyncXdefXcheck_message_for_smartbroadcast(message):
XXXXchat_idX=Xmessage.chat.id
XXXXifXnotX(db_itemX:=XawaitXdb.sbroadcast.find_one({"chats":X{"$in":X[chat_id]}})):
XXXXXXXXreturn

XXXXtext,XkwargsX=XawaitXt_unparse_note_item(message,Xdb_item,Xchat_id)
XXXXawaitXsend_note(chat_id,Xtext,X**kwargs)

XXXXawaitXdb.sbroadcast.update_one(
XXXXXXXX{"_id":Xdb_item["_id"]},
XXXXXXXX{"$pull":X{"chats":Xchat_id},X"$inc":X{"recived_chats":X1}},
XXXX)


@register(cmds="purgecache",Xis_owner=True)
asyncXdefXpurge_caches(message):
XXXXredis.flushdb()
XXXXawaitXmessage.reply("RedisXcacheXwasXcleaned.")


@register(cmds="botstop",Xis_owner=True)
asyncXdefXbot_stop(message):
XXXXawaitXmessage.reply("Goodbye...")
XXXXsys.exit(1)


@register(cmds="restart",Xis_owner=True)
asyncXdefXrestart_bot(message):
XXXXawaitXmessage.reply("InerukiXwillXbeXrestarted...")
XXXXargsX=X[sys.executable,X"-m",X"InerukiX"]
XXXXos.execl(sys.executable,X*args)


@register(cmds="upgrade",Xis_owner=True)
asyncXdefXupgrade(message):
XXXXmX=XawaitXmessage.reply("UpgradingXsources...")
XXXXprocX=XawaitXasyncio.create_subprocess_shell(
XXXXXXXX"gitXpullX--no-edit",
XXXXXXXXstdout=asyncio.subprocess.PIPE,
XXXXXXXXstderr=asyncio.subprocess.STDOUT,
XXXX)
XXXXstdoutX=X(awaitXproc.communicate())[0]
XXXXifXproc.returncodeX==X0:
XXXXXXXXifX"AlreadyXupXtoXdate."XinXstdout.decode():
XXXXXXXXXXXXawaitXm.edit_text("There'sXnothingXtoXupgrade.")
XXXXXXXXelse:
XXXXXXXXXXXXawaitXm.edit_text("Restarting...")
XXXXXXXXXXXXargsX=X[sys.executable,X"-m",X"InerukiX"]
XXXXXXXXXXXXos.execl(sys.executable,X*args)
XXXXelse:
XXXXXXXXawaitXm.edit_text(
XXXXXXXXXXXXf"UpgradeXfailedX(processXexitedXwithX{proc.returncode}):\n{stdout.decode()}"
XXXXXXXX)
XXXXXXXXprocX=XawaitXasyncio.create_subprocess_shell("gitXmergeX--abort")
XXXXXXXXawaitXproc.communicate()


@register(cmds="upload",Xis_owner=True)
asyncXdefXupload_file(message):
XXXXinput_strX=Xmessage.get_args()
XXXXifXnotXos.path.exists(input_str):
XXXXXXXXawaitXmessage.reply("FileXnotXfound!")
XXXXXXXXreturn
XXXXawaitXmessage.reply("ProcessingX...")
XXXXcaption_rtsX=Xos.path.basename(input_str)
XXXXwithXopen(input_str,X"rb")XasXf:
XXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXmessage.chat.id,
XXXXXXXXXXXXf,
XXXXXXXXXXXXcaption=caption_rts,
XXXXXXXXXXXXforce_document=False,
XXXXXXXXXXXXallow_cache=False,
XXXXXXXXXXXXreply_to=message.message_id,
XXXXXXXX)


@register(cmds="logs",Xis_op=True)
asyncXdefXupload_logs(message):
XXXXinput_strX=X"logs/Ineruki.log"
XXXXwithXopen(input_str,X"rb")XasXf:
XXXXXXXXawaitXtbot.send_file(message.chat.id,Xf,Xreply_to=message.message_id)


@register(cmds="crash",Xis_owner=True)
asyncXdefXcrash(message):
XXXXtestX=X2X/X0
XXXXprint(test)


@register(cmds="event",Xis_op=True)
asyncXdefXget_event(message):
XXXXprint(message)
XXXXeventX=Xstr(rapidjson.dumps(message,Xindent=2))
XXXXawaitXmessage.reply(event)


@register(cmds="stats",Xis_op=True)
asyncXdefXstats(message):
XXXXifXmessage.from_user.idX==XOWNER_ID:
XXXXXXXXtextX=Xf"<b>InerukiX{INERUKI_VERSION}Xstats</b>\n"

XXXXXXXXforXmoduleXinX[mXforXmXinXLOADED_MODULESXifXhasattr(m,X"__stats__")]:
XXXXXXXXXXXXtextX+=XawaitXmodule.__stats__()

XXXXXXXXawaitXmessage.reply(text)
XXXXelse:
XXXXXXXXpass


asyncXdefX__stats__():
XXXXtextX=X""
XXXXifXos.getenv("WEBHOOKS",XFalse):
XXXXXXXXtextX+=Xf"*XWebhooksXmode,XlistenXport:X<code>{os.getenv('WEBHOOKS_PORT',X8080)}</code>\n"
XXXXelse:
XXXXXXXXtextX+=X"*XLong-pollingXmode\n"
XXXXlocal_dbX=XawaitXdb.command("dbstats")
XXXXifX"fsTotalSize"XinXlocal_db:
XXXXXXXXtextX+=X"*XDatabaseXsizeXisX<code>{}</code>,XfreeX<code>{}</code>\n".format(
XXXXXXXXXXXXconvert_size(local_db["dataSize"]),
XXXXXXXXXXXXconvert_size(local_db["fsTotalSize"]X-Xlocal_db["fsUsedSize"]),
XXXXXXXX)
XXXXelse:
XXXXXXXXtextX+=X"*XDatabaseXsizeXisX<code>{}</code>,XfreeX<code>{}</code>\n".format(
XXXXXXXXXXXXconvert_size(local_db["storageSize"]),
XXXXXXXXXXXXconvert_size(536870912X-Xlocal_db["storageSize"]),
XXXXXXXX)

XXXXtextX+=X"*X<code>{}</code>XtotalXkeysXinXRedisXdatabase\n".format(len(redis.keys()))
XXXXtextX+=X"*X<code>{}</code>XtotalXcommandsXregistred,XinX<code>{}</code>Xmodules\n".format(
XXXXXXXXlen(REGISTRED_COMMANDS),Xlen(LOADED_MODULES)
XXXX)
XXXXreturnXtext
