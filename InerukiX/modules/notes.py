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

importXdifflib
importXre
fromXcontextlibXimportXsuppress
fromXdatetimeXimportXdatetime

fromXaiogram.dispatcher.filters.builtinXimportXCommandStart
fromXaiogram.types.inline_keyboardXimportXInlineKeyboardButton,XInlineKeyboardMarkup
fromXaiogram.utils.deep_linkingXimportXget_start_link
fromXaiogram.utils.exceptionsXimportX(
XXXXBadRequest,
XXXXMessageCantBeDeleted,
XXXXMessageNotModified,
)
fromXbabel.datesXimportXformat_datetime
fromXpymongoXimportXReplaceOne
fromXtelethon.errors.rpcerrorlistXimportXMessageDeleteForbiddenError

fromXInerukiXXimportXbot
fromXInerukiX.decoratorXimportXregister
fromXInerukiX.services.mongoXimportXdb
fromXInerukiX.services.redisXimportXredis
fromXInerukiX.services.telethonXimportXtbot

fromX.utils.connectionsXimportXchat_connection,Xset_connected_command
fromX.utils.disableXimportXdisableable_dec
fromX.utils.languageXimportXget_string,Xget_strings_dec
fromX.utils.messageXimportXget_arg,Xneed_args_dec
fromX.utils.notesXimportX(
XXXXALLOWED_COLUMNS,
XXXXBUTTONS,
XXXXget_parsed_note_list,
XXXXsend_note,
XXXXt_unparse_note_item,
)
fromX.utils.user_detailsXimportXget_user_link

RESTRICTED_SYMBOLS_IN_NOTENAMESX=X[
XXXX":",
XXXX"**",
XXXX"__",
XXXX"`",
XXXX"#",
XXXX'"',
XXXX"[",
XXXX"]",
XXXX"'",
XXXX"$",
XXXX"||",
]


asyncXdefXget_similar_note(chat_id,Xnote_name):
XXXXall_notesX=X[]
XXXXasyncXforXnoteXinXdb.notes.find({"chat_id":Xchat_id}):
XXXXXXXXall_notes.extend(note["names"])

XXXXifXlen(all_notes)X>X0:
XXXXXXXXcheckX=Xdifflib.get_close_matches(note_name,Xall_notes)
XXXXXXXXifXlen(check)X>X0:
XXXXXXXXXXXXreturnXcheck[0]

XXXXreturnXNone


defXclean_notes(func):
XXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXeventX=Xargs[0]

XXXXXXXXmessageX=XawaitXfunc(*args,X**kwargs)
XXXXXXXXifXnotXmessage:
XXXXXXXXXXXXreturn

XXXXXXXXifXevent.chat.typeX==X"private":
XXXXXXXXXXXXreturn

XXXXXXXXchat_idX=Xevent.chat.id

XXXXXXXXdataX=XawaitXdb.clean_notes.find_one({"chat_id":Xchat_id})
XXXXXXXXifXnotXdata:
XXXXXXXXXXXXreturn

XXXXXXXXifXdata["enabled"]XisXnotXTrue:
XXXXXXXXXXXXreturn

XXXXXXXXifX"msgs"XinXdata:
XXXXXXXXXXXXwithXsuppress(MessageDeleteForbiddenError):
XXXXXXXXXXXXXXXXawaitXtbot.delete_messages(chat_id,Xdata["msgs"])

XXXXXXXXmsgsX=X[]
XXXXXXXXifXhasattr(message,X"message_id"):
XXXXXXXXXXXXmsgs.append(message.message_id)
XXXXXXXXelse:
XXXXXXXXXXXXmsgs.append(message.id)

XXXXXXXXmsgs.append(event.message_id)

XXXXXXXXawaitXdb.clean_notes.update_one({"chat_id":Xchat_id},X{"$set":X{"msgs":Xmsgs}})

XXXXreturnXwrapped_1


