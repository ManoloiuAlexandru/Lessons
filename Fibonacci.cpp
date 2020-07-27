/*
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to the Nth number.
*/
#include<iostream>
using namespace std;
int fibonaci(int nr)
{
	if (nr == 1 || nr == 2)
	{
		return 1;
	}
	else
	{
		return fibonaci(nr - 1) + fibonaci(nr - 2);
	}
}
int main()
{
	int number;
	cout << "What element from the Fibonacci Sequence you want ?";
	cin >> number;
	cout << fibonaci(number);
}
