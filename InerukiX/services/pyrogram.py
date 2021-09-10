#XThisXfileXisXpartXofXInerukiXBotX(TelegramXBot)

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
importXlogging

fromXpyrogramXimportXClient

#XfromXpyromodXimportXlisten
fromXInerukiX.configXimportXget_int_key,Xget_str_key

TOKENX=Xget_str_key("TOKEN",Xrequired=True)
APP_IDX=Xget_int_key("APP_ID",Xrequired=True)
APP_HASHX=Xget_str_key("APP_HASH",Xrequired=True)
session_nameX=XTOKEN.split(":")[0]
pbotX=XClient(
XXXXsession_name,
XXXXapi_id=APP_ID,
XXXXapi_hash=APP_HASH,
XXXXbot_token=TOKEN,
)

#XdisableXloggingXforXpyrogramX[notXforXERRORXlogging]
logging.getLogger("pyrogram").setLevel(level=logging.ERROR)

pbot.start()
