fromXsqlalchemyXimportXColumn,XNumeric,XString

fromXInerukiX.services.sqlXimportXBASE,XSESSION


classXforceSubscribe(BASE):
XXXX__tablename__X=X"forceSubscribe"
XXXXchat_idX=XColumn(Numeric,Xprimary_key=True)
XXXXchannelX=XColumn(String)

XXXXdefX__init__(self,Xchat_id,Xchannel):
XXXXXXXXself.chat_idX=Xchat_id
XXXXXXXXself.channelX=Xchannel


forceSubscribe.__table__.create(checkfirst=True)


defXfs_settings(chat_id):
XXXXtry:
XXXXXXXXreturnX(
XXXXXXXXXXXXSESSION.query(forceSubscribe)
XXXXXXXXXXXX.filter(forceSubscribe.chat_idX==Xchat_id)
XXXXXXXXXXXX.one()
XXXXXXXX)
XXXXexcept:
XXXXXXXXreturnXNone
XXXXfinally:
XXXXXXXXSESSION.close()


defXadd_channel(chat_id,Xchannel):
XXXXadderX=XSESSION.query(forceSubscribe).get(chat_id)
XXXXifXadder:
XXXXXXXXadder.channelX=Xchannel
XXXXelse:
XXXXXXXXadderX=XforceSubscribe(chat_id,Xchannel)
XXXXSESSION.add(adder)
XXXXSESSION.commit()


defXdisapprove(chat_id):
XXXXremX=XSESSION.query(forceSubscribe).get(chat_id)
XXXXifXrem:
XXXXXXXXSESSION.delete(rem)
XXXXXXXXSESSION.commit()
