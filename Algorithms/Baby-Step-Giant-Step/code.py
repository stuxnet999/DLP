#BABY STEP GIANT STEP algorithm

import math
from Crypto.Util.number import *

# a = g^x mod p
# x is the unknown value

def bsgs(g, a, p):
    # To solve g^e mod p = a and find e
    m = int(math.ceil(math.sqrt(p-1)))
    # Baby Step
    table = {pow(g, i, p): i for i in range(m)}
    print(table)
    # Giant Step Precomputation c = g^(-m) mod p
    c = pow(g, m*(p-2), p)
    # Giant Step
    for j in range(m):
        x = (a*pow(c, j, p)) % p
        if x in table:
		res = j*m + table[x]        
		return res
    return None		 
    

g = 7
p = 8
a = 1
answer =  bsgs(g, a, p)
print(answer)  
    
    
