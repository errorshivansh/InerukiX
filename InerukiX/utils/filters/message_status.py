#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2019Aiogram
#
#ThisfileispartofInerukiBot.
#
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


classNotForwarded(BoundFilter):
key="not_forwarded"

def__init__(self,not_forwarded):
self.not_forwarded=not_forwarded

asyncdefcheck(self,message:types.Message):
if"forward_from"notinmessage:
returnTrue


classNoArgs(BoundFilter):
key="no_args"

def__init__(self,no_args):
self.no_args=no_args

asyncdefcheck(self,message:types.Message):
ifnotlen(message.text.split(""))>1:
returnTrue


classHasArgs(BoundFilter):
key="has_args"

def__init__(self,has_args):
self.has_args=has_args

asyncdefcheck(self,message:types.Message):
iflen(message.text.split(""))>1:
returnTrue


classCmdNotMonospaced(BoundFilter):
key="cmd_not_mono"

def__init__(self,cmd_not_mono):
self.cmd_not_mono=cmd_not_mono

asyncdefcheck(self,message:types.Message):
if(
message.entities
andmessage.entities[0]["type"]=="code"
andmessage.entities[0]["offset"]<1
):
returnFalse
returnTrue


dp.filters_factory.bind(NotForwarded)
dp.filters_factory.bind(NoArgs)
dp.filters_factory.bind(HasArgs)
dp.filters_factory.bind(CmdNotMonospaced)
