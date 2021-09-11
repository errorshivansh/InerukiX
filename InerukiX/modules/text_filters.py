#ThisfilteisportedfromWilliamButcherBot
#CreditsgoestoTheHamkerCat


#Portedfromhttps://github.com/TheHamkerCat/WilliamButcherBot
"""
MITLicense
Copyright(c)2021TheHamkerCat
Permissionisherebygranted,freeofcharge,toanypersonobtainingacopy
ofthissoftwareandassociateddocumentationfiles(the"Software"),todeal
intheSoftwarewithoutrestriction,includingwithoutlimitationtherights
touse,copy,modify,merge,publish,distribute,sublicense,and/orsell
copiesoftheSoftware,andtopermitpersonstowhomtheSoftwareis
furnishedtodoso,subjecttothefollowingconditions:
Theabovecopyrightnoticeandthispermissionnoticeshallbeincludedinall
copiesorsubstantialportionsoftheSoftware.
THESOFTWAREISPROVIDED"ASIS",WITHOUTWARRANTYOFANYKIND,EPRESSOR
IMPLIED,INCLUDINGBUTNOTLIMITEDTOTHEWARRANTIESOFMERCHANTABILITY,
FITNESSFORAPARTICULARPURPOSEANDNONINFRINGEMENT.INNOEVENTSHALLTHE
AUTHORSORCOPYRIGHTHOLDERSBELIABLEFORANYCLAIM,DAMAGESOROTHER
LIABILITY,WHETHERINANACTIONOFCONTRACT,TORTOROTHERWISE,ARISINGFROM,
OUTOFORINCONNECTIONWITHTHESOFTWAREORTHEUSEOROTHERDEALINGSINTHE
SOFTWARE.
"""


frompyrogramimportfilters

fromIneruki.db.mongo_helpers.filterdbimport(
delete_filter,
get_filter,
get_filters_names,
save_filter,
)
fromIneruki.function.pluginhelpersimportmember_permissions
fromIneruki.services.pyrogramimportpbotasapp

#Originalfile>>https://github.com/TheHamkerCat/WilliamButcherBot/blob/dev/wbb/modules/filters.py


@app.on_message(filters.command("filter")&~filters.edited&~filters.private)
asyncdefsave_filters(_,message):
iflen(message.command)<2ornotmessage.reply_to_message:
awaitmessage.reply_text(
"Usage:\nReplytoatextorstickerwith/filter<textfiltername>tosaveit.\n\nNOTE:**TRYOURNEWFILTERSYSTEMWITH/addfilter**"
)

elifnotmessage.reply_to_message.textandnotmessage.reply_to_message.sticker:
awaitmessage.reply_text(
"__**Youcanonlysavetextorstickersastextfilters.**__\n\nNOTE:**TRY/addfilterFOROTHERFILETYPES**"
)

eliflen(awaitmember_permissions(message.chat.id,message.from_user.id))<1:
awaitmessage.reply_text("**Youdon'thaveenoughpermissions**")
elifnot"can_change_info"in(
awaitmember_permissions(message.chat.id,message.from_user.id)
):
awaitmessage.reply_text("**Youdon'thaveenoughpermissions**")
else:
name=message.text.split(None,1)[1].strip()
ifnotname:
awaitmessage.reply_text("**Usage**\n__/filter<textfiltername>__")
return
_type="text"ifmessage.reply_to_message.textelse"sticker"
_filter={
"type":_type,
"data":message.reply_to_message.text.markdown
if_type=="text"
elsemessage.reply_to_message.sticker.file_id,
}
awaitsave_filter(message.chat.id,name,_filter)
awaitmessage.reply_text(f"__**Savedfilter{name}.**__")


@app.on_message(filters.command("filters")&~filters.edited&~filters.private)
asyncdefget_filterss(_,message):
_filters=awaitget_filters_names(message.chat.id)
ifnot_filters:
return
else:
msg=f"Textfiltersin{message.chat.title}\n"
for_filterin_filters:
msg+=f"**-**`{_filter}`\n"
awaitmessage.reply_text(msg)


@app.on_message(filters.command("stop")&~filters.edited&~filters.private)
asyncdefdel_filter(_,message):
iflen(message.command)<2:
awaitmessage.reply_text(
"**Usage**\n__/stop<textfiltername>\nIffilter/delfilter<filtername>__"
)

eliflen(awaitmember_permissions(message.chat.id,message.from_user.id))<1:
awaitmessage.reply_text("**Youdon'thaveenoughpermissions**")

else:
name=message.text.split(None,1)[1].strip()
ifnotname:
awaitmessage.reply_text(
"**Usage**\n__/stop<textfiltername>\nIffilter/delfilter<filtername>__"
)
return
chat_id=message.chat.id
deleted=awaitdelete_filter(chat_id,name)
ifdeleted:
awaitmessage.reply_text(f"**Deletedfilter{name}.**")
else:
awaitmessage.reply_text(f"**Nosuchfilter.**")


@app.on_message(
filters.incoming&filters.text&~filters.private&~filters.channel&~filters.bot
)
asyncdeffilters_re(_,message):
try:
ifmessage.text[0]!="/":
text=message.text.lower().strip().split("")
iftext:
chat_id=message.chat.id
list_of_filters=awaitget_filters_names(chat_id)
forwordintext:
ifwordinlist_of_filters:
_filter=awaitget_filter(chat_id,word)
data_type=_filter["type"]
data=_filter["data"]
ifdata_type=="text":
awaitmessage.reply_text(data)
else:
awaitmessage.reply_sticker(data)
message.continue_propagation()
exceptException:
pass
