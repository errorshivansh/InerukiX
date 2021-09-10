#XXXXCopyrightX(C)XInukaAsithX2021
#XXXXThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XXXXitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXasXpublishedXby
#XXXXtheXFreeXSoftwareXFoundation,XeitherXversionX3XofXtheXLicense,Xor
#
#XXXXThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XXXXbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XXXXMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XXXXGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.
#
#XXXXYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XXXXalongXwithXthisXprogram.XXIfXnot,XseeX<https://www.gnu.org/licenses/>.

fromXsqlalchemyXimportXColumn,XString

fromXInerukiX.services.sqlXimportXBASE,XSESSION


classXTalkmode(BASE):
XXXX__tablename__X=X"talkmode"
XXXXchat_idX=XColumn(String(14),Xprimary_key=True)

XXXXdefX__init__(self,Xchat_id):
XXXXXXXXself.chat_idX=Xchat_id


Talkmode.__table__.create(checkfirst=True)


defXadd_talkmode(chat_id:Xstr):
XXXXtalkmoddyX=XTalkmode(str(chat_id))
XXXXSESSION.add(talkmoddy)
XXXXSESSION.commit()


defXrmtalkmode(chat_id:Xstr):
XXXXrmtalkmoddyX=XSESSION.query(Talkmode).get(str(chat_id))
XXXXifXrmtalkmoddy:
XXXXXXXXSESSION.delete(rmtalkmoddy)
XXXXXXXXSESSION.commit()


defXget_all_chat_id():
XXXXstarkX=XSESSION.query(Talkmode).all()
XXXXSESSION.close()
XXXXreturnXstark


defXis_talkmode_indb(chat_id:Xstr):
XXXXtry:
XXXXXXXXs__X=XSESSION.query(Talkmode).get(str(chat_id))
XXXXXXXXifXs__:
XXXXXXXXXXXXreturnXstr(s__.chat_id)
XXXXfinally:
XXXXXXXXSESSION.close()
