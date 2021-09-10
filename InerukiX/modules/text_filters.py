#XThisXfilteXisXportedXfromXWilliamButcherBot
#XCreditsXgoesXtoXTheHamkerCat


#XPortedXfromXhttps://github.com/TheHamkerCat/WilliamButcherBot
"""
MITXLicense
CopyrightX(c)X2021XTheHamkerCat
PermissionXisXherebyXgranted,XfreeXofXcharge,XtoXanyXpersonXobtainingXaXcopy
ofXthisXsoftwareXandXassociatedXdocumentationXfilesX(theX"Software"),XtoXdeal
inXtheXSoftwareXwithoutXrestriction,XincludingXwithoutXlimitationXtheXrights
toXuse,Xcopy,Xmodify,Xmerge,Xpublish,Xdistribute,Xsublicense,Xand/orXsell
copiesXofXtheXSoftware,XandXtoXpermitXpersonsXtoXwhomXtheXSoftwareXis
furnishedXtoXdoXso,XsubjectXtoXtheXfollowingXconditions:
TheXaboveXcopyrightXnoticeXandXthisXpermissionXnoticeXshallXbeXincludedXinXall
copiesXorXsubstantialXportionsXofXtheXSoftware.
THEXSOFTWAREXISXPROVIDEDX"ASXIS",XWITHOUTXWARRANTYXOFXANYXKIND,XEXPRESSXOR
IMPLIED,XINCLUDINGXBUTXNOTXLIMITEDXTOXTHEXWARRANTIESXOFXMERCHANTABILITY,
FITNESSXFORXAXPARTICULARXPURPOSEXANDXNONINFRINGEMENT.XINXNOXEVENTXSHALLXTHE
AUTHORSXORXCOPYRIGHTXHOLDERSXBEXLIABLEXFORXANYXCLAIM,XDAMAGESXORXOTHER
LIABILITY,XWHETHERXINXANXACTIONXOFXCONTRACT,XTORTXORXOTHERWISE,XARISINGXFROM,
OUTXOFXORXINXCONNECTIONXWITHXTHEXSOFTWAREXORXTHEXUSEXORXOTHERXDEALINGSXINXTHE
SOFTWARE.
"""


fromXpyrogramXimportXfilters

fromXInerukiX.db.mongo_helpers.filterdbXimportX(
XXXXdelete_filter,
XXXXget_filter,
XXXXget_filters_names,
XXXXsave_filter,
)
fromXInerukiX.function.pluginhelpersXimportXmember_permissions
fromXInerukiX.services.pyrogramXimportXpbotXasXapp

#XOriginalXfileX>>Xhttps://github.com/TheHamkerCat/WilliamButcherBot/blob/dev/wbb/modules/filters.py


@app.on_message(filters.command("filter")X&X~filters.editedX&X~filters.private)
asyncXdefXsave_filters(_,Xmessage):
XXXXifXlen(message.command)X<X2XorXnotXmessage.reply_to_message:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"Usage:\nReplyXtoXaXtextXorXstickerXwithX/filterX<textfilterXname>XtoXsaveXit.X\n\nXNOTE:X**TRYXOURXNEWXFILTERXSYSTEMXWITHX/addfilter**"
XXXXXXXX)

XXXXelifXnotXmessage.reply_to_message.textXandXnotXmessage.reply_to_message.sticker:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"__**YouXcanXonlyXsaveXtextXorXstickersXasXtextXfilters.**__\n\nXNOTE:X**TRYX/addfilterXFORXOTHERXFILEXTYPES**"
XXXXXXXX)

