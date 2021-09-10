#XCopyrightX(C)X2021Xerrorshivansh


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

fromXpymongoXimportXMongoClient
fromXtelethonXimportX*
fromXtelethon.tlXimportX*

fromXInerukiXXimportXBOT_ID
fromXInerukiX.configXimportXget_str_key
fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbot

MONGO_DB_URIX=Xget_str_key("MONGO_URI",Xrequired=True)
clientX=XMongoClient()
clientX=XMongoClient(MONGO_DB_URI)
dbX=Xclient["InerukiX"]
approved_usersX=Xdb.approve
dbbX=Xclient["InerukiX"]
poll_idX=Xdbb.pollid


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXtbot(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXifXisinstance(chat,Xtypes.InputPeerChat):
XXXXXXXXuiX=XawaitXtbot.get_peer_id(user)
XXXXXXXXpsX=X(
XXXXXXXXXXXXawaitXtbot(functions.messages.GetFullChatRequest(chat.chat_id))
XXXXXXXX).full_chat.participants.participants
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXXnext((pXforXpXinXpsXifXp.user_idX==Xui),XNone),
XXXXXXXXXXXX(types.ChatParticipantAdmin,Xtypes.ChatParticipantCreator),
XXXXXXXX)
XXXXreturnXNone


@register(pattern="^/pollX(.*)")
asyncXdefX_(event):
XXXXapproved_userssX=Xapproved_users.find({})
XXXXforXchXinXapproved_userss:
XXXXXXXXiidX=Xch["id"]
XXXXXXXXuserssX=Xch["user"]
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelifXevent.chat_idX==XiidXandXevent.sender_idX==Xuserss:
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXtry:
XXXXXXXXquewX=Xevent.pattern_match.group(1)
XXXXexceptXException:
XXXXXXXXawaitXevent.reply("WhereXisXtheXquestionX?")
XXXXXXXXreturn
XXXXifX"|"XinXquew:
XXXXXXXXsecrets,Xquess,XoptionsX=Xquew.split("|")
XXXXsecretX=Xsecrets.strip()

XXXXifXnotXsecret:
XXXXXXXXawaitXevent.reply("IXneedXaXpollXidXofX5XdigitsXtoXmakeXaXpoll")
XXXXXXXXreturn

XXXXtry:
XXXXXXXXsecretX=Xstr(secret)
XXXXexceptXValueError:
XXXXXXXXawaitXevent.reply("PollXidXshouldXcontainXonlyXnumbers")
XXXXXXXXreturn

XXXX#Xprint(secret)

XXXXifXlen(secret)X!=X5:
XXXXXXXXawaitXevent.reply("PollXidXshouldXbeXanXintegerXofX5Xdigits")
XXXXXXXXreturn

XXXXallpollX=Xpoll_id.find({})
XXXX#Xprint(secret)
XXXXforXcXinXallpoll:
XXXXXXXXifXevent.sender_idX==Xc["user"]:
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"PleaseXstopXtheXpreviousXpollXbeforeXcreatingXaXnewXoneX!"
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn
XXXXpoll_id.insert_one({"user":Xevent.sender_id,X"pollid":Xsecret})

XXXXquesX=Xquess.strip()
XXXXoptionX=Xoptions.strip()
XXXXquizX=Xoption.split("X")[1X-X1]
XXXXifX"True"XinXquiz:
XXXXXXXXquizyX=XTrue
XXXXXXXXifX"@"XinXquiz:
XXXXXXXXXXXXone,XtwoX=Xquiz.split("@")
XXXXXXXXXXXXrightoneX=Xtwo.strip()
XXXXXXXXelse:
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"YouXneedXtoXselectXtheXrightXanswerXwithXquestionXnumberXlikeXTrue@1,XTrue@3Xetc.."
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn

