#WrittenbyerrorshivanshfortheInerukiproject
#ThisfileispartofInerukiBot(TelegramBot)

#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseas
#publishedbytheFreeSoftwareFoundation,eitherversion3ofthe
#License,or(atyouroption)anylaterversion.

#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.


importjson
importmath

importrequests

fromIneruki.decoratorimportregister

from.utils.disableimportdisableable_dec
from.utils.messageimportget_args_str


@register(cmds=["math","simplify"])
@disableable_dec("math")
asyncdef_(message):
args=get_args_str(message)
response=requests.get(f"https://newton.now.sh/api/v2/simplify/{args}")
c=response.text
obj=json.loads(c)
j=obj["result"]
awaitmessage.reply(j)


@register(cmds=["factor","factorize"])
@disableable_dec("factor")
asyncdef_(message):
args=get_args_str(message)
response=requests.get(f"https://newton.now.sh/api/v2/factor/{args}")
c=response.text
obj=json.loads(c)
j=obj["result"]
awaitmessage.reply(j)


@register(cmds="derive")
@disableable_dec("derive")
asyncdef_(message):
args=get_args_str(message)
response=requests.get(f"https://newton.now.sh/api/v2/derive/{args}")
c=response.text
obj=json.loads(c)
j=obj["result"]
awaitmessage.reply(j)


@register(cmds="integrate")
@disableable_dec("integrate")
asyncdef_(message):
args=get_args_str(message)
response=requests.get(f"https://newton.now.sh/api/v2/integrate/{args}")
c=response.text
obj=json.loads(c)
j=obj["result"]
awaitmessage.reply(j)


@register(cmds="zeroes")
@disableable_dec("zeroes")
asyncdef_(message):
args=get_args_str(message)
response=requests.get(f"https://newton.now.sh/api/v2/zeroes/{args}")
c=response.text
obj=json.loads(c)
j=obj["result"]
awaitmessage.reply(j)


@register(cmds="tangent")
@disableable_dec("tangent")
asyncdef_(message):
args=get_args_str(message)
response=requests.get(f"https://newton.now.sh/api/v2/tangent/{args}")
c=response.text
obj=json.loads(c)
j=obj["result"]
awaitmessage.reply(j)


@register(cmds="area")
@disableable_dec("area")
asyncdef_(message):
args=get_args_str(message)
response=requests.get(f"https://newton.now.sh/api/v2/area/{args}")
c=response.text
obj=json.loads(c)
j=obj["result"]
awaitmessage.reply(j)


@register(cmds="cos")
@disableable_dec("cos")
asyncdef_(message):
args=get_args_str(message)
awaitmessage.reply(str(math.cos(int(args))))


@register(cmds="sin")
@disableable_dec("sin")
asyncdef_(message):
args=get_args_str(message)
awaitmessage.reply(str(math.sin(int(args))))


@register(cmds="tan")
@disableable_dec("tan")
asyncdef_(message):
args=get_args_str(message)
awaitmessage.reply(str(math.tan(int(args))))


@register(cmds="arccos")
@disableable_dec("arccos")
asyncdef_(message):
args=get_args_str(message)
awaitmessage.reply(str(math.acos(int(args))))


@register(cmds="arcsin")
@disableable_dec("arcsin")
asyncdef_(message):
args=get_args_str(message)
awaitmessage.reply(str(math.asin(int(args))))


@register(cmds="arctan")
@disableable_dec("arctan")
asyncdef_(message):
args=get_args_str(message)
awaitmessage.reply(str(math.atan(int(args))))


@register(cmds="abs")
@disableable_dec("abs")
asyncdef_(message):
args=get_args_str(message)
awaitmessage.reply(str(math.fabs(int(args))))


@register(cmds="log")
@disableable_dec("log")
asyncdef_(message):
args=get_args_str(message)
awaitmessage.reply(str(math.log(int(args))))


__help__="""
Solvescomplexmathproblemsusinghttps://newton.now.shandpythonmathmodule
-/simplify-Math/math2^2+2(2)
-/factor-Factor/factorx^2+2x
-/derive-Derive/derivex^2+2x
-/integrate-Integrate/integratex^2+2x
-/zeroes-Find0's/zeroesx^2+2x
-/tangent-FindTangent/tangent2lx^
-/area-AreaUnderCurve/area2:4lx^3`
-/cos-Cosine/cospi
-/sin-Sine/sin0
-/tan-Tangent/tan0
-/arccos-InverseCosine/arccos1
-/arcsin-InverseSine/arcsin0
-/arctan-InverseTangent/arctan0
-/abs-AbsoluteValue/abs-1
-/log*-Logarithm/log2l8

Keepinmind,Tofindthetangentlineofafunctionatacertainxvalue,sendtherequestasc|f(x)wherecisthegivenxvalueandf(x)isthefunctionexpression,theseparatorisaverticalbar'|'.Seethetableaboveforanexamplerequest.
Tofindtheareaunderafunction,sendtherequestasc:d|f(x)wherecisthestartingxvalue,distheendingxvalue,andf(x)isthefunctionunderwhichyouwantthecurvebetweenthetwoxvalues.
Tocomputefractions,enterexpressionsasnumerator(over)denominator.Forexample,toprocess2/4youmustsendinyourexpressionas2(over)4.Theresultexpressionwillbeinstandardmathnotation(1/2,3/4).
"""

__mod_name__="Maths"
