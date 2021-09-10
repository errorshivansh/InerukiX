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


fromXapscheduler.schedulers.asyncioXimportXAsyncIOScheduler
fromXtelethonXimportXevents,Xfunctions
fromXtelethon.tl.typesXimportXChatBannedRights

fromXInerukiXXimportXBOT_ID
fromXInerukiX.function.telethonbasicsXimportXis_admin
fromXInerukiX.services.sql.night_mode_sqlXimportX(
XXXXadd_nightmode,
XXXXget_all_chat_id,
XXXXis_nightmode_indb,
XXXXrmnightmode,
)
fromXInerukiX.services.telethonXimportXtbot

CLEAN_GROUPSX=XFalse
hehesX=XChatBannedRights(
XXXXuntil_date=None,
XXXXsend_messages=True,
XXXXsend_media=True,
XXXXsend_stickers=True,
XXXXsend_gifs=True,
XXXXsend_games=True,
XXXXsend_inline=True,
XXXXsend_polls=True,
XXXXinvite_users=True,
XXXXpin_messages=True,
XXXXchange_info=True,
)
openheheX=XChatBannedRights(
XXXXuntil_date=None,
XXXXsend_messages=False,
XXXXsend_media=False,
XXXXsend_stickers=False,
XXXXsend_gifs=False,
XXXXsend_games=False,
XXXXsend_inline=False,
XXXXsend_polls=False,
XXXXinvite_users=True,
XXXXpin_messages=True,
XXXXchange_info=True,
)


@tbot.on(events.NewMessage(pattern="/nightmodeX(.*)"))
asyncXdefXclose_ws(event):

XXXXifXnotXevent.is_group:
XXXXXXXXawaitXevent.reply("YouXCanXOnlyXNsfwXWatchXinXGroups.")
XXXXXXXXreturn
XXXXinput_strX=Xevent.pattern_match.group(1)
XXXXifXnotXawaitXis_admin(event,XBOT_ID):
XXXXXXXXawaitXevent.reply("`IXShouldXBeXAdminXToXDoXThis!`")
XXXXXXXXreturn
XXXXifXawaitXis_admin(event,Xevent.message.sender_id):
XXXXXXXXifX(
XXXXXXXXXXXXinput_strX==X"on"
XXXXXXXXXXXXorXinput_strX==X"On"
XXXXXXXXXXXXorXinput_strX==X"ON"
XXXXXXXXXXXXorXinput_strX==X"enable"
XXXXXXXX):
XXXXXXXXXXXXifXis_nightmode_indb(str(event.chat_id)):
XXXXXXXXXXXXXXXXawaitXevent.reply("ThisXChatXisXHasXAlreadyXEnabledXNightXMode.")
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXadd_nightmode(str(event.chat_id))
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXXf"**AddedXChatX{event.chat.title}XWithXIdX{event.chat_id}XToXDatabase.XThisXGroupXWillXBeXClosedXOnX12Am(IST)XAndXWillXOpenedXOnX06Am(IST)**"
XXXXXXXXXXXX)
XXXXXXXXelifX(
XXXXXXXXXXXXinput_strX==X"off"
XXXXXXXXXXXXorXinput_strX==X"Off"
XXXXXXXXXXXXorXinput_strX==X"OFF"
XXXXXXXXXXXXorXinput_strX==X"disable"
XXXXXXXX):

XXXXXXXXXXXXifXnotXis_nightmode_indb(str(event.chat_id)):
XXXXXXXXXXXXXXXXawaitXevent.reply("ThisXChatXisXHasXNotXEnabledXNightXMode.")
XXXXXXXXXXXXXXXXreturn
XXXXXXXXXXXXrmnightmode(str(event.chat_id))
XXXXXXXXXXXXawaitXevent.reply(
XXXXXXXXXXXXXXXXf"**RemovedXChatX{event.chat.title}XWithXIdX{event.chat_id}XFromXDatabase.XThisXGroupXWillXBeXNoXLongerXClosedXOnX12Am(IST)XAndXWillXOpenedXOnX06Am(IST)**"
XXXXXXXXXXXX)
XXXXXXXXelse:
XXXXXXXXXXXXawaitXevent.reply("IXundestandX`/nightmodeXon`XandX`/nightmodeXoff`Xonly")
XXXXelse:
XXXXXXXXawaitXevent.reply("`YouXShouldXBeXAdminXToXDoXThis!`")
XXXXXXXXreturn


asyncXdefXjob_close():
XXXXws_chatsX=Xget_all_chat_id()
XXXXifXlen(ws_chats)X==X0:
XXXXXXXXreturn
XXXXforXwarnerXinXws_chats:
XXXXXXXXtry:
XXXXXXXXXXXXawaitXtbot.send_message(
XXXXXXXXXXXXXXXXint(warner.chat_id),
XXXXXXXXXXXXXXXX"`12:00XAm,XGroupXIsXClosingXTillX6XAm.XNightXModeXStartedX!`X\n**PoweredXByX@InerukiXbot**",
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXtbot(
XXXXXXXXXXXXXXXXfunctions.messages.EditChatDefaultBannedRightsRequest(
XXXXXXXXXXXXXXXXXXXXpeer=int(warner.chat_id),Xbanned_rights=hehes
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXX)
XXXXXXXXXXXXifXCLEAN_GROUPS:
XXXXXXXXXXXXXXXXasyncXforXuserXinXtbot.iter_participants(int(warner.chat_id)):
XXXXXXXXXXXXXXXXXXXXifXuser.deleted:
XXXXXXXXXXXXXXXXXXXXXXXXawaitXtbot.edit_permissions(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXint(warner.chat_id),Xuser.id,Xview_messages=False
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXexceptXExceptionXasXe:
XXXXXXXXXXXXprint(f"UnableXToXCloseXGroupX{warner}X-X{e}")


schedulerX=XAsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_close,Xtrigger="cron",Xhour=23,Xminute=55)
scheduler.start()


asyncXdefXjob_open():
XXXXws_chatsX=Xget_all_chat_id()
XXXXifXlen(ws_chats)X==X0:
XXXXXXXXreturn
XXXXforXwarnerXinXws_chats:
XXXXXXXXtry:
XXXXXXXXXXXXawaitXtbot.send_message(
XXXXXXXXXXXXXXXXint(warner.chat_id),
XXXXXXXXXXXXXXXX"`06:00XAm,XGroupXIsXOpening.`\n**PoweredXByX@InerukiXBot**",
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXtbot(
XXXXXXXXXXXXXXXXfunctions.messages.EditChatDefaultBannedRightsRequest(
XXXXXXXXXXXXXXXXXXXXpeer=int(warner.chat_id),Xbanned_rights=openhehe
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXX)
XXXXXXXXexceptXExceptionXasXe:
XXXXXXXXXXXXprint(f"UnableXToXOpenXGroupX{warner.chat_id}X-X{e}")


#XRunXeverydayXatX06
schedulerX=XAsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_open,Xtrigger="cron",Xhour=6,Xminute=10)
scheduler.start()

__mod_name__X=X"NightXMode"

__help__X=X"""
<b>XTheXNightXmodeX</b>
CloseXyourXgroupXatX12.00Xa.m.XandXopenXbackXatX6.00Xa.m.(IST)
<i>XOnlyXavailableXforXasianXcountriesX(IndiaXStandardXtime)</i>

-X/nightmodeX[ON/OFF]:XEnable/DisableXNightXMode.

"""
