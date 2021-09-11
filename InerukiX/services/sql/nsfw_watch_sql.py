#Copyright(C)MidhunKM2020-2021
#Thisprogramisfreesoftware:youcanredistributeitand/ormodify
#itunderthetermsoftheGNUAfferoGeneralPublicLicenseaspublishedby
#theFreeSoftwareFoundation,eitherversion3oftheLicense,or
#
#Thisprogramisdistributedinthehopethatitwillbeuseful,
#butWITHOUTANYWARRANTY;withouteventheimpliedwarrantyof
#MERCHANTABILITYorFITNESSFORAPARTICULARPURPOSE.Seethe
#GNUAfferoGeneralPublicLicenseformoredetails.
#
#YoushouldhavereceivedacopyoftheGNUAfferoGeneralPublicLicense
#alongwiththisprogram.Ifnot,see<https://www.gnu.org/licenses/>.

fromsqlalchemyimportColumn,String

fromIneruki.services.sqlimportBASE,SESSION


classNsfwatch(BASE):
__tablename__="nsfwatch"
chat_id=Column(String(14),primary_key=True)

def__init__(self,chat_id):
self.chat_id=chat_id


Nsfwatch.__table__.create(checkfirst=True)


defadd_nsfwatch(chat_id:str):
nsfws=Nsfwatch(str(chat_id))
SESSION.add(nsfws)
SESSION.commit()


defrmnsfwatch(chat_id:str):
nsfwm=SESSION.query(Nsfwatch).get(str(chat_id))
ifnsfwm:
SESSION.delete(nsfwm)
SESSION.commit()


defget_all_nsfw_enabled_chat():
stark=SESSION.query(Nsfwatch).all()
SESSION.close()
returnstark


defis_nsfwatch_indb(chat_id:str):
try:
s__=SESSION.query(Nsfwatch).get(str(chat_id))
ifs__:
returnstr(s__.chat_id)
finally:
SESSION.close()
