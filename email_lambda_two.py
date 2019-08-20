user1_email = input('What is your username?')
user2_email = input('What is your friends username?')


def email_address(
    username, domain): return f'Email Address: {username}{domain}'

# def email_address(
#     username, domain): return f'Email Address: {username}{domain}'


user1 = email_address(user1_email, '@gmail.com')
user2 = email_address(user2_email, '@gmail.com')

print(user1)
print(user2)
