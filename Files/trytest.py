import requests
import json

#urlunica = f'https://a.4cdn.org/pol/thread/268219903.json'
urlunica = f'https://a.4cdn.org/pol/thread/272072268.json'

print(urlunica)
subr = requests.get(urlunica)    
print(subr)
print(" done in ", subr.elapsed.total_seconds())
try:
    hilos = subr.json()
except:
    print("thread 404 :( ")
with open('testintry.json', 'w') as f:
    #try:
    json.dump(hilos, f, indent=2)
    #except:
    #    print("no existe el thread")