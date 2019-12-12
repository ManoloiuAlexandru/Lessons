/* Given an array of numbers sort it with bubble sort algorithm*/
import java.util.Scanner;

public class Test {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Number of numbers ? ");
		int n = scanner.nextInt();
		int[] array = new int[100];
		for (int i=0;i<n;i++)
		{
			System.out.println("The number ? ");
			array[i]= scanner.nextInt();
		}
		int ok=0,i,aux;
		while(ok==0)
		{
			ok=1;
			for (i=0;i<n-1;i++)
				if (array[i]>array[i+1]) 
				{
					aux=array[i];
					array[i]=array[i+1];
					array[i+1]=aux;
					ok=0;
				}
		}
		for (i=0;i<n;i++)
			System.out.print(array[i]+" ");
	}
}
