import collections
import heapq
class solution(object):
    def topkFrequently(self,nums,k):
        """
        :type:nums:list[int]
        :type:k: int
        :return: list[int]
        from the the list get the top k frequently element
        such as nums=[1,1,2,2,3]  k=2,频率相关：{1:3,2:2,3:1}, so the resultlist=[1,2]
        """
        counts = collections.Counter(nums)
        heap = []
        for key, cnt in counts.items():
            if len(heap)<k:
                heapq.heappush(heap,(cnt, key))
            else:
                if heap[0][0]<cnt:
                    heapq.heappush(heap,(cnt,key))
        return [x[1] for x in heap]