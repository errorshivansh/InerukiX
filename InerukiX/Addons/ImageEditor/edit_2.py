#XByX@TroJanzHEX
importXos
importXshutil

importXcv2
importXnumpyXasXnp
fromXPILXimportXImage,XImageDraw,XImageEnhance


asyncXdefXcircle_with_bg(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"circle.png"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXimgX=XImage.open(a).convert("RGB")
XXXXXXXXXXXXnpImageX=Xnp.array(img)
XXXXXXXXXXXXh,XwX=Ximg.size
XXXXXXXXXXXXalphaX=XImage.new("L",Ximg.size,X0)
XXXXXXXXXXXXdrawX=XImageDraw.Draw(alpha)
XXXXXXXXXXXXdraw.pieslice([0,X0,Xh,Xw],X0,X360,Xfill=255)
XXXXXXXXXXXXnpAlphaX=Xnp.array(alpha)
XXXXXXXXXXXXnpImageX=Xnp.dstack((npImage,XnpAlpha))
XXXXXXXXXXXXImage.fromarray(npImage).save(edit_img_loc)
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
XXXXXXXXprint("circle_with_bg-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


asyncXdefXcircle_without_bg(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"circle.png"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXimgX=XImage.open(a).convert("RGB")
XXXXXXXXXXXXnpImageX=Xnp.array(img)
XXXXXXXXXXXXh,XwX=Ximg.size
XXXXXXXXXXXXalphaX=XImage.new("L",Ximg.size,X0)
XXXXXXXXXXXXdrawX=XImageDraw.Draw(alpha)
XXXXXXXXXXXXdraw.pieslice([0,X0,Xh,Xw],X0,X360,Xfill=255)
XXXXXXXXXXXXnpAlphaX=Xnp.array(alpha)
XXXXXXXXXXXXnpImageX=Xnp.dstack((npImage,XnpAlpha))
XXXXXXXXXXXXImage.fromarray(npImage).save(edit_img_loc)
XXXXXXXXXXXXawaitXmessage.reply_chat_action("upload_document")
XXXXXXXXXXXXawaitXmessage.reply_to_message.reply_document(edit_img_loc,Xquote=True)
XXXXXXXXXXXXawaitXmsg.delete()
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply_text("WhyXdidXyouXdeleteXthat??")
XXXXXXXXtry:
XXXXXXXXXXXXshutil.rmtree(f"./DOWNLOADS/{userid}")
XXXXXXXXexceptXException:
XXXXXXXXXXXXpass
XXXXexceptXExceptionXasXe:
XXXXXXXXprint("circle_without_bg-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


asyncXdefXsticker(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"sticker.webp"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXos.rename(a,Xedit_img_loc)
XXXXXXXXXXXXawaitXmessage.reply_to_message.reply_sticker(edit_img_loc,Xquote=True)
XXXXXXXXXXXXawaitXmsg.delete()
XXXXXXXXelse:
XXXXXXXXXXXXawaitXmessage.reply_text("WhyXdidXyouXdeleteXthat??")
XXXXXXXXtry:
XXXXXXXXXXXXshutil.rmtree(f"./DOWNLOADS/{userid}")
XXXXXXXXexceptXException:
XXXXXXXXXXXXpass
XXXXexceptXExceptionXasXe:
XXXXXXXXprint("sticker-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


defXadd_corners(im,Xrad):
XXXXcircleX=XImage.new("L",X(radX*X2,XradX*X2),X0)
XXXXdrawX=XImageDraw.Draw(circle)
XXXXdraw.ellipse((0,X0,XradX*X2,XradX*X2),Xfill=255)
XXXXalphaX=XImage.new("L",Xim.size,X255)
XXXXw,XhX=Xim.size
XXXXalpha.paste(circle.crop((0,X0,Xrad,Xrad)),X(0,X0))
XXXXalpha.paste(circle.crop((0,Xrad,Xrad,XradX*X2)),X(0,XhX-Xrad))
XXXXalpha.paste(circle.crop((rad,X0,XradX*X2,Xrad)),X(wX-Xrad,X0))
XXXXalpha.paste(circle.crop((rad,Xrad,XradX*X2,XradX*X2)),X(wX-Xrad,XhX-Xrad))
XXXXim.putalpha(alpha)
XXXXreturnXim


asyncXdefXedge_curved(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"edge_curved.webp"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXimX=XImage.open(a)
XXXXXXXXXXXXimX=Xadd_corners(im,X100)
XXXXXXXXXXXXim.save(edit_img_loc)
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
XXXXXXXXprint("edge_curved-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


asyncXdefXcontrast(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"contrast.jpg"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXimageX=XImage.open(a)
XXXXXXXXXXXXcontrastX=XImageEnhance.Contrast(image)
XXXXXXXXXXXXcontrast.enhance(1.5).save(edit_img_loc)
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
XXXXXXXXprint("contrast-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


defXsepia(img):
XXXXwidth,XheightX=Ximg.size
XXXXnew_imgX=Ximg.copy()
XXXXforXxXinXrange(width):
XXXXXXXXforXyXinXrange(height):
XXXXXXXXXXXXred,Xgreen,XblueX=Ximg.getpixel((x,Xy))
XXXXXXXXXXXXnew_valX=X0.3X*XredX+X0.59X*XgreenX+X0.11X*Xblue
XXXXXXXXXXXXnew_redX=Xint(new_valX*X2)
XXXXXXXXXXXXifXnew_redX>X255:
XXXXXXXXXXXXXXXXnew_redX=X255
XXXXXXXXXXXXnew_greenX=Xint(new_valX*X1.5)
XXXXXXXXXXXXifXnew_greenX>X255:
XXXXXXXXXXXXXXXXnew_greenX=X255
XXXXXXXXXXXXnew_blueX=Xint(new_val)
XXXXXXXXXXXXifXnew_blueX>X255:
XXXXXXXXXXXXXXXXnew_blueX=X255

XXXXXXXXXXXXnew_img.putpixel((x,Xy),X(new_red,Xnew_green,Xnew_blue))

XXXXreturnXnew_img


asyncXdefXsepia_mode(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"sepia.jpg"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXimageX=XImage.open(a)
XXXXXXXXXXXXnew_imgX=Xsepia(image)
XXXXXXXXXXXXnew_img.save(edit_img_loc)
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
XXXXXXXXprint("sepia_mode-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


defXdodgeV2(x,Xy):
XXXXreturnXcv2.divide(x,X255X-Xy,Xscale=256)


asyncXdefXpencil(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"pencil.jpg"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXimgX=Xcv2.imread(a)
XXXXXXXXXXXXimg_grayX=Xcv2.cvtColor(img,Xcv2.COLOR_BGR2GRAY)
XXXXXXXXXXXXimg_invertX=Xcv2.bitwise_not(img_gray)
XXXXXXXXXXXXimg_smoothingX=Xcv2.GaussianBlur(img_invert,X(21,X21),XsigmaX=0,XsigmaY=0)
XXXXXXXXXXXXfinal_imgX=XdodgeV2(img_gray,Ximg_smoothing)
XXXXXXXXXXXXcv2.imwrite(edit_img_loc,Xfinal_img)
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
XXXXXXXXprint("pencil-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn


defXcolor_quantization(img,Xk):
XXXXdataX=Xnp.float32(img).reshape((-1,X3))
XXXXcriteriaX=X(cv2.TERM_CRITERIA_EPSX+Xcv2.TERM_CRITERIA_MAX_ITER,X20,X1.0)
XXXX_,Xlabel,XcenterX=Xcv2.kmeans(
XXXXXXXXdata,Xk,XNone,Xcriteria,X10,Xcv2.KMEANS_RANDOM_CENTERS
XXXX)
XXXXcenterX=Xnp.uint8(center)
XXXXresultX=Xcenter[label.flatten()]
XXXXresultX=Xresult.reshape(img.shape)
XXXXreturnXresult


asyncXdefXcartoon(client,Xmessage):
XXXXtry:
XXXXXXXXuseridX=Xstr(message.chat.id)
XXXXXXXXifXnotXos.path.isdir(f"./DOWNLOADS/{userid}"):
XXXXXXXXXXXXos.makedirs(f"./DOWNLOADS/{userid}")
XXXXXXXXdownload_locationX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+XuseridX+X".jpg"
XXXXXXXXedit_img_locX=X"./DOWNLOADS"X+X"/"X+XuseridX+X"/"X+X"kang.jpg"
XXXXXXXXifXnotXmessage.reply_to_message.empty:
XXXXXXXXXXXXmsgX=XawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXX"DownloadingXimage",Xquote=True
XXXXXXXXXXXX)
XXXXXXXXXXXXaX=XawaitXclient.download_media(
XXXXXXXXXXXXXXXXmessage=message.reply_to_message,Xfile_name=download_location
XXXXXXXXXXXX)
XXXXXXXXXXXXawaitXmsg.edit("ProcessingXImage...")
XXXXXXXXXXXXimgX=Xcv2.imread(a)
XXXXXXXXXXXXedgesX=Xcv2.Canny(img,X100,X200)
XXXXXXXXXXXXgrayX=Xcv2.cvtColor(img,Xcv2.COLOR_BGR2GRAY)
XXXXXXXXXXXXedgesX=Xcv2.adaptiveThreshold(
XXXXXXXXXXXXXXXXgray,X255,Xcv2.ADAPTIVE_THRESH_MEAN_C,Xcv2.THRESH_BINARY,X9,X5
XXXXXXXXXXXX)
XXXXXXXXXXXXcolorX=Xcv2.bilateralFilter(img,Xd=9,XsigmaColor=200,XsigmaSpace=200)

XXXXXXXXXXXXcv2.bitwise_and(color,Xcolor,Xmask=edges)
XXXXXXXXXXXXimg_1X=Xcolor_quantization(img,X7)
XXXXXXXXXXXXcv2.imwrite(edit_img_loc,Ximg_1)
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
XXXXXXXXprint("cartoon-errorX-X"X+Xstr(e))
XXXXXXXXifX"USER_IS_BLOCKED"XinXstr(e):
XXXXXXXXXXXXreturn
XXXXXXXXelse:
XXXXXXXXXXXXtry:
XXXXXXXXXXXXXXXXawaitXmessage.reply_to_message.reply_text(
XXXXXXXXXXXXXXXXXXXX"SomethingXwentXwrong!",Xquote=True
XXXXXXXXXXXXXXXX)
XXXXXXXXXXXXexceptXException:
XXXXXXXXXXXXXXXXreturn
