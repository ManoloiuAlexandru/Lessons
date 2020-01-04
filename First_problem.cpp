/*In a tree are white globes, twice as many red globes and green globes as 3 less then the number of red globes.
How many globes are there?
Solution in C++:*/
#include<iostream>
using namespace std;
int main()
{
    long long white_globes, green_globes, red_globes,total=0;
    cin >> white_globes;
    red_globes = white_globes * 2;
    green_globes = red_globes - 3;
    white_globes = white_globes + red_globes + green_globes;
    cout << total;
}
