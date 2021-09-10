importXpymongo

fromXInerukiX.configXimportXget_str_key

MONGO2X=Xget_str_key("FILTERS_MONGO",XNone)
MONGOX=Xget_str_key("MONGO_URI",Xrequired=True)
ifXMONGO2X==XNone:
XXXXMONGO2X=XMONGO
myclientX=Xpymongo.MongoClient(MONGO2)
mydbX=Xmyclient["Ineruki"]
mycolX=Xmydb["CONNECTION"]


asyncXdefXadd_connection(group_id,Xuser_id):
XXXXqueryX=Xmycol.find_one({"_id":Xuser_id},X{"_id":X0,X"active_group":X0})
XXXXifXqueryXisXnotXNone:
XXXXXXXXgroup_idsX=X[]
XXXXXXXXforXxXinXquery["group_details"]:
XXXXXXXXXXXXgroup_ids.append(x["group_id"])

XXXXXXXXifXgroup_idXinXgroup_ids:
XXXXXXXXXXXXreturnXFalse

XXXXgroup_detailsX=X{"group_id":Xgroup_id}

XXXXdataX=X{
XXXXXXXX"_id":Xuser_id,
XXXXXXXX"group_details":X[group_details],
XXXXXXXX"active_group":Xgroup_id,
XXXX}

XXXXifXmycol.count_documents({"_id":Xuser_id})X==X0:
XXXXXXXXtry:
XXXXXXXXXXXXmycol.insert_one(data)
XXXXXXXXXXXXreturnXTrue
XXXXXXXXexcept:
XXXXXXXXXXXXprint("SomeXerrorXoccured!")

XXXXelse:
XXXXXXXXtry:
XXXXXXXXXXXXmycol.update_one(
XXXXXXXXXXXXXXXX{"_id":Xuser_id},
XXXXXXXXXXXXXXXX{
XXXXXXXXXXXXXXXXXXXX"$push":X{"group_details":Xgroup_details},
XXXXXXXXXXXXXXXXXXXX"$set":X{"active_group":Xgroup_id},
XXXXXXXXXXXXXXXX},
XXXXXXXXXXXX)
XXXXXXXXXXXXreturnXTrue
XXXXXXXXexcept:
XXXXXXXXXXXXprint("SomeXerrorXoccured!")


asyncXdefXactive_connection(user_id):

XXXXqueryX=Xmycol.find_one({"_id":Xuser_id},X{"_id":X0,X"group_details":X0})
XXXXifXquery:
XXXXXXXXgroup_idX=Xquery["active_group"]
XXXXXXXXifXgroup_idX!=XNone:
XXXXXXXXXXXXreturnXint(group_id)
XXXXXXXXelse:
XXXXXXXXXXXXreturnXNone
XXXXelse:
XXXXXXXXreturnXNone


asyncXdefXall_connections(user_id):
XXXXqueryX=Xmycol.find_one({"_id":Xuser_id},X{"_id":X0,X"active_group":X0})
XXXXifXqueryXisXnotXNone:
XXXXXXXXgroup_idsX=X[]
XXXXXXXXforXxXinXquery["group_details"]:
XXXXXXXXXXXXgroup_ids.append(x["group_id"])
XXXXXXXXreturnXgroup_ids
XXXXelse:
XXXXXXXXreturnXNone


asyncXdefXif_active(user_id,Xgroup_id):
XXXXqueryX=Xmycol.find_one({"_id":Xuser_id},X{"_id":X0,X"group_details":X0})
XXXXifXqueryXisXnotXNone:
XXXXXXXXifXquery["active_group"]X==Xgroup_id:
XXXXXXXXXXXXreturnXTrue
XXXXXXXXelse:
XXXXXXXXXXXXreturnXFalse
XXXXelse:
XXXXXXXXreturnXFalse


asyncXdefXmake_active(user_id,Xgroup_id):
XXXXupdateX=Xmycol.update_one({"_id":Xuser_id},X{"$set":X{"active_group":Xgroup_id}})
XXXXifXupdate.modified_countX==X0:
XXXXXXXXreturnXFalse
XXXXelse:
XXXXXXXXreturnXTrue


asyncXdefXmake_inactive(user_id):
XXXXupdateX=Xmycol.update_one({"_id":Xuser_id},X{"$set":X{"active_group":XNone}})
XXXXifXupdate.modified_countX==X0:
XXXXXXXXreturnXFalse
XXXXelse:
XXXXXXXXreturnXTrue


asyncXdefXdelete_connection(user_id,Xgroup_id):

XXXXtry:
XXXXXXXXupdateX=Xmycol.update_one(
XXXXXXXXXXXX{"_id":Xuser_id},X{"$pull":X{"group_details":X{"group_id":Xgroup_id}}}
XXXXXXXX)
XXXXXXXXifXupdate.modified_countX==X0:
XXXXXXXXXXXXreturnXFalse
XXXXXXXXelse:
XXXXXXXXXXXXqueryX=Xmycol.find_one({"_id":Xuser_id},X{"_id":X0})
XXXXXXXXXXXXifXlen(query["group_details"])X>=X1:
XXXXXXXXXXXXXXXXifXquery["active_group"]X==Xgroup_id:
XXXXXXXXXXXXXXXXXXXXprvs_group_idX=Xquery["group_details"][
XXXXXXXXXXXXXXXXXXXXXXXXlen(query["group_details"])X-X1
XXXXXXXXXXXXXXXXXXXX]["group_id"]

XXXXXXXXXXXXXXXXXXXXmycol.update_one(
XXXXXXXXXXXXXXXXXXXXXXXX{"_id":Xuser_id},X{"$set":X{"active_group":Xprvs_group_id}}
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXmycol.update_one({"_id":Xuser_id},X{"$set":X{"active_group":XNone}})
XXXXXXXXXXXXreturnXTrue
XXXXexceptXExceptionXasXe:
XXXXXXXXprint(e)
XXXXXXXXreturnXFalse
