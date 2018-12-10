#include <iostream>
#include <math.h>

void sumofsquares(int a, int b) {
		for (int i = a; i < b; ++i)
		{
			int A = pow(a, 2);
			int B = pow(b, 2);
			int newA = pow(i, 2);
			int sum = A + newA + B;
			std::cout << "The sum of the squares of each number is ";
			std::cout << sum << std::endl;
		}
		//the correct answer will always be the last, i've been unable to get it to print only that
		
	}


int main()
{
	int x = 7;
	int y = 9;
	sumofsquares(x,y);
	return 0;
}