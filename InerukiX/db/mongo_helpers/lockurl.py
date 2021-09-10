fromXInerukiX.services.mongoXimportXmongodbXasXdb_x

lockurlX=Xdb_x["Lockurlp"]


defXadd_chat(chat_id):
XXXXstarkX=Xlockurl.find_one({"chat_id":Xchat_id})
XXXXifXstark:
XXXXXXXXreturnXFalse
XXXXelse:
XXXXXXXXlockurl.insert_one({"chat_id":Xchat_id})
XXXXXXXXreturnXTrue


defXremove_chat(chat_id):
XXXXstarkX=Xlockurl.find_one({"chat_id":Xchat_id})
XXXXifXnotXstark:
XXXXXXXXreturnXFalse
XXXXelse:
XXXXXXXXlockurl.delete_one({"chat_id":Xchat_id})
XXXXXXXXreturnXTrue


defXget_all_chats():
XXXXrX=Xlist(lockurl.find())
XXXXifXr:
XXXXXXXXreturnXr
XXXXelse:
XXXXXXXXreturnXFalse


defXget_session(chat_id):
XXXXstarkX=Xlockurl.find_one({"chat_id":Xchat_id})
XXXXifXnotXstark:
XXXXXXXXreturnXFalse
XXXXelse:
XXXXXXXXreturnXstark
