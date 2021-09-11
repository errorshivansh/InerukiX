fromtypingimportDict,List,Union

fromIneruki.services.mongo2importdb

#Portedfromhttps://github.com/TheHamkerCat/WilliamButcherBot
"""
MITLicense
Copyright(c)2021TheHamkerCat
Permissionisherebygranted,freeofcharge,toanypersonobtainingacopy
ofthissoftwareandassociateddocumentationfiles(the"Software"),todeal
intheSoftwarewithoutrestriction,includingwithoutlimitationtherights
touse,copy,modify,merge,publish,distribute,sublicense,and/orsell
copiesoftheSoftware,andtopermitpersonstowhomtheSoftwareis
furnishedtodoso,subjecttothefollowingconditions:
Theabovecopyrightnoticeandthispermissionnoticeshallbeincludedinall
copiesorsubstantialportionsoftheSoftware.
THESOFTWAREISPROVIDED"ASIS",WITHOUTWARRANTYOFANYKIND,EPRESSOR
IMPLIED,INCLUDINGBUTNOTLIMITEDTOTHEWARRANTIESOFMERCHANTABILITY,
FITNESSFORAPARTICULARPURPOSEANDNONINFRINGEMENT.INNOEVENTSHALLTHE
AUTHORSORCOPYRIGHTHOLDERSBELIABLEFORANYCLAIM,DAMAGESOROTHER
LIABILITY,WHETHERINANACTIONOFCONTRACT,TORTOROTHERWISE,ARISINGFROM,
OUTOFORINCONNECTIONWITHTHESOFTWAREORTHEUSEOROTHERDEALINGSINTHE
SOFTWARE.
"""


filtersdb=db.filters


"""Filtersfuncions"""


asyncdef_get_filters(chat_id:int)->Dict[str,int]:
_filters=awaitfiltersdb.find_one({"chat_id":chat_id})
if_filters:
_filters=_filters["filters"]
else:
_filters={}
return_filters


asyncdefget_filters_names(chat_id:int)->List[str]:
_filters=[]
for_filterinawait_get_filters(chat_id):
_filters.append(_filter)
return_filters


asyncdefget_filter(chat_id:int,name:str)->Union[bool,dict]:
name=name.lower().strip()
_filters=await_get_filters(chat_id)
ifnamein_filters:
return_filters[name]
else:
returnFalse


asyncdefsave_filter(chat_id:int,name:str,_filter:dict):
name=name.lower().strip()
_filters=await_get_filters(chat_id)
_filters[name]=_filter

awaitfiltersdb.update_one(
{"chat_id":chat_id},{"$set":{"filters":_filters}},upsert=True
)


asyncdefdelete_filter(chat_id:int,name:str)->bool:
filtersd=await_get_filters(chat_id)
name=name.lower().strip()
ifnameinfiltersd:
delfiltersd[name]
awaitfiltersdb.update_one(
{"chat_id":chat_id},{"$set":{"filters":filtersd}},upsert=True
)
returnTrue
returnFalse
