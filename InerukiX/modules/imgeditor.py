#By@TroJanzHE
#Improvedbyerrorshivansh

frompyrogramimportfilters
frompyrogram.typesimport(
CallbackQuery,
InlineKeyboardButton,
InlineKeyboardMarkup,
Message,
)

#By@TroJanzHE
fromIneruki.Addons.ImageEditor.edit_1import(#pylint:disable=import-error
black_white,
box_blur,
bright,
g_blur,
mix,
normal_blur,
)
fromIneruki.Addons.ImageEditor.edit_2import(#pylint:disable=import-error
cartoon,
circle_with_bg,
circle_without_bg,
contrast,
edge_curved,
pencil,
sepia_mode,
sticker,
)
fromIneruki.Addons.ImageEditor.edit_3import(#pylint:disable=import-error
black_border,
blue_border,
green_border,
red_border,
)
fromIneruki.Addons.ImageEditor.edit_4import(#pylint:disable=import-error
inverted,
removebg_plain,
removebg_sticker,
removebg_white,
rotate_90,
rotate_180,
rotate_270,
round_sticker,
)
fromIneruki.Addons.ImageEditor.edit_5import(#pylint:disable=import-error
normalglitch_1,
normalglitch_2,
normalglitch_3,
normalglitch_4,
normalglitch_5,
scanlineglitch_1,
scanlineglitch_2,
scanlineglitch_3,
scanlineglitch_4,
scanlineglitch_5,
)
fromIneruki.services.pyrogramimportpbotasClient

lel=00000000
#pylint:disable=import-error
@Client.on_message(filters.command(["edit","editor"]))
asyncdefphoto(client:Client,message:Message):
try:
ifnotmessage.reply_to_message.photo:
awaitclient.send_message(message.chat.id,"Replytoanimageman!ㅤㅤ")
return
except:
return
globallel
try:
lel=message.from_user.id
except:
return
try:
awaitclient.send_message(
chat_id=message.chat.id,
text="Selectyourrequiredmodefrombelow!ㅤㅤ",
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(text="💡BRIGHT",callback_data="bright"),
InlineKeyboardButton(text="🖼MIED",callback_data="mix"),
InlineKeyboardButton(text="🔳B&W",callback_data="b|w"),
],
[
InlineKeyboardButton(text="🟡CIRCLE",callback_data="circle"),
InlineKeyboardButton(text="🩸BLUR",callback_data="blur"),
InlineKeyboardButton(text="🌌BORDER",callback_data="border"),
],
[
InlineKeyboardButton(text="🎉STICKER",callback_data="stick"),
InlineKeyboardButton(text="↩️ROTATE",callback_data="rotate"),
InlineKeyboardButton(
text="🔦CONTRAST",callback_data="contrast"
),
],
[
InlineKeyboardButton(text="🌇SEPIA",callback_data="sepia"),
InlineKeyboardButton(text="✏️PENCIL",callback_data="pencil"),
InlineKeyboardButton(text="🐶CARTOON",callback_data="cartoon"),
],
[
InlineKeyboardButton(text="🔄INVERT",callback_data="inverted"),
InlineKeyboardButton(text="🔮GLITCH",callback_data="glitch"),
InlineKeyboardButton(
text="✂️REMOVEBG",callback_data="removebg"
),
],
[
InlineKeyboardButton(text="❌CLOSE",callback_data="close_e"),
],
]
),
reply_to_message_id=message.reply_to_message.message_id,
)
exceptExceptionase:
print("photomarkuperror-"+str(e))
if"USER_IS_BLOCKED"instr(e):
return
else:
try:
awaitmessage.reply_text("Somethingwentwrong!",quote=True)
exceptException:
return


@Client.on_callback_query()
asyncdefcb_handler(client:Client,query:CallbackQuery):
user_id=query.from_user.id
iflel==user_id:
ifquery.data=="removebg":
awaitquery.message.edit_text(
"**Selectrequiredmode**ㅤㅤㅤㅤ",
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="WITHWHITEBG",callback_data="rmbgwhite"
),
InlineKeyboardButton(
text="WITHOUTBG",callback_data="rmbgplain"
),
],
[
InlineKeyboardButton(
text="STICKER",callback_data="rmbgsticker"
)
],
]
),
)
elifquery.data=="stick":
awaitquery.message.edit(
"**SelectaType**",
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(text="Normal",callback_data="stkr"),
InlineKeyboardButton(
text="EdgeCurved",callback_data="cur_ved"
),
],
[
InlineKeyboardButton(
text="Circle",callback_data="circle_sticker"
)
],
]
),
)
elifquery.data=="rotate":
awaitquery.message.edit_text(
"**SelecttheDegree**",
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(text="180",callback_data="180"),
InlineKeyboardButton(text="90",callback_data="90"),
],
[InlineKeyboardButton(text="270",callback_data="270")],
]
),
)

