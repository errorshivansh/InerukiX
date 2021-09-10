#XVoicsXChatbotXModuleXCreditsXPranavXAjayX🐰GithubX=XRed-AuraX🐹XTelegram=X@madepranav
#X@lyciachatbotXsupportXNow
importXos

importXaiofiles
importXaiohttp
fromXpyrogramXimportXfilters

fromXInerukiX.services.pyrogramXimportXpbotXasXLYCIA


asyncXdefXfetch(url):
XXXXasyncXwithXaiohttp.ClientSession()XasXsession:
XXXXXXXXasyncXwithXsession.get(url)XasXresp:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXdataX=XawaitXresp.json()
XXXXXXXXXXXXexcept:
XXXXXXXXXXXXXXXXdataX=XawaitXresp.text()
XXXXreturnXdata


asyncXdefXai_lycia(url):
XXXXai_nameX=X"Inerukix.mp3"
XXXXasyncXwithXaiohttp.ClientSession()XasXsession:
XXXXXXXXasyncXwithXsession.get(url)XasXresp:
XXXXXXXXXXXXifXresp.statusX==X200:
XXXXXXXXXXXXXXXXfX=XawaitXaiofiles.open(ai_name,Xmode="wb")
XXXXXXXXXXXXXXXXawaitXf.write(awaitXresp.read())
XXXXXXXXXXXXXXXXawaitXf.close()
XXXXreturnXai_name


@LYCIA.on_message(filters.command("Ineruki"))
asyncXdefXLycia(_,Xmessage):
XXXXifXlen(message.command)X<X2:
XXXXXXXXawaitXmessage.reply_text("InerukiXXAIXVoiceXChatbot")
XXXXXXXXreturn
XXXXtextX=Xmessage.text.split(None,X1)[1]
XXXXlyciaX=Xtext.replace("X",X"%20")
XXXXmX=XawaitXmessage.reply_text("InerukixXIsXBest...")
XXXXtry:
XXXXXXXXLX=XawaitXfetch(
XXXXXXXXXXXXf"https://api.affiliateplus.xyz/api/chatbot?message={lycia}&botname=Ineruki&ownername=errorshivansh&user=1"
XXXXXXXX)
XXXXXXXXchatbotX=XL["message"]
XXXXXXXXVoiceAiX=Xf"https://lyciavoice.herokuapp.com/lycia?text={chatbot}&lang=hi"
XXXXXXXXnameX=X"InerukiX"
XXXXexceptXExceptionXasXe:
XXXXXXXXawaitXm.edit(str(e))
XXXXXXXXreturn
XXXXawaitXm.edit("MadeXByX@madepranav...")
XXXXLyciaVoiceX=XawaitXai_lycia(VoiceAi)
XXXXawaitXm.edit("Repyping...")
XXXXawaitXmessage.reply_audio(audio=LyciaVoice,Xtitle=chatbot,Xperformer=name)
XXXXos.remove(LyciaVoice)
XXXXawaitXm.delete()
