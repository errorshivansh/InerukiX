#Copyright(C)2021Red-Aura&errorshivansh&HamkerCat

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

importemoji

url="https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
importre

importaiohttp

#fromgoogle_trans_newimportgoogle_translator
fromgoogletransimportTranslatorasgoogle_translator
frompyrogramimportfilters

fromInerukiimportBOT_ID
fromIneruki.db.mongo_helpers.aichatimportadd_chat,get_session,remove_chat
fromIneruki.function.inlinehelperimportarq
fromIneruki.function.pluginhelpersimportadmins_only,edit_or_reply
fromIneruki.services.pyrogramimportpbotasInerukix

translator=google_translator()


asyncdeflunaQuery(query:str,user_id:int):
luna=awaitarq.luna(query,user_id)
returnluna.result


defextract_emojis(s):
return"".join(cforcinsifcinemoji.UNICODE_EMOJI)


asyncdeffetch(url):
try:
asyncwithaiohttp.Timeout(10.0):
asyncwithaiohttp.ClientSession()assession:
asyncwithsession.get(url)asresp:
try:
data=awaitresp.json()
except:
data=awaitresp.text()
returndata
except:
print("AIresponseTimeout")
return


Ineruki_chats=[]
en_chats=[]
#AIChat(C)2020-2021by@InukaAsith


@Inerukix.on_message(
filters.command("chatbot")&~filters.edited&~filters.bot&~filters.private
)
@admins_only
asyncdefhmm(_,message):
globalIneruki_chats
iflen(message.command)!=2:
awaitmessage.reply_text(
"Ionlyrecognize`/chatboton`and/chatbot`offonly`"
)
message.continue_propagation()
status=message.text.split(None,1)[1]
chat_id=message.chat.id
ifstatus=="ON"orstatus=="on"orstatus=="On":
lel=awaitedit_or_reply(message,"`Processing...`")
lol=add_chat(int(message.chat.id))
ifnotlol:
awaitlel.edit("InerukiAIAlreadyActivatedInThisChat")
return
awaitlel.edit(
f"InerukiAISuccessfullyAddedForUsersInTheChat{message.chat.id}"
)

elifstatus=="OFF"orstatus=="off"orstatus=="Off":
lel=awaitedit_or_reply(message,"`Processing...`")
Escobar=remove_chat(int(message.chat.id))
ifnotEscobar:
awaitlel.edit("InerukiAIWasNotActivatedInThisChat")
return
awaitlel.edit(
f"InerukiAISuccessfullyDeactivatedForUsersInTheChat{message.chat.id}"
)

elifstatus=="EN"orstatus=="en"orstatus=="english":
ifnotchat_idinen_chats:
en_chats.append(chat_id)
awaitmessage.reply_text("EnglishAIchatEnabled!")
return
awaitmessage.reply_text("AIChatIsAlreadyDisabled.")
message.continue_propagation()
else:
awaitmessage.reply_text(
"Ionlyrecognize`/chatboton`and/chatbot`offonly`"
)


@Inerukix.on_message(
filters.text
&filters.reply
&~filters.bot
&~filters.edited
&~filters.via_bot
&~filters.forwarded,
group=2,
)
asyncdefhmm(client,message):
ifnotget_session(int(message.chat.id)):
return
ifnotmessage.reply_to_message:
return
try:
senderr=message.reply_to_message.from_user.id
except:
return
ifsenderr!=BOT_ID:
return
msg=message.text
chat_id=message.chat.id
ifmsg.startswith("/")ormsg.startswith("@"):
message.continue_propagation()
ifchat_idinen_chats:
test=msg
test=test.replace("Ineruki","Aco")
test=test.replace("Ineruki","Aco")
response=awaitlunaQuery(
test,message.from_user.idifmessage.from_userelse0
)
response=response.replace("Aco","Ineruki")
response=response.replace("aco","Ineruki")

pro=response
try:
awaitInerukix.send_chat_action(message.chat.id,"typing")
awaitmessage.reply_text(pro)
exceptCFError:
return

else:
u=msg.split()
emj=extract_emojis(msg)
msg=msg.replace(emj,"")
if(
[(k)forkinuifk.startswith("@")]
and[(k)forkinuifk.startswith("#")]
and[(k)forkinuifk.startswith("/")]
andre.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)",msg)!=[]
):

h="".join(filter(lambdax:x[0]!="@",u))
km=re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)",r"",h)
tm=km.split()
jm="".join(filter(lambdax:x[0]!="#",tm))
hm=jm.split()
rm="".join(filter(lambdax:x[0]!="/",hm))
elif[(k)forkinuifk.startswith("@")]:

rm="".join(filter(lambdax:x[0]!="@",u))
elif[(k)forkinuifk.startswith("#")]:
rm="".join(filter(lambdax:x[0]!="#",u))
elif[(k)forkinuifk.startswith("/")]:
rm="".join(filter(lambdax:x[0]!="/",u))
elifre.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)",msg)!=[]:
rm=re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)",r"",msg)
else:
rm=msg
#print(rm)
try:
lan=translator.detect(rm)
lan=lan.lang
except:
return
test=rm
ifnot"en"inlanandnotlan=="":
try:
test=translator.translate(test,dest="en")
test=test.text
except:
return
#test=emoji.demojize(test.strip())

