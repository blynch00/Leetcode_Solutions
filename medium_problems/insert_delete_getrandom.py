import random

class RandomizedSet:

    def __init__(self):
        self.elem_counts = {}
        self.elem_list = []
        self.count = 0
    def insert(self, val: int) -> bool:
        # If not in hash map, insert at the last index of array, and give the key/value pair this value
        if val not in self.elem_counts:
            self.elem_counts[val] = self.count
            self.elem_list.append(val)
            self.count += 1
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        # If we are removing a value that is not at the end, replace the element at removed 
        # index with last index, replace key/value of replacing value, then pop last
        if val in self.elem_counts:
            if self.elem_counts[val] != self.count - 1:  # If not last element
                # Swap last element with current element
                current_index = self.elem_counts[val]
                self.elem_counts[self.count - 1] = current_index
                self.elem_list[current_index] = self.elem_list[self.count - 1]
                # Change counts; set last element's count to old count
                self.elem_list.pop()
                self.count -= 1
                self.elem_counts.pop(val)
                return True
                # Remove index,decrement self.count,  return True

        else:
            return False

    def getRandom(self) -> int:
        # Generate a random integer of values between 0 and len(array) - 1, returning associated number of the given list
        random_index = random.randint(0, self.count-1)
        return self.elem_list[random_index]
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()