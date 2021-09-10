#XPortedXfromX@MissJuliaRobot

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


importXos
importXsubprocess

importXrequests
fromXgttsXimportXgTTS,XgTTSError
fromXrequestsXimportXget
fromXtelethon.tlXimportXfunctions,Xtypes
fromXtelethon.tl.typesXimportX*

fromXInerukiX.configXimportXget_str_key
fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbot

IBM_WATSON_CRED_PASSWORDX=Xget_str_key("IBM_WATSON_CRED_PASSWORD",XNone)
IBM_WATSON_CRED_URLX=Xget_str_key("IBM_WATSON_CRED_URL",XNone)
WOLFRAM_IDX=Xget_str_key("WOLFRAM_ID",XNone)
TEMP_DOWNLOAD_DIRECTORYX=X"./"


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


@register(pattern=r"^/ask(?:X|$)([\s\S]*)")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXifXnotXevent.reply_to_msg_id:
XXXXXXXXiX=Xevent.pattern_match.group(1)
XXXXXXXXappidX=XWOLFRAM_ID
XXXXXXXXserverX=Xf"https://api.wolframalpha.com/v1/spoken?appid={appid}&i={i}"
XXXXXXXXresX=Xget(server)
XXXXXXXXifX"WolframXAlphaXdidXnotXunderstand"XinXres.text:
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"Sorry,XIneruki'sXAIXsystemsXcould'tXrecognizedXyourXquestion.."
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn
XXXXXXXXawaitXevent.reply(f"**{i}**\n\n"X+Xres.text,Xparse_mode="markdown")

XXXXifXevent.reply_to_msg_id:
XXXXXXXXprevious_messageX=XawaitXevent.get_reply_message()
XXXXXXXXrequired_file_nameX=XawaitXtbot.download_media(
XXXXXXXXXXXXprevious_message,XTEMP_DOWNLOAD_DIRECTORY
XXXXXXXX)
XXXXXXXXifXIBM_WATSON_CRED_URLXisXNoneXorXIBM_WATSON_CRED_PASSWORDXisXNone:
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"YouXneedXtoXsetXtheXrequiredXENVXvariablesXforXthisXmodule.X\nModuleXstopping"
XXXXXXXXXXXX)
XXXXXXXXelse:
XXXXXXXXXXXXheadersX=X{
XXXXXXXXXXXXXXXX"Content-Type":Xprevious_message.media.document.mime_type,
XXXXXXXXXXXX}
XXXXXXXXXXXXdataX=Xopen(required_file_name,X"rb").read()
XXXXXXXXXXXXresponseX=Xrequests.post(
XXXXXXXXXXXXXXXXIBM_WATSON_CRED_URLX+X"/v1/recognize",
XXXXXXXXXXXXXXXXheaders=headers,
XXXXXXXXXXXXXXXXdata=data,
XXXXXXXXXXXXXXXXauth=("apikey",XIBM_WATSON_CRED_PASSWORD),
XXXXXXXXXXXX)
XXXXXXXXXXXXrX=Xresponse.json()
XXXXXXXXXXXXifX"results"XinXr:
XXXXXXXXXXXXXXXX#XprocessXtheXjsonXtoXappropriateXstringXformat
XXXXXXXXXXXXXXXXresultsX=Xr["results"]
XXXXXXXXXXXXXXXXtranscript_responseX=X""
XXXXXXXXXXXXXXXXforXalternativeXinXresults:
XXXXXXXXXXXXXXXXXXXXalternativesX=Xalternative["alternatives"][0]
XXXXXXXXXXXXXXXXXXXXtranscript_responseX+=X"X"X+Xstr(alternatives["transcript"])
XXXXXXXXXXXXXXXXifXtranscript_responseX!=X"":
XXXXXXXXXXXXXXXXXXXXstring_to_showX=X"{}".format(transcript_response)
XXXXXXXXXXXXXXXXXXXXappidX=XWOLFRAM_ID
XXXXXXXXXXXXXXXXXXXXserverX=Xf"https://api.wolframalpha.com/v1/spoken?appid={appid}&i={string_to_show}"
XXXXXXXXXXXXXXXXXXXXresX=Xget(server)

XXXXXXXXXXXXXXXXXXXXifX"WolframXAlphaXdidXnotXunderstand"XinXres:
XXXXXXXXXXXXXXXXXXXXXXXXanswerX=X(
XXXXXXXXXXXXXXXXXXXXXXXXXXXX"I'mXsorryXIneruki'sXAIXsystemXcan'tXundestandXyourXproblem"
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXXXXXanswerX=Xres.text
XXXXXXXXXXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXXXXXXXXXttsX=XgTTS(answer,Xtld="com",Xlang="en")
XXXXXXXXXXXXXXXXXXXXXXXXtts.save("results.mp3")
XXXXXXXXXXXXXXXXXXXXexceptXAssertionError:
XXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXexceptXValueError:
XXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXexceptXRuntimeError:
XXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXexceptXgTTSError:
XXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXwithXopen("results.mp3",X"r"):
XXXXXXXXXXXXXXXXXXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXXXXXXXXXXXXXXXXX"results.mp3",
XXXXXXXXXXXXXXXXXXXXXXXXXXXXvoice_note=True,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXreply_to=event.id,
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXos.remove("results.mp3")
XXXXXXXXXXXXXXXXXXXXos.remove(required_file_name)
XXXXXXXXXXXXXXXXelifX(
XXXXXXXXXXXXXXXXXXXXtranscript_responseX==X"WolframXAlphaXdidXnotXunderstandXyourXinput"
XXXXXXXXXXXXXXXX):
XXXXXXXXXXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXXXXXXXXXanswerX=X"Sorry,XIneruki'sXAIXsystemXcan'tXunderstandXyou.."
XXXXXXXXXXXXXXXXXXXXXXXXttsX=XgTTS(answer,Xtld="com",Xlang="en")
XXXXXXXXXXXXXXXXXXXXXXXXtts.save("results.mp3")
XXXXXXXXXXXXXXXXXXXXexceptXAssertionError:
XXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXexceptXValueError:
XXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXexceptXRuntimeError:
XXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXexceptXgTTSError:
XXXXXXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXXXXXXXXXwithXopen("results.mp3",X"r"):
XXXXXXXXXXXXXXXXXXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXXXXXXXXXXXXXXXXX"results.mp3",
XXXXXXXXXXXXXXXXXXXXXXXXXXXXvoice_note=True,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXreply_to=event.id,
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXos.remove("results.mp3")
XXXXXXXXXXXXXXXXXXXXos.remove(required_file_name)
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXawaitXevent.reply("APIXFailureX!")
XXXXXXXXXXXXXXXXos.remove(required_file_name)


@register(pattern="^/howdoiX(.*)")
asyncXdefXhowdoi(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelifXevent.chat_idX==XiidXandXevent.sender_idX==Xuserss:
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn

XXXXstrX=Xevent.pattern_match.group(1)
XXXXjitX=Xsubprocess.check_output(["howdoi",Xf"{str}"])
XXXXpitX=Xjit.decode()
XXXXawaitXevent.reply(pit)
