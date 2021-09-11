#Copyright(C)2020-2021byDevsExpo@Github,<https://github.com/DevsExpo>.
#
#Thisfileispartof<https://github.com/DevsExpo/FridayUserBot>project,
#andisreleasedunderthe"GNUv3.0LicenseAgreement".
#Pleasesee<https://github.com/DevsExpo/blob/master/LICENSE>
#
#Allrightsreserved.


frompyrogramimportfilters

fromIneruki.function.pluginhelpersimportadmins_only,get_text
fromIneruki.services.pyrogramimportpbot


@pbot.on_message(filters.command("tagall")&~filters.edited&~filters.bot)
@admins_only
asyncdeftagall(client,message):
awaitmessage.reply("`Processing.....`")
sh=get_text(message)
ifnotsh:
sh="Hi!"
mentions=""
asyncformemberinclient.iter_chat_members(message.chat.id):
mentions+=member.user.mention+""
n=4096
kk=[mentions[i:i+n]foriinrange(0,len(mentions),n)]
foriinkk:
j=f"<b>{sh}</b>\n{i}"
awaitclient.send_message(message.chat.id,j,parse_mode="html")


_mod_name_="Tagall"
_help_="""
-/tagall:Tageveryoneinachat
"""
