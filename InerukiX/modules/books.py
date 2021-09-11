#Copyright(C)2020DevsExpo
#Copyright(C)2021InukaAsith
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
importre

importrequests
frombs4importBeautifulSoup
fromtelethonimportevents

fromIneruki.services.telethonimporttbot


@tbot.on(events.NewMessage(pattern="^/book(.*)"))
asyncdef_(event):
ifevent.fwd_from:
return
input_str=event.pattern_match.group(1)
lool=0
KkK=awaitevent.reply("searchingforthebook...")
lin="https://b-ok.cc/s/"
text=input_str
link=lin+text

headers=[
"User-Agent",
"Mozilla/5.0(Macintosh;IntelMacOS10.15;rv:74.0)Gecko/20100101Firefox/74.0",
]
page=requests.get(link)
soup=BeautifulSoup(page.content,"html.parser")
f=open("book.txt","w")
total=soup.find(class_="totalCounter")
fornbintotal.descendants:
nbx=nb.replace("(","").replace(")","")
ifnbx=="0":
awaitevent.reply("NoBooksFoundwiththatname.")
else:

fortrinsoup.find_all("td"):
fortdintr.find_all("h3"):
fortsintd.find_all("a"):
title=ts.get_text()
lool=lool+1
fortsintd.find_all("a",attrs={"href":re.compile("^/book/")}):
ref=ts.get("href")
link="https://b-ok.cc"+ref

f.write("\n"+title)
f.write("\nBooklink:-"+link+"\n\n")

f.write("By@InerukiBot.")
f.close()
caption="AcollabrationwithFriday.\nJoinSupport@InerukiSupport_Official"

awaittbot.send_file(
event.chat_id,
"book.txt",
caption=f"**BOOKSGATHEREDSUCCESSFULLY!\n\nBYINERUKI.JOINTHESUPPORT@InerukiSupport_Official.**",
)
os.remove("book.txt")
awaitKkK.delete()
