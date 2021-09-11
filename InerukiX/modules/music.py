#Copyright(C)2021errorshivansh


#ThisfileispartofIneruki(TelegramBot)

#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseas
#publishedbytheFreeSoftwareFoundation,eitherversion3ofthe
#License,or(atyouroption)anylaterversion.

#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.

#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<http://www.gnu.org/licenses/>.

importio
importos

importlyricsgenius
frompyrogramimportfilters
fromtswiftimportSong

fromIneruki.configimportget_str_key
fromIneruki.services.pyrogramimportpbot

GENIUS=get_str_key("GENIUS_API_TOKEN",None)


#Lel,Didn'tGetTimeToMakeNewOneSoUsedPluginMadebr@mrconfusedand@sandy1709donteditcredits


@pbot.on_message(filters.command(["lyric","lyrics"]))
asyncdef_(client,message):
lel=awaitmessage.reply("SearchingForLyrics.....")
query=message.text
ifnotquery:
awaitlel.edit("`WhatIamSupposedtofind`")
return

song=""
song=Song.find_song(query)
ifsong:
ifsong.lyrics:
reply=song.format()
else:
reply="Couldn'tfindanylyricsforthatsong!trywithartistnamealongwithsongifstilldoesntworktry`.glyrics`"
else:
reply="lyricsnotfound!trywithartistnamealongwithsongifstilldoesntworktry`.glyrics`"

iflen(reply)>4095:
withio.BytesIO(str.encode(reply))asout_file:
out_file.name="lyrics.text"
awaitclient.send_document(
message.chat.id,
out_file,
force_document=True,
allow_cache=False,
caption=query,
reply_to_msg_id=message.message_id,
)
awaitlel.delete()
else:
awaitlel.edit(reply)#editorreply


@pbot.on_message(filters.command(["glyric","glyrics"]))
asyncdeflyrics(client,message):

ifr"-"inmessage.text:
pass
else:
awaitmessage.reply(
"`Error:pleaseuse'-'asdividerfor<artist>and<song>`\n"
"eg:`.glyricsNickiMinaj-SuperBass`"
)
return

ifGENIUSisNone:
awaitmessage.reply(
"`Providegeniusaccesstokentoconfig.pyorHerokuConfigfirstkthxbye!`"
)
else:
genius=lyricsgenius.Genius(GENIUS)
try:
args=message.text.split(".lyrics")[1].split("-")
artist=args[0].strip("")
song=args[1].strip("")
exceptException:
awaitmessage.reply("`Lelpleaseprovideartistandsongnames`")
return

iflen(args)<1:
awaitmessage.reply("`Pleaseprovideartistandsongnames`")
return

lel=awaitmessage.reply(f"`Searchinglyricsfor{artist}-{song}...`")

try:
songs=genius.search_song(song,artist)
exceptTypeError:
songs=None

ifsongsisNone:
awaitlel.edit(f"Song**{artist}-{song}**notfound!")
return
iflen(songs.lyrics)>4096:
awaitlel.edit("`Lyricsistoobig,viewthefiletoseeit.`")
withopen("lyrics.txt","w+")asf:
f.write(f"Searchquery:\n{artist}-{song}\n\n{songs.lyrics}")
awaitclient.send_document(
message.chat.id,
"lyrics.txt",
reply_to_msg_id=message.message_id,
)
os.remove("lyrics.txt")
else:
awaitlel.edit(
f"**Searchquery**:\n`{artist}-{song}`\n\n```{songs.lyrics}```"
)
return


__mod_name__="Music"

__help__="""
/video<i>query</i>:downloadvideofromyoutube.
/deezer<i>query</i>:downloadfromdeezer.
/saavn<I>query</i>:downloadsongfromsaavn.
/music<i>query</i>:downloadsongfromytservers.(APIBASED)
/lyrics<i>songname</i>:Thispluginsearchesforsonglyricswithsongname.
/glyrics<i>songname</i>:Thispluginsearchesforsonglyricswithsongnameandartist.
"""
