name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!") 


age = input("How old are you? ")
age = int(age)

# more practice below using the car scenario

car = ("What kind of car are you looking for today? ")
answer = input(car)
print(f"\nOk. Let me check our inventory and see what models of {answer} we have available.")
