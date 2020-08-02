/*
Write a program that prints on each line the numbers from 1 to n.
But for multiples of three print "Fizz" instead of the number, and for multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
*/
#include<iostream>
using namespace std;
void FizzBuzz(int n)
{
	for (int i = 0; i <= n; i++)
	{
		if (i % 15 == 0)
		{
			cout << "FizzBuzz" << endl;
		}
		else if (i % 5 == 0)
		{
			cout << "Buzz" << endl;
		}
		else if (i % 3 == 0)
		{
			cout << "Fizz" << endl;
		}
		else
		{
			cout << i << endl;
		}
	}
}
int main()
{
	int n;
	cin >> n;
	FizzBuzz(n);
}
