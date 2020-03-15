/*Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
https://leetcode.com/problems/contains-duplicate/
*/
using System;
using System.Collections.Generic;

namespace test1
{
    class Program
    {
        static int containsDuplicates(int[] array_of_elem,int array_length)
        {
            for (int i=0;i< array_length - 1;i++)
            {
                for (int j = i + 1; j < array_length; j++)
                {
                    if (array_of_elem[i] == array_of_elem[j])
                    {
                        return 1;                
                    }
                }
            }
            return 0;
        }
        static void Main(string[] args)
        {
            int[] array_of_elements = new int[100];
            Console.WriteLine("Length of the array:");
            int array_leng = Convert.ToInt32(Console.ReadLine());
            for (int i=0;i<array_leng;i++)
            {
                Console.WriteLine("Numebr in the list");
                int nr = Convert.ToInt32(Console.ReadLine());
                array_of_elements[i] = nr;
            }
            if (Program.containsDuplicates(array_of_elements, array_leng) ==1)
            {
                Console.WriteLine("Contains duplicates");
            }
            else
            {
                Console.WriteLine("Contains non duplicate");
            }
        }
    }
}
