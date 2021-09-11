#ThisfileispartofIneruki(TelegramBot)

#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseas
#publishedbytheFreeSoftwareFoundation,eitherversion3ofthe
#License,or(atyouroption)anylaterversion.

#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.

#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<http://www.gnu.org/licenses/>.

importos

importyaml
frombabel.coreimportLocale

fromIneruki.services.mongoimportdb
fromIneruki.services.redisimportredis
fromIneruki.utils.loggerimportlog

LANGUAGES={}

log.info("Loadinglocalizations...")

forfilenameinos.listdir("Ineruki/localization"):
log.debug("Loadinglanguagefile"+filename)
withopen("Ineruki/localization/"+filename,"r",encoding="utf8")asf:
lang=yaml.load(f,Loader=yaml.CLoader)

lang_code=lang["language_info"]["code"]
lang["language_info"]["babel"]=Locale(lang_code)

LANGUAGES[lang_code]=lang

log.info(
"Languagesloaded:{}".format(
[
language["language_info"]["babel"].display_name
forlanguageinLANGUAGES.values()
]
)
)


asyncdefget_chat_lang(chat_id):
r=redis.get("lang_cache_{}".format(chat_id))
ifr:
returnr
else:
db_lang=awaitdb.lang.find_one({"chat_id":chat_id})
ifdb_lang:
#Rebuildlangcache
redis.set("lang_cache_{}".format(chat_id),db_lang["lang"])
returndb_lang["lang"]
user_lang=awaitdb.user_list.find_one({"user_id":chat_id})
ifuser_langanduser_lang["user_lang"]inLANGUAGES:
#Addtelegramlanguageinlangcache
redis.set("lang_cache_{}".format(chat_id),user_lang["user_lang"])
returnuser_lang["user_lang"]
else:
return"en"


asyncdefchange_chat_lang(chat_id,lang):
redis.set("lang_cache_{}".format(chat_id),lang)
awaitdb.lang.update_one(
{"chat_id":chat_id},{"$set":{"chat_id":chat_id,"lang":lang}},upsert=True
)


asyncdefget_strings(chat_id,module,mas_name="STRINGS"):
chat_lang=awaitget_chat_lang(chat_id)
ifchat_langnotinLANGUAGES:
awaitchange_chat_lang(chat_id,"en")

classStrings:
@staticmethod
defget_strings(lang,mas_name,module):

if(
mas_namenotinLANGUAGES[lang]
ormodulenotinLANGUAGES[lang][mas_name]
):
return{}

data=LANGUAGES[lang][mas_name][module]

ifmas_name=="STRINGS":
data["language_info"]=LANGUAGES[chat_lang]["language_info"]
returndata

defget_string(self,name):
data=self.get_strings(chat_lang,mas_name,module)
ifnamenotindata:
data=self.get_strings("en",mas_name,module)

returndata[name]

def__getitem__(self,key):
returnself.get_string(key)

returnStrings()


asyncdefget_string(chat_id,module,name,mas_name="STRINGS"):
strings=awaitget_strings(chat_id,module,mas_name=mas_name)
returnstrings[name]


defget_strings_dec(module,mas_name="STRINGS"):
defwrapped(func):
asyncdefwrapped_1(*args,**kwargs):
message=args[0]
ifhasattr(message,"chat"):
chat_id=message.chat.id
elifhasattr(message,"message"):
chat_id=message.message.chat.id
else:
chat_id=None

strings=awaitget_strings(chat_id,module,mas_name=mas_name)
returnawaitfunc(*args,strings,**kwargs)

returnwrapped_1

returnwrapped


asyncdefget_chat_lang_info(chat_id):
chat_lang=awaitget_chat_lang(chat_id)
returnLANGUAGES[chat_lang]["language_info"]
