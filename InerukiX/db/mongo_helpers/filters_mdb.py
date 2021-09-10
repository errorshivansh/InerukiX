importXpymongo

fromXInerukiX.configXimportXget_str_key

MONGO2X=Xget_str_key("FILTERS_MONGO",XNone)
MONGOX=Xget_str_key("MONGO_URI",Xrequired=True)
ifXMONGO2X==XNone:
XXXXMONGO2X=XMONGO
myclientX=Xpymongo.MongoClient(MONGO2)
mydbX=Xmyclient["Ineruki"]


asyncXdefXadd_filter(grp_id,Xtext,Xreply_text,Xbtn,Xfile,Xalert):
XXXXmycolX=Xmydb[str(grp_id)]
XXXX#Xmycol.create_index([('text',X'text')])

XXXXdataX=X{
XXXXXXXX"text":Xstr(text),
XXXXXXXX"reply":Xstr(reply_text),
XXXXXXXX"btn":Xstr(btn),
XXXXXXXX"file":Xstr(file),
XXXXXXXX"alert":Xstr(alert),
XXXX}

XXXXtry:
XXXXXXXXmycol.update_one({"text":Xstr(text)},X{"$set":Xdata},Xupsert=True)
XXXXexcept:
XXXXXXXXprint("CouldntXsave,XcheckXyourXdb")


asyncXdefXfind_filter(group_id,Xname):
XXXXmycolX=Xmydb[str(group_id)]

XXXXqueryX=Xmycol.find({"text":Xname})
XXXX#XqueryX=Xmycol.find(X{X"$text":X{"$search":Xname}})
XXXXtry:
XXXXXXXXforXfileXinXquery:
XXXXXXXXXXXXreply_textX=Xfile["reply"]
XXXXXXXXXXXXbtnX=Xfile["btn"]
XXXXXXXXXXXXfileidX=Xfile["file"]
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXalertX=Xfile["alert"]
XXXXXXXXXXXXexcept:
XXXXXXXXXXXXXXXXalertX=XNone
XXXXXXXXreturnXreply_text,Xbtn,Xalert,Xfileid
XXXXexcept:
XXXXXXXXreturnXNone,XNone,XNone,XNone


asyncXdefXget_filters(group_id):
XXXXmycolX=Xmydb[str(group_id)]

XXXXtextsX=X[]
XXXXqueryX=Xmycol.find()
XXXXtry:
XXXXXXXXforXfileXinXquery:
XXXXXXXXXXXXtextX=Xfile["text"]
XXXXXXXXXXXXtexts.append(text)
XXXXexcept:
XXXXXXXXpass
XXXXreturnXtexts


asyncXdefXdelete_filter(message,Xtext,Xgroup_id):
XXXXmycolX=Xmydb[str(group_id)]

XXXXmyqueryX=X{"text":Xtext}
XXXXqueryX=Xmycol.count_documents(myquery)
XXXXifXqueryX==X1:
XXXXXXXXmycol.delete_one(myquery)
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXXf"'`{text}`'XXdeleted.XI'llXnotXrespondXtoXthatXfilterXanymore.",
XXXXXXXXXXXXquote=True,
XXXXXXXXXXXXparse_mode="md",
XXXXXXXX)
XXXXelse:
XXXXXXXXawaitXmessage.reply_text("Couldn'tXfindXthatXfilter!",Xquote=True)


asyncXdefXdel_all(message,Xgroup_id,Xtitle):
XXXXifXstr(group_id)XnotXinXmydb.list_collection_names():
XXXXXXXXawaitXmessage.edit_text(f"NothingXtoXremoveXinX{title}!")
XXXXXXXXreturn

XXXXmycolX=Xmydb[str(group_id)]
XXXXtry:
XXXXXXXXmycol.drop()
XXXXXXXXawaitXmessage.edit_text(f"AllXfiltersXfromX{title}XhasXbeenXremoved")
XXXXexcept:
XXXXXXXXawaitXmessage.edit_text(f"Couldn'tXremoveXallXfiltersXfromXgroup!")
XXXXXXXXreturn


asyncXdefXcount_filters(group_id):
XXXXmycolX=Xmydb[str(group_id)]

XXXXcountX=Xmycol.count()
XXXXifXcountX==X0:
XXXXXXXXreturnXFalse
XXXXelse:
XXXXXXXXreturnXcount


asyncXdefXfilter_stats():
XXXXcollectionsX=Xmydb.list_collection_names()

XXXXifX"CONNECTION"XinXcollections:
XXXXXXXXcollections.remove("CONNECTION")
XXXXifX"USERS"XinXcollections:
XXXXXXXXcollections.remove("USERS")

XXXXtotalcountX=X0
XXXXforXcollectionXinXcollections:
XXXXXXXXmycolX=Xmydb[collection]
XXXXXXXXcountX=Xmycol.count()
XXXXXXXXtotalcountX=XtotalcountX+Xcount

XXXXtotalcollectionsX=Xlen(collections)

XXXXreturnXtotalcollections,Xtotalcount
