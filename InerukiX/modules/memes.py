#Thisfileiscopiedfrom@Missjuliarobot
#Fullcreditstooriginalauthor

importasyncio
importio
importjson
importos
importrandom
importre
importstring
importsubprocess
importtextwrap
importurllib.request
fromrandomimportrandint,randrange,uniform

importemoji
importnltk
fromcowpyimportcow
fromfontTools.ttLibimportTTFont
fromPILimportImage,ImageDraw,ImageEnhance,ImageFont,ImageOps
fromseleniumimportwebdriver
fromselenium.webdriver.chrome.optionsimportOptions
fromtelethonimport*
fromtelethon.tlimportfunctions
fromtelethon.tl.typesimport*
fromzalgo_textimportzalgo

fromInerukiimport*
fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbot
fromIneruki.services.telethonuserbotimportubot

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

WIDE_MAP={i:i+0xFEE0foriinrange(0x21,0x7F)}
WIDE_MAP[0x20]=0x3000


@register(pattern="^/owu$")
asyncdefmsg(event):

reply_tex=awaitevent.get_reply_message()
reply_text=reply_tex.text
ifreply_textisNone:
awaitevent.reply("Replytoamessagetomakememe.")
return
faces=[
"(・`ω´・)",
";;w;;",
"owo",
"UwU",
">w<",
"^w^",
r"\(^o\)(/o^)/",
"(^_^)∠☆",
"(ô_ô)",
"~:o",
";____;",
"(*^*)",
"(>_",
"(♥_♥)",
"*(^O^)*",
"((+_+))",
]
text=re.sub(r"[rl]","w",reply_text)
text=re.sub(r"[ｒｌ]","ｗ",reply_text)
text=re.sub(r"[RL]","W",text)
text=re.sub(r"[ＲＬ]","Ｗ",text)
text=re.sub(r"n([aeiouａｅｉｏｕ])",r"ny\1",text)
text=re.sub(r"ｎ([ａｅｉｏｕ])",r"ｎｙ\1",text)
text=re.sub(r"N([aeiouAEIOU])",r"Ny\1",text)
text=re.sub(r"Ｎ([ａｅｉｏｕＡＥＩＯＵ])",r"Ｎｙ\1",text)
text=re.sub(r"\!+",""+random.choice(faces),text)
text=re.sub(r"！+",""+random.choice(faces),text)
text=text.replace("ove","uv")
text=text.replace("ｏｖｅ","ｕｖ")
text+=""+random.choice(faces)
awaitevent.reply(text)


@register(pattern="^/copypasta$")
asyncdefmsg(event):

rtex=awaitevent.get_reply_message()
rtext=rtex.text
ifrtextisNone:
awaitevent.reply("Replytoamessagettomakememe.")
return
emojis=[
"😂",
"😂",
"👌",
"✌",
"💞",
"👍",
"👌",
"💯",
"🎶",
"👀",
"😂",
"👓",
"👏",
"👐",
"🍕",
"💥",
"🍴",
"💦",
"💦",
"🍑",
"🍆",
"😩",
"😏",
"👉👌",
"👀",
"👅",
"😩",
"🚰",
]
reply_text=random.choice(emojis)
b_char=random.choice(rtext).lower()
forcinrtext:
ifc=="":
reply_text+=random.choice(emojis)
elifcinemojis:
reply_text+=c
reply_text+=random.choice(emojis)
elifc.lower()==b_char:
reply_text+="🅱️"
else:
ifbool(random.getrandbits(1)):
reply_text+=c.upper()
else:
reply_text+=c.lower()
reply_text+=random.choice(emojis)
awaitevent.reply(reply_text)


@register(pattern="^/bmoji$")
asyncdefmsg(event):

rtex=awaitevent.get_reply_message()
rtext=rtex.text
ifrtextisNone:
awaitevent.reply("Replytoamessagetomakememe.")
return
b_char=random.choice(rtext).lower()
reply_text=rtext.replace(b_char,"🅱️").replace(b_char.upper(),"🅱️")
awaitevent.reply(reply_text)


@register(pattern="^/clapmoji$")
asyncdefmsg(event):

rtex=awaitevent.get_reply_message()
rtext=rtex.text
ifrtextisNone:
awaitevent.reply("Replytoamessagetomakememe.")
return
reply_text="👏"
reply_text+=rtext.replace("","👏")
reply_text+="👏"
awaitevent.reply(reply_text)


@register(pattern="^/stretch$")
asyncdefmsg(event):

rtex=awaitevent.get_reply_message()
rtext=rtex.text
ifrtextisNone:
awaitevent.reply("Replytoamessagetomakememe.")
return
count=random.randint(3,10)
reply_text=re.sub(r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵ])",(r"\1"*count),rtext)
awaitevent.reply(reply_text)


@register(pattern="^/vapor(?:|$)(.*)")
asyncdefmsg(event):

rtex=awaitevent.get_reply_message()
rtext=rtex.text
ifrtext:
data=rtext
else:
data=event.pattern_match.group(1)
ifdataisNone:
awaitevent.reply("Eitherprovidesomeinputorreplytoamessage.")
return

reply_text=str(data).translate(WIDE_MAP)
awaitevent.reply(reply_text)


@register(pattern="^/zalgofy$")
asyncdefmsg(event):

rtex=awaitevent.get_reply_message()
rtext=rtex.text
ifrtextisNone:
awaitevent.reply("Replytoamessagetomakememe.")
return
reply_text=zalgo.zalgo().zalgofy(rtext)
awaitevent.reply(reply_text)


@register(pattern="^/forbesify$")
asyncdefmsg(event):

rtex=awaitevent.get_reply_message()
rtext=rtex.text
ifrtextisNone:
awaitevent.reply("Replytoamessagetomakememe.")
return
data=rtext

data=data.lower()
accidentals=["VB","VBD","VBG","VBN"]
reply_text=data.split()
offset=0

tagged=dict(nltk.pos_tag(reply_text))

forkinrange(len(reply_text)):
i=reply_text[k+offset]
iftagged.get(i)inaccidentals:
reply_text.insert(k+offset,"accidentally")
offset+=1

reply_text=string.capwords("".join(reply_text))
awaitevent.reply(reply_text)


@register(pattern="^/shout(.*)")
asyncdefmsg(event):

rtext=event.pattern_match.group(1)

args=rtext

iflen(args)==0:
awaitevent.reply("Whereistext?")
return

msg="```"
text="".join(args)
result=[]
result.append("".join(list(text)))
forpos,symbolinenumerate(text[1:]):
result.append(symbol+""+""*pos+symbol)
result=list("\n".join(result))
result[0]=text[0]
result="".join(result)
msg="```\n"+result+"```"
awaitevent.reply(msg)


@register(pattern="^/angrymoji$")
asyncdefmsg(event):

rtex=awaitevent.get_reply_message()
rtext=rtex.text
ifrtextisNone:
awaitevent.reply("Replytoamessagetomakememe.")
return
reply_text="😡"
foriinrtext:
ifi=="":
reply_text+="😡"
else:
reply_text+=i
reply_text+="😡"
awaitevent.reply(reply_text)


@register(pattern="^/crymoji$")
asyncdefmsg(event):

rtex=awaitevent.get_reply_message()
rtext=rtex.text
ifrtextisNone:
awaitevent.reply("Replytoamessagetomakememe.")
return
reply_text="😭"
foriinrtext:
ifi=="":
reply_text+="😭"
else:
reply_text+=i
reply_text+="😭"
awaitevent.reply(reply_text)


