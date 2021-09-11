#Copyright(C)2021errorshivansh


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

importjson

importrequests
fromgoogle_trans_newimportgoogle_translator
fromPyDictionaryimportPyDictionary
fromtelethonimport*
fromtelethon.tl.typesimport*

fromIneruki.services.eventsimportregister

API_KEY="6ae0c3a0-afdc-4532-a810-82ded0054236"
URL="http://services.gingersoftware.com/Ginger/correct/json/GingerTheText"


@register(pattern="^/tr?(.*)")
asyncdef_(event):
input_str=event.pattern_match.group(1)
ifevent.reply_to_msg_id:
previous_message=awaitevent.get_reply_message()
text=previous_message.message
lan=input_stror"en"
elif"|"ininput_str:
lan,text=input_str.split("|")
else:
awaitevent.reply(
"`/tr<LanguageCode>`asreplytoamessageor`/tr<LanguageCode>|<text>`"
)
return
text=text.strip()
lan=lan.strip()
translator=google_translator()
try:
translated=translator.translate(text,lang_tgt=lan)
after_tr_text=translated
detect_result=translator.detect(text)
output_str=("**TRANSLATEDSuccesfully**from{}to{}\n\n""{}").format(
detect_result[0],lan,after_tr_text
)
awaitevent.reply(output_str)
exceptExceptionasexc:
awaitevent.reply(str(exc))


@register(pattern="^/spell(?:|$)(.*)")
asyncdef_(event):
ctext=awaitevent.get_reply_message()
msg=ctext.text
#print(msg)
params=dict(lang="US",clientVersion="2.0",apiKey=API_KEY,text=msg)

res=requests.get(URL,params=params)
changes=json.loads(res.text).get("LightGingerTheTextResult")
curr_string=""
prev_end=0

forchangeinchanges:
start=change.get("From")
end=change.get("To")+1
suggestions=change.get("Suggestions")
ifsuggestions:
sugg_str=suggestions[0].get("Text")
curr_string+=msg[prev_end:start]+sugg_str
prev_end=end

curr_string+=msg[prev_end:]
awaitevent.reply(curr_string)


dictionary=PyDictionary()


@register(pattern="^/define")
asyncdef_(event):
text=event.text[len("/define"):]
word=f"{text}"
let=dictionary.meaning(word)
set=str(let)
jet=set.replace("{","")
net=jet.replace("}","")
got=net.replace("'","")
awaitevent.reply(got)


@register(pattern="^/synonyms")
asyncdef_(event):
text=event.text[len("/synonyms"):]
word=f"{text}"
let=dictionary.synonym(word)
set=str(let)
jet=set.replace("{","")
net=jet.replace("}","")
got=net.replace("'","")
awaitevent.reply(got)


@register(pattern="^/antonyms")
asyncdef_(event):
text=message.text[len("/antonyms"):]
word=f"{text}"
let=dictionary.antonym(word)
set=str(let)
jet=set.replace("{","")
net=jet.replace("}","")
got=net.replace("'","")
awaitevent.reply(got)


__help__="""
-/tr<i>languagecode</i>or/tr<i>languagecode</i>,<i>text</i>:Typeinreplytoamessageor(/tr<i>languagecode</i>,<i>text</i>)togetit'stranslationinthedestinationlanguage
-/define<i>text</i>:Typethewordorexpressionyouwanttosearch\nForexample/definelesbian
-/spell:whilereplyingtoamessage,willreplywithagrammarcorrectedversion
-/forbesify:Correctyourpunctuationsbetterusetheadvangedspellmodule
-/synonyms<i>word</i>:Findthesynonymsofaword
-/antonyms<i>word</i>:Findtheantonymsofaword
"""

__mod_name__="Lang-Tools"
