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
importio
fromdatetimeimportdatetime,timedelta

importrapidjson
fromaiogramimporttypes
fromaiogram.dispatcher.filters.stateimportState,StatesGroup
fromaiogram.types.input_fileimportInputFile
frombabel.datesimportformat_timedelta

fromInerukiimportOPERATORS,bot
fromIneruki.decoratorimportregister
fromIneruki.services.redisimportredis

from.importLOADED_MODULES
from.utils.connectionsimportchat_connection
from.utils.languageimportget_strings_dec

VERSION=5


#Waitingforimportfilestate
classImportFileWait(StatesGroup):
waiting=State()


@register(cmds="export",user_admin=True)
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("imports_exports")
asyncdefexport_chat_data(message,chat,strings):
chat_id=chat["chat_id"]
key="export_lock:"+str(chat_id)
ifredis.get(key)andmessage.from_user.idnotinOPERATORS:
ttl=format_timedelta(
timedelta(seconds=redis.ttl(key)),strings["language_info"]["babel"]
)
awaitmessage.reply(strings["exports_locked"]%ttl)
return

redis.set(key,1)
redis.expire(key,7200)

msg=awaitmessage.reply(strings["started_exporting"])
data={
"general":{
"chat_name":chat["chat_title"],
"chat_id":chat_id,
"date":datetime.now().strftime("%Y-%m-%d%H:%M:%S"),
"version":VERSION,
}
}

formodulein[mforminLOADED_MODULESifhasattr(m,"__export__")]:
awaitasyncio.sleep(0)#Switchtoothereventsbeforecontinue
ifk:=awaitmodule.__export__(chat_id):
data.update(k)

jfile=InputFile(
io.StringIO(rapidjson.dumps(data,indent=2)),filename=f"{chat_id}_export.json"
)
text=strings["export_done"].format(chat_name=chat["chat_title"])
awaitmessage.answer_document(jfile,text,reply=message.message_id)
awaitmsg.delete()


@register(cmds="import",user_admin=True)
@get_strings_dec("imports_exports")
asyncdefimport_reply(message,strings):
if"document"inmessage:
document=message.document
else:
if"reply_to_message"notinmessage:
awaitImportFileWait.waiting.set()
awaitmessage.reply(strings["send_import_file"])
return

elif"document"notinmessage.reply_to_message:
awaitmessage.reply(strings["rpl_to_file"])
return
document=message.reply_to_message.document

awaitimport_fun(message,document)


@register(
state=ImportFileWait.waiting,
content_types=types.ContentTypes.DOCUMENT,
allow_kwargs=True,
)
asyncdefimport_state(message,state=None,**kwargs):
awaitimport_fun(message,message.document)
awaitstate.finish()


@chat_connection(admin=True,only_groups=True)
@get_strings_dec("imports_exports")
asyncdefimport_fun(message,document,chat,strings):
chat_id=chat["chat_id"]
key="import_lock:"+str(chat_id)
ifredis.get(key)andmessage.from_user.idnotinOPERATORS:
ttl=format_timedelta(
timedelta(seconds=redis.ttl(key)),strings["language_info"]["babel"]
)
awaitmessage.reply(strings["imports_locked"]%ttl)
return

redis.set(key,1)
redis.expire(key,7200)

msg=awaitmessage.reply(strings["started_importing"])
ifdocument["file_size"]>52428800:
awaitmessage.reply(strings["big_file"])
return
data=awaitbot.download_file_by_id(document.file_id,io.BytesIO())
try:
data=rapidjson.load(data)
exceptValueError:
returnawaitmessage.reply(strings["invalid_file"])

if"general"notindata:
awaitmessage.reply(strings["bad_file"])
return

file_version=data["general"]["version"]

iffile_version>VERSION:
awaitmessage.reply(strings["file_version_so_new"])
return

imported=[]
formodulein[mforminLOADED_MODULESifhasattr(m,"__import__")]:
module_name=module.__name__.replace("Ineruki.modules.","")
ifmodule_namenotindata:
continue
ifnotdata[module_name]:
continue

imported.append(module_name)
awaitasyncio.sleep(0)#Switchtoothereventsbeforecontinue
awaitmodule.__import__(chat_id,data[module_name])

awaitmsg.edit_text(strings["import_done"])


__mod_name__="Backups"

__help__="""
Sometimesyouwanttoseeallofyourdatainyourchatsoryouwanttocopyyourdatatoanotherchatsoryouevenwanttoswiftbots,inallthesecasesimports/exportsforyou!

<b>Availablecommands:</b>
-/export:Exportchat'sdatatoJSONfile
-/import:ImportJSONfiletochat

<b>Notes:</b>Exporting/importingavaibleevery2hourstopreventflooding.
"""
