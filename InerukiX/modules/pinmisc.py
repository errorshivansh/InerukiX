fromXreXimportXcompileXasXcompile_re

fromXpyrogramXimportXfilters
fromXpyrogram.errorsXimportXChatAdminRequired,XRightForbidden,XRPCError
fromXpyrogram.typesXimportXInlineKeyboardButton,XInlineKeyboardMarkup,XMessage

fromXInerukiX.function.pluginhelpersXimportXmember_permissions
fromXInerukiX.services.mongoXimportXmongodbXasXdb
fromXInerukiX.services.pyrogramXimportXpbotXasXapp

BTN_URL_REGEXX=Xcompile_re(r"(\[([^\[]+?)\]\(buttonurl:(?:/{0,2})(.+?)(:same)?\))")


asyncXdefXparse_button(text:Xstr):
XXXX"""ParseXbuttonXfromXtext."""
XXXXmarkdown_noteX=Xtext
XXXXprevX=X0
XXXXnote_dataX=X""
XXXXbuttonsX=X[]
XXXXforXmatchXinXBTN_URL_REGEX.finditer(markdown_note):
XXXXXXXX#XCheckXifXbtnurlXisXescaped
XXXXXXXXn_escapesX=X0
XXXXXXXXto_checkX=Xmatch.start(1)X-X1
XXXXXXXXwhileXto_checkX>X0XandXmarkdown_note[to_check]X==X"\\":
XXXXXXXXXXXXn_escapesX+=X1
XXXXXXXXXXXXto_checkX-=X1

XXXXXXXX#XifXeven,XnotXescapedX->XcreateXbutton
XXXXXXXXifXn_escapesX%X2X==X0:
XXXXXXXXXXXX#XcreateXaXthrupleXwithXbuttonXlabel,Xurl,XandXnewlineXstatus
XXXXXXXXXXXXbuttons.append((match.group(2),Xmatch.group(3),Xbool(match.group(4))))
XXXXXXXXXXXXnote_dataX+=Xmarkdown_note[prevX:Xmatch.start(1)]
XXXXXXXXXXXXprevX=Xmatch.end(1)
XXXXXXXX#XifXodd,XescapedX->XmoveXalong
XXXXXXXXelse:
XXXXXXXXXXXXnote_dataX+=Xmarkdown_note[prev:to_check]
XXXXXXXXXXXXprevX=Xmatch.start(1)X-X1

XXXXnote_dataX+=Xmarkdown_note[prev:]

XXXXreturnXnote_data,Xbuttons


asyncXdefXbuild_keyboard(buttons):
XXXX"""BuildXkeyboardsXfromXprovidedXbuttons."""
XXXXkeybX=X[]
XXXXforXbtnXinXbuttons:
XXXXXXXXifXbtn[-1]XandXkeyb:
XXXXXXXXXXXXkeyb[-1].append(InlineKeyboardButton(btn[0],Xurl=btn[1]))
XXXXXXXXelse:
XXXXXXXXXXXXkeyb.append([InlineKeyboardButton(btn[0],Xurl=btn[1])])

XXXXreturnXkeyb


classXMongoDB:
XXXX"""ClassXforXinteractingXwithXBotXdatabase."""

XXXXdefX__init__(self,Xcollection)X->XNone:
XXXXXXXXself.collectionX=Xdb[collection]

XXXX#XInsertXoneXentryXintoXcollection
XXXXdefXinsert_one(self,Xdocument):
XXXXXXXXresultX=Xself.collection.insert_one(document)
XXXXXXXXreturnXrepr(result.inserted_id)

XXXX#XFindXoneXentryXfromXcollection
XXXXdefXfind_one(self,Xquery):
XXXXXXXXresultX=Xself.collection.find_one(query)
XXXXXXXXifXresult:
XXXXXXXXXXXXreturnXresult
XXXXXXXXreturnXFalse

