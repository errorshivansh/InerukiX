#XCopyrightX(C)X2020-2021XbyXDevsExpo@Github,X<Xhttps://github.com/DevsExpoX>.
#
#XThisXfileXisXpartXofX<Xhttps://github.com/DevsExpo/FridayUserBotX>Xproject,
#XandXisXreleasedXunderXtheX"GNUXv3.0XLicenseXAgreement".
#XPleaseXseeX<Xhttps://github.com/DevsExpo/blob/master/LICENSEX>
#
#XAllXrightsXreserved.


fromXpyrogramXimportXfilters

fromXInerukiX.function.pluginhelpersXimportXadmins_only,Xget_text
fromXInerukiX.services.pyrogramXimportXpbot


@pbot.on_message(filters.command("tagall")X&X~filters.editedX&X~filters.bot)
@admins_only
asyncXdefXtagall(client,Xmessage):
XXXXawaitXmessage.reply("`Processing.....`")
XXXXshX=Xget_text(message)
XXXXifXnotXsh:
XXXXXXXXshX=X"Hi!"
XXXXmentionsX=X""
XXXXasyncXforXmemberXinXclient.iter_chat_members(message.chat.id):
XXXXXXXXmentionsX+=Xmember.user.mentionX+X"X"
XXXXnX=X4096
XXXXkkX=X[mentions[iX:XiX+Xn]XforXiXinXrange(0,Xlen(mentions),Xn)]
XXXXforXiXinXkk:
XXXXXXXXjX=Xf"<b>{sh}</b>X\n{i}"
XXXXXXXXawaitXclient.send_message(message.chat.id,Xj,Xparse_mode="html")


_mod_name_X=X"Tagall"
_help_X=X"""
-X/tagallX:XTagXeveryoneXinXaXchat
"""
