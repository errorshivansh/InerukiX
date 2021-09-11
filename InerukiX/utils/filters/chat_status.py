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

fromInerukiimportdp


classOnlyPM(BoundFilter):
key="only_pm"

def__init__(self,only_pm):
self.only_pm=only_pm

asyncdefcheck(self,message:types.Message):
ifmessage.from_user.id==message.chat.id:
returnTrue


classOnlyGroups(BoundFilter):
key="only_groups"

def__init__(self,only_groups):
self.only_groups=only_groups

asyncdefcheck(self,message:types.Message):
ifnotmessage.from_user.id==message.chat.id:
returnTrue


dp.filters_factory.bind(OnlyPM)
dp.filters_factory.bind(OnlyGroups)
