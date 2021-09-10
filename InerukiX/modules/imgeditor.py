#XByX@TroJanzHEX
#XImprovedXbyXerrorshivansh

fromXpyrogramXimportXfilters
fromXpyrogram.typesXimportX(
XXXXCallbackQuery,
XXXXInlineKeyboardButton,
XXXXInlineKeyboardMarkup,
XXXXMessage,
)

#XByX@TroJanzHEX
fromXInerukiX.Addons.ImageEditor.edit_1XimportX(XX#Xpylint:disable=import-error
XXXXblack_white,
XXXXbox_blur,
XXXXbright,
XXXXg_blur,
XXXXmix,
XXXXnormal_blur,
)
fromXInerukiX.Addons.ImageEditor.edit_2XimportX(XX#Xpylint:disable=import-error
XXXXcartoon,
XXXXcircle_with_bg,
XXXXcircle_without_bg,
XXXXcontrast,
XXXXedge_curved,
XXXXpencil,
XXXXsepia_mode,
XXXXsticker,
)
fromXInerukiX.Addons.ImageEditor.edit_3XimportX(XX#Xpylint:disable=import-error
XXXXblack_border,
XXXXblue_border,
XXXXgreen_border,
XXXXred_border,
)
fromXInerukiX.Addons.ImageEditor.edit_4XimportX(XX#Xpylint:disable=import-error
XXXXinverted,
XXXXremovebg_plain,
XXXXremovebg_sticker,
XXXXremovebg_white,
XXXXrotate_90,
XXXXrotate_180,
XXXXrotate_270,
XXXXround_sticker,
)
fromXInerukiX.Addons.ImageEditor.edit_5XimportX(XX#Xpylint:disable=import-error
XXXXnormalglitch_1,
XXXXnormalglitch_2,
XXXXnormalglitch_3,
XXXXnormalglitch_4,
XXXXnormalglitch_5,
XXXXscanlineglitch_1,
XXXXscanlineglitch_2,
XXXXscanlineglitch_3,
XXXXscanlineglitch_4,
XXXXscanlineglitch_5,
)
fromXInerukiX.services.pyrogramXimportXpbotXasXClient

