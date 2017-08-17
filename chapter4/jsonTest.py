import json
from urllib.request import urlopen

# def getCounty(ipAddress):
#     response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
#     responseJson = json.loads(response)
#     return responseJson.get("country_code")
#
# print(getCounty("50.78.253.58"))

jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}], ' \
             '"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)

print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number")+
      jsonObj.get("arrayOfNums")[2].get("number"))
print(jsonObj.get("arrayOfFruits")[2].get("fruit"))