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


importos
fromdatetimeimportdatetime

fromPILimportImage
fromtelegraphimportTelegraph,exceptions,upload_file
fromtelethonimportevents

fromIneruki.services.telethonimporttbotasborg

telegraph=Telegraph()
r=telegraph.create_account(short_name="Ineruki")
auth_url=r["auth_url"]

#Willchangelater
TMP_DOWNLOAD_DIRECTORY="./"

BOTLOG=False


@borg.on(events.NewMessage(pattern="/telegraph(media|text)?(.*)"))
asyncdef_(event):
ifevent.fwd_from:
return
optional_title=event.pattern_match.group(2)
ifevent.reply_to_msg_id:
start=datetime.now()
r_message=awaitevent.get_reply_message()
input_str=event.pattern_match.group(1)
ifinput_str=="media":
downloaded_file_name=awaitborg.download_media(
r_message,TMP_DOWNLOAD_DIRECTORY
)
end=datetime.now()
ms=(end-start).seconds
awaitevent.reply(
"Downloadedto{}in{}seconds.".format(downloaded_file_name,ms)
)
ifdownloaded_file_name.endswith((".webp")):
resize_image(downloaded_file_name)
try:
start=datetime.now()
media_urls=upload_file(downloaded_file_name)
exceptexceptions.TelegraphExceptionasexc:
awaitevent.edit("ERROR:"+str(exc))
os.remove(downloaded_file_name)
else:
end=datetime.now()
ms_two=(end-start).seconds
os.remove(downloaded_file_name)
awaitevent.reply(
"Uploadedtohttps://telegra.ph{}in{}seconds.".format(
media_urls[0],(ms+ms_two)
),
link_preview=True,
)
elifinput_str=="text":
user_object=awaitborg.get_entity(r_message.sender_id)
title_of_page=user_object.first_name#+""+user_object.last_name
#apparently,allUsersdonothavelast_namefield
ifoptional_title:
title_of_page=optional_title
page_content=r_message.message
ifr_message.media:
ifpage_content!="":
title_of_page=page_content
downloaded_file_name=awaitborg.download_media(
r_message,TMP_DOWNLOAD_DIRECTORY
)
m_list=None
withopen(downloaded_file_name,"rb")asfd:
m_list=fd.readlines()
forminm_list:
page_content+=m.decode("UTF-8")+"\n"
os.remove(downloaded_file_name)
page_content=page_content.replace("\n","<br>")
response=telegraph.create_page(title_of_page,html_content=page_content)
end=datetime.now()
ms=(end-start).seconds
awaitevent.reply(
"Pastedtohttps://telegra.ph/{}in{}seconds.".format(
response["path"],ms
),
link_preview=True,
)
else:
awaitevent.reply("Replytoamessagetogetapermanenttelegra.phlink.")


defresize_image(image):
im=Image.open(image)
im.save(image,"PNG")


__mod_name__="""
<b>Telegraphtext/videouploadplugin</b>
-/telegraphmedia<i>replytoimageorvideo<i>:Uploadimageandvideodirectlytotelegraph.
-/telegraphtext<i>replytotext</i>:uploadtextdirectlytotelegraph.
"""

__mod_name__="Telegraph"
