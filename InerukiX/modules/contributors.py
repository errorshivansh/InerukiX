#Copyright(C)2021ProgrammingError

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

importgithub#pyGithub
frompyrogramimportfilters

fromIneruki.services.pyrogramimportpbotasclient


@client.on_message(filters.command("contributors")&~filters.edited)
asyncdefgive_cobtribs(c,m):
g=github.Github()
co=""
n=0
repo=g.get_repo("errorshivansh/Ineruki")
foriinrepo.get_contributors():
n+=1
co+=f"{n}.[{i.login}](https://github.com/{i.login})\n"
t=f"**InerukiContributors**\n\n{co}"
awaitm.reply(t,disable_web_page_preview=True)
