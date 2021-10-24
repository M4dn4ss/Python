import requests
import json

api_url = "https://api.exchangerate.host/latest?base="

deteriorated_currency = input("deteriorated currency kind: ")
received_currency = input("received currency kind: ")
amount = int(input(f"How much {deteriorated_currency} would like to deteriorate: "))

result = requests.get(api_url + deteriorated_currency)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(deteriorated_currency, result["rates"][received_currency], received_currency))
print("{0} {1} = {2} {3}".format(amount, deteriorated_currency, amount * result["rates"][received_currency], received_currency))
