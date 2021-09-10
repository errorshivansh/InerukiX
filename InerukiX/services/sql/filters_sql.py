fromXsqlalchemyXimportXColumn,XLargeBinary,XNumeric,XString,XUnicodeText

fromXInerukiX.services.sqlXimportXBASE,XSESSION


classXFilters(BASE):
XXXX__tablename__X=X"cust_filters"
XXXXchat_idX=XColumn(String(14),Xprimary_key=True)
XXXXkeywordX=XColumn(UnicodeText,Xprimary_key=True)
XXXXreplyX=XColumn(UnicodeText)
XXXXsnip_typeX=XColumn(Numeric)
XXXXmedia_idX=XColumn(UnicodeText)
XXXXmedia_access_hashX=XColumn(UnicodeText)
XXXXmedia_file_referenceX=XColumn(LargeBinary)

XXXXdefX__init__(
XXXXXXXXself,
XXXXXXXXchat_id,
XXXXXXXXkeyword,
XXXXXXXXreply,
XXXXXXXXsnip_type,
XXXXXXXXmedia_id=None,
XXXXXXXXmedia_access_hash=None,
XXXXXXXXmedia_file_reference=None,
XXXX):
XXXXXXXXself.chat_idX=Xchat_id
XXXXXXXXself.keywordX=Xkeyword
XXXXXXXXself.replyX=Xreply
XXXXXXXXself.snip_typeX=Xsnip_type
XXXXXXXXself.media_idX=Xmedia_id
XXXXXXXXself.media_access_hashX=Xmedia_access_hash
XXXXXXXXself.media_file_referenceX=Xmedia_file_reference


Filters.__table__.create(checkfirst=True)


defXget_filter(chat_id,Xkeyword):
XXXXtry:
XXXXXXXXreturnXSESSION.query(Filters).get((str(chat_id),Xkeyword))
XXXXexceptXBaseException:
XXXXXXXXreturnXNone
XXXXfinally:
XXXXXXXXSESSION.close()


defXget_all_filters(chat_id):
XXXXtry:
XXXXXXXXreturnXSESSION.query(Filters).filter(Filters.chat_idX==Xstr(chat_id)).all()
XXXXexceptXBaseException:
XXXXXXXXreturnXNone
XXXXfinally:
XXXXXXXXSESSION.close()


defXadd_filter(
XXXXchat_id,
XXXXkeyword,
XXXXreply,
XXXXsnip_type,
XXXXmedia_id,
XXXXmedia_access_hash,
XXXXmedia_file_reference,
):
XXXXadderX=XSESSION.query(Filters).get((str(chat_id),Xkeyword))
XXXXifXadder:
XXXXXXXXadder.replyX=Xreply
XXXXXXXXadder.snip_typeX=Xsnip_type
XXXXXXXXadder.media_idX=Xmedia_id
XXXXXXXXadder.media_access_hashX=Xmedia_access_hash
XXXXXXXXadder.media_file_referenceX=Xmedia_file_reference
XXXXelse:
XXXXXXXXadderX=XFilters(
XXXXXXXXXXXXchat_id,
XXXXXXXXXXXXkeyword,
XXXXXXXXXXXXreply,
XXXXXXXXXXXXsnip_type,
XXXXXXXXXXXXmedia_id,
XXXXXXXXXXXXmedia_access_hash,
XXXXXXXXXXXXmedia_file_reference,
XXXXXXXX)
XXXXSESSION.add(adder)
XXXXSESSION.commit()


defXremove_filter(chat_id,Xkeyword):
XXXXsaved_filterX=XSESSION.query(Filters).get((str(chat_id),Xkeyword))
XXXXifXsaved_filter:
XXXXXXXXSESSION.delete(saved_filter)
XXXXXXXXSESSION.commit()


defXremove_all_filters(chat_id):
XXXXsaved_filterX=XSESSION.query(Filters).filter(Filters.chat_idX==Xstr(chat_id))
XXXXifXsaved_filter:
XXXXXXXXsaved_filter.delete()
XXXXXXXXSESSION.commit()
