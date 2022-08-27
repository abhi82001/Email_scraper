
import requests
from bs4 import BeautifulSoup
import re
import time


print("Program to get all Email ID from Website!!!!!")
time.sleep(1)


def input_url():
    url = input("Enter url to get E-mail : ")
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.content, "html.parser")
        text = soup.get_text()
        print("loading..............")
        time.sleep(2)
        print("-------------------------------------------------")
        if text == '':
            exit()
            print("[!] Enter the valid URl......")
        else:
            pattern = r"[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]+"
            string = re.findall(pattern, text)
            email = set(string)
            if email == set(''):
                print("[!] There is no Email in a website. Try another website....")
                input_url()
            else:
                print(f"E-mail : {email} ")
    except Exception as e:
        print(e)
        choice = input("[!] Enter valid url...To continue enter 'c' or want to quite enter 'q' : ")
        if choice == 'q':
            print("Thanks for using this program!!!!!")
            exit()
        elif choice == 'c':
            input_url()
        else:
            print("[!] You didn't enter a valid key, Exiting from program...!!!!!")


input_url()



