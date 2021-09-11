importjson

importrequests
fromtelethonimporttypes

fromIneruki.services.eventsimportregister
fromIneruki.services.telethonimporttbotasclient


asyncdefis_register_admin(chat,user):
ifisinstance(chat,(types.InputPeerChannel,types.InputChannel)):

returnisinstance(
(
awaitclient(functions.channels.GetParticipantRequest(chat,user))
).participant,
(types.ChannelParticipantAdmin,types.ChannelParticipantCreator),
)
elifisinstance(chat,types.InputPeerChat):

ui=awaitclient.get_peer_id(user)
ps=(
awaitclient(functions.messages.GetFullChatRequest(chat.chat_id))
).full_chat.participants.participants
returnisinstance(
next((pforpinpsifp.user_id==ui),None),
(types.ChatParticipantAdmin,types.ChatParticipantCreator),
)
else:
returnNone


@register(pattern=r"^/phone(.*)")
asyncdefphone(event):
ifevent.is_group:
ifnot(awaitis_register_admin(event.input_chat,event.message.sender_id)):
awaitevent.reply("☎️Youarenotadmin🚶‍♀️")
return
information=event.pattern_match.group(1)
number=information
key="fe65b94e78fc2e3234c1c6ed1b771abd"
api=(
"http://apilayer.net/api/validate?access_key="
+key
+"&number="
+number
+"&country_code=&format=1"
)
output=requests.get(api)
content=output.text
obj=json.loads(content)
country_code=obj["country_code"]
country_name=obj["country_name"]
location=obj["location"]
carrier=obj["carrier"]
line_type=obj["line_type"]
validornot=obj["valid"]
aa="Valid:"+str(validornot)
a="Phonenumber:"+str(number)
b="Country:"+str(country_code)
c="CountryName:"+str(country_name)
d="Location:"+str(location)
e="Carrier:"+str(carrier)
f="Device:"+str(line_type)
g=f"{aa}\n{a}\n{b}\n{c}\n{d}\n{e}\n{f}"
awaitevent.reply(g)