@register(cmds="save",Xuser_admin=True,Xuser_can_change_info=True)
@need_args_dec()
@chat_connection(admin=True)
@get_strings_dec("notes")
asyncXdefXsave_note(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXargX=Xget_arg(message).lower()
XXXXifXarg[0]X==X"#":
XXXXXXXXargX=Xarg[1:]

XXXXsymX=XNone
XXXXifXany((symX:=Xs)XinXargXforXsXinXRESTRICTED_SYMBOLS_IN_NOTENAMES):
XXXXXXXXawaitXmessage.reply(strings["notename_cant_contain"].format(symbol=sym))
XXXXXXXXreturn

XXXXnote_namesX=Xarg.split("|")

XXXXnoteX=XawaitXget_parsed_note_list(message)

XXXXnote["names"]X=Xnote_names
XXXXnote["chat_id"]X=Xchat_id

XXXXifX"text"XnotXinXnoteXandX"file"XnotXinXnote:
XXXXXXXXawaitXmessage.reply(strings["blank_note"])
XXXXXXXXreturn

XXXXifXold_noteX:=XawaitXdb.notes.find_one(
XXXXXXXX{"chat_id":Xchat_id,X"names":X{"$in":Xnote_names}}
XXXX):
XXXXXXXXtextX=Xstrings["note_updated"]
XXXXXXXXifX"created_date"XinXold_note:
XXXXXXXXXXXXnote["created_date"]X=Xold_note["created_date"]
XXXXXXXXXXXXnote["created_user"]X=Xold_note["created_user"]
XXXXXXXXnote["edited_date"]X=Xdatetime.now()
XXXXXXXXnote["edited_user"]X=Xmessage.from_user.id
XXXXelse:
XXXXXXXXtextX=Xstrings["note_saved"]
XXXXXXXXnote["created_date"]X=Xdatetime.now()
XXXXXXXXnote["created_user"]X=Xmessage.from_user.id

XXXXawaitXdb.notes.replace_one(
XXXXXXXX{"_id":Xold_note["_id"]}XifXold_noteXelseXnote,Xnote,Xupsert=True
XXXX)

XXXXtextX+=Xstrings["you_can_get_note"]
XXXXtextX=Xtext.format(note_name=note_names[0],Xchat_title=chat["chat_title"])
XXXXifXlen(note_names)X>X1:
XXXXXXXXtextX+=Xstrings["note_aliases"]
XXXXXXXXforXnotenameXinXnote_names:
XXXXXXXXXXXXtextX+=Xf"X<code>#{notename}</code>"

XXXXawaitXmessage.reply(text)


@get_strings_dec("notes")
asyncXdefXget_note(
XXXXmessage,
XXXXstrings,
XXXXnote_name=None,
XXXXdb_item=None,
XXXXchat_id=None,
XXXXsend_id=None,
XXXXrpl_id=None,
XXXXnoformat=False,
XXXXevent=None,
XXXXuser=None,
):
XXXXifXnotXchat_id:
XXXXXXXXchat_idX=Xmessage.chat.id

XXXXifXnotXsend_id:
XXXXXXXXsend_idX=Xmessage.chat.id

XXXXifXrpl_idXisXFalse:
XXXXXXXXrpl_idX=XNone
XXXXelifXnotXrpl_id:
XXXXXXXXrpl_idX=Xmessage.message_id

XXXXifXnotXdb_itemXandXnotX(
XXXXXXXXdb_itemX:=XawaitXdb.notes.find_one(
XXXXXXXXXXXX{"chat_id":Xchat_id,X"names":X{"$in":X[note_name]}}
XXXXXXXX)
XXXX):
XXXXXXXXawaitXbot.send_message(chat_id,Xstrings["no_note"],Xreply_to_message_id=rpl_id)
XXXXXXXXreturn

XXXXtext,XkwargsX=XawaitXt_unparse_note_item(
XXXXXXXXmessage,Xdb_item,Xchat_id,Xnoformat=noformat,Xevent=event,Xuser=user
XXXX)
XXXXkwargs["reply_to"]X=Xrpl_id

XXXXreturnXawaitXsend_note(send_id,Xtext,X**kwargs)


@register(cmds="get")
@disableable_dec("get")
@need_args_dec()
@chat_connection(command="get")
@get_strings_dec("notes")
@clean_notes
asyncXdefXget_note_cmd(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXchat_nameX=Xchat["chat_title"]

XXXXnote_nameX=Xget_arg(message).lower()
XXXXifXnote_name[0]X==X"#":
XXXXXXXXnote_nameX=Xnote_name[1:]

XXXXifX"reply_to_message"XinXmessage:
XXXXXXXXrpl_idX=Xmessage.reply_to_message.message_id
XXXXXXXXuserX=Xmessage.reply_to_message.from_user
XXXXelse:
XXXXXXXXrpl_idX=Xmessage.message_id
XXXXXXXXuserX=Xmessage.from_user

XXXXifXnotX(
XXXXXXXXnoteX:=XawaitXdb.notes.find_one(
XXXXXXXXXXXX{"chat_id":Xint(chat_id),X"names":X{"$in":X[note_name]}}
XXXXXXXX)
XXXX):
XXXXXXXXtextX=Xstrings["cant_find_note"].format(chat_name=chat_name)
XXXXXXXXifXalleged_note_nameX:=XawaitXget_similar_note(chat_id,Xnote_name):
XXXXXXXXXXXXtextX+=Xstrings["u_mean"].format(note_name=alleged_note_name)
XXXXXXXXawaitXmessage.reply(text)
XXXXXXXXreturn

XXXXnoformatX=XFalse
XXXXifXlen(argsX:=Xmessage.text.split("X"))X>X2:
XXXXXXXXarg2X=Xargs[2].lower()
XXXXXXXXnoformatX=Xarg2XinX("noformat",X"raw")

XXXXreturnXawaitXget_note(
XXXXXXXXmessage,Xdb_item=note,Xrpl_id=rpl_id,Xnoformat=noformat,Xuser=user
XXXX)


@register(regexp=r"^#([\w-]+)",Xallow_kwargs=True)
@disableable_dec("get")
@chat_connection(command="get")
@clean_notes
asyncXdefXget_note_hashtag(message,Xchat,Xregexp=None,X**kwargs):
XXXXchat_idX=Xchat["chat_id"]

XXXXnote_nameX=Xregexp.group(1).lower()
XXXXifXnotX(
XXXXXXXXnoteX:=XawaitXdb.notes.find_one(
XXXXXXXXXXXX{"chat_id":Xint(chat_id),X"names":X{"$in":X[note_name]}}
XXXXXXXX)
XXXX):
XXXXXXXXreturn

XXXXifX"reply_to_message"XinXmessage:
XXXXXXXXrpl_idX=Xmessage.reply_to_message.message_id
XXXXXXXXuserX=Xmessage.reply_to_message.from_user
XXXXelse:
XXXXXXXXrpl_idX=Xmessage.message_id
XXXXXXXXuserX=Xmessage.from_user

XXXXreturnXawaitXget_note(message,Xdb_item=note,Xrpl_id=rpl_id,Xuser=user)


@register(cmds=["notes",X"saved"])
@disableable_dec("notes")
@chat_connection(command="notes")
@get_strings_dec("notes")
@clean_notes
asyncXdefXget_notes_list_cmd(message,Xchat,Xstrings):
XXXXifX(
XXXXXXXXawaitXdb.privatenotes.find_one({"chat_id":Xchat["chat_id"]})
XXXXXXXXandXmessage.chat.idX==Xchat["chat_id"]
XXXX):XX#XWorkaroundXtoXavoidXsendingXPNXtoXconnectedXPM
XXXXXXXXtextX=Xstrings["notes_in_private"]
XXXXXXXXifXnotX(keywordX:=Xmessage.get_args()):
XXXXXXXXXXXXkeywordX=XNone
XXXXXXXXbuttonX=XInlineKeyboardMarkup().add(
XXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXtext="ClickXhere",
XXXXXXXXXXXXXXXXurl=awaitXget_start_link(f"notes_{chat['chat_id']}_{keyword}"),
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXreturnXawaitXmessage.reply(
XXXXXXXXXXXXtext,Xreply_markup=button,Xdisable_web_page_preview=True
XXXXXXXX)
XXXXelse:
XXXXXXXXreturnXawaitXget_notes_list(message,Xchat=chat)


@get_strings_dec("notes")
asyncXdefXget_notes_list(message,Xstrings,Xchat,Xkeyword=None,Xpm=False):
XXXXtextX=Xstrings["notelist_header"].format(chat_name=chat["chat_title"])

XXXXnotesX=X(
XXXXXXXXawaitXdb.notes.find({"chat_id":Xchat["chat_id"]})
XXXXXXXX.sort("names",X1)
XXXXXXXX.to_list(length=300)
XXXX)
XXXXifXnotXnotes:
XXXXXXXXreturnXawaitXmessage.reply(
XXXXXXXXXXXXstrings["notelist_no_notes"].format(chat_title=chat["chat_title"])
XXXXXXXX)

XXXXasyncXdefXsearch_notes(request):
XXXXXXXXnonlocalXnotes,Xtext,Xnote,Xnote_name
XXXXXXXXtextX+=X"\n"X+Xstrings["notelist_search"].format(request=request)
XXXXXXXXall_notesX=Xnotes
XXXXXXXXnotesX=X[]
XXXXXXXXforXnoteXinXall_notes:
XXXXXXXXXXXXforXnote_nameXinXnote["names"]:
XXXXXXXXXXXXXXXXifXre.search(request,Xnote_name):
XXXXXXXXXXXXXXXXXXXXnotes.append(note)
XXXXXXXXifXlen(notes)X<=X0:
XXXXXXXXXXXXreturnXawaitXmessage.reply(strings["no_notes_pattern"]X%Xrequest)

XXXX#XSearch
XXXXifXkeyword:
XXXXXXXXawaitXsearch_notes(keyword)
XXXXifXlen(keywordX:=Xmessage.get_args())X>X0XandXpmXisXFalse:
XXXXXXXXawaitXsearch_notes(keyword)

XXXXifXlen(notes)X>X0:
XXXXXXXXforXnoteXinXnotes:
XXXXXXXXXXXXtextX+=X"\n-"
XXXXXXXXXXXXforXnote_nameXinXnote["names"]:
XXXXXXXXXXXXXXXXtextX+=Xf"X<code>#{note_name}</code>"
XXXXXXXXtextX+=Xstrings["you_can_get_note"]

XXXXXXXXtry:
XXXXXXXXXXXXreturnXawaitXmessage.reply(text)
XXXXXXXXexceptXBadRequest:
XXXXXXXXXXXXawaitXmessage.answer(text)


@register(cmds="search")
@chat_connection()
@get_strings_dec("notes")
@clean_notes
asyncXdefXsearch_in_note(message,Xchat,Xstrings):
XXXXrequestX=Xmessage.get_args()
XXXXtextX=Xstrings["search_header"].format(
XXXXXXXXchat_name=chat["chat_title"],Xrequest=request
XXXX)

XXXXnotesX=Xdb.notes.find(
XXXXXXXX{"chat_id":Xchat["chat_id"],X"text":X{"$regex":Xrequest,X"$options":X"i"}}
XXXX).sort("names",X1)
XXXXforXnoteXinX(checkX:=XawaitXnotes.to_list(length=300)):
XXXXXXXXtextX+=X"\n-"
XXXXXXXXforXnote_nameXinXnote["names"]:
XXXXXXXXXXXXtextX+=Xf"X<code>#{note_name}</code>"
XXXXtextX+=Xstrings["you_can_get_note"]
XXXXifXnotXcheck:
XXXXXXXXreturnXawaitXmessage.reply(
XXXXXXXXXXXXstrings["notelist_no_notes"].format(chat_title=chat["chat_title"])
XXXXXXXX)
XXXXreturnXawaitXmessage.reply(text)


@register(cmds=["clear",X"delnote"],Xuser_admin=True,Xuser_can_change_info=True)
@chat_connection(admin=True)
@need_args_dec()
@get_strings_dec("notes")
asyncXdefXclear_note(message,Xchat,Xstrings):
XXXXnote_namesX=Xget_arg(message).lower().split("|")

XXXXremovedX=X""
XXXXnot_removedX=X""
XXXXforXnote_nameXinXnote_names:
XXXXXXXXifXnote_name[0]X==X"#":
XXXXXXXXXXXXnote_nameX=Xnote_name[1:]

XXXXXXXXifXnotX(
XXXXXXXXXXXXnoteX:=XawaitXdb.notes.find_one(
XXXXXXXXXXXXXXXX{"chat_id":Xchat["chat_id"],X"names":X{"$in":X[note_name]}}
XXXXXXXXXXXX)
XXXXXXXX):
XXXXXXXXXXXXifXlen(note_names)X<=X1:
XXXXXXXXXXXXXXXXtextX=Xstrings["cant_find_note"].format(chat_name=chat["chat_title"])
XXXXXXXXXXXXXXXXifXalleged_note_nameX:=XawaitXget_similar_note(
XXXXXXXXXXXXXXXXXXXXchat["chat_id"],Xnote_name
XXXXXXXXXXXXXXXX):
XXXXXXXXXXXXXXXXXXXXtextX+=Xstrings["u_mean"].format(note_name=alleged_note_name)
XXXXXXXXXXXXXXXXawaitXmessage.reply(text)
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXnot_removedX+=X"X#"X+Xnote_name
XXXXXXXXXXXXXXXXcontinue

XXXXXXXXawaitXdb.notes.delete_one({"_id":Xnote["_id"]})
XXXXXXXXremovedX+=X"X#"X+Xnote_name

XXXXifXlen(note_names)X>X1:
XXXXXXXXtextX=Xstrings["note_removed_multiple"].format(
XXXXXXXXXXXXchat_name=chat["chat_title"],Xremoved=removed
XXXXXXXX)
XXXXXXXXifXnot_removed:
XXXXXXXXXXXXtextX+=Xstrings["not_removed_multiple"].format(not_removed=not_removed)
XXXXXXXXawaitXmessage.reply(text)
XXXXelse:
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["note_removed"].format(
XXXXXXXXXXXXXXXXnote_name=note_name,Xchat_name=chat["chat_title"]
XXXXXXXXXXXX)
XXXXXXXX)


@register(cmds="clearall",Xuser_admin=True,Xuser_can_change_info=True)
@chat_connection(admin=True)
@get_strings_dec("notes")
asyncXdefXclear_all_notes(message,Xchat,Xstrings):
XXXX#XEnsureXnotesXcount
XXXXifXnotXawaitXdb.notes.find_one({"chat_id":Xchat["chat_id"]}):
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["notelist_no_notes"].format(chat_title=chat["chat_title"])
XXXXXXXX)
XXXXXXXXreturn

XXXXtextX=Xstrings["clear_all_text"].format(chat_name=chat["chat_title"])
XXXXbuttonsX=XInlineKeyboardMarkup()
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXstrings["clearall_btn_yes"],Xcallback_data="clean_all_notes_cb"
XXXXXXXX)
XXXX)
XXXXbuttons.add(
XXXXXXXXInlineKeyboardButton(strings["clearall_btn_no"],Xcallback_data="cancel")
XXXX)
XXXXawaitXmessage.reply(text,Xreply_markup=buttons)


