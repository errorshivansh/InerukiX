importXre
fromXtypingXimportXList

fromXpyrogram.typesXimportXInlineKeyboardButton

BTN_URL_REGEXX=Xre.compile(
XXXXr"(\[([^\[]+?)\]\((buttonurl|buttonalert):(?:/{0,2})(.+?)(:same)?\))"
)

SMART_OPENX=X"“"
SMART_CLOSEX=X"”"
START_CHARX=X("'",X'"',XSMART_OPEN)


defXsplit_quotes(text:Xstr)X->XList:
XXXXifXany(text.startswith(char)XforXcharXinXSTART_CHAR):
XXXXXXXXcounterX=X1XX#XignoreXfirstXcharX->XisXsomeXkindXofXquote
XXXXXXXXwhileXcounterX<Xlen(text):
XXXXXXXXXXXXifXtext[counter]X==X"\\":
XXXXXXXXXXXXXXXXcounterX+=X1
XXXXXXXXXXXXelifXtext[counter]X==Xtext[0]XorX(
XXXXXXXXXXXXXXXXtext[0]X==XSMART_OPENXandXtext[counter]X==XSMART_CLOSE
XXXXXXXXXXXX):
XXXXXXXXXXXXXXXXbreak
XXXXXXXXXXXXcounterX+=X1
XXXXXXXXelse:
XXXXXXXXXXXXreturnXtext.split(None,X1)

XXXXXXXX#X1XtoXavoidXstartingXquote,XandXcounterXisXexclusiveXsoXavoidsXending
XXXXXXXXkeyX=Xremove_escapes(text[1:counter].strip())
XXXXXXXX#XindexXwillXbeXinXrange,XorX`else`XwouldXhaveXbeenXexecutedXandXreturned
XXXXXXXXrestX=Xtext[counterX+X1X:].strip()
XXXXXXXXifXnotXkey:
XXXXXXXXXXXXkeyX=Xtext[0]X+Xtext[0]
XXXXXXXXreturnXlist(filter(None,X[key,Xrest]))
XXXXelse:
XXXXXXXXreturnXtext.split(None,X1)


defXparser(text,Xkeyword):
XXXXifX"buttonalert"XinXtext:
XXXXXXXXtextX=Xtext.replace("\n",X"\\n").replace("\t",X"\\t")
XXXXbuttonsX=X[]
XXXXnote_dataX=X""
XXXXprevX=X0
XXXXiX=X0
XXXXalertsX=X[]
XXXXforXmatchXinXBTN_URL_REGEX.finditer(text):
XXXXXXXX#XCheckXifXbtnurlXisXescaped
XXXXXXXXn_escapesX=X0
XXXXXXXXto_checkX=Xmatch.start(1)X-X1
XXXXXXXXwhileXto_checkX>X0XandXtext[to_check]X==X"\\":
XXXXXXXXXXXXn_escapesX+=X1
XXXXXXXXXXXXto_checkX-=X1

XXXXXXXX#XifXeven,XnotXescapedX->XcreateXbutton
XXXXXXXXifXn_escapesX%X2X==X0:
XXXXXXXXXXXXnote_dataX+=Xtext[prevX:Xmatch.start(1)]
XXXXXXXXXXXXprevX=Xmatch.end(1)
XXXXXXXXXXXXifXmatch.group(3)X==X"buttonalert":
XXXXXXXXXXXXXXXX#XcreateXaXthrupleXwithXbuttonXlabel,Xurl,XandXnewlineXstatus
XXXXXXXXXXXXXXXXifXbool(match.group(5))XandXbuttons:
XXXXXXXXXXXXXXXXXXXXbuttons[-1].append(
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXtext=match.group(2),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXcallback_data=f"alertmessage:{i}:{keyword}",
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXbuttons.append(
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext=match.group(2),
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXcallback_data=f"alertmessage:{i}:{keyword}",
XXXXXXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXiX=XiX+X1
XXXXXXXXXXXXXXXXalerts.append(match.group(4))
XXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXifXbool(match.group(5))XandXbuttons:
XXXXXXXXXXXXXXXXXXXXbuttons[-1].append(
XXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXtext=match.group(2),Xurl=match.group(4).replace("X",X"")
XXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXelse:
XXXXXXXXXXXXXXXXXXXXbuttons.append(
XXXXXXXXXXXXXXXXXXXXXXXX[
XXXXXXXXXXXXXXXXXXXXXXXXXXXXInlineKeyboardButton(
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXtext=match.group(2),Xurl=match.group(4).replace("X",X"")
XXXXXXXXXXXXXXXXXXXXXXXXXXXX)
XXXXXXXXXXXXXXXXXXXXXXXX]
XXXXXXXXXXXXXXXXXXXX)

XXXXXXXX#XifXodd,XescapedX->XmoveXalong
XXXXXXXXelse:
XXXXXXXXXXXXnote_dataX+=Xtext[prev:to_check]
XXXXXXXXXXXXprevX=Xmatch.start(1)X-X1
XXXXelse:
XXXXXXXXnote_dataX+=Xtext[prev:]

XXXXtry:
XXXXXXXXreturnXnote_data,Xbuttons,Xalerts
XXXXexcept:
XXXXXXXXreturnXnote_data,Xbuttons,XNone


defXremove_escapes(text:Xstr)X->Xstr:
XXXXcounterX=X0
XXXXresX=X""
XXXXis_escapedX=XFalse
XXXXwhileXcounterX<Xlen(text):
XXXXXXXXifXis_escaped:
XXXXXXXXXXXXresX+=Xtext[counter]
XXXXXXXXXXXXis_escapedX=XFalse
XXXXXXXXelifXtext[counter]X==X"\\":
XXXXXXXXXXXXis_escapedX=XTrue
XXXXXXXXelse:
XXXXXXXXXXXXresX+=Xtext[counter]
XXXXXXXXcounterX+=X1
XXXXreturnXres


defXhumanbytes(size):
XXXXifXnotXsize:
XXXXXXXXreturnX""
XXXXpowerX=X2X**X10
XXXXnX=X0
XXXXDic_powerNX=X{0:X"X",X1:X"Ki",X2:X"Mi",X3:X"Gi",X4:X"Ti"}
XXXXwhileXsizeX>Xpower:
XXXXXXXXsizeX/=Xpower
XXXXXXXXnX+=X1
XXXXreturnXstr(round(size,X2))X+X"X"X+XDic_powerN[n]X+X"B"
