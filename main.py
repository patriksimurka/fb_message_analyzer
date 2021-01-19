# -*- coding: utf-8 -*-

import json

def fix_text(string):
	return string.encode('latin1').decode('utf8')

def fix_dict(dictionary):
	return { k.replace(k, fix_text(k)): v for k, v in dictionary.items() }

data = []

with open("message_3.json", "r") as read_file:
	data1 = json.load(read_file)
	data.append(data1)

with open("message_2.json", "r") as read_file:
	data2 = json.load(read_file)
	data.append(data2)

with open("message_1.json", "r") as read_file:
	data3= json.load(read_file)
	data.append(data3)

pocet_sprav = {}

for i in data:
	for j in i['messages']:
		pocet_sprav[j['sender_name']] = pocet_sprav.get(j['sender_name'], 0) + 1

print(fix_dict(pocet_sprav))


