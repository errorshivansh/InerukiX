#Copyright(C)2020-2021byDevsExpo@Github,<https://github.com/DevsExpo>.
#
#Thisfileispartof<https://github.com/DevsExpo/FridayUserBot>project,
#andisreleasedunderthe"GNUv3.0LicenseAgreement".
#Pleasesee<https://github.com/DevsExpo/blob/master/LICENSE>
#
#Allrightsreserved.

importos

importrequests
frompyrogramimportfilters

fromIneruki.function.pluginhelpersimportedit_or_reply,get_text
fromIneruki.services.pyrogramimportpbot


@pbot.on_message(filters.command("paste")&~filters.edited&~filters.bot)
asyncdefpaste(client,message):
pablo=awaitedit_or_reply(message,"`PleaseWait.....`")
tex_t=get_text(message)
message_s=tex_t
ifnottex_t:
ifnotmessage.reply_to_message:
awaitpablo.edit("`ReplyToFile/GiveMeTextToPaste!`")
return
ifnotmessage.reply_to_message.text:
file=awaitmessage.reply_to_message.download()
m_list=open(file,"r").read()
message_s=m_list
print(message_s)
os.remove(file)
elifmessage.reply_to_message.text:
message_s=message.reply_to_message.text
key=(
requests.post("https://nekobin.com/api/documents",json={"content":message_s})
.json()
.get("result")
.get("key")
)
url=f"https://nekobin.com/{key}"
raw=f"https://nekobin.com/raw/{key}"
reply_text=f"PastedTextTo[NekoBin]({url})AndForRaw[ClickHere]({raw})"
awaitpablo.edit(reply_text)
