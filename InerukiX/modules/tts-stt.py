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
fromXdatetimeXimportXdatetime

importXrequests
fromXgttsXimportXgTTS,XgTTSError
fromXtelethon.tlXimportXfunctions,Xtypes

fromXInerukiX.configXimportXget_str_key
fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbot

IBM_WATSON_CRED_PASSWORDX=Xget_str_key("IBM_WATSON_CRED_PASSWORD",Xrequired=False)
IBM_WATSON_CRED_URLX=Xget_str_key("IBM_WATSON_CRED_URL",Xrequired=False)
TEMP_DOWNLOAD_DIRECTORYX=X"./"


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXtbot(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXifXisinstance(chat,Xtypes.InputPeerUser):
XXXXXXXXreturnXTrue


@register(pattern="^/ttsX(.*)")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXinput_strX=Xevent.pattern_match.group(1)
XXXXreply_to_idX=Xevent.message.id
XXXXifXevent.reply_to_msg_id:
XXXXXXXXprevious_messageX=XawaitXevent.get_reply_message()
XXXXXXXXtextX=Xprevious_message.message
XXXXXXXXlanX=Xinput_str
XXXXelifX"|"XinXinput_str:
XXXXXXXXlan,XtextX=Xinput_str.split("|")
XXXXelse:
XXXXXXXXawaitXevent.reply(
XXXXXXXXXXXX"InvalidXSyntax\nFormatX`/ttsXlangX|Xtext`\nForXeg:X`/ttsXenX|Xhello`"
XXXXXXXX)
XXXXXXXXreturn
XXXXtextX=Xtext.strip()
XXXXlanX=Xlan.strip()
XXXXtry:
XXXXXXXXttsX=XgTTS(text,Xtld="com",Xlang=lan)
XXXXXXXXtts.save("k.mp3")
XXXXexceptXAssertionError:
XXXXXXXXawaitXevent.reply(
XXXXXXXXXXXX"TheXtextXisXempty.\n"
XXXXXXXXXXXX"NothingXleftXtoXspeakXafterXpre-precessing,X"
XXXXXXXXXXXX"tokenizingXandXcleaning."
XXXXXXXX)
XXXXXXXXreturn
XXXXexceptXValueError:
XXXXXXXXawaitXevent.reply("LanguageXisXnotXsupported.")
XXXXXXXXreturn
XXXXexceptXRuntimeError:
XXXXXXXXawaitXevent.reply("ErrorXloadingXtheXlanguagesXdictionary.")
XXXXXXXXreturn
XXXXexceptXgTTSError:
XXXXXXXXawaitXevent.reply("ErrorXinXGoogleXText-to-SpeechXAPIXrequestX!")
XXXXXXXXreturn
XXXXwithXopen("k.mp3",X"r"):
XXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXevent.chat_id,X"k.mp3",Xvoice_note=True,Xreply_to=reply_to_id
XXXXXXXX)
XXXXXXXXos.remove("k.mp3")


#X------XTHANKSXTOXLONAMIX------#


@register(pattern="^/stt$")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXis_register_admin(event.input_chat,Xevent.message.sender_id):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXstartX=Xdatetime.now()
XXXXifXnotXos.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
XXXXXXXXos.makedirs(TEMP_DOWNLOAD_DIRECTORY)

XXXXifXevent.reply_to_msg_id:
XXXXXXXXprevious_messageX=XawaitXevent.get_reply_message()
XXXXXXXXrequired_file_nameX=XawaitXevent.client.download_media(
XXXXXXXXXXXXprevious_message,XTEMP_DOWNLOAD_DIRECTORY
XXXXXXXX)
XXXXXXXXifXIBM_WATSON_CRED_URLXisXNoneXorXIBM_WATSON_CRED_PASSWORDXisXNone:
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"YouXneedXtoXsetXtheXrequiredXENVXvariablesXforXthisXmodule.X\nModuleXstopping"
XXXXXXXXXXXX)
XXXXXXXXelse:
XXXXXXXXXXXX#XawaitXevent.reply("StartingXanalysis")
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
XXXXXXXXXXXXXXXXtranscript_confidenceX=X""
XXXXXXXXXXXXXXXXforXalternativeXinXresults:
XXXXXXXXXXXXXXXXXXXXalternativesX=Xalternative["alternatives"][0]
XXXXXXXXXXXXXXXXXXXXtranscript_responseX+=X"X"X+Xstr(alternatives["transcript"])
XXXXXXXXXXXXXXXXXXXXtranscript_confidenceX+=X(
XXXXXXXXXXXXXXXXXXXXXXXX"X"X+Xstr(alternatives["confidence"])X+X"X+X"
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXendX=Xdatetime.now()
XXXXXXXXXXXXXXXXmsX=X(endX-Xstart).seconds
XXXXXXXXXXXXXXXXifXtranscript_responseX!=X"":
XXXXXXXXXXXXXXXXXXXXstring_to_showX=X"TRANSCRIPT:X`{}`\nTimeXTaken:X{}Xseconds\nConfidence:X`{}`".format(
XXXXXXXXXXXXXXXXXXXXXXXXtranscript_response,Xms,Xtranscript_confidence
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXstring_to_showX=X"TRANSCRIPT:X`Nil`\nTimeXTaken:X{}Xseconds\n\n**NoXResultsXFound**".format(
XXXXXXXXXXXXXXXXXXXXXXXXms
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXawaitXevent.reply(string_to_show)
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXawaitXevent.reply(r["error"])
XXXXXXXXXXXX#Xnow,XremoveXtheXtemporaryXfile
XXXXXXXXXXXXos.remove(required_file_name)
XXXXelse:
XXXXXXXXawaitXevent.reply("ReplyXtoXaXvoiceXmessage,XtoXgetXtheXtextXoutXofXit.")


_mod_name_X=X"TextXtoXSpeech"

_help_X=X"""
X-X/tts:XReplyXtoXanyXmessageXtoXgetXtextXtoXspeechXoutput
X-X/stt:XTypeXinXreplyXtoXaXvoiceXmessage(englishXonly)XtoXextractXtextXfromXit.
"""
