#XInerukiXXExampleXpluginXformat

##XBasic:XSimpleXPlugins
```python3

fromXInerukiX.decoratorXimportXregister
fromX.utils.disableXimportXdisableable_dec
fromX.utils.messageXimportXget_args_str

@register(cmds="Hi")
@disableable_dec("Hi")
asyncXdefX_(message):
XXXXjX=X"HelloXthere"
XXXXawaitXmessage.reply(j)
XXXX
__mod_name__X=X"Hi"
__help__X=X"""
<b>Hi</b>
-X/hi:XSayXHelloXThere
"""
```

##XBasic:XEnvXVars
```python3
#XYouXcanXimportXenvXlikeXthis.XIfXconfigXpresentXautoXuseXconfig

fromXInerukiX.decoratorXimportXregister
fromX.utils.disableXimportXdisableable_dec
fromX.utils.messageXimportXget_args_str
fromXInerukiX.configXimportXget_int_key,Xget_str_key

HI_STRINGX=Xget_str_key("HI_STRING",Xrequired=True)X#XString
MULTIX=Xget_int_key("MULTI",Xrequired=True)X#Intiger

@register(cmds="Hi")
@disableable_dec("Hi")
asyncXdefX_(message):
XXXXjX=XHI_STRING*MULTI
XXXXawaitXmessage.reply(j)
XXXX
__mod_name__X=X"Hi"
__help__X=X"""
<b>Hi</b>
-X/hi:XSayXHelloXThere
"""
```



##XAdvanced:XPyrogram
```python3
fromXInerukiX.function.pluginhelpersXimportXadmins_only
fromXInerukiX.services.pyrogramXimportXpbot

@pbot.on_message(filters.command("hi")X&X~filters.editedX&X~filters.bot)
@admins_only
asyncXdefXhmm(client,Xmessage):
XXXXjX=X"HelloXthere"
XXXXawaitXmessage.reply(j)
XXXX
__mod_name__X=X"Hi"
__help__X=X"""
<b>Hi</b>
-X/hi:XSayXHelloXThere
"""
```

##XAdvanced:XTelethon
```python3

fromXInerukiX.services.telethonXimportXtbot
fromXInerukiX.services.eventsXimportXregister

@register(pattern="^/hi$")
asyncXdefXhmm(event):
XXXXjX=X"HelloXthere"
XXXXawaitXevent.reply(j)
XXXX
__mod_name__X=X"Hi"
__help__X=X"""
<b>Hi</b>
-X/hi:XSayXHelloXThere
"""
```