test=test.replace("Ineruki","Aco")
test=test.replace("Ineruki","Aco")
response=awaitlunaQuery(
test,message.from_user.idifmessage.from_userelse0
)
response=response.replace("Aco","Ineruki")
response=response.replace("aco","Ineruki")
response=response.replace("Luna","Ineruki")
response=response.replace("luna","Ineruki")
pro=response
ifnot"en"inlanandnotlan=="":
try:
pro=translator.translate(pro,dest=lan)
pro=pro.text
except:
return
try:
awaitInerukix.send_chat_action(message.chat.id,"typing")
awaitmessage.reply_text(pro)
exceptCFError:
return


@Inerukix.on_message(
filters.text&filters.private&~filters.edited&filters.reply&~filters.bot
)
asyncdefinuka(client,message):
msg=message.text
ifmsg.startswith("/")ormsg.startswith("@"):
message.continue_propagation()
u=msg.split()
emj=extract_emojis(msg)
msg=msg.replace(emj,"")
if(
[(k)forkinuifk.startswith("@")]
and[(k)forkinuifk.startswith("#")]
and[(k)forkinuifk.startswith("/")]
andre.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)",msg)!=[]
):

h="".join(filter(lambdax:x[0]!="@",u))
km=re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)",r"",h)
tm=km.split()
jm="".join(filter(lambdax:x[0]!="#",tm))
hm=jm.split()
rm="".join(filter(lambdax:x[0]!="/",hm))
elif[(k)forkinuifk.startswith("@")]:

rm="".join(filter(lambdax:x[0]!="@",u))
elif[(k)forkinuifk.startswith("#")]:
rm="".join(filter(lambdax:x[0]!="#",u))
elif[(k)forkinuifk.startswith("/")]:
rm="".join(filter(lambdax:x[0]!="/",u))
elifre.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)",msg)!=[]:
rm=re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)",r"",msg)
else:
rm=msg
#print(rm)
try:
lan=translator.detect(rm)
lan=lan.lang
except:
return
test=rm
ifnot"en"inlanandnotlan=="":
try:
test=translator.translate(test,dest="en")
test=test.text
except:
return

#test=emoji.demojize(test.strip())

#Kangwiththecreditsbitches@InukaASiTH
test=test.replace("Ineruki","Aco")
test=test.replace("Ineruki","Aco")

response=awaitlunaQuery(test,message.from_user.idifmessage.from_userelse0)
response=response.replace("Aco","Ineruki")
response=response.replace("aco","Ineruki")

pro=response
ifnot"en"inlanandnotlan=="":
pro=translator.translate(pro,dest=lan)
pro=pro.text
try:
awaitInerukix.send_chat_action(message.chat.id,"typing")
awaitmessage.reply_text(pro)
exceptCFError:
return


@Inerukix.on_message(
filters.regex("Ineruki|Ineruki|Ineruki|Inerukix|Inerukix")
&~filters.bot
&~filters.via_bot
&~filters.forwarded
&~filters.reply
&~filters.channel
&~filters.edited
)
asyncdefinuka(client,message):
msg=message.text
ifmsg.startswith("/")ormsg.startswith("@"):
message.continue_propagation()
u=msg.split()
emj=extract_emojis(msg)
msg=msg.replace(emj,"")
if(
[(k)forkinuifk.startswith("@")]
and[(k)forkinuifk.startswith("#")]
and[(k)forkinuifk.startswith("/")]
andre.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)",msg)!=[]
):

h="".join(filter(lambdax:x[0]!="@",u))
km=re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)",r"",h)
tm=km.split()
jm="".join(filter(lambdax:x[0]!="#",tm))
hm=jm.split()
rm="".join(filter(lambdax:x[0]!="/",hm))
elif[(k)forkinuifk.startswith("@")]:

rm="".join(filter(lambdax:x[0]!="@",u))
elif[(k)forkinuifk.startswith("#")]:
rm="".join(filter(lambdax:x[0]!="#",u))
elif[(k)forkinuifk.startswith("/")]:
rm="".join(filter(lambdax:x[0]!="/",u))
elifre.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)",msg)!=[]:
rm=re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)",r"",msg)
else:
rm=msg
#print(rm)
try:
lan=translator.detect(rm)
lan=lan.lang
except:
return
test=rm
ifnot"en"inlanandnotlan=="":
try:
test=translator.translate(test,dest="en")
test=test.text
except:
return

#test=emoji.demojize(test.strip())

test=test.replace("Ineruki","Aco")
test=test.replace("Ineruki","Aco")
response=awaitlunaQuery(test,message.from_user.idifmessage.from_userelse0)
response=response.replace("Aco","Ineruki")
response=response.replace("aco","Ineruki")

pro=response
ifnot"en"inlanandnotlan=="":
try:
pro=translator.translate(pro,dest=lan)
pro=pro.text
exceptException:
return
try:
awaitInerukix.send_chat_action(message.chat.id,"typing")
awaitmessage.reply_text(pro)
exceptCFError:
return


__help__="""
<b>Chatbot</b>
INERUKIAI3.0ISTHEONLYAISYSTEMWHICHCANDETECT&REPLYUPTO200LANGUAGES

-/chatbot[ON/OFF]:EnablesanddisablesAIChatmode(ECLUSIVE)
-/chatbotEN:EnablesEnglishonlychatbot


<b>Assistant</b>
-/ask[question]:AskquestionfromIneruki
-/ask[replytovoicenote]:Getvoicereply

"""

__mod_name__="AIAssistant"
