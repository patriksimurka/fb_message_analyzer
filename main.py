# -*- coding: utf-8 -*-

import json
import matplotlib.pyplot as plt

def fix_text(string):
	return string.encode('latin1').decode('utf8')

def fix_dict(dictionary):
	return { k.replace(k, fix_text(k)): v for k, v in dictionary.items() }

def generate_plot(dictionary):
	plt.bar(range(len(dictionary)), list(dictionary.values()), align='center')
	plt.xticks(range(len(dictionary)), list(dictionary.keys()))
	plt.show()

data = []

with open("message_3.json", "r") as read_file:
	data1 = json.load(read_file)
	data.append(data1)

with open("message_2.json", "r") as read_file:
	data2 = json.load(read_file)
	data.append(data2)

with open("message_1.json", "r") as read_file:
	data3 = json.load(read_file)
	data.append(data3)

pocet_sprav = {}

for i in data:
	for j in i['messages']:
		pocet_sprav[j['sender_name']] = pocet_sprav.get(j['sender_name'], 0) + 1

pocet_sprav = fix_dict(pocet_sprav)

haha_reacts_received = {}

for l in data:
	for i in l['messages']:
		try:
			for j in i['reactions']:
				if fix_text(j['reaction']) == '😆':
					haha_reacts_received[i['sender_name']] = haha_reacts_received.get(i['sender_name'], 0) + 1

		except KeyError:
			pass

haha_reacts_received = fix_dict(haha_reacts_received)
for key, val in haha_reacts_received.items():
	haha_reacts_received[key] = round(val/pocet_sprav[key],3)

#generate_plot(fix_dict(pocet_sprav))

print(haha_reacts_received)