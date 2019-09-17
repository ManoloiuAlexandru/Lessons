/*The following sub-programs are considered defined:
- s1, with two parameters: a, b two integers with a maximum of 4 digits each; subprogram
interchanges the values of two variables transmitted through the parameters a and b.
- s2, with three parameters: a, a one-dimensional array with exactly 100 elements, numbers
integers with a maximum of 4 digits each, p, a natural number (p≤100), q, a natural number
(Q≤100). The subprogram looks for the first element divisible by 5 in the sequence ap, ap + 1, ..., aq,
and returns its position, if there is such an element, or the value -1 in the case
contrary.
a) Only write the subprogram header s1. (4p).
b) Write the complete definition of subprogram s2. (6p).
c) Write the program that reads from the keyboard a natural value n (0 <n≤100) and
then a one-dimensional array of, with n elements, integers up to 4 digits each.
The program determines, using useful calls from subprogram s2, the first divisible element
with 5 (if any) and the last element divisible by 5 (if any) of table a, interchange
find the values of the found elements, using the subprogram call s1, and then write on the first line of
the elements of the painting thus transformed, separated by one
space, or the value 0 if the array contains less than two elements divisible by 5.
Example: for n = 7 and the table a = (6,10,4,15,2,5,8), the program will write to the file:
6 5 4 15 2 10 8*/
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
