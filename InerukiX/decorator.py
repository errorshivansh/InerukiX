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

importtime
fromimportlibimportimport_module

fromaiogramimporttypes
fromaiogram.dispatcher.handlerimportSkipHandler
fromsentry_sdkimportconfigure_scope

fromInerukiimportBOT_USERNAME,dp
fromIneruki.configimportget_bool_key
fromIneruki.modules.errorimportparse_update
fromIneruki.utils.filtersimportALL_FILTERS
fromIneruki.utils.loggerimportlog

DEBUG_MODE=get_bool_key("DEBUG_MODE")
ALLOW_F_COMMANDS=get_bool_key("ALLOW_FORWARDS_COMMANDS")
ALLOW_COMMANDS_FROM_EC=get_bool_key("ALLOW_ECEL")
CMD_NOT_MONO=get_bool_key("DISALLOW_MONO_CMDS")

REGISTRED_COMMANDS=[]
COMMANDS_ALIASES={}

#Importfilters
log.info("Filterstoload:%s",str(ALL_FILTERS))
formodule_nameinALL_FILTERS:
log.debug("Importing"+module_name)
imported_module=import_module("Ineruki.utils.filters."+module_name)
log.info("Filtersloaded!")


defregister(*args,cmds=None,f=None,allow_edited=True,allow_kwargs=False,**kwargs):
ifcmdsandtype(cmds)isstr:
cmds=[cmds]

register_kwargs={}

ifcmdsandnotf:
regex=r"\A^{}(".format("[!/]"ifALLOW_COMMANDS_FROM_ECelse"/")

if"not_forwarded"notinkwargsandALLOW_F_COMMANDSisFalse:
kwargs["not_forwarded"]=True

if"cmd_not_mono"notinkwargsandCMD_NOT_MONO:
kwargs["cmd_not_mono"]=True

foridx,cmdinenumerate(cmds):
ifcmdinREGISTRED_COMMANDS:
log.warn(f"Duplicationof/{cmd}command")
REGISTRED_COMMANDS.append(cmd)
regex+=cmd

ifnotidx==len(cmds)-1:
ifnotcmds[0]inCOMMANDS_ALIASES:
COMMANDS_ALIASES[cmds[0]]=[cmds[idx+1]]
else:
COMMANDS_ALIASES[cmds[0]].append(cmds[idx+1])
regex+="|"

if"disable_args"inkwargs:
delkwargs["disable_args"]
regex+=f")($|@{BOT_USERNAME}$)"
else:
regex+=f")(|@{BOT_USERNAME})(:?|$)"

register_kwargs["regexp"]=regex

eliff=="text":
register_kwargs["content_types"]=types.ContentTypes.TET

eliff=="welcome":
register_kwargs["content_types"]=types.ContentTypes.NEW_CHAT_MEMBERS

eliff=="leave":
register_kwargs["content_types"]=types.ContentTypes.LEFT_CHAT_MEMBER

eliff=="service":
register_kwargs["content_types"]=types.ContentTypes.NEW_CHAT_MEMBERS
eliff=="any":
register_kwargs["content_types"]=types.ContentTypes.ANY

log.debug(f"Registrednewhandler:<d><n>{str(register_kwargs)}</></>")

register_kwargs.update(kwargs)

defdecorator(func):
asyncdefnew_func(*def_args,**def_kwargs):
message=def_args[0]

ifcmds:
message.conf["cmds"]=cmds

ifallow_kwargsisFalse:
def_kwargs=dict()

withconfigure_scope()asscope:
parsed_update=parse_update(dict(message))
scope.set_extra("update",str(parsed_update))

ifDEBUG_MODE:
#log.debug('[*]Starting{}.'.format(func.__name__))
#log.debug('Event:\n'+str(message))
start=time.time()
awaitfunc(*def_args,**def_kwargs)
log.debug(
"[*]{}Time:{}sec.".format(func.__name__,time.time()-start)
)
else:
awaitfunc(*def_args,**def_kwargs)
raiseSkipHandler()

iff=="cb":
dp.register_callback_query_handler(new_func,*args,**register_kwargs)
else:
dp.register_message_handler(new_func,*args,**register_kwargs)
ifallow_editedisTrue:
dp.register_edited_message_handler(new_func,*args,**register_kwargs)

returndecorator
