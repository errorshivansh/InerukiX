#XByX@TroJanzHEX
importXio
importXos
importXshutil

importXcv2
importXnumpyXasXnp
importXrequests
fromXPILXimportXImage,XImageDraw,XImageOps

fromXInerukiX.configXimportXget_str_key

RemoveBG_APIX=Xget_str_key("REM_BG_API_KEY",Xrequired=False)


asyncXdefXrotate_90(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"rotate_90.jpg"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXsrcX=Xcv2.imread(a)
XXXXXXXXXXXXimageX=Xcv2.rotate(src,Xcv2.cv2.ROTATE_90_CLOCKWISE)
XXXXXXXXXXXXcv2.imwrite(edit_img_loc,Ximage)
XXXXXXXXXXXXawaitXmessage.reply_chat_action("upload_photo")
XXXXXXXXXXXXawaitXmessage.reply_to_message.reply_photo(edit_img_loc,Xquote=True)
XXXXXXXXXXXXawaitXmsg.delete()
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply_text("WhyXdidXyouXdeleteXthat??")
XXXXXXXXtry:
XXXXXXXXXXXXshutil.rmtree(f"./DOWNLOADS/{userid}")
XXXXXXXXexceptXException:
XXXXXXXXXXXXpass
XXXXexceptXExceptionXasXe:
XXXXXXXXprint("rotate_90-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


asyncXdefXrotate_180(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"rotate_180.jpg"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXsrcX=Xcv2.imread(a)
XXXXXXXXXXXXimageX=Xcv2.rotate(src,Xcv2.ROTATE_180)
XXXXXXXXXXXXcv2.imwrite(edit_img_loc,Ximage)
XXXXXXXXXXXXawaitXmessage.reply_chat_action("upload_photo")
XXXXXXXXXXXXawaitXmessage.reply_to_message.reply_photo(edit_img_loc,Xquote=True)
XXXXXXXXXXXXawaitXmsg.delete()
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply_text("WhyXdidXyouXdeleteXthat??")
XXXXXXXXtry:
XXXXXXXXXXXXshutil.rmtree(f"./DOWNLOADS/{userid}")
XXXXXXXXexceptXException:
XXXXXXXXXXXXpass
XXXXexceptXExceptionXasXe:
XXXXXXXXprint("rotate_180-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


asyncXdefXrotate_270(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"rotate_270.jpg"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXsrcX=Xcv2.imread(a)
XXXXXXXXXXXXimageX=Xcv2.rotate(src,Xcv2.ROTATE_90_COUNTERCLOCKWISE)
XXXXXXXXXXXXcv2.imwrite(edit_img_loc,Ximage)
XXXXXXXXXXXXawaitXmessage.reply_chat_action("upload_photo")
XXXXXXXXXXXXawaitXmessage.reply_to_message.reply_photo(edit_img_loc,Xquote=True)
XXXXXXXXXXXXawaitXmsg.delete()
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply_text("WhyXdidXyouXdeleteXthat??")
XXXXXXXXtry:
XXXXXXXXXXXXshutil.rmtree(f"./DOWNLOADS/{userid}")
XXXXXXXXexceptXException:
XXXXXXXXXXXXpass
XXXXexceptXExceptionXasXe:
XXXXXXXXprint("rotate_270-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


defXresize_photo(photo:Xstr,Xuserid:Xstr)X->Xio.BytesIO:
XXXXimageX=XImage.open(photo)
XXXXmaxsizeX=X512
XXXXscaleX=XmaxsizeX/Xmax(image.width,Ximage.height)
XXXXnew_sizeX=X(int(image.widthX*Xscale),Xint(image.heightX*Xscale))
XXXXimageX=Ximage.resize(new_size,XImage.LANCZOS)
XXXXresized_photoX=Xio.BytesIO()
XXXXresized_photo.nameX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"resized.png"
XXXXimage.save(resized_photo,X"PNG")
XXXXreturnXresized_photo


asyncXdefXround_sticker(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"rounded.webp"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXresizedX=Xresize_photo(a,Xuserid)
XXXXXXXXXXXXimgX=XImage.open(resized).convert("RGB")
XXXXXXXXXXXXnpImageX=Xnp.array(img)
XXXXXXXXXXXXh,XwX=Ximg.size
XXXXXXXXXXXXalphaX=XImage.new("L",Ximg.size,X0)
XXXXXXXXXXXXdrawX=XImageDraw.Draw(alpha)
XXXXXXXXXXXXdraw.pieslice([0,X0,Xh,Xw],X0,X360,Xfill=255)
XXXXXXXXXXXXnpAlphaX=Xnp.array(alpha)
XXXXXXXXXXXXnpImageX=Xnp.dstack((npImage,XnpAlpha))
XXXXXXXXXXXXImage.fromarray(npImage).save(edit_img_loc)
XXXXXXXXXXXXawaitXmessage.reply_chat_action("upload_photo")
XXXXXXXXXXXXawaitXmessage.reply_to_message.reply_sticker(edit_img_loc,Xquote=True)
XXXXXXXXXXXXawaitXmsg.delete()
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply_text("WhyXdidXyouXdeleteXthat??")
XXXXXXXXtry:
XXXXXXXXXXXXshutil.rmtree(f"./DOWNLOADS/{userid}")
XXXXXXXXexceptXException:
XXXXXXXXXXXXpass
XXXXexceptXExceptionXasXe:
XXXXXXXXprint("round_sticker-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


asyncXdefXinverted(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"inverted.png"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXimageX=XImage.open(a)
XXXXXXXXXXXXinverted_imageX=XImageOps.invert(image)
XXXXXXXXXXXXinverted_image.save(edit_img_loc)
XXXXXXXXXXXXawaitXmessage.reply_chat_action("upload_photo")
XXXXXXXXXXXXawaitXmessage.reply_to_message.reply_photo(edit_img_loc,Xquote=True)
XXXXXXXXXXXXawaitXmsg.delete()
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply_text("WhyXdidXyouXdeleteXthat??")
XXXXXXXXtry:
XXXXXXXXXXXXshutil.rmtree(f"./DOWNLOADS/{userid}")
XXXXXXXXexceptXException:
XXXXXXXXXXXXpass
XXXXexceptXExceptionXasXe:
XXXXXXXXprint("inverted-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


asyncXdefXremovebg_plain(client,Xmessage):
XXXXtry:
XXXXXXXXifXnotX(RemoveBG_APIX==X""):
XXXXXXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"nobgplain.png"
XXXXXXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXawaitXclient.download_media(
XXXXXXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")

XXXXXXXXXXXXXXXXresponseX=Xrequests.post(
XXXXXXXXXXXXXXXXXXXX"https://api.remove.bg/v1.0/removebg",
XXXXXXXXXXXXXXXXXXXXfiles={"image_file":Xopen(download_location,X"rb")},
XXXXXXXXXXXXXXXXXXXXdata={"size":X"auto"},
XXXXXXXXXXXXXXXXXXXXheaders={"X-Api-Key":XRemoveBG_API},
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXifXresponse.status_codeX==X200:
XXXXXXXXXXXXXXXXXXXXwithXopen(f"{edit_img_loc}",X"wb")XasXout:
XXXXXXXXXXXXXXXXXXXXXXXXout.write(response.content)
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXXXXXX"CheckXifXyourXapiXisXcorrect",Xquote=True
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXreturn

XXXXXXXXXXXXXXXXawaitXmessage.reply_chat_action("upload_document")
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_document(edit_img_loc,Xquote=True)
XXXXXXXXXXXXXXXXawaitXmsg.delete()
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXawaitXmessage.reply_text("WhyXdidXyouXdeleteXthat??")
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXshutil.rmtree(f"./DOWNLOADS/{userid}")
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"GetXtheXapiXfromXhttps://www.remove.bg/b/background-removal-apiXandXaddXinXConfigXVar",
XXXXXXXXXXXXXXXXquote=True,
XXXXXXXXXXXXXXXXdisable_web_page_preview=True,
XXXXXXXXXXXX)
XXXXexceptXExceptionXasXe:
XXXXXXXXprint("removebg_plain-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


asyncXdefXremovebg_white(client,Xmessage):
XXXXtry:
XXXXXXXXifXnotX(RemoveBG_APIX==X""):
XXXXXXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"nobgwhite.png"
XXXXXXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXawaitXclient.download_media(
XXXXXXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")

XXXXXXXXXXXXXXXXresponseX=Xrequests.post(
XXXXXXXXXXXXXXXXXXXX"https://api.remove.bg/v1.0/removebg",
XXXXXXXXXXXXXXXXXXXXfiles={"image_file":Xopen(download_location,X"rb")},
XXXXXXXXXXXXXXXXXXXXdata={"size":X"auto"},
XXXXXXXXXXXXXXXXXXXXheaders={"X-Api-Key":XConfig.RemoveBG_API},
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXifXresponse.status_codeX==X200:
XXXXXXXXXXXXXXXXXXXXwithXopen(f"{edit_img_loc}",X"wb")XasXout:
XXXXXXXXXXXXXXXXXXXXXXXXout.write(response.content)
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXXXXXX"CheckXifXyourXapiXisXcorrect",Xquote=True
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXreturn

XXXXXXXXXXXXXXXXawaitXmessage.reply_chat_action("upload_photo")
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_photo(edit_img_loc,Xquote=True)
XXXXXXXXXXXXXXXXawaitXmsg.delete()
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXawaitXmessage.reply_text("WhyXdidXyouXdeleteXthat??")
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXshutil.rmtree(f"./DOWNLOADS/{userid}")
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"GetXtheXapiXfromXhttps://www.remove.bg/b/background-removal-apiXandXaddXinXConfigXVar",
XXXXXXXXXXXXXXXXquote=True,
XXXXXXXXXXXXXXXXdisable_web_page_preview=True,
XXXXXXXXXXXX)
XXXXexceptXExceptionXasXe:
XXXXXXXXprint("removebg_white-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


asyncXdefXremovebg_sticker(client,Xmessage):
XXXXtry:
XXXXXXXXifXnotX(RemoveBG_APIX==X""):
XXXXXXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"nobgsticker.webp"
XXXXXXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXawaitXclient.download_media(
XXXXXXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")

XXXXXXXXXXXXXXXXresponseX=Xrequests.post(
XXXXXXXXXXXXXXXXXXXX"https://api.remove.bg/v1.0/removebg",
XXXXXXXXXXXXXXXXXXXXfiles={"image_file":Xopen(download_location,X"rb")},
XXXXXXXXXXXXXXXXXXXXdata={"size":X"auto"},
XXXXXXXXXXXXXXXXXXXXheaders={"X-Api-Key":XRemoveBG_API},
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXifXresponse.status_codeX==X200:
XXXXXXXXXXXXXXXXXXXXwithXopen(f"{edit_img_loc}",X"wb")XasXout:
XXXXXXXXXXXXXXXXXXXXXXXXout.write(response.content)
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXXXXXX"CheckXifXyourXapiXisXcorrect",Xquote=True
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXreturn

XXXXXXXXXXXXXXXXawaitXmessage.reply_chat_action("upload_photo")
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_sticker(edit_img_loc,Xquote=True)
XXXXXXXXXXXXXXXXawaitXmsg.delete()
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXawaitXmessage.reply_text("WhyXdidXyouXdeleteXthat??")
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXshutil.rmtree(f"./DOWNLOADS/{userid}")
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXpass
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"GetXtheXapiXfromXhttps://www.remove.bg/b/background-removal-apiXandXaddXinXConfigXVar",
XXXXXXXXXXXXXXXXquote=True,
XXXXXXXXXXXXXXXXdisable_web_page_preview=True,
XXXXXXXXXXXX)
XXXXexceptXExceptionXasXe:
XXXXXXXXprint("removebg_sticker-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn
