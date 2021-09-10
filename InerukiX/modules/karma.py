#XPortedXFromXWilliamButcherXBot.
#XCreditsXGoesXtoXWilliamButcherBot
#XPortedXfromXhttps://github.com/TheHamkerCat/WilliamButcherBot
"""
MITXLicense
CopyrightX(c)X2021XTheHamkerCat
PermissionXisXherebyXgranted,XfreeXofXcharge,XtoXanyXpersonXobtainingXaXcopy
ofXthisXsoftwareXandXassociatedXdocumentationXfilesX(theX"Software"),XtoXdeal
inXtheXSoftwareXwithoutXrestriction,XincludingXwithoutXlimitationXtheXrights
toXuse,Xcopy,Xmodify,Xmerge,Xpublish,Xdistribute,Xsublicense,Xand/orXsell
copiesXofXtheXSoftware,XandXtoXpermitXpersonsXtoXwhomXtheXSoftwareXis
furnishedXtoXdoXso,XsubjectXtoXtheXfollowingXconditions:
TheXaboveXcopyrightXnoticeXandXthisXpermissionXnoticeXshallXbeXincludedXinXall
copiesXorXsubstantialXportionsXofXtheXSoftware.
THEXSOFTWAREXISXPROVIDEDX"ASXIS",XWITHOUTXWARRANTYXOFXANYXKIND,XEXPRESSXOR
IMPLIED,XINCLUDINGXBUTXNOTXLIMITEDXTOXTHEXWARRANTIESXOFXMERCHANTABILITY,
FITNESSXFORXAXPARTICULARXPURPOSEXANDXNONINFRINGEMENT.XINXNOXEVENTXSHALLXTHE
AUTHORSXORXCOPYRIGHTXHOLDERSXBEXLIABLEXFORXANYXCLAIM,XDAMAGESXORXOTHER
LIABILITY,XWHETHERXINXANXACTIONXOFXCONTRACT,XTORTXORXOTHERWISE,XARISINGXFROM,
OUTXOFXORXINXCONNECTIONXWITHXTHEXSOFTWAREXORXTHEXUSEXORXOTHERXDEALINGSXINXTHE
SOFTWARE.
"""

fromXtypingXimportXDict,XUnion

fromXpyrogramXimportXfilters

fromXInerukiX.db.mongo_helpers.karmaXimportXis_karma_on,Xkarma_off,Xkarma_on
fromXInerukiX.function.pluginhelpersXimportXmember_permissions
fromXInerukiX.services.mongo2XimportXdb
fromXInerukiX.services.pyrogramXimportXpbotXasXapp

karmadbX=Xdb.karma
karma_positive_groupX=X3
karma_negative_groupX=X4


asyncXdefXint_to_alpha(user_id:Xint)X->Xstr:
XXXXalphabetX=X["a",X"b",X"c",X"d",X"e",X"f",X"g",X"h",X"i",X"j"]
XXXXtextX=X""
XXXXuser_idX=Xstr(user_id)
XXXXforXiXinXuser_id:
XXXXXXXXtextX+=Xalphabet[int(i)]
XXXXreturnXtext


asyncXdefXalpha_to_int(user_id_alphabet:Xstr)X->Xint:
XXXXalphabetX=X["a",X"b",X"c",X"d",X"e",X"f",X"g",X"h",X"i",X"j"]
XXXXuser_idX=X""
XXXXforXiXinXuser_id_alphabet:
XXXXXXXXindexX=Xalphabet.index(i)
XXXXXXXXuser_idX+=Xstr(index)
XXXXuser_idX=Xint(user_id)
XXXXreturnXuser_id


asyncXdefXget_karmas_count()X->Xdict:
XXXXchatsX=Xkarmadb.find({"chat_id":X{"$lt":X0}})
XXXXifXnotXchats:
XXXXXXXXreturnX{}
XXXXchats_countX=X0
XXXXkarmas_countX=X0
XXXXforXchatXinXawaitXchats.to_list(length=1000000):
XXXXXXXXforXiXinXchat["karma"]:
XXXXXXXXXXXXkarmas_countX+=Xchat["karma"][i]["karma"]
XXXXXXXXchats_countX+=X1
XXXXreturnX{"chats_count":Xchats_count,X"karmas_count":Xkarmas_count}


asyncXdefXget_karmas(chat_id:Xint)X->XDict[str,Xint]:
XXXXkarmaX=XawaitXkarmadb.find_one({"chat_id":Xchat_id})
XXXXifXkarma:
XXXXXXXXkarmaX=Xkarma["karma"]
XXXXelse:
XXXXXXXXkarmaX=X{}
XXXXreturnXkarma


