import random
import string 

a = int(input("Enter Password Length :"))
chars = string.ascii_letters + string.digits + string.punctuation
password =''.join(random.choice(chars) for _ in range(a))

print("Generated Password :", password)