CARBONLANG="en"


@register(pattern="^/carbon(.*)")
asyncdefcarbon_api(e):

jj="`Processing..`"
gg=awaite.reply(jj)
CARBON="https://carbon.now.sh/?bg=rgba(239%2C40%2C44%2C1)&t=one-light&wt=none&l=application%2Ftypescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={code}"
globalCARBONLANG
code=e.pattern_match.group(1)
awaitgg.edit("`Processing..\n25%`")
os.chdir("./")
ifos.path.isfile("./carbon.png"):
os.remove("./carbon.png")
url=CARBON.format(code=code,lang=CARBONLANG)
chrome_options=Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location=GOOGLE_CHROME_BIN
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
prefs={"download.default_directory":"./"}
chrome_options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome(executable_path=CHROME_DRIVER,options=chrome_options)
driver.get(url)
awaitgg.edit("`Processing..\n50%`")
download_path="./"
driver.command_executor._commands["send_command"]=(
"POST",
"/session/$sessionId/chromium/send_command",
)
params={
"cmd":"Page.setDownloadBehavior",
"params":{"behavior":"allow","downloadPath":download_path},
}
driver.execute("send_command",params)
driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
awaitgg.edit("`Processing..\n75%`")
whilenotos.path.isfile("./carbon.png"):
awaitasyncio.sleep(1)
awaitgg.edit("`Processing..\n100%`")
file="./carbon.png"
awaite.edit("`Uploading..`")
awaittbot.send_file(
e.chat_id,
file,
caption="Madeusing[Carbon](https://carbon.now.sh/about/),\
\naprojectby[DawnLabs](https://dawnlabs.io/)",
force_document=True,
)
os.remove("./carbon.png")
driver.quit()


@register(pattern="^/deepfry(?:|$)(.*)")
asyncdefdeepfryer(event):

try:
frycount=int(event.pattern_match.group(1))
iffrycount<1:
raiseValueError
exceptValueError:
frycount=1
ifevent.is_reply:
reply_message=awaitevent.get_reply_message()
data=awaitcheck_media(reply_message)
ifisinstance(data,bool):
awaitevent.reply("`Ican'tdeepfrythat!`")
return
else:
awaitevent.reply("`Replytoanimageorstickertodeepfryit!`")
return

image=io.BytesIO()
awaittbot.download_media(data,image)
image=Image.open(image)

for_inrange(frycount):
image=awaitdeepfry(image)
fried_io=io.BytesIO()
fried_io.name="image.jpeg"
image.save(fried_io,"JPEG")
fried_io.seek(0)
awaitevent.reply(file=fried_io)


asyncdefdeepfry(img:Image)->Image:
colours=(
(randint(50,200),randint(40,170),randint(40,190)),
(randint(190,255),randint(170,240),randint(180,250)),
)
img=img.copy().convert("RGB")
img=img.convert("RGB")
width,height=img.width,img.height
img=img.resize(
(int(width**uniform(0.8,0.9)),int(height**uniform(0.8,0.9))),
resample=Image.LANCZOS,
)
img=img.resize(
(int(width**uniform(0.85,0.95)),int(height**uniform(0.85,0.95))),
resample=Image.BILINEAR,
)
img=img.resize(
(int(width**uniform(0.89,0.98)),int(height**uniform(0.89,0.98))),
resample=Image.BICUBIC,
)
img=img.resize((width,height),resample=Image.BICUBIC)
img=ImageOps.posterize(img,randint(3,7))
overlay=img.split()[0]
overlay=ImageEnhance.Contrast(overlay).enhance(uniform(1.0,2.0))
overlay=ImageEnhance.Brightness(overlay).enhance(uniform(1.0,2.0))
overlay=ImageOps.colorize(overlay,colours[0],colours[1])
img=Image.blend(img,overlay,uniform(0.1,0.4))
img=ImageEnhance.Sharpness(img).enhance(randint(5,300))
returnimg


asyncdefcheck_media(reply_message):
ifreply_messageandreply_message.media:
ifreply_message.photo:
data=reply_message.photo
elifreply_message.document:
if(
DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
inreply_message.media.document.attributes
):
returnFalse
if(
reply_message.gif
orreply_message.video
orreply_message.audio
orreply_message.voice
):
returnFalse
data=reply_message.media.document
else:
returnFalse
else:
returnFalse
ifnotdataordataisNone:
returnFalse
returndata


@register(pattern="^/type(.*)")
asyncdeftypewriter(typew):

message=typew.pattern_match.group(1)
ifmessage:
pass
else:
awaittypew.reply("`Giveatexttotype!`")
return
typing_symbol="|"
old_text=""
now=awaittypew.reply(typing_symbol)
awaitasyncio.sleep(2)
forcharacterinmessage:
old_text=old_text+""+character
typing_text=old_text+""+typing_symbol
awaitnow.edit(typing_text)
awaitasyncio.sleep(2)
awaitnow.edit(old_text)
awaitasyncio.sleep(2)


@register(pattern="^/sticklet(.*)")
asyncdefsticklet(event):

R=random.randint(0,256)
G=random.randint(0,256)
B=random.randint(0,256)

#gettheinputtext
#thetextonwhichwewouldliketodothemagicon
sticktext=event.pattern_match.group(1)

#deletetheuserbotcommand,
#idon'tknowwhythisisrequired
#awaitevent.delete()

#https://docs.python.org/3/library/textwrap.html#textwrap.wrap
sticktext=textwrap.wrap(sticktext,width=10)
#convertsbackthelisttoastring
sticktext="\n".join(sticktext)

image=Image.new("RGBA",(512,512),(255,255,255,0))
draw=ImageDraw.Draw(image)
fontsize=230

FONT_FILE=awaitget_font_file(ubot,"@IndianBot_Fonts")

font=ImageFont.truetype(FONT_FILE,size=fontsize)

whiledraw.multiline_textsize(sticktext,font=font)>(512,512):
fontsize-=3
font=ImageFont.truetype(FONT_FILE,size=fontsize)

width,height=draw.multiline_textsize(sticktext,font=font)
draw.multiline_text(
((512-width)/2,(512-height)/2),sticktext,font=font,fill=(R,G,B)
)

image_stream=io.BytesIO()
image_stream.name="@Julia.webp"
image.save(image_stream,"WebP")
image_stream.seek(0)

#finally,replythesticker
awaitevent.reply(file=image_stream,reply_to=event.message.reply_to_msg_id)
#replacingupperlinewiththistogetreplytags

#cleanup
try:
os.remove(FONT_FILE)
exceptBaseException:
pass


asyncdefget_font_file(client,channel_id):
#firstgetthefontmessages
font_file_message_s=awaitclient.get_messages(
entity=channel_id,
filter=InputMessagesFilterDocument,
#thismightcauseFLOODWAIT,
#ifusedtoomanytimes
limit=None,
)
#getarandomfontfromthelistoffonts
#https://docs.python.org/3/library/random.html#random.choice
font_file_message=random.choice(font_file_message_s)
#downloadandreturnthefilepath
returnawaitclient.download_media(font_file_message)


@register(pattern=r"^/(\w+)say(.*)")
asyncdefunivsaye(cowmsg):

"""For.cowsaymodule,uniborgwrapperforcowwhichsaysthings."""
ifnotcowmsg.text[0].isalpha()andcowmsg.text[0]notin("#","@"):
arg=cowmsg.pattern_match.group(1).lower()
text=cowmsg.pattern_match.group(2)

