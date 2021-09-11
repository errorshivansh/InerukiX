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


importhtml

importtldextract
fromtelethonimportevents,types
fromtelethon.tlimportfunctions

importIneruki.services.sql.urlblacklist_sqlasurlsql
fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbot


asyncdefcan_change_info(message):
result=awaittbot(
functions.channels.GetParticipantRequest(
channel=message.chat_id,
user_id=message.sender_id,
)
)
p=result.participant
returnisinstance(p,types.ChannelParticipantCreator)or(
isinstance(p,types.ChannelParticipantAdmin)andp.admin_rights.change_info
)


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):
returnisinstance(
(
awaittbot(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
ifisinstance(chat,types.InputPeerUser):
returnTrue


@register(pattern="^/addurl")
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.is_private:
return
ifevent.is_group:
ifawaitcan_change_info(message=event):
pass
else:
return
chat=event.chat
urls=event.text.split(None,1)
iflen(urls)>1:
urls=urls[1]
to_blacklist=list({uri.strip()foruriinurls.split("\n")ifuri.strip()})
blacklisted=[]

foruriinto_blacklist:
extract_url=tldextract.extract(uri)
ifextract_url.domainandextract_url.suffix:
blacklisted.append(extract_url.domain+"."+extract_url.suffix)
urlsql.blacklist_url(
chat.id,extract_url.domain+"."+extract_url.suffix
)

iflen(to_blacklist)==1:
extract_url=tldextract.extract(to_blacklist[0])
ifextract_url.domainandextract_url.suffix:
awaitevent.reply(
"Added<code>{}</code>domaintotheblacklist!".format(
html.escape(extract_url.domain+"."+extract_url.suffix)
),
parse_mode="html",
)
else:
awaitevent.reply("Youaretryingtoblacklistaninvalidurl")
else:
awaitevent.reply(
"Added<code>{}</code>domainstotheblacklist.".format(
len(blacklisted)
),
parse_mode="html",
)
else:
awaitevent.reply("Tellmewhichurlsyouwouldliketoaddtotheblacklist.")


@register(pattern="^/delurl")
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.is_private:
return
ifevent.is_group:
ifawaitcan_change_info(message=event):
pass
else:
return
chat=event.chat
urls=event.text.split(None,1)

iflen(urls)>1:
urls=urls[1]
to_unblacklist=list({uri.strip()foruriinurls.split("\n")ifuri.strip()})
unblacklisted=0
foruriinto_unblacklist:
extract_url=tldextract.extract(uri)
success=urlsql.rm_url_from_blacklist(
chat.id,extract_url.domain+"."+extract_url.suffix
)
ifsuccess:
unblacklisted+=1

iflen(to_unblacklist)==1:
ifunblacklisted:
awaitevent.reply(
"Removed<code>{}</code>fromtheblacklist!".format(
html.escape(to_unblacklist[0])
),
parse_mode="html",
)
else:
awaitevent.reply("Thisisn'tablacklisteddomain...!")
elifunblacklisted==len(to_unblacklist):
awaitevent.reply(
"Removed<code>{}</code>domainsfromtheblacklist.".format(
unblacklisted
),
parse_mode="html",
)
elifnotunblacklisted:
awaitevent.reply("Noneofthesedomainsexist,sotheyweren'tremoved.")
else:
awaitevent.reply(
"Removed<code>{}</code>domainsfromtheblacklist.{}didnotexist,sowerenotremoved.".format(
unblacklisted,len(to_unblacklist)-unblacklisted
),
parse_mode="html",
)
else:
awaitevent.reply(
"Tellmewhichdomainsyouwouldliketoremovefromtheblacklist."
)


@tbot.on(events.NewMessage(incoming=True))
asyncdefon_url_message(event):
ifevent.is_private:
return
chat=event.chat
extracted_domains=[]
for(ent,txt)inevent.get_entities_text():
ifent.offset!=0:
break
ifisinstance(ent,types.MessageEntityUrl):
url=txt
extract_url=tldextract.extract(url)
extracted_domains.append(extract_url.domain+"."+extract_url.suffix)
forurlinurlsql.get_blacklisted_urls(chat.id):
ifurlinextracted_domains:
try:
awaitevent.delete()
except:
return


@register(pattern="^/geturl$")
asyncdef_(event):
ifevent.fwd_from:
return
ifevent.is_private:
return
ifevent.is_group:
ifawaitcan_change_info(message=event):
pass
else:
return
chat=event.chat
base_string="Current<b>blacklisted</b>domains:\n"
blacklisted=urlsql.get_blacklisted_urls(chat.id)
ifnotblacklisted:
awaitevent.reply("Therearenoblacklisteddomainshere!")
return
fordomaininblacklisted:
base_string+="-<code>{}</code>\n".format(domain)
awaitevent.reply(base_string,parse_mode="html")


__help__="""
<b>Ineruki'sfiltersaretheblacklisttoo</b>
-/addfilter[trigger]Selectaction:blackliststhetrigger
-/delfilter[trigger]:stopblacklistingacertainblacklisttrigger
-/filters:listallactiveblacklistfilters

<b>UrlBlacklist</B>
-/geturl:Viewthecurrentblacklistedurls
-/addurl[urls]:Addadomaintotheblacklist.Thebotwillautomaticallyparsetheurl.
-/delurl[urls]:Removeurlsfromtheblacklist.
<b>Example:</b>
-/addblacklisttheadminssuck:Thiswillremove"theadminssuck"everytimesomenon-admintypesit
-/addurlbit.ly:Thiswoulddeleteanymessagecontainingurl"bit.ly"
"""
__mod_name__="Blacklist"
