#XCopyrightX(C)X2018X-X2020XMrYacha.XAllXrightsXreserved.XSourceXcodeXavailableXunderXtheXAGPL.
#XCopyrightX(C)X2019XAiogram
#
#XThisXfileXisXpartXofXInerukiBot.
#
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


classXNotForwarded(BoundFilter):
XXXXkeyX=X"not_forwarded"

XXXXdefX__init__(self,Xnot_forwarded):
XXXXXXXXself.not_forwardedX=Xnot_forwarded

XXXXasyncXdefXcheck(self,Xmessage:Xtypes.Message):
XXXXXXXXifX"forward_from"XnotXinXmessage:
XXXXXXXXXXXXreturnXTrue


classXNoArgs(BoundFilter):
XXXXkeyX=X"no_args"

XXXXdefX__init__(self,Xno_args):
XXXXXXXXself.no_argsX=Xno_args

XXXXasyncXdefXcheck(self,Xmessage:Xtypes.Message):
XXXXXXXXifXnotXlen(message.text.split("X"))X>X1:
XXXXXXXXXXXXreturnXTrue


classXHasArgs(BoundFilter):
XXXXkeyX=X"has_args"

XXXXdefX__init__(self,Xhas_args):
XXXXXXXXself.has_argsX=Xhas_args

XXXXasyncXdefXcheck(self,Xmessage:Xtypes.Message):
XXXXXXXXifXlen(message.text.split("X"))X>X1:
XXXXXXXXXXXXreturnXTrue


classXCmdNotMonospaced(BoundFilter):
XXXXkeyX=X"cmd_not_mono"

XXXXdefX__init__(self,Xcmd_not_mono):
XXXXXXXXself.cmd_not_monoX=Xcmd_not_mono

XXXXasyncXdefXcheck(self,Xmessage:Xtypes.Message):
XXXXXXXXifX(
XXXXXXXXXXXXmessage.entities
XXXXXXXXXXXXandXmessage.entities[0]["type"]X==X"code"
XXXXXXXXXXXXandXmessage.entities[0]["offset"]X<X1
XXXXXXXX):
XXXXXXXXXXXXreturnXFalse
XXXXXXXXreturnXTrue


dp.filters_factory.bind(NotForwarded)
dp.filters_factory.bind(NoArgs)
dp.filters_factory.bind(HasArgs)
dp.filters_factory.bind(CmdNotMonospaced)