asyncXdefXget_karma(chat_id:Xint,Xname:Xstr)X->XUnion[bool,Xdict]:
XXXXnameX=Xname.lower().strip()
XXXXkarmasX=XawaitXget_karmas(chat_id)
XXXXifXnameXinXkarmas:
XXXXXXXXreturnXkarmas[name]


asyncXdefXupdate_karma(chat_id:Xint,Xname:Xstr,Xkarma:Xdict):
XXXXnameX=Xname.lower().strip()
XXXXkarmasX=XawaitXget_karmas(chat_id)
XXXXkarmas[name]X=Xkarma
XXXXawaitXkarmadb.update_one(
XXXXXXXX{"chat_id":Xchat_id},X{"$set":X{"karma":Xkarmas}},Xupsert=True
XXXX)


_mod_name_X=X"Karma"
_help_X=X"""[UPVOTE]X-XUseXupvoteXkeywordsXlikeX"+",X"+1",X"thanks"XetcXtoXupvoteXaXmessage.
[DOWNVOTE]X-XUseXdownvoteXkeywordsXlikeX"-",X"-1",XetcXtoXdownvoteXaXmessage.
ReplyXtoXaXmessageXwithX/karmaXtoXcheckXaXuser'sXkarma
SendX/karmaXwithoutXreplyingXtoXanyXmessageXtoXchekXkarmaXlistXofXtopX10Xusers
<i>XSpecialXCreditsXtoXWilliamButcherBotX</i>"""


regex_upvoteX=Xr"^((?i)\+|\+\+|\+1|thx|tnx|ty|thankXyou|thanx|thanks|pro|cool|good|👍)$"
regex_downvoteX=Xr"^(\-|\-\-|\-1|👎)$"


@app.on_message(
XXXXfilters.text
XXXX&Xfilters.group
XXXX&Xfilters.incoming
XXXX&Xfilters.reply
XXXX&Xfilters.regex(regex_upvote)
XXXX&X~filters.via_bot
XXXX&X~filters.bot
XXXX&X~filters.edited,
XXXXgroup=karma_positive_group,
)
asyncXdefXupvote(_,Xmessage):

XXXXifXnotXawaitXis_karma_on(message.chat.id):
XXXXXXXXreturn
XXXXtry:
XXXXXXXXifXmessage.reply_to_message.from_user.idX==Xmessage.from_user.id:
XXXXXXXXXXXXreturn
XXXXexcept:
XXXXXXXXreturn
XXXXchat_idX=Xmessage.chat.id
XXXXtry:
XXXXXXXXuser_idX=Xmessage.reply_to_message.from_user.id
XXXXexcept:
XXXXXXXXreturn
XXXXuser_mentionX=Xmessage.reply_to_message.from_user.mention
XXXXcurrent_karmaX=XawaitXget_karma(chat_id,XawaitXint_to_alpha(user_id))
XXXXifXcurrent_karma:
XXXXXXXXcurrent_karmaX=Xcurrent_karma["karma"]
XXXXXXXXkarmaX=Xcurrent_karmaX+X1
XXXXXXXXnew_karmaX=X{"karma":Xkarma}
XXXXXXXXawaitXupdate_karma(chat_id,XawaitXint_to_alpha(user_id),Xnew_karma)
XXXXelse:
XXXXXXXXkarmaX=X1
XXXXXXXXnew_karmaX=X{"karma":Xkarma}
XXXXXXXXawaitXupdate_karma(chat_id,XawaitXint_to_alpha(user_id),Xnew_karma)
XXXXawaitXmessage.reply_text(
XXXXXXXXf"IncrementedXKarmaXofX{user_mention}XByX1X\nTotalXPoints:X{karma}"
XXXX)


@app.on_message(
XXXXfilters.text
XXXX&Xfilters.group
XXXX&Xfilters.incoming
XXXX&Xfilters.reply
XXXX&Xfilters.regex(regex_downvote)
XXXX&X~filters.via_bot
XXXX&X~filters.bot
XXXX&X~filters.edited,
XXXXgroup=karma_negative_group,
)
asyncXdefXdownvote(_,Xmessage):

