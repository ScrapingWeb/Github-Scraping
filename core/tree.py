from treelib  import Node, Tree
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

def tree(github_username):
	url = urlopen(Request("https://api.github.com/users/" + github_username)).read().decode().strip()
	r = requests.get('https://api.github.com/users/' + github_username)
	
	getgithub = get(f'https://api.github.com/users/{github_username}?fields=name,avatar_url,html_url,location,blog,email,bio,twitter_username,followers,following,updated_at')
	getgithubResult = getgithub.json()

	tree = Tree()
	tree.create_node(f"\n{github_username}", 1)

	tree.create_node(f"{Fore.YELLOW}Information{Fore.RESET}", 2,parent=1)
	tree.create_node("Name     : {}".format(getgithubResult["name"]),22,parent=2)
	tree.create_node("Location : {}".format(getgithubResult["location"]),33,parent=2)
	tree.create_node("Email      : {}".format(getgithubResult["email"]),44,parent=2)
	tree.create_node("Twitter  : {}".format(getgithubResult["twitter_username"]),55,parent=2)
	tree.create_node("Biographie : {}".format(getgithubResult["bio"]),66,parent=2)
	tree.create_node("Blog       : {}".format(getgithubResult["blog"]),77,parent=2)
	tree.create_node("Followers  : {}".format(getgithubResult["followers"]),88,parent=2)
	tree.create_node("Following  : {}".format(getgithubResult["following"]),99,parent=2)

	tree.create_node(f"{Fore.BLUE}Information Date{Fore.RESET}", 3,parent=2)
	tree.create_node("Create at  : {}".format(getgithubResult["created_at"]),100,parent=3)
	tree.create_node("Update at  : {}".format(getgithubResult["updated_at"]),110,parent=3)

	tree.create_node(f"{Fore.MAGENTA}Other Information{Fore.RESET}", 4,parent=2)
	tree.create_node("Link       : {}".format(getgithubResult["html_url"]),120,parent=3)
	tree.create_node("Avatar URL : {}".format(getgithubResult["avatar_url"]),130,parent=3)

	tree.show()