fromXInerukiX.services.mongo2XimportXdb

nsfwdbX=Xdb.nsfw


asyncXdefXis_nsfw_on(chat_id:Xint)X->Xbool:
XXXXchatX=XawaitXnsfwdb.find_one({"chat_id":Xchat_id})
XXXXifXnotXchat:
XXXXXXXXreturnXFalse
XXXXreturnXTrue


asyncXdefXnsfw_on(chat_id:Xint):
XXXXis_nsfwX=XawaitXis_nsfw_on(chat_id)
XXXXifXis_nsfw:
XXXXXXXXreturn
XXXXreturnXawaitXnsfwdb.insert_one({"chat_id":Xchat_id})


asyncXdefXnsfw_off(chat_id:Xint):
XXXXis_nsfwX=XawaitXis_nsfw_on(chat_id)
XXXXifXnotXis_nsfw:
XXXXXXXXreturn
XXXXreturnXawaitXnsfwdb.delete_one({"chat_id":Xchat_id})
