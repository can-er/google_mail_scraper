"""
Author: KORKUT Caner
Date: 11-04-20
This program allows to get a range of email address through the db of Google Dorks
Ce programme permet d'utiliser la db Google Dorks afin d'obtenir une série d'adresses emails ciblées
"""

import googlesearch
import requests 
import re


def get_target_area():
	return input("Definissez votre domaine de recherche: ")

def get_number_of_results():
	return int(input("Definissez le nombre de resultats souhaites: "))

def facebook_activated():
	typed_val = input("Faire la recherche sur Facebook [O/N] ? ")
	if typed_val.upper() == "O":
		return True
	else:
		if typed_val.upper() == "N":
			return False
		else:
			print("erreur")
			pass

def query_generator():
	speciality = get_target_area()
	famous_domains = '"@gmail.com" OR "@hotmail.com" OR "@outlook.com" OR "@yahoo.fr"'
	if facebook_activated():
		return "{} {} {}".format("site:facebook",speciality,famous_domains)
	else:
		return "{} {} {}".format("",speciality,famous_domains)

def get_google_results(query, numberOfResults = 25):
	my_results_list = []
	for i in googlesearch.search(query,        # The query you want to run
	                tld = 'com',  # The top level domain
	                lang = 'en',  # The language
	                num = 10,     # Number of results per page
	                start = 0,    # First result to retrieve
	                stop = numberOfResults,  # Last result to retrieve
	                pause = 2.0,  # Lapse between HTTP requests
	               ):	
	    my_results_list.append(i)
	return my_results_list


def get_email_from_urls(urls):
	html_content = ""
	all_emails = []
	emails = []
	for elem in urls:
	    html_content = requests.get(elem)
	    html_content = html_content.text
	    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", html_content)
	    all_emails.append(emails)
	return all_emails

def init_message():
	print("""\
                         _                             _ _
  __ _  ___   ___   __ _| | ___    ___ _ __ ___   __ _(_) |
 / _` |/ _ \ / _ \ / _` | |/ _ \  / _ \ '_ ` _ \ / _` | | |
| (_| | (_) | (_) | (_| | |  __/ |  __/ | | | | | (_| | | |
 \__, |\___/ \___/ \__, |_|\___|  \___|_| |_| |_|\__,_|_|_|
 |___/             |___/
           _                  _
  _____  _| |_ _ __ __ _  ___| |_ ___  _ __
 / _ \ \/ / __| '__/ _` |/ __| __/ _ \| '__|
|  __/>  <| |_| | | (_| | (__| || (_) | |
 \___/_/\_\\\__|_|  \__,_|\___|\__\___/|_|
		""")

if __name__ == '__main__':
	init_message()
	print(get_email_from_urls(get_google_results(query_generator(), get_number_of_results())))