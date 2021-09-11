#PortedFromWilliamButcherBot.
#CreditsGoestoWilliamButcherBot
#Portedfromhttps://github.com/TheHamkerCat/WilliamButcherBot
"""
MITLicense
Copyright(c)2021TheHamkerCat
Permissionisherebygranted,freeofcharge,toanypersonobtainingacopy
ofthissoftwareandassociateddocumentationfiles(the"Software"),todeal
intheSoftwarewithoutrestriction,includingwithoutlimitationtherights
touse,copy,modify,merge,publish,distribute,sublicense,and/orsell
copiesoftheSoftware,andtopermitpersonstowhomtheSoftwareis
furnishedtodoso,subjecttothefollowingconditions:
Theabovecopyrightnoticeandthispermissionnoticeshallbeincludedinall
copiesorsubstantialportionsoftheSoftware.
THESOFTWAREISPROVIDED"ASIS",WITHOUTWARRANTYOFANYKIND,EPRESSOR
IMPLIED,INCLUDINGBUTNOTLIMITEDTOTHEWARRANTIESOFMERCHANTABILITY,
FITNESSFORAPARTICULARPURPOSEANDNONINFRINGEMENT.INNOEVENTSHALLTHE
AUTHORSORCOPYRIGHTHOLDERSBELIABLEFORANYCLAIM,DAMAGESOROTHER
LIABILITY,WHETHERINANACTIONOFCONTRACT,TORTOROTHERWISE,ARISINGFROM,
OUTOFORINCONNECTIONWITHTHESOFTWAREORTHEUSEOROTHERDEALINGSINTHE
SOFTWARE.
"""

fromtypingimportDict,Union

frompyrogramimportfilters

fromIneruki.db.mongo_helpers.karmaimportis_karma_on,karma_off,karma_on
fromIneruki.function.pluginhelpersimportmember_permissions
fromIneruki.services.mongo2importdb
fromIneruki.services.pyrogramimportpbotasapp

karmadb=db.karma
karma_positive_group=3
karma_negative_group=4


asyncdefint_to_alpha(user_id:int)->str:
alphabet=["a","b","c","d","e","f","g","h","i","j"]
text=""
user_id=str(user_id)
foriinuser_id:
text+=alphabet[int(i)]
returntext


asyncdefalpha_to_int(user_id_alphabet:str)->int:
alphabet=["a","b","c","d","e","f","g","h","i","j"]
user_id=""
foriinuser_id_alphabet:
index=alphabet.index(i)
user_id+=str(index)
user_id=int(user_id)
returnuser_id


asyncdefget_karmas_count()->dict:
chats=karmadb.find({"chat_id":{"$lt":0}})
ifnotchats:
return{}
chats_count=0
karmas_count=0
forchatinawaitchats.to_list(length=1000000):
foriinchat["karma"]:
karmas_count+=chat["karma"][i]["karma"]
chats_count+=1
return{"chats_count":chats_count,"karmas_count":karmas_count}


asyncdefget_karmas(chat_id:int)->Dict[str,int]:
karma=awaitkarmadb.find_one({"chat_id":chat_id})
ifkarma:
karma=karma["karma"]
else:
karma={}
returnkarma


asyncdefget_karma(chat_id:int,name:str)->Union[bool,dict]:
name=name.lower().strip()
karmas=awaitget_karmas(chat_id)
ifnameinkarmas:
returnkarmas[name]


asyncdefupdate_karma(chat_id:int,name:str,karma:dict):
name=name.lower().strip()
karmas=awaitget_karmas(chat_id)
karmas[name]=karma
awaitkarmadb.update_one(
{"chat_id":chat_id},{"$set":{"karma":karmas}},upsert=True
)


_mod_name_="Karma"
_help_="""[UPVOTE]-Useupvotekeywordslike"+","+1","thanks"etctoupvoteamessage.
[DOWNVOTE]-Usedownvotekeywordslike"-","-1",etctodownvoteamessage.
Replytoamessagewith/karmatocheckauser'skarma
Send/karmawithoutreplyingtoanymessagetochekkarmalistoftop10users
<i>SpecialCreditstoWilliamButcherBot</i>"""


regex_upvote=r"^((?i)\+|\+\+|\+1|thx|tnx|ty|thankyou|thanx|thanks|pro|cool|good|👍)$"
regex_downvote=r"^(\-|\-\-|\-1|👎)$"


