import requests

# params = {'username':'JoJo','password':'password'}
# r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
# print("Cookie is set to:")
# print(r.cookies.get_dict())
# print('-------------')
# print("Going to profile page...")
# r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",cookies = r.cookies)
# print(r.text)

session = requests.Session()

params = {'username':'JoJo','password':'password'}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
print("Cookie is set to:")
print(s.cookies.get_dict())
print('-------------')
print("Going to profile page...")
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)