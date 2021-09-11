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

importglob
importos.path


deflist_all_filters():
mod_paths=glob.glob(os.path.dirname(__file__)+"/*.py")
all_filters=[
os.path.basename(f)[:-3]
forfinmod_paths
ifos.path.isfile(f)andf.endswith(".py")andnotf.endswith("__init__.py")
]

returnall_filters


ALL_FILTERS=sorted(list(list_all_filters()))

__all__=ALL_FILTERS+["ALL_FILTERS"]