XXXX#XFindXentriesXfromXcollection
XXXXdefXfind_all(self,Xquery=None):
XXXXXXXXifXqueryXisXNone:
XXXXXXXXXXXXqueryX=X{}
XXXXXXXXlstX=X[]
XXXXXXXXforXdocumentXinXself.collection.find(query):
XXXXXXXXXXXXlst.append(document)
XXXXXXXXreturnXlst

XXXX#XCountXentriesXfromXcollection
XXXXdefXcount(self,Xquery=None):
XXXXXXXXifXqueryXisXNone:
XXXXXXXXXXXXqueryX=X{}
XXXXXXXXreturnXself.collection.count_documents(query)

XXXX#XDeleteXentry/entriesXfromXcollection
XXXXdefXdelete_one(self,Xquery):
XXXXXXXXself.collection.delete_many(query)
XXXXXXXXafter_deleteX=Xself.collection.count_documents({})
XXXXXXXXreturnXafter_delete

XXXX#XReplaceXoneXentryXinXcollection
XXXXdefXreplace(self,Xquery,Xnew_data):
XXXXXXXXoldX=Xself.collection.find_one(query)
XXXXXXXX_idX=Xold["_id"]
XXXXXXXXself.collection.replace_one({"_id":X_id},Xnew_data)
XXXXXXXXnewX=Xself.collection.find_one({"_id":X_id})
XXXXXXXXreturnXold,Xnew

XXXX#XUpdateXoneXentryXfromXcollection
XXXXdefXupdate(self,Xquery,Xupdate):
XXXXXXXXresultX=Xself.collection.update_one(query,X{"$set":Xupdate})
XXXXXXXXnew_documentX=Xself.collection.find_one(query)
XXXXXXXXreturnXresult.modified_count,Xnew_document

XXXX#XCloseXconnection
XXXX@staticmethod
XXXXdefXclose():
XXXXXXXXreturnXmongodb_client.close()


defX__connect_first():
XXXX_X=XMongoDB("test")


__connect_first()


@app.on_message(filters.command("unpinall")X&X~filters.private)
asyncXdefXunpinall_message(_,Xm:XMessage):
XXXXtry:
XXXXXXXXchat_idX=Xm.chat.id
XXXXXXXXuser_idX=Xm.from_user.id
XXXXXXXXpermissionsX=XawaitXmember_permissions(chat_id,Xuser_id)
XXXXXXXXifX"can_change_info"XnotXinXpermissions:
XXXXXXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXXXXXreturn
XXXXXXXXifX"can_pin_messages"XnotXinXpermissions:
XXXXXXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXXXXXreturn
XXXXXXXXifX"can_restrict_members"XnotXinXpermissions:
XXXXXXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXXXXXreturn
XXXXXXXXifX"can_promote_members"XnotXinXpermissions:
XXXXXXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXXXXXreturn
XXXXXXXXtry:
XXXXXXXXXXXXawaitX_.unpin_all_chat_messages(m.chat.id)
XXXXXXXXXXXXawaitXm.reply("IXhaveXunpinnedXallXmessages")
XXXXXXXXexceptXChatAdminRequired:
XXXXXXXXXXXXawaitXm.reply("I'mXnotXadminXhere")
XXXXXXXXexceptXRightForbidden:
XXXXXXXXXXXXawaitXm.reply("IXdon'tXhaveXenoughXrightsXtoXunpinXhere")
XXXXXXXXexceptXRPCErrorXasXef:
XXXXXXXXXXXXawaitXm.reply_text(ef)
XXXXXXXXXXXXreturn

XXXXexceptXExceptionXasXe:
XXXXXXXXprint(e)
XXXXXXXXawaitXm.reply_text(e)
XXXXXXXXreturn


fromXthreadingXimportXRLock

INSERTION_LOCKX=XRLock()


classXPins:
XXXX"""ClassXforXmanagingXantichannelpinsXinXchats."""

