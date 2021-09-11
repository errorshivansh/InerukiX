#VoicsChatbotModuleCreditsPranavAjay🐰Github=Red-Aura🐹Telegram=@madepranav
#@lyciachatbotsupportNow
importos

importaiofiles
importaiohttp
frompyrogramimportfilters

fromIneruki.services.pyrogramimportpbotasLYCIA


asyncdeffetch(url):
asyncwithaiohttp.ClientSession()assession:
asyncwithsession.get(url)asresp:
try:
data=awaitresp.json()
except:
data=awaitresp.text()
returndata


asyncdefai_lycia(url):
ai_name="Inerukix.mp3"
asyncwithaiohttp.ClientSession()assession:
asyncwithsession.get(url)asresp:
ifresp.status==200:
f=awaitaiofiles.open(ai_name,mode="wb")
awaitf.write(awaitresp.read())
awaitf.close()
returnai_name


@LYCIA.on_message(filters.command("Ineruki"))
asyncdefLycia(_,message):
iflen(message.command)<2:
awaitmessage.reply_text("InerukiAIVoiceChatbot")
return
text=message.text.split(None,1)[1]
lycia=text.replace("","%20")
m=awaitmessage.reply_text("InerukixIsBest...")
try:
L=awaitfetch(
f"https://api.affiliateplus.xyz/api/chatbot?message={lycia}&botname=Ineruki&ownername=errorshivansh&user=1"
)
chatbot=L["message"]
VoiceAi=f"https://lyciavoice.herokuapp.com/lycia?text={chatbot}&lang=hi"
name="Ineruki"
exceptExceptionase:
awaitm.edit(str(e))
return
awaitm.edit("MadeBy@madepranav...")
LyciaVoice=awaitai_lycia(VoiceAi)
awaitm.edit("Repyping...")
awaitmessage.reply_audio(audio=LyciaVoice,title=chatbot,performer=name)
os.remove(LyciaVoice)
awaitm.delete()
