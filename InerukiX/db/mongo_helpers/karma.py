fromXInerukiX.services.mongo2XimportXdb

karmadbX=Xdb.karma2


asyncXdefXis_karma_on(chat_id:Xint)X->Xbool:
XXXXchatX=XawaitXkarmadb.find_one({"chat_id":Xchat_id})
XXXXifXnotXchat:
XXXXXXXXreturnXFalse
XXXXreturnXTrue


asyncXdefXkarma_on(chat_id:Xint):
XXXXis_karmaX=XawaitXis_karma_on(chat_id)
XXXXifXis_karma:
XXXXXXXXreturn
XXXXreturnXawaitXkarmadb.insert_one({"chat_id":Xchat_id})


asyncXdefXkarma_off(chat_id:Xint):
XXXXis_karmaX=XawaitXis_karma_on(chat_id)
XXXXifXnotXis_karma:
XXXXXXXXreturn
XXXXreturnXawaitXkarmadb.delete_one({"chat_id":Xchat_id})