@register(regexp="clean_all_notes_cb",Xf="cb",Xis_admin=True,Xuser_can_change_info=True)
@chat_connection(admin=True)
@get_strings_dec("notes")
asyncXdefXclear_all_notes_cb(event,Xchat,Xstrings):
XXXXnumX=X(awaitXdb.notes.delete_many({"chat_id":Xchat["chat_id"]})).deleted_count

XXXXtextX=Xstrings["clearall_done"].format(num=num,Xchat_name=chat["chat_title"])
XXXXawaitXevent.message.edit_text(text)


@register(cmds="noteinfo",Xuser_admin=True)
@chat_connection()
@need_args_dec()
@get_strings_dec("notes")
@clean_notes
asyncXdefXnote_info(message,Xchat,Xstrings):
XXXXnote_nameX=Xget_arg(message).lower()
XXXXifXnote_name[0]X==X"#":
XXXXXXXXnote_nameX=Xnote_name[1:]

XXXXifXnotX(
XXXXXXXXnoteX:=XawaitXdb.notes.find_one(
XXXXXXXXXXXX{"chat_id":Xchat["chat_id"],X"names":X{"$in":X[note_name]}}
XXXXXXXX)
XXXX):
XXXXXXXXtextX=Xstrings["cant_find_note"].format(chat_name=chat["chat_title"])
XXXXXXXXifXalleged_note_nameX:=XawaitXget_similar_note(chat["chat_id"],Xnote_name):
XXXXXXXXXXXXtextX+=Xstrings["u_mean"].format(note_name=alleged_note_name)
XXXXXXXXreturnXawaitXmessage.reply(text)

