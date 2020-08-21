import requests
import re

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J%stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org' % username

session = requests.Session()
response = session.get(url, auth = (username,password))

content = response.text

print(content)