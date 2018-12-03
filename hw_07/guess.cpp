#include <iostream>

int main()
{
	int i, guess;
  	std::cout << "Please enter an integer value between 0-99 (inclusive): " << std::endl;
  	std::cin >> i;

  	for (int guess = 0; guess < 100;) {
  		int ans;
  		std::cout << guess << std::endl;
  		std::cout << "If this is your number, type 0. If this is lower than your number, type -1. If this is higher than your number, type 1" << std::endl;
  		std::cin >> ans;
  		while(ans != 0) {
  			if (ans == -1)
  			{
  				std::cout << ++guess << std::endl;
  			}
  			if (ans == 1)
  			{
  				std::cout << --guess << std::endl;
  			}
  			std::cout << "If this is your number, type 0. If this is lower than your number, type -1. If this is higher than your number, type 1" << std::endl;
  			std::cin >> ans;
  		}
  		if (ans == 0)
  		{
  			std::cout << "Found your number! Thanks for playing" << std::endl;
  		}

  	}

	return 0;
}