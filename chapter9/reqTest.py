import requests

# params = {'firstname':'Ryan', 'lastname':'Mitchell'}
# r = requests.post("http://pythonscraping.com/files/processing.php", data=params)

# params = {'email_addr':'ryan.e.mitchell@gamil.com'}
# r = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi", data=params)

files = {'uploadFile':open('../files/logo.png','rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php",file=files)
print(r.text)