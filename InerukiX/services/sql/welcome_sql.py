fromXsqlalchemyXimportXBigInteger,XBoolean,XColumn,XString,XUnicodeText

fromXInerukiX.services.sqlXimportXBASE,XSESSION


classXGoodbye(BASE):
XXXX__tablename__X=X"goodbye"
XXXXchat_idX=XColumn(String(14),Xprimary_key=True)
XXXXcustom_goodbye_messageX=XColumn(UnicodeText)
XXXXmedia_file_idX=XColumn(UnicodeText)
XXXXshould_clean_goodbyeX=XColumn(Boolean,Xdefault=False)
XXXXprevious_goodbyeX=XColumn(BigInteger)

XXXXdefX__init__(
XXXXXXXXself,
XXXXXXXXchat_id,
XXXXXXXXcustom_goodbye_message,
XXXXXXXXshould_clean_goodbye,
XXXXXXXXprevious_goodbye,
XXXXXXXXmedia_file_id=None,
XXXX):
XXXXXXXXself.chat_idX=Xchat_id
XXXXXXXXself.custom_goodbye_messageX=Xcustom_goodbye_message
XXXXXXXXself.media_file_idX=Xmedia_file_id
XXXXXXXXself.should_clean_goodbyeX=Xshould_clean_goodbye
XXXXXXXXself.previous_goodbyeX=Xprevious_goodbye


Goodbye.__table__.create(checkfirst=True)


defXget_current_goodbye_settings(chat_id):
XXXXtry:
XXXXXXXXreturnXSESSION.query(Goodbye).filter(Goodbye.chat_idX==Xstr(chat_id)).one()
XXXXexcept:
XXXXXXXXreturnXNone
XXXXfinally:
XXXXXXXXSESSION.close()


defXadd_goodbye_setting(
XXXXchat_id,
XXXXcustom_goodbye_message,
XXXXshould_clean_goodbye,
XXXXprevious_goodbye,
XXXXmedia_file_id,
):
XXXX#XadderX=XSESSION.query(Goodbye).get(chat_id)
XXXXadderX=XGoodbye(
XXXXXXXXchat_id,
XXXXXXXXcustom_goodbye_message,
XXXXXXXXshould_clean_goodbye,
XXXXXXXXprevious_goodbye,
XXXXXXXXmedia_file_id,
XXXX)
XXXXSESSION.add(adder)
XXXXSESSION.commit()


defXrm_goodbye_setting(chat_id):
XXXXremX=XSESSION.query(Goodbye).get(str(chat_id))
XXXXifXrem:
XXXXXXXXSESSION.delete(rem)
XXXXXXXXSESSION.commit()


defXupdate_previous_goodbye(chat_id,Xprevious_goodbye):
XXXXrowX=XSESSION.query(Goodbye).get(str(chat_id))
XXXXrow.previous_goodbyeX=Xprevious_goodbye
XXXX#XcommitXtheXchangesXtoXtheXDB
XXXXSESSION.commit()
