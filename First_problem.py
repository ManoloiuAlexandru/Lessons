'''In a tree are white globes, twice as many red globes and green globes as 3 less then the number of red globes.
How many globes are there?

Personal note:
The time complexity of this program is: O(1)
Solution in Python:'''

white_globes = int(input())
red_globes = white_globes * 2
green_globes = red_globes - 3
total_globes = white_globes + red_globes + green_globes
print(total_globes)
