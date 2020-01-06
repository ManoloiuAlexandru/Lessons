import java.util.*;
import java.io.*;

public class First_problem {
	public static void main(String[] args) {
		int white_globes;
		int red_globes;
		int green_globes;
		int total_globes = 0;

		Scanner scanner = new Scanner(System.in);

		System.out.println("What is the number of white globes?");

		white_globes = scanner.nextInt();
		red_globes = white_globes * 2;
		green_globes = red_globes - 3;
		total_globes = white_globes + red_globes + green_globes;
		System.out.print(total_globes);

	}
}