XXXXXXXXquizoptionssX=X[]
XXXXXXXXtry:
XXXXXXXXXXXXabX=Xoption.split("X")[4X-X1]
XXXXXXXXXXXXcdX=Xoption.split("X")[5X-X1]
XXXXXXXXXXXXquizoptionss.append(types.PollAnswer(ab,Xb"1"))
XXXXXXXXXXXXquizoptionss.append(types.PollAnswer(cd,Xb"2"))
XXXXXXXXexceptXException:
XXXXXXXXXXXXawaitXevent.reply("AtXleastXneedXtwoXoptionsXtoXcreateXaXpoll")
XXXXXXXXXXXXreturn
XXXXXXXXtry:
XXXXXXXXXXXXefX=Xoption.split("X")[6X-X1]
XXXXXXXXXXXXquizoptionss.append(types.PollAnswer(ef,Xb"3"))
XXXXXXXXexceptXException:
XXXXXXXXXXXXefX=XNone
XXXXXXXXtry:
XXXXXXXXXXXXghX=Xoption.split("X")[7X-X1]
XXXXXXXXXXXXquizoptionss.append(types.PollAnswer(gh,Xb"4"))
XXXXXXXXexceptXException:
XXXXXXXXXXXXghX=XNone
XXXXXXXXtry:
XXXXXXXXXXXXijX=Xoption.split("X")[8X-X1]
XXXXXXXXXXXXquizoptionss.append(types.PollAnswer(ij,Xb"5"))
XXXXXXXXexceptXException:
XXXXXXXXXXXXijX=XNone
XXXXXXXXtry:
XXXXXXXXXXXXklX=Xoption.split("X")[9X-X1]
XXXXXXXXXXXXquizoptionss.append(types.PollAnswer(kl,Xb"6"))
XXXXXXXXexceptXException:
XXXXXXXXXXXXklX=XNone
XXXXXXXXtry:
XXXXXXXXXXXXmnX=Xoption.split("X")[10X-X1]
XXXXXXXXXXXXquizoptionss.append(types.PollAnswer(mn,Xb"7"))
XXXXXXXXexceptXException:
XXXXXXXXXXXXmnX=XNone
XXXXXXXXtry:
XXXXXXXXXXXXopX=Xoption.split("X")[11X-X1]
XXXXXXXXXXXXquizoptionss.append(types.PollAnswer(op,Xb"8"))
XXXXXXXXexceptXException:
XXXXXXXXXXXXopX=XNone
XXXXXXXXtry:
XXXXXXXXXXXXqrX=Xoption.split("X")[12X-X1]
XXXXXXXXXXXXquizoptionss.append(types.PollAnswer(qr,Xb"9"))
XXXXXXXXexceptXException:
XXXXXXXXXXXXqrX=XNone
XXXXXXXXtry:
XXXXXXXXXXXXstX=Xoption.split("X")[13X-X1]
XXXXXXXXXXXXquizoptionss.append(types.PollAnswer(st,Xb"10"))
XXXXXXXXexceptXException:
XXXXXXXXXXXXstX=XNone

XXXXelifX"False"XinXquiz:
XXXXXXXXquizyX=XFalse
XXXXelse:
XXXXXXXXawaitXevent.reply("WrongXargumentsXprovidedX!")
XXXXXXXXreturn