XXXX#XDatabaseXnameXtoXconnectXtoXtoXpreformXoperations
XXXXdb_nameX=X"antichannelpin"

XXXXdefX__init__(self,Xchat_id:Xint)X->XNone:
XXXXXXXXself.collectionX=XMongoDB(self.db_name)
XXXXXXXXself.chat_idX=Xchat_id
XXXXXXXXself.chat_infoX=Xself.__ensure_in_db()

XXXXdefXget_settings(self):
XXXXXXXXwithXINSERTION_LOCK:
XXXXXXXXXXXXreturnXself.chat_info

XXXXdefXantichannelpin_on(self):
XXXXXXXXwithXINSERTION_LOCK:
XXXXXXXXXXXXreturnXself.set_on("antichannelpin")

XXXXdefXcleanlinked_on(self):
XXXXXXXXwithXINSERTION_LOCK:
XXXXXXXXXXXXreturnXself.set_on("cleanlinked")

XXXXdefXantichannelpin_off(self):
XXXXXXXXwithXINSERTION_LOCK:
XXXXXXXXXXXXreturnXself.set_off("antichannelpin")

XXXXdefXcleanlinked_off(self):
XXXXXXXXwithXINSERTION_LOCK:
XXXXXXXXXXXXreturnXself.set_off("cleanlinked")

XXXXdefXset_on(self,Xatype:Xstr):
XXXXXXXXwithXINSERTION_LOCK:
XXXXXXXXXXXXotypeX=X"cleanlinked"XifXatypeX==X"antichannelpin"XelseX"antichannelpin"
XXXXXXXXXXXXreturnXself.collection.update(
XXXXXXXXXXXXXXXX{"_id":Xself.chat_id},
XXXXXXXXXXXXXXXX{atype:XTrue,Xotype:XFalse},
XXXXXXXXXXXX)

XXXXdefXset_off(self,Xatype:Xstr):
XXXXXXXXwithXINSERTION_LOCK:
XXXXXXXXXXXXotypeX=X"cleanlinked"XifXatypeX==X"antichannelpin"XelseX"antichannelpin"
XXXXXXXXXXXXreturnXself.collection.update(
XXXXXXXXXXXXXXXX{"_id":Xself.chat_id},
XXXXXXXXXXXXXXXX{atype:XFalse,Xotype:XFalse},
XXXXXXXXXXXX)

XXXXdefX__ensure_in_db(self):
XXXXXXXXchat_dataX=Xself.collection.find_one({"_id":Xself.chat_id})
XXXXXXXXifXnotXchat_data:
XXXXXXXXXXXXnew_dataX=X{
XXXXXXXXXXXXXXXX"_id":Xself.chat_id,
XXXXXXXXXXXXXXXX"antichannelpin":XFalse,
XXXXXXXXXXXXXXXX"cleanlinked":XFalse,
XXXXXXXXXXXX}
XXXXXXXXXXXXself.collection.insert_one(new_data)
XXXXXXXXXXXXreturnXnew_data
XXXXXXXXreturnXchat_data

XXXX#XMigrateXifXchatXidXchanges!
XXXXdefXmigrate_chat(self,Xnew_chat_id:Xint):
XXXXXXXXold_chat_dbX=Xself.collection.find_one({"_id":Xself.chat_id})
XXXXXXXXnew_dataX=Xold_chat_db.update({"_id":Xnew_chat_id})
XXXXXXXXself.collection.insert_one(new_data)
XXXXXXXXself.collection.delete_one({"_id":Xself.chat_id})

XXXX#X-----XStaticXMethodsX-----
XXXX@staticmethod
XXXXdefXcount_chats(atype:Xstr):
XXXXXXXXwithXINSERTION_LOCK:
XXXXXXXXXXXXcollectionX=XMongoDB(Pins.db_name)
XXXXXXXXXXXXreturnXcollection.count({atype:XTrue})

