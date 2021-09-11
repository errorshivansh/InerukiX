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

importjson
importos
importrandom
importtextwrap
importurllib

importemoji
fromfontTools.ttLibimportTTFont
fromPILimportImage,ImageDraw,ImageFont,ImageOps
fromtelethon.tlimportfunctions,types

fromIneruki.services.eventsimportregister

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
else:
img=emojis["⛔"]
returnawaittransparent(
urllib.request.urlretrieve(img,"resources/emoji.png")[0]
)


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


@register(pattern="^/q")
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
