#InerukiExamplepluginformat

##Basic:SimplePlugins
```python3

fromIneruki.decoratorimportregister
from.utils.disableimportdisableable_dec
from.utils.messageimportget_args_str

@register(cmds="Hi")
@disableable_dec("Hi")
asyncdef_(message):
j="Hellothere"
awaitmessage.reply(j)

__mod_name__="Hi"
__help__="""
<b>Hi</b>
-/hi:SayHelloThere
"""
```

##Basic:EnvVars
```python3
#Youcanimportenvlikethis.Ifconfigpresentautouseconfig

fromIneruki.decoratorimportregister
from.utils.disableimportdisableable_dec
from.utils.messageimportget_args_str
fromIneruki.configimportget_int_key,get_str_key

HI_STRING=get_str_key("HI_STRING",required=True)#String
MULTI=get_int_key("MULTI",required=True)#Intiger

@register(cmds="Hi")
@disableable_dec("Hi")
asyncdef_(message):
j=HI_STRING*MULTI
awaitmessage.reply(j)

__mod_name__="Hi"
__help__="""
<b>Hi</b>
-/hi:SayHelloThere
"""
```



##Advanced:Pyrogram
```python3
fromIneruki.function.pluginhelpersimportadmins_only
fromIneruki.services.pyrogramimportpbot

@pbot.on_message(filters.command("hi")&~filters.edited&~filters.bot)
@admins_only
asyncdefhmm(client,message):
j="Hellothere"
awaitmessage.reply(j)

__mod_name__="Hi"
__help__="""
<b>Hi</b>
-/hi:SayHelloThere
"""
```

##Advanced:Telethon
```python3

fromIneruki.services.telethonimporttbot
fromIneruki.services.eventsimportregister

@register(pattern="^/hi$")
asyncdefhmm(event):
j="Hellothere"
awaitevent.reply(j)

__mod_name__="Hi"
__help__="""
<b>Hi</b>
-/hi:SayHelloThere
"""
```
