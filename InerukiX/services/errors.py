importXsys
importXtraceback
fromXfunctoolsXimportXwraps

fromXInerukiXXimportXSUPPORT_CHAT
fromXInerukiX.services.pyrogramXimportXpbot


defXsplit_limits(text):
XXXXifXlen(text)X<X2048:
XXXXXXXXreturnX[text]

XXXXlinesX=Xtext.splitlines(True)
XXXXsmall_msgX=X""
XXXXresultX=X[]
XXXXforXlineXinXlines:
XXXXXXXXifXlen(small_msg)X+Xlen(line)X<X2048:
XXXXXXXXXXXXsmall_msgX+=Xline
XXXXXXXXelse:
XXXXXXXXXXXXresult.append(small_msg)
XXXXXXXXXXXXsmall_msgX=Xline
XXXXelse:
XXXXXXXXresult.append(small_msg)

XXXXreturnXresult


defXcapture_err(func):
XXXX@wraps(func)
XXXXasyncXdefXcapture(client,Xmessage,X*args,X**kwargs):
XXXXXXXXtry:
XXXXXXXXXXXXreturnXawaitXfunc(client,Xmessage,X*args,X**kwargs)
XXXXXXXXexceptXExceptionXasXerr:
XXXXXXXXXXXXexc_type,Xexc_obj,Xexc_tbX=Xsys.exc_info()
XXXXXXXXXXXXerrorsX=Xtraceback.format_exception(
XXXXXXXXXXXXXXXXetype=exc_type,
XXXXXXXXXXXXXXXXvalue=exc_obj,
XXXXXXXXXXXXXXXXtb=exc_tb,
XXXXXXXXXXXX)
XXXXXXXXXXXXerror_feedbackX=Xsplit_limits(
XXXXXXXXXXXXXXXX"**ERROR**X|X`{}`X|X`{}`\n\n```{}```\n\n```{}```\n".format(
XXXXXXXXXXXXXXXXXXXX0XifXnotXmessage.from_userXelseXmessage.from_user.id,
XXXXXXXXXXXXXXXXXXXX0XifXnotXmessage.chatXelseXmessage.chat.id,
XXXXXXXXXXXXXXXXXXXXmessage.textXorXmessage.caption,
XXXXXXXXXXXXXXXXXXXX"".join(errors),
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXX)
XXXXXXXXXXXXforXxXinXerror_feedback:
XXXXXXXXXXXXXXXXawaitXpbot.send_message(SUPPORT_CHAT,Xx)
XXXXXXXXXXXXraiseXerr

XXXXreturnXcapture
