#XCopyrightX(C)X2021Xerrorshivansh


#XThisXfileXisXpartXofXInerukiX(TelegramXBot)

#XThisXprogramXisXfreeXsoftware:XyouXcanXredistributeXitXand/orXmodify
#XitXunderXtheXtermsXofXtheXGNUXAfferoXGeneralXPublicXLicenseXas
#XpublishedXbyXtheXFreeXSoftwareXFoundation,XeitherXversionX3XofXthe
#XLicense,XorX(atXyourXoption)XanyXlaterXversion.

#XThisXprogramXisXdistributedXinXtheXhopeXthatXitXwillXbeXuseful,
#XbutXWITHOUTXANYXWARRANTY;XwithoutXevenXtheXimpliedXwarrantyXof
#XMERCHANTABILITYXorXFITNESSXFORXAXPARTICULARXPURPOSE.XXSeeXthe
#XGNUXAfferoXGeneralXPublicXLicenseXforXmoreXdetails.

#XYouXshouldXhaveXreceivedXaXcopyXofXtheXGNUXAfferoXGeneralXPublicXLicense
#XalongXwithXthisXprogram.XXIfXnot,XseeX<http://www.gnu.org/licenses/>.

importXre
fromXrandomXimportXchoice

importXrequests
fromXbs4XimportXBeautifulSoup

fromXInerukiX.decoratorXimportXregister

fromX.utils.disableXimportXdisableable_dec
fromX.utils.messageXimportXget_arg


@register(cmds="direct")
@disableable_dec("direct")
asyncXdefXdirect_link_generator(message):
XXXXtextX=Xget_arg(message)

XXXXifXnotXtext:
XXXXXXXXmX=X"Usage:X<code>/directX(url)</code>"
XXXXXXXXawaitXmessage.reply(m)
XXXXXXXXreturn

XXXXifXtext:
XXXXXXXXlinksX=Xre.findall(r"\bhttps?://.*\.\S+",Xtext)
XXXXelse:
XXXXXXXXreturn

XXXXreplyX=X[]
XXXXifXnotXlinks:
XXXXXXXXawaitXmessage.reply("NoXlinksXfound!")
XXXXXXXXreturn

XXXXforXlinkXinXlinks:
XXXXXXXXifX"sourceforge.net"XinXlink:
XXXXXXXXXXXXreply.append(sourceforge(link))
XXXXXXXXelse:
XXXXXXXXXXXXreply.append(
XXXXXXXXXXXXXXXXre.findall(r"\bhttps?://(.*?[^/]+)",Xlink)[0]X+X"XisXnotXsupported"
XXXXXXXXXXXX)

XXXXawaitXmessage.reply("\n".join(reply))


defXsourceforge(url:Xstr)X->Xstr:
XXXXtry:
XXXXXXXXlinkX=Xre.findall(r"\bhttps?://.*sourceforge\.net\S+",Xurl)[0]
XXXXexceptXIndexError:
XXXXXXXXreplyX=X"NoXSourceForgeXlinksXfound\n"
XXXXXXXXreturnXreply

XXXXfile_pathX=Xre.findall(r"/files(.*)/download",Xlink)
XXXXifXnotXfile_path:
XXXXXXXXfile_pathX=Xre.findall(r"/files(.*)",Xlink)
XXXXfile_pathX=Xfile_path[0]
XXXXreplyX=Xf"MirrorsXforX<code>{file_path.split('/')[-1]}</code>\n"
XXXXprojectX=Xre.findall(r"projects?/(.*?)/files",Xlink)[0]
XXXXmirrorsX=X(
XXXXXXXXf"https://sourceforge.net/settings/mirror_choices?"
XXXXXXXXf"projectname={project}&filename={file_path}"
XXXX)
XXXXpageX=XBeautifulSoup(requests.get(mirrors).content,X"lxml")
XXXXinfoX=Xpage.find("ul",X{"id":X"mirrorList"}).findAll("li")

XXXXforXmirrorXinXinfo[1:]:
XXXXXXXXnameX=Xre.findall(r"\((.*)\)",Xmirror.text.strip())[0]
XXXXXXXXdl_urlX=X(
XXXXXXXXXXXXf'https://{mirror["id"]}.dl.sourceforge.net/project/{project}/{file_path}'
XXXXXXXX)
XXXXXXXXreplyX+=Xf'<aXhref="{dl_url}">{name}</a>X'
XXXXreturnXreply


defXuseragent():
XXXXuseragentsX=XBeautifulSoup(
XXXXXXXXrequests.get(
XXXXXXXXXXXX"https://developers.whatismybrowser.com/"
XXXXXXXXXXXX"useragents/explore/operating_system_name/android/"
XXXXXXXX).content,
XXXXXXXX"lxml",
XXXX).findAll("td",X{"class":X"useragent"})
XXXXuser_agentX=Xchoice(useragents)
XXXXreturnXuser_agent.text
