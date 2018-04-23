def exponent(x, n):
    if (n <0):
        return exponent(1 / x, -n);
    elif( n == 0 ):
        return  1;
    elif (n == 1):
        return  x ;
    elif( n%2==0):
        return exponent(x * x,  n / 2);
    else:
        return x * exponent(x * x, (n - 1) / 2);
print(exponent(2,3)%3)