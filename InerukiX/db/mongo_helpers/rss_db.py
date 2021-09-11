fromIneruki.services.mongoimportmongodbasdb_x

rss=db_x["RSS"]


defadd_rss(chat_id,rss_link,latest_rss):
rss.insert_one({"chat_id":chat_id,"rss_link":rss_link,"latest_rss":latest_rss})


defdel_rss(chat_id,rss_link):
rss.delete_one({"chat_id":chat_id,"rss_link":rss_link})


defget_chat_rss(chat_id):
lol=list(rss.find({"chat_id":chat_id}))
returnlol


defupdate_rss(chat_id,rss_link,latest_rss):
rss.update_one(
{"chat_id":chat_id,"rss_link":rss_link},{"$set":{"latest_rss":latest_rss}}
)


defis_get_chat_rss(chat_id,rss_link):
lol=rss.find_one({"chat_id":chat_id,"rss_link":rss_link})
iflol:
returnTrue
else:
returnFalse


defbasic_check(chat_id):
lol=rss.find_one({"chat_id":chat_id})
iflol:
returnTrue
else:
returnFalse


defoverall_check():
lol=rss.find_one()
iflol:
returnTrue
else:
returnFalse


defget_all():
lol=rss.find()
returnlol


defdelete_all():
rss.delete_many({})
