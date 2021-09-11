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


classNightmode(BASE):
__tablename__="nightmode"
chat_id=Column(String(14),primary_key=True)

def__init__(self,chat_id):
self.chat_id=chat_id


Nightmode.__table__.create(checkfirst=True)


defadd_nightmode(chat_id:str):
nightmoddy=Nightmode(str(chat_id))
SESSION.add(nightmoddy)
SESSION.commit()


defrmnightmode(chat_id:str):
rmnightmoddy=SESSION.query(Nightmode).get(str(chat_id))
ifrmnightmoddy:
SESSION.delete(rmnightmoddy)
SESSION.commit()


defget_all_chat_id():
stark=SESSION.query(Nightmode).all()
SESSION.close()
returnstark


defis_nightmode_indb(chat_id:str):
try:
s__=SESSION.query(Nightmode).get(str(chat_id))
ifs__:
returnstr(s__.chat_id)
finally:
SESSION.close()
