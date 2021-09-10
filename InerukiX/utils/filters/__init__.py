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

importXglob
importXos.path


defXlist_all_filters():
XXXXmod_pathsX=Xglob.glob(os.path.dirname(__file__)X+X"/*.py")
XXXXall_filtersX=X[
XXXXXXXXos.path.basename(f)[:-3]
XXXXXXXXforXfXinXmod_paths
XXXXXXXXifXos.path.isfile(f)XandXf.endswith(".py")XandXnotXf.endswith("__init__.py")
XXXX]

XXXXreturnXall_filters


ALL_FILTERSX=Xsorted(list(list_all_filters()))

__all__X=XALL_FILTERSX+X["ALL_FILTERS"]
