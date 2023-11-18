import requests
import fake_useragent
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

link = "https://browser-info.ru/"
response = requests.get(link, headers=header).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id='tool_padding')

check_js = block.find('div', id='javascript_check')
display_js = check_js.find_all('span')

check_cookie = block.find('div', id='cookie_check')
display_cookie = check_cookie.find_all('span')

check_version = block.find('div', id="flash_version")
display_version = check_version.find_all('span')

check_user = block.find('div', id='user_agent').text

print(f"{display_js[0].text} - {display_js[1].text}")
print(f"{display_cookie[0].text} - {display_cookie[1].text}")
print(f"{display_version[0].text} - {display_version[1].text}")
print(check_user)
