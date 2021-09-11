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

importdatetime
importio
importmath
importos
fromioimportBytesIO

importrequests
fromaiogram.types.input_fileimportInputFile
frombs4importBeautifulSoupasbs
fromPILimportImage
frompyrogramimportfilters
fromtelethonimport*
fromtelethon.errors.rpcerrorlistimportStickersetInvalidError
fromtelethon.tl.functions.messagesimportGetStickerSetRequest
fromtelethon.tl.typesimport(
DocumentAttributeSticker,
InputStickerSetID,
InputStickerSetShortName,
MessageMediaPhoto,
)

fromInerukiimportbot
fromIneruki.decoratorimportregister
fromIneruki.services.eventsimportregisterasIneruki
fromIneruki.services.pyrogramimportpbot
fromIneruki.services.telethonimporttbot
fromIneruki.services.telethonuserbotimportubot

from.utils.disableimportdisableable_dec
from.utils.languageimportget_strings_dec


defis_it_animated_sticker(message):
try:
ifmessage.mediaandmessage.media.document:
mime_type=message.media.document.mime_type
if"tgsticker"inmime_type:
returnTrue
returnFalse
returnFalse
exceptBaseException:
returnFalse


defis_message_image(message):
ifmessage.media:
ifisinstance(message.media,MessageMediaPhoto):
returnTrue
ifmessage.media.document:
ifmessage.media.document.mime_type.split("/")[0]=="image":
returnTrue
returnFalse
returnFalse


asyncdefsilently_send_message(conv,text):
awaitconv.send_message(text)
response=awaitconv.get_response()
awaitconv.mark_read(message=response)
returnresponse


asyncdefstickerset_exists(conv,setname):
try:
awaittbot(GetStickerSetRequest(InputStickerSetShortName(setname)))
response=awaitsilently_send_message(conv,"/addsticker")
ifresponse.text=="Invalidpackselected.":
awaitsilently_send_message(conv,"/cancel")
returnFalse
awaitsilently_send_message(conv,"/cancel")
returnTrue
exceptStickersetInvalidError:
returnFalse


defresize_image(image,save_locaton):
"""CopyrightRhyseSimpson:
https://github.com/skittles9823/SkittBot/blob/master/tg_bot/modules/stickers.py
"""
im=Image.open(image)
maxsize=(512,512)
if(im.widthandim.height)<512:
size1=im.width
size2=im.height
ifim.width>im.height:
scale=512/size1
size1new=512
size2new=size2*scale
else:
scale=512/size2
size1new=size1*scale
size2new=512
size1new=math.floor(size1new)
size2new=math.floor(size2new)
sizenew=(size1new,size2new)
im=im.resize(sizenew)
else:
im.thumbnail(maxsize)
im.save(save_locaton,"PNG")


deffind_instance(items,class_or_tuple):
foriteminitems:
ifisinstance(item,class_or_tuple):
returnitem
returnNone


@Ineruki(pattern="^/searchsticker(.*)")
asyncdef_(event):
input_str=event.pattern_match.group(1)
combot_stickers_url="https://combot.org/telegram/stickers?q="
text=requests.get(combot_stickers_url+input_str)
soup=bs(text.text,"lxml")
results=soup.find_all("a",{"class":"sticker-pack__btn"})
titles=soup.find_all("div","sticker-pack__title")
ifnotresults:
awaitevent.reply("Noresultsfound:(")
return
reply=f"StickersRelatedto**{input_str}**:"
forresult,titleinzip(results,titles):
link=result["href"]
reply+=f"\nâ€¢[{title.get_text()}]({link})"
awaitevent.reply(reply)


@Ineruki(pattern="^/packinfo$")
asyncdef_(event):
approved_userss=approved_users.find({})
forchinapproved_userss:
iid=ch["id"]
userss=ch["user"]
ifevent.is_group:
ifawaitis_register_admin(event.input_chat,event.message.sender_id):
pass
elifevent.chat_id==iidandevent.sender_id==userss:
pass
else:
return

