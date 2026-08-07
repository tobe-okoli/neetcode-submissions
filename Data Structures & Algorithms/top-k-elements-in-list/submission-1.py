class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] +=1

        n = len(nums)
        if n == 0:
            return nums
        
        buckets = []
        for i in range(n + 1):
            buckets.append([])
        for num, count in frequency.items():
            buckets[count].append(num)
        output = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
        return output
       
        