ifarg=="cow":
arg="default"
ifargnotincow.COWACTERS:
return
cheese=cow.get_cow(arg)
cheese=cheese()

awaitcowmsg.reply(f"`{cheese.milk(text).replace('`','´')}`")


@register(pattern="^/basketball$")
asyncdef_(event):
ifevent.fwd_from:
return

input_str=print(randrange(6))
r=awaitevent.reply(file=InputMediaDice("🏀"))
ifinput_str:
try:
required_number=int(input_str)
whilenotr.media.value==required_number:
awaitr.delete()
r=awaitevent.reply(file=InputMediaDice("🏀"))
exceptBaseException:
pass


@register(pattern="^/jackpot$")
asyncdef_(event):
ifevent.fwd_from:
return

awaitevent.reply(file=InputMediaDice("🎰"))


@register(pattern="^/dart$")
asyncdef_(event):
ifevent.fwd_from:
return

input_str=print(randrange(7))
r=awaitevent.reply(file=InputMediaDice("🎯"))
ifinput_str:
try:
required_number=int(input_str)
whilenotr.media.value==required_number:
awaitr.delete()
r=awaitevent.reply(file=InputMediaDice("🎯"))
exceptBaseException:
pass


#OringinalSourcefromNicegrill:https://github.com/erenmetesar/NiceGrill/
#PortedtoLyndaby:@pokurt

COLORS=[
"#F07975",
"#F49F69",
"#F9C84A",
"#8CC56E",
"#6CC7DC",
"#80C1FA",
"#BCB3F9",
"#E181AC",
]


asyncdefprocess(msg,user,client,reply,replied=None):
ifnotos.path.isdir("resources"):
os.mkdir("resources",0o755)
urllib.request.urlretrieve(
"https://github.com/erenmetesar/modules-repo/raw/master/Roboto-Regular.ttf",
"resources/Roboto-Regular.ttf",
)
urllib.request.urlretrieve(
"https://github.com/erenmetesar/modules-repo/raw/master/Quivira.otf",
"resources/Quivira.otf",
)
urllib.request.urlretrieve(
"https://github.com/erenmetesar/modules-repo/raw/master/Roboto-Medium.ttf",
"resources/Roboto-Medium.ttf",
)
urllib.request.urlretrieve(
"https://github.com/erenmetesar/modules-repo/raw/master/DroidSansMono.ttf",
"resources/DroidSansMono.ttf",
)
urllib.request.urlretrieve(
"https://github.com/erenmetesar/modules-repo/raw/master/Roboto-Italic.ttf",
"resources/Roboto-Italic.ttf",
)

#Importıngfontsandgettingsthesizeoftext
font=ImageFont.truetype("resources/Roboto-Medium.ttf",43,encoding="utf-16")
font2=ImageFont.truetype("resources/Roboto-Regular.ttf",33,encoding="utf-16")
mono=ImageFont.truetype("resources/DroidSansMono.ttf",30,encoding="utf-16")
italic=ImageFont.truetype("resources/Roboto-Italic.ttf",33,encoding="utf-16")
fallback=ImageFont.truetype("resources/Quivira.otf",43,encoding="utf-16")

#Splittingtext
maxlength=0
width=0
text=[]
forlineinmsg.split("\n"):
length=len(line)
iflength>43:
text+=textwrap.wrap(line,43)
maxlength=43
ifwidth<fallback.getsize(line[:43])[0]:
if"MessageEntityCode"instr(reply.entities):
width=mono.getsize(line[:43])[0]+30
else:
width=fallback.getsize(line[:43])[0]
next
else:
text.append(line+"\n")
ifwidth<fallback.getsize(line)[0]:
if"MessageEntityCode"instr(reply.entities):
width=mono.getsize(line)[0]+30
else:
width=fallback.getsize(line)[0]
ifmaxlength<length:
maxlength=length

title=""
try:
details=awaitclient(
functions.channels.GetParticipantRequest(reply.chat_id,user.id)
)
ifisinstance(details.participant,types.ChannelParticipantCreator):
title=details.participant.rankifdetails.participant.rankelse"Creator"
elifisinstance(details.participant,types.ChannelParticipantAdmin):
title=details.participant.rankifdetails.participant.rankelse"Admin"
exceptTypeError:
pass
titlewidth=font2.getsize(title)[0]

#Getusername
lname=""ifnotuser.last_nameelseuser.last_name
tot=user.first_name+""+lname

namewidth=fallback.getsize(tot)[0]+10

ifnamewidth>width:
width=namewidth
width+=titlewidth+30iftitlewidth>width-namewidthelse-(titlewidth-30)
height=len(text)*40

#ProfilePhotoBG
pfpbg=Image.new("RGBA",(125,600),(0,0,0,0))

#DrawTemplate
top,middle,bottom=awaitdrawer(width,height)
#ProfilePhotoCheckandFetch
yes=False
color=random.choice(COLORS)
asyncforphotoinclient.iter_profile_photos(user,limit=1):
yes=True
ifyes:
pfp=awaitclient.download_profile_photo(user)
paste=Image.open(pfp)
os.remove(pfp)
paste.thumbnail((105,105))

#Mask
mask_im=Image.new("L",paste.size,0)
draw=ImageDraw.Draw(mask_im)
draw.ellipse((0,0,105,105),fill=255)

#ApplyMask
pfpbg.paste(paste,(0,0),mask_im)
else:
paste,color=awaitno_photo(user,tot)
pfpbg.paste(paste,(0,0))

#Creatingabigcanvastogatheralltheelements
canvassize=(
middle.width+pfpbg.width,
top.height+middle.height+bottom.height,
)
canvas=Image.new("RGBA",canvassize)
draw=ImageDraw.Draw(canvas)

