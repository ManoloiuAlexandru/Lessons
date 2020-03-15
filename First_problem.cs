/*In a tree are white globes, twice as many red globes and green globes as 3 less then the number of red globes.
How many globes are there?*/
using System;

namespace test1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("How many globes are ?");
            int white_globes = Convert.ToInt32(Console.ReadLine());
            int red_globes = white_globes * 2;
            int green_globes = red_globes - 3;
            int total_globes = white_globes + red_globes + green_globes;
            Console.WriteLine("Total Globes:" + total_globes);
        }
    }
}
