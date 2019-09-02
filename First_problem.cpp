/*In a tree are white globes, twice as many red globes and green globes as 3 less then the number of red globes.
How many globes are there?

Solution in C++:*/
#include<iostream>
using namespace std;
int main()
{
    long long a,gv,gr;
    cin>>a;
    gr=a*2;
    gv=gr-3;
    a=a+gr+gv;
    cout<<a;
}
