#include <stdio.h>
#include <math.h>

int main()
{

int error;
char c;
float F, G, Y, a, x;

printf(" 1-G\n 2-F\n 3-Y\n");
printf ("Выберите функцию \n");
scanf ("%c", &c);

switch (c)
{
	case '1':
	   printf ("Введите число a \n");
       scanf ("%f", &a);
       printf ("Введите число x \n");
       scanf ("%f", &x);
       if ((54*pow(a,2)+87*a*x+35*pow(x,2)) == 0)
	        {
	        error = 1; 	
		    printf("Функция не может быть вычислена так как знаменатель не может быть равен 0\n");
		    break;
	        }
	   G = (3*(3*pow(a,2)-13*a*x+4*pow(x,2)))/(54*pow(a,2)+87*a*x+35*pow(x,2));
	   printf("%f\n",G);
	break;

	case '2':
	   printf ("Введите число a \n");
       scanf ("%f", &a);
       printf ("Введите число x \n");
       scanf ("%f", &x);
	   F = -tanh(63*pow(a,2)-5*a*x-2*pow(x,2));
	   printf("F=%f\n",F);
	break;

	case '3':
	   printf ("Введите число a \n");
       scanf ("%f", &a);
       printf ("Введите число x \n");
       scanf ("%f", &x);
	   Y = -asin(8*pow(a,2)-15*a*x-27*pow(x,2));
	   printf("Y=%f\n",Y);
	break;

	default:
		printf("Такой функции нету \n");
		error = 4;
	break;
}
	return error;
}