XXXXpvoteX=Xoption.split("X")[2X-X1]
XXXXifX"True"XinXpvote:
XXXXXXXXpvotyX=XTrue
XXXXelifX"False"XinXpvote:
XXXXXXXXpvotyX=XFalse
XXXXelse:
XXXXXXXXawaitXevent.reply("WrongXargumentsXprovidedX!")
XXXXXXXXreturn
XXXXmchoiceX=Xoption.split("X")[3X-X1]
XXXXifX"True"XinXmchoice:
XXXXXXXXmchoiceeX=XTrue
XXXXelifX"False"XinXmchoice:
XXXXXXXXmchoiceeX=XFalse
XXXXelse:
XXXXXXXXawaitXevent.reply("WrongXargumentsXprovidedX!")
XXXXXXXXreturn
XXXXoptionssX=X[]
XXXXtry:
XXXXXXXXabX=Xoption.split("X")[4X-X1]
XXXXXXXXcdX=Xoption.split("X")[5X-X1]
XXXXXXXXoptionss.append(types.PollAnswer(ab,Xb"1"))
XXXXXXXXoptionss.append(types.PollAnswer(cd,Xb"2"))
XXXXexceptXException:
XXXXXXXXawaitXevent.reply("AtXleastXneedXtwoXoptionsXtoXcreateXaXpoll")
XXXXXXXXreturn
XXXXtry:
XXXXXXXXefX=Xoption.split("X")[6X-X1]
XXXXXXXXoptionss.append(types.PollAnswer(ef,Xb"3"))
XXXXexceptXException:
XXXXXXXXefX=XNone
XXXXtry:
XXXXXXXXghX=Xoption.split("X")[7X-X1]
XXXXXXXXoptionss.append(types.PollAnswer(gh,Xb"4"))
XXXXexceptXException:
XXXXXXXXghX=XNone
XXXXtry:
XXXXXXXXijX=Xoption.split("X")[8X-X1]
XXXXXXXXoptionss.append(types.PollAnswer(ij,Xb"5"))
XXXXexceptXException:
XXXXXXXXijX=XNone
XXXXtry:
XXXXXXXXklX=Xoption.split("X")[9X-X1]
XXXXXXXXoptionss.append(types.PollAnswer(kl,Xb"6"))
XXXXexceptXException:
XXXXXXXXklX=XNone
XXXXtry:
XXXXXXXXmnX=Xoption.split("X")[10X-X1]
XXXXXXXXoptionss.append(types.PollAnswer(mn,Xb"7"))
XXXXexceptXException:
XXXXXXXXmnX=XNone
XXXXtry:
XXXXXXXXopX=Xoption.split("X")[11X-X1]
XXXXXXXXoptionss.append(types.PollAnswer(op,Xb"8"))
XXXXexceptXException:
XXXXXXXXopX=XNone
XXXXtry:
XXXXXXXXqrX=Xoption.split("X")[12X-X1]
XXXXXXXXoptionss.append(types.PollAnswer(qr,Xb"9"))
XXXXexceptXException:
XXXXXXXXqrX=XNone
XXXXtry:
XXXXXXXXstX=Xoption.split("X")[13X-X1]
XXXXXXXXoptionss.append(types.PollAnswer(st,Xb"10"))
XXXXexceptXException:
XXXXXXXXstX=XNone

XXXXifXpvotyXisXFalseXandXquizyXisXFalseXandXmchoiceeXisXFalse:
XXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXtypes.InputMediaPoll(
XXXXXXXXXXXXXXXXpoll=types.Poll(id=12345,Xquestion=ques,Xanswers=optionss,Xquiz=False)
XXXXXXXXXXXX),
XXXXXXXX)

XXXXifXpvotyXisXTrueXandXquizyXisXFalseXandXmchoiceeXisXTrue:
XXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXtypes.InputMediaPoll(
XXXXXXXXXXXXXXXXpoll=types.Poll(
XXXXXXXXXXXXXXXXXXXXid=12345,
XXXXXXXXXXXXXXXXXXXXquestion=ques,
XXXXXXXXXXXXXXXXXXXXanswers=optionss,
XXXXXXXXXXXXXXXXXXXXquiz=False,
XXXXXXXXXXXXXXXXXXXXmultiple_choice=True,
XXXXXXXXXXXXXXXXXXXXpublic_voters=True,
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXX),
XXXXXXXX)

XXXXifXpvotyXisXFalseXandXquizyXisXFalseXandXmchoiceeXisXTrue:
XXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXtypes.InputMediaPoll(
XXXXXXXXXXXXXXXXpoll=types.Poll(
XXXXXXXXXXXXXXXXXXXXid=12345,
XXXXXXXXXXXXXXXXXXXXquestion=ques,
XXXXXXXXXXXXXXXXXXXXanswers=optionss,
XXXXXXXXXXXXXXXXXXXXquiz=False,
XXXXXXXXXXXXXXXXXXXXmultiple_choice=True,
XXXXXXXXXXXXXXXXXXXXpublic_voters=False,
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXX),
XXXXXXXX)

