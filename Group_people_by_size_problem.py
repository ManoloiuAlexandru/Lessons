'''
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
'''
class Solution:
    def groupThePeople(self, groupSizes):
        nr_and_length = dict()
        for i in groupSizes:
            nr_and_length[i] = list()
        for i in range(0, len(groupSizes)):
            nr_and_length[groupSizes[i]].append(i)
        final_list = list()
        for key in nr_and_length:
            length_of_list = len(nr_and_length[key])
            while (length_of_list >= key):
                new_list = list()
                for i in range(0, len(nr_and_length[key])):
                    if i % key == 0 and i != 0:
                        final_list.append(new_list)
                        new_list = list()
                        new_list.append(nr_and_length[key][i])
                    else:
                        new_list.append(nr_and_length[key][i])
                    length_of_list -= 1
                final_list.append(new_list)
        return final_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
