class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        st = set(nums)
        longest = 0

        for num in st:
            if num - 1 not in st:
                current = num
                length = 1

                while current + 1 in st:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest