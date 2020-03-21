KAPREKAR_CONSTANT = 6174

def num_kaprekar_iterations(n):
  # Fill this in.
    l , m , c = int(''.join(sorted(set(str(n)))[::-1]) +'0') , int(''.join(sorted(set(str(n)))) )  , 0
    while n !=   KAPREKAR_CONSTANT:
        n = l - m
        #print(l , '-' , m , '=' , n)
        c+=1
        l , m = int(''.join(sorted(set(str(n)))[::-1]) ) , int(''.join(sorted(set(str(n)))) ) 
    return c 
print (num_kaprekar_iterations(123))
