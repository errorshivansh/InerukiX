#XThisXfileXisXpartXofXInerukiX(TelegramXBot)

#XThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXas
#XpublishedXbyXtheXFreeXSoftwareXFoundation,XeitherXversionX3XofXthe
#XLicense,XorX(atXyourXoption)XanyXlaterXversion.
#
#XThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.
#
#XYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XalongXwithXthisXprogram.XXIfXnot,XseeX<http://www.gnu.org/licenses/>.
#
#XThisXfileXisXpartXofXIneruki.

fromXtypingXimportXUnion


classXSanTeXDoc:
XXXXdefX__init__(self,X*args):
XXXXXXXXself.itemsX=Xlist(args)

XXXXdefX__str__(self)X->Xstr:
XXXXXXXXreturnX"\n".join([str(items)XforXitemsXinXself.items])

XXXXdefX__add__(self,Xother):
XXXXXXXXself.items.append(other)
XXXXXXXXreturnXself


classXStyleFormationCore:
XXXXstart:Xstr
XXXXend:Xstr

XXXXdefX__init__(self,Xtext:Xstr):
XXXXXXXXself.textX=Xf"{self.start}{text}{self.end}"

XXXXdefX__str__(self)X->Xstr:
XXXXXXXXreturnXself.text


classXBold(StyleFormationCore):
XXXXstartX=X"<b>"
XXXXendX=X"</b>"


classXItalic(StyleFormationCore):
XXXXstartX=X"<i>"
XXXXendX=X"</i>"


classXCode(StyleFormationCore):
XXXXstartX=X"<code>"
XXXXendX=X"</code>"


classXPre(StyleFormationCore):
XXXXstartX=X"<pre>"
XXXXendX=X"</pre>"


classXStrikethrough(StyleFormationCore):
XXXXstartX=X"<s>"
XXXXendX=X"</s>"


classXUnderline(StyleFormationCore):
XXXXstartX=X"<u>"
XXXXendX=X"</u>"


classXSection:
XXXXdefX__init__(self,X*args,Xtitle="",Xindent=3,Xbold=True,Xpostfix=":"):
XXXXXXXXself.title_textX=Xtitle
XXXXXXXXself.itemsX=Xlist(args)
XXXXXXXXself.indentX=Xindent
XXXXXXXXself.boldX=Xbold
XXXXXXXXself.postfixX=Xpostfix

XXXX@property
XXXXdefXtitle(self)X->Xstr:
XXXXXXXXtitleX=Xself.title_text
XXXXXXXXtextX=Xstr(Bold(title))XifXself.boldXelseXtitle
XXXXXXXXtextX+=Xself.postfix
XXXXXXXXreturnXtext

XXXXdefX__str__(self)X->Xstr:
XXXXXXXXtextX=Xself.title
XXXXXXXXspaceX=X"X"X*Xself.indent
XXXXXXXXforXitemXinXself.items:
XXXXXXXXXXXXtextX+=X"\n"

XXXXXXXXXXXXifXtype(item)XisXSection:
XXXXXXXXXXXXXXXXitem.indentX*=X2
XXXXXXXXXXXXifXtype(item)XisXSList:
XXXXXXXXXXXXXXXXitem.indentX=Xself.indent
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXtextX+=Xspace

XXXXXXXXXXXXtextX+=Xstr(item)

XXXXXXXXreturnXtext

XXXXdefX__add__(self,Xother):
XXXXXXXXself.items.append(other)
XXXXXXXXreturnXself


classXSList:
XXXXdefX__init__(self,X*args,Xindent=0,Xprefix="-X"):
XXXXXXXXself.itemsX=Xlist(args)
XXXXXXXXself.prefixX=Xprefix
XXXXXXXXself.indentX=Xindent

XXXXdefX__str__(self)X->Xstr:
XXXXXXXXspaceX=X"X"X*Xself.indentXifXself.indentXelseX"X"
XXXXXXXXtextX=X""
XXXXXXXXforXidx,XitemXinXenumerate(self.items):
XXXXXXXXXXXXifXidxX>X0:
XXXXXXXXXXXXXXXXtextX+=X"\n"
XXXXXXXXXXXXtextX+=Xf"{space}{self.prefix}{item}"

XXXXXXXXreturnXtext


classXKeyValue:
XXXXdefX__init__(self,Xtitle,Xvalue,Xsuffix=":X"):
XXXXXXXXself.titleX=Xtitle
XXXXXXXXself.valueX=Xvalue
XXXXXXXXself.suffixX=Xsuffix

XXXXdefX__str__(self)X->Xstr:
XXXXXXXXtextX=Xf"{self.title}{self.suffix}{self.value}"
XXXXXXXXreturnXtext


classXMultiKeyValue:
XXXXdefX__init__(self,X*items:XUnion[list,Xtuple],Xsuffix=":X",Xseparator=",X"):
XXXXXXXXself.items:XlistX=Xitems
XXXXXXXXself.suffixX=Xsuffix
XXXXXXXXself.separatorX=Xseparator

XXXXdefX__str__(self)X->Xstr:
XXXXXXXXtextX=X""
XXXXXXXXitems_countX=Xlen(self.items)
XXXXXXXXforXidx,XitemXinXenumerate(self.items):
XXXXXXXXXXXXtextX+=Xf"{item[0]}{self.suffix}{item[1]}"

XXXXXXXXXXXXifXitems_countX-X1X!=Xidx:
XXXXXXXXXXXXXXXXtextX+=Xself.separator

XXXXXXXXreturnXtext
