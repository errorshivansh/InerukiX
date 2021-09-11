fromreimportcompileascompile_re

frompyrogramimportfilters
frompyrogram.errorsimportChatAdminRequired,RightForbidden,RPCError
frompyrogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup,Message

fromIneruki.function.pluginhelpersimportmember_permissions
fromIneruki.services.mongoimportmongodbasdb
fromIneruki.services.pyrogramimportpbotasapp

BTN_URL_REGE=compile_re(r"(\[([^\[]+?)\]\(buttonurl:(?:/{0,2})(.+?)(:same)?\))")


asyncdefparse_button(text:str):
"""Parsebuttonfromtext."""
markdown_note=text
prev=0
note_data=""
buttons=[]
formatchinBTN_URL_REGE.finditer(markdown_note):
#Checkifbtnurlisescaped
n_escapes=0
to_check=match.start(1)-1
whileto_check>0andmarkdown_note[to_check]=="\\":
n_escapes+=1
to_check-=1

#ifeven,notescaped->createbutton
ifn_escapes%2==0:
#createathruplewithbuttonlabel,url,andnewlinestatus
buttons.append((match.group(2),match.group(3),bool(match.group(4))))
note_data+=markdown_note[prev:match.start(1)]
prev=match.end(1)
#ifodd,escaped->movealong
else:
note_data+=markdown_note[prev:to_check]
prev=match.start(1)-1

note_data+=markdown_note[prev:]

returnnote_data,buttons


asyncdefbuild_keyboard(buttons):
"""Buildkeyboardsfromprovidedbuttons."""
keyb=[]
forbtninbuttons:
ifbtn[-1]andkeyb:
keyb[-1].append(InlineKeyboardButton(btn[0],url=btn[1]))
else:
keyb.append([InlineKeyboardButton(btn[0],url=btn[1])])

returnkeyb


classMongoDB:
"""ClassforinteractingwithBotdatabase."""

def__init__(self,collection)->None:
self.collection=db[collection]

#Insertoneentryintocollection
definsert_one(self,document):
result=self.collection.insert_one(document)
returnrepr(result.inserted_id)

#Findoneentryfromcollection
deffind_one(self,query):
result=self.collection.find_one(query)
ifresult:
returnresult
returnFalse

#Findentriesfromcollection
deffind_all(self,query=None):
ifqueryisNone:
query={}
lst=[]
fordocumentinself.collection.find(query):
lst.append(document)
returnlst

#Countentriesfromcollection
defcount(self,query=None):
ifqueryisNone:
query={}
returnself.collection.count_documents(query)

#Deleteentry/entriesfromcollection
defdelete_one(self,query):
self.collection.delete_many(query)
after_delete=self.collection.count_documents({})
returnafter_delete

#Replaceoneentryincollection
defreplace(self,query,new_data):
old=self.collection.find_one(query)
_id=old["_id"]
self.collection.replace_one({"_id":_id},new_data)
new=self.collection.find_one({"_id":_id})
returnold,new

#Updateoneentryfromcollection
defupdate(self,query,update):
result=self.collection.update_one(query,{"$set":update})
new_document=self.collection.find_one(query)
returnresult.modified_count,new_document

#Closeconnection
@staticmethod
defclose():
returnmongodb_client.close()


def__connect_first():
_=MongoDB("test")


__connect_first()


@app.on_message(filters.command("unpinall")&~filters.private)
asyncdefunpinall_message(_,m:Message):
try:
chat_id=m.chat.id
user_id=m.from_user.id
permissions=awaitmember_permissions(chat_id,user_id)
if"can_change_info"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
if"can_pin_messages"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
if"can_restrict_members"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
if"can_promote_members"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
try:
await_.unpin_all_chat_messages(m.chat.id)
awaitm.reply("Ihaveunpinnedallmessages")
exceptChatAdminRequired:
awaitm.reply("I'mnotadminhere")
exceptRightForbidden:
awaitm.reply("Idon'thaveenoughrightstounpinhere")
exceptRPCErrorasef:
awaitm.reply_text(ef)
return

exceptExceptionase:
print(e)
awaitm.reply_text(e)
return


fromthreadingimportRLock

INSERTION_LOCK=RLock()


classPins:
"""Classformanagingantichannelpinsinchats."""

#Databasenametoconnecttotopreformoperations
db_name="antichannelpin"

def__init__(self,chat_id:int)->None:
self.collection=MongoDB(self.db_name)
self.chat_id=chat_id
self.chat_info=self.__ensure_in_db()

defget_settings(self):
withINSERTION_LOCK:
returnself.chat_info

defantichannelpin_on(self):
withINSERTION_LOCK:
returnself.set_on("antichannelpin")

defcleanlinked_on(self):
withINSERTION_LOCK:
returnself.set_on("cleanlinked")

defantichannelpin_off(self):
withINSERTION_LOCK:
returnself.set_off("antichannelpin")

defcleanlinked_off(self):
withINSERTION_LOCK:
returnself.set_off("cleanlinked")

defset_on(self,atype:str):
withINSERTION_LOCK:
otype="cleanlinked"ifatype=="antichannelpin"else"antichannelpin"
returnself.collection.update(
{"_id":self.chat_id},
{atype:True,otype:False},
)