XXXXifXpvotyXisXTrueXandXquizyXisXFalseXandXmchoiceeXisXFalse:
XXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXtypes.InputMediaPoll(
XXXXXXXXXXXXXXXXpoll=types.Poll(
XXXXXXXXXXXXXXXXXXXXid=12345,
XXXXXXXXXXXXXXXXXXXXquestion=ques,
XXXXXXXXXXXXXXXXXXXXanswers=optionss,
XXXXXXXXXXXXXXXXXXXXquiz=False,
XXXXXXXXXXXXXXXXXXXXmultiple_choice=False,
XXXXXXXXXXXXXXXXXXXXpublic_voters=True,
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXX),
XXXXXXXX)

XXXXifXpvotyXisXFalseXandXquizyXisXTrueXandXmchoiceeXisXFalse:
XXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXtypes.InputMediaPoll(
XXXXXXXXXXXXXXXXpoll=types.Poll(
XXXXXXXXXXXXXXXXXXXXid=12345,Xquestion=ques,Xanswers=quizoptionss,Xquiz=True
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXcorrect_answers=[f"{rightone}"],
XXXXXXXXXXXX),
XXXXXXXX)

XXXXifXpvotyXisXTrueXandXquizyXisXTrueXandXmchoiceeXisXFalse:
XXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXtypes.InputMediaPoll(
XXXXXXXXXXXXXXXXpoll=types.Poll(
XXXXXXXXXXXXXXXXXXXXid=12345,
XXXXXXXXXXXXXXXXXXXXquestion=ques,
XXXXXXXXXXXXXXXXXXXXanswers=quizoptionss,
XXXXXXXXXXXXXXXXXXXXquiz=True,
XXXXXXXXXXXXXXXXXXXXpublic_voters=True,
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXcorrect_answers=[f"{rightone}"],
XXXXXXXXXXXX),
XXXXXXXX)

XXXXifXpvotyXisXTrueXandXquizyXisXTrueXandXmchoiceeXisXTrue:
XXXXXXXXawaitXevent.reply("YouXcan'tXuseXmultipleXvotingXwithXquizXmode")
XXXXXXXXreturn
XXXXifXpvotyXisXFalseXandXquizyXisXTrueXandXmchoiceeXisXTrue:
XXXXXXXXawaitXevent.reply("YouXcan'tXuseXmultipleXvotingXwithXquizXmode")
XXXXXXXXreturn


@register(pattern="^/stoppollX(.*)")
asyncXdefXstop(event):
XXXXsecretX=Xevent.pattern_match.group(1)
XXXX#Xprint(secret)
XXXXapproved_userssX=Xapproved_users.find({})
XXXXforXchXinXapproved_userss:
XXXXXXXXiidX=Xch["id"]
XXXXXXXXuserssX=Xch["user"]
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelifXevent.chat_idX==XiidXandXevent.sender_idX==Xuserss:
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn

XXXXifXnotXevent.reply_to_msg_id:
XXXXXXXXawaitXevent.reply("PleaseXreplyXtoXaXpollXtoXstopXit")
XXXXXXXXreturn

XXXXifXinputXisXNone:
XXXXXXXXawaitXevent.reply("WhereXisXtheXpollXidX?")
XXXXXXXXreturn

XXXXtry:
XXXXXXXXsecretX=Xstr(secret)
XXXXexceptXValueError:
XXXXXXXXawaitXevent.reply("PollXidXshouldXcontainXonlyXnumbers")
XXXXXXXXreturn

XXXXifXlen(secret)X!=X5:
XXXXXXXXawaitXevent.reply("PollXidXshouldXbeXanXintegerXofX5Xdigits")
XXXXXXXXreturn

XXXXmsgX=XawaitXevent.get_reply_message()

