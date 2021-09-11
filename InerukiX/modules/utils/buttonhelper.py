importre
fromtypingimportList

frompyrogram.typesimportInlineKeyboardButton

BTN_URL_REGE=re.compile(
r"(\[([^\[]+?)\]\((buttonurl|buttonalert):(?:/{0,2})(.+?)(:same)?\))"
)

SMART_OPEN="“"
SMART_CLOSE="”"
START_CHAR=("'",'"',SMART_OPEN)


defsplit_quotes(text:str)->List:
ifany(text.startswith(char)forcharinSTART_CHAR):
counter=1#ignorefirstchar->issomekindofquote
whilecounter<len(text):
iftext[counter]=="\\":
counter+=1
eliftext[counter]==text[0]or(
text[0]==SMART_OPENandtext[counter]==SMART_CLOSE
):
break
counter+=1
else:
returntext.split(None,1)

#1toavoidstartingquote,andcounterisexclusivesoavoidsending
key=remove_escapes(text[1:counter].strip())
#indexwillbeinrange,or`else`wouldhavebeenexecutedandreturned
rest=text[counter+1:].strip()
ifnotkey:
key=text[0]+text[0]
returnlist(filter(None,[key,rest]))
else:
returntext.split(None,1)


defparser(text,keyword):
if"buttonalert"intext:
text=text.replace("\n","\\n").replace("\t","\\t")
buttons=[]
note_data=""
prev=0
i=0
alerts=[]
formatchinBTN_URL_REGE.finditer(text):
#Checkifbtnurlisescaped
n_escapes=0
to_check=match.start(1)-1
whileto_check>0andtext[to_check]=="\\":
n_escapes+=1
to_check-=1

#ifeven,notescaped->createbutton
ifn_escapes%2==0:
note_data+=text[prev:match.start(1)]
prev=match.end(1)
ifmatch.group(3)=="buttonalert":
#createathruplewithbuttonlabel,url,andnewlinestatus
ifbool(match.group(5))andbuttons:
buttons[-1].append(
InlineKeyboardButton(
text=match.group(2),
callback_data=f"alertmessage:{i}:{keyword}",
)
)
else:
buttons.append(
[
InlineKeyboardButton(
text=match.group(2),
callback_data=f"alertmessage:{i}:{keyword}",
)
]
)
i=i+1
alerts.append(match.group(4))
else:
ifbool(match.group(5))andbuttons:
buttons[-1].append(
InlineKeyboardButton(
text=match.group(2),url=match.group(4).replace("","")
)
)
else:
buttons.append(
[
InlineKeyboardButton(
text=match.group(2),url=match.group(4).replace("","")
)
]
)

#ifodd,escaped->movealong
else:
note_data+=text[prev:to_check]
prev=match.start(1)-1
else:
note_data+=text[prev:]

try:
returnnote_data,buttons,alerts
except:
returnnote_data,buttons,None


defremove_escapes(text:str)->str:
counter=0
res=""
is_escaped=False
whilecounter<len(text):
ifis_escaped:
res+=text[counter]
is_escaped=False
eliftext[counter]=="\\":
is_escaped=True
else:
res+=text[counter]
counter+=1
returnres


defhumanbytes(size):
ifnotsize:
return""
power=2**10
n=0
Dic_powerN={0:"",1:"Ki",2:"Mi",3:"Gi",4:"Ti"}
whilesize>power:
size/=power
n+=1
returnstr(round(size,2))+""+Dic_powerN[n]+"B"