XXXXtextX=Xstrings["note_info_title"]

XXXXnote_namesX=X""
XXXXforXnote_nameXinXnote["names"]:
XXXXXXXXnote_namesX+=Xf"X<code>#{note_name}</code>"

XXXXtextX+=Xstrings["note_info_note"]X%Xnote_names
XXXXtextX+=Xstrings["note_info_content"]X%X(
XXXXXXXX"text"XifX"file"XnotXinXnoteXelseXnote["file"]["type"]
XXXX)

XXXXifX"parse_mode"XnotXinXnoteXorXnote["parse_mode"]X==X"md":
XXXXXXXXparse_modeX=X"Markdown"
XXXXelifXnote["parse_mode"]X==X"html":
XXXXXXXXparse_modeX=X"HTML"
XXXXelifXnote["parse_mode"]X==X"none":
XXXXXXXXparse_modeX=X"None"
XXXXelse:
XXXXXXXXraiseXTypeError()

XXXXtextX+=Xstrings["note_info_parsing"]X%Xparse_mode

XXXXifX"created_date"XinXnote:
XXXXXXXXtextX+=Xstrings["note_info_created"].format(
XXXXXXXXXXXXdate=format_datetime(
XXXXXXXXXXXXXXXXnote["created_date"],Xlocale=strings["language_info"]["babel"]
XXXXXXXXXXXX),
XXXXXXXXXXXXuser=awaitXget_user_link(note["created_user"]),
XXXXXXXX)

