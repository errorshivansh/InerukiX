#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2021errorshivansh
#Copyright(C)2020InukaAsith

#ThisfileispartofIneruki(TelegramBot)

#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseas
#publishedbytheFreeSoftwareFoundation,eitherversion3ofthe
#License,or(atyouroption)anylaterversion.

#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.

#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<http://www.gnu.org/licenses/>.

importasyncio
importhtml
importos
importsys

importrapidjson
importrequests

fromInerukiimportINERUKI_VERSION,OWNER_ID,bot,dp
fromIneruki.decoratorimportCOMMANDS_ALIASES,REGISTRED_COMMANDS,register
fromIneruki.modulesimportLOADED_MODULES
fromIneruki.services.mongoimportdb,mongodb
fromIneruki.services.redisimportredis
fromIneruki.services.telethonimporttbot

from.utils.covertimportconvert_size
from.utils.messageimportneed_args_dec
from.utils.notesimportBUTTONS,get_parsed_note_list,send_note,t_unparse_note_item
from.utils.termimportchat_term


@register(cmds="allcommands",is_op=True)
asyncdefall_commands_list(message):
text=""
forcmdinREGISTRED_COMMANDS:
text+="*/"+cmd+"\n"
awaitmessage.reply(text)


@register(cmds="allcmdsaliases",is_op=True)
asyncdefall_cmds_aliases_list(message):
text=""
text=str(COMMANDS_ALIASES)
awaitmessage.reply(text)


@register(cmds="loadedmodules",is_op=True)
asyncdefall_modules_list(message):
text=""
formoduleinLOADED_MODULES:
text+="*"+module.__name__+"\n"
awaitmessage.reply(text)


@register(cmds="avaiblebtns",is_op=True)
asyncdefall_btns_list(message):
text="Avaiblemessageinlinebtns:\n"
formoduleinBUTTONS:
text+="*"+module+"\n"
awaitmessage.reply(text)


@register(cmds="ip",is_owner=True,only_pm=True)
asyncdefget_bot_ip(message):
awaitmessage.reply(requests.get("http://ipinfo.io/ip").text)


@register(cmds="term",is_owner=True)
asyncdefcmd_term(message):
ifmessage.from_user.idindevs:
msg=awaitmessage.reply("Running...")
command=str(message.text.split("",1)[1])
text="<b>Shell:</b>\n"
text+=(
"<code>"
+html.escape(awaitchat_term(message,command),quote=False)
+"</code>"
)
awaitmsg.edit_text(text)
else:
pass


@register(cmds="leavechat",is_owner=True)
@need_args_dec()
asyncdefleave_chat(message):
arg=message.text.split()[1]
cname=message.chat.title
awaitbot.leave_chat(chat_id=arg)
awaitmessage.reply(f"Done,Ileftthegroup<b>{cname}</b>")


@register(cmds="sbroadcast",is_owner=True)
@need_args_dec()
asyncdefsbroadcast(message):
data=awaitget_parsed_note_list(message,split_args=-1)
dp.register_message_handler(check_message_for_smartbroadcast)

awaitdb.sbroadcast.drop({})

chats=mongodb.chat_list.distinct("chat_id")

data["chats_num"]=len(chats)
data["recived_chats"]=0
data["chats"]=chats

awaitdb.sbroadcast.insert_one(data)
awaitmessage.reply(
"Smartbroadcastplannedfor<code>{}</code>chats".format(len(chats))
)


@register(cmds="stopsbroadcast",is_owner=True)
asyncdefstop_sbroadcast(message):
dp.message_handlers.unregister(check_message_for_smartbroadcast)
old=awaitdb.sbroadcast.find_one({})
awaitdb.sbroadcast.drop({})
awaitmessage.reply(
"Smartbroadcaststopped."
"Itwassendedto<code>%d</code>chats."%old["recived_chats"]
)


@register(cmds="continuebroadcast",is_owner=True)
asyncdefcontinue_sbroadcast(message):
dp.register_message_handler(check_message_for_smartbroadcast)
returnawaitmessage.reply("Re-registeredthebroadcasthandler.")


#Checkonsmartbroadcast
asyncdefcheck_message_for_smartbroadcast(message):
chat_id=message.chat.id
ifnot(db_item:=awaitdb.sbroadcast.find_one({"chats":{"$in":[chat_id]}})):
return

