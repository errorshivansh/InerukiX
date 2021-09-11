#SupportDualMongoDBnow
#Forfreeusers

frommotor.motor_asyncioimportAsyncIOMotorClientasMongoClient

fromIneruki.configimportget_str_key

MONGO2=get_str_key("MONGO_URI_2",None)
MONGO=get_str_key("MONGO_URI",required=True)
ifMONGO2==None:
MONGO2=MONGO

mongo_client=MongoClient(MONGO2)
db=mongo_client.Ineruki
