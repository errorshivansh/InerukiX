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
importXsubprocess

fromXInerukiX.services.telethonXimportXtbot


asyncXdefXchat_term(message,Xcommand):
XXXXresultX=XawaitXterm(command)
XXXXifXlen(result)X>X4096:
XXXXXXXXoutputX=Xopen("output.txt",X"w+")
XXXXXXXXoutput.write(result)
XXXXXXXXoutput.close()
XXXXXXXXawaitXtbot.send_file(
XXXXXXXXXXXXmessage.chat.id,
XXXXXXXXXXXX"output.txt",
XXXXXXXXXXXXreply_to=message["message_id"],
XXXXXXXXXXXXcaption="`OutputXtooXlarge,XsendingXasXfile`",
XXXXXXXX)
XXXXXXXXsubprocess.run(["rm",X"output.txt"],Xstdout=subprocess.PIPE)
XXXXreturnXresult


asyncXdefXterm(command):
XXXXprocessX=XawaitXasyncio.create_subprocess_shell(
XXXXXXXXcommand,Xstdout=asyncio.subprocess.PIPE,Xstderr=asyncio.subprocess.PIPE
XXXX)
XXXXstdout,XstderrX=XawaitXprocess.communicate()
XXXXresultX=Xstr(stdout.decode().strip())X+Xstr(stderr.decode().strip())
XXXXreturnXresult
