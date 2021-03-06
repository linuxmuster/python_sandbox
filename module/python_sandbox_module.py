#!/usr/bin/python3
print('Loading testmodule...')

import pprint

#### functions ##############################
def print_data(item,name='default_name'):
    """Übergabe mehrerer Daten"""
    print(f"{name} hat {len(name)} Buchstaben")
    print(f"{item} hat {len(item)} Buchstaben")
    return 0

def greeting(users,username):
    """Übergabe EINER komplexen Datenstruktur"""
    #print(users) # overview of the data structure
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(users)
    print(f"{users['sAMAccountName'][username]['firstname']} is greeted in the morning with: {users['sAMAccountName'][username]['morning_greeting']}")
    print(f"{users['sAMAccountName'][username]['firstname']} is greeted in the evening with: {users['sAMAccountName'][username]['evening_greeting']}")
    print()


print('... testmodule loaded')
