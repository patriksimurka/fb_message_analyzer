# -*- coding: utf-8 -*-

import json
import matplotlib.pyplot as plt

reactions_enabled = 999999999999999

reacts = ['😆', '❤', '👍', '😮', '😢']



def fix_text(string):
	return string.encode('latin1').decode('utf8')

def fix_dict(dictionary):
	return { k.replace(k, fix_text(k)): v for k, v in dictionary.items() }

def generate_plot(dictionary):
	plt.bar(range(len(dictionary)), list(dictionary.values()), align='center')
	plt.xticks(range(len(dictionary)), list(dictionary.keys()))
	plt.show()

def get_react_per_message(react):
	result = {}

	for l in data:
		for i in l['messages']:
			try:
				for j in i['reactions']:
					if fix_text(j['reaction']) == react:
						result[i['sender_name']] = result.get(i['sender_name'], 0) + 1

			except KeyError:
				pass

	result = fix_dict(result)
	for key, val in result.items():
		result[key] = round(val/pocet_sprav_s_reactami[key], 3)

	return result



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

		#find out when reactions were enabled
		if 'reactions' in j:
			if int(j['timestamp_ms']) < reactions_enabled:
				reactions_enabled = int(j['timestamp_ms'])

pocet_sprav = fix_dict(pocet_sprav)



pocet_sprav_s_reactami = {}
for i in data:
	for j in i['messages']:
		if int(j['timestamp_ms']) > reactions_enabled:
			pocet_sprav_s_reactami[j['sender_name']] = pocet_sprav_s_reactami.get(j['sender_name'], 0) + 1

pocet_sprav_s_reactami = fix_dict(pocet_sprav_s_reactami)


#generate_plot(fix_dict(pocet_sprav))

print(get_react_per_message('😆'))
print(fix_text('ð\x9f\x8d\x90'))