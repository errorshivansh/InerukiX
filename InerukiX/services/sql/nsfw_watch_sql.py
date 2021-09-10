#XXXXCopyrightX(C)XMidhunXKMX2020-2021
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


classXNsfwatch(BASE):
XXXX__tablename__X=X"nsfwatch"
XXXXchat_idX=XColumn(String(14),Xprimary_key=True)

XXXXdefX__init__(self,Xchat_id):
XXXXXXXXself.chat_idX=Xchat_id


Nsfwatch.__table__.create(checkfirst=True)


defXadd_nsfwatch(chat_id:Xstr):
XXXXnsfwsX=XNsfwatch(str(chat_id))
XXXXSESSION.add(nsfws)
XXXXSESSION.commit()


defXrmnsfwatch(chat_id:Xstr):
XXXXnsfwmX=XSESSION.query(Nsfwatch).get(str(chat_id))
XXXXifXnsfwm:
XXXXXXXXSESSION.delete(nsfwm)
XXXXXXXXSESSION.commit()


defXget_all_nsfw_enabled_chat():
XXXXstarkX=XSESSION.query(Nsfwatch).all()
XXXXSESSION.close()
XXXXreturnXstark


defXis_nsfwatch_indb(chat_id:Xstr):
XXXXtry:
XXXXXXXXs__X=XSESSION.query(Nsfwatch).get(str(chat_id))
XXXXXXXXifXs__:
XXXXXXXXXXXXreturnXstr(s__.chat_id)
XXXXfinally:
XXXXXXXXSESSION.close()
