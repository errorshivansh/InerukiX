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


importasyncio
importfunctools
importpickle
fromtypingimportOptional,Union

fromIneruki.services.redisimportbredis
fromIneruki.utils.loggerimportlog


asyncdefset_value(key,value,ttl):
value=pickle.dumps(value)
bredis.set(key,value)
ifttl:
bredis.expire(key,ttl)


classcached:
def__init__(
self,
ttl:Optional[Union[int,float]]=None,
key:Optional[str]=None,
no_self:bool=False,
):
self.ttl=ttl
self.key=key
self.no_self=no_self

def__call__(self,*args,**kwargs):
ifnothasattr(self,"func"):
self.func=args[0]
#wrap
functools.update_wrapper(self,self.func)
#return``cached``objectwhenfunctionisnotbeingcalled
returnself
returnself._set(*args,**kwargs)

asyncdef_set(self,*args:dict,**kwargs:dict):
key=self.__build_key(*args,**kwargs)

ifbredis.exists(key):
value=pickle.loads(bredis.get(key))
returnvalueiftype(value)isnot_NotSetelsevalue.real_value

result=awaitself.func(*args,**kwargs)
ifresultisNone:
result=_NotSet()
asyncio.ensure_future(set_value(key,result,ttl=self.ttl))
log.debug(f"Cached:writingnewdataforkey-{key}")
returnresultiftype(result)isnot_NotSetelseresult.real_value

def__build_key(self,*args:dict,**kwargs:dict)->str:
ordered_kwargs=sorted(kwargs.items())

new_key=(
self.keyifself.keyelse(self.func.__module__or"")+self.func.__name__
)
new_key+=str(args[1:]ifself.no_selfelseargs)

ifordered_kwargs:
new_key+=str(ordered_kwargs)

returnnew_key

asyncdefreset_cache(self,*args,new_value=None,**kwargs):
"""
>>>@cached()
>>>defsomefunction(arg):
>>>pass
>>>
>>>[...]
>>>arg=...#samething^^
>>>awaitsomefunction.reset_cache(arg,new_value='Something')

:paramnew_value:new/updatedvaluetobeset[optional]
"""

key=self.__build_key(*args,**kwargs)
ifnew_value:
returnset_value(key,new_value,ttl=self.ttl)
returnbredis.delete(key)


class_NotSet:
real_value=None

def__repr__(self)->str:
return"NotSet"
