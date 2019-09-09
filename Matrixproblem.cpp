/*
To give a quadratic matrix of dimension n * n calculate the last digit of the product of the elements on line k.*/

#include <iostream>

using namespace std;

int main()
{
    int p=1,l,c,k,a[100][100],n;
    cin>>n;
    for (l=1;l<=n;l++)
        for (c=1;c<=n;c++)
            cin>>a[l][c];
    
    cin>>k;
    
    for (c=1;c<=n;c++)
        p=p*a[k][c];
    
    cout<<p%10;
    
}
