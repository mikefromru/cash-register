import requests
import webbrowser
import os
from dotenv import load_dotenv
from art import *
from simple_term_menu import TerminalMenu


load_dotenv('project/.env')

def get_qrfile():
    url = os.getenv('SITE_URL') + 'cash_machine/'
    payload = {'items': [1, 2, 3]}

    r = requests.post(url, json=payload)
    if r.status_code == 200:
        redirect_url = r.json()
        webbrowser.open_new_tab(redirect_url.get('redirect_url'))

def main():
    name = 'Cash-register'
    print(text2art(name))
    options = [
        'Get QR-Code to get PDF bill', 
        'Exit'
    ]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 0:
        get_qrfile()
    else:
        raise SystemExit()


if __name__ ==  '__main__':
    main()