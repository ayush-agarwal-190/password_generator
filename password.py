import random
from symtable import Symbol
lower="abcdefghijklmnop"
upper="ABCDEFGHIJKLMNOP"
NUMBER="0123456789"
Symbol="[]{}#*;,_"

all=lower+upper+NUMBER+Symbol
length=9
password="".join(random.sample(all,length))
print("the password you generated is:",password)
# Subscribe my channel
