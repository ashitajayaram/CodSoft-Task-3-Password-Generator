import string
import random

n=int(input("Enter the length of required password(minimum 3 chars): "))
allcombo=string.ascii_letters+string.digits+"#@$"
password=[random.choice(string.ascii_letters),random.choice(string.digits),random.choice("#$@")]
password+=[random.choice(allcombo) for i in range(n-3)]
random.shuffle(password)
finalpassword="".join(password)
print(f"Required password of length {n} is: {finalpassword}")