y=80
ifreplied:
#Creatingabigcanvastogatheralltheelements
replname=""ifnotreplied.sender.last_nameelsereplied.sender.last_name
reptot=replied.sender.first_name+""+replname
font2.getsize(reptot)[0]
ifreply.sticker:
sticker=awaitreply.download_media()
stimg=Image.open(sticker)
canvas=canvas.resize((stimg.width+pfpbg.width,stimg.height+160))
top=Image.new("RGBA",(200+stimg.width,300),(29,29,29,255))
draw=ImageDraw.Draw(top)
awaitreplied_user(draw,reptot,replied.message.replace("\n",""),20)
top=top.crop((135,70,top.width,300))
canvas.paste(pfpbg,(0,0))
canvas.paste(top,(pfpbg.width+10,0))
canvas.paste(stimg,(pfpbg.width+10,140))
os.remove(sticker)
returnTrue,canvas
canvas=canvas.resize((canvas.width+60,canvas.height+120))
top,middle,bottom=awaitdrawer(middle.width+60,height+105)
canvas.paste(pfpbg,(0,0))
canvas.paste(top,(pfpbg.width,0))
canvas.paste(middle,(pfpbg.width,top.height))
canvas.paste(bottom,(pfpbg.width,top.height+middle.height))
draw=ImageDraw.Draw(canvas)
ifreplied.sticker:
replied.text="Sticker"
elifreplied.photo:
replied.text="Photo"
elifreplied.audio:
replied.text="Audio"
elifreplied.voice:
replied.text="VoiceMessage"
elifreplied.document:
replied.text="Document"
awaitreplied_user(
draw,
reptot,
replied.message.replace("\n",""),
maxlength+len(title),
len(title),
)
y=200
elifreply.sticker:
sticker=awaitreply.download_media()
stimg=Image.open(sticker)
canvas=canvas.resize((stimg.width+pfpbg.width+30,stimg.height+10))
canvas.paste(pfpbg,(0,0))
canvas.paste(stimg,(pfpbg.width+10,10))
os.remove(sticker)
returnTrue,canvas
elifreply.documentandnotreply.audioandnotreply.audio:
docname=".".join(reply.document.attributes[-1].file_name.split(".")[:-1])
doctype=reply.document.attributes[-1].file_name.split(".")[-1].upper()
ifreply.document.size<1024:
docsize=str(reply.document.size)+"Bytes"
elifreply.document.size<1048576:
docsize=str(round(reply.document.size/1024,2))+"KB"
elifreply.document.size<1073741824:
docsize=str(round(reply.document.size/1024**2,2))+"MB"
else:
docsize=str(round(reply.document.size/1024**3,2))+"GB"
docbglen=(
font.getsize(docsize)[0]
iffont.getsize(docsize)[0]>font.getsize(docname)[0]
elsefont.getsize(docname)[0]
)
canvas=canvas.resize((pfpbg.width+width+docbglen,160+height))
top,middle,bottom=awaitdrawer(width+docbglen,height+30)
canvas.paste(pfpbg,(0,0))
canvas.paste(top,(pfpbg.width,0))
canvas.paste(middle,(pfpbg.width,top.height))
canvas.paste(bottom,(pfpbg.width,top.height+middle.height))
canvas=awaitdoctype(docname,docsize,doctype,canvas)
y=80iftextelse0
else:
canvas.paste(pfpbg,(0,0))
canvas.paste(top,(pfpbg.width,0))
canvas.paste(middle,(pfpbg.width,top.height))
canvas.paste(bottom,(pfpbg.width,top.height+middle.height))
y=85

#WritingUser'sName
space=pfpbg.width+30
namefallback=ImageFont.truetype("resources/Quivira.otf",43,encoding="utf-16")
forletterintot:
ifletterinemoji.UNICODE_EMOJI:
newemoji,mask=awaitemoji_fetch(letter)
canvas.paste(newemoji,(space,24),mask)
space+=40
else:
ifnotawaitfontTest(letter):
draw.text((space,20),letter,font=namefallback,fill=color)
space+=namefallback.getsize(letter)[0]
else:
draw.text((space,20),letter,font=font,fill=color)
space+=font.getsize(letter)[0]

iftitle:
draw.text(
(canvas.width-titlewidth-20,25),title,font=font2,fill="#898989"
)

#Writingallseparatingemojisandregulartexts
x=pfpbg.width+30
bold,mono,italic,link=awaitget_entity(reply)
index=0
emojicount=0
textfallback=ImageFont.truetype("resources/Quivira.otf",33,encoding="utf-16")
textcolor="white"
forlineintext:
forletterinline:
index=(
msg.find(letter)ifemojicount==0elsemsg.find(letter)+emojicount
)
foroffset,lengthinbold.items():
ifindexinrange(offset,length):
font2=ImageFont.truetype(
"resources/Roboto-Medium.ttf",33,encoding="utf-16"
)
textcolor="white"
foroffset,lengthinitalic.items():
ifindexinrange(offset,length):
font2=ImageFont.truetype(
"resources/Roboto-Italic.ttf",33,encoding="utf-16"
)
textcolor="white"
foroffset,lengthinmono.items():
ifindexinrange(offset,length):
font2=ImageFont.truetype(
"resources/DroidSansMono.ttf",30,encoding="utf-16"
)
textcolor="white"
foroffset,lengthinlink.items():
ifindexinrange(offset,length):
font2=ImageFont.truetype(
"resources/Roboto-Regular.ttf",30,encoding="utf-16"
)
textcolor="#898989"
ifletterinemoji.UNICODE_EMOJI:
newemoji,mask=awaitemoji_fetch(letter)
canvas.paste(newemoji,(x,y-2),mask)
x+=45
emojicount+=1
else:
ifnotawaitfontTest(letter):
draw.text((x,y),letter,font=textfallback,fill=textcolor)
x+=textfallback.getsize(letter)[0]
else:
draw.text((x,y),letter,font=font2,fill=textcolor)
x+=font2.getsize(letter)[0]
msg=msg.replace(letter,"¶",1)
y+=40
x=pfpbg.width+30
returnTrue,canvas


asyncdefdrawer(width,height):
#Toppart
top=Image.new("RGBA",(width,20),(0,0,0,0))
draw=ImageDraw.Draw(top)
draw.line((10,0,top.width-20,0),fill=(29,29,29,255),width=50)
draw.pieslice((0,0,30,50),180,270,fill=(29,29,29,255))
draw.pieslice((top.width-75,0,top.width,50),270,360,fill=(29,29,29,255))

#Middlepart
middle=Image.new("RGBA",(top.width,height+75),(29,29,29,255))

#Bottompart
bottom=ImageOps.flip(top)

returntop,middle,bottom


asyncdeffontTest(letter):
test=TTFont("resources/Roboto-Medium.ttf")
fortableintest["cmap"].tables:
iford(letter)intable.cmap.keys():
returnTrue


asyncdefget_entity(msg):
bold={0:0}
italic={0:0}
mono={0:0}
link={0:0}
ifnotmsg.entities:
returnbold,mono,italic,link
forentityinmsg.entities:
ifisinstance(entity,types.MessageEntityBold):
bold[entity.offset]=entity.offset+entity.length
elifisinstance(entity,types.MessageEntityItalic):
italic[entity.offset]=entity.offset+entity.length
elifisinstance(entity,types.MessageEntityCode):
mono[entity.offset]=entity.offset+entity.length
elifisinstance(entity,types.MessageEntityUrl):
link[entity.offset]=entity.offset+entity.length
elifisinstance(entity,types.MessageEntityTextUrl):
link[entity.offset]=entity.offset+entity.length
elifisinstance(entity,types.MessageEntityMention):
link[entity.offset]=entity.offset+entity.length
returnbold,mono,italic,link


asyncdefdoctype(name,size,type,canvas):
font=ImageFont.truetype("resources/Roboto-Medium.ttf",38)
doc=Image.new("RGBA",(130,130),(29,29,29,255))
draw=ImageDraw.Draw(doc)
draw.ellipse((0,0,130,130),fill="#434343")
draw.line((66,28,66,53),width=14,fill="white")
draw.polygon([(67,77),(90,53),(42,53)],fill="white")
draw.line((40,87,90,87),width=8,fill="white")
canvas.paste(doc,(160,23))
draw2=ImageDraw.Draw(canvas)
draw2.text((320,40),name,font=font,fill="white")
draw2.text((320,97),size+type,font=font,fill="#AAAAAA")
returncanvas


asyncdefno_photo(reply,tot):
pfp=Image.new("RGBA",(105,105),(0,0,0,0))
pen=ImageDraw.Draw(pfp)
color=random.choice(COLORS)
pen.ellipse((0,0,105,105),fill=color)
letter=""ifnottotelsetot[0]
font=ImageFont.truetype("resources/Roboto-Regular.ttf",60)
pen.text((32,17),letter,font=font,fill="white")
returnpfp,color


