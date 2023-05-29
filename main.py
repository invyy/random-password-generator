import random
letters = "abcde"
numbers = "12345"
abc = letters + numbers
length = int(input("How long is password?"))
password = ""
for i in range(0,length):
    password += random.choice(abc)
print("Your password is - ", password)



