importpymongo

fromIneruki.configimportget_str_key

MONGO2=get_str_key("FILTERS_MONGO",None)
MONGO=get_str_key("MONGO_URI",required=True)
ifMONGO2==None:
MONGO2=MONGO
myclient=pymongo.MongoClient(MONGO2)
mydb=myclient["Ineruki"]
mycol=mydb["CONNECTION"]


asyncdefadd_connection(group_id,user_id):
query=mycol.find_one({"_id":user_id},{"_id":0,"active_group":0})
ifqueryisnotNone:
group_ids=[]
forxinquery["group_details"]:
group_ids.append(x["group_id"])

ifgroup_idingroup_ids:
returnFalse

group_details={"group_id":group_id}

data={
"_id":user_id,
"group_details":[group_details],
"active_group":group_id,
}

ifmycol.count_documents({"_id":user_id})==0:
try:
mycol.insert_one(data)
returnTrue
except:
print("Someerroroccured!")

else:
try:
mycol.update_one(
{"_id":user_id},
{
"$push":{"group_details":group_details},
"$set":{"active_group":group_id},
},
)
returnTrue
except:
print("Someerroroccured!")


asyncdefactive_connection(user_id):

query=mycol.find_one({"_id":user_id},{"_id":0,"group_details":0})
ifquery:
group_id=query["active_group"]
ifgroup_id!=None:
returnint(group_id)
else:
returnNone
else:
returnNone


asyncdefall_connections(user_id):
query=mycol.find_one({"_id":user_id},{"_id":0,"active_group":0})
ifqueryisnotNone:
group_ids=[]
forxinquery["group_details"]:
group_ids.append(x["group_id"])
returngroup_ids
else:
returnNone


asyncdefif_active(user_id,group_id):
query=mycol.find_one({"_id":user_id},{"_id":0,"group_details":0})
ifqueryisnotNone:
ifquery["active_group"]==group_id:
returnTrue
else:
returnFalse
else:
returnFalse


asyncdefmake_active(user_id,group_id):
update=mycol.update_one({"_id":user_id},{"$set":{"active_group":group_id}})
ifupdate.modified_count==0:
returnFalse
else:
returnTrue


asyncdefmake_inactive(user_id):
update=mycol.update_one({"_id":user_id},{"$set":{"active_group":None}})
ifupdate.modified_count==0:
returnFalse
else:
returnTrue


asyncdefdelete_connection(user_id,group_id):

try:
update=mycol.update_one(
{"_id":user_id},{"$pull":{"group_details":{"group_id":group_id}}}
)
ifupdate.modified_count==0:
returnFalse
else:
query=mycol.find_one({"_id":user_id},{"_id":0})
iflen(query["group_details"])>=1:
ifquery["active_group"]==group_id:
prvs_group_id=query["group_details"][
len(query["group_details"])-1
]["group_id"]

mycol.update_one(
{"_id":user_id},{"$set":{"active_group":prvs_group_id}}
)
else:
mycol.update_one({"_id":user_id},{"$set":{"active_group":None}})
returnTrue
exceptExceptionase:
print(e)
returnFalse