asyncdefemoji_fetch(emoji):
emojis=json.loads(
urllib.request.urlopen(
"https://github.com/erenmetesar/modules-repo/raw/master/emojis.txt"
)
.read()
.decode()
)
ifemojiinemojis:
img=emojis[emoji]
returnawaittransparent(
urllib.request.urlretrieve(img,"resources/emoji.png")[0]
)
img=emojis["⛔"]
returnawaittransparent(urllib.request.urlretrieve(img,"resources/emoji.png")[0])


asyncdeftransparent(emoji):
emoji=Image.open(emoji).convert("RGBA")
emoji.thumbnail((40,40))

#Mask
mask=Image.new("L",(40,40),0)
draw=ImageDraw.Draw(mask)
draw.ellipse((0,0,40,40),fill=255)
returnemoji,mask


asyncdefreplied_user(draw,tot,text,maxlength,title):
namefont=ImageFont.truetype("resources/Roboto-Medium.ttf",38)
namefallback=ImageFont.truetype("resources/Quivira.otf",38)
textfont=ImageFont.truetype("resources/Roboto-Regular.ttf",32)
textfallback=ImageFont.truetype("resources/Roboto-Medium.ttf",38)
maxlength=maxlength+7ifmaxlength<10elsemaxlength
text=text[:maxlength-2]+".."iflen(text)>maxlengthelsetext
draw.line((165,90,165,170),width=5,fill="white")
space=0
forletterintot:
ifnotawaitfontTest(letter):
draw.text((180+space,86),letter,font=namefallback,fill="#888888")
space+=namefallback.getsize(letter)[0]
else:
draw.text((180+space,86),letter,font=namefont,fill="#888888")
space+=namefont.getsize(letter)[0]
space=0
forletterintext:
ifnotawaitfontTest(letter):
draw.text((180+space,132),letter,font=textfallback,fill="#888888")
space+=textfallback.getsize(letter)[0]
else:
draw.text((180+space,132),letter,font=textfont,fill="white")
space+=textfont.getsize(letter)[0]


@register(pattern="^/quotly$")
asyncdef_(event):
ifevent.fwd_from:
return

reply=awaitevent.get_reply_message()
msg=reply.message
repliedreply=awaitreply.get_reply_message()
user=(
awaitevent.client.get_entity(reply.forward.sender)
ifreply.fwd_from
elsereply.sender
)
res,canvas=awaitprocess(msg,user,event.client,reply,repliedreply)
ifnotres:
return
canvas.save("sticker.webp")
awaitevent.client.send_file(
event.chat_id,"sticker.webp",reply_to=event.reply_to_msg_id
)
os.remove("sticker.webp")


EMOJI_PATTERN=re.compile(
"["
"\U0001F1E0-\U0001F1FF"#flags(iOS)
"\U0001F300-\U0001F5FF"#symbols&pictographs
"\U0001F600-\U0001F64F"#emoticons
"\U0001F680-\U0001F6FF"#transport&mapsymbols
"\U0001F700-\U0001F77F"#alchemicalsymbols
"\U0001F780-\U0001F7FF"#GeometricShapesExtended
"\U0001F800-\U0001F8FF"#SupplementalArrows-C
"\U0001F900-\U0001F9FF"#SupplementalSymbolsandPictographs
"\U0001FA00-\U0001FA6F"#ChessSymbols
"\U0001FA70-\U0001FAFF"#SymbolsandPictographsExtended-A
"\U00002702-\U000027B0"#Dingbats
"]+"
)


defdeEmojify(inputString:str)->str:
"""Removeemojisandothernon-safecharactersfromstring"""
returnre.sub(EMOJI_PATTERN,"",inputString)


#MadeBy@MissJulia_Robot


@register(pattern="^/animate(.*)")
asyncdefstickerizer(event):

newtext=event.pattern_match.group(1)
animus=[20,32,33,40,41,42,58]
sticcers=awaitubot.inline_query(
"stickerizerbot",f"#{random.choice(animus)}{(deEmojify(newtext))}"
)
null=awaitsticcers[0].download_media(TEMP_DOWNLOAD_DIRECTORY)
bara=str(null)
awaitevent.client.send_file(event.chat_id,bara,reply_to=event.id)
os.remove(bara)


@register(pattern="^/dice$")
asyncdef_(event):
ifevent.fwd_from:
return

input_str=print(randrange(7))
r=awaitevent.reply(file=InputMediaDice(""))
ifinput_str:
try:
required_number=int(input_str)
whilenotr.media.value==required_number:
awaitr.delete()
r=awaitevent.reply(file=InputMediaDice(""))
exceptBaseException:
pass


@register(pattern="^/fortune$")
asyncdeffortunate(event):
ifevent.fwd_from:
return

jit=subprocess.check_output(["python","fortune.py"])
pit=jit.decode()
awaitevent.reply(pit)


ABUSE_STRINGS=(
"Fuckoff",
"Stfugofuckyourself",
"Urmumgey",
"Urdadlesbo",
"YouAssfucker",
"Nigga",
"Urgrannytranny",
"younoob",
"RelaxyourRear,dersnothingtofear,TheRapetrainisfinallyhere",
"Stfubc",
"StfuandGtfoUnub",
"GTFObsdk",
"CUnt",
"Madharchod",
"Gayishere",
"Urdadgeybc",
)

EYES=[
["⌐■","■"],
["͠°","°"],
["⇀","↼"],
["´•","•`"],
["´","`"],
["`","´"],
["ó","ò"],
["ò","ó"],
["⸌","⸍"],
[">","<"],
["Ƹ̵̡","Ʒ"],
["ᗒ","ᗕ"],
["⟃","⟄"],
["⪧","⪦"],
["⪦","⪧"],
["⪩","⪨"],
["⪨","⪩"],
["⪰","⪯"],
["⫑","⫒"],
["⨴","⨵"],
["⩿","⪀"],
["⩾","⩽"],
["⩺","⩹"],
["⩹","⩺"],
["◥▶","◀◤"],
["◍","◎"],
["/͠-","┐͡-\\"],
["⌣","⌣”"],
["͡⎚","͡⎚"],
["≋"],
["૦ઁ"],
["ͯ"],
["͌"],
["ළ"],
["◉"],
["☉"],
["・"],
["▰"],
["ᵔ"],
["ﾟ"],
["□"],
["☼"],
["*"],
["`"],
["⚆"],
["⊜"],
[">"],
["❍"],
["￣"],
["─"],
["✿"],
["•"],
["T"],
["^"],
["ⱺ"],
["@"],
["ȍ"],
[""],
[""],
["x"],
["-"],
["$"],
["Ȍ"],
["ʘ"],
["Ꝋ"],
[""],
["⸟"],
["๏"],
["ⴲ"],
["◕"],
["◔"],
["✧"],
["■"],
["♥"],
["͡°"],
["¬"],
["º"],
["⨶"],
["⨱"],
["⏓"],
["⏒"],
["⍜"],
["⍤"],
["ᚖ"],
["ᴗ"],
["ಠ"],
["σ"],
["☯"],
]

MOUTHS=[
["v"],
["ᴥ"],
["ᗝ"],
["Ѡ"],
["ᗜ"],
["Ꮂ"],
["ᨓ"],
["ᨎ"],
["ヮ"],
["╭͜ʖ╮"],
["͟ل͜"],
["͜ʖ"],
["͟ʖ"],
["ʖ̯"],
["ω"],
["³"],
["ε"],
["﹏"],
["□"],
["ل͜"],
["‿"],
["╭╮"],
["‿‿"],
["▾"],
["‸"],
["Д"],
["∀"],
["!"],
["人"],
["."],
["ロ"],
["_"],
["෴"],
["ѽ"],
["ഌ"],
["⏠"],
["⏏"],
["⍊"],
["⍘"],
["ツ"],
["益"],
["╭∩╮"],
["Ĺ̯"],
["◡"],
["͜つ"],
]

