#XXXXMissJuliaRobotX(AXTelegramXBotXProject)
#XXXXCopyrightX(C)X2019-PresentXAnonymousX(https://t.me/MissJulia_Robot)

#XXXXThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XXXXitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXasXpublishedXby
#XXXXtheXFreeXSoftwareXFoundation,XinXversionX3XofXtheXLicense.

#XXXXThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XXXXbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XXXXMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XXXXGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.

#XXXXYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XXXXalongXwithXthisXprogram.XXIfXnot,XseeX<Xhttps://www.gnu.org/licenses/agpl-3.0.en.htmlX>


importXthreading

fromXsqlalchemyXimportXColumn,XString,XUnicodeText

fromXInerukiX.services.sqlXimportXBASE,XSESSION


classXURLBlackListFilters(BASE):
XXXX__tablename__X=X"url_blacklist"
XXXXchat_idX=XColumn(String(14),Xprimary_key=True)
XXXXdomainX=XColumn(UnicodeText,Xprimary_key=True,Xnullable=False)

XXXXdefX__init__(self,Xchat_id,Xdomain):
XXXXXXXXself.chat_idX=Xstr(chat_id)
XXXXXXXXself.domainX=Xstr(domain)


URLBlackListFilters.__table__.create(checkfirst=True)

URL_BLACKLIST_FILTER_INSERTION_LOCKX=Xthreading.RLock()

CHAT_URL_BLACKLISTSX=X{}


defXblacklist_url(chat_id,Xdomain):
XXXXwithXURL_BLACKLIST_FILTER_INSERTION_LOCK:
XXXXXXXXdomain_filtX=XURLBlackListFilters(str(chat_id),Xdomain)

XXXXXXXXSESSION.merge(domain_filt)
XXXXXXXXSESSION.commit()
XXXXXXXXCHAT_URL_BLACKLISTS.setdefault(str(chat_id),Xset()).add(domain)


defXrm_url_from_blacklist(chat_id,Xdomain):
XXXXwithXURL_BLACKLIST_FILTER_INSERTION_LOCK:
XXXXXXXXdomain_filtX=XSESSION.query(URLBlackListFilters).get((str(chat_id),Xdomain))
XXXXXXXXifXdomain_filt:
XXXXXXXXXXXXifXdomainXinXCHAT_URL_BLACKLISTS.get(str(chat_id),Xset()):
XXXXXXXXXXXXXXXXCHAT_URL_BLACKLISTS.get(str(chat_id),Xset()).remove(domain)
XXXXXXXXXXXXSESSION.delete(domain_filt)
XXXXXXXXXXXXSESSION.commit()
XXXXXXXXXXXXreturnXTrue

XXXXXXXXSESSION.close()
XXXXXXXXreturnXFalse


defXget_blacklisted_urls(chat_id):
XXXXreturnXCHAT_URL_BLACKLISTS.get(str(chat_id),Xset())


defX_load_chat_blacklist():
XXXXglobalXCHAT_URL_BLACKLISTS
XXXXtry:
XXXXXXXXchatsX=XSESSION.query(URLBlackListFilters.chat_id).distinct().all()
XXXXXXXXforX(chat_id,)XinXchats:
XXXXXXXXXXXXCHAT_URL_BLACKLISTS[chat_id]X=X[]

XXXXXXXXall_urlsX=XSESSION.query(URLBlackListFilters).all()
XXXXXXXXforXurlXinXall_urls:
XXXXXXXXXXXXCHAT_URL_BLACKLISTS[url.chat_id]X+=X[url.domain]
XXXXXXXXCHAT_URL_BLACKLISTSX=X{k:Xset(v)XforXk,XvXinXCHAT_URL_BLACKLISTS.items()}
XXXXfinally:
XXXXXXXXSESSION.close()


_load_chat_blacklist()
