
import requests


out = requests.get('http://www.google.com/')

#print(out.text)
print("import requests" + "\n" + "out = requests.get('http://www.google.com/')"
        + "\n" + "with open('filename.txt', 'wb') as r:"+ "\n" + "  r.write(out.content)")
with open('filename.txt', 'wb') as r: 
    r.write(out.content)
    

