#XAllXCreditXToXWilliamXButcherXBot.
#XPortedXThisXPluginXhereXByXDevilXfromXwbb.
importXos

fromXpyrogramXimportXfilters

fromXInerukiXXimportXOWNER_ID
fromXInerukiX.services.pyrogramXimportXpbotXasXapp


@app.on_message(filters.command("install")X&Xfilters.user(OWNER_ID))
asyncXdefXinstall_module(_,Xmessage):
XXXXifXnotXmessage.reply_to_message:
XXXXXXXXawaitXmessage.reply_text("ReplyXToXAX.pyXFileXToXInstallXIt.")
XXXXXXXXreturn
XXXXifXnotXmessage.reply_to_message.document:
XXXXXXXXawaitXmessage.reply_text("ReplyXToXAX.pyXFileXToXInstallXIt.")
XXXXXXXXreturn
XXXXdocumentX=Xmessage.reply_to_message.document
XXXXifXdocument.mime_typeX!=X"text/x-python":
XXXXXXXXawaitXmessage.reply_text("INVALID_MIME_TYPE,XReplyXToXAXCorrectX.pyXFile.")
XXXXXXXXreturn
XXXXmX=XawaitXmessage.reply_text("**InstallingXModule**")
XXXXawaitXmessage.reply_to_message.download(f"./InerukiX/modules/{document.file_name}")
XXXXawaitXm.edit("**Restarting**")
XXXXos.execvp(
XXXXXXXXf"python{str(pyver.split('X')[0])[:3]}",
XXXXXXXX[f"python{str(pyver.split('X')[0])[:3]}",X"-m",X"InerukiX"],
XXXX)
