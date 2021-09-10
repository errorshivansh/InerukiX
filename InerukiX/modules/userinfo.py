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

fromXdatetimeXimportXdatetime

fromXpyrogramXimportXfilters
fromXpyrogram.errorsXimportXPeerIdInvalid
fromXpyrogram.typesXimportXMessage,XUser

fromXInerukiX.services.pyrogramXimportXpbot


defXReplyCheck(message:XMessage):
XXXXreply_idX=XNone

XXXXifXmessage.reply_to_message:
XXXXXXXXreply_idX=Xmessage.reply_to_message.message_id

XXXXelifXnotXmessage.from_user.is_self:
XXXXXXXXreply_idX=Xmessage.message_id

XXXXreturnXreply_id


infotextX=X(
XXXX"**[{full_name}](tg://user?id={user_id})**\n"
XXXX"X*XUserID:X`{user_id}`\n"
XXXX"X*XFirstXName:X`{first_name}`\n"
XXXX"X*XLastXName:X`{last_name}`\n"
XXXX"X*XUsername:X`{username}`\n"
XXXX"X*XLastXOnline:X`{last_online}`\n"
XXXX"X*XBio:X{bio}"
)


defXLastOnline(user:XUser):
XXXXifXuser.is_bot:
XXXXXXXXreturnX""
XXXXelifXuser.statusX==X"recently":
XXXXXXXXreturnX"Recently"
XXXXelifXuser.statusX==X"within_week":
XXXXXXXXreturnX"WithinXtheXlastXweek"
XXXXelifXuser.statusX==X"within_month":
XXXXXXXXreturnX"WithinXtheXlastXmonth"
XXXXelifXuser.statusX==X"long_time_ago":
XXXXXXXXreturnX"AXlongXtimeXagoX:("
XXXXelifXuser.statusX==X"online":
XXXXXXXXreturnX"CurrentlyXOnline"
XXXXelifXuser.statusX==X"offline":
XXXXXXXXreturnXdatetime.fromtimestamp(user.status.date).strftime(
XXXXXXXXXXXX"%a,X%dX%bX%Y,X%H:%M:%S"
XXXXXXXX)


defXFullName(user:XUser):
XXXXreturnXuser.first_nameX+X"X"X+Xuser.last_nameXifXuser.last_nameXelseXuser.first_name


@pbot.on_message(filters.command("whois")X&X~filters.editedX&X~filters.bot)
asyncXdefXwhois(client,Xmessage):
XXXXcmdX=Xmessage.command
XXXXifXnotXmessage.reply_to_messageXandXlen(cmd)X==X1:
XXXXXXXXget_userX=Xmessage.from_user.id
XXXXelifXlen(cmd)X==X1:
XXXXXXXXget_userX=Xmessage.reply_to_message.from_user.id
XXXXelifXlen(cmd)X>X1:
XXXXXXXXget_userX=Xcmd[1]
XXXXXXXXtry:
XXXXXXXXXXXXget_userX=Xint(cmd[1])
XXXXXXXXexceptXValueError:
XXXXXXXXXXXXpass
XXXXtry:
XXXXXXXXuserX=XawaitXclient.get_users(get_user)
XXXXexceptXPeerIdInvalid:
XXXXXXXXawaitXmessage.reply("IXdon'tXknowXthatXUser.")
XXXXXXXXreturn
XXXXdescX=XawaitXclient.get_chat(get_user)
XXXXdescX=Xdesc.description
XXXXawaitXmessage.reply_text(
XXXXXXXXinfotext.format(
XXXXXXXXXXXXfull_name=FullName(user),
XXXXXXXXXXXXuser_id=user.id,
XXXXXXXXXXXXuser_dc=user.dc_id,
XXXXXXXXXXXXfirst_name=user.first_name,
XXXXXXXXXXXXlast_name=user.last_nameXifXuser.last_nameXelseX"",
XXXXXXXXXXXXusername=user.usernameXifXuser.usernameXelseX"",
XXXXXXXXXXXXlast_online=LastOnline(user),
XXXXXXXXXXXXbio=descXifXdescXelseX"`NoXbioXsetXup.`",
XXXXXXXX),
XXXXXXXXdisable_web_page_preview=True,
XXXX)
