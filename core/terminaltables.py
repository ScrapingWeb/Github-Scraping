import sys, importlib
import sys, os, requests
from terminaltables import SingleTable
import requests, re, json
from colorama import init, Fore,  Back,  Style
from requests import *
from colorama import *
import urllib
import os
from urllib.request import Request, urlopen

def terminaltables(github_username):
	url = urlopen(Request('https://api.github.com/users/' + github_username)).read().decode().strip()

	r = requests.get('https://api.github.com/users/' + github_username)


	getgithub = get(f'https://api.github.com/users/{github_username}?fields=name,location,email,bio,twitter_username,followers,following')
	getgithubResult = getgithub.json()

	table_data = [
	['Name','Location', 'Email', 'Bio', 'Twitter Username', 'Followers', 'Followings'],
	[f'{getgithubResult["name"]}', f'{getgithubResult["location"]}', f'{getgithubResult["email"]}', f'{getgithubResult["bio"]}', f'{getgithubResult["twitter_username"]}', f'{getgithubResult["followers"]}', f'{getgithubResult["following"]}']
	]

	table = SingleTable(table_data, f' {github_username} ')
	print("\n" + table.table)