XXXXifX"edited_date"XinXnote:
XXXXXXXXtextX+=Xstrings["note_info_updated"].format(
XXXXXXXXXXXXdate=format_datetime(
XXXXXXXXXXXXXXXXnote["edited_date"],Xlocale=strings["language_info"]["babel"]
XXXXXXXXXXXX),
XXXXXXXXXXXXuser=awaitXget_user_link(note["edited_user"]),
XXXXXXXX)

XXXXreturnXawaitXmessage.reply(text)


BUTTONS.update({"note":X"btnnotesm",X"#":X"btnnotesm"})


@register(regexp=r"btnnotesm_(\w+)_(.*)",Xf="cb",Xallow_kwargs=True)
@get_strings_dec("notes")
asyncXdefXnote_btn(event,Xstrings,Xregexp=None,X**kwargs):
XXXXchat_idX=Xint(regexp.group(2))
XXXXuser_idX=Xevent.from_user.id
XXXXnote_nameX=Xregexp.group(1).lower()

XXXXifXnotX(
XXXXXXXXnoteX:=XawaitXdb.notes.find_one(
XXXXXXXXXXXX{"chat_id":Xchat_id,X"names":X{"$in":X[note_name]}}
XXXXXXXX)
XXXX):
XXXXXXXXawaitXevent.answer(strings["no_note"])
XXXXXXXXreturn

XXXXwithXsuppress(MessageCantBeDeleted):
XXXXXXXXawaitXevent.message.delete()
XXXXawaitXget_note(
XXXXXXXXevent.message,
XXXXXXXXdb_item=note,
XXXXXXXXchat_id=chat_id,
XXXXXXXXsend_id=user_id,
XXXXXXXXrpl_id=None,
XXXXXXXXevent=event,
XXXX)


@register(CommandStart(re.compile(r"btnnotesm")),Xallow_kwargs=True)
@get_strings_dec("notes")
asyncXdefXnote_start(message,Xstrings,Xregexp=None,X**kwargs):
XXXX#XDon'tXevenXaskXwhatXitXmeans,XmostlyXitXworkaroundXtoXsupportXnoteXnamesXwithX_
XXXXargsX=Xre.search(r"^([a-zA-Z0-9]+)_(.*?)(-\d+)$",Xmessage.get_args())
XXXXchat_idX=Xint(args.group(3))
XXXXuser_idX=Xmessage.from_user.id
XXXXnote_nameX=Xargs.group(2).strip("_")

