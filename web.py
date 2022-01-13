
"""Cite:
Url: https://towardsdatascience.com/how-to-download-files-using-python-ffbca63beb5c
Author: Aaron S
Date: Feb 5, 2020
"""
import requests


out = requests.get('http://www.google.com/')

#print(out.text)
print("import requests" + "\n" + "out = requests.get('http://www.google.com/')"
        + "\n" + "with open('filename.txt', 'wb') as r:"+ "\n" + "  r.write(out.content)")
with open('filename.txt', 'wb') as r:
    r.write(out.content)

    
    
    
    
