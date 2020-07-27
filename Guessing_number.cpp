/*
In the function we are using binary search to guess a number from the interval [low,high]. The reason we use binary search it is because it reaches a solution after at most k=1+[log(high-low+1)].
In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array.
https://www.geeksforgeeks.org/complexity-analysis-of-binary-search/
*/
#include<iostream>
using namespace std;
int guess(int n, int low, int high)
{
	int turns = 0, mid;
	while (high>=low)
	{
		turns += 1;
		mid = (low + high) / 2;
		if (mid == n)
		{
			return turns;
		}
		else if (mid < n)
		{
			low = mid + 1;
		}
		else
		{
			high = mid + 1;
		}
	}
	return turns;
}
int main()
{
	cout << guess(764, 1, 1000000);
}