defset_off(self,atype:str):
withINSERTION_LOCK:
otype="cleanlinked"ifatype=="antichannelpin"else"antichannelpin"
returnself.collection.update(
{"_id":self.chat_id},
{atype:False,otype:False},
)

def__ensure_in_db(self):
chat_data=self.collection.find_one({"_id":self.chat_id})
ifnotchat_data:
new_data={
"_id":self.chat_id,
"antichannelpin":False,
"cleanlinked":False,
}
self.collection.insert_one(new_data)
returnnew_data
returnchat_data

#Migrateifchatidchanges!
defmigrate_chat(self,new_chat_id:int):
old_chat_db=self.collection.find_one({"_id":self.chat_id})
new_data=old_chat_db.update({"_id":new_chat_id})
self.collection.insert_one(new_data)
self.collection.delete_one({"_id":self.chat_id})

#-----StaticMethods-----
@staticmethod
defcount_chats(atype:str):
withINSERTION_LOCK:
collection=MongoDB(Pins.db_name)
returncollection.count({atype:True})

@staticmethod
deflist_chats(query:str):
withINSERTION_LOCK:
collection=MongoDB(Pins.db_name)
returncollection.find_all({query:True})

@staticmethod
defload_from_db():
withINSERTION_LOCK:
collection=MongoDB(Pins.db_name)
returncollection.findall()

@staticmethod
defrepair_db(collection):
all_data=collection.find_all()
keys={"antichannelpin":False,"cleanlinked":False}
fordatainall_data:
forkey,valinkeys.items():
try:
_=data[key]
exceptKeyError:
collection.update({"_id":data["_id"]},{key:val})


def__pre_req_pins_chats():
collection=MongoDB(Pins.db_name)
Pins.repair_db(collection)


@app.on_message(filters.command("antichannelpin")&~filters.private)
asyncdefanti_channel_pin(_,m:Message):
chat_id=m.chat.id
user_id=m.from_user.id
permissions=awaitmember_permissions(chat_id,user_id)
if"can_change_info"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
if"can_pin_messages"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
if"can_restrict_members"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
if"can_promote_members"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
pinsdb=Pins(m.chat.id)
iflen(m.text.split())==1:
status=pinsdb.get_settings()["antichannelpin"]
awaitm.reply_text(f"Antichannelpincurrently:{status}")
return

iflen(m.text.split())==2:
ifm.command[1]in("yes","on","true"):
pinsdb.antichannelpin_on()
msg="Antichannelpinturnedonforthischat"
elifm.command[1]in("no","off","false"):
pinsdb.antichannelpin_off()
msg="Antichannelpinturnedoffforthischat"
else:
awaitm.reply_text("Invalidsyntax")
return

awaitm.reply_text(msg)
return


@app.on_message(filters.command("cleanlinked")&~filters.private)
asyncdefclean_linked(_,m:Message):
chat_id=m.chat.id
user_id=m.from_user.id
permissions=awaitmember_permissions(chat_id,user_id)
if"can_change_info"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
if"can_pin_messages"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
if"can_restrict_members"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
if"can_promote_members"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
pinsdb=Pins(m.chat.id)

iflen(m.text.split())==1:
status=pinsdb.get_settings()["cleanlinked"]
awaitm.reply_text(f"Cleanlinkedpinscurrently:{status}")
return

iflen(m.text.split())==2:
ifm.command[1]in("yes","on","true"):
pinsdb.cleanlinked_on()
msg="TurnedonCleanLinked!Nowallthemessagesfromlinkedchannelwillbedeleted!"
elifm.command[1]in("no","off","false"):
pinsdb.cleanlinked_off()
msg="TurnedoffCleanLinked!Messagesfromlinkedchannelwillnotbedeleted!"
else:
awaitm.reply("Invalidsyntax")
return

awaitm.reply(msg)
return


@app.on_message(filters.command("permapin")&~filters.private)
asyncdefperma_pin(_,m:Message):
chat_id=m.chat.id
user_id=m.from_user.id
permissions=awaitmember_permissions(chat_id,user_id)
if"can_change_info"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
if"can_pin_messages"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
if"can_restrict_members"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
if"can_promote_members"notinpermissions:
awaitm.reply_text("YouDon'tHaveEnoughPermissions.")
return
ifm.reply_to_messageorlen(m.text.split())>1:
ifm.reply_to_message:
text=m.reply_to_message.text
eliflen(m.text.split())>1:
text=m.text.split(None,1)[1]
teks,button=awaitparse_button(text)
button=awaitbuild_keyboard(button)
button=InlineKeyboardMarkup(button)ifbuttonelseNone
z=awaitm.reply_text(teks,reply_markup=button)
awaitz.pin()
else:
awaitm.reply_text("Replytoamessageorentertexttopinit.")
awaitm.delete()
return


@app.on_message(filters.linked_channel)
asyncdefantichanpin_cleanlinked(c,m:Message):
try:
msg_id=m.message_id
pins_db=Pins(m.chat.id)
curr=pins_db.get_settings()
ifcurr["antichannelpin"]:
awaitc.unpin_chat_message(chat_id=m.chat.id,message_id=msg_id)
ifcurr["cleanlinked"]:
awaitc.delete_messages(m.chat.id,msg_id)
exceptChatAdminRequired:
awaitm.reply_text(
"DisabledantichannelpinasIdon'thaveenoughadminrights!",
)
pins_db.antichannelpin_off()
exceptException:
return
return
