#ThisfileispartofIneruki(TelegramBot)

#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseas
#publishedbytheFreeSoftwareFoundation,eitherversion3ofthe
#License,or(atyouroption)anylaterversion.

#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.

#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<http://www.gnu.org/licenses/>.

fromaiogramimporttypes
fromaiogram.dispatcher.filtersimportBoundFilter

fromInerukiimportOPERATORS,dp
fromIneruki.configimportget_int_key
fromIneruki.modules.utils.languageimportget_strings_dec
fromIneruki.modules.utils.user_detailsimportis_user_admin
fromIneruki.services.mongoimportmongodb


classIsAdmin(BoundFilter):
key="is_admin"

def__init__(self,is_admin):
self.is_admin=is_admin

@get_strings_dec("global")
asyncdefcheck(self,event,strings):

ifhasattr(event,"message"):
chat_id=event.message.chat.id
else:
chat_id=event.chat.id

ifnotawaitis_user_admin(chat_id,event.from_user.id):
task=event.answerifhasattr(event,"message")elseevent.reply
awaittask(strings["u_not_admin"])
returnFalse
returnTrue


classIsOwner(BoundFilter):
key="is_owner"

def__init__(self,is_owner):
self.is_owner=is_owner

asyncdefcheck(self,message:types.Message):
ifmessage.from_user.id==get_int_key("OWNER_ID"):
returnTrue


classIsOP(BoundFilter):
key="is_op"

def__init__(self,is_op):
self.is_owner=is_op

asyncdefcheck(self,message:types.Message):
ifmessage.from_user.idinOPERATORS:
returnTrue


classNotGbanned(BoundFilter):
key="not_gbanned"

def__init__(self,not_gbanned):
self.not_gbanned=not_gbanned

asyncdefcheck(self,message:types.Message):
check=mongodb.blacklisted_users.find_one({"user":message.from_user.id})
ifnotcheck:
returnTrue


dp.filters_factory.bind(IsAdmin)
dp.filters_factory.bind(IsOwner)
dp.filters_factory.bind(NotGbanned)
dp.filters_factory.bind(IsOP)
