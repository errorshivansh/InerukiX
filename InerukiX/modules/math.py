#XWrittenXbyXerrorshivanshXforXtheXInerukiXproject
#XThisXfileXisXpartXofXInerukiXBotX(TelegramXBot)

#XThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXas
#XpublishedXbyXtheXFreeXSoftwareXFoundation,XeitherXversionX3XofXthe
#XLicense,XorX(atXyourXoption)XanyXlaterXversion.

#XThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.


importXjson
importXmath

importXrequests

fromXInerukiX.decoratorXimportXregister

fromX.utils.disableXimportXdisableable_dec
fromX.utils.messageXimportXget_args_str


@register(cmds=["math",X"simplify"])
@disableable_dec("math")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXresponseX=Xrequests.get(f"https://newton.now.sh/api/v2/simplify/{args}")
XXXXcX=Xresponse.text
XXXXobjX=Xjson.loads(c)
XXXXjX=Xobj["result"]
XXXXawaitXmessage.reply(j)


@register(cmds=["factor",X"factorize"])
@disableable_dec("factor")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXresponseX=Xrequests.get(f"https://newton.now.sh/api/v2/factor/{args}")
XXXXcX=Xresponse.text
XXXXobjX=Xjson.loads(c)
XXXXjX=Xobj["result"]
XXXXawaitXmessage.reply(j)


@register(cmds="derive")
@disableable_dec("derive")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXresponseX=Xrequests.get(f"https://newton.now.sh/api/v2/derive/{args}")
XXXXcX=Xresponse.text
XXXXobjX=Xjson.loads(c)
XXXXjX=Xobj["result"]
XXXXawaitXmessage.reply(j)


@register(cmds="integrate")
@disableable_dec("integrate")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXresponseX=Xrequests.get(f"https://newton.now.sh/api/v2/integrate/{args}")
XXXXcX=Xresponse.text
XXXXobjX=Xjson.loads(c)
XXXXjX=Xobj["result"]
XXXXawaitXmessage.reply(j)


@register(cmds="zeroes")
@disableable_dec("zeroes")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXresponseX=Xrequests.get(f"https://newton.now.sh/api/v2/zeroes/{args}")
XXXXcX=Xresponse.text
XXXXobjX=Xjson.loads(c)
XXXXjX=Xobj["result"]
XXXXawaitXmessage.reply(j)


@register(cmds="tangent")
@disableable_dec("tangent")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXresponseX=Xrequests.get(f"https://newton.now.sh/api/v2/tangent/{args}")
XXXXcX=Xresponse.text
XXXXobjX=Xjson.loads(c)
XXXXjX=Xobj["result"]
XXXXawaitXmessage.reply(j)


@register(cmds="area")
@disableable_dec("area")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXresponseX=Xrequests.get(f"https://newton.now.sh/api/v2/area/{args}")
XXXXcX=Xresponse.text
XXXXobjX=Xjson.loads(c)
XXXXjX=Xobj["result"]
XXXXawaitXmessage.reply(j)


@register(cmds="cos")
@disableable_dec("cos")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXawaitXmessage.reply(str(math.cos(int(args))))


@register(cmds="sin")
@disableable_dec("sin")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXawaitXmessage.reply(str(math.sin(int(args))))


@register(cmds="tan")
@disableable_dec("tan")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXawaitXmessage.reply(str(math.tan(int(args))))


@register(cmds="arccos")
@disableable_dec("arccos")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXawaitXmessage.reply(str(math.acos(int(args))))


@register(cmds="arcsin")
@disableable_dec("arcsin")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXawaitXmessage.reply(str(math.asin(int(args))))


@register(cmds="arctan")
@disableable_dec("arctan")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXawaitXmessage.reply(str(math.atan(int(args))))


@register(cmds="abs")
@disableable_dec("abs")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXawaitXmessage.reply(str(math.fabs(int(args))))


@register(cmds="log")
@disableable_dec("log")
asyncXdefX_(message):
XXXXargsX=Xget_args_str(message)
XXXXawaitXmessage.reply(str(math.log(int(args))))


__help__X=X"""
SolvesXcomplexXmathXproblemsXusingXhttps://newton.now.shXandXpythonXmathXmodule
X-X/simplify-XMathX/mathX2^2+2(2)
X-X/factorX-XFactorX/factorXx^2X+X2x
X-X/deriveX-XDeriveX/deriveXx^2+2x
X-X/integrateX-XIntegrateX/integrateXx^2+2x
X-X/zeroesX-XFindX0'sX/zeroesXx^2+2x
X-X/tangentX-XFindXTangentX/tangentX2lx^
X-X/areaX-XAreaXUnderXCurveX/areaX2:4lx^3`
X-X/cosX-XCosineX/cosXpi
X-X/sinX-XSineX/sinX0
X-X/tanX-XTangentX/tanX0
X-X/arccosX-XInverseXCosineX/arccosX1
X-X/arcsinX-XInverseXSineX/arcsinX0
X-X/arctanX-XInverseXTangentX/arctanX0
X-X/absX-XAbsoluteXValueX/absX-1
X-X/log*X-XLogarithmX/logX2l8
X
KeepXinXmind,XToXfindXtheXtangentXlineXofXaXfunctionXatXaXcertainXxXvalue,XsendXtheXrequestXasXc|f(x)XwhereXcXisXtheXgivenXxXvalueXandXf(x)XisXtheXfunctionXexpression,XtheXseparatorXisXaXverticalXbarX'|'.XSeeXtheXtableXaboveXforXanXexampleXrequest.
ToXfindXtheXareaXunderXaXfunction,XsendXtheXrequestXasXc:d|f(x)XwhereXcXisXtheXstartingXxXvalue,XdXisXtheXendingXxXvalue,XandXf(x)XisXtheXfunctionXunderXwhichXyouXwantXtheXcurveXbetweenXtheXtwoXxXvalues.
ToXcomputeXfractions,XenterXexpressionsXasXnumerator(over)denominator.XForXexample,XtoXprocessX2/4XyouXmustXsendXinXyourXexpressionXasX2(over)4.XTheXresultXexpressionXwillXbeXinXstandardXmathXnotationX(1/2,X3/4).
"""

__mod_name__X=X"Maths"
