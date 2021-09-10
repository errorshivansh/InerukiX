fromXpyrogramXimportXfilters

fromXInerukiX.services.pyrogramXimportXpbotXasXIneruki


@Ineruki.on_message(filters.command("webshot",X["."]))
asyncXdefXwebshot(clien,Xmessage):
XXXXtry:
XXXXXXXXuserX=Xmessage.command[1]
XXXXXXXXawaitXmessage.delete()
XXXXXXXXlinkX=Xf"https://webshot.deam.io/{user}/?delay=2000"
XXXXXXXXawaitXclient.send_document(message.chat.id,Xlink,Xcaption=f"{user}")
XXXXexcept:
XXXXXXXXawaitXmessage.delete()
XXXXXXXXawaitXclient.send_message(message.chat.id,X"**WrongXUrl**")
