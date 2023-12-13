name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

name = "David"
print(name.lower())
print(name.upper())
print(name.title())

famous_person = "albert einstein"
message = "A person who never made a mistake never tried anything new."
print(f"{famous_person.title()} once said, '{message}'")

test = "  One\tTwo\nThree  "
formatted = test.strip()
print(formatted)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

name = 'ada lovelace'
print(name.title())
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.count('a'))

template = '{0:.2f} {1:s} are worth US${2:d}'
formatted = template.format(4.5560, 'Argentine Pesos', 1)
print(formatted)