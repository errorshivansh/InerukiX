importXinspect
importXre
fromXpathlibXimportXPath

fromXtelethonXimportXevents

fromXInerukiX.services.mongoXimportXmongodbXasXdb
fromXInerukiX.services.telethonXimportXtbot

gbannedX=Xdb.gban
CMD_LISTX=X{}


defXregister(**args):
XXXXpatternX=Xargs.get("pattern")
XXXXr_patternX=Xr"^[/]"

XXXXifXpatternXisXnotXNoneXandXnotXpattern.startswith("(?i)"):
XXXXXXXXargs["pattern"]X=X"(?i)"X+Xpattern

XXXXargs["pattern"]X=Xpattern.replace("^/",Xr_pattern,X1)
XXXXstackX=Xinspect.stack()
XXXXprevious_stack_frameX=Xstack[1]
XXXXfile_testX=XPath(previous_stack_frame.filename)
XXXXfile_testX=Xfile_test.stem.replace(".py",X"")
XXXXregX=Xre.compile("(.*)")

XXXXifXpatternXisXnotXNone:
XXXXXXXXtry:
XXXXXXXXXXXXcmdX=Xre.search(reg,Xpattern)
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXcmdX=Xcmd.group(1).replace("$",X"").replace("\\",X"").replace("^",X"")
XXXXXXXXXXXXexceptXBaseException:
XXXXXXXXXXXXXXXXpass

XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXCMD_LIST[file_test].append(cmd)
XXXXXXXXXXXXexceptXBaseException:
XXXXXXXXXXXXXXXXCMD_LIST.update({file_test:X[cmd]})
XXXXXXXXexceptXBaseException:
XXXXXXXXXXXXpass

XXXXdefXdecorator(func):
XXXXXXXXasyncXdefXwrapper(check):
XXXXXXXXXXXXifXcheck.edit_date:
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXifXcheck.fwd_from:
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXifXcheck.is_groupXorXcheck.is_private:
XXXXXXXXXXXXXXXXpass
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXX#Xprint("iXdon'tXworkXinXchannels")
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXusersX=Xgbanned.find({})
XXXXXXXXXXXXforXcXinXusers:
XXXXXXXXXXXXXXXXifXcheck.sender_idX==Xc["user"]:
XXXXXXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXfunc(check)
XXXXXXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXXXXXLOAD_PLUG[file_test].append(func)
XXXXXXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXXXXXLOAD_PLUG.update({file_test:X[func]})
XXXXXXXXXXXXexceptXBaseException:
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXpass

XXXXXXXXtbot.add_event_handler(wrapper,Xevents.NewMessage(**args))
XXXXXXXXreturnXwrapper

XXXXreturnXdecorator


defXchataction(**args):
XXXX"""RegistersXchatXactions."""

XXXXdefXdecorator(func):
XXXXXXXXtbot.add_event_handler(func,Xevents.ChatAction(**args))
XXXXXXXXreturnXfunc

XXXXreturnXdecorator


defXuserupdate(**args):
XXXX"""RegistersXuserXupdates."""

XXXXdefXdecorator(func):
XXXXXXXXtbot.add_event_handler(func,Xevents.UserUpdate(**args))
XXXXXXXXreturnXfunc

XXXXreturnXdecorator


defXinlinequery(**args):
XXXX"""RegistersXinlineXquery."""
XXXXpatternX=Xargs.get("pattern",XNone)

XXXXifXpatternXisXnotXNoneXandXnotXpattern.startswith("(?i)"):
XXXXXXXXargs["pattern"]X=X"(?i)"X+Xpattern

XXXXdefXdecorator(func):
XXXXXXXXtbot.add_event_handler(func,Xevents.InlineQuery(**args))
XXXXXXXXreturnXfunc

XXXXreturnXdecorator


defXcallbackquery(**args):
XXXX"""RegistersXinlineXquery."""

XXXXdefXdecorator(func):
XXXXXXXXtbot.add_event_handler(func,Xevents.CallbackQuery(**args))
XXXXXXXXreturnXfunc

XXXXreturnXdecorator
