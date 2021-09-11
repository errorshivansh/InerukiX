fromIneruki.services.mongoimportmongodbasdb_x

lockurl=db_x["Lockurlp"]


defadd_chat(chat_id):
stark=lockurl.find_one({"chat_id":chat_id})
ifstark:
returnFalse
else:
lockurl.insert_one({"chat_id":chat_id})
returnTrue


defremove_chat(chat_id):
stark=lockurl.find_one({"chat_id":chat_id})
ifnotstark:
returnFalse
else:
lockurl.delete_one({"chat_id":chat_id})
returnTrue


defget_all_chats():
r=list(lockurl.find())
ifr:
returnr
else:
returnFalse


defget_session(chat_id):
stark=lockurl.find_one({"chat_id":chat_id})
ifnotstark:
returnFalse
else:
returnstark
