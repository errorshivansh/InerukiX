importXpymongo

fromXInerukiX.configXimportXget_str_key

MONGO2X=Xget_str_key("FILTERS_MONGO",XNone)
MONGOX=Xget_str_key("MONGO_URI",Xrequired=True)
ifXMONGO2X==XNone:
XXXXMONGO2X=XMONGO
myclientX=Xpymongo.MongoClient(MONGO2)
mydbX=Xmyclient["Ineruki"]
mycolX=Xmydb["USERS"]


asyncXdefXadd_user(id,Xusername,Xname,Xdcid):
XXXXdataX=X{"_id":Xid,X"username":Xusername,X"name":Xname,X"dc_id":Xdcid}
XXXXtry:
XXXXXXXXmycol.update_one({"_id":Xid},X{"$set":Xdata},Xupsert=True)
XXXXexcept:
XXXXXXXXpass


asyncXdefXall_users():
XXXXcountX=Xmycol.count()
XXXXreturnXcount


asyncXdefXfind_user(id):
XXXXqueryX=Xmycol.find({"_id":Xid})

XXXXtry:
XXXXXXXXforXfileXinXquery:
XXXXXXXXXXXXnameX=Xfile["name"]
XXXXXXXXXXXXusernameX=Xfile["username"]
XXXXXXXXXXXXdc_idX=Xfile["dc_id"]
XXXXXXXXreturnXname,Xusername,Xdc_id
XXXXexcept:
XXXXXXXXreturnXNone,XNone,XNone
