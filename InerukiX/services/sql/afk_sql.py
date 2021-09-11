#ReconfiguredwithAioGrambyInerukiDevTeam
#TimeraddedbyMissJuliaRobot
importthreading
importtime

fromsqlalchemyimportBoolean,Column,Integer,String,UnicodeText

fromIneruki.services.sqlimportBASE,SESSION


classAFK(BASE):
__tablename__="afk_usrs"

user_id=Column(Integer,primary_key=True)
is_afk=Column(Boolean)
reason=Column(UnicodeText)
start_time=Column(String)

def__init__(self,user_id,reason="",is_afk=True,start_time=""):
self.user_id=user_id
self.reason=reason
self.is_afk=is_afk
self.start_time=start_time

def__repr__(self):
return"afk_statusfor{}".format(self.user_id)


AFK.__table__.create(checkfirst=True)
INSERTION_LOCK=threading.RLock()

AFK_USERS={}
AFK_USERSS={}


defis_afk(user_id):
returnuser_idinAFK_USERS
returnuser_idinAFK_USERSS


defcheck_afk_status(user_id):
try:
returnSESSION.query(AFK).get(user_id)
finally:
SESSION.close()


defset_afk(user_id,reason,start_time=""):
withINSERTION_LOCK:
curr=SESSION.query(AFK).get(user_id)
ifnotcurr:
curr=AFK(user_id,reason,True,start_time)
else:
curr.is_afk=True
curr.reason=reason
curr.start_time=time.time()
AFK_USERS[user_id]=reason
AFK_USERSS[user_id]=start_time
SESSION.add(curr)
SESSION.commit()


defrm_afk(user_id):
withINSERTION_LOCK:
curr=SESSION.query(AFK).get(user_id)
ifcurr:
ifuser_idinAFK_USERS:#sanitycheck
delAFK_USERS[user_id]
delAFK_USERSS[user_id]
SESSION.delete(curr)
SESSION.commit()
returnTrue

SESSION.close()
returnFalse


def__load_afk_users():
globalAFK_USERS
globalAFK_USERSS
try:
all_afk=SESSION.query(AFK).all()
AFK_USERS={user.user_id:user.reasonforuserinall_afkifuser.is_afk}
AFK_USERSS={user.user_id:user.start_timeforuserinall_afkifuser.is_afk}
finally:
SESSION.close()


__load_afk_users()
