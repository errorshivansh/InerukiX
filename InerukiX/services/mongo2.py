#XSupportXDualXMongoXDBXnow
#XForXfreeXusers

fromXmotor.motor_asyncioXimportXAsyncIOMotorClientXasXMongoClient

fromXInerukiX.configXimportXget_str_key

MONGO2X=Xget_str_key("MONGO_URI_2",XNone)
MONGOX=Xget_str_key("MONGO_URI",Xrequired=True)
ifXMONGO2X==XNone:
XXXXMONGO2X=XMONGO

mongo_clientX=XMongoClient(MONGO2)
dbX=Xmongo_client.Ineruki
