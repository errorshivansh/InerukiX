#XCopyrightX(C)X2021Xerrorshivansh


#XThisXfileXisXpartXofXInerukiX(TelegramXBot)

#XThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXas
#XpublishedXbyXtheXFreeXSoftwareXFoundation,XeitherXversionX3XofXthe
#XLicense,XorX(atXyourXoption)XanyXlaterXversion.

#XThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.

#XYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XalongXwithXthisXprogram.XXIfXnot,XseeX<http://www.gnu.org/licenses/>.

importXio
importXos

importXlyricsgenius
fromXpyrogramXimportXfilters
fromXtswiftXimportXSong

fromXInerukiX.configXimportXget_str_key
fromXInerukiX.services.pyrogramXimportXpbot

GENIUSX=Xget_str_key("GENIUS_API_TOKEN",XNone)


#XLel,XDidn'tXGetXTimeXToXMakeXNewXOneXSoXUsedXPluginXMadeXbrX@mrconfusedXandX@sandy1709XdontXeditXcredits


@pbot.on_message(filters.command(["lyric",X"lyrics"]))
asyncXdefX_(client,Xmessage):
XXXXlelX=XawaitXmessage.reply("SearchingXForXLyrics.....")
XXXXqueryX=Xmessage.text
XXXXifXnotXquery:
XXXXXXXXawaitXlel.edit("`WhatXIXamXSupposedXtoXfindX`")
XXXXXXXXreturn

XXXXsongX=X""
XXXXsongX=XSong.find_song(query)
XXXXifXsong:
XXXXXXXXifXsong.lyrics:
XXXXXXXXXXXXreplyX=Xsong.format()
XXXXXXXXelse:
XXXXXXXXXXXXreplyX=X"Couldn'tXfindXanyXlyricsXforXthatXsong!XtryXwithXartistXnameXalongXwithXsongXifXstillXdoesntXworkXtryX`.glyrics`"
XXXXelse:
XXXXXXXXreplyX=X"lyricsXnotXfound!XtryXwithXartistXnameXalongXwithXsongXifXstillXdoesntXworkXtryX`.glyrics`"

XXXXifXlen(reply)X>X4095:
XXXXXXXXwithXio.BytesIO(str.encode(reply))XasXout_file:
XXXXXXXXXXXXout_file.nameX=X"lyrics.text"
XXXXXXXXXXXXawaitXclient.send_document(
XXXXXXXXXXXXXXXXmessage.chat.id,
XXXXXXXXXXXXXXXXout_file,
XXXXXXXXXXXXXXXXforce_document=True,
XXXXXXXXXXXXXXXXallow_cache=False,
XXXXXXXXXXXXXXXXcaption=query,
XXXXXXXXXXXXXXXXreply_to_msg_id=message.message_id,
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXlel.delete()
XXXXelse:
XXXXXXXXawaitXlel.edit(reply)XX#XeditXorXreply


@pbot.on_message(filters.command(["glyric",X"glyrics"]))
asyncXdefXlyrics(client,Xmessage):

XXXXifXr"-"XinXmessage.text:
XXXXXXXXpass
XXXXelse:
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXX"`Error:XpleaseXuseX'-'XasXdividerXforX<artist>XandX<song>`\n"
XXXXXXXXXXXX"eg:X`.glyricsXNickiXMinajX-XSuperXBass`"
XXXXXXXX)
XXXXXXXXreturn

XXXXifXGENIUSXisXNone:
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXX"`ProvideXgeniusXaccessXtokenXtoXconfig.pyXorXHerokuXConfigXfirstXkthxbye!`"
XXXXXXXX)
XXXXelse:
XXXXXXXXgeniusX=Xlyricsgenius.Genius(GENIUS)
XXXXXXXXtry:
XXXXXXXXXXXXargsX=Xmessage.text.split(".lyrics")[1].split("-")
XXXXXXXXXXXXartistX=Xargs[0].strip("X")
XXXXXXXXXXXXsongX=Xargs[1].strip("X")
XXXXXXXXexceptXException:
XXXXXXXXXXXXawaitXmessage.reply("`LelXpleaseXprovideXartistXandXsongXnames`")
XXXXXXXXXXXXreturn

XXXXifXlen(args)X<X1:
XXXXXXXXawaitXmessage.reply("`PleaseXprovideXartistXandXsongXnames`")
XXXXXXXXreturn

XXXXlelX=XawaitXmessage.reply(f"`SearchingXlyricsXforX{artist}X-X{song}...`")

XXXXtry:
XXXXXXXXsongsX=Xgenius.search_song(song,Xartist)
XXXXexceptXTypeError:
XXXXXXXXsongsX=XNone

XXXXifXsongsXisXNone:
XXXXXXXXawaitXlel.edit(f"SongX**{artist}X-X{song}**XnotXfound!")
XXXXXXXXreturn
XXXXifXlen(songs.lyrics)X>X4096:
XXXXXXXXawaitXlel.edit("`LyricsXisXtooXbig,XviewXtheXfileXtoXseeXit.`")
XXXXXXXXwithXopen("lyrics.txt",X"w+")XasXf:
XXXXXXXXXXXXf.write(f"SearchXquery:X\n{artist}X-X{song}\n\n{songs.lyrics}")
XXXXXXXXawaitXclient.send_document(
XXXXXXXXXXXXmessage.chat.id,
XXXXXXXXXXXX"lyrics.txt",
XXXXXXXXXXXXreply_to_msg_id=message.message_id,
XXXXXXXX)
XXXXXXXXos.remove("lyrics.txt")
XXXXelse:
XXXXXXXXawaitXlel.edit(
XXXXXXXXXXXXf"**SearchXquery**:X\n`{artist}X-X{song}`\n\n```{songs.lyrics}```"
XXXXXXXX)
XXXXreturn


__mod_name__X=X"Music"

__help__X=X"""
/videoX<i>query</i>:XdownloadXvideoXfromXyoutube.X
/deezerX<i>query</i>:XdownloadXfromXdeezer.X
/saavnX<I>query</i>:XdownloadXsongXfromXsaavn.X
/musicX<i>query</i>:XdownloadXsongXfromXytXservers.X(APIXBASED)X
/lyricsX<i>songXname</i>X:XThisXpluginXsearchesXforXsongXlyricsXwithXsongXname.
/glyricsX<i>XsongXnameX</i>X:XThisXpluginXsearchesXforXsongXlyricsXwithXsongXnameXandXartist.
"""
