class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if a == nums[i-1] and i > 0:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r-= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res




#In 3Sum, we sort the array so every triplet can be treated in increasing order (x ≤ y ≤ z),
#which gives each combination a single, unique form. We fix a as the smallest number and use
#two pointers to find the other two values to the right, knowing that moving the left pointer
#increases the sum and moving the right pointer decreases it — this only works because the 
#array is sorted. Once we finish all pairs for a given a, we never revisit earlier numbers 
#(like going back to -4) because any triplet involving them was already counted when they 
#were the smallest value. If the array were unsorted, this logic would break because pointer 
#movement wouldn’t reliably change the sum, causing us to miss valid combinations or check 
#things incorrectly. A hash map works for 2Sum because you only need to find one missing 
#number, but in 3Sum you need a pair of numbers that work together, and without sorting, 
#you’d generate the same triplet in different orders (like [-1, 0, 1], [0, -1, 1], etc.), 
#requiring extra work to remove duplicates — sorting avoids all of this by enforcing 
#structure and ensuring each triplet is found exactly once.