XXXXifXnotXawaitXis_karma_on(message.chat.id):
XXXXXXXXreturn
XXXXtry:
XXXXXXXXifXmessage.reply_to_message.from_user.idX==Xmessage.from_user.id:
XXXXXXXXXXXXreturn
XXXXexcept:
XXXXXXXXreturn
XXXXchat_idX=Xmessage.chat.id
XXXXtry:
XXXXXXXXuser_idX=Xmessage.reply_to_message.from_user.id
XXXXexcept:
XXXXXXXXreturn
XXXXuser_mentionX=Xmessage.reply_to_message.from_user.mention
XXXXcurrent_karmaX=XawaitXget_karma(chat_id,XawaitXint_to_alpha(user_id))
XXXXifXcurrent_karma:
XXXXXXXXcurrent_karmaX=Xcurrent_karma["karma"]
XXXXXXXXkarmaX=Xcurrent_karmaX-X1
XXXXXXXXnew_karmaX=X{"karma":Xkarma}
XXXXXXXXawaitXupdate_karma(chat_id,XawaitXint_to_alpha(user_id),Xnew_karma)
XXXXelse:
XXXXXXXXkarmaX=X1
XXXXXXXXnew_karmaX=X{"karma":Xkarma}
XXXXXXXXawaitXupdate_karma(chat_id,XawaitXint_to_alpha(user_id),Xnew_karma)
XXXXawaitXmessage.reply_text(
XXXXXXXXf"DecrementedXKarmaXOfX{user_mention}XByX1X\nTotalXPoints:X{karma}"
XXXX)


@app.on_message(filters.command("karma")X&Xfilters.group)
asyncXdefXkarma(_,Xmessage):
XXXXchat_idX=Xmessage.chat.id
XXXXifXlen(message.command)X!=X2:
XXXXXXXXifXnotXmessage.reply_to_message:
XXXXXXXXXXXXkarmaX=XawaitXget_karmas(chat_id)
XXXXXXXXXXXXmsgX=Xf"**KarmaXlistXofX{message.chat.title}:-X**\n"
XXXXXXXXXXXXlimitX=X0
XXXXXXXXXXXXkarma_diccX=X{}
XXXXXXXXXXXXforXiXinXkarma:
XXXXXXXXXXXXXXXXuser_idX=XawaitXalpha_to_int(i)
XXXXXXXXXXXXXXXXuser_karmaX=Xkarma[i]["karma"]
XXXXXXXXXXXXXXXXkarma_dicc[str(user_id)]X=Xuser_karma
XXXXXXXXXXXXXXXXkarma_arrangedX=Xdict(
XXXXXXXXXXXXXXXXXXXXsorted(karma_dicc.items(),Xkey=lambdaXitem:Xitem[1],Xreverse=True)
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXforXuser_idd,Xkarma_countXinXkarma_arranged.items():
XXXXXXXXXXXXXXXXifXlimitX>X9:
XXXXXXXXXXXXXXXXXXXXbreak
XXXXXXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXXXXXuser_nameX=X(awaitXapp.get_users(int(user_idd))).username
XXXXXXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXXXXXcontinue
XXXXXXXXXXXXXXXXmsgX+=Xf"{user_name}X:X`{karma_count}`\n"
XXXXXXXXXXXXXXXXlimitX+=X1
XXXXXXXXXXXXawaitXmessage.reply_text(msg)
XXXXXXXXelse:
XXXXXXXXXXXXuser_idX=Xmessage.reply_to_message.from_user.id
XXXXXXXXXXXXkarmaX=XawaitXget_karma(chat_id,XawaitXint_to_alpha(user_id))
XXXXXXXXXXXXifXkarma:
XXXXXXXXXXXXXXXXkarmaX=Xkarma["karma"]
XXXXXXXXXXXXXXXXawaitXmessage.reply_text(f"**TotalXPoints**:X__{karma}__")
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXkarmaX=X0
XXXXXXXXXXXXXXXXawaitXmessage.reply_text(f"**TotalXPoints**:X__{karma}__")
XXXXXXXXreturn
XXXXstatusX=Xmessage.text.split(None,X1)[1].strip()
XXXXstatusX=Xstatus.lower()
XXXXchat_idX=Xmessage.chat.id
XXXXuser_idX=Xmessage.from_user.id
XXXXpermissionsX=XawaitXmember_permissions(chat_id,Xuser_id)
XXXXifX"can_change_info"XnotXinXpermissions:
XXXXXXXXawaitXmessage.reply_text("YouXdon'tXhaveXenoughXpermissions.")
XXXXXXXXreturn
XXXXifXstatusX==X"on"XorXstatusX==X"ON":
XXXXXXXXawaitXkarma_on(chat_id)
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXXf"AddedXChatX{chat_id}XToXDatabase.XKarmaXwillXbeXenabledXhere"
XXXXXXXX)
XXXXelifXstatusX==X"off"XorXstatusX==X"OFF":
XXXXXXXXawaitXkarma_off(chat_id)
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXXf"RemovedXChatX{chat_id}XToXDatabase.XKarmaXwillXbeXdisabledXhere"
XXXXXXXX)
