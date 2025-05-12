import string
import random
if __name__ == "__main__":
    s1=string.ascii_uppercase
    #print(s1)
    s2=string.ascii_lowercase
    # print(s2)
    s3=string.digits
    # print(s3)
    s4=string.punctuation
    # print(s4)
    pass_len=int(input("Enter the length of password:-" ))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    # print(s)
    print("Your Password is--")
    print("".join(random.sample(s,pass_len)))