XXXXifXnotX(
XXXXXXXXnoteX:=XawaitXdb.notes.find_one(
XXXXXXXXXXXX{"chat_id":Xchat_id,X"names":X{"$in":X[note_name]}}
XXXXXXXX)
XXXX):
XXXXXXXXawaitXmessage.reply(strings["no_note"])
XXXXXXXXreturn

XXXXawaitXget_note(message,Xdb_item=note,Xchat_id=chat_id,Xsend_id=user_id,Xrpl_id=None)


@register(cmds="start",Xonly_pm=True)
@get_strings_dec("connections")
asyncXdefXbtn_note_start_state(message,Xstrings):
XXXXkeyX=X"btn_note_start_state:"X+Xstr(message.from_user.id)
XXXXifXnotX(cachedX:=Xredis.hgetall(key)):
XXXXXXXXreturn

XXXXchat_idX=Xint(cached["chat_id"])
XXXXuser_idX=Xmessage.from_user.id
XXXXnote_nameX=Xcached["notename"]

XXXXnoteX=XawaitXdb.notes.find_one({"chat_id":Xchat_id,X"names":X{"$in":X[note_name]}})
XXXXawaitXget_note(message,Xdb_item=note,Xchat_id=chat_id,Xsend_id=user_id,Xrpl_id=None)

XXXXredis.delete(key)


@register(cmds="privatenotes",Xis_admin=True,Xuser_can_change_info=True)
@chat_connection(admin=True)
@get_strings_dec("notes")
asyncXdefXprivate_notes_cmd(message,Xchat,Xstrings):
XXXXchat_idX=Xchat["chat_id"]
XXXXchat_nameX=Xchat["chat_title"]
XXXXtextX=Xstr

XXXXtry:
XXXXXXXX(textX:=X"".join(message.text.split()[1]).lower())
XXXXexceptXIndexError:
XXXXXXXXpass

XXXXenablingX=X["true",X"enable",X"on"]
XXXXdisablingX=X["false",X"disable",X"off"]
XXXXifXdatabaseX:=XawaitXdb.privatenotes.find_one({"chat_id":Xchat_id}):
XXXXXXXXifXtextXinXenabling:
XXXXXXXXXXXXawaitXmessage.reply(strings["already_enabled"]X%Xchat_name)
XXXXXXXXXXXXreturn
XXXXifXtextXinXenabling:
XXXXXXXXawaitXdb.privatenotes.insert_one({"chat_id":Xchat_id})
XXXXXXXXawaitXmessage.reply(strings["enabled_successfully"]X%Xchat_name)
XXXXelifXtextXinXdisabling:
XXXXXXXXifXnotXdatabase:
XXXXXXXXXXXXawaitXmessage.reply(strings["not_enabled"])
XXXXXXXXXXXXreturn
XXXXXXXXawaitXdb.privatenotes.delete_one({"_id":Xdatabase["_id"]})
XXXXXXXXawaitXmessage.reply(strings["disabled_successfully"]X%Xchat_name)
XXXXelse:
XXXXXXXX#XAssumeXadminXaskedXforXcurrentXstate
XXXXXXXXifXdatabase:
XXXXXXXXXXXXstateX=Xstrings["enabled"]
XXXXXXXXelse:
XXXXXXXXXXXXstateX=Xstrings["disabled"]
XXXXXXXXawaitXmessage.reply(
XXXXXXXXXXXXstrings["current_state_info"].format(state=state,Xchat=chat_name)
XXXXXXXX)


@register(cmds="cleannotes",Xis_admin=True,Xuser_can_change_info=True)
@chat_connection(admin=True)
@get_strings_dec("notes")
asyncXdefXclean_notes(message,Xchat,Xstrings):
XXXXdisableX=X["no",X"off",X"0",X"false",X"disable"]
XXXXenableX=X["yes",X"on",X"1",X"true",X"enable"]

XXXXchat_idX=Xchat["chat_id"]

XXXXargX=Xget_arg(message)
XXXXifXargXandXarg.lower()XinXenable:
XXXXXXXXawaitXdb.clean_notes.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},X{"$set":X{"enabled":XTrue}},Xupsert=True
XXXXXXXX)
XXXXXXXXtextX=Xstrings["clean_notes_enable"].format(chat_name=chat["chat_title"])
XXXXelifXargXandXarg.lower()XinXdisable:
XXXXXXXXawaitXdb.clean_notes.update_one(
XXXXXXXXXXXX{"chat_id":Xchat_id},X{"$set":X{"enabled":XFalse}},Xupsert=True
XXXXXXXX)
XXXXXXXXtextX=Xstrings["clean_notes_disable"].format(chat_name=chat["chat_title"])
XXXXelse:
XXXXXXXXdataX=XawaitXdb.clean_notes.find_one({"chat_id":Xchat_id})
XXXXXXXXifXdataXandXdata["enabled"]XisXTrue:
XXXXXXXXXXXXtextX=Xstrings["clean_notes_enabled"].format(chat_name=chat["chat_title"])
XXXXXXXXelse:
XXXXXXXXXXXXtextX=Xstrings["clean_notes_disabled"].format(chat_name=chat["chat_title"])

