# -*- coding: utf-8 -*-

import json
import matplotlib.pyplot as plt
from datetime import datetime
import itertools

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

reactions_enabled = 1490959854091
first_timestamp = 1476517987830
last_timestamp = 1611004843325
reacts = ['😆', '❤', '👍', '😮', '😢', '😠']
participants = ['Mokriš Andrej', 'Denis Garčala', 'Denis Gero', 'Braňo Faktor', 'Patrik Šimurka']
colors = ['black', 'red', 'blue', 'green', 'pink']


def fix_text(string):
	return string.encode('latin1').decode('utf8')

def fix_dict(dictionary):
	return { k.replace(k, fix_text(k)): v for k, v in dictionary.items() }

def convert_timestamp(timestamp):
	dt_object = datetime.fromtimestamp(timestamp/1000)
	return str(dt_object).split()[0]

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
					reacts.append(j['reaction'])
					if fix_text(j['reaction']) == react:
						result[i['sender_name']] = result.get(i['sender_name'], 0) + 1

			except KeyError:
				pass
	result = fix_dict(result)
	for key, val in result.items():
		result[key] = round(val/pocet_sprav_s_reactami()[key], 5)

	return result

def get_reacts_given(react):
	result = {}

	for l in data:
		for i in l['messages']:
			try:
				for j in i['reactions']:
					if fix_text(j['reaction']) == react:
						result[j['actor']] = result.get(j['actor'], 0) + 1

			except KeyError:
				pass
	return fix_dict(result)

def get_message_counts(who, list_of_dicts):
		result = []
		for i in list_of_dicts:
			try:
				result.append(i[who])
			except KeyError:
				result.append(0)
		return result

def graph_message_count(resolution=10):
	step = (last_timestamp - first_timestamp) // (resolution - 1)
	timestamps = [convert_timestamp(first_timestamp + (i * step)) for i in range(resolution)]
	message_counts = [pocet_sprav(first_timestamp, first_timestamp + (i * step)) for i in range(resolution)]
	for ind, participant in enumerate(participants):
		plt.plot(timestamps, get_message_counts(participant, message_counts), color=colors[ind], label=participant)
	plt.xticks(timestamps[::resolution//100],  rotation='vertical')
	plt.legend(loc="upper left")
	plt.title('Správy v jebačoch')

	plt.show()

def get_word_counts(who, list_of_dicts):
		result = []
		for i in list_of_dicts:
			try:
				result.append(i[who])
			except KeyError:
				result.append(0)
		return result

	
def pocet_sprav(ab=first_timestamp, until=last_timestamp):
	result = {}
	for i in data:
		for j in i['messages']:
			if ab <= int(j['timestamp_ms']) <= until:
				result[j['sender_name']] = result.get(j['sender_name'], 0) + 1

	result = fix_dict(result)
	return result

def graph_word_count(resolution=10):
	step = (last_timestamp - first_timestamp) // (resolution - 1)
	timestamps = [convert_timestamp(first_timestamp + (i * step)) for i in range(resolution)]
	word_counts = [pocet_slov(first_timestamp, first_timestamp + (i * step)) for i in range(resolution)]
	for ind, participant in enumerate(participants):
		plt.plot(timestamps, get_word_counts(participant, word_counts), color=colors[ind], label=participant)
	plt.xticks(timestamps[::resolution//100],  rotation='vertical')
	plt.legend(loc="upper left")
	plt.title('Slová v jebačoch')

	plt.show()

def pocet_slov(ab=first_timestamp, until=last_timestamp):
	result = {}
	for i in data:
		for j in i['messages']:
			if ab <= int(j['timestamp_ms']) <= until:
				try:
					for k in j['content'].split():
						result[j['sender_name']] = result.get(j['sender_name'], 0) + 1
				except KeyError:
					pass
	return fix_dict(result)

def pocet_sprav_s_reactami():
	return pocet_sprav(reactions_enabled,)

def get_word_histogram(ab=first_timestamp, until=last_timestamp, **kwargs):
	result = {}
	for i in data:
		for j in i['messages']:
			if ab <= j['timestamp_ms'] <= until:
				if 'kto' in kwargs:
					if j['sender_name'] == kwargs['kto']:
						try:
							for slovo in j['content'].split():
								try:
									slovo = fix_text(slovo)
								except UnicodeDecodeError:
									pass
								if len(slovo) > 3:
									result[slovo] = result.get(slovo, 0) + 1
						except KeyError:
							pass

				else:
					try:
						for slovo in j['content'].split():
							try:
								slovo = fix_text(slovo)
							except UnicodeDecodeError:
								pass
							if len(slovo) > 3:
								result[slovo] = result.get(slovo, 0) + 1
					except KeyError:
						pass

	return {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}

def get_word_count(word):
	count = 0
	for i in data:
		for j in i['messages']:
			try:
				for slovo in j['content'].split():
					try:
						if word == fix_text(slovo):
							count += 1
					except UnicodeDecodeError:
						pass
			except KeyError:
				pass

	return count

def generate_histogram(dictionary, kolko):
	dictionary = dict(itertools.islice(dictionary.items(), kolko))
	plt.bar(*zip(*dictionary.items()))
	plt.xticks(rotation='vertical')
	plt.title('Braňo Faktor dlhsie ako 3')
	plt.show()

#generate_histogram(get_word_histogram(ab=first_timestamp, until=last_timestamp, kto='Bra\u00c5\u0088o Faktor'),100)
#generate_plot(fix_dict(pocet_sprav))

#print(pocet_sprav())

#graph_message_count(5000)

#graph_word_count(5000)
#print()
#print(get_reacts_given('❤'))

