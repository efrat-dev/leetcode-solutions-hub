1class Solution(object):
2    def getConcatenation(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        ##First solution
8        # count=0
9        # a=[]
10        # for i in range(2):
11        #   for index in range(len(nums)):
12        #       a.append(nums[index])
13
14        # return a
15
16        ##Pythonic solution - 1
17        # return nums+nums
18
19        ##Pythonic solution - 2
20        return nums*2