fromsqlalchemyimportBigInteger,Boolean,Column,String,UnicodeText

fromIneruki.services.sqlimportBASE,SESSION


classGoodbye(BASE):
__tablename__="goodbye"
chat_id=Column(String(14),primary_key=True)
custom_goodbye_message=Column(UnicodeText)
media_file_id=Column(UnicodeText)
should_clean_goodbye=Column(Boolean,default=False)
previous_goodbye=Column(BigInteger)

def__init__(
self,
chat_id,
custom_goodbye_message,
should_clean_goodbye,
previous_goodbye,
media_file_id=None,
):
self.chat_id=chat_id
self.custom_goodbye_message=custom_goodbye_message
self.media_file_id=media_file_id
self.should_clean_goodbye=should_clean_goodbye
self.previous_goodbye=previous_goodbye


Goodbye.__table__.create(checkfirst=True)


defget_current_goodbye_settings(chat_id):
try:
returnSESSION.query(Goodbye).filter(Goodbye.chat_id==str(chat_id)).one()
except:
returnNone
finally:
SESSION.close()


defadd_goodbye_setting(
chat_id,
custom_goodbye_message,
should_clean_goodbye,
previous_goodbye,
media_file_id,
):
#adder=SESSION.query(Goodbye).get(chat_id)
adder=Goodbye(
chat_id,
custom_goodbye_message,
should_clean_goodbye,
previous_goodbye,
media_file_id,
)
SESSION.add(adder)
SESSION.commit()


defrm_goodbye_setting(chat_id):
rem=SESSION.query(Goodbye).get(str(chat_id))
ifrem:
SESSION.delete(rem)
SESSION.commit()


defupdate_previous_goodbye(chat_id,previous_goodbye):
row=SESSION.query(Goodbye).get(str(chat_id))
row.previous_goodbye=previous_goodbye
#committhechangestotheDB
SESSION.commit()