ifnotevent.is_reply:
awaitevent.reply("Replytoanystickertogetit'spackinfo.")
return
rep_msg=awaitevent.get_reply_message()
ifnotrep_msg.document:
awaitevent.reply("Replytoanystickertogetit'spackinfo.")
return
stickerset_attr_s=rep_msg.document.attributes
stickerset_attr=find_instance(stickerset_attr_s,DocumentAttributeSticker)
ifnotstickerset_attr.stickerset:
awaitevent.reply("stickerdoesnotbelongtoapack.")
return
get_stickerset=awaittbot(
GetStickerSetRequest(
InputStickerSetID(
id=stickerset_attr.stickerset.id,
access_hash=stickerset_attr.stickerset.access_hash,
)
)
)
pack_emojis=[]
fordocument_stickeringet_stickerset.packs:
ifdocument_sticker.emoticonnotinpack_emojis:
pack_emojis.append(document_sticker.emoticon)
awaitevent.reply(
f"**StickerTitle:**`{get_stickerset.set.title}\n`"
f"**StickerShortName:**`{get_stickerset.set.short_name}`\n"
f"**Official:**`{get_stickerset.set.official}`\n"
f"**Archived:**`{get_stickerset.set.archived}`\n"
f"**StickersInPack:**`{len(get_stickerset.packs)}`\n"
f"**EmojisInPack:**{''.join(pack_emojis)}"
)


deffind_instance(items,class_or_tuple):
foriteminitems:
ifisinstance(item,class_or_tuple):
returnitem
returnNone


DEFAULTUSER="Ineruki"
FILLED_UP_DADDY="Invalidpackselected."


asyncdefget_sticker_emoji(event):
reply_message=awaitevent.get_reply_message()
try:
final_emoji=reply_message.media.document.attributes[1].alt
except:
final_emoji="😎"
returnfinal_emoji


@Ineruki(pattern="^/kang?(.*)")
asyncdef_(event):
ifnotevent.is_reply:
awaitevent.reply("PLease,ReplyToASticker/ImageToAddItYourPack")
return
reply_message=awaitevent.get_reply_message()
sticker_emoji=awaitget_sticker_emoji(event)
input_str=event.pattern_match.group(1)
ifinput_str:
sticker_emoji=input_str
user=awaitevent.get_sender()
ifnotuser.first_name:
user.first_name=user.id
pack=1
userid=event.sender_id
first_name=user.first_name
packname=f"{first_name}'sStickerVol.{pack}"
packshortname=f"Ineruki_stickers_{userid}"
kanga=awaitevent.reply(
"Hello,ThisStickerLooksNoice.MindifInerukistealit"
)
is_a_s=is_it_animated_sticker(reply_message)
file_ext_ns_ion="Stickers.png"
file=awaitevent.client.download_file(reply_message.media)
uploaded_sticker=None
ifis_a_s:
file_ext_ns_ion="AnimatedSticker.tgs"
uploaded_sticker=awaitubot.upload_file(file,file_name=file_ext_ns_ion)
packname=f"{first_name}'sAnimatedStickerVol.{pack}"
packshortname=f"Ineruki_animated_{userid}"
elifnotis_message_image(reply_message):
awaitkanga.edit("Ohno..ThisMessagetypeisinvalid")
return
else:
withBytesIO(file)asmem_file,BytesIO()assticker:
resize_image(mem_file,sticker)
sticker.seek(0)
uploaded_sticker=awaitubot.upload_file(
sticker,file_name=file_ext_ns_ion
)

awaitkanga.edit("ThisStickerisGonnaGetStolen.....")

asyncwithubot.conversation("@Stickers")asd_conv:
now=datetime.datetime.now()
dt=now+datetime.timedelta(minutes=1)
ifnotawaitstickerset_exists(d_conv,packshortname):