XXXXawaitXmessage.reply(text)


@register(CommandStart(re.compile("notes")))
@get_strings_dec("notes")
asyncXdefXprivate_notes_func(message,Xstrings):
XXXXargsX=Xmessage.get_args().split("_")
XXXXchat_idX=Xargs[1]
XXXXkeywordX=Xargs[2]XifXargs[2]X!=X"None"XelseXNone
XXXXawaitXset_connected_command(message.from_user.id,Xint(chat_id),X["get",X"notes"])
XXXXchatX=XawaitXdb.chat_list.find_one({"chat_id":Xint(chat_id)})
XXXXawaitXmessage.answer(strings["privatenotes_notif"].format(chat=chat["chat_title"]))
XXXXawaitXget_notes_list(message,Xchat=chat,Xkeyword=keyword,Xpm=True)


asyncXdefX__stats__():
XXXXtextX=X"*X<code>{}</code>XtotalXnotes\n".format(awaitXdb.notes.count_documents({}))
XXXXreturnXtext


asyncXdefX__export__(chat_id):
XXXXdataX=X[]
XXXXnotesX=X(
XXXXXXXXawaitXdb.notes.find({"chat_id":Xchat_id}).sort("names",X1).to_list(length=300)
XXXX)
XXXXforXnoteXinXnotes:
XXXXXXXXdelXnote["_id"]
XXXXXXXXdelXnote["chat_id"]
XXXXXXXXnote["created_date"]X=Xstr(note["created_date"])
XXXXXXXXifX"edited_date"XinXnote:
XXXXXXXXXXXXnote["edited_date"]X=Xstr(note["edited_date"])
XXXXXXXXdata.append(note)

XXXXreturnX{"notes":Xdata}


ALLOWED_COLUMNS_NOTESX=XALLOWED_COLUMNSX+X[
XXXX"names",
XXXX"created_date",
XXXX"created_user",
XXXX"edited_date",
XXXX"edited_user",
]


asyncXdefX__import__(chat_id,Xdata):
XXXXifXnotXdata:
XXXXXXXXreturn

XXXXnewX=X[]
XXXXforXnoteXinXdata:

XXXXXXXX#XFileXverX1XtoX2
XXXXXXXXifX"name"XinXnote:
XXXXXXXXXXXXnote["names"]X=X[note["name"]]
XXXXXXXXXXXXdelXnote["name"]

XXXXXXXXforXitemXinX[iXforXiXinXnoteXifXiXnotXinXALLOWED_COLUMNS_NOTES]:
XXXXXXXXXXXXdelXnote[item]

XXXXXXXXnote["chat_id"]X=Xchat_id
XXXXXXXXnote["created_date"]X=Xdatetime.fromisoformat(note["created_date"])
XXXXXXXXifX"edited_date"XinXnote:
XXXXXXXXXXXXnote["edited_date"]X=Xdatetime.fromisoformat(note["edited_date"])
XXXXXXXXnew.append(
XXXXXXXXXXXXReplaceOne(
XXXXXXXXXXXXXXXX{"chat_id":Xnote["chat_id"],X"names":X{"$in":X[note["names"][0]]}},
XXXXXXXXXXXXXXXXnote,
XXXXXXXXXXXXXXXXupsert=True,
XXXXXXXXXXXX)
XXXXXXXX)

XXXXawaitXdb.notes.bulk_write(new)


asyncXdefXfilter_handle(message,Xchat,Xdata):
XXXXchat_idX=Xchat["chat_id"]
XXXXread_chat_idX=Xmessage.chat.id
XXXXnote_nameX=Xdata["note_name"]
XXXXnoteX=XawaitXdb.notes.find_one({"chat_id":Xchat_id,X"names":X{"$in":X[note_name]}})
XXXXawaitXget_note(
XXXXXXXXmessage,Xdb_item=note,Xchat_id=chat_id,Xsend_id=read_chat_id,Xrpl_id=None
XXXX)


asyncXdefXsetup_start(message):
XXXXtextX=XawaitXget_string(message.chat.id,X"notes",X"filters_setup_start")
XXXXwithXsuppress(MessageNotModified):
XXXXXXXXawaitXmessage.edit_text(text)


asyncXdefXsetup_finish(message,Xdata):
XXXXnote_nameX=Xmessage.text.split("X",X1)[0].split()[0]

XXXXifXnotX(awaitXdb.notes.find_one({"chat_id":Xdata["chat_id"],X"names":Xnote_name})):
XXXXXXXXawaitXmessage.reply("noXsuchXnote!")
XXXXXXXXreturn

XXXXreturnX{"note_name":Xnote_name}


