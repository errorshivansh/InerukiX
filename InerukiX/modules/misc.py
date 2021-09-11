#Copyright(C)2018-2020MrYacha.Allrightsreserved.SourcecodeavailableundertheAGPL.
#Copyright(C)2021errorshivansh
#Copyright(C)2020InukaAsith

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


importre
fromcontextlibimportsuppress
fromdatetimeimportdatetime

importwikipedia

#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<http://www.gnu.org/licenses/>.
fromaiogram.typesimportInlineKeyboardButton,InlineKeyboardMarkup,Message
fromaiogram.utils.exceptionsimport(
BadRequest,
MessageNotModified,
MessageToDeleteNotFound,
)

fromIneruki.decoratorimportregister

from.utils.disableimportdisableable_dec
from.utils.httpximporthttp
from.utils.languageimportget_strings_dec
from.utils.messageimportget_args_str
from.utils.notesimportget_parsed_note_list,send_note,t_unparse_note_item
from.utils.user_detailsimportis_user_admin


@register(cmds="buttonshelp",no_args=True,only_pm=True)
asyncdefbuttons_help(message):
awaitmessage.reply(
"""
<b>Buttons:</b>
Hereyouwillknowhowtosetupbuttonsinyournote,welcomenote,etc...

Therearedifferenttypesofbuttons!

<i>DuetocurrentImplementationaddinginvalidbuttonsyntaxtoyournotewillraiseerror!Thiswillbefixedinnextmajorversion.</i>

<b>Didyouknow?</b>
Youcouldsavebuttonsinsamerowusingthissyntax
<code>[Button](btn{mode}:{argsifany}:same)</code>
(adding<code>:same</code>likethatdoesthejob.)

<b>ButtonNote:</b>
<i>Don'tconfusethistitlewithnoteswithbuttons</i>😜

Thistypesofbuttonwillallowyoutoshowspecificnotestouserswhentheyclickonbuttons!

Youcansavenotewithbuttonnotewithoutanyhasslebyaddingbelowlinetoyournote(Don'tforgettoreplace<code>notename</code>accordingtoyou😀)

<code>[ButtonName](btnnote:notename)</code>

<b>URLButton:</b>
Ahasyouguessed!ThismethodisusedtoaddURLbuttontoyournote.Withthisyoucanredirectuserstoyourwebsiteorevenredirectingthemtoanychannel,chatormessages!

YoucanaddURLbuttonbyaddingfollowingsyntaxtoyournote

<code>[ButtonName](btnurl:https://your.link.here)</code>

<b>Buttonrules:</b>
Wellinv2weintroducedsomechanges,rulesarenowsavedseperatelyunlikesavedasnotebeforev2soitrequireseperatebuttonmethod!

YoucanusethisbuttonmethodforincludingRulesbuttoninyourwelcomemessages,filtersetc..literallyanywhere*

Youusethisbuttonwithaddingfollowingsyntaxtoyourmessagewhichsupportformatting!
<code>[ButtonName](btnrules)</code>
"""
)


@register(cmds="variableshelp",no_args=True,only_pm=True)
asyncdefbuttons_help(message):
awaitmessage.reply(
"""
<b>Variables:</b>
Variablesarespecialwordswhichwillbereplacedbyactualinfo

<b>Avaiblevariables:</b>
<code>{first}</code>:User'sfirstname
<code>{last}</code>:User'slastname
<code>{fullname}</code>:User'sfullname
<code>{id}</code>:User'sID
<code>{mention}</code>:Mentiontheuserusingfirstname
<code>{username}</code>:Gettheusername,ifuserdon'thaveusernamewillbereturnedmention
<code>{chatid}</code>:Chat'sID
<code>{chatname}</code>:Chatname
<code>{chatnick}</code>:Chatusername
"""
)


@register(cmds="wiki")
@disableable_dec("wiki")
asyncdefwiki(message):
args=get_args_str(message)
wikipedia.set_lang("en")
try:
pagewiki=wikipedia.page(args)
exceptwikipedia.exceptions.PageErrorase:
awaitmessage.reply(f"Noresultsfound!\nError:<code>{e}</code>")
return
exceptwikipedia.exceptions.DisambiguationErrorasrefer:
refer=str(refer).split("\n")
iflen(refer)>=6:
batas=6
else:
batas=len(refer)
text=""
forxinrange(batas):
ifx==0:
text+=refer[x]+"\n"
else:
text+="-`"+refer[x]+"`\n"
awaitmessage.reply(text)
return
exceptIndexError:
msg.reply_text("Writeamessagetosearchfromwikipediasources.")
return
title=pagewiki.title
summary=pagewiki.summary
button=InlineKeyboardMarkup().add(
InlineKeyboardButton("🔧MoreInfo...",url=wikipedia.page(args).url)
)
awaitmessage.reply(
("Theresultof{}is:\n\n<b>{}</b>\n{}").format(args,title,summary),
reply_markup=button,
)


