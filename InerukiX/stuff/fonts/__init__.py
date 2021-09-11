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


deflist_all_fonts():
importglob
fromos.pathimportbasename,dirname,isfile

mod_paths=glob.glob(dirname(__file__)+"/*.ttf")
all_fonts=[
dirname(f)+"/"+basename(f)
forfinmod_paths
ifisfile(f)andf.endswith(".ttf")
]
returnall_fonts


ALL_FONTS=sorted(list_all_fonts())
__all__=ALL_FONTS+["ALL_FONTS"]
