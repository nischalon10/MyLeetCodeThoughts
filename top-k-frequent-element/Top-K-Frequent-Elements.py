class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in range(0,len(nums)):
            if nums[i] not in dict1.keys():
                dict1[nums[i]] = 1 
            else:
                dict1[nums[i]] += 1
        sorteddict = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
        res = []
        for i in sorteddict[0:k]:
            res.append(i[0])
        return res
