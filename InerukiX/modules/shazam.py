importos
fromjsonimportJSONDecodeError

importrequests

#importffmpeg
frompyrogramimportfilters

fromIneruki.function.pluginhelpersimportadmins_only,edit_or_reply,fetch_audio
fromIneruki.services.pyrogramimportpbot


@pbot.on_message(filters.command(["identify","shazam"]))
@admins_only
asyncdefshazamm(client,message):
kek=awaitedit_or_reply(message,"`ShazamingInProgress!`")
ifnotmessage.reply_to_message:
awaitkek.edit("ReplyToTheAudio.")
return
ifos.path.exists("friday.mp3"):
os.remove("friday.mp3")
kkk=awaitfetch_audio(client,message)
downloaded_file_name=kkk
f={"file":(downloaded_file_name,open(downloaded_file_name,"rb"))}
awaitkek.edit("**SearchingForThisSongInFriday'sDataBase.**")
r=requests.post("https://starkapi.herokuapp.com/shazam/",files=f)
try:
xo=r.json()
exceptJSONDecodeError:
awaitkek.edit(
"`SeemsLikeOurServerHasSomeIssues,PleaseTryAgainLater!`"
)
return
ifxo.get("success")isFalse:
awaitkek.edit("`SongNotFoundINDatabase.PleaseTryAgain.`")
os.remove(downloaded_file_name)
return
xoo=xo.get("response")
zz=xoo[1]
zzz=zz.get("track")
zzz.get("sections")[3]
nt=zzz.get("images")
image=nt.get("coverarthq")
by=zzz.get("subtitle")
title=zzz.get("title")
messageo=f"""<b>SongShazamed.</b>
<b>SongName:</b>{title}
<b>SongBy:</b>{by}
<u><b>IdentifiedUsing@InerukiBot-Joinoursupport@InerukiSupport_Official</b></u>
<i>Poweredby@FridayOT</i>
"""
awaitclient.send_photo(message.chat.id,image,messageo,parse_mode="HTML")
os.remove(downloaded_file_name)
awaitkek.delete()


#__mod_name__="Shazam"
#__help__="""
#<b>SHAZAMMER</b>
#<u>Findanysongwithit'smusicorpartofsong</u>
#-/shazam:identifythesongfromFriday'sDatabase

#<i>Specialcreditstofridayuserbot</i>
#"""
