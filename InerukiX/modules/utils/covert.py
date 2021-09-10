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

importXmath


defXconvert_size(size_bytes):
XXXXifXsize_bytesX==X0:
XXXXXXXXreturnX"0B"
XXXXsize_nameX=X("B",X"KB",X"MB",X"GB",X"TB",X"PB",X"EB",X"ZB",X"YB")
XXXXiX=Xint(math.floor(math.log(size_bytes,X1024)))
XXXXpX=Xmath.pow(1024,Xi)
XXXXsX=Xround(size_bytesX/Xp,X2)
XXXXreturnX"%sX%s"X%X(s,Xsize_name[i])