XXXX@staticmethod
XXXXdefXlist_chats(query:Xstr):
XXXXXXXXwithXINSERTION_LOCK:
XXXXXXXXXXXXcollectionX=XMongoDB(Pins.db_name)
XXXXXXXXXXXXreturnXcollection.find_all({query:XTrue})

XXXX@staticmethod
XXXXdefXload_from_db():
XXXXXXXXwithXINSERTION_LOCK:
XXXXXXXXXXXXcollectionX=XMongoDB(Pins.db_name)
XXXXXXXXXXXXreturnXcollection.findall()

XXXX@staticmethod
XXXXdefXrepair_db(collection):
XXXXXXXXall_dataX=Xcollection.find_all()
XXXXXXXXkeysX=X{"antichannelpin":XFalse,X"cleanlinked":XFalse}
XXXXXXXXforXdataXinXall_data:
XXXXXXXXXXXXforXkey,XvalXinXkeys.items():
XXXXXXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXXXXX_X=Xdata[key]
XXXXXXXXXXXXXXXXexceptXKeyError:
XXXXXXXXXXXXXXXXXXXXcollection.update({"_id":Xdata["_id"]},X{key:Xval})


defX__pre_req_pins_chats():
XXXXcollectionX=XMongoDB(Pins.db_name)
XXXXPins.repair_db(collection)


@app.on_message(filters.command("antichannelpin")X&X~filters.private)
asyncXdefXanti_channel_pin(_,Xm:XMessage):
XXXXchat_idX=Xm.chat.id
XXXXuser_idX=Xm.from_user.id
XXXXpermissionsX=XawaitXmember_permissions(chat_id,Xuser_id)
XXXXifX"can_change_info"XnotXinXpermissions:
XXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXreturn
XXXXifX"can_pin_messages"XnotXinXpermissions:
XXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXreturn
XXXXifX"can_restrict_members"XnotXinXpermissions:
XXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXreturn
XXXXifX"can_promote_members"XnotXinXpermissions:
XXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXreturn
XXXXpinsdbX=XPins(m.chat.id)
XXXXifXlen(m.text.split())X==X1:
XXXXXXXXstatusX=Xpinsdb.get_settings()["antichannelpin"]
XXXXXXXXawaitXm.reply_text(f"AntichannelpinXcurrently:X{status}")
XXXXXXXXreturn

XXXXifXlen(m.text.split())X==X2:
XXXXXXXXifXm.command[1]XinX("yes",X"on",X"true"):
XXXXXXXXXXXXpinsdb.antichannelpin_on()
XXXXXXXXXXXXmsgX=X"AntichannelpinXturnedXonXforXthisXchat"
XXXXXXXXelifXm.command[1]XinX("no",X"off",X"false"):
XXXXXXXXXXXXpinsdb.antichannelpin_off()
XXXXXXXXXXXXmsgX=X"AntichannelpinXturnedXoffXforXthisXchat"
XXXXXXXXelse:
XXXXXXXXXXXXawaitXm.reply_text("InvalidXsyntax")
XXXXXXXXXXXXreturn

XXXXawaitXm.reply_text(msg)
XXXXreturn


@app.on_message(filters.command("cleanlinked")X&X~filters.private)
asyncXdefXclean_linked(_,Xm:XMessage):
XXXXchat_idX=Xm.chat.id
XXXXuser_idX=Xm.from_user.id
XXXXpermissionsX=XawaitXmember_permissions(chat_id,Xuser_id)
XXXXifX"can_change_info"XnotXinXpermissions:
XXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXreturn
XXXXifX"can_pin_messages"XnotXinXpermissions:
XXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXreturn
XXXXifX"can_restrict_members"XnotXinXpermissions:
XXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXreturn
XXXXifX"can_promote_members"XnotXinXpermissions:
XXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXreturn
XXXXpinsdbX=XPins(m.chat.id)

