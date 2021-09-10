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

importXasyncio
importXos
importXre

fromXtelethonXimportXButton,Xevents,Xutils
fromXtelethon.tlXimportXfunctions,Xtypes

fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.sql.filters_sqlXimportX(
XXXXadd_filter,
XXXXget_all_filters,
XXXXremove_all_filters,
XXXXremove_filter,
)
fromXInerukiX.services.telethonXimportXtbot

DELETE_TIMEOUTX=X0
TYPE_TEXTX=X0
TYPE_PHOTOX=X1
TYPE_DOCUMENTX=X2
last_triggered_filtersX=X{}


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


@tbot.on(events.NewMessage(pattern=None))
asyncXdefXon_snip(event):

XXXXglobalXlast_triggered_filters

XXXXnameX=Xevent.raw_text

XXXXifXevent.chat_idXinXlast_triggered_filters:

XXXXXXXXifXnameXinXlast_triggered_filters[event.chat_id]:

XXXXXXXXXXXXreturnXFalse

XXXXsnipsX=Xget_all_filters(event.chat_id)

XXXXifXsnips:

XXXXXXXXforXsnipXinXsnips:

XXXXXXXXXXXXpatternX=Xr"(X|^|[^\w])"X+Xre.escape(snip.keyword)X+Xr"(X|$|[^\w])"

XXXXXXXXXXXXifXre.search(pattern,Xname,Xflags=re.IGNORECASE):

XXXXXXXXXXXXXXXXifXsnip.snip_typeX==XTYPE_PHOTO:

XXXXXXXXXXXXXXXXXXXXmediaX=Xtypes.InputPhoto(
XXXXXXXXXXXXXXXXXXXXXXXXint(snip.media_id),
XXXXXXXXXXXXXXXXXXXXXXXXint(snip.media_access_hash),
XXXXXXXXXXXXXXXXXXXXXXXXsnip.media_file_reference,
XXXXXXXXXXXXXXXXXXXX)

XXXXXXXXXXXXXXXXelifXsnip.snip_typeX==XTYPE_DOCUMENT:

XXXXXXXXXXXXXXXXXXXXmediaX=Xtypes.InputDocument(
XXXXXXXXXXXXXXXXXXXXXXXXint(snip.media_id),
XXXXXXXXXXXXXXXXXXXXXXXXint(snip.media_access_hash),
XXXXXXXXXXXXXXXXXXXXXXXXsnip.media_file_reference,
XXXXXXXXXXXXXXXXXXXX)

XXXXXXXXXXXXXXXXelse:

XXXXXXXXXXXXXXXXXXXXmediaX=XNone

XXXXXXXXXXXXXXXXevent.message.id

XXXXXXXXXXXXXXXXifXevent.reply_to_msg_id:

XXXXXXXXXXXXXXXXXXXXevent.reply_to_msg_id

XXXXXXXXXXXXXXXXfilterX=X""
XXXXXXXXXXXXXXXXoptionsX=X""
XXXXXXXXXXXXXXXXbuttoX=XNone

