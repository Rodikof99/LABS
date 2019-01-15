import math

exit1 = 0
while exit1 == 0:

	mas = []	
	print("Функция G - 1, Функция F - 2, Функция Y - 3, Введите число: \n")
	number = int(input())
	
	if number == 1:
		i = 0
		a = float (input ("a:"))
		x = float (input ("x:"))
		x2 = float (input("x2:"))
		shag = float (input("Шаг вычисления:"))
		if shag > x2:
			print ("Шаг вычисления функции больше чем сама область вычисления функции\n")
			continue
		while x <= x2:
			if (54*pow(a,2)+87*a*x+35*pow(x,2)) == 0:
				print ("Функция не может быть вычислена так как знаменатель не может быть равен 0\n")
				exit(0)
			G = (3*(3*pow(a,2)-13*a*x+4*pow(x,2)))/(54*pow(a,2)+87*a*x+35*pow(x,2))
			mas.append(G)
			print ('{:2f}\t {:2f}'.format(x,mas[i]))
			i = i + 1
			x = x + shag

		minimum = min(mas)
		maximum = max(mas)
		print ('Минимальный элемент ''%2f' %minimum)
		print ('Максимальный элемент ''%2f' %maximum) 	 	
				

	elif number == 2:
		i = 0
		a = float (input ("a:"))
		x = float (input ("x:"))
		x2 = float (input("x2:"))
		shag = float (input("Шаг вычисления:"))
		if shag > x2:
			print ("Шаг вычисления функции больше чем сама область вычисления функции\n")
			continue
		while x <= x2:	
			F = -tanh(63*pow(a,2)-5*a*x-2*pow(x,2))
			mas.append(F)
			print ('{:2f}\t {:2f}'.format(x,mas[i]))
			i = i + 1
			x = x + shag

		minimum = min(mas)
		maximum = max(mas)
		print ('Минимальный элемент ''%2f' %minimum)
		print ('Максимальный элемент ''%2f' %maximum) 	 	
			
	elif number == 3:
			a = float (input ("a:"))
			x = float (input ("x:"))
			x2 = float (input("x2:"))
			if a == 0 and x == 0:
				print("\nНевозможно сосчитать функцию.")
				continue
			shag = float (input("Шаг вычисления:"))
			if shag > x2:
				print ("Шаг вычисления функции больше чем сама область вычисления функции\n")
				continue
			while x <= x2:	
				Y = -asin(8*pow(a,2)-15*a*x-27*pow(x,2))
				mas.append(Y)
				print ('{:2f}\t {:2f}'.format(x,mas[i]))
				i = i + 1
				x = x + shag

			minimum = min(mas)
			maximum = max(mas)
			print ('Минимальный элемент ''%2f' %minimum)
			print ('Максимальный элемент ''%2f' %maximum)
			
	else:
		print('Такой функции нету\n')

	print ("Хотите выйти из программы 1 - да 0 - нет")
	exit1 = int(input())		
	