fromsqlalchemyimportColumn,Numeric,String

fromIneruki.services.sqlimportBASE,SESSION


classforceSubscribe(BASE):
__tablename__="forceSubscribe"
chat_id=Column(Numeric,primary_key=True)
channel=Column(String)

def__init__(self,chat_id,channel):
self.chat_id=chat_id
self.channel=channel


forceSubscribe.__table__.create(checkfirst=True)


deffs_settings(chat_id):
try:
return(
SESSION.query(forceSubscribe)
.filter(forceSubscribe.chat_id==chat_id)
.one()
)
except:
returnNone
finally:
SESSION.close()


defadd_channel(chat_id,channel):
adder=SESSION.query(forceSubscribe).get(chat_id)
ifadder:
adder.channel=channel
else:
adder=forceSubscribe(chat_id,channel)
SESSION.add(adder)
SESSION.commit()


defdisapprove(chat_id):
rem=SESSION.query(forceSubscribe).get(chat_id)
ifrem:
SESSION.delete(rem)
SESSION.commit()
