import math

exit1 = 0
while exit1 == 0:

	dictg = {}
	dictf = {}
	dicty = {}
	vivod = []
	mas = []
	stg = []
	stf = []
	sty = []
	mas.clear()
	stg.clear()
	stf.clear()
	sty.clear()
	print ('Функция G')	
	sta = input("a:")
	a = float(sta)
	stx = input("x:")
	x = float(stx)
	stx2 = input("x2:")
	x2 = float(stx2)
	stk = input("Количество шагов вычисления:")
	kolshag = float (stk)
	shag = (x2 - x)/kolshag
	if shag > x2:
		print ("Шаг вычисления функции больше чем сама область вычисления функции\n")
		continue

	i = 0
	while x <= x2-shag:
		if (54*pow(a,2)+87*a*x+35*pow(x,2)) == 0:
			print ("Функция не может быть вычислена так как знаменатель не может быть равен 0\n")
			exit(0)
		G = (3*(3*pow(a,2)-13*a*x+4*pow(x,2)))/(54*pow(a,2)+87*a*x+35*pow(x,2))
		mas.append(G)
		stg = "\t".join([str(i) for i in mas])
		print ('{:2f}\t {:2f}'.format(x,mas[i]))
		i = i + 1
		x = x + shag
	print(stg)
	dictg[g] = stg
	sh = input("Задайте шаблон для поиска совпадения ")
	sovp = stg.count(sh)
	print('Колличество совпадений ' '%d' %sovp)
	minimum = min(mas)
	maximum = max(mas)
	print ('Минимальный элемент ''%2f' %minimum)
	print ('Максимальный элемент ''%2f' %maximum)

	print ('Функция F')				
	sta = input("a:")
	a = float(sta)
	stx = input("x:")
	x = float(stx)
	stx2 = input("x2:")
	x2 = float(stx2)
	stk = input("Количество шагов вычисления:")
	kolshag = float (stk)
	shag = (x2 - x)/kolshag
	if shag > x2-shag:
		print ("Шаг вычисления функции больше чем сама область вычисления функции\n")
		continue

	mas.clear()	
	i = 0
	while x <= x2-shag:	
		F = -tanh(63*pow(a,2)-5*a*x-2*pow(x,2))
		mas.append(F)
		stf = "\t".join([str(i) for i in mas])
		print ('{:2f}\t {:2f}'.format(x,mas[i]))
		i = i + 1
		x = x + shag

	print(stf)
	dictf[f] = stf
	sh = input("Задайте шаблон для поиска совпадения")
	sovp = stf.count(sh)
	print('Колличество совпадений ' '%d' %sovp)
	minimum = min(mas)
	maximum = max(mas)
	print ('Минимальный элемент ''%2f' %minimum)
	print ('Максимальный элемент ''%2f' %maximum) 

	mas.clear()
	print ('Функция Y')
	i = 0		
	sta = input("a:")
	a = float(sta)
	stx = input("x:")
	x = float(stx)
	stx2 = input("x2:")
	x2 = float(stx2)
	if a == 0 and x == 0:
		print("\nНевозможно сосчитать функцию.")
		continue
	stk = input("Количество шагов вычисления:")
	kolshag = float (stk)
	shag = (x2 - x)/kolshag
	if shag > x2:
		print ("Шаг вычисления функции больше чем сама область вычисления функции\n")
		continue
	while x <= x2-shag:
		Y = -asin(8*pow(a,2)-15*a*x-27*pow(x,2))
		mas.append(Y)
		sty = "\t".join([str(i) for i in mas])
		print ('{:2f}\t {:2f}'.format(x,mas[i]))
		i = i + 1
		x = x + shag

	print(sty)
	dicty[y] = sty
	sh = input("Задайте шаблон для поиска совпадения")
	sovp = sty.count(sh)
	print('Колличество совпадений ' '%d' %sovp)
	minimum = min(mas)
	maximum = max(mas)
	print ('Минимальный элемент ''%2f' %minimum)
	print ('Максимальный элемент ''%2f' %maximum)



	vivod.append(dictg)
	vivod.append(dictf)
	vivod.append(dicty)
			


	print ("Хотите выйти из программы 1 - да 0 - нет")
	exit1 = int(input())		
	