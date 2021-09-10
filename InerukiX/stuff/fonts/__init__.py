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


defXlist_all_fonts():
XXXXimportXglob
XXXXfromXos.pathXimportXbasename,Xdirname,Xisfile

XXXXmod_pathsX=Xglob.glob(dirname(__file__)X+X"/*.ttf")
XXXXall_fontsX=X[
XXXXXXXXdirname(f)X+X"/"X+Xbasename(f)
XXXXXXXXforXfXinXmod_paths
XXXXXXXXifXisfile(f)XandXf.endswith(".ttf")
XXXX]
XXXXreturnXall_fonts


ALL_FONTSX=Xsorted(list_all_fonts())
__all__X=XALL_FONTSX+X["ALL_FONTS"]