@register(cmds="github")
@disableable_dec("github")
asyncdefgithub(message):
text=message.text[len("/github"):]
response=awaithttp.get(f"https://api.github.com/users/{text}")
usr=response.json()

ifusr.get("login"):
text=f"<b>Username:</b><ahref='https://github.com/{usr['login']}'>{usr['login']}</a>"

whitelist=[
"name",
"id",
"type",
"location",
"blog",
"bio",
"followers",
"following",
"hireable",
"public_gists",
"public_repos",
"email",
"company",
"updated_at",
"created_at",
]

difnames={
"id":"AccountID",
"type":"Accounttype",
"created_at":"Accountcreatedat",
"updated_at":"Lastupdated",
"public_repos":"PublicRepos",
"public_gists":"PublicGists",
}

goaway=[None,0,"null",""]

forx,yinusr.items():
ifxinwhitelist:
x=difnames.get(x,x.title())

ifxin("Accountcreatedat","Lastupdated"):
y=datetime.strptime(y,"%Y-%m-%dT%H:%M:%SZ")

ifynotingoaway:
ifx=="Blog":
x="Website"
y=f"<ahref='{y}'>Here!</a>"
text+="\n<b>{}:</b>{}".format(x,y)
else:
text+="\n<b>{}:</b><code>{}</code>".format(x,y)
reply_text=text
else:
reply_text="Usernotfound.Makesureyouenteredvalidusername!"
awaitmessage.reply(reply_text,disable_web_page_preview=True)


@register(cmds="ip")
@disableable_dec("ip")
asyncdefip(message):
try:
ip=message.text.split(maxsplit=1)[1]
exceptIndexError:
awaitmessage.reply(f"Apparentlyyouforgotsomething!")
return

response=awaithttp.get(f"http://ip-api.com/json/{ip}")
ifresponse.status_code==200:
lookup_json=response.json()
else:
awaitmessage.reply(
f"Anerroroccurredwhenlookingfor<b>{ip}</b>:<b>{response.status_code}</b>"
)
return

fixed_lookup={}

forkey,valueinlookup_json.items():
special={
"lat":"Latitude",
"lon":"Longitude",
"isp":"ISP",
"as":"AS",
"asname":"ASname",
}
ifkeyinspecial:
fixed_lookup[special[key]]=str(value)
continue

key=re.sub(r"([a-z])([A-Z])",r"\g<1>\g<2>",key)
key=key.capitalize()

ifnotvalue:
value="None"

fixed_lookup[key]=str(value)

text=""

forkey,valueinfixed_lookup.items():
text=text+f"<b>{key}:</b><code>{value}</code>\n"

awaitmessage.reply(text)


@register(cmds="cancel",state="*",allow_kwargs=True)
asyncdefcancel_handle(message,state,**kwargs):
awaitstate.finish()
awaitmessage.reply("Cancelled.")


asyncdefdelmsg_filter_handle(message,chat,data):
ifawaitis_user_admin(data["chat_id"],message.from_user.id):
return
withsuppress(MessageToDeleteNotFound):
awaitmessage.delete()


asyncdefreplymsg_filter_handler(message,chat,data):
text,kwargs=awaitt_unparse_note_item(
message,data["reply_text"],chat["chat_id"]
)
kwargs["reply_to"]=message.message_id
withsuppress(BadRequest):
awaitsend_note(chat["chat_id"],text,**kwargs)


@get_strings_dec("misc")
asyncdefreplymsg_setup_start(message,strings):
withsuppress(MessageNotModified):
awaitmessage.edit_text(strings["send_text"])


asyncdefreplymsg_setup_finish(message,data):
reply_text=awaitget_parsed_note_list(
message,allow_reply_message=False,split_args=-1
)
return{"reply_text":reply_text}


@get_strings_dec("misc")
asyncdefcustomise_reason_start(message:Message,strings:dict):
awaitmessage.reply(strings["send_customised_reason"])


@get_strings_dec("misc")
asyncdefcustomise_reason_finish(message:Message,_:dict,strings:dict):
ifmessage.textisNone:
awaitmessage.reply(strings["expected_text"])
returnFalse
elifmessage.textin{"None"}:
return{"reason":None}
return{"reason":message.text}


__filters__={
"delete_message":{
"title":{"module":"misc","string":"delmsg_filter_title"},
"handle":delmsg_filter_handle,
"del_btn_name":lambdamsg,data:f"Delmessage:{data['handler']}",
},
"reply_message":{
"title":{"module":"misc","string":"replymsg_filter_title"},
"handle":replymsg_filter_handler,
"setup":{"start":replymsg_setup_start,"finish":replymsg_setup_finish},
"del_btn_name":lambdamsg,data:f"Replyto{data['handler']}:\"{data['reply_text'].get('text','None')}\"",
},
}
