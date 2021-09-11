#Copyright(C)@chsaiujwal2020-2021
#Editedbyerrorshivansh
#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseaspublishedby
#theFreeSoftwareFoundation,eitherversion3oftheLicense,or
#
#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.
#
#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<https://www.gnu.org/licenses/>.

importos

importrequests
fromfakerimportFaker
fromfaker.providersimportinternet
fromtelethonimportevents

fromIneruki.function.telethonbasicsimportis_admin
fromIneruki.services.telethonimporttbot


@tbot.on(events.NewMessage(pattern="/fakegen$"))
asyncdefhi(event):
ifevent.fwd_from:
return
ifevent.is_group:
ifnotawaitis_admin(event,event.message.sender_id):
awaitevent.reply("`YouShouldBeAdminToDoThis!`")
return
fake=Faker()
print("FAKEDETAILSGENERATED\n")
name=str(fake.name())
fake.add_provider(internet)
address=str(fake.address())
ip=fake.ipv4_private()
cc=fake.credit_card_full()
email=fake.ascii_free_email()
job=fake.job()
android=fake.android_platform_token()
pc=fake.chrome()
awaitevent.reply(
f"<b><u>FakeInformationGenerated</b></u>\n<b>Name:-</b><code>{name}</code>\n\n<b>Address:-</b><code>{address}</code>\n\n<b>IPADDRESS:-</b><code>{ip}</code>\n\n<b>creditcard:-</b><code>{cc}</code>\n\n<b>EmailId:-</b><code>{email}</code>\n\n<b>Job:-</b><code>{job}</code>\n\n<b>androiduseragent:-</b><code>{android}</code>\n\n<b>Pcuseragent:-</b><code>{pc}</code>",
parse_mode="HTML",
)


@tbot.on(events.NewMessage(pattern="/picgen$"))
asyncdef_(event):
ifevent.fwd_from:
return
ifawaitis_admin(event,event.message.sender_id):
url="https://thispersondoesnotexist.com/image"
response=requests.get(url)
ifresponse.status_code==200:
withopen("FRIDAYOT.jpg","wb")asf:
f.write(response.content)

captin=f"FakeImagepoweredby@InerukiSupport_Official."
fole="FRIDAYOT.jpg"
awaittbot.send_file(event.chat_id,fole,caption=captin)
awaitevent.delete()
os.system("rm./FRIDAYOT.jpg")
