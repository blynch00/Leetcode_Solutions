from collections import *
from typing import *
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if len(words) == 1:
            return words[0]
        # Make a counter()
        count = Counter(words)
        # create tuple pairs
        tuple_list = [(key, value) for value, key in count.items()]
        #print(tuple_list)
        # make the tuple list a max heap
        heapq.heapify_max(tuple_list)
        #print(f"Max: {max(tuple_list)} Heap: {tuple_list}")
        
        # Make the final list
        return_words = []
        while len(return_words) < k:
            temp_list = []
            max_count = max(tuple_list)[0]
            while tuple_list and max(tuple_list)[0] == max_count:
                temp_list.append(heapq.heappop_max(tuple_list)[1])
            temp_list.sort()
            return_words += temp_list
        return return_words[:k]