text,kwargs=awaitt_unparse_note_item(message,db_item,chat_id)
awaitsend_note(chat_id,text,**kwargs)

awaitdb.sbroadcast.update_one(
{"_id":db_item["_id"]},
{"$pull":{"chats":chat_id},"$inc":{"recived_chats":1}},
)


@register(cmds="purgecache",is_owner=True)
asyncdefpurge_caches(message):
redis.flushdb()
awaitmessage.reply("Rediscachewascleaned.")


@register(cmds="botstop",is_owner=True)
asyncdefbot_stop(message):
awaitmessage.reply("Goodbye...")
sys.exit(1)


@register(cmds="restart",is_owner=True)
asyncdefrestart_bot(message):
awaitmessage.reply("Inerukiwillberestarted...")
args=[sys.executable,"-m","Ineruki"]
os.execl(sys.executable,*args)


@register(cmds="upgrade",is_owner=True)
asyncdefupgrade(message):
m=awaitmessage.reply("Upgradingsources...")
proc=awaitasyncio.create_subprocess_shell(
"gitpull--no-edit",
stdout=asyncio.subprocess.PIPE,
stderr=asyncio.subprocess.STDOUT,
)
stdout=(awaitproc.communicate())[0]
ifproc.returncode==0:
if"Alreadyuptodate."instdout.decode():
awaitm.edit_text("There'snothingtoupgrade.")
else:
awaitm.edit_text("Restarting...")
args=[sys.executable,"-m","Ineruki"]
os.execl(sys.executable,*args)
else:
awaitm.edit_text(
f"Upgradefailed(processexitedwith{proc.returncode}):\n{stdout.decode()}"
)
proc=awaitasyncio.create_subprocess_shell("gitmerge--abort")
awaitproc.communicate()


@register(cmds="upload",is_owner=True)
asyncdefupload_file(message):
input_str=message.get_args()
ifnotos.path.exists(input_str):
awaitmessage.reply("Filenotfound!")
return
awaitmessage.reply("Processing...")
caption_rts=os.path.basename(input_str)
withopen(input_str,"rb")asf:
awaittbot.send_file(
message.chat.id,
f,
caption=caption_rts,
force_document=False,
allow_cache=False,
reply_to=message.message_id,
)


@register(cmds="logs",is_op=True)
asyncdefupload_logs(message):
input_str="logs/Ineruki.log"
withopen(input_str,"rb")asf:
awaittbot.send_file(message.chat.id,f,reply_to=message.message_id)


@register(cmds="crash",is_owner=True)
asyncdefcrash(message):
test=2/0
print(test)


@register(cmds="event",is_op=True)
asyncdefget_event(message):
print(message)
event=str(rapidjson.dumps(message,indent=2))
awaitmessage.reply(event)


@register(cmds="stats",is_op=True)
asyncdefstats(message):
ifmessage.from_user.id==OWNER_ID:
text=f"<b>Ineruki{INERUKI_VERSION}stats</b>\n"

formodulein[mforminLOADED_MODULESifhasattr(m,"__stats__")]:
text+=awaitmodule.__stats__()

awaitmessage.reply(text)
else:
pass


asyncdef__stats__():
text=""
ifos.getenv("WEBHOOKS",False):
text+=f"*Webhooksmode,listenport:<code>{os.getenv('WEBHOOKS_PORT',8080)}</code>\n"
else:
text+="*Long-pollingmode\n"
local_db=awaitdb.command("dbstats")
if"fsTotalSize"inlocal_db:
text+="*Databasesizeis<code>{}</code>,free<code>{}</code>\n".format(
convert_size(local_db["dataSize"]),
convert_size(local_db["fsTotalSize"]-local_db["fsUsedSize"]),
)
else:
text+="*Databasesizeis<code>{}</code>,free<code>{}</code>\n".format(
convert_size(local_db["storageSize"]),
convert_size(536870912-local_db["storageSize"]),
)

text+="*<code>{}</code>totalkeysinRedisdatabase\n".format(len(redis.keys()))
text+="*<code>{}</code>totalcommandsregistred,in<code>{}</code>modules\n".format(
len(REGISTRED_COMMANDS),len(LOADED_MODULES)
)
returntext
