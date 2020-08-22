class Classic_problems:
    @staticmethod
    def containsDuplicate(nums) -> bool:
        """
        Given an array of integers, find if the array contains any duplicates.
        """
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    @staticmethod
    def fibonaci(nr):
        """
        Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to the Nth number.
        """
        if nr == 1 or nr == 2:
            return 1
        else:
            return Classic_problems.fibonaci(nr - 1) + Classic_problems.fibonaci(nr - 2)

    @staticmethod
    def fizz_buzz():
        """
        Function that prints on each line the numbers from 1 to 100.
        But for multiples of three print "Fizz" instead of the number, and for multiples of five print "Buzz".
        For numbers which are multiples of both three and five print "FizzBuzz".
        """
        for i in range(1, 101):
            if i % 15 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Buzz")
            elif i % 3 == 0:
                print("Fizz")
            else:
                print(i)

    @staticmethod
    def maxSubArray(array):
        """
        Given an integer array nums, returns the contiguous subarray (containing at least one number) which has the largest sum and return its sum
        """
        max_so_far = array[0]
        max_ending_here = 0

        for i in range(0, len(array)):
            max_ending_here += array[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far
