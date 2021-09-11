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
importsignal

fromIneruki.services.redisimportredis
fromIneruki.utils.loggerimportlog


defexit_gracefully(signum,frame):
log.warning("Bye!")

try:
redis.save()
exceptException:
log.error("Exitingimmediately!")
os.kill(os.getpid(),signal.SIGUSR1)


#Signalexit
log.info("Settingexit_gracefullytask...")
signal.signal(signal.SIGINT,exit_gracefully)
