/* Given an array of numbers sort it with bubble osrt tehnic*/
#include <iostream>

using namespace std;

int main()
{
    int ok=0,aux,n,i,ar[100]={0};
    cin>>n;
    for (i=0;i<n;i++)
        cin>>ar[i];
    
    while(ok==0)
    {
        ok=1;
        for (i=0;i<n-1;i++)
            if (ar[i]>ar[i+1]) 
            {
                aux=ar[i];
                ar[i]=ar[i+1];
                ar[i+1]=aux;
                ok=0;
            }
    }
    for (i=0;i<n;i++)
    cout<<ar[i]<<" ";
}
