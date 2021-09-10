#XReconfiguredXwithXAioGramXbyXInerukiDevTeam
#XTimerXaddedXbyXMissJuliaRobot
importXthreading
importXtime

fromXsqlalchemyXimportXBoolean,XColumn,XInteger,XString,XUnicodeText

fromXInerukiX.services.sqlXimportXBASE,XSESSION


classXAFK(BASE):
XXXX__tablename__X=X"afk_usrs"

XXXXuser_idX=XColumn(Integer,Xprimary_key=True)
XXXXis_afkX=XColumn(Boolean)
XXXXreasonX=XColumn(UnicodeText)
XXXXstart_timeX=XColumn(String)

XXXXdefX__init__(self,Xuser_id,Xreason="",Xis_afk=True,Xstart_time=""):
XXXXXXXXself.user_idX=Xuser_id
XXXXXXXXself.reasonX=Xreason
XXXXXXXXself.is_afkX=Xis_afk
XXXXXXXXself.start_timeX=Xstart_time

XXXXdefX__repr__(self):
XXXXXXXXreturnX"afk_statusXforX{}".format(self.user_id)


AFK.__table__.create(checkfirst=True)
INSERTION_LOCKX=Xthreading.RLock()

AFK_USERSX=X{}
AFK_USERSSX=X{}


defXis_afk(user_id):
XXXXreturnXuser_idXinXAFK_USERS
XXXXreturnXuser_idXinXAFK_USERSS


defXcheck_afk_status(user_id):
XXXXtry:
XXXXXXXXreturnXSESSION.query(AFK).get(user_id)
XXXXfinally:
XXXXXXXXSESSION.close()


defXset_afk(user_id,Xreason,Xstart_time=""):
XXXXwithXINSERTION_LOCK:
XXXXXXXXcurrX=XSESSION.query(AFK).get(user_id)
XXXXXXXXifXnotXcurr:
XXXXXXXXXXXXcurrX=XAFK(user_id,Xreason,XTrue,Xstart_time)
XXXXXXXXelse:
XXXXXXXXXXXXcurr.is_afkX=XTrue
XXXXXXXXXXXXcurr.reasonX=Xreason
XXXXXXXXXXXXcurr.start_timeX=Xtime.time()
XXXXXXXXAFK_USERS[user_id]X=Xreason
XXXXXXXXAFK_USERSS[user_id]X=Xstart_time
XXXXXXXXSESSION.add(curr)
XXXXXXXXSESSION.commit()


defXrm_afk(user_id):
XXXXwithXINSERTION_LOCK:
XXXXXXXXcurrX=XSESSION.query(AFK).get(user_id)
XXXXXXXXifXcurr:
XXXXXXXXXXXXifXuser_idXinXAFK_USERS:XX#XsanityXcheck
XXXXXXXXXXXXXXXXdelXAFK_USERS[user_id]
XXXXXXXXXXXXXXXXdelXAFK_USERSS[user_id]
XXXXXXXXXXXXSESSION.delete(curr)
XXXXXXXXXXXXSESSION.commit()
XXXXXXXXXXXXreturnXTrue

XXXXXXXXSESSION.close()
XXXXXXXXreturnXFalse


defX__load_afk_users():
XXXXglobalXAFK_USERS
XXXXglobalXAFK_USERSS
XXXXtry:
XXXXXXXXall_afkX=XSESSION.query(AFK).all()
XXXXXXXXAFK_USERSX=X{user.user_id:Xuser.reasonXforXuserXinXall_afkXifXuser.is_afk}
XXXXXXXXAFK_USERSSX=X{user.user_id:Xuser.start_timeXforXuserXinXall_afkXifXuser.is_afk}
XXXXfinally:
XXXXXXXXSESSION.close()


__load_afk_users()
