importinspect
importre
frompathlibimportPath

fromtelethonimportevents

fromIneruki.services.mongoimportmongodbasdb
fromIneruki.services.telethonimporttbot

gbanned=db.gban
CMD_LIST={}


defregister(**args):
pattern=args.get("pattern")
r_pattern=r"^[/]"

ifpatternisnotNoneandnotpattern.startswith("(?i)"):
args["pattern"]="(?i)"+pattern

args["pattern"]=pattern.replace("^/",r_pattern,1)
stack=inspect.stack()
previous_stack_frame=stack[1]
file_test=Path(previous_stack_frame.filename)
file_test=file_test.stem.replace(".py","")
reg=re.compile("(.*)")

ifpatternisnotNone:
try:
cmd=re.search(reg,pattern)
try:
cmd=cmd.group(1).replace("$","").replace("\\","").replace("^","")
exceptBaseException:
pass

try:
CMD_LIST[file_test].append(cmd)
exceptBaseException:
CMD_LIST.update({file_test:[cmd]})
exceptBaseException:
pass

defdecorator(func):
asyncdefwrapper(check):
ifcheck.edit_date:
return
ifcheck.fwd_from:
return
ifcheck.is_grouporcheck.is_private:
pass
else:
#print("idon'tworkinchannels")
return
users=gbanned.find({})
forcinusers:
ifcheck.sender_id==c["user"]:
return
try:
awaitfunc(check)
try:
LOAD_PLUG[file_test].append(func)
exceptException:
LOAD_PLUG.update({file_test:[func]})
exceptBaseException:
return
else:
pass

tbot.add_event_handler(wrapper,events.NewMessage(**args))
returnwrapper

returndecorator


defchataction(**args):
"""Registerschatactions."""

defdecorator(func):
tbot.add_event_handler(func,events.ChatAction(**args))
returnfunc

returndecorator


defuserupdate(**args):
"""Registersuserupdates."""

defdecorator(func):
tbot.add_event_handler(func,events.UserUpdate(**args))
returnfunc

returndecorator


definlinequery(**args):
"""Registersinlinequery."""
pattern=args.get("pattern",None)

ifpatternisnotNoneandnotpattern.startswith("(?i)"):
args["pattern"]="(?i)"+pattern

defdecorator(func):
tbot.add_event_handler(func,events.InlineQuery(**args))
returnfunc

returndecorator


defcallbackquery(**args):
"""Registersinlinequery."""

defdecorator(func):
tbot.add_event_handler(func,events.CallbackQuery(**args))
returnfunc

returndecorator
