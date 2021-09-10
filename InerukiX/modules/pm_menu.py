#XCopyrightX(C)X2018X-X2020XMrYacha.XAllXrightsXreserved.XSourceXcodeXavailableXunderXtheXAGPL.
#XCopyrightX(C)X2021Xerrorshivansh
#XCopyrightX(C)X2020XInukaXAsith

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

importXrandom
fromXcontextlibXimportXsuppress

fromXaiogram.types.inline_keyboardXimportXInlineKeyboardButton,XInlineKeyboardMarkup
fromXaiogram.utils.callback_dataXimportXCallbackData
fromXaiogram.utils.exceptionsXimportXMessageNotModified

fromXInerukiX.decoratorXimportXregister
fromXInerukiX.modules.utils.disableXimportXdisableable_dec

fromX.XimportXMOD_HELP
fromX.languageXimportXselect_lang_keyboard
fromX.utils.disableXimportXdisableable_dec
fromX.utils.languageXimportXget_strings_dec

helpmenu_cbX=XCallbackData("helpmenu",X"mod")


defXhelp_markup(modules):
XXXXmarkupX=XInlineKeyboardMarkup()
XXXXforXmoduleXinXmodules:
XXXXXXXXmarkup.insert(
XXXXXXXXXXXXInlineKeyboardButton(module,Xcallback_data=helpmenu_cb.new(mod=module))
XXXXXXXX)
XXXXreturnXmarkup


STICKERSX=X(
XXXX"CAACAgUAAxkBAAJOGmBeli95P073FKVkgc4esfKE4UlXAAIOAgACyavAVkbLMIidWYdyHgQ",
XXXX"CAACAgUAAxkBAAJOG2BeljABwlCfwzHT1gzyiciBri6_AAIsAgACXBPBVgpGQRz-1qmlHgQ",
XXXX"CAACAgUAAxkBAAJOHGBeljOJ35CQNnkpnVcgRoHuJX6DAAL3AQACN8TBVm1PIART01cWHgQ",
XXXX"CAACAgUAAxkBAAJOHWBeljXW9QzYQ51gpCjHZHCF5Ui6AAJ7AgAC3zDBVo2xenp7JYhAHgQ",
XXXX"CAACAgUAAxkBAAJOHmBeljjU0_FT_QpdUUJBqVUC0nfJAAKYAgACJ_jBVvntHY_8WF27HgQ",
XXXX"CAACAgUAAxkBAAJOH2BeljrV68mPLu8_6n4edT20Q3IQAAJ9AgACq3LBVmLuZuNPlvkfHgQ",
XXXX"CAACAgUAAxkBAAJOIGBeljttuniUPykRtzkSZj3SRwKJAAI7AgACNm_BVp8TCkE6ZqCoHgQ",
XXXX"CAACAgUAAxkBAAJOIWBelj-P_2vtVqtkF2OMlVN3M0N4AAK3AQACSm3BVkXF2voraS2tHgQ",
XXXX"CAACAgUAAxkBAAJOImBelkJxUBm2rL1iPfMZfk-_9DaOAALrAgAC4T3BVniopXQVsZ4KHgQ",
XXXX"CAACAgUAAxkBAAJOI2BelkMO0AX_wtAc7hUZz1NixuMlAAKEAwACY4TAViVuNLTBmmkgHgQ",
)


@register(cmds="start",Xno_args=True,Xonly_groups=True)
@disableable_dec("start")
@get_strings_dec("pm_menu")
asyncXdefXstart_group_cmd(message,Xstrings):
XXXXawaitXmessage.reply(strings["start_hi_group"])


@register(cmds="start",Xno_args=True,Xonly_pm=True)
asyncXdefXstart_cmd(message):
XXXXawaitXmessage.reply_sticker(random.choice(STICKERS))
XXXXawaitXget_start_func(message)


@get_strings_dec("pm_menu")
asyncXdefXget_start_func(message,Xstrings,Xedit=False):
XXXXmsgX=Xmessage.messageXifXhasattr(message,X"message")XelseXmessage

