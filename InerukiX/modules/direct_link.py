#Copyright(C)2021errorshivansh


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

importre
fromrandomimportchoice

importrequests
frombs4importBeautifulSoup

fromIneruki.decoratorimportregister

from.utils.disableimportdisableable_dec
from.utils.messageimportget_arg


@register(cmds="direct")
@disableable_dec("direct")
asyncdefdirect_link_generator(message):
text=get_arg(message)

ifnottext:
m="Usage:<code>/direct(url)</code>"
awaitmessage.reply(m)
return

iftext:
links=re.findall(r"\bhttps?://.*\.\S+",text)
else:
return

reply=[]
ifnotlinks:
awaitmessage.reply("Nolinksfound!")
return

forlinkinlinks:
if"sourceforge.net"inlink:
reply.append(sourceforge(link))
else:
reply.append(
re.findall(r"\bhttps?://(.*?[^/]+)",link)[0]+"isnotsupported"
)

awaitmessage.reply("\n".join(reply))


defsourceforge(url:str)->str:
try:
link=re.findall(r"\bhttps?://.*sourceforge\.net\S+",url)[0]
exceptIndexError:
reply="NoSourceForgelinksfound\n"
returnreply

file_path=re.findall(r"/files(.*)/download",link)
ifnotfile_path:
file_path=re.findall(r"/files(.*)",link)
file_path=file_path[0]
reply=f"Mirrorsfor<code>{file_path.split('/')[-1]}</code>\n"
project=re.findall(r"projects?/(.*?)/files",link)[0]
mirrors=(
f"https://sourceforge.net/settings/mirror_choices?"
f"projectname={project}&filename={file_path}"
)
page=BeautifulSoup(requests.get(mirrors).content,"lxml")
info=page.find("ul",{"id":"mirrorList"}).findAll("li")

formirrorininfo[1:]:
name=re.findall(r"\((.*)\)",mirror.text.strip())[0]
dl_url=(
f'https://{mirror["id"]}.dl.sourceforge.net/project/{project}/{file_path}'
)
reply+=f'<ahref="{dl_url}">{name}</a>'
returnreply


defuseragent():
useragents=BeautifulSoup(
requests.get(
"https://developers.whatismybrowser.com/"
"useragents/explore/operating_system_name/android/"
).content,
"lxml",
).findAll("td",{"class":"useragent"})
user_agent=choice(useragents)
returnuser_agent.text
