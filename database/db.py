import shelve

database = shelve.open('accounts.db')

print(database['trial'])