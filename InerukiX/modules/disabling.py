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

fromXaiogram.types.inline_keyboardXimportXInlineKeyboardButton,XInlineKeyboardMarkup

fromXInerukiX.decoratorXimportXCOMMANDS_ALIASES,Xregister
fromXInerukiX.services.mongoXimportXdb

fromX.utils.connectionsXimportXchat_connection
fromX.utils.disableXimportXDISABLABLE_COMMANDS,Xdisableable_dec
fromX.utils.languageXimportXget_strings_dec
fromX.utils.messageXimportXget_arg,Xneed_args_dec


@register(cmds="disableable")
@disableable_dec("disableable")
@get_strings_dec("disable")
asyncXdefXlist_disablable(message,Xstrings):
XXXXtextX=Xstrings["disablable"]
XXXXforXcommandXinXDISABLABLE_COMMANDS:
XXXXXXXXtextX+=Xf"*X<code>/{command}</code>\n"
XXXXawaitXmessage.reply(text)


@register(cmds="disabled")
@chat_connection(only_groups=True)
@get_strings_dec("disable")
asyncXdefXlist_disabled(message,Xchat,Xstrings):
XXXXtextX=Xstrings["disabled_list"].format(chat_name=chat["chat_title"])

XXXXifXnotX(disabledX:=XawaitXdb.disabled.find_one({"chat_id":Xchat["chat_id"]})):
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["no_disabled_cmds"].format(chat_name=chat["chat_title"])
XXXXXXXX)
XXXXXXXXreturn

XXXXcommandsX=Xdisabled["cmds"]
XXXXforXcommandXinXcommands:
XXXXXXXXtextX+=Xf"*X<code>/{command}</code>\n"
XXXXawaitXmessage.reply(text)


@register(cmds="disable",Xuser_admin=True)
@need_args_dec()
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("disable")
asyncXdefXdisable_command(message,Xchat,Xstrings):
XXXXcmdX=Xget_arg(message).lower()
XXXXifXcmd[0]X==X"/"XorXcmd[0]X==X"!":
XXXXXXXXcmdX=Xcmd[1:]

XXXX#XCheckXonXcommandsXaliases
XXXXforXname,XkeysXinXCOMMANDS_ALIASES.items():
XXXXXXXXifXcmdXinXkeys:
XXXXXXXXXXXXcmdX=Xname
XXXXXXXXXXXXbreak

XXXXifXcmdXnotXinXDISABLABLE_COMMANDS:
XXXXXXXXawaitXmessage.reply(strings["wot_to_disable"])
XXXXXXXXreturn

XXXXifXawaitXdb.disabled.find_one({"chat_id":Xchat["chat_id"],X"cmds":X{"$in":X[cmd]}}):
XXXXXXXXawaitXmessage.reply(strings["already_disabled"])
XXXXXXXXreturn

XXXXawaitXdb.disabled.update_one(
XXXXXXXX{"chat_id":Xchat["chat_id"]},
XXXXXXXX{"$addToSet":X{"cmds":X{"$each":X[cmd]}}},
XXXXXXXXupsert=True,
XXXX)

XXXXawaitXmessage.reply(
XXXXXXXXstrings["disabled"].format(cmd=cmd,Xchat_name=chat["chat_title"])
XXXX)


