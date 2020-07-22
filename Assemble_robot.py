'''
Vlad has build a robot that can build different items from small parts. Vlad wants to estimate the time it will take for his robot to build the item

Vlad will provide an estimate about the time it will take for the item to be created based on the size of each of the parts. The robot can only combine 2 parts at a time.
The time required to put 2 parts together is equal to the sum of the parts size. The size of the newly constructed part is also equal to the sum of the part's sizes.
This process is repeated until all of the parts have been merged together to form the final product.

Write an algorithm to output the minimum possible time to put the N parts together and build the final product.

Input
The input to the function consists of two arguments:
numOfParts, an integer representing the number of the parts;
parts a list of the integers representing the size of the parts.

Output
Return an integer representing the minimum time required to assemble all the parts.

Constraints
0<numOfParts<1000000
0<parts[i]<1000000
0<=i<numOfParts

If numOfParts is one then return 0

Example
Input
numOfParts=4
parts=[8,4,6,12]

Output
58

The best way to assemble the parts is as follows:
1)Assemble the parts 4 and 6 the time is 10; Size of the remaining parts:[8,10,12]
2)Assemble the parts 8 and 10 the time is 18; Size of the remaining parts:[18,12]
3)Assemble the parts 18 and 12 the time is 30;
The total time required to assemble the parts is 10+18+30=58.
'''


def minTime(numOfParts, parts):
    if numOfParts == 1:
        return 0
    else:
        parts = sorted(parts)
        final_parts = list()
        while len(parts) > 1:
            final_parts.append(parts[0] + parts[1])
            parts = parts[2:]
            parts.append(final_parts[-1])
            parts = sorted(parts)
        return sum(final_parts)


if __name__ == '__main__':
    print(minTime(4, [8, 4, 6, 12]))
