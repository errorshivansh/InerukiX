fromsqlalchemyimportColumn,LargeBinary,Numeric,String,UnicodeText

fromIneruki.services.sqlimportBASE,SESSION


classFilters(BASE):
__tablename__="cust_filters"
chat_id=Column(String(14),primary_key=True)
keyword=Column(UnicodeText,primary_key=True)
reply=Column(UnicodeText)
snip_type=Column(Numeric)
media_id=Column(UnicodeText)
media_access_hash=Column(UnicodeText)
media_file_reference=Column(LargeBinary)

def__init__(
self,
chat_id,
keyword,
reply,
snip_type,
media_id=None,
media_access_hash=None,
media_file_reference=None,
):
self.chat_id=chat_id
self.keyword=keyword
self.reply=reply
self.snip_type=snip_type
self.media_id=media_id
self.media_access_hash=media_access_hash
self.media_file_reference=media_file_reference


Filters.__table__.create(checkfirst=True)


defget_filter(chat_id,keyword):
try:
returnSESSION.query(Filters).get((str(chat_id),keyword))
exceptBaseException:
returnNone
finally:
SESSION.close()


defget_all_filters(chat_id):
try:
returnSESSION.query(Filters).filter(Filters.chat_id==str(chat_id)).all()
exceptBaseException:
returnNone
finally:
SESSION.close()


defadd_filter(
chat_id,
keyword,
reply,
snip_type,
media_id,
media_access_hash,
media_file_reference,
):
adder=SESSION.query(Filters).get((str(chat_id),keyword))
ifadder:
adder.reply=reply
adder.snip_type=snip_type
adder.media_id=media_id
adder.media_access_hash=media_access_hash
adder.media_file_reference=media_file_reference
else:
adder=Filters(
chat_id,
keyword,
reply,
snip_type,
media_id,
media_access_hash,
media_file_reference,
)
SESSION.add(adder)
SESSION.commit()


defremove_filter(chat_id,keyword):
saved_filter=SESSION.query(Filters).get((str(chat_id),keyword))
ifsaved_filter:
SESSION.delete(saved_filter)
SESSION.commit()


defremove_all_filters(chat_id):
saved_filter=SESSION.query(Filters).filter(Filters.chat_id==str(chat_id))
ifsaved_filter:
saved_filter.delete()
SESSION.commit()
