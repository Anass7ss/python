#email python
email= input("entrer votre email")
index=email.index("@")
username=email[:email.index("@")]
domain=email[:index+1]
print(f"your username is{username}and do")
