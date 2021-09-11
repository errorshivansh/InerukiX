importpymongo

fromIneruki.configimportget_str_key

MONGO2=get_str_key("FILTERS_MONGO",None)
MONGO=get_str_key("MONGO_URI",required=True)
ifMONGO2==None:
MONGO2=MONGO
myclient=pymongo.MongoClient(MONGO2)
mydb=myclient["Ineruki"]
mycol=mydb["USERS"]


asyncdefadd_user(id,username,name,dcid):
data={"_id":id,"username":username,"name":name,"dc_id":dcid}
try:
mycol.update_one({"_id":id},{"$set":data},upsert=True)
except:
pass


asyncdefall_users():
count=mycol.count()
returncount


asyncdeffind_user(id):
query=mycol.find({"_id":id})

try:
forfileinquery:
name=file["name"]
username=file["username"]
dc_id=file["dc_id"]
returnname,username,dc_id
except:
returnNone,None,None
