fromIneruki.services.mongo2importdb

karmadb=db.karma2


asyncdefis_karma_on(chat_id:int)->bool:
chat=awaitkarmadb.find_one({"chat_id":chat_id})
ifnotchat:
returnFalse
returnTrue


asyncdefkarma_on(chat_id:int):
is_karma=awaitis_karma_on(chat_id)
ifis_karma:
return
returnawaitkarmadb.insert_one({"chat_id":chat_id})


asyncdefkarma_off(chat_id:int):
is_karma=awaitis_karma_on(chat_id)
ifnotis_karma:
return
returnawaitkarmadb.delete_one({"chat_id":chat_id})
