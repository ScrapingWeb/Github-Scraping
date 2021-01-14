from core.terminaltables import terminaltables
from core.tree import tree
from colorama import Fore, init

github_username = input(f"[{Fore.YELLOW}?{Fore.RESET} Username: ")
print(f"[{Fore.RED}!{Fore.RESET}] Scraping en cours sur '{github_username}'...")
terminaltables(github_username)
tree(github_username)
