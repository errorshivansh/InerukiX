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

fromXcontextlibXimportXsuppress

fromXaiogram.types.inline_keyboardXimportXInlineKeyboardButton,XInlineKeyboardMarkup
fromXaiogram.utils.callback_dataXimportXCallbackData
fromXaiogram.utils.exceptionsXimportXMessageNotModified

fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.mongoXimportXdb

fromX.utils.languageXimportX(
XXXXLANGUAGES,
XXXXchange_chat_lang,
XXXXget_chat_lang_info,
XXXXget_strings,
XXXXget_strings_dec,
)
fromX.utils.messageXimportXget_arg

select_lang_cbX=XCallbackData("select_lang_cb",X"lang",X"back_btn")
translators_lang_cbX=XCallbackData("translators_lang_cb",X"lang")


@register(cmds="lang",Xno_args=True,Xuser_can_change_info=True)
asyncXdefXselect_lang_cmd(message):
XXXXawaitXselect_lang_keyboard(message)


@get_strings_dec("language")
asyncXdefXselect_lang_keyboard(message,Xstrings,Xedit=False):
XXXXmarkupX=XInlineKeyboardMarkup(row_width=2)
XXXXtaskX=Xmessage.replyXifXeditXisXFalseXelseXmessage.edit_text

XXXXlang_infoX=XawaitXget_chat_lang_info(message.chat.id)

XXXXifXmessage.chat.typeX==X"private":
XXXXXXXXtextX=Xstrings["your_lang"].format(
XXXXXXXXXXXXlang=lang_info["flag"]X+X"X"X+Xlang_info["babel"].display_name
XXXXXXXX)
XXXXXXXXtextX+=Xstrings["select_pm_lang"]

XXXX#XTODO:XConnectedXchatXlangXinfo

XXXXelse:
XXXXXXXXtextX=Xstrings["chat_lang"].format(
XXXXXXXXXXXXlang=lang_info["flag"]X+X"X"X+Xlang_info["babel"].display_name
XXXXXXXX)
XXXXXXXXtextX+=Xstrings["select_chat_lang"]

XXXXforXlangXinXLANGUAGES.values():
XXXXXXXXlang_infoX=Xlang["language_info"]
XXXXXXXXmarkup.insert(
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXlang_info["flag"]X+X"X"X+Xlang_info["babel"].display_name,
XXXXXXXXXXXXXXXXcallback_data=select_lang_cb.new(
XXXXXXXXXXXXXXXXXXXXlang=lang_info["code"],Xback_btn=FalseXifXeditXisXFalseXelseXTrue
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXX)

XXXXmarkup.add(
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXstrings["crowdin_btn"],Xurl="https://t.me/Inerukisupport_official"
XXXXXXXX)
XXXX)
XXXXifXedit:
XXXXXXXXmarkup.add(InlineKeyboardButton(strings["back"],Xcallback_data="go_to_start"))
XXXXwithXsuppress(MessageNotModified):
XXXXXXXXawaitXtask(text,Xreply_markup=markup)


asyncXdefXchange_lang(message,Xlang,Xe=False,Xback_btn=False):
XXXXchat_idX=Xmessage.chat.id
XXXXawaitXchange_chat_lang(chat_id,Xlang)

XXXXstringsX=XawaitXget_strings(chat_id,X"language")

XXXXlang_infoX=XLANGUAGES[lang]["language_info"]

XXXXtextX=Xstrings["lang_changed"].format(
XXXXXXXXlang_name=lang_info["flag"]X+X"X"X+Xlang_info["babel"].display_name
XXXX)
XXXXtextX+=Xstrings["help_us_translate"]

XXXXmarkupX=XInlineKeyboardMarkup()

XXXXifX"translators"XinXlang_info:
XXXXXXXXmarkup.add(
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXstrings["see_translators"],
XXXXXXXXXXXXXXXXcallback_data=translators_lang_cb.new(lang=lang),
XXXXXXXXXXXX)
XXXXXXXX)

XXXXifXback_btnX==X"True":
XXXXXXXX#XCallback_dataXconvertsXbooleanXtoXstr
XXXXXXXXmarkup.add(InlineKeyboardButton(strings["back"],Xcallback_data="go_to_start"))

XXXXifXe:
XXXXXXXXwithXsuppress(MessageNotModified):
XXXXXXXXXXXXawaitXmessage.edit_text(
XXXXXXXXXXXXXXXXtext,Xreply_markup=markup,Xdisable_web_page_preview=True
XXXXXXXXXXXX)
XXXXelse:
XXXXXXXXawaitXmessage.reply(text,Xreply_markup=markup,Xdisable_web_page_preview=True)


@register(cmds="lang",Xhas_args=True,Xuser_can_change_info=True)
@get_strings_dec("language")
asyncXdefXselect_lang_msg(message,Xstrings):
XXXXlangX=Xget_arg(message).lower()

XXXXifXlangXnotXinXLANGUAGES:
XXXXXXXXawaitXmessage.reply(strings["not_supported_lang"])
XXXXXXXXreturn

XXXXawaitXchange_lang(message,Xlang)


@register(
XXXXselect_lang_cb.filter(),
XXXXf="cb",
XXXXallow_kwargs=True,
)
asyncXdefXselect_lang_callback(query,Xcallback_data=None,X**kwargs):
XXXXlangX=Xcallback_data["lang"]
XXXXback_btnX=Xcallback_data["back_btn"]
XXXXawaitXchange_lang(query.message,Xlang,Xe=True,Xback_btn=back_btn)


asyncXdefX__stats__():
XXXXreturnXf"*X<code>{len(LANGUAGES)}</code>XlanguagesXloaded.\n"


asyncXdefX__export__(chat_id):
XXXXlangX=XawaitXget_chat_lang_info(chat_id)

XXXXreturnX{"language":Xlang["code"]}


asyncXdefX__import__(chat_id,Xdata):
XXXXifXdataXnotXinXLANGUAGES:
XXXXXXXXreturn
XXXXawaitXdb.lang.update_one(
XXXXXXXX{"chat_id":Xchat_id},X{"$set":X{"lang":Xdata}},Xupsert=True
XXXX)


__mod_name__X=X"Languages"

__help__X=X"""
ThisXmoduleXisXdedicatedXtowardsXutlisingXIneruki'sXlocalizationXfeature!XYouXcanXalsoX<aXhref='https://crowdin.com/project/InerukiXx'>contribute</a>XforXimprovingXlocalizationXinXIneruki!

<b>AvailableXcommands:</b>
-X/lang:XShowsXaXlistXofXavaibleXlanguages
-X/langX(languageXcodename):XSetsXaXlanguage

<b>Example:</b>X<code>/lang</code>
InerukiXwillXsendXyouXbunchXofXinlineXbuttonsXwhereXyouXcanXselectXyourXpreferedXlanguageXinterativelyXwithoutXanyXhassles!
"""
