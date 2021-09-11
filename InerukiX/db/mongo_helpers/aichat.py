fromIneruki.services.mongoimportmongodbasdb_x

lydia=db_x["CAHTBOT"]


defadd_chat(chat_id):
stark=lydia.find_one({"chat_id":chat_id})
ifstark:
returnFalse
else:
lydia.insert_one({"chat_id":chat_id})
returnTrue


defremove_chat(chat_id):
stark=lydia.find_one({"chat_id":chat_id})
ifnotstark:
returnFalse
else:
lydia.delete_one({"chat_id":chat_id})
returnTrue


defget_all_chats():
r=list(lydia.find())
ifr:
returnr
else:
returnFalse


defget_session(chat_id):
stark=lydia.find_one({"chat_id":chat_id})
ifnotstark:
returnFalse
else:
returnstark
