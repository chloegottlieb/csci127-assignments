#include <iostream>
#include <math.h>

void discriminant(int a, int b, int c) {
	int discrimA = (a);
	std::string discrimX2 = "(x)^2)+";
	int discrimB = (b);
	std::string discrimX= "(x)+";
	int discrimC = (c);
	std::string discrim0 = "=0";
	std::cout << discrimA;
	std::cout << discrimX2;
	std::cout << discrimB;
	std::cout << discrimX; 
	std::cout << discrimC; 
	std::cout << discrim0 << std::endl;
	int discrim = ((pow(b, 2))-((4)*(a)*(c)));
	std::cout << "The discriminant is equal to ";
	std::cout << discrim << std::endl;
	// std::cout << a
	// std::cout << "(x)^2)+";
	// std::cout << b;
	// std::cout << "(x)+";
	// std::cout << c;
	// std::cout << "=0" << std::endl;
	return;
} 

int quadsolve(int a, int b, int c) {
	// discriminant(a,b,c);
	int discrim = ((pow(b, 2))-((4)*(a)*(c)));
	int quadpos = ((-b)+sqrt(((pow(b, 1))-(4)*(a)*(c))))/((2)*(a));
	if (discrim >= 0) {
		int quadpos = ((-b)+sqrt(((pow(b, 1))-(4)*(a)*(c))))/((2)*(a));
		std::cout << "The discriminant is positive so the quadratic is ";
		std::cout << quadpos << std::endl;

	}
	else if (discrim < 0) {
		std::cout << "The discriminant is negative, return ";
		std::cout << 0 << std::endl;
	}
}

int main() {
	int x=2;
	int y=9;
	int z=11;
	// int j=1;
	// int k=4;
	// int l=-5;
	discriminant(x,y,z);
	quadsolve(x,y,z);
	// discriminant(j,k,l);
	// quadsolve(j,k,l);
// 	return 0;
}

