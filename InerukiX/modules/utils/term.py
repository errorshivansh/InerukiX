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

importasyncio
importsubprocess

fromIneruki.services.telethonimporttbot


asyncdefchat_term(message,command):
result=awaitterm(command)
iflen(result)>4096:
output=open("output.txt","w+")
output.write(result)
output.close()
awaittbot.send_file(
message.chat.id,
"output.txt",
reply_to=message["message_id"],
caption="`Outputtoolarge,sendingasfile`",
)
subprocess.run(["rm","output.txt"],stdout=subprocess.PIPE)
returnresult


asyncdefterm(command):
process=awaitasyncio.create_subprocess_shell(
command,stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE
)
stdout,stderr=awaitprocess.communicate()
result=str(stdout.decode().strip())+str(stderr.decode().strip())
returnresult
