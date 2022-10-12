from time import sleep
import requests
import json
import sys
from collections import OrderedDict

url = "https://breachdirectory.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": "<BREACH DATABASE RAPID API KEY>",
	"X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
}
print("")
print("BreachDatabase.Org Checker")
print("==========================")
print("")
if len(sys.argv) > 1:
    search_query = sys.argv[1]
    search = {"func":"auto","term":search_query}
    response_search = requests.request("GET", url, headers=headers, params=search)
    parse_json = json.loads(response_search.text, object_pairs_hook=OrderedDict)
    print(parse_json)
    results = parse_json['result']

    for item in results:
        dehash = { "func":"dehash","term":item['hash'] }
        response_dehash = requests.request("GET", url, headers=headers, params=dehash)
        parse_json = json.loads(response_dehash.text, object_pairs_hook=OrderedDict)
        dehashed = parse_json['found']
        print("Password:" ,item['password']," || Decrypted: ", dehashed," || Sources:",item['sources'])
        sleep(1)
else:
    print("Usage: python breach-checker.py <username or email>")
    print("")

