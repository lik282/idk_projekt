email = input("Please enter your email address: ")
index = email.index("@")
username = email[:index]
domain = email[index+1:]

print(f"your email address is {username} and ur domain is {domain}")