lelX=X00000000
#Xpylint:disable=import-error
@Client.on_message(filters.command(["edit",X"editor"]))
asyncXdefXphoto(client:XClient,Xmessage:XMessage):
XXXXtry:
XXXXXXXXifXnotXmessage.reply_to_message.photo:
XXXXXXXXXXXXawaitXclient.send_message(message.chat.id,X"ReplyXtoXanXimageXman!ㅤㅤ")
XXXXXXXXXXXXreturn
XXXXexcept:
XXXXXXXXreturn
XXXXglobalXlel
XXXXtry:
XXXXXXXXlelX=Xmessage.from_user.id
XXXXexcept:
XXXXXXXXreturn
XXXXtry:
XXXXXXXXawaitXclient.send_message(
XXXXXXXXXXXXchat_id=message.chat.id,
XXXXXXXXXXXXtext="SelectXyourXrequiredXmodeXfromXbelow!ㅤㅤ",
XXXXXXXXXXXXreply_markup=InlineKeyboardMarkup(
XXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="💡XBRIGHT",Xcallback_data="bright"),
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="🖼XMIXED",Xcallback_data="mix"),
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="🔳XB&W",Xcallback_data="b|w"),
XXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="🟡XCIRCLE",Xcallback_data="circle"),
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="🩸XBLUR",Xcallback_data="blur"),
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="🌌XBORDER",Xcallback_data="border"),
XXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="🎉XSTICKER",Xcallback_data="stick"),
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="↩️XROTATE",Xcallback_data="rotate"),
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="🔦XCONTRAST",Xcallback_data="contrast"
XXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="🌇XSEPIA",Xcallback_data="sepia"),
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="✏️XPENCIL",Xcallback_data="pencil"),
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="🐶XCARTOON",Xcallback_data="cartoon"),
XXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="🔄XINVERT",Xcallback_data="inverted"),
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="🔮XGLITCH",Xcallback_data="glitch"),
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="✂️XREMOVEXBG",Xcallback_data="removebg"
XXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="❌XCLOSE",Xcallback_data="close_e"),
XXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXX]
XXXXXXXXXXXX),
XXXXXXXXXXXXreply_to_message_id=message.reply_to_message.message_id,
XXXXXXXX)
XXXXexceptXExceptionXasXe:
XXXXXXXXprint("photomarkupXerrorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_text("SomethingXwentXwrong!",Xquote=True)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


@Client.on_callback_query()
asyncXdefXcb_handler(client:XClient,Xquery:XCallbackQuery):
XXXXuser_idX=Xquery.from_user.id
XXXXifXlelX==Xuser_id:
XXXXXXXXifXquery.dataX==X"removebg":
XXXXXXXXXXXXawaitXquery.message.edit_text(
XXXXXXXXXXXXXXXX"**SelectXrequiredXmode**ㅤㅤㅤㅤ",
XXXXXXXXXXXXXXXXreply_markup=InlineKeyboardMarkup(
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="WITHXWHITEXBG",Xcallback_data="rmbgwhite"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="WITHOUTXBG",Xcallback_data="rmbgplain"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="STICKER",Xcallback_data="rmbgsticker"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXXelifXquery.dataX==X"stick":
XXXXXXXXXXXXawaitXquery.message.edit(
XXXXXXXXXXXXXXXX"**SelectXaXType**",
XXXXXXXXXXXXXXXXreply_markup=InlineKeyboardMarkup(
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="Normal",Xcallback_data="stkr"),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="EdgeXCurved",Xcallback_data="cur_ved"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="Circle",Xcallback_data="circle_sticker"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXXelifXquery.dataX==X"rotate":
XXXXXXXXXXXXawaitXquery.message.edit_text(
XXXXXXXXXXXXXXXX"**SelectXtheXDegree**",
XXXXXXXXXXXXXXXXreply_markup=InlineKeyboardMarkup(
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="180",Xcallback_data="180"),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="90",Xcallback_data="90"),
XXXXXXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXXXXXX[InlineKeyboardButton(text="270",Xcallback_data="270")],
XXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)

XXXXXXXXelifXquery.dataX==X"glitch":
XXXXXXXXXXXXawaitXquery.message.edit_text(
XXXXXXXXXXXXXXXX"**SelectXrequiredXmode**ㅤㅤㅤㅤ",
XXXXXXXXXXXXXXXXreply_markup=InlineKeyboardMarkup(
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="NORMAL",Xcallback_data="normalglitch"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="SCANXLINES",Xcallback_data="scanlineglitch"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXXelifXquery.dataX==X"normalglitch":
XXXXXXXXXXXXawaitXquery.message.edit_text(
XXXXXXXXXXXXXXXX"**SelectXGlitchXpowerXlevel**",
XXXXXXXXXXXXXXXXreply_markup=InlineKeyboardMarkup(
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="1",Xcallback_data="normalglitch1"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="2",Xcallback_data="normalglitch2"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="3",Xcallback_data="normalglitch3"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="4",Xcallback_data="normalglitch4"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="5",Xcallback_data="normalglitch5"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXXelifXquery.dataX==X"scanlineglitch":
XXXXXXXXXXXXawaitXquery.message.edit_text(
XXXXXXXXXXXXXXXX"**SelectXGlitchXpowerXlevel**",
XXXXXXXXXXXXXXXXreply_markup=InlineKeyboardMarkup(
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="1",Xcallback_data="scanlineglitch1"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="2",Xcallback_data="scanlineglitch2"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="3",Xcallback_data="scanlineglitch3"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="4",Xcallback_data="scanlineglitch4"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="5",Xcallback_data="scanlineglitch5"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXXelifXquery.dataX==X"blur":
XXXXXXXXXXXXawaitXquery.message.edit(
XXXXXXXXXXXXXXXX"**SelectXaXType**",
XXXXXXXXXXXXXXXXreply_markup=InlineKeyboardMarkup(
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="box",Xcallback_data="box"),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="normal",Xcallback_data="normal"),
XXXXXXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXXXXXX[InlineKeyboardButton(text="Gaussian",Xcallback_data="gas")],
XXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXXelifXquery.dataX==X"circle":
XXXXXXXXXXXXawaitXquery.message.edit_text(
XXXXXXXXXXXXXXXX"**SelectXrequiredXmode**",
XXXXXXXXXXXXXXXXreply_markup=InlineKeyboardMarkup(
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="WITHXBG",Xcallback_data="circlewithbg"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="WITHOUTXBG",Xcallback_data="circlewithoutbg"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXXelifXquery.dataX==X"border":
XXXXXXXXXXXXawaitXquery.message.edit(
XXXXXXXXXXXXXXXX"**SelectXBorder**",
XXXXXXXXXXXXXXXXreply_markup=InlineKeyboardMarkup(
XXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="🔴XREDX🔴",Xcallback_data="red"),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="🟢XGreenX🟢",Xcallback_data="green"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext="⚫XBlackX⚫",Xcallback_data="black"
XXXXXXXXXXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(text="🔵XBlueX🔵",Xcallback_data="blue"),
XXXXXXXXXXXXXXXXXXXXXXXX],
XXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)

XXXXXXXXelifXquery.dataX==X"bright":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXbright(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"close_e":
XXXXXXXXXXXXawaitXquery.message.delete()

XXXXXXXXelifXquery.dataX==X"mix":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXmix(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"b|w":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXblack_white(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"circlewithbg":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXcircle_with_bg(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"circlewithoutbg":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXcircle_without_bg(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"green":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXgreen_border(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"blue":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXblue_border(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"red":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXred_border(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"black":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXblack_border(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"circle_sticker":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXround_sticker(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"inverted":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXinverted(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"stkr":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXsticker(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"cur_ved":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXedge_curved(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"90":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXrotate_90(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"180":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXrotate_180(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"270":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXrotate_270(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"contrast":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXcontrast(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"box":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXbox_blur(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"gas":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXg_blur(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"normal":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXnormal_blur(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"sepia":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXsepia_mode(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"pencil":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXpencil(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"cartoon":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXcartoon(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"normalglitch1":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXnormalglitch_1(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"normalglitch2":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXnormalglitch_2(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"normalglitch3":
XXXXXXXXXXXXawaitXnormalglitch_3(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"normalglitch4":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXnormalglitch_4(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"normalglitch5":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXnormalglitch_5(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"scanlineglitch1":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXscanlineglitch_1(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"scanlineglitch2":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXscanlineglitch_2(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"scanlineglitch3":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXscanlineglitch_3(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"scanlineglitch4":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXscanlineglitch_4(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"scanlineglitch5":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXscanlineglitch_5(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"rmbgwhite":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXremovebg_white(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"rmbgplain":
XXXXXXXXXXXXawaitXquery.message.delete()
XXXXXXXXXXXXawaitXremovebg_plain(client,Xquery.message)

XXXXXXXXelifXquery.dataX==X"rmbgsticker":
XXXXXXXXXXXXawaitXremovebg_sticker(client,Xquery.message)


__mod_name__X=X"ImageXEditor"
__help__X=X"""
<b>XIMAGEXEDITORX</b>
InerukiXhaveXsomeXadvancedXimageXeditingXtoolsXinbuilt
Bright,XCircle,XRemBG,XBlur,XBorder,XFlip,XGlitch,XStickerXmakerXandXmore

-X/editX[replyXtoXimage]:XOpenXtheXimageXeditor
-X/rmbgX[REPLY]:XRevoveXBGXofXrepliedXimage/sticker.

<i>XSpecialXcreditsXtoXTroJanzHEXX</i>
"""
