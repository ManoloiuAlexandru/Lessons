/*The following sub-programs are considered defined:
- p1 which receives by means of parameter n a natural number with a maximum of 8 digits and
returns the sum of the digits of the number received by parameter n
Example: if n is equal to 1234 the value returned by the subprogram will be 10.
-p2 which receives through the parameter n a natural number with a maximum of 8 digits,
deletes the last digit of this number and returns the new number obtained.
Example: if n is equal to 1234 the value returned by the subprogram will be 123.
a) Write only the header of the subprograms p1 and p2.
b) Write a C/C++ program that reads from the keyboard a natural number n with n
8 digits and determines, by useful calls of subprograms p1 and p2, the number of digits
equal to 0 from his writing n. The program will display the number obtained.
Example: if n is 102030, the program will display the value 3.*/

#include <iostream>

using namespace std;

int p1(int n)
{
    int sum=0;
    while(n>0)
    {
        sum=sum+n%10;
        n=n/10;
    }
    return sum;
}
int p2(int &n)
{
    n=n/10;
    return n;
}
int main()
{
    int n,nrz=0;
    cin>>n;
    while(n>0)
    {
        if (p1(n%10)==0)
            nrz++;
        n=p2(n);
    }
    cout<<nrz;
}
