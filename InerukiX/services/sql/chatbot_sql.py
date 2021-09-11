importthreading

fromsqlalchemyimportColumn,String

fromIneruki.services.sqlimportBASE,SESSION


classChatbotChats(BASE):
__tablename__="chatbot_chats"
chat_id=Column(String(14),primary_key=True)
ses_id=Column(String(70))
expires=Column(String(15))

def__init__(self,chat_id,ses_id,expires):
self.chat_id=chat_id
self.ses_id=ses_id
self.expires=expires


ChatbotChats.__table__.create(checkfirst=True)

INSERTION_LOCK=threading.RLock()


defis_chat(chat_id):
try:
chat=SESSION.query(ChatbotChats).get(str(chat_id))
ifchat:
returnTrue
returnFalse
finally:
SESSION.close()


defset_ses(chat_id,ses_id,expires):
withINSERTION_LOCK:
autochat=SESSION.query(ChatbotChats).get(str(chat_id))
ifnotautochat:
autochat=ChatbotChats(str(chat_id),str(ses_id),str(expires))
else:
autochat.ses_id=str(ses_id)
autochat.expires=str(expires)

SESSION.add(autochat)
SESSION.commit()


defget_ses(chat_id):
autochat=SESSION.query(ChatbotChats).get(str(chat_id))
sesh=""
exp=""
ifautochat:
sesh=str(autochat.ses_id)
exp=str(autochat.expires)

SESSION.close()
returnsesh,exp


defrem_chat(chat_id):
withINSERTION_LOCK:
autochat=SESSION.query(ChatbotChats).get(str(chat_id))
ifautochat:
SESSION.delete(autochat)

SESSION.commit()


defget_all_chats():
try:
returnSESSION.query(ChatbotChats.chat_id).all()
finally:
SESSION.close()