elifquery.data=="glitch":
awaitquery.message.edit_text(
"**Selectrequiredmode**ㅤㅤㅤㅤ",
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="NORMAL",callback_data="normalglitch"
),
InlineKeyboardButton(
text="SCANLINES",callback_data="scanlineglitch"
),
]
]
),
)
elifquery.data=="normalglitch":
awaitquery.message.edit_text(
"**SelectGlitchpowerlevel**",
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="1",callback_data="normalglitch1"
),
InlineKeyboardButton(
text="2",callback_data="normalglitch2"
),
InlineKeyboardButton(
text="3",callback_data="normalglitch3"
),
],
[
InlineKeyboardButton(
text="4",callback_data="normalglitch4"
),
InlineKeyboardButton(
text="5",callback_data="normalglitch5"
),
],
]
),
)
elifquery.data=="scanlineglitch":
awaitquery.message.edit_text(
"**SelectGlitchpowerlevel**",
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="1",callback_data="scanlineglitch1"
),
InlineKeyboardButton(
text="2",callback_data="scanlineglitch2"
),
InlineKeyboardButton(
text="3",callback_data="scanlineglitch3"
),
],
[
InlineKeyboardButton(
text="4",callback_data="scanlineglitch4"
),
InlineKeyboardButton(
text="5",callback_data="scanlineglitch5"
),
],
]
),
)
elifquery.data=="blur":
awaitquery.message.edit(
"**SelectaType**",
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(text="box",callback_data="box"),
InlineKeyboardButton(text="normal",callback_data="normal"),
],
[InlineKeyboardButton(text="Gaussian",callback_data="gas")],
]
),
)
elifquery.data=="circle":
awaitquery.message.edit_text(
"**Selectrequiredmode**",
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text="WITHBG",callback_data="circlewithbg"
),
InlineKeyboardButton(
text="WITHOUTBG",callback_data="circlewithoutbg"
),
]
]
),
)
elifquery.data=="border":
awaitquery.message.edit(
"**SelectBorder**",
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton(text="🔴RED🔴",callback_data="red"),
InlineKeyboardButton(
text="🟢Green🟢",callback_data="green"
),
],
[
InlineKeyboardButton(
text="⚫Black⚫",callback_data="black"
),
InlineKeyboardButton(text="🔵Blue🔵",callback_data="blue"),
],
]
),
)

elifquery.data=="bright":
awaitquery.message.delete()
awaitbright(client,query.message)

elifquery.data=="close_e":
awaitquery.message.delete()

elifquery.data=="mix":
awaitquery.message.delete()
awaitmix(client,query.message)

elifquery.data=="b|w":
awaitquery.message.delete()
awaitblack_white(client,query.message)

elifquery.data=="circlewithbg":
awaitquery.message.delete()
awaitcircle_with_bg(client,query.message)

elifquery.data=="circlewithoutbg":
awaitquery.message.delete()
awaitcircle_without_bg(client,query.message)

elifquery.data=="green":
awaitquery.message.delete()
awaitgreen_border(client,query.message)

elifquery.data=="blue":
awaitquery.message.delete()
awaitblue_border(client,query.message)

elifquery.data=="red":
awaitquery.message.delete()
awaitred_border(client,query.message)

elifquery.data=="black":
awaitquery.message.delete()
awaitblack_border(client,query.message)

elifquery.data=="circle_sticker":
awaitquery.message.delete()
awaitround_sticker(client,query.message)

elifquery.data=="inverted":
awaitquery.message.delete()
awaitinverted(client,query.message)

elifquery.data=="stkr":
awaitquery.message.delete()
awaitsticker(client,query.message)

elifquery.data=="cur_ved":
awaitquery.message.delete()
awaitedge_curved(client,query.message)

elifquery.data=="90":
awaitquery.message.delete()
awaitrotate_90(client,query.message)

elifquery.data=="180":
awaitquery.message.delete()
awaitrotate_180(client,query.message)

elifquery.data=="270":
awaitquery.message.delete()
awaitrotate_270(client,query.message)

elifquery.data=="contrast":
awaitquery.message.delete()
awaitcontrast(client,query.message)

elifquery.data=="box":
awaitquery.message.delete()
awaitbox_blur(client,query.message)

elifquery.data=="gas":
awaitquery.message.delete()
awaitg_blur(client,query.message)

elifquery.data=="normal":
awaitquery.message.delete()
awaitnormal_blur(client,query.message)

elifquery.data=="sepia":
awaitquery.message.delete()
awaitsepia_mode(client,query.message)

elifquery.data=="pencil":
awaitquery.message.delete()
awaitpencil(client,query.message)

elifquery.data=="cartoon":
awaitquery.message.delete()
awaitcartoon(client,query.message)

elifquery.data=="normalglitch1":
awaitquery.message.delete()
awaitnormalglitch_1(client,query.message)

elifquery.data=="normalglitch2":
awaitquery.message.delete()
awaitnormalglitch_2(client,query.message)

elifquery.data=="normalglitch3":
awaitnormalglitch_3(client,query.message)

elifquery.data=="normalglitch4":
awaitquery.message.delete()
awaitnormalglitch_4(client,query.message)

elifquery.data=="normalglitch5":
awaitquery.message.delete()
awaitnormalglitch_5(client,query.message)

elifquery.data=="scanlineglitch1":
awaitquery.message.delete()
awaitscanlineglitch_1(client,query.message)

elifquery.data=="scanlineglitch2":
awaitquery.message.delete()
awaitscanlineglitch_2(client,query.message)

elifquery.data=="scanlineglitch3":
awaitquery.message.delete()
awaitscanlineglitch_3(client,query.message)

elifquery.data=="scanlineglitch4":
awaitquery.message.delete()
awaitscanlineglitch_4(client,query.message)

elifquery.data=="scanlineglitch5":
awaitquery.message.delete()
awaitscanlineglitch_5(client,query.message)

elifquery.data=="rmbgwhite":
awaitquery.message.delete()
awaitremovebg_white(client,query.message)

elifquery.data=="rmbgplain":
awaitquery.message.delete()
awaitremovebg_plain(client,query.message)

elifquery.data=="rmbgsticker":
awaitremovebg_sticker(client,query.message)


__mod_name__="ImageEditor"
__help__="""
<b>IMAGEEDITOR</b>
Inerukihavesomeadvancedimageeditingtoolsinbuilt
Bright,Circle,RemBG,Blur,Border,Flip,Glitch,Stickermakerandmore

-/edit[replytoimage]:Opentheimageeditor
-/rmbg[REPLY]:RevoveBGofrepliedimage/sticker.

<i>SpecialcreditstoTroJanzHE</i>
"""
