import requests
from bs4 import BeautifulSoup
import re
import time

print("Program to get all Email ID from Website!!!!!")
time.sleep(1)


class EmailScrap:
    def get_url(self):
        url = input("Enter url to get E-mail: ")
        try:
            if url == " " or url is None:
                choice = input("[!] Enter valid url...To continue enter 'c' or want to quite enter 'q' : ")
                if choice == 'q':
                    print("Thanks for using this program!!!!!")
                    exit()
                elif choice == 'c':
                    self.get_url()
                else:
                    print("[*] You didn't enter a valid key, Exiting from program...!!!!!")
            else:
                req = requests.get(url)
                soup = BeautifulSoup(req.content, "html.parser")
                for link in soup.find_all('a'):
                    hrf = link.get('href')
                    if hrf == "" or hrf == "#" or hrf is None:
                        continue
                    else:
                        try:
                            req2 = requests.get(hrf)
                            soup2 = BeautifulSoup(req2.content, "html.parser")
                            text = soup2.get_text()
                            pattern = r"[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]+"
                            string = re.findall(pattern, text)
                            print(f"E-mail: {string}")
                        except Exception as e:
                            print(e)
                            continue
        except Exception as E:
            print(E)
            choice = input("[!] Enter valid url...To continue enter 'c' or want to quite enter 'q' : ")
            if choice == 'q':
                print("Thanks for using this program!!!!!")
                exit()
            elif choice == 'c':
                self.get_url()
            else:
                print("[*] You didn't enter a valid key, Exiting from program...!!!!!")


mail = EmailScrap()
mail.get_url()

