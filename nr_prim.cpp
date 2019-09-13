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
