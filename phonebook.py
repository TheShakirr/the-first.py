phonebook= {
    "Shakir":"12345",
    "ahmed" : "67890",
    "ali": "54321"
    }

print("Shakir number:",phonebook.get("Shakir", "Uknown"))
print("abdi number:", phonebook.get("abdi", "uknown"))


for name in phonebook:
    print (name, ">", phonebook[name])

for name,number in phonebook.items():
    print(name, ":", number)