XXXXXXXXXXXXXXXXifX"|"XinXsnip.reply:
XXXXXXXXXXXXXXXXXXXXfilter,XoptionsX=Xsnip.reply.split("|")
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXfilterX=Xstr(snip.reply)
XXXXXXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXXXXXfilterX=Xfilter.strip()
XXXXXXXXXXXXXXXXXXXXbuttonX=Xoptions.strip()
XXXXXXXXXXXXXXXXXXXXifX"•"XinXbutton:
XXXXXXXXXXXXXXXXXXXXXXXXmbuttonX=Xbutton.split("•")
XXXXXXXXXXXXXXXXXXXXXXXXlbuttonX=X[]
XXXXXXXXXXXXXXXXXXXXXXXXforXiXinXmbutton:
XXXXXXXXXXXXXXXXXXXXXXXXXXXXparamsX=Xre.findall(r"\'(.*?)\'",Xi)XorXre.findall(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXr"\"(.*?)\"",Xi
XXXXXXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXXXXXlbutton.append(params)
XXXXXXXXXXXXXXXXXXXXXXXXlongbuttonX=X[]
XXXXXXXXXXXXXXXXXXXXXXXXforXcXinXlbutton:
XXXXXXXXXXXXXXXXXXXXXXXXXXXXbuttoX=X[Button.url(*c)]
XXXXXXXXXXXXXXXXXXXXXXXXXXXXlongbutton.append(butto)
XXXXXXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXXXXXparamsX=Xre.findall(r"\'(.*?)\'",Xbutton)XorXre.findall(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXr"\"(.*?)\"",Xbutton
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXXbuttoX=X[Button.url(*params)]
XXXXXXXXXXXXXXXXexceptXBaseException:
XXXXXXXXXXXXXXXXXXXXfilterX=Xfilter.strip()
XXXXXXXXXXXXXXXXXXXXbuttoX=XNone

XXXXXXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXXXXXawaitXevent.reply(filter,Xbuttons=longbutton,Xfile=media)
XXXXXXXXXXXXXXXXexcept:
XXXXXXXXXXXXXXXXXXXXawaitXevent.reply(filter,Xbuttons=butto,Xfile=media)

XXXXXXXXXXXXXXXXifXevent.chat_idXnotXinXlast_triggered_filters:

XXXXXXXXXXXXXXXXXXXXlast_triggered_filters[event.chat_id]X=X[]

XXXXXXXXXXXXXXXXlast_triggered_filters[event.chat_id].append(name)

XXXXXXXXXXXXXXXXawaitXasyncio.sleep(DELETE_TIMEOUT)

XXXXXXXXXXXXXXXXlast_triggered_filters[event.chat_id].remove(name)


@register(pattern="^/cfilterX(.*)")
asyncXdefXon_snip_save(event):
XXXXifXevent.is_group:
XXXXXXXXifXnotXawaitXcan_change_info(message=event):
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn

XXXXnameX=Xevent.pattern_match.group(1)
XXXXmsgX=XawaitXevent.get_reply_message()

XXXXifXmsg:

XXXXXXXXsnipX=X{"type":XTYPE_TEXT,X"text":Xmsg.messageXorX""}

XXXXXXXXifXmsg.media:

XXXXXXXXXXXXmediaX=XNone

XXXXXXXXXXXXifXisinstance(msg.media,Xtypes.MessageMediaPhoto):

XXXXXXXXXXXXXXXXmediaX=Xutils.get_input_photo(msg.media.photo)

XXXXXXXXXXXXXXXXsnip["type"]X=XTYPE_PHOTO

XXXXXXXXXXXXelifXisinstance(msg.media,Xtypes.MessageMediaDocument):

XXXXXXXXXXXXXXXXmediaX=Xutils.get_input_document(msg.media.document)

XXXXXXXXXXXXXXXXsnip["type"]X=XTYPE_DOCUMENT

XXXXXXXXXXXXifXmedia:

XXXXXXXXXXXXXXXXsnip["id"]X=Xmedia.id

XXXXXXXXXXXXXXXXsnip["hash"]X=Xmedia.access_hash

XXXXXXXXXXXXXXXXsnip["fr"]X=Xmedia.file_reference

XXXXXXXXadd_filter(
XXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXname,
XXXXXXXXXXXXsnip["text"],
XXXXXXXXXXXXsnip["type"],
XXXXXXXXXXXXsnip.get("id"),
XXXXXXXXXXXXsnip.get("hash"),
XXXXXXXXXXXXsnip.get("fr"),
XXXXXXXX)

XXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXf"ClassicXFilterX{name}XsavedXsuccessfully.XyouXcanXgetXitXwithX{name}\nNote:XTryXourXnewXfilterXsystemX/addfilterX"
XXXXXXXX)

XXXXelse:

XXXXXXXXawaitXevent.reply(
XXXXXXXXXXXX"Usage:XReplyXtoXuserXmessageXwithX/cfilterX<text>..X\nNotXRecomendedXuseXnewXfilterXsystemX/savefilter"
XXXXXXXX)


@register(pattern="^/stopcfilterX(.*)")
asyncXdefXon_snip_delete(event):
XXXXifXevent.is_group:
XXXXXXXXifXnotXawaitXcan_change_info(message=event):
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn
XXXXnameX=Xevent.pattern_match.group(1)

XXXXremove_filter(event.chat_id,Xname)

XXXXawaitXevent.reply(f"FilterX**{name}**XdeletedXsuccessfully")


@register(pattern="^/cfilters$")
asyncXdefXon_snip_list(event):
XXXXifXevent.is_group:
XXXXXXXXpass
XXXXelse:
XXXXXXXXreturn
XXXXall_snipsX=Xget_all_filters(event.chat_id)

XXXXOUT_STRX=X"AvailableXClassicXFiltersXinXtheXCurrentXChat:\n"

XXXXifXlen(all_snips)X>X0:

XXXXXXXXforXa_snipXinXall_snips:

XXXXXXXXXXXXOUT_STRX+=Xf"👉{a_snip.keyword}X\n"

XXXXelse:

XXXXXXXXOUT_STRX=X"NoXClassicXFiltersXinXthisXchat.X"

XXXXifXlen(OUT_STR)X>X4096:

XXXXXXXXwithXio.BytesIO(str.encode(OUT_STR))XasXout_file:

XXXXXXXXXXXXout_file.nameX=X"filters.text"

XXXXXXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXXXXXXout_file,
XXXXXXXXXXXXXXXXforce_document=True,
XXXXXXXXXXXXXXXXallow_cache=False,
XXXXXXXXXXXXXXXXcaption="AvailableXClassicXFiltersXinXtheXCurrentXChat",
XXXXXXXXXXXXXXXXreply_to=event,
XXXXXXXXXXXX)

XXXXelse:

XXXXXXXXawaitXevent.reply(OUT_STR)


@register(pattern="^/stopallcfilters$")
asyncXdefXon_all_snip_delete(event):
XXXXifXevent.is_group:
XXXXXXXXifXnotXawaitXcan_change_info(message=event):
XXXXXXXXXXXXreturn
XXXXelse:
XXXXXXXXreturn
XXXXremove_all_filters(event.chat_id)
XXXXawaitXevent.reply(f"ClassicXFilterXinXcurrentXchatXdeletedX!")


file_helpX=Xos.path.basename(__file__)
file_helpX=Xfile_help.replace(".py",X"")
file_helpoX=Xfile_help.replace("_",X"X")
