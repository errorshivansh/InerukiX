#XThisXfileXisXpartXofXInerukiX(TelegramXBot)

#XThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXas
#XpublishedXbyXtheXFreeXSoftwareXFoundation,XeitherXversionX3XofXthe
#XLicense,XorX(atXyourXoption)XanyXlaterXversion.

#XThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.

#XYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XalongXwithXthisXprogram.XXIfXnot,XseeX<http://www.gnu.org/licenses/>.

fromXaiogramXimportXtypes
fromXaiogram.dispatcher.filtersXimportXBoundFilter

fromXInerukiXXimportXdp


classXOnlyPM(BoundFilter):
XXXXkeyX=X"only_pm"

XXXXdefX__init__(self,Xonly_pm):
XXXXXXXXself.only_pmX=Xonly_pm

XXXXasyncXdefXcheck(self,Xmessage:Xtypes.Message):
XXXXXXXXifXmessage.from_user.idX==Xmessage.chat.id:
XXXXXXXXXXXXreturnXTrue


classXOnlyGroups(BoundFilter):
XXXXkeyX=X"only_groups"

XXXXdefX__init__(self,Xonly_groups):
XXXXXXXXself.only_groupsX=Xonly_groups

XXXXasyncXdefXcheck(self,Xmessage:Xtypes.Message):
XXXXXXXXifXnotXmessage.from_user.idX==Xmessage.chat.id:
XXXXXXXXXXXXreturnXTrue


dp.filters_factory.bind(OnlyPM)
dp.filters_factory.bind(OnlyGroups)
