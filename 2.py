import math

print ("Выберите функцию\n 1- G\n 2- F\n 3- Y\n")
c = int (input("Номер функции:"))

if c == 1:
	a = float (input ("a:"))
	x = float (input ("x:"))
	if (54*pow(a,2)+87*a*x+35*pow(x,2)) == 0:
		print ("Функция не может быть вычислена так как знаменатель не может быть равен 0\n")
		exit(0)
	G = (3*(3*pow(a,2)-13*a*x+4*pow(x,2)))/(54*pow(a,2)+87*a*x+35*pow(x,2))
	print ("G=""%2f" %G)

elif c == 2:
	a = float (input ("a:"))
	x = float (input ("x:"))	
	F = -tanh(63*pow(a,2)-5*a*x-2*pow(x,2));
	print ("F=""%2f" %F)

elif c == 3:
	a = float (input ("a:"))
	x = float (input ("x:"))
	Y = -asin(8*pow(a,2)-15*a*x-27*pow(x,2));
	print ("Y=""%2f" %Y)
	
else:
	print('Такой функции нету\n')
	