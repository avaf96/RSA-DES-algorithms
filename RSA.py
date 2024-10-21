from decimal import Decimal
import random
from sympy import *
from time import time
  
#-------------------------------------- RSA --------------------------------------#

def gcd(m,n): 
    if n==0:  
        return m 
    else: 
        return gcd(n,m%n) 

def eqGcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = eqGcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modularInverse(a, m):
    g, x, y = eqGcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

def splitInt(number_string, interval=2):
    newList = []
    for ditget in range(0, len(number_string), interval):
        newList.append(int(number_string[ditget:ditget + interval]))
    return newList



key_start_time = time()

#------------------------------------------------------Generate p & q randomly
# primes=[]
# for i in range(int(sqrt(2)*pow(2,27)),pow(2,28)):
#     if (isprime(i)):
#         primes.append(i)

# p = random.choice(primes)
# q = random.choice(primes)
# while(q==p):
#     q = random.choice(primes)

#-------------------------------------------------------User must enter p & q
# p= input("Enter p: ")
# q= input("Enter q: ")


p=189812533
q=189812551
print("\n p:" , p , " q:" , q)

n = p*q 
print("\n n:" , n )

phi_n = (p-1)*(q-1) 
print("\n phi_n:" , phi_n)

for e in range(pow(2,32),phi_n): 
    if gcd(e,phi_n)== 1: 
        break
print("\n e:" , e)

d = modularInverse(e, phi_n)
print("\n d:" , d)

public_key = (e,n)
private_key = (d,n)
print("\n public key:" , public_key)
print("\n private key:" , private_key)

key_end_time = time()
key_time = key_end_time - key_start_time

def encrypt(public_key,plain_text):
    e,n = public_key
    ciphered=[]
    msg=0
    count=0 
    block_array = []
    plaintxt_Length = len(plain_text)
    for i in plain_text:
        if(ord(i)>=100):
            if((ord(i)-99) <= 9):
                block_array.append("0" + str(ord(i)-99))
                count+=1
                plaintxt_Length-=1
            else:
                block_array.append(str(ord(i)-99))
                count+=1
                plaintxt_Length-=1
        else:
            block_array.append(str(ord(i)))
            count+=1
            plaintxt_Length-=1

        if(count==8 or plaintxt_Length==0):
            msg = ''.join(block_array)
            c=pow(int(msg),e,n)
            ciphered.append(c)
            count=0
            block_array.clear()
    return ciphered

def decrypt(private_key,cipher_text):
    d,n = private_key
    decrypted=''
    msg=0
    for i in cipher_text:
        msg=str(pow(int(i),d,n))
        if(len(msg) % 2 != 0):
            msg = "0" + msg
        list1 = splitInt(msg,2)
        for i in list1:
            if(i<=31):
                c=chr(i+99)
                decrypted+=c
            else:
                c=chr(i)
                decrypted+=c
    return decrypted



input_msg = input("\n Enter your msg: ")

enc_start_time = time()
enc = encrypt(public_key,input_msg)
enc_end_time = time()
print ("\n Encrypted msg: " , enc)
print("\n Encription time: ", enc_end_time - enc_start_time + key_time) 

dec_start_time = time()
dec = decrypt(private_key,enc)  
dec_end_time  = time()
print ("\n Decrypted msg: " , dec )
print("\n Decryption time: ", dec_end_time  - dec_start_time  + key_time ,"\n")













