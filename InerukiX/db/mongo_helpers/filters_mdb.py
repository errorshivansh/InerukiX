importpymongo

fromIneruki.configimportget_str_key

MONGO2=get_str_key("FILTERS_MONGO",None)
MONGO=get_str_key("MONGO_URI",required=True)
ifMONGO2==None:
MONGO2=MONGO
myclient=pymongo.MongoClient(MONGO2)
mydb=myclient["Ineruki"]


asyncdefadd_filter(grp_id,text,reply_text,btn,file,alert):
mycol=mydb[str(grp_id)]
#mycol.create_index([('text','text')])

data={
"text":str(text),
"reply":str(reply_text),
"btn":str(btn),
"file":str(file),
"alert":str(alert),
}

try:
mycol.update_one({"text":str(text)},{"$set":data},upsert=True)
except:
print("Couldntsave,checkyourdb")


asyncdeffind_filter(group_id,name):
mycol=mydb[str(group_id)]

query=mycol.find({"text":name})
#query=mycol.find({"$text":{"$search":name}})
try:
forfileinquery:
reply_text=file["reply"]
btn=file["btn"]
fileid=file["file"]
try:
alert=file["alert"]
except:
alert=None
returnreply_text,btn,alert,fileid
except:
returnNone,None,None,None


asyncdefget_filters(group_id):
mycol=mydb[str(group_id)]

texts=[]
query=mycol.find()
try:
forfileinquery:
text=file["text"]
texts.append(text)
except:
pass
returntexts


asyncdefdelete_filter(message,text,group_id):
mycol=mydb[str(group_id)]

myquery={"text":text}
query=mycol.count_documents(myquery)
ifquery==1:
mycol.delete_one(myquery)
awaitmessage.reply_text(
f"'`{text}`'deleted.I'llnotrespondtothatfilteranymore.",
quote=True,
parse_mode="md",
)
else:
awaitmessage.reply_text("Couldn'tfindthatfilter!",quote=True)


asyncdefdel_all(message,group_id,title):
ifstr(group_id)notinmydb.list_collection_names():
awaitmessage.edit_text(f"Nothingtoremovein{title}!")
return

mycol=mydb[str(group_id)]
try:
mycol.drop()
awaitmessage.edit_text(f"Allfiltersfrom{title}hasbeenremoved")
except:
awaitmessage.edit_text(f"Couldn'tremoveallfiltersfromgroup!")
return


asyncdefcount_filters(group_id):
mycol=mydb[str(group_id)]

count=mycol.count()
ifcount==0:
returnFalse
else:
returncount


asyncdeffilter_stats():
collections=mydb.list_collection_names()

if"CONNECTION"incollections:
collections.remove("CONNECTION")
if"USERS"incollections:
collections.remove("USERS")

totalcount=0
forcollectionincollections:
mycol=mydb[collection]
count=mycol.count()
totalcount=totalcount+count

totalcollections=len(collections)

returntotalcollections,totalcount
