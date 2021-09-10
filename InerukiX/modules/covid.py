#XCopyrightX(C)X2021XTheHamkerCat
#XEditedXbyXerrorshivansh

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

fromXpyrogramXimportXfilters

fromXInerukiX.function.pluginhelpersXimportXfetch,Xjson_prettify
fromXInerukiX.services.pyrogramXimportXpbotXasXapp


@app.on_message(filters.command("covid")X&X~filters.edited)
asyncXdefXcovid(_,Xmessage):
XXXXifXlen(message.command)X==X1:
XXXXXXXXdataX=XawaitXfetch("https://corona.lmao.ninja/v2/all")
XXXXXXXXdataX=XawaitXjson_prettify(data)
XXXXXXXXawaitXapp.send_message(message.chat.id,Xtext=data)
XXXXXXXXreturn
XXXXifXlen(message.command)X!=X1:
XXXXXXXXcountryX=Xmessage.text.split(None,X1)[1].strip()
XXXXXXXXcountryX=Xcountry.replace("X",X"")
XXXXXXXXdataX=XawaitXfetch(f"https://corona.lmao.ninja/v2/countries/{country}")
XXXXXXXXdataX=XawaitXjson_prettify(data)
XXXXXXXXawaitXapp.send_message(message.chat.id,Xtext=data)
XXXXXXXXreturn
