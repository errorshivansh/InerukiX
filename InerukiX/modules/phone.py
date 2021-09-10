importXjson

importXrequests
fromXtelethonXimportXtypes

fromXInerukiX.services.eventsXimportXregister
fromXInerukiX.services.telethonXimportXtbotXasXclient


asyncXdefXis_register_admin(chat,Xuser):
XXXXifXisinstance(chat,X(types.InputPeerChannel,Xtypes.InputChannel)):

XXXXXXXXreturnXisinstance(
XXXXXXXXXXXX(
XXXXXXXXXXXXXXXXawaitXclient(functions.channels.GetParticipantRequest(chat,Xuser))
XXXXXXXXXXXX).participant,
XXXXXXXXXXXX(types.ChannelParticipantAdmin,Xtypes.ChannelParticipantCreator),
XXXXXXXX)
XXXXelifXisinstance(chat,Xtypes.InputPeerChat):

XXXXXXXXuiX=XawaitXclient.get_peer_id(user)
XXXXXXXXpsX=X(
XXXXXXXXXXXXawaitXclient(functions.messages.GetFullChatRequest(chat.chat_id))
XXXXXXXX).full_chat.participants.participants
XXXXXXXXreturnXisinstance(
XXXXXXXXXXXXnext((pXforXpXinXpsXifXp.user_idX==Xui),XNone),
XXXXXXXXXXXX(types.ChatParticipantAdmin,Xtypes.ChatParticipantCreator),
XXXXXXXX)
XXXXelse:
XXXXXXXXreturnXNone


@register(pattern=r"^/phoneX(.*)")
asyncXdefXphone(event):
XXXXifXevent.is_group:
XXXXXXXXifXnotX(awaitXis_register_admin(event.input_chat,Xevent.message.sender_id)):
XXXXXXXXXXXXawaitXevent.reply("☎️XYouXareXnotXadminX🚶‍♀️")
XXXXXXXXXXXXreturn
XXXXinformationX=Xevent.pattern_match.group(1)
XXXXnumberX=Xinformation
XXXXkeyX=X"fe65b94e78fc2e3234c1c6ed1b771abd"
XXXXapiX=X(
XXXXXXXX"http://apilayer.net/api/validate?access_key="
XXXXXXXX+Xkey
XXXXXXXX+X"&number="
XXXXXXXX+Xnumber
XXXXXXXX+X"&country_code=&format=1"
XXXX)
XXXXoutputX=Xrequests.get(api)
XXXXcontentX=Xoutput.text
XXXXobjX=Xjson.loads(content)
XXXXcountry_codeX=Xobj["country_code"]
XXXXcountry_nameX=Xobj["country_name"]
XXXXlocationX=Xobj["location"]
XXXXcarrierX=Xobj["carrier"]
XXXXline_typeX=Xobj["line_type"]
XXXXvalidornotX=Xobj["valid"]
XXXXaaX=X"Valid:X"X+Xstr(validornot)
XXXXaX=X"PhoneXnumber:X"X+Xstr(number)
XXXXbX=X"Country:X"X+Xstr(country_code)
XXXXcX=X"CountryXName:X"X+Xstr(country_name)
XXXXdX=X"Location:X"X+Xstr(location)
XXXXeX=X"Carrier:X"X+Xstr(carrier)
XXXXfX=X"Device:X"X+Xstr(line_type)
XXXXgX=Xf"{aa}\n{a}\n{b}\n{c}\n{d}\n{e}\n{f}"
XXXXawaitXevent.reply(g)