EARS=[
["q","p"],
["ʢ","ʡ"],
["⸮","?"],
["ʕ","ʔ"],
["ᖗ","ᖘ"],
["ᕦ","ᕥ"],
["ᕦ(",")ᕥ"],
["ᕙ(",")ᕗ"],
["ᘳ","ᘰ"],
["ᕮ","ᕭ"],
["ᕳ","ᕲ"],
["(",")"],
["[","]"],
["¯\\_","_/¯"],
["୧","୨"],
["୨","୧"],
["⤜(",")⤏"],
["☞","☞"],
["ᑫ","ᑷ"],
["ᑴ","ᑷ"],
["ヽ(",")ﾉ"],
["\\(",")/"],
["乁(",")ㄏ"],
["└[","]┘"],
["(づ",")づ"],
["(ง",")ง"],
["⎝","⎠"],
["ლ(","ლ)"],
["ᕕ(",")ᕗ"],
["(∩",")⊃━☆ﾟ.*"],
]

TOSS=(
"Heads",
"Tails",
)


@register(pattern="^/roll$")
asyncdefmsg(event):

awaitevent.reply(str(random.choice(range(1,7))))


@register(pattern="^/toss$")
asyncdefmsg(event):
awaitevent.reply(random.choice(TOSS))


@register(pattern="^/abuse$")
asyncdefmsg(event):

ifevent.reply_to_msg_id:
reply=awaitevent.get_reply_message()
replyto=reply.sender_id
else:
replyto=event.sender_id
awaittbot.send_message(
event.chat_id,random.choice(ABUSE_STRINGS),reply_to=replyto
)


@register(pattern="^/bluetext$")
asyncdefmsg(event):

ifevent.reply_to_msg_id:
reply=awaitevent.get_reply_message()
replyto=reply.sender_id
else:
replyto=event.sender_id
awaittbot.send_message(
event.chat_id,
"/BLUE/TET/MUST/CLICK/I/AM/A/STUPID/ANIMAL/THAT/IS/ATTRACTED/TO/COLORS",
reply_to=replyto,
)


@register(pattern="^/rlg$")
asyncdef_(event):

eyes=random.choice(EYES)
mouth=random.choice(MOUTHS)
ears=random.choice(EARS)
repl=format(ears+eyes+mouth+eyes+ears)
awaitevent.reply(repl)


@register(pattern="^/decide$")
asyncdef_(event):

r=randint(1,100)
ifr<=65:
awaitevent.reply("Yes.")
elifr<=90:
awaitevent.reply("NoU.")
else:
awaitevent.reply("Maybe.")


@register(pattern="^/table$")
asyncdef_(event):

r=randint(1,100)
ifr<=45:
awaitevent.reply("(╯°□°）╯彡┻━┻")
elifr<=90:
awaitevent.reply("Sendmoneytobuynewtabletoflip")
else:
awaitevent.reply("Godosomeworkinsteadofflippingtablesmaboy.")


SFW_STRINGS=(
"Owww...Suchastupididiot.",
"Don'tdrinkandtype.",
"Ithinkyoushouldgohomeorbetteramentalasylum.",
"Commandnotfound.Justlikeyourbrain.",
"Doyourealizeyouaremakingafoolofyourself?Apparentlynot.",
"Youcantypebetterthanthat.",
"Botrule544section9preventsmefromreplyingtostupidhumanslikeyou.",
"Sorry,wedonotsellbrains.",
"Believemeyouarenotnormal.",
"Ibetyourbrainfeelsasgoodasnew,seeingthatyouneveruseit.",
"IfIwantedtokillmyselfI'dclimbyouregoandjumptoyourIQ.",
"Zombieseatbrains...you'resafe.",
"Youdidn'tevolvefromapes,theyevolvedfromyou.",
"ComebackandtalktomewhenyourI.Q.exceedsyourage.",
"I'mnotsayingyou'restupid,I'mjustsayingyou'vegotbadluckwhenitcomestothinking.",
"Whatlanguageareyouspeaking?Causeitsoundslikebullshit.",
"Stupidityisnotacrimesoyouarefreetogo.",
"YouareproofthatevolutionCANgoinreverse.",
"IwouldaskyouhowoldyouarebutIknowyoucan'tcountthathigh.",
"Asanoutsider,whatdoyouthinkofthehumanrace?",
"Brainsaren'teverything.Inyourcasethey'renothing.",
"Ordinarilypeopleliveandlearn.Youjustlive.",
"Idon'tknowwhatmakesyousostupid,butitreallyworks.",
"Keeptalking,somedayyou'llsaysomethingintelligent!(Idoubtitthough)",
"Shockme,saysomethingintelligent.",
"YourIQ'slowerthanyourshoesize.",
"Alas!Yourneurotransmittersarenomoreworking.",
"Areyoucrazyyoufool.",
"Everyonehastherighttobestupidbutyouareabusingtheprivilege.",
"I'msorryIhurtyourfeelingswhenIcalledyoustupid.Ithoughtyoualreadyknewthat.",
"Youshouldtrytastingcyanide.",
"Yourenzymesaremeanttodigestratpoison.",
"Youshouldtrysleepingforever.",
"Pickupagunandshootyourself.",
"Youcouldmakeaworldrecordbyjumpingfromaplanewithoutparachute.",
"StoptalkingBSandjumpinfrontofarunningbullettrain.",
"TrybathingwithHydrochloricAcidinsteadofwater.",
"Trythis:ifyouholdyourbreathunderwaterforanhour,youcanthenholditforever.",
"GoGreen!StopinhalingOxygen.",
"Godwassearchingforyou.Youshouldleavetomeethim.",
"giveyour100%.Now,godonateblood.",
"Tryjumpingfromahundredstorybuildingbutyoucandoitonlyonce.",
"Youshoulddonateyourbrainseeingthatyouneverusedit.",
"Volunteerfortargetinanfiringrange.",
"Headshotsarefun.Getyourselfone.",
"Youshouldtryswimmingwithgreatwhitesharks.",
"Youshouldpaintyourselfredandruninabullmarathon.",
"Youcanstayunderwaterfortherestofyourlifewithoutcomingbackup.",
"Howaboutyoustopbreathingforlike1day?That'llbegreat.",
"Tryprovokingatigerwhileyoubothareinacage.",
"Haveyoutriedshootingyourselfashighas100musingacanon.",
"YoushouldtryholdingTNTinyourmouthandignitingit.",
"TryplayingcatchandthrowwithRDitsfun.",
"Iheardphogineispoisonousbutiguessyouwontmindinhalingitforfun.",
"LaunchyourselfintoouterspacewhileforgettingoxygenonEarth.",
"Youshouldtryplayingsnakeandladders,withrealsnakesandnoladders.",
"DancenakedonacoupleofHTwires.",
"ActiveVolcanoisthebestswimmingpoolforyou.",
"Youshouldtryhotbathinavolcano.",
"Trytospendonedayinacoffinanditwillbeyoursforever.",
"HitUraniumwithaslowmovingneutroninyourpresence.Itwillbeaworthwhileexperience.",
"Youcanbethefirstpersontosteponsun.Haveatry.",
"Peoplelikeyouarethereasonwehavemiddlefingers.",
"Whenyourmomdroppedyouoffattheschool,shegotaticketforlittering.",
"You’resouglythatwhenyoucry,thetearsrolldownthebackofyourhead…justtoavoidyourface.",
"Ifyou’retalkingbehindmybackthenyou’reinaperfectpositiontokissmya**!.",
"Stupidityisnotacrimesoyouarefreetogo.",
)


