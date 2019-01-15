#include <stdio.h>
#include <math.h>

int main()
{
	float a,x;
	printf("Введите значения переменных:\n");
	scanf("%f", &a);
	scanf("%f", &x);
	float G = (3*(3*pow(a,2)-13*a*x+4*pow(x,2)))/(54*pow(a,2)+87*a*x+35*pow(x,2));
	float F = -tanh(63*pow(a,2)-5*a*x-2*pow(x,2));
	float Y = -asin(8*pow(a,2)-15*a*x-27*pow(x,2));
	printf("G = %f\nF = %f\nY = %f\n", G, F, Y);
	return 0;
}
