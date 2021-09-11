#AllCreditToWilliamButcherBot.
#PortedThisPluginhereByDevilfromwbb.
importos

frompyrogramimportfilters

fromInerukiimportOWNER_ID
fromIneruki.services.pyrogramimportpbotasapp


@app.on_message(filters.command("install")&filters.user(OWNER_ID))
asyncdefinstall_module(_,message):
ifnotmessage.reply_to_message:
awaitmessage.reply_text("ReplyToA.pyFileToInstallIt.")
return
ifnotmessage.reply_to_message.document:
awaitmessage.reply_text("ReplyToA.pyFileToInstallIt.")
return
document=message.reply_to_message.document
ifdocument.mime_type!="text/x-python":
awaitmessage.reply_text("INVALID_MIME_TYPE,ReplyToACorrect.pyFile.")
return
m=awaitmessage.reply_text("**InstallingModule**")
awaitmessage.reply_to_message.download(f"./Ineruki/modules/{document.file_name}")
awaitm.edit("**Restarting**")
os.execvp(
f"python{str(pyver.split('')[0])[:3]}",
[f"python{str(pyver.split('')[0])[:3]}","-m","Ineruki"],
)
