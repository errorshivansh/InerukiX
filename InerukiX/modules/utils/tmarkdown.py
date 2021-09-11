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

importre
importwarnings

fromtelethon.helpersimportadd_surrogate,del_surrogate,strip_text
fromtelethon.tlimportTLObject
fromtelethon.tl.typesimport(
MessageEntityBold,
MessageEntityCode,
MessageEntityItalic,
MessageEntityMentionName,
MessageEntityPre,
MessageEntityStrike,
MessageEntityTextUrl,
MessageEntityUnderline,
)

DEFAULT_DELIMITERS={
"**":MessageEntityBold,
"__":MessageEntityItalic,
"~~":MessageEntityStrike,
"++":MessageEntityUnderline,
"`":MessageEntityCode,
"```":MessageEntityPre,
}

DEFAULT_URL_RE=re.compile(r"\[([\S\s]+?)\]\((.+?)\)")
DEFAULT_URL_FORMAT="[{0}]({1})"


defoverlap(a,b,x,y):
returnmax(a,x)<min(b,y)


defparse(message,delimiters=None,url_re=None):
"""
Parsesthegivenmarkdownmessageandreturnsitsstrippedrepresentation
plusalistoftheMessageEntity'sthatwerefound.
:parammessage:themessagewithmarkdown-likesyntaxtobeparsed.
:paramdelimiters:thedelimiterstobeused,{delimiter:type}.
:paramurl_re:theURLbytesregextobeused.Musthavetwogroups.
:return:atupleconsistingof(cleanmessage,[messageentities]).
"""
ifnotmessage:
returnmessage,[]

ifurl_reisNone:
url_re=DEFAULT_URL_RE
elifisinstance(url_re,str):
url_re=re.compile(url_re)

ifnotdelimiters:
ifdelimitersisnotNone:
returnmessage,[]
delimiters=DEFAULT_DELIMITERS

#Buildaregextoefficientlytestalldelimitersatonce.
#Notethatthelargestdelimitershouldgofirst,wedon't
#want```tobeinterpretedasasingleback-tickinacodeblock.
delim_re=re.compile(
"|".join(
"({})".format(re.escape(k))
forkinsorted(delimiters,key=len,reverse=True)
)
)

#Cannotuseaforloopbecauseweneedtoskipsomeindices
i=0
result=[]

#Workonbytelevelwiththeutf-16leencodingtogettheoffsetsright.
#Theoffsetwilljustbehalftheindexwe'reat.
message=add_surrogate(message)
whilei<len(message):
m=delim_re.match(message,pos=i)

#Didwefindsomedelimiterhereat`i`?
ifm:
delim=next(filter(None,m.groups()))

#+1toavoidmatchingrightafter(e.g."****")
end=message.find(delim,i+len(delim)+1)

#Didwefindtheearliestclosingtag?
ifend!=-1:

#Removethedelimiterfromthestring
message="".join(
(
message[:i],
message[i+len(delim):end],
message[end+len(delim):],
)
)

#Checkotheraffectedentities
forentinresult:
#Iftheendisafterourstart,itisaffected
ifent.offset+ent.length>i:
#Iftheoldstartisalsobeforeours,itisfullyenclosed
ifent.offset<=i:
ent.length-=len(delim)*2
else:
ent.length-=len(delim)

#Appendthefoundentity
ent=delimiters[delim]
ifent==MessageEntityPre:
result.append(ent(i,end-i-len(delim),""))#has'lang'
else:
result.append(ent(i,end-i-len(delim)))

#Nonestedentitiesinsidecodeblocks
ifentin(MessageEntityCode,MessageEntityPre):
i=end-len(delim)

continue

elifurl_re:
m=url_re.match(message,pos=i)
ifm:
#ReplacethewholematchwithonlytheinlineURLtext.
message="".join(
(message[:m.start()],m.group(1),message[m.end():])
)

delim_size=m.end()-m.start()-len(m.group())
forentinresult:
#Iftheendisafterourstart,itisaffected
ifent.offset+ent.length>m.start():
ent.length-=delim_size

result.append(
MessageEntityTextUrl(
offset=m.start(),
length=len(m.group(1)),
url=del_surrogate(m.group(2)),
)
)
i+=len(m.group(1))
continue

i+=1

message=strip_text(message,result)
returndel_surrogate(message),result


defunparse(text,entities,delimiters=None,url_fmt=None):
"""
Performsthereverseoperationto.parse(),effectivelyreturning
markdown-likesyntaxgivenanormaltextanditsMessageEntity's.
:paramtext:thetexttobereconvertedintomarkdown.
:paramentities:theMessageEntity'sappliedtothetext.
:return:amarkdown-liketextrepresentingthecombinationofbothinputs.
"""
ifnottextornotentities:
returntext

ifnotdelimiters:
ifdelimitersisnotNone:
returntext
delimiters=DEFAULT_DELIMITERS

ifurl_fmtisnotNone:
warnings.warn(
"url_fmtisdeprecated"
)#sinceitcomplicateseverything*alot*

ifisinstance(entities,TLObject):
entities=(entities,)

text=add_surrogate(text)
delimiters={v:kfork,vindelimiters.items()}
insert_at=[]
forentityinentities:
s=entity.offset
e=entity.offset+entity.length
delimiter=delimiters.get(type(entity),None)
ifdelimiter:
insert_at.append((s,delimiter))
insert_at.append((e,delimiter))
else:
url=None
ifisinstance(entity,MessageEntityTextUrl):
url=entity.url
elifisinstance(entity,MessageEntityMentionName):
url="tg://user?id={}".format(entity.user_id)
ifurl:
insert_at.append((s,"["))
insert_at.append((e,"]({})".format(url)))

insert_at.sort(key=lambdat:t[0])
whileinsert_at:
at,what=insert_at.pop()

#Ifweareinthemiddleofasurrogatenudgethepositionby+1.
#Otherwisewewouldendupwithmalformedtextandfailtoencode.
#Forexampleofbadinput:"Hi\ud83d\ude1c"
#https://en.wikipedia.org/wiki/UTF-16#U+010000_to_U+10FFFF
whileat<len(text)and"\ud800"<=text[at]<="\udfff":
at+=1

text=text[:at]+what+text[at:]

returndel_surrogate(text)


deftbold(text,sep=""):
returnf"**{text}**"


deftitalic(text,sep=""):
returnf"__{text}__"


deftcode(text,sep=""):
returnf"`{text}`"


deftpre(text,sep=""):
returnf"```{text}```"


deftstrikethrough(text,sep=""):
returnf"~~{text}~~"


deftunderline(text,sep=""):
returnf"++{text}++"


deftlink(title,url):
return"[{0}]({1})".format(title,url)
