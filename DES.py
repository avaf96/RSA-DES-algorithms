from time import time

#------------------------------------------DES-----------------------------------------#


#Permutation matrix
initial_prm = [58, 50, 42, 34, 26, 18, 10, 2,60, 52, 44, 36, 28, 20, 12, 4,62, 54, 46, 38, 30, 22, 14, 6,64, 56, 48, 40, 32, 24, 16,8,57,
                49, 41, 33, 25, 17, 9, 1,59, 51, 43, 35, 27, 19, 11, 3,61,53, 45, 37, 29, 21, 13, 5,63, 55, 47, 39, 31, 23, 15, 7] 

key_initial_prm =  [57, 49, 41, 33, 25, 17, 9,1, 58, 50, 42, 34, 26, 18,10, 2, 59, 51, 43, 35, 27,19, 11, 3, 60, 52, 44, 36,63, 55, 47, 39,
                    31, 23, 15,7, 62, 54, 46, 38, 30, 22,14, 6, 61, 53, 45, 37, 29,21, 13, 5, 28, 20, 12, 4]

key_shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

compress_prm = [14, 17, 11, 24, 1, 5, 3, 28,15, 6, 21, 10, 23, 19, 12, 4,26, 8, 16, 7, 27, 20, 13, 2,41, 52, 31, 37, 47, 55, 30, 40,51,
                45, 33, 48, 44, 49, 39, 56,34, 53, 46, 42, 50, 36, 29, 32]

expand_prm =  [32, 1, 2, 3, 4, 5,4, 5, 6, 7, 8, 9,8, 9, 10, 11, 12, 13,12, 13, 14, 15, 16, 17,16, 17, 18, 19, 20, 21,20, 21, 22, 23, 24, 25,
                24, 25, 26, 27, 28, 29,28, 29, 30, 31, 32, 1]

S_box_prm = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],],

               [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],],

                [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
                ],

                [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
                ],  

                [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
                ], 

                [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
                ], 

                [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
                ],
                
                [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
                ]
            ]

PBox_prm = [16, 7, 20, 21, 29, 12, 28, 17,1, 15, 23, 26, 5, 18, 31, 10,2, 8, 24, 14, 32, 27, 3, 9,19, 13, 30, 6, 22, 11, 4, 25]

final_prm = [40, 8, 48, 16, 56, 24, 64, 32,39, 7, 47, 15, 55, 23, 63, 31,38, 6, 46, 14, 54, 22, 62, 30,37, 5, 45, 13, 53, 21, 61, 29,36, 4,
             44, 12, 52, 20, 60, 28,35, 3, 43, 11, 51, 19, 59, 27,34, 2, 42, 10, 50, 18, 58, 26,33, 1, 41, 9, 49, 17, 57, 25] 



def encrypt(plain_text,input_key):
    keys = generateKeys(input_key)
    plain = addPadding(plain_text)
    plain_blocks = splitList(plain, 8)
    result = list()
    for block in plain_blocks: 
        block = strToBinary(block) 
        block = permutation(block,initial_prm) 
        l, r = splitList(block, 32) 
        right_side = None
        for i in range(16): 
            expanded_r = permutation(r, expand_prm) 
            right_side = xor(keys[i], expanded_r) 
            right_side = sBoxSubstitution(right_side) 
            right_side = permutation(right_side, PBox_prm)
            right_side = xor(l, right_side)
            l = r
            r = right_side
        result += permutation(r+l, final_prm)
    final_res = binaryToStr(result)
    return final_res 

def decrypt(cipher_text,input_key):
    keys = generateKeys(input_key)
    cipher_blocks = splitList(cipher_text, 8)
    result = list()
    for block in cipher_blocks: 
        block = strToBinary(block) 
        block = permutation(block,initial_prm) 
        l, r = splitList(block, 32) 
        right_side = None
        for i in range(16): 
            expanded_r = permutation(r, expand_prm) 
            right_side = xor(keys[15-i], expanded_r)
            right_side = sBoxSubstitution(right_side) 
            right_side = permutation(right_side, PBox_prm)
            right_side = xor(l, right_side)
            l = r
            r = right_side
        result += permutation(r+l, final_prm)
    final_res = binaryToStr(result)
    return removePadding(final_res) 


def addPadding(txt): 
    pad_len = 8 - (len(txt) % 8)
    txt += pad_len * chr(pad_len)
    return txt

def removePadding(data): 
    pad_len = ord(data[-1])
    return data[:-pad_len]

def generateKeys(input_key): 
        keys = []
        key = strToBinary(input_key)
        key = permutation(key, key_initial_prm) 
        l, r = splitList(key, 28) 
        for i in range(16):
            l, r = shift(l, r, key_shifts[i]) 
            merged_key = l + r 
            keys.append(permutation(merged_key, compress_prm))
        return keys

def sBoxSubstitution(right_exp): 
    subblocks = splitList(right_exp, 6) 
    result = list()
    for i in range(len(subblocks)): 
        block = subblocks[i]
        row = int(str(block[0])+str(block[5]) ,2)
        column = int(''.join([str(x) for x in block[1:][:-1]]),2) 
        val = S_box_prm[i][row][column] 
        bin = binValOfChar(val, 4)
        result += [int(x) for x in bin]
    return result

def strToBinary(text): 
    array = list()
    for char in text:
        binval = binValOfChar(char, 8) 
        array.extend([int(x) for x in list(binval)])
    return array

def binValOfChar(val, bitsize):
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "Needs more bits"
    while len(binval) < bitsize:
        binval = "0"+binval 
    return binval 
    
def binaryToStr(array): 
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in  splitList(array,8)]])        
    return res

def splitList(s, n):
    return [s[k:k+n] for k in range(0, len(s), n)]
  
def permutation(block, array):
    return [block[x-1] for x in array]

def shift(l, r, n): 
        return l[n:] + l[:n] , r[n:] + r[:n]

def xor(t1, t2): 
    return [x^y for x,y in zip(t1,t2)]




key = input ("\n Enter key (It must be 8 char): ")
while len(key) < 8:
    key = input ("\n Enter key (It must be 8 char): ")
if len(key) > 8:
    key = key[:8] 

input_msg = input ("\n Enter your msg: ")

enc_start_time = time()
enc = encrypt(input_msg,key)
enc_end_time = time()
print ("\n Encrypted msg: " , enc)
print("\n Encription time: ", enc_end_time - enc_start_time)

dec_start_time = time()
dec = decrypt(enc,key)
dec_end_time = time()
print ("\n Decrypted msg: " , dec)
print("\n Decryption time: ", dec_end_time - dec_start_time)



# 8 char key: nZr4u7x!
# 8 char key: 9z$C&F)J
# 8 char key: Yp2s5v8y
# 8 char key: WmZq4t7w