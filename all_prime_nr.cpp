/*
Given a number n, print all primes smaller than or equal to n.
Example:
Input : n =10
Output : 2 3 5 7
Input : n = 20
Output: 2 3 5 7 11 13 17 19
*/
#include<iostream>
using namespace std;
int prime(int number)
{
	for (int d = 2; d < number / 2; d++)
	{
		if (number % d == 0)
		{
			return 0;
		}
	}
		return 1;
}
int main()
{
	int number;
	cout << "What is the number?";
	cin >> number;
	for (int i = 2; i <= number; i++)
	{
		if (prime(i) == 1)
			cout << i << " ";
	}
}
