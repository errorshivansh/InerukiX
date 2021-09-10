#XCopyrightX(C)X2020XDevsExpo
#XCopyrightX(C)X2021XInukaXAsith
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


importXos
importXre

importXrequests
fromXbs4XimportXBeautifulSoup
fromXtelethonXimportXevents

fromXInerukiX.services.telethonXimportXtbot


@tbot.on(events.NewMessage(pattern="^/bookX(.*)"))
asyncXdefX_(event):
XXXXifXevent.fwd_from:
XXXXXXXXreturn
XXXXinput_strX=Xevent.pattern_match.group(1)
XXXXloolX=X0
XXXXKkKX=XawaitXevent.reply("searchingXforXtheXbook...")
XXXXlinX=X"https://b-ok.cc/s/"
XXXXtextX=Xinput_str
XXXXlinkX=XlinX+Xtext

XXXXheadersX=X[
XXXXXXXX"User-Agent",
XXXXXXXX"Mozilla/5.0X(Macintosh;XIntelXMacXOSXXX10.15;Xrv:74.0)XGecko/20100101XFirefox/74.0",
XXXX]
XXXXpageX=Xrequests.get(link)
XXXXsoupX=XBeautifulSoup(page.content,X"html.parser")
XXXXfX=Xopen("book.txt",X"w")
XXXXtotalX=Xsoup.find(class_="totalCounter")
XXXXforXnbXinXtotal.descendants:
XXXXXXXXnbxX=Xnb.replace("(",X"").replace(")",X"")
XXXXifXnbxX==X"0":
XXXXXXXXawaitXevent.reply("NoXBooksXFoundXwithXthatXname.")
XXXXelse:

XXXXXXXXforXtrXinXsoup.find_all("td"):
XXXXXXXXXXXXforXtdXinXtr.find_all("h3"):
XXXXXXXXXXXXXXXXforXtsXinXtd.find_all("a"):
XXXXXXXXXXXXXXXXXXXXtitleX=Xts.get_text()
XXXXXXXXXXXXXXXXXXXXloolX=XloolX+X1
XXXXXXXXXXXXXXXXforXtsXinXtd.find_all("a",Xattrs={"href":Xre.compile("^/book/")}):
XXXXXXXXXXXXXXXXXXXXrefX=Xts.get("href")
XXXXXXXXXXXXXXXXXXXXlinkX=X"https://b-ok.cc"X+Xref

XXXXXXXXXXXXXXXXf.write("\n"X+Xtitle)
XXXXXXXXXXXXXXXXf.write("\nBookXlink:-X"X+XlinkX+X"\n\n")

XXXXXXXXf.write("ByX@InerukiXBot.")
XXXXXXXXf.close()
XXXXXXXXcaptionX=X"AXcollabrationXwithXFriday.\nXJoinXSupportX@InerukiSupport_Official"

XXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXevent.chat_id,
XXXXXXXXXXXX"book.txt",
XXXXXXXXXXXXcaption=f"**BOOKSXGATHEREDXSUCCESSFULLY!\n\nBYXINERUKIX.XJOINXTHEXSUPPORTX@InerukiSupport_Official.**",
XXXXXXXX)
XXXXXXXXos.remove("book.txt")
XXXXXXXXawaitXKkK.delete()
