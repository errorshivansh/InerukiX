fromIneruki.services.mongo2importdb

nsfwdb=db.nsfw


asyncdefis_nsfw_on(chat_id:int)->bool:
chat=awaitnsfwdb.find_one({"chat_id":chat_id})
ifnotchat:
returnFalse
returnTrue


asyncdefnsfw_on(chat_id:int):
is_nsfw=awaitis_nsfw_on(chat_id)
ifis_nsfw:
return
returnawaitnsfwdb.insert_one({"chat_id":chat_id})


asyncdefnsfw_off(chat_id:int):
is_nsfw=awaitis_nsfw_on(chat_id)
ifnotis_nsfw:
return
returnawaitnsfwdb.delete_one({"chat_id":chat_id})
