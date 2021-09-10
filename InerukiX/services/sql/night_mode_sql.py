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


classXNightmode(BASE):
XXXX__tablename__X=X"nightmode"
XXXXchat_idX=XColumn(String(14),Xprimary_key=True)

XXXXdefX__init__(self,Xchat_id):
XXXXXXXXself.chat_idX=Xchat_id


Nightmode.__table__.create(checkfirst=True)


defXadd_nightmode(chat_id:Xstr):
XXXXnightmoddyX=XNightmode(str(chat_id))
XXXXSESSION.add(nightmoddy)
XXXXSESSION.commit()


defXrmnightmode(chat_id:Xstr):
XXXXrmnightmoddyX=XSESSION.query(Nightmode).get(str(chat_id))
XXXXifXrmnightmoddy:
XXXXXXXXSESSION.delete(rmnightmoddy)
XXXXXXXXSESSION.commit()


defXget_all_chat_id():
XXXXstarkX=XSESSION.query(Nightmode).all()
XXXXSESSION.close()
XXXXreturnXstark


defXis_nightmode_indb(chat_id:Xstr):
XXXXtry:
XXXXXXXXs__X=XSESSION.query(Nightmode).get(str(chat_id))
XXXXXXXXifXs__:
XXXXXXXXXXXXreturnXstr(s__.chat_id)
XXXXfinally:
XXXXXXXXSESSION.close()
