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

fromXdatetimeXimportXtimedelta

#XelifXraw_button[1]X==X'note':
#XtX=XInlineKeyboardButton(raw_button[0],Xcallback_data='get_note_{}_{}'.format(chat_id,Xraw_button[2]))
#XelifXraw_button[1]X==X'alert':
#XtX=XInlineKeyboardButton(raw_button[0],Xcallback_data='get_alert_{}_{}'.format(chat_id,Xraw_button[2]))
#XelifXraw_button[1]X==X'deletemsg':
#XtX=XInlineKeyboardButton(raw_button[0],Xcallback_data='get_delete_msg_{}_{}'.format(chat_id,Xraw_button[2]))


classXInvalidTimeUnit(Exception):
XXXXpass


defXget_arg(message):
XXXXtry:
XXXXXXXXreturnXmessage.get_args().split()[0]
XXXXexceptXIndexError:
XXXXXXXXreturnX""


defXget_args(message):
XXXXargsX=Xmessage.get_args().split()
XXXXifXargsXisXNone:
XXXXXXXX#XgettingXargsXfromXnon-command
XXXXXXXXargsX=Xmessage.text.split()
XXXXreturnXargs


defXget_args_str(message):
XXXXreturnX"X".join(get_args(message))


defXget_cmd(message):
XXXXcmdX=Xmessage.get_command().lower()[1:].split("@")[0]
XXXXreturnXcmd


defXconvert_time(time_val):
XXXXifXnotXany(time_val.endswith(unit)XforXunitXinX("m",X"h",X"d")):
XXXXXXXXraiseXTypeError

XXXXtime_numX=Xint(time_val[:-1])
XXXXunitX=Xtime_val[-1]
XXXXkwargsX=X{}

XXXXifXunitX==X"m":
XXXXXXXXkwargs["minutes"]X=Xtime_num
XXXXelifXunitX==X"h":
XXXXXXXXkwargs["hours"]X=Xtime_num
XXXXelifXunitX==X"d":
XXXXXXXXkwargs["days"]X=Xtime_num
XXXXelse:
XXXXXXXXraiseXInvalidTimeUnit()

XXXXvalX=Xtimedelta(**kwargs)

XXXXreturnXval


defXconvert_timedelta(time):
XXXXreturnX{"days":Xtime.days,X"seconds":Xtime.seconds}


defXneed_args_dec(num=1):
XXXXdefXwrapped(func):
XXXXXXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXXXXXmessageX=Xargs[0]
XXXXXXXXXXXXifXlen(message.text.split("X"))X>Xnum:
XXXXXXXXXXXXXXXXreturnXawaitXfunc(*args,X**kwargs)
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXawaitXmessage.reply("GiveXmeXargs!")

XXXXXXXXreturnXwrapped_1

XXXXreturnXwrapped
