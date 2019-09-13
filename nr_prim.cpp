/*Subprogram f, with one parameter:
- receives through the parameter a natural number with a maximum of 8 digits (a> 1);
- returns the smallest prime divisor of the value of parameter a.
Example: for value 45 of parameter a, the subprogram will return value 3
because a = 32
* 5, and its smallest prime divisor is 3.
a) Write the complete definition of the subprogram f.
b) Write a C++/C program that reads from the keyboard a non-natural number n
(n≤100) and a string of n natural numbers of up to 8 digits each, all numbers in the string
being strictly greater than 1. Using useful subprogram calls f, the program will
determine and will display on the screen all prime numbers in the read string. The determined numbers se
they will display on the screen, separated by a space. If there are no such numbers it will be displayed
the message does NOT EXIST on the screen.*/
#include <iostream>

using namespace std;

int celmd(int a)
{
    for (int d=2;d<a/2+1;d++)
        if (a%d==0)
            return d;
    return 0;
}
int main()
{
   int n,listnr[100]={0};
   cin>>n;
   for (int i=0;i<n;i++)
    cin>>listnr[i];
    int exist=0;
    for (int nr=0;nr<n;nr++)
        if (celmd(nr)==0) 
        {cout<<nr;
        exist=1;
        }
    if exist==0 cout<<"NOT EXIST";
}
