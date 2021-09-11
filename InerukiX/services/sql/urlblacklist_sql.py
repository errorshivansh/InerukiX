#MissJuliaRobot(ATelegramBotProject)
#Copyright(C)2019-PresentAnonymous(https://t.me/MissJulia_Robot)

#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseaspublishedby
#theFreeSoftwareFoundation,inversion3oftheLicense.

#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.

#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<https://www.gnu.org/licenses/agpl-3.0.en.html>


importthreading

fromsqlalchemyimportColumn,String,UnicodeText

fromIneruki.services.sqlimportBASE,SESSION


classURLBlackListFilters(BASE):
__tablename__="url_blacklist"
chat_id=Column(String(14),primary_key=True)
domain=Column(UnicodeText,primary_key=True,nullable=False)

def__init__(self,chat_id,domain):
self.chat_id=str(chat_id)
self.domain=str(domain)


URLBlackListFilters.__table__.create(checkfirst=True)

URL_BLACKLIST_FILTER_INSERTION_LOCK=threading.RLock()

CHAT_URL_BLACKLISTS={}


defblacklist_url(chat_id,domain):
withURL_BLACKLIST_FILTER_INSERTION_LOCK:
domain_filt=URLBlackListFilters(str(chat_id),domain)

SESSION.merge(domain_filt)
SESSION.commit()
CHAT_URL_BLACKLISTS.setdefault(str(chat_id),set()).add(domain)


defrm_url_from_blacklist(chat_id,domain):
withURL_BLACKLIST_FILTER_INSERTION_LOCK:
domain_filt=SESSION.query(URLBlackListFilters).get((str(chat_id),domain))
ifdomain_filt:
ifdomaininCHAT_URL_BLACKLISTS.get(str(chat_id),set()):
CHAT_URL_BLACKLISTS.get(str(chat_id),set()).remove(domain)
SESSION.delete(domain_filt)
SESSION.commit()
returnTrue

SESSION.close()
returnFalse


defget_blacklisted_urls(chat_id):
returnCHAT_URL_BLACKLISTS.get(str(chat_id),set())


def_load_chat_blacklist():
globalCHAT_URL_BLACKLISTS
try:
chats=SESSION.query(URLBlackListFilters.chat_id).distinct().all()
for(chat_id,)inchats:
CHAT_URL_BLACKLISTS[chat_id]=[]

all_urls=SESSION.query(URLBlackListFilters).all()
forurlinall_urls:
CHAT_URL_BLACKLISTS[url.chat_id]+=[url.domain]
CHAT_URL_BLACKLISTS={k:set(v)fork,vinCHAT_URL_BLACKLISTS.items()}
finally:
SESSION.close()


_load_chat_blacklist()
