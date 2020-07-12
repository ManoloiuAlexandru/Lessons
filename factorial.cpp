/*Write a C ++ program that returns for a natural number n transmitted as a parameter the value of n!, Ex: 1 • 2 • ... • n.*/
#include <iostream>

using namespace std;

int fact(int n)
{
    int i,p=1;
    for (i=1;i<=n;i++)
        p=p*i;
    if (n==0) return 1;
    else return p;
}

int main()
{
    int n;
    cin>>n;
    cout<<fact(n);
}
