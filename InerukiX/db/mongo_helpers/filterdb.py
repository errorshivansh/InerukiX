fromXtypingXimportXDict,XList,XUnion

fromXInerukiX.services.mongo2XimportXdb

#XPortedXfromXhttps://github.com/TheHamkerCat/WilliamButcherBot
"""
MITXLicense
CopyrightX(c)X2021XTheHamkerCat
PermissionXisXherebyXgranted,XfreeXofXcharge,XtoXanyXpersonXobtainingXaXcopy
ofXthisXsoftwareXandXassociatedXdocumentationXfilesX(theX"Software"),XtoXdeal
inXtheXSoftwareXwithoutXrestriction,XincludingXwithoutXlimitationXtheXrights
toXuse,Xcopy,Xmodify,Xmerge,Xpublish,Xdistribute,Xsublicense,Xand/orXsell
copiesXofXtheXSoftware,XandXtoXpermitXpersonsXtoXwhomXtheXSoftwareXis
furnishedXtoXdoXso,XsubjectXtoXtheXfollowingXconditions:
TheXaboveXcopyrightXnoticeXandXthisXpermissionXnoticeXshallXbeXincludedXinXall
copiesXorXsubstantialXportionsXofXtheXSoftware.
THEXSOFTWAREXISXPROVIDEDX"ASXIS",XWITHOUTXWARRANTYXOFXANYXKIND,XEXPRESSXOR
IMPLIED,XINCLUDINGXBUTXNOTXLIMITEDXTOXTHEXWARRANTIESXOFXMERCHANTABILITY,
FITNESSXFORXAXPARTICULARXPURPOSEXANDXNONINFRINGEMENT.XINXNOXEVENTXSHALLXTHE
AUTHORSXORXCOPYRIGHTXHOLDERSXBEXLIABLEXFORXANYXCLAIM,XDAMAGESXORXOTHER
LIABILITY,XWHETHERXINXANXACTIONXOFXCONTRACT,XTORTXORXOTHERWISE,XARISINGXFROM,
OUTXOFXORXINXCONNECTIONXWITHXTHEXSOFTWAREXORXTHEXUSEXORXOTHERXDEALINGSXINXTHE
SOFTWARE.
"""


filtersdbX=Xdb.filters


"""XFiltersXfuncionsX"""


asyncXdefX_get_filters(chat_id:Xint)X->XDict[str,Xint]:
XXXX_filtersX=XawaitXfiltersdb.find_one({"chat_id":Xchat_id})
XXXXifX_filters:
XXXXXXXX_filtersX=X_filters["filters"]
XXXXelse:
XXXXXXXX_filtersX=X{}
XXXXreturnX_filters


asyncXdefXget_filters_names(chat_id:Xint)X->XList[str]:
XXXX_filtersX=X[]
XXXXforX_filterXinXawaitX_get_filters(chat_id):
XXXXXXXX_filters.append(_filter)
XXXXreturnX_filters


asyncXdefXget_filter(chat_id:Xint,Xname:Xstr)X->XUnion[bool,Xdict]:
XXXXnameX=Xname.lower().strip()
XXXX_filtersX=XawaitX_get_filters(chat_id)
XXXXifXnameXinX_filters:
XXXXXXXXreturnX_filters[name]
XXXXelse:
XXXXXXXXreturnXFalse


asyncXdefXsave_filter(chat_id:Xint,Xname:Xstr,X_filter:Xdict):
XXXXnameX=Xname.lower().strip()
XXXX_filtersX=XawaitX_get_filters(chat_id)
XXXX_filters[name]X=X_filter

XXXXawaitXfiltersdb.update_one(
XXXXXXXX{"chat_id":Xchat_id},X{"$set":X{"filters":X_filters}},Xupsert=True
XXXX)


asyncXdefXdelete_filter(chat_id:Xint,Xname:Xstr)X->Xbool:
XXXXfiltersdX=XawaitX_get_filters(chat_id)
XXXXnameX=Xname.lower().strip()
XXXXifXnameXinXfiltersd:
XXXXXXXXdelXfiltersd[name]
XXXXXXXXawaitXfiltersdb.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},X{"$set":X{"filters":Xfiltersd}},Xupsert=True
XXXXXXXX)
XXXXXXXXreturnXTrue
XXXXreturnXFalse
