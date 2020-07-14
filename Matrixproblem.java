//To give a quadratic matrix of dimension n * n calculate the last digit of the product of the elements on line k.''

import java.util.Scanner;

public class Matrixproblem {
public static void main(String[] args) 
	{
		Scanner scanner = new Scanner(System.in);
		System.out.println("n=");
		Integer n=scanner.nextInt();
		System.out.println("k=");
		Integer k=scanner.nextInt();
		Integer[][] matrix=new Integer[100][100];
		for (Integer l=0;l<n;l++)
		{
			for (Integer c=0;c<n;c++)
			{
				System.out.println("Element=");
				matrix[l][c]=scanner.nextInt();
			}
		}
		Integer product=1;
		for (Integer c=0;c<n;c++)
		{
			product*=matrix[k-1][c];
		}
		System.out.print(product);
	}
}
