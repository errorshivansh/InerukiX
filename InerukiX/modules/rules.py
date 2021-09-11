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

importre

fromaiogram.dispatcher.filtersimportCommandStart

fromIneruki.decoratorimportregister
fromIneruki.services.mongoimportdb

from.utils.connectionsimportchat_connection
from.utils.disableimportdisableable_dec
from.utils.languageimportget_strings_dec
from.utils.notesimport(
ALLOWED_COLUMNS,
BUTTONS,
get_parsed_note_list,
send_note,
t_unparse_note_item,
)


@register(cmds=["setrules","saverules"],user_admin=True)
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("rules")
asyncdefset_rules(message,chat,strings):
chat_id=chat["chat_id"]

#FIME:documentsareallowtosaved(why?),checkforargsifno'reply_to_message'
note=awaitget_parsed_note_list(message,allow_reply_message=True,split_args=-1)
note["chat_id"]=chat_id

if(
awaitdb.rules.replace_one({"chat_id":chat_id},note,upsert=True)
).modified_count>0:
text=strings["updated"]
else:
text=strings["saved"]

awaitmessage.reply(text%chat["chat_title"])


@register(cmds="rules")
@disableable_dec("rules")
@chat_connection(only_groups=True)
@get_strings_dec("rules")
asyncdefrules(message,chat,strings):
chat_id=chat["chat_id"]
send_id=message.chat.id

if"reply_to_message"inmessage:
rpl_id=message.reply_to_message.message_id
else:
rpl_id=message.message_id

iflen(args:=message.get_args().split())>0:
arg1=args[0].lower()
else:
arg1=None
noformat=arg1in("noformat","raw")

ifnot(db_item:=awaitdb.rules.find_one({"chat_id":chat_id})):
awaitmessage.reply(strings["not_found"])
return

text,kwargs=awaitt_unparse_note_item(
message,db_item,chat_id,noformat=noformat
)
kwargs["reply_to"]=rpl_id

awaitsend_note(send_id,text,**kwargs)


@register(cmds="resetrules",user_admin=True)
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("rules")
asyncdefreset_rules(message,chat,strings):
chat_id=chat["chat_id"]

if(awaitdb.rules.delete_one({"chat_id":chat_id})).deleted_count<1:
awaitmessage.reply(strings["not_found"])
return

awaitmessage.reply(strings["deleted"])


BUTTONS.update({"rules":"btn_rules"})


@register(CommandStart(re.compile("btn_rules")))
@get_strings_dec("rules")
asyncdefrules_btn(message,strings):
chat_id=(message.get_args().split("_"))[2]
user_id=message.chat.id
ifnot(db_item:=awaitdb.rules.find_one({"chat_id":int(chat_id)})):
awaitmessage.answer(strings["not_found"])
return

text,kwargs=awaitt_unparse_note_item(message,db_item,chat_id)
awaitsend_note(user_id,text,**kwargs)


asyncdef__export__(chat_id):
rules=awaitdb.rules.find_one({"chat_id":chat_id})
ifrules:
delrules["_id"]
delrules["chat_id"]

return{"rules":rules}


asyncdef__import__(chat_id,data):
rules=data
forcolumnin[iforiindataifinotinALLOWED_COLUMNS]:
delrules[column]

rules["chat_id"]=chat_id
awaitdb.rules.replace_one({"chat_id":rules["chat_id"]},rules,upsert=True)


__mod_name__="Rules"

__help__="""
<b>AvailableCommands:</b>
-/setrules(rules):savestherules(alsoworkswithreply)
-/rules:Showstherulesofchatifany!
-/resetrules:Resetsgroup'srules
"""
