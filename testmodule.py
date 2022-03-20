#!/usr/bin/python3
print('Loading testmodule...')

#### functions ##############################
def print_data(item,name='default_name'):
    """Übergabe mehrerer Daten"""
    print(f"{name} hat {len(name)} Buchstaben")
    print(f"{item} hat {len(item)} Buchstaben")
    return 0

def greeting(data):
    """Übergabe EINER komplexen Datenstruktur"""
    print(data) # overview of the data structure
    print(f"{data['name']} is greeted in the morning with: {data['morning_greeting']}")
    print(f"{data['name']} is greeted in the evening with: {data['evening_greeting']}")

print('... testmodule loaded')
