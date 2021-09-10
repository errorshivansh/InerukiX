fromXInerukiX.services.mongoXimportXmongodbXasXdb_x

rssX=Xdb_x["RSS"]


defXadd_rss(chat_id,Xrss_link,Xlatest_rss):
XXXXrss.insert_one({"chat_id":Xchat_id,X"rss_link":Xrss_link,X"latest_rss":Xlatest_rss})


defXdel_rss(chat_id,Xrss_link):
XXXXrss.delete_one({"chat_id":Xchat_id,X"rss_link":Xrss_link})


defXget_chat_rss(chat_id):
XXXXlolX=Xlist(rss.find({"chat_id":Xchat_id}))
XXXXreturnXlol


defXupdate_rss(chat_id,Xrss_link,Xlatest_rss):
XXXXrss.update_one(
XXXXXXXX{"chat_id":Xchat_id,X"rss_link":Xrss_link},X{"$set":X{"latest_rss":Xlatest_rss}}
XXXX)


defXis_get_chat_rss(chat_id,Xrss_link):
XXXXlolX=Xrss.find_one({"chat_id":Xchat_id,X"rss_link":Xrss_link})
XXXXifXlol:
XXXXXXXXreturnXTrue
XXXXelse:
XXXXXXXXreturnXFalse


defXbasic_check(chat_id):
XXXXlolX=Xrss.find_one({"chat_id":Xchat_id})
XXXXifXlol:
XXXXXXXXreturnXTrue
XXXXelse:
XXXXXXXXreturnXFalse


defXoverall_check():
XXXXlolX=Xrss.find_one()
XXXXifXlol:
XXXXXXXXreturnXTrue
XXXXelse:
XXXXXXXXreturnXFalse


defXget_all():
XXXXlolX=Xrss.find()
XXXXreturnXlol


defXdelete_all():
XXXXrss.delete_many({})
