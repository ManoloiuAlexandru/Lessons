/*'''A number n is called an extrapolated if both it and any number obtained by the permutation
circular numbers of n, are prime numbers. For example, the number 197 is a number
extrapolated because 197, 971, 719 are prime numbers. Number 23 is not extrapolated
because 32 is not prime.
a) Write the complete definition of a subprogram f, with a parameter, subprogram that:
- receives through the parameter a natural number with a maximum of 2 digits (a> 1);
- returns the sum of all the exponents from the prime factorization of the value
of parameter a.
Example: for a = 90 the subprogram will return the value 4, because a = 2 * 32
* 5 and
1 + 2 + 1 = 4.
b) Write a program that reads from the keyboard a natural number n, 2≤n≤99, and
which, using useful subprogram calls f, checks to see if n is an extra number and
Displays the message YES on the screen, otherwise the message NO.'''*/

#include <iostream>

using namespace std;

int prim(int a)
{
    int sum=0,ca=a;
    for (int d=2;d<ca/2+1;d++)
        {
            int power=0;
            while(a%d==0)
            {
                power++;
                a=a/d;
            }
            if (power!=0)
                sum=sum+power;
        }
    return sum;
}
int extraprim(int a)
{
    if (prim(a)!=0)
        cout<<"NO";
    else
    {
        int inv=0;
        while(a>0)
        {
            inv=inv*10+a%10;
            a=a/10;
        }
        if (prim(inv)!=0)
            cout<<"NO";
        else
        cout<<"YES";
    }
}
int main()
{
   extraprim(13);
}
