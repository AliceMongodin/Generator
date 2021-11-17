# -*- coding: utf8 -*-
import random
import json


#read value from JSON file
def read_value_from_json(file, key):
	values = []
	with open(file, encoding= "utf8") as f:
		data = json.load(f)
		for entry in data:
				values.append(entry[key])
		return values 

def clean_strings(sentences):
	cleaned = []
	for sentence in sentences:
		clean_sentence = sentence.strip()
		cleaned.append(clean_sentence)
	return cleaned

def get_random_item(my_list):
	rand_numb = random.randint(0, len(my_list) - 1)
	item = my_list[rand_numb]
	return item

def get_random_quote():
    all_values = read_value_from_json('quotes.json', 'quote')
    clean_values = clean_strings(all_values)
    return get_random_item(clean_values)

def get_random_character():
	all_values = read_value_from_json('characters.json', 'character')
	clean_values = clean_strings(all_values)
	return get_random_item(clean_values)

def message (character, quote):
	n_character = character.capitalize()
	n_quote = quote.capitalize()
	return "{} a dit : {}".format(n_character, n_quote)

user_answer = input("Tapez 'Entrée' pour générer une autre citation ou 'B' pour terminer le programme.")


while user_answer != "B" :
		print(message(get_random_character(), get_random_quote()))
		user_answer = input("Tapez 'Entrée' pour générer une autre citation ou 'B' pour terminer le programme.")

