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

fromcontextlibimportsuppress

fromaiogram.types.inline_keyboardimportInlineKeyboardButton,InlineKeyboardMarkup
fromaiogram.utils.callback_dataimportCallbackData
fromaiogram.utils.exceptionsimportMessageNotModified

fromIneruki.decoratorimportregister
fromIneruki.services.mongoimportdb

from.utils.languageimport(
LANGUAGES,
change_chat_lang,
get_chat_lang_info,
get_strings,
get_strings_dec,
)
from.utils.messageimportget_arg

select_lang_cb=CallbackData("select_lang_cb","lang","back_btn")
translators_lang_cb=CallbackData("translators_lang_cb","lang")


@register(cmds="lang",no_args=True,user_can_change_info=True)
asyncdefselect_lang_cmd(message):
awaitselect_lang_keyboard(message)


@get_strings_dec("language")
asyncdefselect_lang_keyboard(message,strings,edit=False):
markup=InlineKeyboardMarkup(row_width=2)
task=message.replyifeditisFalseelsemessage.edit_text

lang_info=awaitget_chat_lang_info(message.chat.id)

ifmessage.chat.type=="private":
text=strings["your_lang"].format(
lang=lang_info["flag"]+""+lang_info["babel"].display_name
)
text+=strings["select_pm_lang"]

#TODO:Connectedchatlanginfo

else:
text=strings["chat_lang"].format(
lang=lang_info["flag"]+""+lang_info["babel"].display_name
)
text+=strings["select_chat_lang"]

forlanginLANGUAGES.values():
lang_info=lang["language_info"]
markup.insert(
InlineKeyboardButton(
lang_info["flag"]+""+lang_info["babel"].display_name,
callback_data=select_lang_cb.new(
lang=lang_info["code"],back_btn=FalseifeditisFalseelseTrue
),
)
)

markup.add(
InlineKeyboardButton(
strings["crowdin_btn"],url="https://t.me/Inerukisupport_official"
)
)
ifedit:
markup.add(InlineKeyboardButton(strings["back"],callback_data="go_to_start"))
withsuppress(MessageNotModified):
awaittask(text,reply_markup=markup)


asyncdefchange_lang(message,lang,e=False,back_btn=False):
chat_id=message.chat.id
awaitchange_chat_lang(chat_id,lang)

strings=awaitget_strings(chat_id,"language")

lang_info=LANGUAGES[lang]["language_info"]

text=strings["lang_changed"].format(
lang_name=lang_info["flag"]+""+lang_info["babel"].display_name
)
text+=strings["help_us_translate"]

markup=InlineKeyboardMarkup()

if"translators"inlang_info:
markup.add(
InlineKeyboardButton(
strings["see_translators"],
callback_data=translators_lang_cb.new(lang=lang),
)
)

ifback_btn=="True":
#Callback_dataconvertsbooleantostr
markup.add(InlineKeyboardButton(strings["back"],callback_data="go_to_start"))

ife:
withsuppress(MessageNotModified):
awaitmessage.edit_text(
text,reply_markup=markup,disable_web_page_preview=True
)
else:
awaitmessage.reply(text,reply_markup=markup,disable_web_page_preview=True)


@register(cmds="lang",has_args=True,user_can_change_info=True)
@get_strings_dec("language")
asyncdefselect_lang_msg(message,strings):
lang=get_arg(message).lower()

iflangnotinLANGUAGES:
awaitmessage.reply(strings["not_supported_lang"])
return

awaitchange_lang(message,lang)


@register(
select_lang_cb.filter(),
f="cb",
allow_kwargs=True,
)
asyncdefselect_lang_callback(query,callback_data=None,**kwargs):
lang=callback_data["lang"]
back_btn=callback_data["back_btn"]
awaitchange_lang(query.message,lang,e=True,back_btn=back_btn)


asyncdef__stats__():
returnf"*<code>{len(LANGUAGES)}</code>languagesloaded.\n"


asyncdef__export__(chat_id):
lang=awaitget_chat_lang_info(chat_id)

return{"language":lang["code"]}


asyncdef__import__(chat_id,data):
ifdatanotinLANGUAGES:
return
awaitdb.lang.update_one(
{"chat_id":chat_id},{"$set":{"lang":data}},upsert=True
)


__mod_name__="Languages"

__help__="""
ThismoduleisdedicatedtowardsutlisingIneruki'slocalizationfeature!Youcanalso<ahref='https://crowdin.com/project/Inerukix'>contribute</a>forimprovinglocalizationinIneruki!

<b>Availablecommands:</b>
-/lang:Showsalistofavaiblelanguages
-/lang(languagecodename):Setsalanguage

<b>Example:</b><code>/lang</code>
Inerukiwillsendyoubunchofinlinebuttonswhereyoucanselectyourpreferedlanguageinterativelywithoutanyhassles!
"""
