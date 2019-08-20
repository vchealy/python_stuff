user1_email = input('What is your username?')
user2_email = input('What is your friends username?')

fixed_domain = '@gmail.com'
email_address = lambda username, fixed_domain: f'Email Address: {username}{fixed_domain}'

user1 = email_address(user1_email, fixed_domain)
user2 = email_address(user2_email, fixed_domain)


print(user1)
print(user2)
