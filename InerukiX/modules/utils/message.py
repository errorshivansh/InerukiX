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

fromdatetimeimporttimedelta

#elifraw_button[1]=='note':
#t=InlineKeyboardButton(raw_button[0],callback_data='get_note_{}_{}'.format(chat_id,raw_button[2]))
#elifraw_button[1]=='alert':
#t=InlineKeyboardButton(raw_button[0],callback_data='get_alert_{}_{}'.format(chat_id,raw_button[2]))
#elifraw_button[1]=='deletemsg':
#t=InlineKeyboardButton(raw_button[0],callback_data='get_delete_msg_{}_{}'.format(chat_id,raw_button[2]))


classInvalidTimeUnit(Exception):
pass


defget_arg(message):
try:
returnmessage.get_args().split()[0]
exceptIndexError:
return""


defget_args(message):
args=message.get_args().split()
ifargsisNone:
#gettingargsfromnon-command
args=message.text.split()
returnargs


defget_args_str(message):
return"".join(get_args(message))


defget_cmd(message):
cmd=message.get_command().lower()[1:].split("@")[0]
returncmd


defconvert_time(time_val):
ifnotany(time_val.endswith(unit)forunitin("m","h","d")):
raiseTypeError

time_num=int(time_val[:-1])
unit=time_val[-1]
kwargs={}

ifunit=="m":
kwargs["minutes"]=time_num
elifunit=="h":
kwargs["hours"]=time_num
elifunit=="d":
kwargs["days"]=time_num
else:
raiseInvalidTimeUnit()

val=timedelta(**kwargs)

returnval


defconvert_timedelta(time):
return{"days":time.days,"seconds":time.seconds}


defneed_args_dec(num=1):
defwrapped(func):
asyncdefwrapped_1(*args,**kwargs):
message=args[0]
iflen(message.text.split(""))>num:
returnawaitfunc(*args,**kwargs)
else:
awaitmessage.reply("Givemeargs!")

returnwrapped_1

returnwrapped
