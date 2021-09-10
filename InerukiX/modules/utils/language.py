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

importXyaml
fromXbabel.coreXimportXLocale

fromXInerukiX.services.mongoXimportXdb
fromXInerukiX.services.redisXimportXredis
fromXInerukiX.utils.loggerXimportXlog

LANGUAGESX=X{}

log.info("LoadingXlocalizations...")

forXfilenameXinXos.listdir("InerukiX/localization"):
XXXXlog.debug("LoadingXlanguageXfileX"X+Xfilename)
XXXXwithXopen("InerukiX/localization/"X+Xfilename,X"r",Xencoding="utf8")XasXf:
XXXXXXXXlangX=Xyaml.load(f,XLoader=yaml.CLoader)

XXXXXXXXlang_codeX=Xlang["language_info"]["code"]
XXXXXXXXlang["language_info"]["babel"]X=XLocale(lang_code)

XXXXXXXXLANGUAGES[lang_code]X=Xlang

log.info(
XXXX"LanguagesXloaded:X{}".format(
XXXXXXXX[
XXXXXXXXXXXXlanguage["language_info"]["babel"].display_name
XXXXXXXXXXXXforXlanguageXinXLANGUAGES.values()
XXXXXXXX]
XXXX)
)


asyncXdefXget_chat_lang(chat_id):
XXXXrX=Xredis.get("lang_cache_{}".format(chat_id))
XXXXifXr:
XXXXXXXXreturnXr
XXXXelse:
XXXXXXXXdb_langX=XawaitXdb.lang.find_one({"chat_id":Xchat_id})
XXXXXXXXifXdb_lang:
XXXXXXXXXXXX#XRebuildXlangXcache
XXXXXXXXXXXXredis.set("lang_cache_{}".format(chat_id),Xdb_lang["lang"])
XXXXXXXXXXXXreturnXdb_lang["lang"]
XXXXXXXXuser_langX=XawaitXdb.user_list.find_one({"user_id":Xchat_id})
XXXXXXXXifXuser_langXandXuser_lang["user_lang"]XinXLANGUAGES:
XXXXXXXXXXXX#XAddXtelegramXlanguageXinXlangXcache
XXXXXXXXXXXXredis.set("lang_cache_{}".format(chat_id),Xuser_lang["user_lang"])
XXXXXXXXXXXXreturnXuser_lang["user_lang"]
XXXXXXXXelse:
XXXXXXXXXXXXreturnX"en"


asyncXdefXchange_chat_lang(chat_id,Xlang):
XXXXredis.set("lang_cache_{}".format(chat_id),Xlang)
XXXXawaitXdb.lang.update_one(
XXXXXXXX{"chat_id":Xchat_id},X{"$set":X{"chat_id":Xchat_id,X"lang":Xlang}},Xupsert=True
XXXX)


asyncXdefXget_strings(chat_id,Xmodule,Xmas_name="STRINGS"):
XXXXchat_langX=XawaitXget_chat_lang(chat_id)
XXXXifXchat_langXnotXinXLANGUAGES:
XXXXXXXXawaitXchange_chat_lang(chat_id,X"en")

XXXXclassXStrings:
XXXXXXXX@staticmethod
XXXXXXXXdefXget_strings(lang,Xmas_name,Xmodule):

XXXXXXXXXXXXifX(
XXXXXXXXXXXXXXXXmas_nameXnotXinXLANGUAGES[lang]
XXXXXXXXXXXXXXXXorXmoduleXnotXinXLANGUAGES[lang][mas_name]
XXXXXXXXXXXX):
XXXXXXXXXXXXXXXXreturnX{}

XXXXXXXXXXXXdataX=XLANGUAGES[lang][mas_name][module]

XXXXXXXXXXXXifXmas_nameX==X"STRINGS":
XXXXXXXXXXXXXXXXdata["language_info"]X=XLANGUAGES[chat_lang]["language_info"]
XXXXXXXXXXXXreturnXdata

XXXXXXXXdefXget_string(self,Xname):
XXXXXXXXXXXXdataX=Xself.get_strings(chat_lang,Xmas_name,Xmodule)
XXXXXXXXXXXXifXnameXnotXinXdata:
XXXXXXXXXXXXXXXXdataX=Xself.get_strings("en",Xmas_name,Xmodule)

XXXXXXXXXXXXreturnXdata[name]

XXXXXXXXdefX__getitem__(self,Xkey):
XXXXXXXXXXXXreturnXself.get_string(key)

XXXXreturnXStrings()


asyncXdefXget_string(chat_id,Xmodule,Xname,Xmas_name="STRINGS"):
XXXXstringsX=XawaitXget_strings(chat_id,Xmodule,Xmas_name=mas_name)
XXXXreturnXstrings[name]


defXget_strings_dec(module,Xmas_name="STRINGS"):
XXXXdefXwrapped(func):
XXXXXXXXasyncXdefXwrapped_1(*args,X**kwargs):
XXXXXXXXXXXXmessageX=Xargs[0]
XXXXXXXXXXXXifXhasattr(message,X"chat"):
XXXXXXXXXXXXXXXXchat_idX=Xmessage.chat.id
XXXXXXXXXXXXelifXhasattr(message,X"message"):
XXXXXXXXXXXXXXXXchat_idX=Xmessage.message.chat.id
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXchat_idX=XNone

XXXXXXXXXXXXstringsX=XawaitXget_strings(chat_id,Xmodule,Xmas_name=mas_name)
XXXXXXXXXXXXreturnXawaitXfunc(*args,Xstrings,X**kwargs)

XXXXXXXXreturnXwrapped_1

XXXXreturnXwrapped


asyncXdefXget_chat_lang_info(chat_id):
XXXXchat_langX=XawaitXget_chat_lang(chat_id)
XXXXreturnXLANGUAGES[chat_lang]["language_info"]