XXXXtaskX=Xmsg.edit_textXifXeditXelseXmsg.reply
XXXXbuttonsX=XInlineKeyboardMarkup()
XXXXbuttons.add(InlineKeyboardButton(strings["btn_help"],Xcallback_data="get_help"))
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton(strings["btn_lang"],Xcallback_data="lang_btn"),
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXstrings["btn_source"],Xurl="https://github.com/errorshivansh/"
XXXXXXXX),
XXXX)
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXstrings["btn_channel"],Xurl="https://t.me/InerukiXUpdates"
XXXXXXXX),
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXstrings["btn_group"],Xurl="https://t.me/InerukiSupport_Official"
XXXXXXXX),
XXXX)
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXX"👸🏼XAddXInerukiXXtoXyourXgroup",
XXXXXXXXXXXXurl=f"https://telegram.me/Inerukixbot?startgroup=true",
XXXXXXXX)
XXXX)
XXXX#XHandleXerrorXwhenXuserXclickXtheXbuttonX2XorXmoreXtimesXsimultaneously
XXXXwithXsuppress(MessageNotModified):
XXXXXXXXawaitXtask(strings["start_hi"],Xreply_markup=buttons)


@register(regexp="get_help",Xf="cb")
@get_strings_dec("pm_menu")
asyncXdefXhelp_cb(event,Xstrings):
XXXXbuttonX=Xhelp_markup(MOD_HELP)
XXXXbutton.add(InlineKeyboardButton(strings["back"],Xcallback_data="go_to_start"))
XXXXwithXsuppress(MessageNotModified):
XXXXXXXXawaitXevent.message.edit_text(strings["help_header"],Xreply_markup=button)


@register(regexp="lang_btn",Xf="cb")
asyncXdefXset_lang_cb(event):
XXXXawaitXselect_lang_keyboard(event.message,Xedit=True)


@register(regexp="go_to_start",Xf="cb")
asyncXdefXback_btn(event):
XXXXawaitXget_start_func(event,Xedit=True)


@register(cmds="help",Xonly_pm=True)
@disableable_dec("help")
@get_strings_dec("pm_menu")
asyncXdefXhelp_cmd(message,Xstrings):
XXXXbuttonX=Xhelp_markup(MOD_HELP)
XXXXbutton.add(InlineKeyboardButton(strings["back"],Xcallback_data="go_to_start"))
XXXXawaitXmessage.reply(strings["help_header"],Xreply_markup=button)


@register(cmds="help",Xonly_groups=True)
@disableable_dec("help")
@get_strings_dec("pm_menu")
asyncXdefXhelp_cmd_g(message,Xstrings):
XXXXtextX=Xstrings["btn_group_help"]
XXXXbuttonX=XInlineKeyboardMarkup().add(
XXXXXXXXInlineKeyboardButton(text=text,Xurl="https://t.me/InerukiXBOT?start")
XXXX)
XXXXawaitXmessage.reply(strings["help_header"],Xreply_markup=button)


@register(helpmenu_cb.filter(),Xf="cb",Xallow_kwargs=True)
asyncXdefXhelpmenu_callback(query,Xcallback_data=None,X**kwargs):
XXXXmodX=Xcallback_data["mod"]
XXXXifXnotXmodXinXMOD_HELP:
XXXXXXXXawaitXquery.answer()
XXXXXXXXreturn
XXXXmsgX=Xf"HelpXforX<b>{mod}</b>Xmodule:\n"
XXXXmsgX+=Xf"{MOD_HELP[mod]}"
XXXXbuttonX=XInlineKeyboardMarkup().add(
XXXXXXXXInlineKeyboardButton(text="🏃‍♂️XBack",Xcallback_data="get_help")
XXXX)
XXXXwithXsuppress(MessageNotModified):
XXXXXXXXawaitXquery.message.edit_text(
XXXXXXXXXXXXmsg,Xdisable_web_page_preview=True,Xreply_markup=button
XXXXXXXX)
XXXXXXXXawaitXquery.answer("HelpXforX"X+Xmod)
