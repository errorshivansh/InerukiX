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

fromaiogram.types.inline_keyboardimportInlineKeyboardButton,InlineKeyboardMarkup

fromIneruki.decoratorimportCOMMANDS_ALIASES,register
fromIneruki.services.mongoimportdb

from.utils.connectionsimportchat_connection
from.utils.disableimportDISABLABLE_COMMANDS,disableable_dec
from.utils.languageimportget_strings_dec
from.utils.messageimportget_arg,need_args_dec


@register(cmds="disableable")
@disableable_dec("disableable")
@get_strings_dec("disable")
asyncdeflist_disablable(message,strings):
text=strings["disablable"]
forcommandinDISABLABLE_COMMANDS:
text+=f"*<code>/{command}</code>\n"
awaitmessage.reply(text)


@register(cmds="disabled")
@chat_connection(only_groups=True)
@get_strings_dec("disable")
asyncdeflist_disabled(message,chat,strings):
text=strings["disabled_list"].format(chat_name=chat["chat_title"])

ifnot(disabled:=awaitdb.disabled.find_one({"chat_id":chat["chat_id"]})):
awaitmessage.reply(
strings["no_disabled_cmds"].format(chat_name=chat["chat_title"])
)
return

commands=disabled["cmds"]
forcommandincommands:
text+=f"*<code>/{command}</code>\n"
awaitmessage.reply(text)


@register(cmds="disable",user_admin=True)
@need_args_dec()
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("disable")
asyncdefdisable_command(message,chat,strings):
cmd=get_arg(message).lower()
ifcmd[0]=="/"orcmd[0]=="!":
cmd=cmd[1:]

#Checkoncommandsaliases
forname,keysinCOMMANDS_ALIASES.items():
ifcmdinkeys:
cmd=name
break

ifcmdnotinDISABLABLE_COMMANDS:
awaitmessage.reply(strings["wot_to_disable"])
return

ifawaitdb.disabled.find_one({"chat_id":chat["chat_id"],"cmds":{"$in":[cmd]}}):
awaitmessage.reply(strings["already_disabled"])
return

awaitdb.disabled.update_one(
{"chat_id":chat["chat_id"]},
{"$addToSet":{"cmds":{"$each":[cmd]}}},
upsert=True,
)

awaitmessage.reply(
strings["disabled"].format(cmd=cmd,chat_name=chat["chat_title"])
)


@register(cmds="enable")
@need_args_dec()
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("disable")
asyncdefenable_command(message,chat,strings):
chat_id=chat["chat_id"]
cmd=get_arg(message).lower()
ifcmd[0]=="/"orcmd[0]=="!":
cmd=cmd[1:]

#Checkoncommandsaliases
forname,keysinCOMMANDS_ALIASES.items():
ifcmdinkeys:
cmd=name
break

ifcmdnotinDISABLABLE_COMMANDS:
awaitmessage.reply(strings["wot_to_enable"])
return

ifnotawaitdb.disabled.find_one(
{"chat_id":chat["chat_id"],"cmds":{"$in":[cmd]}}
):
awaitmessage.reply(strings["already_enabled"])
return

awaitdb.disabled.update_one({"chat_id":chat_id},{"$pull":{"cmds":cmd}})

awaitmessage.reply(
strings["enabled"].format(cmd=cmd,chat_name=chat["chat_title"])
)


@register(cmds="enableall",is_admin=True)
@chat_connection(admin=True,only_groups=True)
@get_strings_dec("disable")
asyncdefenable_all(message,chat,strings):
#Ensurethatsomethingisdisabled
ifnotawaitdb.disabled.find_one({"chat_id":chat["chat_id"]}):
awaitmessage.reply(
strings["not_disabled_anything"].format(chat_title=chat["chat_title"])
)
return

text=strings["enable_all_text"].format(chat_name=chat["chat_title"])
buttons=InlineKeyboardMarkup()
buttons.add(
InlineKeyboardButton(
strings["enable_all_btn_yes"],callback_data="enable_all_notes_cb"
)
)
buttons.add(
InlineKeyboardButton(strings["enable_all_btn_no"],callback_data="cancel")
)
awaitmessage.reply(text,reply_markup=buttons)


@register(regexp="enable_all_notes_cb",f="cb",is_admin=True)
@chat_connection(admin=True)
@get_strings_dec("disable")
asyncdefenable_all_notes_cb(event,chat,strings):
data=awaitdb.disabled.find_one({"chat_id":chat["chat_id"]})
awaitdb.disabled.delete_one({"_id":data["_id"]})

text=strings["enable_all_done"].format(
num=len(data["cmds"]),chat_name=chat["chat_title"]
)
awaitevent.message.edit_text(text)


asyncdef__export__(chat_id):
disabled=awaitdb.disabled.find_one({"chat_id":chat_id})

return{"disabling":disabled["cmds"]ifdisabledelse[]}


asyncdef__import__(chat_id,data):
new=[]
forcmdindata:
ifcmdnotinDISABLABLE_COMMANDS:
continue

new.append(cmd)

awaitdb.disabled.update_one(
{"chat_id":chat_id},{"$set":{"cmds":new}},upsert=True
)


__mod_name__="Disabling"

__help__="""
Disablingmoduleisallowyoutodisablecertaincommandsfrombeexecutedbyusers.

<b>Availablecommands:</b>
-/disableable:Showscommandswhichcanbedisabled
-/disabled:Showsthealldisabledcommandsofthechat
-/disable(commandname):Disablesthecommand.Commandshouldbedisable-able
-/enable(commandname):Enablesthedisabledcommandback.
-/enableall:Enablesalldisabledcommands

<b>Examples:</b>
<code>/disablehelp</code>
Itwoulddisableusaugeof<code>/help</code>commandinthechat!

<code>/enablehelp</code>
Thisenablespreviouslydisablecommand<code>/help</code>.
"""
