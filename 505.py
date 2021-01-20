from main import fix_dict
import json 

data = []
with open("505/message_4.json", "r") as read_file:
	data1 = json.load(read_file)
	data.append(data1)
with open("505/message_3.json", "r") as read_file:
	data2 = json.load(read_file)
	data.append(data2)
with open("505/message_2.json", "r") as read_file:
	data3 = json.load(read_file)
	data.append(data3)
with open("505/message_1.json", "r") as read_file:
	data4 = json.load(read_file)
	data.append(data4)


def get_message_count():
	messages = {}
	for i in data:
		for j in i['messages']:
			messages[j['sender_name']] = messages.get(j['sender_name'], 0) + 1
	return {k: v for k, v in sorted(fix_dict(messages).items(), key=lambda item: item[1], reverse=True)}

print(get_message_count())
