import json
import os
print (os.getcwd())

foo = open('Chelsio-6-4-TCP.json', 'r')

print (foo)

data = json.load(foo)

print (data[2]['title'])