@app.on_message(
filters.text
&filters.group
&filters.incoming
&filters.reply
&filters.regex(regex_upvote)
&~filters.via_bot
&~filters.bot
&~filters.edited,
group=karma_positive_group,
)
asyncdefupvote(_,message):

ifnotawaitis_karma_on(message.chat.id):
return
try:
ifmessage.reply_to_message.from_user.id==message.from_user.id:
return
except:
return
chat_id=message.chat.id
try:
user_id=message.reply_to_message.from_user.id
except:
return
user_mention=message.reply_to_message.from_user.mention
current_karma=awaitget_karma(chat_id,awaitint_to_alpha(user_id))
ifcurrent_karma:
current_karma=current_karma["karma"]
karma=current_karma+1
new_karma={"karma":karma}
awaitupdate_karma(chat_id,awaitint_to_alpha(user_id),new_karma)
else:
karma=1
new_karma={"karma":karma}
awaitupdate_karma(chat_id,awaitint_to_alpha(user_id),new_karma)
awaitmessage.reply_text(
f"IncrementedKarmaof{user_mention}By1\nTotalPoints:{karma}"
)


@app.on_message(
filters.text
&filters.group
&filters.incoming
&filters.reply
&filters.regex(regex_downvote)
&~filters.via_bot
&~filters.bot
&~filters.edited,
group=karma_negative_group,
)
asyncdefdownvote(_,message):

ifnotawaitis_karma_on(message.chat.id):
return
try:
ifmessage.reply_to_message.from_user.id==message.from_user.id:
return
except:
return
chat_id=message.chat.id
try:
user_id=message.reply_to_message.from_user.id
except:
return
user_mention=message.reply_to_message.from_user.mention
current_karma=awaitget_karma(chat_id,awaitint_to_alpha(user_id))
ifcurrent_karma:
current_karma=current_karma["karma"]
karma=current_karma-1
new_karma={"karma":karma}
awaitupdate_karma(chat_id,awaitint_to_alpha(user_id),new_karma)
else:
karma=1
new_karma={"karma":karma}
awaitupdate_karma(chat_id,awaitint_to_alpha(user_id),new_karma)
awaitmessage.reply_text(
f"DecrementedKarmaOf{user_mention}By1\nTotalPoints:{karma}"
)


@app.on_message(filters.command("karma")&filters.group)
asyncdefkarma(_,message):
chat_id=message.chat.id
iflen(message.command)!=2:
ifnotmessage.reply_to_message:
karma=awaitget_karmas(chat_id)
msg=f"**Karmalistof{message.chat.title}:-**\n"
limit=0
karma_dicc={}
foriinkarma:
user_id=awaitalpha_to_int(i)
user_karma=karma[i]["karma"]
karma_dicc[str(user_id)]=user_karma
karma_arranged=dict(
sorted(karma_dicc.items(),key=lambdaitem:item[1],reverse=True)
)
foruser_idd,karma_countinkarma_arranged.items():
iflimit>9:
break
try:
user_name=(awaitapp.get_users(int(user_idd))).username
exceptException:
continue
msg+=f"{user_name}:`{karma_count}`\n"
limit+=1
awaitmessage.reply_text(msg)
else:
user_id=message.reply_to_message.from_user.id
karma=awaitget_karma(chat_id,awaitint_to_alpha(user_id))
ifkarma:
karma=karma["karma"]
awaitmessage.reply_text(f"**TotalPoints**:__{karma}__")
else:
karma=0
awaitmessage.reply_text(f"**TotalPoints**:__{karma}__")
return
status=message.text.split(None,1)[1].strip()
status=status.lower()
chat_id=message.chat.id
user_id=message.from_user.id
permissions=awaitmember_permissions(chat_id,user_id)
if"can_change_info"notinpermissions:
awaitmessage.reply_text("Youdon'thaveenoughpermissions.")
return
ifstatus=="on"orstatus=="ON":
awaitkarma_on(chat_id)
awaitmessage.reply_text(
f"AddedChat{chat_id}ToDatabase.Karmawillbeenabledhere"
)
elifstatus=="off"orstatus=="OFF":
awaitkarma_off(chat_id)
awaitmessage.reply_text(
f"RemovedChat{chat_id}ToDatabase.Karmawillbedisabledhere"
)