XXXXifXlen(m.text.split())X==X1:
XXXXXXXXstatusX=Xpinsdb.get_settings()["cleanlinked"]
XXXXXXXXawaitXm.reply_text(f"CleanlinkedXpinsXcurrently:X{status}")
XXXXXXXXreturn

XXXXifXlen(m.text.split())X==X2:
XXXXXXXXifXm.command[1]XinX("yes",X"on",X"true"):
XXXXXXXXXXXXpinsdb.cleanlinked_on()
XXXXXXXXXXXXmsgX=X"TurnedXonXCleanLinked!XNowXallXtheXmessagesXfromXlinkedXchannelXwillXbeXdeleted!"
XXXXXXXXelifXm.command[1]XinX("no",X"off",X"false"):
XXXXXXXXXXXXpinsdb.cleanlinked_off()
XXXXXXXXXXXXmsgX=X"TurnedXoffXCleanLinked!XMessagesXfromXlinkedXchannelXwillXnotXbeXdeleted!"
XXXXXXXXelse:
XXXXXXXXXXXXawaitXm.reply("InvalidXsyntax")
XXXXXXXXXXXXreturn

XXXXawaitXm.reply(msg)
XXXXreturn


@app.on_message(filters.command("permapin")X&X~filters.private)
asyncXdefXperma_pin(_,Xm:XMessage):
XXXXchat_idX=Xm.chat.id
XXXXuser_idX=Xm.from_user.id
XXXXpermissionsX=XawaitXmember_permissions(chat_id,Xuser_id)
XXXXifX"can_change_info"XnotXinXpermissions:
XXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXreturn
XXXXifX"can_pin_messages"XnotXinXpermissions:
XXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXreturn
XXXXifX"can_restrict_members"XnotXinXpermissions:
XXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXreturn
XXXXifX"can_promote_members"XnotXinXpermissions:
XXXXXXXXawaitXm.reply_text("YouXDon'tXHaveXEnoughXPermissions.")
XXXXXXXXreturn
XXXXifXm.reply_to_messageXorXlen(m.text.split())X>X1:
XXXXXXXXifXm.reply_to_message:
XXXXXXXXXXXXtextX=Xm.reply_to_message.text
XXXXXXXXelifXlen(m.text.split())X>X1:
XXXXXXXXXXXXtextX=Xm.text.split(None,X1)[1]
XXXXXXXXteks,XbuttonX=XawaitXparse_button(text)
XXXXXXXXbuttonX=XawaitXbuild_keyboard(button)
XXXXXXXXbuttonX=XInlineKeyboardMarkup(button)XifXbuttonXelseXNone
XXXXXXXXzX=XawaitXm.reply_text(teks,Xreply_markup=button)
XXXXXXXXawaitXz.pin()
XXXXelse:
XXXXXXXXawaitXm.reply_text("ReplyXtoXaXmessageXorXenterXtextXtoXpinXit.")
XXXXawaitXm.delete()
XXXXreturn


@app.on_message(filters.linked_channel)
asyncXdefXantichanpin_cleanlinked(c,Xm:XMessage):
XXXXtry:
XXXXXXXXmsg_idX=Xm.message_id
XXXXXXXXpins_dbX=XPins(m.chat.id)
XXXXXXXXcurrX=Xpins_db.get_settings()
XXXXXXXXifXcurr["antichannelpin"]:
XXXXXXXXXXXXawaitXc.unpin_chat_message(chat_id=m.chat.id,Xmessage_id=msg_id)
XXXXXXXXifXcurr["cleanlinked"]:
XXXXXXXXXXXXawaitXc.delete_messages(m.chat.id,Xmsg_id)
XXXXexceptXChatAdminRequired:
XXXXXXXXawaitXm.reply_text(
XXXXXXXXXXXX"DisabledXantichannelpinXasXIXdon'tXhaveXenoughXadminXrights!",
XXXXXXXX)
XXXXXXXXpins_db.antichannelpin_off()
XXXXexceptXException:
XXXXXXXXreturn
XXXXreturn
