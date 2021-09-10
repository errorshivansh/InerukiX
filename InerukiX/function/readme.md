#XHereXweXdefineXfunctions

##XEssentials
###XImportingXPyrogramXadminXcheck
```python3
fromXInerukiX.function.pluginhelpersXimportXadmins_only

@admins_only
```

###XGettingXtextXfromXcmd
```python3
fromXInerukiX.function.pluginhelpersXimportXget_text

asyncXdefXhi(client,message):
XXargsX=Xget_text(message)
```

###XEditXorXreply
```python3
fromXInerukiX.function.pluginhelpersXimportXedit_or_reply

asyncXdefXhi(client,message):
XXawaitXedit_or_reply("Hi")
```
##XSOMEXFUNCTIONSXAREXCOPIEDXFROMXhttps://github.com/TheHamkerCat/WilliamButcherBot
##XANDXSOMEXFROMXFRIDAYXUSERBOT
