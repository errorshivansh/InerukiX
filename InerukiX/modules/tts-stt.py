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
fromdatetimeimportdatetime

importrequests
fromgttsimportgTTS,gTTSError
fromtelethon.tlimportfunctions,types

fromIneruki.configimportget_str_key
fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbot

IBM_WATSON_CRED_PASSWORD=get_str_key("IBM_WATSON_CRED_PASSWORD",required=False)
IBM_WATSON_CRED_URL=get_str_key("IBM_WATSON_CRED_URL",required=False)
TEMP_DOWNLOAD_DIRECTORY="./"


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):
returnisinstance(
(
awaittbot(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerUser):
returnTrue


@register(pattern="^/tts(.*)")
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
else:
return
input_str=event.pattern_match.group(1)
reply_to_id=event.message.id
ifevent.reply_to_msg_id:
previous_message=awaitevent.get_reply_message()
text=previous_message.message
lan=input_str
elif"|"ininput_str:
lan,text=input_str.split("|")
else:
awaitevent.reply(
"InvalidSyntax\nFormat`/ttslang|text`\nForeg:`/ttsen|hello`"
)
return
text=text.strip()
lan=lan.strip()
try:
tts=gTTS(text,tld="com",lang=lan)
tts.save("k.mp3")
exceptAssertionError:
awaitevent.reply(
"Thetextisempty.\n"
"Nothinglefttospeakafterpre-precessing,"
"tokenizingandcleaning."
)
return
exceptValueError:
awaitevent.reply("Languageisnotsupported.")
return
exceptRuntimeError:
awaitevent.reply("Errorloadingthelanguagesdictionary.")
return
exceptgTTSError:
awaitevent.reply("ErrorinGoogleText-to-SpeechAPIrequest!")
return
withopen("k.mp3","r"):
awaittbot.send_file(
event.chat_id,"k.mp3",voice_note=True,reply_to=reply_to_id
)
os.remove("k.mp3")


#------THANKSTOLONAMI------#


@register(pattern="^/stt$")
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
else:
return
start=datetime.now()
ifnotos.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
os.makedirs(TEMP_DOWNLOAD_DIRECTORY)

ifevent.reply_to_msg_id:
previous_message=awaitevent.get_reply_message()
required_file_name=awaitevent.client.download_media(
previous_message,TEMP_DOWNLOAD_DIRECTORY
)
ifIBM_WATSON_CRED_URLisNoneorIBM_WATSON_CRED_PASSWORDisNone:
awaitevent.reply(
"YouneedtosettherequiredENVvariablesforthismodule.\nModulestopping"
)
else:
#awaitevent.reply("Startinganalysis")
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
transcript_confidence=""
foralternativeinresults:
alternatives=alternative["alternatives"][0]
transcript_response+=""+str(alternatives["transcript"])
transcript_confidence+=(
""+str(alternatives["confidence"])+"+"
)
end=datetime.now()
ms=(end-start).seconds
iftranscript_response!="":
string_to_show="TRANSCRIPT:`{}`\nTimeTaken:{}seconds\nConfidence:`{}`".format(
transcript_response,ms,transcript_confidence
)
else:
string_to_show="TRANSCRIPT:`Nil`\nTimeTaken:{}seconds\n\n**NoResultsFound**".format(
ms
)
awaitevent.reply(string_to_show)
else:
awaitevent.reply(r["error"])
#now,removethetemporaryfile
os.remove(required_file_name)
else:
awaitevent.reply("Replytoavoicemessage,togetthetextoutofit.")


_mod_name_="TexttoSpeech"

_help_="""
-/tts:Replytoanymessagetogettexttospeechoutput
-/stt:Typeinreplytoavoicemessage(englishonly)toextracttextfromit.
"""
