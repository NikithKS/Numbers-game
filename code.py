import random
import string
import time
print("Pick a number between 10 and 100\n  ")
time.sleep(3)
print("Then add the digits of number\n")
time.sleep(1)
n=input("That is Eg. for 45:\n    4+5=9\nOnce done hit enter\n")
print("Now substarct the sum of digits from the initial number\n")
time.sleep(1)
print("That is for 45:\n     45-9=36\n")
n=input("Once done hit enter\n")
print("Now see which alphbet do you get infront of the number you got\n")
time.sleep(3)
char=string.ascii_uppercase
for x in range (1):
   n=random.choice(char)
i=1
flag=0
print(n)
lst=([9,18,27,36,45,54,63,72,81,90,99])
for i in range(1,100):
    if i in lst :
       flag=1
    if(flag==0):
         for x in range (1):
              m=random.choice(char)
         print("{0}----{1}".format(i,m))
    else:
         print("{0}----{1}".format(i,n))
    flag=0
j=input("Hit enter when you find the number")
time.sleep(1)
print("Did you get {0}".format(n))