__filters__X=X{
XXXX"get_note":X{
XXXXXXXX"title":X{"module":X"notes",X"string":X"filters_title"},
XXXXXXXX"handle":Xfilter_handle,
XXXXXXXX"setup":X{"start":Xsetup_start,X"finish":Xsetup_finish},
XXXXXXXX"del_btn_name":XlambdaXmsg,Xdata:Xf"GetXnote:X{data['note_name']}",
XXXX}
}


__mod_name__X=X"Notes"

__help__X=X"""
SometimesXyouXneedXtoXsaveXsomeXdata,XlikeXtextXorXpictures.XWithXnotes,XyouXcanXsaveXanyXtypesXofXTelegram'sXdataXinXyourXchats.
AlsoXnotesXperfectlyXworkingXinXPMXwithXIneruki.

<b>AvailableXcommands:</b>
-X/saveX(name)X(data):XSavesXtheXnote.
-X#(name)XorX/getX(name):XGetXtheXnoteXregisteredXtoXthatXword.
-X/clearX(name):XdeletesXtheXnote.
-X/notesXorX/saved:XListsXallXnotes.
-X/noteinfoX(name):XShowsXdetailedXinfoXaboutXtheXnote.
-X/searchX(searchXpattern):XSearchXtextXinXnotes
-X/clearall:XClearsXallXnotes

<b>OnlyXinXgroups:</b>
-X/privatenotesX(on/off):XRedirectXuserXinXPMXtoXseeXnotes
-X/cleannotesX(on/off):XWillXcleanXoldXnotesXmessages

<b>Examples:</b>
AnXexampleXofXhowXtoXsaveXaXnoteXwouldXbeXvia:
<code>/saveXdataXThisXisXexampleXnote!</code>
Now,XanyoneXusingX<code>/getXdata</code>,XorX<code>#data</code>XwillXbeXrepliedXtoXwithXThisXisXexampleXnote!.

<b>SavingXpicturesXandXotherXnon-textXdata:</b>
IfXyouXwantXtoXsaveXanXimage,Xgif,XorXsticker,XorXanyXotherXdata,XdoXtheXfollowing:
<code>/saveXword</code>XwhileXreplyingXtoXaXstickerXorXwhateverXdataXyou'dXlike.XNow,XtheXnoteXatX<code>#word</code>XcontainsXaXstickerXwhichXwillXbeXsentXasXaXreply.

<b>RemovingXmanyXnotesXperXoneXrequest:</b>
ToXremoveXmanyXnotesXyouXcanXuseXtheX/clearXcommand,XjustXplaceXallXnoteXnamesXwhichXyouXwantXtoXremoveXasXargumentXofXtheXcommand,XuseX|XasXseprator,XforXexample:
<code>/clearXnote1|note2|note3</code>

<b>NotesXaliases:</b>
YouXcanXsaveXnoteXwithXmanyXnames,Xexample:
<code>/saveXname1|name2|name3</code>
ThatXwillXsaveXaXnoteXwithX3XdifferentXnames,XbyXanyXyouXcanX/getXnote,XthatXcanXbeXusefulXifXusersXinXyourXchatXtryingXtoXgetXnotesXwhichXexitsXbyXotherXnames.

<b>NotesXbuttonsXandXvariables:</b>
NotesXsupportXinlineXbuttons,XsendX/buttonshelpXtoXgetXstartedXwithXusingXit.
VariablesXareXspecialXwordsXwhichXwillXbeXreplacedXbyXactualXinfoXlikeXifXyouXaddX<code>{id}</code>XinXyourXnoteXitXwillXbeXreplacedXbyXuserXIDXwhichXaskedXnote.XSendX/variableshelpXtoXgetXstartedXwithXusingXit.

<b>NotesXformattingXandXsettings:</b>
EveryXnoteXcanXcontainXspecialXsettings,XforXexampleXyouXcanXchangeXformattingXmethodXtoXHTMLXbyX<code>%PARSEMODE_HTML</code>XandXfullyXdisableXitXbyX<code>%PARSEMODE_NONE</code>X(XByXdefaultXformattingXisXMarkdownXorXtheXsameXformattingXTelegramXsupportsX)

<code>%PARSEMODE_(HTML,XNONE)</code>:XChangeXtheXnoteXformatting
<code>%PREVIEW</code>:XEnablesXtheXlinksXpreviewXinXsavedXnote

<b>SavingXnotesXfromXotherXMarieXstyleXbots:</b>
InerukiXcanXsaveXnotesXfromXotherXbots,XjustXreplyX/saveXonXtheXsavedXmessageXfromXanotherXbot,XsavingXpicturesXandXbuttonsXsupportedXaswell.

<b>RetrievingXnotesXwithoutXtheXformatting:</b>
ToXretrieveXaXnoteXwithoutXtheXformatting,XuseX<code>/getX(name)Xraw</code>XorX<code>/getX(name)Xnoformat</code>
ThisXwillXretrieveXtheXnoteXandXsendXitXwithoutXformattingXit;XgettingXyouXtheXrawXnote,XallowingXyouXtoXmakeXeasyXedits.
"""
