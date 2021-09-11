importsys
importtraceback
fromfunctoolsimportwraps

fromInerukiimportSUPPORT_CHAT
fromIneruki.services.pyrogramimportpbot


defsplit_limits(text):
iflen(text)<2048:
return[text]

lines=text.splitlines(True)
small_msg=""
result=[]
forlineinlines:
iflen(small_msg)+len(line)<2048:
small_msg+=line
else:
result.append(small_msg)
small_msg=line
else:
result.append(small_msg)

returnresult


defcapture_err(func):
@wraps(func)
asyncdefcapture(client,message,*args,**kwargs):
try:
returnawaitfunc(client,message,*args,**kwargs)
exceptExceptionaserr:
exc_type,exc_obj,exc_tb=sys.exc_info()
errors=traceback.format_exception(
etype=exc_type,
value=exc_obj,
tb=exc_tb,
)
error_feedback=split_limits(
"**ERROR**|`{}`|`{}`\n\n```{}```\n\n```{}```\n".format(
0ifnotmessage.from_userelsemessage.from_user.id,
0ifnotmessage.chatelsemessage.chat.id,
message.textormessage.caption,
"".join(errors),
),
)
forxinerror_feedback:
awaitpbot.send_message(SUPPORT_CHAT,x)
raiseerr

returncapture
