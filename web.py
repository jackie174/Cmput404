import requests

#http = urllib3.PoolManager()

out = requests.get('http://www.google.com/')

print(out.text)

