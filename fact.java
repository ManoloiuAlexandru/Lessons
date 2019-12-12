/*Write a C ++ program that returns for a natural number n transmitted as a parameter the value of n!, Ex: 1 • 2 • ... • n.*/
import java.util.Scanner;

public class Test {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("On what number do you want to make a factorial ? ");
		int nr = scanner.nextInt();
		long result=1;
		for (int i=1;i<=nr;i++)
		{
			result=result*i;
		}
		System.out.print(result);
	}
}
