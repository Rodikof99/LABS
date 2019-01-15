from math import pow, tanh, asin

a = float(input('a = '))
x = float(input('x = '))

G = (3*(3*pow(a,2)-13*a*x+4*pow(x,2)))/(54*pow(a,2)+87*a*x+35*pow(x,2))

print('G = {}'.format((3*(3*pow(a,2)-13*a*x+4*pow(x,2)))/(54*pow(a,2)+87*a*x+35*pow(x,2))))
print('F = {}'.format(-tanh(63*pow(a,2)-5*a*x-2*pow(x,2))))
print('Y = {}'.format(-asin(x)))
