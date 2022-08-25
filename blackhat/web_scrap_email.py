import requests
from bs4 import BeautifulSoup
import re

print("Program to get all Email ID from Website!!!!!")

url = input("Enter the url : ")
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

text = soup.get_text()
pattern = r"[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]+"
string = re.findall(pattern, text)
email = set(string)
print(f"E-mail: {email}")


