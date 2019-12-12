import java.util.Scanner;

public class Test {
	public static long fibonaci(int nr)
	{
		if (nr ==1 || nr==2)
		{
			return 1;
		}
		else
		{
			return fibonaci(nr-1)+fibonaci(nr-2);
		}
	}
public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("What element from the Fibonacci Sequence you want ?");
		int n = scanner.nextInt();
		long res=fibonaci(n);
		System.out.print(res);
	}
}
