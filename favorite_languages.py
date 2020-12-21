favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby', 
	'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print(favorite_languages['sarah'])

#for the below, name is the "key" and language is the "value".  These names can be anything as long as order is correct and fun has .items() after it

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite langauge is {language.title()}!")

for name in favorite_languages.keys():
	print(name.title())


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(f"Hi {name.title()}.")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}.")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

if 'css' not in favorite_languages.values():
	print("Should we add CSS to the poll?")
else:
	print("that language is already here!")