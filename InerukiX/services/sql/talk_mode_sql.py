#Copyright(C)InukaAsith2021
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


classTalkmode(BASE):
__tablename__="talkmode"
chat_id=Column(String(14),primary_key=True)

def__init__(self,chat_id):
self.chat_id=chat_id


Talkmode.__table__.create(checkfirst=True)


defadd_talkmode(chat_id:str):
talkmoddy=Talkmode(str(chat_id))
SESSION.add(talkmoddy)
SESSION.commit()


defrmtalkmode(chat_id:str):
rmtalkmoddy=SESSION.query(Talkmode).get(str(chat_id))
ifrmtalkmoddy:
SESSION.delete(rmtalkmoddy)
SESSION.commit()


defget_all_chat_id():
stark=SESSION.query(Talkmode).all()
SESSION.close()
returnstark


defis_talkmode_indb(chat_id:str):
try:
s__=SESSION.query(Talkmode).get(str(chat_id))
ifs__:
returnstr(s__.chat_id)
finally:
SESSION.close()
