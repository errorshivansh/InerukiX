#XXXXCopyrightX(C)X@chsaiujwalX2020-2021
#XXXXEditedXbyXerrorshivansh
#XXXXThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XXXXitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXasXpublishedXby
#XXXXtheXFreeXSoftwareXFoundation,XeitherXversionX3XofXtheXLicense,Xor
#
#XXXXThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XXXXbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XXXXMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XXXXGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.
#
#XXXXYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XXXXalongXwithXthisXprogram.XXIfXnot,XseeX<https://www.gnu.org/licenses/>.

importXos

importXrequests
fromXfakerXimportXFaker
fromXfaker.providersXimportXinternet
fromXtelethonXimportXevents

fromXInerukiX.function.telethonbasicsXimportXis_admin
fromXInerukiX.services.telethonXimportXtbot


@tbot.on(events.NewMessage(pattern="/fakegen$"))
asyncXdefXhi(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXevent.is_group:
XXXXXXXXifXnotXawaitXis_admin(event,Xevent.message.sender_id):
XXXXXXXXXXXXawaitXevent.reply("`YouXShouldXBeXAdminXToXDoXThis!`")
XXXXXXXXXXXXreturn
XXXXfakeX=XFaker()
XXXXprint("FAKEXDETAILSXGENERATED\n")
XXXXnameX=Xstr(fake.name())
XXXXfake.add_provider(internet)
XXXXaddressX=Xstr(fake.address())
XXXXipX=Xfake.ipv4_private()
XXXXccX=Xfake.credit_card_full()
XXXXemailX=Xfake.ascii_free_email()
XXXXjobX=Xfake.job()
XXXXandroidX=Xfake.android_platform_token()
XXXXpcX=Xfake.chrome()
XXXXawaitXevent.reply(
XXXXXXXXf"<b><u>XFakeXInformationXGenerated</b></u>\n<b>NameX:-</b><code>{name}</code>\n\n<b>Address:-</b><code>{address}</code>\n\n<b>IPXADDRESS:-</b><code>{ip}</code>\n\n<b>creditXcard:-</b><code>{cc}</code>\n\n<b>EmailXId:-</b><code>{email}</code>\n\n<b>Job:-</b><code>{job}</code>\n\n<b>androidXuserXagent:-</b><code>{android}</code>\n\n<b>PcXuserXagent:-</b><code>{pc}</code>",
XXXXXXXXparse_mode="HTML",
XXXX)


@tbot.on(events.NewMessage(pattern="/picgen$"))
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXifXawaitXis_admin(event,Xevent.message.sender_id):
XXXXXXXXurlX=X"https://thispersondoesnotexist.com/image"
XXXXXXXXresponseX=Xrequests.get(url)
XXXXXXXXifXresponse.status_codeX==X200:
XXXXXXXXXXXXwithXopen("FRIDAYOT.jpg",X"wb")XasXf:
XXXXXXXXXXXXXXXXf.write(response.content)

XXXXXXXXcaptinX=Xf"FakeXImageXpoweredXbyX@InerukiSupport_Official."
XXXXXXXXfoleX=X"FRIDAYOT.jpg"
XXXXXXXXawaitXtbot.send_file(event.chat_id,Xfole,Xcaption=captin)
XXXXXXXXawaitXevent.delete()
XXXXXXXXos.system("rmX./FRIDAYOT.jpgX")
