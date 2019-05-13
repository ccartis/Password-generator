import string
import random
def generate_password(length=8,use_upper=False,use_digits=False,use_punctuation=False):
    #create placeholder for generate_password
    password=""

    pool=string.ascii_lowercase
    #add to pool based on what user selected

    if use_upper:
        #do something
        #add to our pool
        pool+=string.ascii_uppercase

    elif use_digits:
       pool+=string.digits
    elif use_punctuation:
        pool+=string.punctuation
    for  i in range(length):
        character=random.choice(pool)
        password+=character




    return password

# ugh=random.randint(1,323)
# print(ugh)
# list_rand=["four","bar","asdf","asfd","wrEew"]
# print(random.choice(list_rand))
password=generate_password(100,True,True,True)
print("My generated password is "+password)
