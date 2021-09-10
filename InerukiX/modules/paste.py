#XCopyrightX(C)X2020-2021XbyXDevsExpo@Github,X<Xhttps://github.com/DevsExpoX>.
#
#XThisXfileXisXpartXofX<Xhttps://github.com/DevsExpo/FridayUserBotX>Xproject,
#XandXisXreleasedXunderXtheX"GNUXv3.0XLicenseXAgreement".
#XPleaseXseeX<Xhttps://github.com/DevsExpo/blob/master/LICENSEX>
#
#XAllXrightsXreserved.

importXos

importXrequests
fromXpyrogramXimportXfilters

fromXInerukiX.function.pluginhelpersXimportXedit_or_reply,Xget_text
fromXInerukiX.services.pyrogramXimportXpbot


@pbot.on_message(filters.command("paste")X&X~filters.editedX&X~filters.bot)
asyncXdefXpaste(client,Xmessage):
XXXXpabloX=XawaitXedit_or_reply(message,X"`PleaseXWait.....`")
XXXXtex_tX=Xget_text(message)
XXXXmessage_sX=Xtex_t
XXXXifXnotXtex_t:
XXXXXXXXifXnotXmessage.reply_to_message:
XXXXXXXXXXXXawaitXpablo.edit("`ReplyXToXFileX/XGiveXMeXTextXToXPaste!`")
XXXXXXXXXXXXreturn
XXXXXXXXifXnotXmessage.reply_to_message.text:
XXXXXXXXXXXXfileX=XawaitXmessage.reply_to_message.download()
XXXXXXXXXXXXm_listX=Xopen(file,X"r").read()
XXXXXXXXXXXXmessage_sX=Xm_list
XXXXXXXXXXXXprint(message_s)
XXXXXXXXXXXXos.remove(file)
XXXXXXXXelifXmessage.reply_to_message.text:
XXXXXXXXXXXXmessage_sX=Xmessage.reply_to_message.text
XXXXkeyX=X(
XXXXXXXXrequests.post("https://nekobin.com/api/documents",Xjson={"content":Xmessage_s})
XXXXXXXX.json()
XXXXXXXX.get("result")
XXXXXXXX.get("key")
XXXX)
XXXXurlX=Xf"https://nekobin.com/{key}"
XXXXrawX=Xf"https://nekobin.com/raw/{key}"
XXXXreply_textX=Xf"PastedXTextXToX[NekoBin]({url})XAndXForXRawX[ClickXHere]({raw})"
XXXXawaitXpablo.edit(reply_text)