XXXXifXstr(msg.sender_id)X!=Xstr(BOT_ID):
XXXXXXXXawaitXevent.reply(
XXXXXXXXXXXX"IXcan'tXdoXthisXoperationXonXthisXpoll.\nProbablyXit'sXnotXcreatedXbyXme"
XXXXXXXX)
XXXXXXXXreturn
XXXXprint(secret)
XXXXifXmsg.poll:
XXXXXXXXallpollX=Xpoll_id.find({})
XXXXXXXXforXcXinXallpoll:
XXXXXXXXXXXXifXnotXevent.sender_idX==Xc["user"]XandXnotXsecretX==Xc["pollid"]:
XXXXXXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXXXXXX"Oops,XeitherXyouXhaven'tXcreatedXthisXpollXorXyouXhaveXgivenXwrongXpollXid"
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXreturn
XXXXXXXXifXmsg.poll.poll.closed:
XXXXXXXXXXXXawaitXevent.reply("Oops,XtheXpollXisXalreadyXclosed.")
XXXXXXXXXXXXreturn
XXXXXXXXpoll_id.delete_one({"user":Xevent.sender_id})
XXXXXXXXpollidX=Xmsg.poll.poll.id
XXXXXXXXawaitXmsg.edit(
XXXXXXXXXXXXfile=types.InputMediaPoll(
XXXXXXXXXXXXXXXXpoll=types.Poll(id=pollid,Xquestion="",Xanswers=[],Xclosed=True)
XXXXXXXXXXXX)
XXXXXXXX)
XXXXXXXXawaitXevent.reply("SuccessfullyXstoppedXtheXpoll")
XXXXelse:
XXXXXXXXawaitXevent.reply("ThisXisn'tXaXpoll")


@register(pattern="^/forgotpollid$")
asyncXdefXstop(event):
XXXXapproved_userssX=Xapproved_users.find({})
XXXXforXchXinXapproved_userss:
XXXXXXXXiidX=Xch["id"]
XXXXXXXXuserssX=Xch["user"]
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelifXevent.chat_idX==XiidXandXevent.sender_idX==Xuserss:
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXallpollX=Xpoll_id.find({})
XXXXforXcXinXallpoll:
XXXXXXXXifXevent.sender_idX==Xc["user"]:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXpoll_id.delete_one({"user":Xevent.sender_id})
XXXXXXXXXXXXXXXXawaitXevent.reply("DoneXyouXcanXnowXcreateXaXnewXpoll.")
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXawaitXevent.reply("SeemsXlikeXyouXhaven'tXcreatedXanyXpollXyetX!")


__help__X=X"""
YouXcanXnowXsendXpollsXanonymouslyXwithXIneruki
HereXisXhowXyouXcanXdoXit:
<b>XParametersX</b>X-
X-Xpoll-idX-XaXpollXidXconsistsXofXanX5XdigitXrandomXinteger,XthisXidXisXautomaticallyXremovedXfromXtheXsystemXwhenXyouXstopXyourXpreviousXpoll
X-XquestionX-XtheXquestionXyouXwannaXask
X-X[True@optionnumber/False](1)X-XquizXmode,XyouXmustXstateXtheXcorrectXanswerXwithX@Xeg:XTrue@XorXTrue@2
X-X[True/False](2)X-XpublicXvotes
X-X[True/False](3)X-XmultipleXchoice
<b>XSyntaxX</b>X-
-X/pollX[poll-id]X<i>question</i>X|X<i>True@optionnumber/False</i>X[True/False]X[True/False]X[option1]X[option2]X...XuptoX[option10]
<b>XExamplesX</b>X-
-X/pollX12345X|XamXiXcool?X|XFalseXFalseXFalseXyesXno`
-X/pollX12345X|XamXiXcool?X|XTrue@1XFalseXFalseXyesXno`
<b>XToXstopXaXpollX</b>
ReplyXtoXtheXpollXwithX`/stoppollX[poll-id]`XtoXstopXtheXpoll
<b>XFogotXpollXidX</b>
-X/forgotpollidX-XtoXresetXpoll

"""


__mod_name__X=X"Polls"
