#Portedfrom@MissJuliaRobot

#Copyright(C)2021errorshivansh


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


importos
importsubprocess

importrequests
fromgttsimportgTTS,gTTSError
fromrequestsimportget
fromtelethon.tlimportfunctions,types
fromtelethon.tl.typesimport*

fromIneruki.configimportget_str_key
fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbot

IBM_WATSON_CRED_PASSWORD=get_str_key("IBM_WATSON_CRED_PASSWORD",None)
IBM_WATSON_CRED_URL=get_str_key("IBM_WATSON_CRED_URL",None)
WOLFRAM_ID=get_str_key("WOLFRAM_ID",None)
TEMP_DOWNLOAD_DIRECTORY="./"


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):

returnisinstance(
(
awaittbot(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerChat):

ui=awaittbot.get_peer_id(user)
ps=(
awaittbot(functions.messages.GetFullChatRequest(chat.chat_id))
).full_chat.participants.participants
returnisinstance(
next((pforpinpsifp.user_id==ui),None),
(types.ChatParticipantAdmin,types.ChatParticipantCreator),
)
returnNone


@register(pattern=r"^/ask(?:|$)([\s\S]*)")
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
else:
return
ifnotevent.reply_to_msg_id:
i=event.pattern_match.group(1)
appid=WOLFRAM_ID
server=f"https://api.wolframalpha.com/v1/spoken?appid={appid}&i={i}"
res=get(server)
if"WolframAlphadidnotunderstand"inres.text:
awaitevent.reply(
"Sorry,Ineruki'sAIsystemscould'trecognizedyourquestion.."
)
return
awaitevent.reply(f"**{i}**\n\n"+res.text,parse_mode="markdown")

ifevent.reply_to_msg_id:
previous_message=awaitevent.get_reply_message()
required_file_name=awaittbot.download_media(
previous_message,TEMP_DOWNLOAD_DIRECTORY
)
ifIBM_WATSON_CRED_URLisNoneorIBM_WATSON_CRED_PASSWORDisNone:
awaitevent.reply(
"YouneedtosettherequiredENVvariablesforthismodule.\nModulestopping"
)
else:
headers={
"Content-Type":previous_message.media.document.mime_type,
}
data=open(required_file_name,"rb").read()
response=requests.post(
IBM_WATSON_CRED_URL+"/v1/recognize",
headers=headers,
data=data,
auth=("apikey",IBM_WATSON_CRED_PASSWORD),
)
r=response.json()
if"results"inr:
#processthejsontoappropriatestringformat
results=r["results"]
transcript_response=""
foralternativeinresults:
alternatives=alternative["alternatives"][0]
transcript_response+=""+str(alternatives["transcript"])
iftranscript_response!="":
string_to_show="{}".format(transcript_response)
appid=WOLFRAM_ID
server=f"https://api.wolframalpha.com/v1/spoken?appid={appid}&i={string_to_show}"
res=get(server)

if"WolframAlphadidnotunderstand"inres:
answer=(
"I'msorryIneruki'sAIsystemcan'tundestandyourproblem"
)
else:
answer=res.text
try:
tts=gTTS(answer,tld="com",lang="en")
tts.save("results.mp3")
exceptAssertionError:
return
exceptValueError:
return
exceptRuntimeError:
return
exceptgTTSError:
return
withopen("results.mp3","r"):
awaittbot.send_file(
event.chat_id,
"results.mp3",
voice_note=True,
reply_to=event.id,
)
os.remove("results.mp3")
os.remove(required_file_name)
elif(
transcript_response=="WolframAlphadidnotunderstandyourinput"
):
try:
answer="Sorry,Ineruki'sAIsystemcan'tunderstandyou.."
tts=gTTS(answer,tld="com",lang="en")
tts.save("results.mp3")
exceptAssertionError:
return
exceptValueError:
return
exceptRuntimeError:
return
exceptgTTSError:
return
withopen("results.mp3","r"):
awaittbot.send_file(
event.chat_id,
"results.mp3",
voice_note=True,
reply_to=event.id,
)
os.remove("results.mp3")
os.remove(required_file_name)
else:
awaitevent.reply("APIFailure!")
os.remove(required_file_name)


@register(pattern="^/howdoi(.*)")
asyncdefhowdoi(event):
ifevent.fwd_from:
return
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
elifevent.chat_id==iidandevent.sender_id==userss:
pass
else:
return

str=event.pattern_match.group(1)
jit=subprocess.check_output(["howdoi",f"{str}"])
pit=jit.decode()
awaitevent.reply(pit)