awaitsilently_send_message(d_conv,"/cancel")
ifis_a_s:
response=awaitsilently_send_message(d_conv,"/newanimated")
else:
response=awaitsilently_send_message(d_conv,"/newpack")
if"Yay!"notinresponse.text:
awaittbot.edit_message(
kanga,f"**Error**!@Stickersreplied:{response.text}"
)
return
response=awaitsilently_send_message(d_conv,packname)
ifnotresponse.text.startswith("Alright!"):
awaittbot.edit_message(
kanga,f"**Error**!@Stickersreplied:{response.text}"
)
return
w=awaitd_conv.send_file(
file=uploaded_sticker,allow_cache=False,force_document=True
)
response=awaitd_conv.get_response()
if"Sorry"inresponse.text:
awaittbot.edit_message(
kanga,f"**Error**!@Stickersreplied:{response.text}"
)
return
awaitsilently_send_message(d_conv,sticker_emoji)
awaitsilently_send_message(d_conv,"/publish")
response=awaitsilently_send_message(d_conv,f"<{packname}>")
awaitsilently_send_message(d_conv,"/skip")
response=awaitsilently_send_message(d_conv,packshortname)
ifresponse.text=="Sorry,thisshortnameisalreadytaken.":
awaittbot.edit_message(
kanga,f"**Error**!@Stickersreplied:{response.text}"
)
return
else:
awaitsilently_send_message(d_conv,"/cancel")
awaitsilently_send_message(d_conv,"/addsticker")
awaitsilently_send_message(d_conv,packshortname)
awaitd_conv.send_file(
file=uploaded_sticker,allow_cache=False,force_document=True
)
response=awaitd_conv.get_response()
ifresponse.text==FILLED_UP_DADDY:
whileresponse.text==FILLED_UP_DADDY:
pack+=1
prevv=int(pack)-1
packname=f"{first_name}'sStickerVol.{pack}"
packshortname=f"Vol_{pack}_with_{userid}"

ifnotawaitstickerset_exists(d_conv,packshortname):
awaittbot.edit_message(
kanga,
"**PackNo.**"
+str(prevv)
+"**isfull!MakinganewPack,Vol.**"
+str(pack),
)
ifis_a_s:
response=awaitsilently_send_message(
d_conv,"/newanimated"
)
else:
response=awaitsilently_send_message(d_conv,"/newpack")
if"Yay!"notinresponse.text:
awaittbot.edit_message(
kanga,f"**Error**!@Stickersreplied:{response.text}"
)
return
response=awaitsilently_send_message(d_conv,packname)
ifnotresponse.text.startswith("Alright!"):
awaittbot.edit_message(
kanga,f"**Error**!@Stickersreplied:{response.text}"
)
return
w=awaitd_conv.send_file(
file=uploaded_sticker,
allow_cache=False,
force_document=True,
)
response=awaitd_conv.get_response()
if"Sorry"inresponse.text:
awaittbot.edit_message(
kanga,f"**Error**!@Stickersreplied:{response.text}"
)
return
awaitsilently_send_message(d_conv,sticker_emoji)
awaitsilently_send_message(d_conv,"/publish")
response=awaitsilently_send_message(
bot_conv,f"<{packname}>"
)
awaitsilently_send_message(d_conv,"/skip")
response=awaitsilently_send_message(d_conv,packshortname)
ifresponse.text=="Sorry,thisshortnameisalreadytaken.":
awaittbot.edit_message(
kanga,f"**Error**!@Stickersreplied:{response.text}"
)
return
else:
awaittbot.edit_message(
kanga,
"**PackNo.**"
+str(prevv)
+"**isfull!SwitchingtoVol.**"
+str(pack),
)
awaitsilently_send_message(d_conv,"/addsticker")
awaitsilently_send_message(d_conv,packshortname)
awaitd_conv.send_file(
file=uploaded_sticker,
allow_cache=False,
force_document=True,
)
response=awaitd_conv.get_response()
if"Sorry"inresponse.text:
awaittbot.edit_message(
kanga,f"**Error**!@Stickersreplied:{response.text}"
)
return
awaitsilently_send_message(d_conv,sticker_emoji)
awaitsilently_send_message(d_conv,"/done")
else:
if"Sorry"inresponse.text:
awaittbot.edit_message(
kanga,f"**Error**!@Stickersreplied:{response.text}"
)
return
awaitsilently_send_message(d_conv,response)
awaitsilently_send_message(d_conv,sticker_emoji)
awaitsilently_send_message(d_conv,"/done")
awaitkanga.edit("InvitingThisStickerToYourPack🚶")
awaitkanga.edit(
f"ThisStickerHasCameToYourPack.`\n**CheckItOut**[Here](t.me/addstickers/{packshortname})"
)
os.system("rm-rfStickers.png")
os.system("rm-rfAnimatedSticker.tgs")
os.system("rm-rf*.webp")