@register(pattern="^/insult$")
asyncdef_(event):

ifevent.reply_to_msg_id:
reply=awaitevent.get_reply_message()
replyto=reply.sender_id
else:
replyto=event.sender_id
awaittbot.send_message(event.chat_id,random.choice(SFW_STRINGS),reply_to=replyto)


reactionhappy=[
"''̵͇З=(▀͜͞ʖ▀)=Ε/̵͇/’’",
"ʕ•ᴥ•ʔ",
"(づ｡◕‿‿◕｡)づ",
"(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧✧ﾟ･:*ヽ(◕ヮ◕ヽ)",
"(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
"(☞ﾟ∀ﾟ)☞",
"|(•◡•)|(❍ᴥ❍Ʋ)",
"(◕‿◕✿)",
"(ᵔᴥᵔ)",
"(☞ﾟヮﾟ)☞☜(ﾟヮﾟ☜)",
"(づ￣³￣)づ",
"♪~ᕕ(ᐛ)ᕗ",
"♥️‿♥️",
"༼つ͡°͜ʖ͡°༽つ",
"༼つಥ_ಥ༽つ",
"ヾ(⌐■_■)ノ♪",
"~(˘▾˘~)",
"◉_◉",
"(•◡•)/",
"(~˘▾˘)~",
"(｡◕‿‿◕｡)",
"☜(˚▽˚)☞",
"(•Ω•)",
"(｡◕‿◕｡)",
"(っ˘ڡ˘Σ)",
"｡◕‿‿◕｡",
"☜(⌒▽⌒)☞",
"｡◕‿◕｡",
"(ღ˘⌣˘ღ)",
"(▰˘◡˘▰)",
"^̮^",
"^̮^",
">_>",
"(^̮^)",
"^̮^",
"^̮^",
]
reactionangry=[
"▄︻̷┻═━一",
"(▀Ĺ̯▀)",
"(ง͠°͟ل͜͡°)ง",
"༼つ◕_◕༽つ",
"ಠ_ಠ",
"''̵͇З=(͠°͟ʖ͡°)=Ε/̵͇/'",
"(ง'̀-'́)ง",
"(ノಠ益ಠ)ノ彡┻━┻",
"(╯°□°)╯︵ꞰOOQƎƆⱯɟ",
"ლ(ಠ益ಠლ)",
"ಠ╭╮ಠ",
"''̵͇З=(•_•)=Ε/̵͇/''",
"(╯°□°）╯︵┻━┻",
"┻━┻︵ヽ(Д´)ﾉ︵┻━┻",
"⌐╦╦═─",
"（╯°□°）╯︵(.O.)",
":')",
"┬──┬ノ(゜-゜ノ)",
"ლ(´ڡლ)",
"(°ロ°)☝️",
"ლ,ᔑ•ﺪ͟͠•ᔐ.ლ",
"┬─┬ノ(º_ºノ)",
"┬─┬﻿︵/(.□.）",
]

