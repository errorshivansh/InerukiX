#ThisfileispartofIneruki(TelegramBot)

#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseas
#publishedbytheFreeSoftwareFoundation,eitherversion3ofthe
#License,or(atyouroption)anylaterversion.
#
#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.
#
#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<http://www.gnu.org/licenses/>.
#
#ThisfileispartofIneruki.

fromtypingimportUnion


classSanTeDoc:
def__init__(self,*args):
self.items=list(args)

def__str__(self)->str:
return"\n".join([str(items)foritemsinself.items])

def__add__(self,other):
self.items.append(other)
returnself


classStyleFormationCore:
start:str
end:str

def__init__(self,text:str):
self.text=f"{self.start}{text}{self.end}"

def__str__(self)->str:
returnself.text


classBold(StyleFormationCore):
start="<b>"
end="</b>"


classItalic(StyleFormationCore):
start="<i>"
end="</i>"


classCode(StyleFormationCore):
start="<code>"
end="</code>"


classPre(StyleFormationCore):
start="<pre>"
end="</pre>"


classStrikethrough(StyleFormationCore):
start="<s>"
end="</s>"


classUnderline(StyleFormationCore):
start="<u>"
end="</u>"


classSection:
def__init__(self,*args,title="",indent=3,bold=True,postfix=":"):
self.title_text=title
self.items=list(args)
self.indent=indent
self.bold=bold
self.postfix=postfix

@property
deftitle(self)->str:
title=self.title_text
text=str(Bold(title))ifself.boldelsetitle
text+=self.postfix
returntext

def__str__(self)->str:
text=self.title
space=""*self.indent
foriteminself.items:
text+="\n"

iftype(item)isSection:
item.indent*=2
iftype(item)isSList:
item.indent=self.indent
else:
text+=space

text+=str(item)

returntext

def__add__(self,other):
self.items.append(other)
returnself


classSList:
def__init__(self,*args,indent=0,prefix="-"):
self.items=list(args)
self.prefix=prefix
self.indent=indent

def__str__(self)->str:
space=""*self.indentifself.indentelse""
text=""
foridx,iteminenumerate(self.items):
ifidx>0:
text+="\n"
text+=f"{space}{self.prefix}{item}"

returntext


classKeyValue:
def__init__(self,title,value,suffix=":"):
self.title=title
self.value=value
self.suffix=suffix

def__str__(self)->str:
text=f"{self.title}{self.suffix}{self.value}"
returntext


classMultiKeyValue:
def__init__(self,*items:Union[list,tuple],suffix=":",separator=","):
self.items:list=items
self.suffix=suffix
self.separator=separator

def__str__(self)->str:
text=""
items_count=len(self.items)
foridx,iteminenumerate(self.items):
text+=f"{item[0]}{self.suffix}{item[1]}"

ifitems_count-1!=idx:
text+=self.separator

returntext
