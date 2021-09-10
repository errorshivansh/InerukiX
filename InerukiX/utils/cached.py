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


importXasyncio
importXfunctools
importXpickle
fromXtypingXimportXOptional,XUnion

fromXInerukiX.services.redisXimportXbredis
fromXInerukiX.utils.loggerXimportXlog


asyncXdefXset_value(key,Xvalue,Xttl):
XXXXvalueX=Xpickle.dumps(value)
XXXXbredis.set(key,Xvalue)
XXXXifXttl:
XXXXXXXXbredis.expire(key,Xttl)


classXcached:
XXXXdefX__init__(
XXXXXXXXself,
XXXXXXXXttl:XOptional[Union[int,Xfloat]]X=XNone,
XXXXXXXXkey:XOptional[str]X=XNone,
XXXXXXXXno_self:XboolX=XFalse,
XXXX):
XXXXXXXXself.ttlX=Xttl
XXXXXXXXself.keyX=Xkey
XXXXXXXXself.no_selfX=Xno_self

XXXXdefX__call__(self,X*args,X**kwargs):
XXXXXXXXifXnotXhasattr(self,X"func"):
XXXXXXXXXXXXself.funcX=Xargs[0]
XXXXXXXXXXXX#Xwrap
XXXXXXXXXXXXfunctools.update_wrapper(self,Xself.func)
XXXXXXXXXXXX#XreturnX``cached``XobjectXwhenXfunctionXisXnotXbeingXcalled
XXXXXXXXXXXXreturnXself
XXXXXXXXreturnXself._set(*args,X**kwargs)

XXXXasyncXdefX_set(self,X*args:Xdict,X**kwargs:Xdict):
XXXXXXXXkeyX=Xself.__build_key(*args,X**kwargs)

XXXXXXXXifXbredis.exists(key):
XXXXXXXXXXXXvalueX=Xpickle.loads(bredis.get(key))
XXXXXXXXXXXXreturnXvalueXifXtype(value)XisXnotX_NotSetXelseXvalue.real_value

XXXXXXXXresultX=XawaitXself.func(*args,X**kwargs)
XXXXXXXXifXresultXisXNone:
XXXXXXXXXXXXresultX=X_NotSet()
XXXXXXXXasyncio.ensure_future(set_value(key,Xresult,Xttl=self.ttl))
XXXXXXXXlog.debug(f"Cached:XwritingXnewXdataXforXkeyX-X{key}")
XXXXXXXXreturnXresultXifXtype(result)XisXnotX_NotSetXelseXresult.real_value

XXXXdefX__build_key(self,X*args:Xdict,X**kwargs:Xdict)X->Xstr:
XXXXXXXXordered_kwargsX=Xsorted(kwargs.items())

XXXXXXXXnew_keyX=X(
XXXXXXXXXXXXself.keyXifXself.keyXelseX(self.func.__module__XorX"")X+Xself.func.__name__
XXXXXXXX)
XXXXXXXXnew_keyX+=Xstr(args[1:]XifXself.no_selfXelseXargs)

XXXXXXXXifXordered_kwargs:
XXXXXXXXXXXXnew_keyX+=Xstr(ordered_kwargs)

XXXXXXXXreturnXnew_key

XXXXasyncXdefXreset_cache(self,X*args,Xnew_value=None,X**kwargs):
XXXXXXXX"""
XXXXXXXX>>>X@cached()
XXXXXXXX>>>XdefXsomefunction(arg):
XXXXXXXX>>>XXXXXpass
XXXXXXXX>>>
XXXXXXXX>>>X[...]
XXXXXXXX>>>XargX=X...X#XsameXthingX^^
XXXXXXXX>>>XawaitXsomefunction.reset_cache(arg,Xnew_value='Something')

XXXXXXXX:paramXnew_value:Xnew/XupdatedXvalueXtoXbeXsetX[optional]
XXXXXXXX"""

XXXXXXXXkeyX=Xself.__build_key(*args,X**kwargs)
XXXXXXXXifXnew_value:
XXXXXXXXXXXXreturnXset_value(key,Xnew_value,Xttl=self.ttl)
XXXXXXXXreturnXbredis.delete(key)


classX_NotSet:
XXXXreal_valueX=XNone

XXXXdefX__repr__(self)X->Xstr:
XXXXXXXXreturnX"NotSet"
