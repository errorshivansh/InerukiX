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

fromXInerukiXXimportXOPERATORS,Xdp
fromXInerukiX.configXimportXget_int_key
fromXInerukiX.modules.utils.languageXimportXget_strings_dec
fromXInerukiX.modules.utils.user_detailsXimportXis_user_admin
fromXInerukiX.services.mongoXimportXmongodb


classXIsAdmin(BoundFilter):
XXXXkeyX=X"is_admin"

XXXXdefX__init__(self,Xis_admin):
XXXXXXXXself.is_adminX=Xis_admin

XXXX@get_strings_dec("global")
XXXXasyncXdefXcheck(self,Xevent,Xstrings):

XXXXXXXXifXhasattr(event,X"message"):
XXXXXXXXXXXXchat_idX=Xevent.message.chat.id
XXXXXXXXelse:
XXXXXXXXXXXXchat_idX=Xevent.chat.id

XXXXXXXXifXnotXawaitXis_user_admin(chat_id,Xevent.from_user.id):
XXXXXXXXXXXXtaskX=Xevent.answerXifXhasattr(event,X"message")XelseXevent.reply
XXXXXXXXXXXXawaitXtask(strings["u_not_admin"])
XXXXXXXXXXXXreturnXFalse
XXXXXXXXreturnXTrue


classXIsOwner(BoundFilter):
XXXXkeyX=X"is_owner"

XXXXdefX__init__(self,Xis_owner):
XXXXXXXXself.is_ownerX=Xis_owner

XXXXasyncXdefXcheck(self,Xmessage:Xtypes.Message):
XXXXXXXXifXmessage.from_user.idX==Xget_int_key("OWNER_ID"):
XXXXXXXXXXXXreturnXTrue


classXIsOP(BoundFilter):
XXXXkeyX=X"is_op"

XXXXdefX__init__(self,Xis_op):
XXXXXXXXself.is_ownerX=Xis_op

XXXXasyncXdefXcheck(self,Xmessage:Xtypes.Message):
XXXXXXXXifXmessage.from_user.idXinXOPERATORS:
XXXXXXXXXXXXreturnXTrue


classXNotGbanned(BoundFilter):
XXXXkeyX=X"not_gbanned"

XXXXdefX__init__(self,Xnot_gbanned):
XXXXXXXXself.not_gbannedX=Xnot_gbanned

XXXXasyncXdefXcheck(self,Xmessage:Xtypes.Message):
XXXXXXXXcheckX=Xmongodb.blacklisted_users.find_one({"user":Xmessage.from_user.id})
XXXXXXXXifXnotXcheck:
XXXXXXXXXXXXreturnXTrue


dp.filters_factory.bind(IsAdmin)
dp.filters_factory.bind(IsOwner)
dp.filters_factory.bind(NotGbanned)
dp.filters_factory.bind(IsOP)
