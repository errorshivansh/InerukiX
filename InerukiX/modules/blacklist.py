#XCopyrightX(C)X2021Xerrorshivansh


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


importXhtml

importXtldextract
fromXtelethonXimportXevents,Xtypes
fromXtelethon.tlXimportXfunctions

importXInerukiX.services.sql.urlblacklist_sqlXasXurlsql
fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbot


asyncXdefXcan_change_info(message):
XXXXresultX=XawaitXtbot(
XXXXXXXXfunctions.channels.GetParticipantRequest(
XXXXXXXXXXXXchannel=message.chat_id,
XXXXXXXXXXXXuser_id=message.sender_id,
XXXXXXXX)
XXXX)
XXXXpX=Xresult.participant
XXXXreturnXisinstance(p,Xtypes.ChannelParticipantCreator)XorX(
XXXXXXXXisinstance(p,Xtypes.ChannelParticipantAdmin)XandXp.admin_rights.change_info
XXXX)


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXtbot(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXifXisinstance(chat,Xtypes.InputPeerUser):
XXXXXXXXreturnXTrue


@register(pattern="^/addurl")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_private:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXcan_change_info(message=event):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXchatX=Xevent.chat
XXXXurlsX=Xevent.text.split(None,X1)
XXXXifXlen(urls)X>X1:
XXXXXXXXurlsX=Xurls[1]
XXXXXXXXto_blacklistX=Xlist({uri.strip()XforXuriXinXurls.split("\n")XifXuri.strip()})
XXXXXXXXblacklistedX=X[]

XXXXXXXXforXuriXinXto_blacklist:
XXXXXXXXXXXXextract_urlX=Xtldextract.extract(uri)
XXXXXXXXXXXXifXextract_url.domainXandXextract_url.suffix:
XXXXXXXXXXXXXXXXblacklisted.append(extract_url.domainX+X"."X+Xextract_url.suffix)
XXXXXXXXXXXXXXXXurlsql.blacklist_url(
XXXXXXXXXXXXXXXXXXXXchat.id,Xextract_url.domainX+X"."X+Xextract_url.suffix
XXXXXXXXXXXXXXXX)

XXXXXXXXifXlen(to_blacklist)X==X1:
XXXXXXXXXXXXextract_urlX=Xtldextract.extract(to_blacklist[0])
XXXXXXXXXXXXifXextract_url.domainXandXextract_url.suffix:
XXXXXXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXXXXXX"AddedX<code>{}</code>XdomainXtoXtheXblacklist!".format(
XXXXXXXXXXXXXXXXXXXXXXXXhtml.escape(extract_url.domainX+X"."X+Xextract_url.suffix)
XXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXparse_mode="html",
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXawaitXevent.reply("YouXareXtryingXtoXblacklistXanXinvalidXurl")
XXXXXXXXelse:
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"AddedX<code>{}</code>XdomainsXtoXtheXblacklist.".format(
XXXXXXXXXXXXXXXXXXXXlen(blacklisted)
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXparse_mode="html",
XXXXXXXXXXXX)
XXXXelse:
XXXXXXXXawaitXevent.reply("TellXmeXwhichXurlsXyouXwouldXlikeXtoXaddXtoXtheXblacklist.")


@register(pattern="^/delurl")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_private:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXcan_change_info(message=event):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXchatX=Xevent.chat
XXXXurlsX=Xevent.text.split(None,X1)

XXXXifXlen(urls)X>X1:
XXXXXXXXurlsX=Xurls[1]
XXXXXXXXto_unblacklistX=Xlist({uri.strip()XforXuriXinXurls.split("\n")XifXuri.strip()})
XXXXXXXXunblacklistedX=X0
XXXXXXXXforXuriXinXto_unblacklist:
XXXXXXXXXXXXextract_urlX=Xtldextract.extract(uri)
XXXXXXXXXXXXsuccessX=Xurlsql.rm_url_from_blacklist(
XXXXXXXXXXXXXXXXchat.id,Xextract_url.domainX+X"."X+Xextract_url.suffix
XXXXXXXXXXXX)
XXXXXXXXXXXXifXsuccess:
XXXXXXXXXXXXXXXXunblacklistedX+=X1

XXXXXXXXifXlen(to_unblacklist)X==X1:
XXXXXXXXXXXXifXunblacklisted:
XXXXXXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXXXXXX"RemovedX<code>{}</code>XfromXtheXblacklist!".format(
XXXXXXXXXXXXXXXXXXXXXXXXhtml.escape(to_unblacklist[0])
XXXXXXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXXXXXparse_mode="html",
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXawaitXevent.reply("ThisXisn'tXaXblacklistedXdomain...!")
XXXXXXXXelifXunblacklistedX==Xlen(to_unblacklist):
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"RemovedX<code>{}</code>XdomainsXfromXtheXblacklist.".format(
XXXXXXXXXXXXXXXXXXXXunblacklisted
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXparse_mode="html",
XXXXXXXXXXXX)
XXXXXXXXelifXnotXunblacklisted:
XXXXXXXXXXXXawaitXevent.reply("NoneXofXtheseXdomainsXexist,XsoXtheyXweren'tXremoved.")
XXXXXXXXelse:
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXX"RemovedX<code>{}</code>XdomainsXfromXtheXblacklist.X{}XdidXnotXexist,XsoXwereXnotXremoved.".format(
XXXXXXXXXXXXXXXXXXXXunblacklisted,Xlen(to_unblacklist)X-Xunblacklisted
XXXXXXXXXXXXXXXX),
XXXXXXXXXXXXXXXXparse_mode="html",
XXXXXXXXXXXX)
XXXXelse:
XXXXXXXXawaitXevent.reply(
XXXXXXXXXXXX"TellXmeXwhichXdomainsXyouXwouldXlikeXtoXremoveXfromXtheXblacklist."
XXXXXXXX)


@tbot.on(events.NewMessage(incoming=True))
asyncXdefXon_url_message(event):
XXXXifXevent.is_private:
XXXXXXXXreturn
XXXXchatX=Xevent.chat
XXXXextracted_domainsX=X[]
XXXXforX(ent,Xtxt)XinXevent.get_entities_text():
XXXXXXXXifXent.offsetX!=X0:
XXXXXXXXXXXXbreak
XXXXXXXXifXisinstance(ent,Xtypes.MessageEntityUrl):
XXXXXXXXXXXXurlX=Xtxt
XXXXXXXXXXXXextract_urlX=Xtldextract.extract(url)
XXXXXXXXXXXXextracted_domains.append(extract_url.domainX+X"."X+Xextract_url.suffix)
XXXXforXurlXinXurlsql.get_blacklisted_urls(chat.id):
XXXXXXXXifXurlXinXextracted_domains:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXevent.delete()
XXXXXXXXXXXXexcept:
XXXXXXXXXXXXXXXXreturn


@register(pattern="^/geturl$")
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_private:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXawaitXcan_change_info(message=event):
XXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXreturn
XXXXchatX=Xevent.chat
XXXXbase_stringX=X"CurrentX<b>blacklisted</b>Xdomains:\n"
XXXXblacklistedX=Xurlsql.get_blacklisted_urls(chat.id)
XXXXifXnotXblacklisted:
XXXXXXXXawaitXevent.reply("ThereXareXnoXblacklistedXdomainsXhere!")
XXXXXXXXreturn
XXXXforXdomainXinXblacklisted:
XXXXXXXXbase_stringX+=X"-X<code>{}</code>\n".format(domain)
XXXXawaitXevent.reply(base_string,Xparse_mode="html")


__help__X=X"""
<b>XIneruki'sXfiltersXareXtheXblacklistXtooX</b>
X-X/addfilterX[trigger]XSelectXaction:XblacklistsXtheXtrigger
X-X/delfilterX[trigger]X:XstopXblacklistingXaXcertainXblacklistXtrigger
X-X/filters:XlistXallXactiveXblacklistXfilters
X
<b>XUrlXBlacklistX</B>
X-X/geturl:XViewXtheXcurrentXblacklistedXurls
X-X/addurlX[urls]:XAddXaXdomainXtoXtheXblacklist.XTheXbotXwillXautomaticallyXparseXtheXurl.
X-X/delurlX[urls]:XRemoveXurlsXfromXtheXblacklist.
<b>XExample:</b>
X-X/addblacklistXtheXadminsXsuck:XThisXwillXremoveX"theXadminsXsuck"XeverytimeXsomeXnon-adminXtypesXit
X-X/addurlXbit.ly:XThisXwouldXdeleteXanyXmessageXcontainingXurlX"bit.ly"
"""
__mod_name__X=X"Blacklist"
