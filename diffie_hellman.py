import random

p=int(input('Enter any prime number: '))
alpha=[]
l1=[]

def check(a, b):
    for i in range(1, b):
        if i in a:
            continue
        else:
            return False

for i in range(2, p):
    for j in range(1, p):
        val=(i**j)%p
        l1.append(val)
    alpha.append(l1)
    l1=[]
    
fin_alpha=[]
for i in range(len(alpha)):
    if check(alpha[i], p) != False:
        fin_alpha.append(alpha.index(alpha[i])+2)

print('The available values for alpha will be: ', *fin_alpha)

a=random.randint(1, p)
b=random.randint(1, p)
while a==b:
    b=random.randint(1, p)

    
sel_alp=min(fin_alpha)

public_A=(sel_alp**a)%p
public_B=(sel_alp**b)%p
c=a*b
key_a=(sel_alp**c)%p
key_b=(sel_alp**c)%p
print(f'Selected value for alpha: {sel_alp}')
print(f'Public_A: {public_A}')
print(f'Public_B: {public_B}')
print(f'Selected key: {key_a}')