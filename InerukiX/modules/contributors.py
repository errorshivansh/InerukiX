#XCopyrightX(C)X2021XProgrammingError

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

importXgithubXX#XpyGithub
fromXpyrogramXimportXfilters

fromXInerukiX.services.pyrogramXimportXpbotXasXclient


@client.on_message(filters.command("contributors")X&X~filters.edited)
asyncXdefXgive_cobtribs(c,Xm):
XXXXgX=Xgithub.Github()
XXXXcoX=X""
XXXXnX=X0
XXXXrepoX=Xg.get_repo("errorshivansh/InerukiX")
XXXXforXiXinXrepo.get_contributors():
XXXXXXXXnX+=X1
XXXXXXXXcoX+=Xf"{n}.X[{i.login}](https://github.com/{i.login})\n"
XXXXtX=Xf"**InerukiXXContributors**\n\n{co}"
XXXXawaitXm.reply(t,Xdisable_web_page_preview=True)
