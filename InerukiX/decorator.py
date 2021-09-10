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

importXtime
fromXimportlibXimportXimport_module

fromXaiogramXimportXtypes
fromXaiogram.dispatcher.handlerXimportXSkipHandler
fromXsentry_sdkXimportXconfigure_scope

fromXInerukiXXimportXBOT_USERNAME,Xdp
fromXInerukiX.configXimportXget_bool_key
fromXInerukiX.modules.errorXimportXparse_update
fromXInerukiX.utils.filtersXimportXALL_FILTERS
fromXInerukiX.utils.loggerXimportXlog

DEBUG_MODEX=Xget_bool_key("DEBUG_MODE")
ALLOW_F_COMMANDSX=Xget_bool_key("ALLOW_FORWARDS_COMMANDS")
ALLOW_COMMANDS_FROM_EXCX=Xget_bool_key("ALLOW_EXCEL")
CMD_NOT_MONOX=Xget_bool_key("DISALLOW_MONO_CMDS")

REGISTRED_COMMANDSX=X[]
COMMANDS_ALIASESX=X{}

#XImportXfilters
log.info("FiltersXtoXload:X%s",Xstr(ALL_FILTERS))
forXmodule_nameXinXALL_FILTERS:
XXXXlog.debug("ImportingX"X+Xmodule_name)
XXXXimported_moduleX=Ximport_module("InerukiX.utils.filters."X+Xmodule_name)
log.info("FiltersXloaded!")


defXregister(*args,Xcmds=None,Xf=None,Xallow_edited=True,Xallow_kwargs=False,X**kwargs):
XXXXifXcmdsXandXtype(cmds)XisXstr:
XXXXXXXXcmdsX=X[cmds]

XXXXregister_kwargsX=X{}

XXXXifXcmdsXandXnotXf:
XXXXXXXXregexX=Xr"\A^{}(".format("[!/]"XifXALLOW_COMMANDS_FROM_EXCXelseX"/")

XXXXXXXXifX"not_forwarded"XnotXinXkwargsXandXALLOW_F_COMMANDSXisXFalse:
XXXXXXXXXXXXkwargs["not_forwarded"]X=XTrue

XXXXXXXXifX"cmd_not_mono"XnotXinXkwargsXandXCMD_NOT_MONO:
XXXXXXXXXXXXkwargs["cmd_not_mono"]X=XTrue

XXXXXXXXforXidx,XcmdXinXenumerate(cmds):
XXXXXXXXXXXXifXcmdXinXREGISTRED_COMMANDS:
XXXXXXXXXXXXXXXXlog.warn(f"DuplicationXofX/{cmd}Xcommand")
XXXXXXXXXXXXREGISTRED_COMMANDS.append(cmd)
XXXXXXXXXXXXregexX+=Xcmd

XXXXXXXXXXXXifXnotXidxX==Xlen(cmds)X-X1:
XXXXXXXXXXXXXXXXifXnotXcmds[0]XinXCOMMANDS_ALIASES:
XXXXXXXXXXXXXXXXXXXXCOMMANDS_ALIASES[cmds[0]]X=X[cmds[idxX+X1]]
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXCOMMANDS_ALIASES[cmds[0]].append(cmds[idxX+X1])
XXXXXXXXXXXXXXXXregexX+=X"|"

XXXXXXXXifX"disable_args"XinXkwargs:
XXXXXXXXXXXXdelXkwargs["disable_args"]
XXXXXXXXXXXXregexX+=Xf")($|@{BOT_USERNAME}$)"
XXXXXXXXelse:
XXXXXXXXXXXXregexX+=Xf")(|@{BOT_USERNAME})(:?X|$)"

XXXXXXXXregister_kwargs["regexp"]X=Xregex

XXXXelifXfX==X"text":
XXXXXXXXregister_kwargs["content_types"]X=Xtypes.ContentTypes.TEXT

XXXXelifXfX==X"welcome":
XXXXXXXXregister_kwargs["content_types"]X=Xtypes.ContentTypes.NEW_CHAT_MEMBERS

XXXXelifXfX==X"leave":
XXXXXXXXregister_kwargs["content_types"]X=Xtypes.ContentTypes.LEFT_CHAT_MEMBER

XXXXelifXfX==X"service":
XXXXXXXXregister_kwargs["content_types"]X=Xtypes.ContentTypes.NEW_CHAT_MEMBERS
XXXXelifXfX==X"any":
XXXXXXXXregister_kwargs["content_types"]X=Xtypes.ContentTypes.ANY

XXXXlog.debug(f"RegistredXnewXhandler:X<d><n>{str(register_kwargs)}</></>")

XXXXregister_kwargs.update(kwargs)

XXXXdefXdecorator(func):
XXXXXXXXasyncXdefXnew_func(*def_args,X**def_kwargs):
XXXXXXXXXXXXmessageX=Xdef_args[0]

XXXXXXXXXXXXifXcmds:
XXXXXXXXXXXXXXXXmessage.conf["cmds"]X=Xcmds

XXXXXXXXXXXXifXallow_kwargsXisXFalse:
XXXXXXXXXXXXXXXXdef_kwargsX=Xdict()

XXXXXXXXXXXXwithXconfigure_scope()XasXscope:
XXXXXXXXXXXXXXXXparsed_updateX=Xparse_update(dict(message))
XXXXXXXXXXXXXXXXscope.set_extra("update",Xstr(parsed_update))

XXXXXXXXXXXXifXDEBUG_MODE:
XXXXXXXXXXXXXXXX#Xlog.debug('[*]XStartingX{}.'.format(func.__name__))
XXXXXXXXXXXXXXXX#Xlog.debug('Event:X\n'X+Xstr(message))
XXXXXXXXXXXXXXXXstartX=Xtime.time()
XXXXXXXXXXXXXXXXawaitXfunc(*def_args,X**def_kwargs)
XXXXXXXXXXXXXXXXlog.debug(
XXXXXXXXXXXXXXXXXXXX"[*]X{}XTime:X{}Xsec.".format(func.__name__,Xtime.time()X-Xstart)
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXawaitXfunc(*def_args,X**def_kwargs)
XXXXXXXXXXXXraiseXSkipHandler()

XXXXXXXXifXfX==X"cb":
XXXXXXXXXXXXdp.register_callback_query_handler(new_func,X*args,X**register_kwargs)
XXXXXXXXelse:
XXXXXXXXXXXXdp.register_message_handler(new_func,X*args,X**register_kwargs)
XXXXXXXXXXXXifXallow_editedXisXTrue:
XXXXXXXXXXXXXXXXdp.register_edited_message_handler(new_func,X*args,X**register_kwargs)

XXXXreturnXdecorator
