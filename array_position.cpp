#include <iostream>

using namespace std;

void s1(int &a,int &b)
{
    int aux;
    aux=a;
    a=b;
    b=aux;
}
int s2(int v[],int p, int q)
{
    if (p<q)
        for (int i=p;i<q;i++)
            if (v[i]%5==0)
                return i;
    if (p>q)
        for (int i=p-1;i>=q;i--)
            if (v[i]%5==0)
                {
                    return i;
                    break;
                }
    return -1;
}
int main()
{
   int n,i,v[100]={0},poz_first,poz_last;
   cin>>n;
   for (i=0;i<n;i++)
        cin>>v[i];
    
    if (s2(v,0,n)!=s2(v,n,0))
    {
        poz_first=s2(v,0,n);
        poz_last=s2(v,n,0);
        if (poz_first!=-1 or poz_last!=-1)
            s1(v[poz_first],v[poz_last]);
    }
    for (i=0;i<n;i++)
        cout<<v[i]<<" ";
}
