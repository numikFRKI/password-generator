import random 
lower = "abcdefghijklmnopqrstuvwxyz"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
unis = "!?*$"

print("What website is this password for?")
websitename = input("You: ")

all=lower + caps + num + unis
length = 32
password = "".join(random.sample(all, length))
print("This is my",websitename,"password",password)