/*
One natural number n (0 <n≤1000000) and the second
line, separated by a space, in non-zero natural numbers (up to 7 digits each)
ascending order.
a) Write a program that reads all the numbers in the file and using an algorithm
efficient in terms of memory used and runtime, determines
for each number read on the second line of the file, the smallest value greater or
equal to this which represents a power of 2. A natural number x is the power of 2 if
there is a natural number k such that x = 2 ^ k
.
The numbers thus determined will be written on the screen, separated by a space.
Example: if the file has the content below
5
3 5 8 9 12
the screen will show:
4 8 8 16 16
*/
#include <iostream>

using namespace std;
int main()
{
    int nrp=1,n,ar[100]={0},i;
    cin>>n;
    for (i=0;i<n;i++)
    cin>>ar[i];
    for (i=0;i<n;i++)
        {
        while(nrp<ar[i])
            nrp=nrp*2;
        cout<<nrp<<" ";
        }
}
