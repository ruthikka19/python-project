import random
import string

length=8

characters=string.ascii_letters+string.digits+string.punctuation

password=""

for i in range(length):
    password+=random.choice(characters)

print("Random Password:",password)