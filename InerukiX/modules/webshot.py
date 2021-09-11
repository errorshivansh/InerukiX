frompyrogramimportfilters

fromIneruki.services.pyrogramimportpbotasIneruki


@Ineruki.on_message(filters.command("webshot",["."]))
asyncdefwebshot(clien,message):
try:
user=message.command[1]
awaitmessage.delete()
link=f"https://webshot.deam.io/{user}/?delay=2000"
awaitclient.send_document(message.chat.id,link,caption=f"{user}")
except:
awaitmessage.delete()
awaitclient.send_message(message.chat.id,"**WrongUrl**")