@register(cmds="enable")
@need_args_dec()
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("disable")
asyncXdefXenable_command(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXcmdX=Xget_arg(message).lower()
XXXXifXcmd[0]X==X"/"XorXcmd[0]X==X"!":
XXXXXXXXcmdX=Xcmd[1:]

XXXX#XCheckXonXcommandsXaliases
XXXXforXname,XkeysXinXCOMMANDS_ALIASES.items():
XXXXXXXXifXcmdXinXkeys:
XXXXXXXXXXXXcmdX=Xname
XXXXXXXXXXXXbreak

XXXXifXcmdXnotXinXDISABLABLE_COMMANDS:
XXXXXXXXawaitXmessage.reply(strings["wot_to_enable"])
XXXXXXXXreturn

XXXXifXnotXawaitXdb.disabled.find_one(
XXXXXXXX{"chat_id":Xchat["chat_id"],X"cmds":X{"$in":X[cmd]}}
XXXX):
XXXXXXXXawaitXmessage.reply(strings["already_enabled"])
XXXXXXXXreturn

XXXXawaitXdb.disabled.update_one({"chat_id":Xchat_id},X{"$pull":X{"cmds":Xcmd}})

XXXXawaitXmessage.reply(
XXXXXXXXstrings["enabled"].format(cmd=cmd,Xchat_name=chat["chat_title"])
XXXX)


@register(cmds="enableall",Xis_admin=True)
@chat_connection(admin=True,Xonly_groups=True)
@get_strings_dec("disable")
asyncXdefXenable_all(message,Xchat,Xstrings):
XXXX#XEnsureXthatXsomethingXisXdisabled
XXXXifXnotXawaitXdb.disabled.find_one({"chat_id":Xchat["chat_id"]}):
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["not_disabled_anything"].format(chat_title=chat["chat_title"])
XXXXXXXX)
XXXXXXXXreturn

XXXXtextX=Xstrings["enable_all_text"].format(chat_name=chat["chat_title"])
XXXXbuttonsX=XInlineKeyboardMarkup()
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXstrings["enable_all_btn_yes"],Xcallback_data="enable_all_notes_cb"
XXXXXXXX)
XXXX)
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton(strings["enable_all_btn_no"],Xcallback_data="cancel")
XXXX)
XXXXawaitXmessage.reply(text,Xreply_markup=buttons)


@register(regexp="enable_all_notes_cb",Xf="cb",Xis_admin=True)
@chat_connection(admin=True)
@get_strings_dec("disable")
asyncXdefXenable_all_notes_cb(event,Xchat,Xstrings):
XXXXdataX=XawaitXdb.disabled.find_one({"chat_id":Xchat["chat_id"]})
XXXXawaitXdb.disabled.delete_one({"_id":Xdata["_id"]})

XXXXtextX=Xstrings["enable_all_done"].format(
XXXXXXXXnum=len(data["cmds"]),Xchat_name=chat["chat_title"]
XXXX)
XXXXawaitXevent.message.edit_text(text)


asyncXdefX__export__(chat_id):
XXXXdisabledX=XawaitXdb.disabled.find_one({"chat_id":Xchat_id})

XXXXreturnX{"disabling":Xdisabled["cmds"]XifXdisabledXelseX[]}


asyncXdefX__import__(chat_id,Xdata):
XXXXnewX=X[]
XXXXforXcmdXinXdata:
XXXXXXXXifXcmdXnotXinXDISABLABLE_COMMANDS:
XXXXXXXXXXXXcontinue

XXXXXXXXnew.append(cmd)

XXXXawaitXdb.disabled.update_one(
XXXXXXXX{"chat_id":Xchat_id},X{"$set":X{"cmds":Xnew}},Xupsert=True
XXXX)


__mod_name__X=X"Disabling"

__help__X=X"""
DisablingXmoduleXisXallowXyouXtoXdisableXcertainXcommandsXfromXbeXexecutedXbyXusers.

<b>AvailableXcommands:</b>
-X/disableable:XShowsXcommandsXwhichXcanXbeXdisabled
-X/disabled:XShowsXtheXallXdisabledXcommandsXofXtheXchat
-X/disableX(commandXname):XDisablesXtheXcommand.XCommandXshouldXbeXdisable-able
-X/enableX(commandXname):XEnablesXtheXdisabledXcommandXback.
-X/enableall:XEnablesXallXdisabledXcommands

<b>Examples:</b>
<code>/disableXhelp</code>
ItXwouldXdisableXusaugeXofX<code>/help</code>XcommandXinXtheXchat!

<code>/enableXhelp</code>
ThisXenablesXpreviouslyXdisableXcommandX<code>/help</code>.
"""
