class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = []
        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        f_sorted = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        f_sorted = f_sorted[:k]

        for item in f_sorted:
            result.append(item[0])
        return result
    

        