#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2021errorshivansh
#Copyright(C)2020InukaAsith

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

importrandom
fromcontextlibimportsuppress

fromaiogram.types.inline_keyboardimportInlineKeyboardButton,InlineKeyboardMarkup
fromaiogram.utils.callback_dataimportCallbackData
fromaiogram.utils.exceptionsimportMessageNotModified

fromIneruki.decoratorimportregister
fromIneruki.modules.utils.disableimportdisableable_dec

from.importMOD_HELP
from.languageimportselect_lang_keyboard
from.utils.disableimportdisableable_dec
from.utils.languageimportget_strings_dec

helpmenu_cb=CallbackData("helpmenu","mod")


defhelp_markup(modules):
markup=InlineKeyboardMarkup()
formoduleinmodules:
markup.insert(
InlineKeyboardButton(module,callback_data=helpmenu_cb.new(mod=module))
)
returnmarkup


STICKERS=(
"CAACAgUAAxkBAAJOGmBeli95P073FKVkgc4esfKE4UlAAIOAgACyavAVkbLMIidWYdyHgQ",
"CAACAgUAAxkBAAJOG2BeljABwlCfwzHT1gzyiciBri6_AAIsAgACBPBVgpGQRz-1qmlHgQ",
"CAACAgUAAxkBAAJOHGBeljOJ35CQNnkpnVcgRoHuJ6DAAL3AQACN8TBVm1PIART01cWHgQ",
"CAACAgUAAxkBAAJOHWBeljW9QzYQ51gpCjHZHCF5Ui6AAJ7AgAC3zDBVo2xenp7JYhAHgQ",
"CAACAgUAAxkBAAJOHmBeljjU0_FT_QpdUUJBqVUC0nfJAAKYAgACJ_jBVvntHY_8WF27HgQ",
"CAACAgUAAxkBAAJOH2BeljrV68mPLu8_6n4edT20Q3IQAAJ9AgACq3LBVmLuZuNPlvkfHgQ",
"CAACAgUAAxkBAAJOIGBeljttuniUPykRtzkSZj3SRwKJAAI7AgACNm_BVp8TCkE6ZqCoHgQ",
"CAACAgUAAxkBAAJOIWBelj-P_2vtVqtkF2OMlVN3M0N4AAK3AQACSm3BVkF2voraS2tHgQ",
"CAACAgUAAxkBAAJOImBelkJxUBm2rL1iPfMZfk-_9DaOAALrAgAC4T3BVniopQVsZ4KHgQ",
"CAACAgUAAxkBAAJOI2BelkMO0A_wtAc7hUZz1NixuMlAAKEAwACY4TAViVuNLTBmmkgHgQ",
)


@register(cmds="start",no_args=True,only_groups=True)
@disableable_dec("start")
@get_strings_dec("pm_menu")
asyncdefstart_group_cmd(message,strings):
awaitmessage.reply(strings["start_hi_group"])


@register(cmds="start",no_args=True,only_pm=True)
asyncdefstart_cmd(message):
awaitmessage.reply_sticker(random.choice(STICKERS))
awaitget_start_func(message)


@get_strings_dec("pm_menu")
asyncdefget_start_func(message,strings,edit=False):
msg=message.messageifhasattr(message,"message")elsemessage

task=msg.edit_textifeditelsemsg.reply
buttons=InlineKeyboardMarkup()
buttons.add(InlineKeyboardButton(strings["btn_help"],callback_data="get_help"))
buttons.add(
InlineKeyboardButton(strings["btn_lang"],callback_data="lang_btn"),
InlineKeyboardButton(
strings["btn_source"],url="https://github.com/errorshivansh/"
),
)
buttons.add(
InlineKeyboardButton(
strings["btn_channel"],url="https://t.me/InerukiUpdates"
),
InlineKeyboardButton(
strings["btn_group"],url="https://t.me/InerukiSupport_Official"
),
)
buttons.add(
InlineKeyboardButton(
"👸🏼AddInerukitoyourgroup",
url=f"https://telegram.me/Inerukixbot?startgroup=true",
)
)
#Handleerrorwhenuserclickthebutton2ormoretimessimultaneously
withsuppress(MessageNotModified):
awaittask(strings["start_hi"],reply_markup=buttons)


@register(regexp="get_help",f="cb")
@get_strings_dec("pm_menu")
asyncdefhelp_cb(event,strings):
button=help_markup(MOD_HELP)
button.add(InlineKeyboardButton(strings["back"],callback_data="go_to_start"))
withsuppress(MessageNotModified):
awaitevent.message.edit_text(strings["help_header"],reply_markup=button)


@register(regexp="lang_btn",f="cb")
asyncdefset_lang_cb(event):
awaitselect_lang_keyboard(event.message,edit=True)


@register(regexp="go_to_start",f="cb")
asyncdefback_btn(event):
awaitget_start_func(event,edit=True)


@register(cmds="help",only_pm=True)
@disableable_dec("help")
@get_strings_dec("pm_menu")
asyncdefhelp_cmd(message,strings):
button=help_markup(MOD_HELP)
button.add(InlineKeyboardButton(strings["back"],callback_data="go_to_start"))
awaitmessage.reply(strings["help_header"],reply_markup=button)


@register(cmds="help",only_groups=True)
@disableable_dec("help")
@get_strings_dec("pm_menu")
asyncdefhelp_cmd_g(message,strings):
text=strings["btn_group_help"]
button=InlineKeyboardMarkup().add(
InlineKeyboardButton(text=text,url="https://t.me/InerukiBOT?start")
)
awaitmessage.reply(strings["help_header"],reply_markup=button)


@register(helpmenu_cb.filter(),f="cb",allow_kwargs=True)
asyncdefhelpmenu_callback(query,callback_data=None,**kwargs):
mod=callback_data["mod"]
ifnotmodinMOD_HELP:
awaitquery.answer()
return
msg=f"Helpfor<b>{mod}</b>module:\n"
msg+=f"{MOD_HELP[mod]}"
button=InlineKeyboardMarkup().add(
InlineKeyboardButton(text="🏃‍♂️Back",callback_data="get_help")
)
withsuppress(MessageNotModified):
awaitquery.message.edit_text(
msg,disable_web_page_preview=True,reply_markup=button
)
awaitquery.answer("Helpfor"+mod)
