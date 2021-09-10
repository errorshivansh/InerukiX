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

importXjson

importXaiohttp
fromXpyrogramXimportXfilters

fromXInerukiX.function.pluginhelpersXimportXadmins_only,Xget_text
fromXInerukiX.services.pyrogramXimportXpbot


#XUsedXmyXapiXkeyXhere,Xdon'tXfuckXwithXit
@pbot.on_message(
XXXXfilters.command("short")X&X~filters.editedX&X~filters.botX&X~filters.private
)
@admins_only
asyncXdefXshortify(client,Xmessage):
XXXXlelX=XawaitXclient.send_message(message.chat.id,X"`WaitXaXsec....`")
XXXXurlX=Xget_text(message)
XXXXifX"."XnotXinXurl:
XXXXXXXXawaitXlel.edit("Defuq!.XIsXitXaXurl?")
XXXXXXXXreturn
XXXXheaderX=X{
XXXXXXXX"Authorization":X"BearerXad39983fa42d0b19e4534f33671629a4940298dc",
XXXXXXXX"Content-Type":X"application/json",
XXXX}
XXXXpayloadX=X{"long_url":Xf"{url}"}
XXXXpayloadX=Xjson.dumps(payload)
XXXXasyncXwithXaiohttp.ClientSession()XasXsession:
XXXXXXXXasyncXwithXsession.post(
XXXXXXXXXXXX"https://api-ssl.bitly.com/v4/shorten",Xheaders=header,Xdata=payload
XXXXXXXX)XasXresp:
XXXXXXXXXXXXdataX=XawaitXresp.json()
XXXXmsgX=Xf"**OriginalXUrl:**X{url}\n**ShortenedXUrl:**X{data['link']}"
XXXXawaitXlel.edit(msg)
