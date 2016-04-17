import numpy as np
import sympy as sy


# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
    ans = 0
    x,y = np.polynomial.legendre.leggauss(n);   
    i = 0;
    if((a==-1)&(b==1)):
        while(i<n):
            ans += y[i]*f(x[i]);
            i = i+1;
    else:
        while(i<n):
            ans += y[i]*((b-a)/2)*f((a+b)/2 + (b-a)*(x[i])/2); 
            i = i+1;

    return ans

if __name__ == "__main__":
    def f(x):
        return (x**2 +7*x)/(1 +np.sqrt(x))**4
    
    def my_integral():
        x = sy.Symbol('x')
        ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
        return ans
    
    print('Answer:                    I = ', my_integral())
    print('Your implementation gives: I = ', gausslegendre(f, 0,1))

  
 