reactions=[
"(͡°͜ʖ͡°)",
"(.•́_ʖ•̀.)",
"(ಠ͜ʖಠ)",
"(͜͡ʖ͡)",
"(ʘ͜ʖʘ)",
"ヾ(´〇`)ﾉ♪♪♪",
"ヽ(o´∀`)ﾉ♪♬",
"♪♬((d⌒ω⌒b))♬♪",
"└(＾＾)┐",
"(￣▽￣)/♫•*¨*•.¸¸♪",
"ヾ(⌐■_■)ノ♪",
"乁(•ω•乁)",
"♬♫♪◖(●o●)◗♪♫♬",
"(っ˘ڡ˘ς)",
"(˘▽˘)っ♨",
"(　・ω・)⊃-[二二]",
"(*´ー`)旦旦(￣ω￣*)",
"(￣▽￣)[][](≧▽≦)",
"(*￣▽￣)旦且(´∀`*)",
"(ノ˘_˘)ノ　ζ|||ζ　ζ|||ζ　ζ|||ζ",
"(ノ°∀°)ノ⌒･*:.｡..｡.:*･゜ﾟ･*☆",
"(⊃｡•́‿•̀｡)⊃━✿✿✿✿✿✿",
"(∩`ﾛ´)⊃━炎炎炎炎炎",
"(・∀・)・・・--------☆",
"(-ω-)／占~~~~~",
"○∞∞∞∞ヽ(^ー^)",
"(*＾＾)/~~~~~~~~~~◎",
"(((￣□)_／",
"(ﾒ￣▽￣)︻┳═一",
"ヽ(･∀･)ﾉ_θ彡☆Σ(ノ`Д´)ノ",
"(*`0´)θ☆(メ°皿°)ﾉ",
"(;-_-)――――――C<―_-)",
"ヽ(>_<ヽ)―⊂|=0ヘ(^‿^)",
"(҂`ﾛ´)︻デ═一＼(º□ºl|l)/",
"/(.□.)＼︵╰(°益°)╯︵/(.□./)",
"(`⌒*)O-(`⌒´Q)",
"(っ•﹏•)っ✴==≡눈٩(`皿´҂)ง",
"ヾ(・ω・)メ(・ω・)ノ",
"(*^ω^)八(⌒▽⌒)八(-‿‿-)ヽ",
"ヽ(⌒ω⌒)人(=^‥^=)ﾉ",
"｡*:☆(・ω・人・ω・)｡:゜☆｡",
"(°(°ω(°ω°(☆ω☆)°ω°)ω°)°)",
"(っ˘▽˘)(˘▽˘)˘▽˘ς)",
"(*＾ω＾)人(＾ω＾*)",
r"＼(▽￣\(￣▽￣)/￣▽)／",
"(￣Θ￣)",
"＼(ˋΘ´)／",
"(´(00)ˋ)",
"＼(￣(oo)￣)／",
"／(≧x≦)＼",
"／(=･x･=)＼",
"(=^･ω･^=)",
"(=;ｪ;=)",
"(=⌒‿‿⌒=)",
"(＾•ω•＾)",
"ଲ(ⓛωⓛ)ଲ",
"ଲ(ⓛωⓛ)ଲ",
"(^◔ᴥ◔^)",
"[(－－)]..zzZ",
"(￣o￣)zzZZzzZZ",
"(＿＿*)Zzz",
"☆ﾐ(o*･ω･)ﾉ",
"ε=ε=ε=ε=┌(;￣▽￣)┘",
"ε===(っ≧ω≦)っ",
"__φ(．．)",
"ヾ(`ー´)シφ__",
"(^▽^)ψ__",
"|･ω･)",
"|д･)",
"┬┴┬┴┤･ω･)ﾉ",
"|･д･)ﾉ",
"(*￣ii￣)",
"(＾〃＾)",
"m(__)m",
"人(__*)",
"(シ..)シ",
"(^_~)",
"(>ω^)",
"(^_<)〜☆",
"(^_<)",
"(づ￣³￣)づ",
"(⊃｡•́‿•̀｡)⊃",
"⊂(´•ω•`⊂)",
"(*・ω・)ﾉ",
"(^-^*)/",
"ヾ(*'▽'*)",
"(^０^)ノ",
"(*°ｰ°)ﾉ",
"(￣ω￣)/",
"(≧▽≦)/",
"w(°ｏ°)w",
"(⊙_⊙)",
"(°ロ°)!",
"∑(O_O;)",
"(￢_￢)",
"(¬_¬)",
"(↼_↼)",
"(￣ω￣;)",
"┐('～`;)┌",
"(・_・;)",
"(＠_＠)",
"(•ิ_•ิ)?",
"ヽ(ー_ー)ノ",
"┐(￣ヘ￣)┌",
"┐(￣～￣)┌",
"┐(´д`)┌",
"╮(︶▽︶)╭",
"ᕕ(ᐛ)ᕗ",
"(ノωヽ)",
"(″ロ゛)",
"(/ω＼)",
"(((＞＜)))",
"~(>_<~)",
"(×_×)",
"(×﹏×)",
"(ノ_<。)",
"(μ_μ)",
"o(TヘTo)",
"(ﾟ，_ゝ｀)",
"(╥ω╥)",
"(／ˍ・、)",
"(つω`｡)",
"(T_T)",
"o(〒﹏〒)o",
"(＃`Д´)",
"(・`ω´・)",
"(`ε´)",
"(ﾒ`ﾛ´)",
"Σ(▼□▼メ)",
"(҂`з´)",
"٩(╬ʘ益ʘ╬)۶",
"↑_(ΦwΦ)Ψ",
"(ﾉಥ益ಥ)ﾉ",
"(＃＞＜)",
"(；￣Д￣)",
"(￢_￢;)",
"(＾＾＃)",
"(￣︿￣)",
"ヾ(￣O￣)ツ",
"(ᗒᗣᗕ)՞",
"(ノ_<。)ヾ(´▽`)",
"ヽ(￣ω￣(。。)ゝ",
"(ﾉ_；)ヾ(´∀`)",
"(´-ω-`(__)",
"(⌒_⌒;)",
"(*/_＼)",
"(◡‿◡*)",
"(//ω//)",
"(￣▽￣*)ゞ",
"(„ಡωಡ„)",
"(ﾉ´з`)ノ",
"(♡-_-♡)",
"(─‿‿─)♡",
"(´ω`♡)",
"(ღ˘⌣˘ღ)",
"(´•ω•`)♡",
"╰(*´︶`*)╯♡",
"(≧◡≦)♡",
"♡(˘▽˘>ԅ(˘⌣˘)",
"σ(≧ε≦σ)♡",
"(˘∀˘)/(μ‿μ)❤",
"Σ>―(〃°ω°〃)♡→",
"(*^ω^)",
"(o^▽^o)",
"ヽ(・∀・)ﾉ",
"(o･ω･o)",
"(^人^)",
"(´ω`)",
"(´•ω•`)",
"╰(▔∀▔)╯",
"(✯◡✯)",
"(⌒‿⌒)",
"(*°▽°*)",
"(´｡•ᵕ•｡`)",
"ヽ(>∀<☆)ノ",
"＼(￣▽￣)／",
"(o˘◡˘o)",
"(╯✧▽✧)╯",
"(‾́◡‾́)",
"(๑˘︶˘๑)",
"(´･ᴗ･`)",
"(͡°ʖ̯͡°)",
"(ఠ͟ʖఠ)",
"(ಥʖ̯ಥ)",
"(≖͜ʖ≖)",
"ヘ(￣ω￣ヘ)",
"(ﾉ≧∀≦)ﾉ",
"└(￣-￣└))",
"┌(＾＾)┘",
"(^_^♪)",
"(〜￣△￣)〜",
"(｢•ω•)｢",
"(˘ɜ˘)♬♪♫",
"(o˘◡˘o)┌iii┐",
"♨o(>_<)o♨",
"(・・)つ―{}@{}@{}-",
"(*´з`)口ﾟ｡ﾟ口(・∀・)",
"(*^^)o∀*∀o(^^*)",
"-●●●-ｃ(・・)",
"(ﾉ≧∀≦)ﾉ‥…━━━★",
"╰(͡°͜ʖ͡°)つ──☆*:・ﾟ",
"(∩ᄑ_ᄑ)⊃━☆ﾟ*･｡*･:≡(ε:)",
]


@register(pattern="^/react$")
asyncdef_(event):

ifevent.reply_to_msg_id:
reply=awaitevent.get_reply_message()
replyto=reply.sender_id
else:
replyto=event.sender_id
react=random.choice(reactions)
awaitevent.reply(react,reply_to=replyto)


@register(pattern="^/rhappy$")
asyncdef_(event):

ifevent.reply_to_msg_id:
reply=awaitevent.get_reply_message()
replyto=reply.sender_id
else:
replyto=event.sender_id
rhappy=random.choice(reactionhappy)
awaitevent.reply(rhappy,reply_to=replyto)


@register(pattern="^/rangry$")
asyncdef_(event):

ifevent.reply_to_msg_id:
reply=awaitevent.get_reply_message()
replyto=reply.sender_id
else:
replyto=event.sender_id
rangry=random.choice(reactionangry)
awaitevent.reply(rangry,reply_to=replyto)


file_help=os.path.basename(__file__)
file_help=file_help.replace(".py","")
file_helpo=file_help.replace("_","")

__help__="""
**Somememescommand,finditalloutyourself!**

-/owo:OWOdetext
-/stretch:STRETCHdetext
-/clapmoji:Typeinreplytoamessageandseemagic
-/bmoji:Typeinreplytoamessageandseemagic
-/copypasta:Typeinreplytoamessageandseemagic
-/vapor:owovapordis
-/shout<i>text</i>:Writeanythingthatuwantittoshould
-/zalgofy:replytoamessagetoglitchitout!
-/table:getflip/unflip:v.
-/decide:Randomlyanswersyes/no/maybe
-/bluetext:Musttypeforfun
-/toss:TossesAcoin
-/abuse:Abusesthecunt
-/insult:Insultthecunt
-/slap:Slapsthecunt
-/roll:Rolladice.
-/rlg:Joinears,nose,mouthandcreateanemo;-;
-/react:Checkonyourown
-/rhappy:Checkonyourown
-/rangry:Checkonyourown
-/angrymoji:Checkonyourown
-/crymoji:Checkonyourown
-/cowsay,/tuxsay,/milksay,/kisssay,/wwwsay,/defaultsay,/bunnysay,/moosesay,/sheepsay,/rensay,/cheesesay,/ghostbusterssay,/skeletonsay<i>text</i>:Returnsastylisharttextfromthegiventext
-/deepfry:Typethisinreplytoanimage/stickertoroasttheimage/sticker
-/figlet:AnotherStyleart
-/dice:RollAdice
-/dart:Throwadartandtryyourluck
-/basketball:Tryyourluckifyoucanentertheballinthering
-/type<i>text</i>:Makethebottypesomethingforyouinaprofessionalway
-/carbon<i>text</i>:Beautifiesyourtextandenwrapsinsideaterminalimage[ENGLISHONLY]
-/sticklet<i>text</i>:Turnatextintoasticker
-/fortune:getsarandomfortunequote
-/quotly:Type/quotlyinreplytoamessagetomakeastickerofthat
-/animate:Enwrapyourtextinabeautifulanime

"""

__mod_name__="Memes"
