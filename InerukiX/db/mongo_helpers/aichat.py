fromXInerukiX.services.mongoXimportXmongodbXasXdb_x

lydiaX=Xdb_x["CAHTBOT"]


defXadd_chat(chat_id):
XXXXstarkX=Xlydia.find_one({"chat_id":Xchat_id})
XXXXifXstark:
XXXXXXXXreturnXFalse
XXXXelse:
XXXXXXXXlydia.insert_one({"chat_id":Xchat_id})
XXXXXXXXreturnXTrue


defXremove_chat(chat_id):
XXXXstarkX=Xlydia.find_one({"chat_id":Xchat_id})
XXXXifXnotXstark:
XXXXXXXXreturnXFalse
XXXXelse:
XXXXXXXXlydia.delete_one({"chat_id":Xchat_id})
XXXXXXXXreturnXTrue


defXget_all_chats():
XXXXrX=Xlist(lydia.find())
XXXXifXr:
XXXXXXXXreturnXr
XXXXelse:
XXXXXXXXreturnXFalse


defXget_session(chat_id):
XXXXstarkX=Xlydia.find_one({"chat_id":Xchat_id})
XXXXifXnotXstark:
XXXXXXXXreturnXFalse
XXXXelse:
XXXXXXXXreturnXstark