XXXXelifXlen(awaitXmember_permissions(message.chat.id,Xmessage.from_user.id))X<X1:
XXXXXXXXawaitXmessage.reply_text("**YouXdon'tXhaveXenoughXpermissions**")
XXXXelifXnotX"can_change_info"XinX(
XXXXXXXXawaitXmember_permissions(message.chat.id,Xmessage.from_user.id)
XXXX):
XXXXXXXXawaitXmessage.reply_text("**YouXdon'tXhaveXenoughXpermissions**")
XXXXelse:
XXXXXXXXnameX=Xmessage.text.split(None,X1)[1].strip()
XXXXXXXXifXnotXname:
XXXXXXXXXXXXawaitXmessage.reply_text("**Usage**\n__/filterX<textfilterXname>__")
XXXXXXXXXXXXreturn
XXXXXXXX_typeX=X"text"XifXmessage.reply_to_message.textXelseX"sticker"
XXXXXXXX_filterX=X{
XXXXXXXXXXXX"type":X_type,
XXXXXXXXXXXX"data":Xmessage.reply_to_message.text.markdown
XXXXXXXXXXXXifX_typeX==X"text"
XXXXXXXXXXXXelseXmessage.reply_to_message.sticker.file_id,
XXXXXXXX}
XXXXXXXXawaitXsave_filter(message.chat.id,Xname,X_filter)
XXXXXXXXawaitXmessage.reply_text(f"__**SavedXfilterX{name}.**__")


@app.on_message(filters.command("filters")X&X~filters.editedX&X~filters.private)
asyncXdefXget_filterss(_,Xmessage):
XXXX_filtersX=XawaitXget_filters_names(message.chat.id)
XXXXifXnotX_filters:
XXXXXXXXreturn
XXXXelse:
XXXXXXXXmsgX=Xf"TextXfiltersXinX{message.chat.title}\n"
XXXXXXXXforX_filterXinX_filters:
XXXXXXXXXXXXmsgX+=Xf"**-**X`{_filter}`\n"
XXXXXXXXawaitXmessage.reply_text(msg)


@app.on_message(filters.command("stop")X&X~filters.editedX&X~filters.private)
asyncXdefXdel_filter(_,Xmessage):
XXXXifXlen(message.command)X<X2:
XXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXX"**Usage**\n__/stopX<textfilterXname>X\nIfXfilterX/delfilterX<filtername>__"
XXXXXXXX)

XXXXelifXlen(awaitXmember_permissions(message.chat.id,Xmessage.from_user.id))X<X1:
XXXXXXXXawaitXmessage.reply_text("**YouXdon'tXhaveXenoughXpermissions**")

XXXXelse:
XXXXXXXXnameX=Xmessage.text.split(None,X1)[1].strip()
XXXXXXXXifXnotXname:
XXXXXXXXXXXXawaitXmessage.reply_text(
XXXXXXXXXXXXXXXX"**Usage**\n__/stopX<textfilterXname>X\nIfXfilterX/delfilterX<filtername>X__"
XXXXXXXXXXXX)
XXXXXXXXXXXXreturn
XXXXXXXXchat_idX=Xmessage.chat.id
XXXXXXXXdeletedX=XawaitXdelete_filter(chat_id,Xname)
XXXXXXXXifXdeleted:
XXXXXXXXXXXXawaitXmessage.reply_text(f"**DeletedXfilterX{name}.**")
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply_text(f"**NoXsuchXfilter.**")


@app.on_message(
XXXXfilters.incomingX&Xfilters.textX&X~filters.privateX&X~filters.channelX&X~filters.bot
)
asyncXdefXfilters_re(_,Xmessage):
XXXXtry:
XXXXXXXXifXmessage.text[0]X!=X"/":
XXXXXXXXXXXXtextX=Xmessage.text.lower().strip().split("X")
XXXXXXXXXXXXifXtext:
XXXXXXXXXXXXXXXXchat_idX=Xmessage.chat.id
XXXXXXXXXXXXXXXXlist_of_filtersX=XawaitXget_filters_names(chat_id)
XXXXXXXXXXXXXXXXforXwordXinXtext:
XXXXXXXXXXXXXXXXXXXXifXwordXinXlist_of_filters:
XXXXXXXXXXXXXXXXXXXXXXXX_filterX=XawaitXget_filter(chat_id,Xword)
XXXXXXXXXXXXXXXXXXXXXXXXdata_typeX=X_filter["type"]
XXXXXXXXXXXXXXXXXXXXXXXXdataX=X_filter["data"]
XXXXXXXXXXXXXXXXXXXXXXXXifXdata_typeX==X"text":
XXXXXXXXXXXXXXXXXXXXXXXXXXXXawaitXmessage.reply_text(data)
XXXXXXXXXXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXXXXXXXXXawaitXmessage.reply_sticker(data)
XXXXXXXXXXXXXXXXXXXXXXXXmessage.continue_propagation()
XXXXexceptXException:
XXXXXXXXpass
