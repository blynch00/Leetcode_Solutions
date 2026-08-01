class Solution:
    def romanToInt(self, s: str) -> int:
        return_int = 0
        # Convert string to array
        new_list = list(s)
        # Track each pairing with a dictionary
        values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sub_pairs = {"IV": 4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        # iterate backwards through pairing, adding to set as needed.
        while len(new_list) - 1 >= 0:
            index = len(new_list) -1
            print(f"Current value: {new_list[index]} = {values[new_list[index]]}")
            if values[new_list[index]] != 1 and len(new_list) != 1:
                print(new_list[index - 1] + new_list[index])
                if (new_list[index - 1] + new_list[index]) in sub_pairs:
                    print(sub_pairs[new_list[index - 1] + new_list[index]])
                    return_int += sub_pairs[new_list[index - 1] + new_list[index]]
                    new_list.pop()
                    new_list.pop()
                    continue
            
            return_int += values[new_list[index]]
            new_list.pop()
        return return_int
                