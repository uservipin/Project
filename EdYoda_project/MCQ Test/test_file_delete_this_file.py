person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
# print(person.items())

dict_key = frozenset(person.keys())

person[dict_key] =True
print((person))