@Ineruki(pattern="^/rmkang$")
asyncdef_(event):
try:
ifnotevent.is_reply:
awaitevent.reply(
"Replytoastickertoremoveitfromyourpersonalstickerpack."
)
return
reply_message=awaitevent.get_reply_message()
kanga=awaitevent.reply("`Deleting.`")

ifnotis_message_image(reply_message):
awaitkanga.edit("Pleasereplytoasticker.")
return

rmsticker=awaitubot.get_messages(event.chat_id,ids=reply_message.id)

stickerset_attr_s=reply_message.document.attributes
stickerset_attr=find_instance(stickerset_attr_s,DocumentAttributeSticker)
ifnotstickerset_attr.stickerset:
awaitevent.reply("Stickerdoesnotbelongtoapack.")
return

get_stickerset=awaittbot(
GetStickerSetRequest(
InputStickerSetID(
id=stickerset_attr.stickerset.id,
access_hash=stickerset_attr.stickerset.access_hash,
)
)
)

packname=get_stickerset.set.short_name

sresult=(
awaitubot(
functions.messages.GetStickerSetRequest(
InputStickerSetShortName(packname)
)
)
).documents
forcinsresult:
ifint(c.id)==int(stickerset_attr.stickerset.id):
pass
else:
awaitkanga.edit(
"Thisstickerisalreadyremovedfromyourpersonalstickerpack."
)
return

awaitkanga.edit("`Deleting..`")

asyncwithubot.conversation("@Stickers")asbot_conv:

awaitsilently_send_message(bot_conv,"/cancel")
response=awaitsilently_send_message(bot_conv,"/delsticker")
if"Choose"notinresponse.text:
awaittbot.edit_message(
kanga,f"**FAILED**!@Stickersreplied:{response.text}"
)
return
response=awaitsilently_send_message(bot_conv,packname)
ifnotresponse.text.startswith("Please"):
awaittbot.edit_message(
kanga,f"**FAILED**!@Stickersreplied:{response.text}"
)
return
try:
awaitrmsticker.forward_to("@Stickers")
exceptExceptionase:
print(e)
ifresponse.text.startswith("Thispackhasonly"):
awaitsilently_send_message(bot_conv,"Deleteanyway")

awaitkanga.edit("`Deleting...`")
response=awaitbot_conv.get_response()
ifnot"Ihavedeleted"inresponse.text:
awaittbot.edit_message(
kanga,f"**FAILED**!@Stickersreplied:{response.text}"
)
return

awaitkanga.edit(
"Successfullydeletedthatstickerfromyourpersonalpack."
)
exceptExceptionase:
os.remove("sticker.webp")
print(e)


@register(cmds="getsticker")
@disableable_dec("getsticker")
@get_strings_dec("stickers")
asyncdefget_sticker(message,strings):
if"reply_to_message"notinmessageor"sticker"notinmessage.reply_to_message:
awaitmessage.reply(strings["rpl_to_sticker"])
return

sticker=message.reply_to_message.sticker
file_id=sticker.file_id
text=strings["ur_sticker"].format(emoji=sticker.emoji,id=file_id)

sticker_file=awaitbot.download_file_by_id(file_id,io.BytesIO())

awaitmessage.reply_document(
InputFile(
sticker_file,filename=f"{sticker.set_name}_{sticker.file_id[:5]}.png"
),
text,
)


@pbot.on_message(filters.command("sticker_id")&~filters.edited)
asyncdefsticker_id(_,message):
ifnotmessage.reply_to_message:
awaitmessage.reply_text("Replytoasticker.")
return
ifnotmessage.reply_to_message.sticker:
awaitmessage.reply_text("Replytoasticker.")
return
file_id=message.reply_to_message.sticker.file_id
awaitmessage.reply_text(f"`{file_id}`")


__mod_name__="Stickers"

__help__="""
Stickersarethebestwaytoshowemotion.

<b>Availablecommands:</b>
-/searchsticker:Searchstickersforgivenquery.
-/packinfo:Replytoastickertogetit'spackinfo
-/getsticker:Uploadsthe.pngofthestickeryou'verepliedto
-/sticker_id:ReplytoStickerforgettingstickerId.
-/kang[Emojiforsticker][replytoImage/Sticker]:Kangrepliedsticker/image.
-/rmkang[REPLY]:Removerepliedstickerfromyourkangpack.
"""
