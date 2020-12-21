banned_users = ['andrew', 'carolina', 'david']
user = 'david'

if user in banned_users:
	print('Sorry, you have been banned. Access Denied')
else:
	print(f"Welcome,{user.title()}")