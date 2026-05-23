class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Montonic Stack: used in stack when counting days in between multiple items
        # "pop before push"

        # if the stack is empty, append item to the stack.

        # If the stack isn't empty, if the day being added is larger than the stack top, change value of answer[i] to high index - low index

        monotonic = []
        answer = [0] * (len(temperatures))
        for x in range(0, len(temperatures)):
            if len(monotonic) == 0:
                monotonic.append(x)
                continue
            # Otherwise, we know there is a day to compare:
            last_day_index = monotonic[-1]
            
            # Case 1: new day is lower/eq to top of stack
            if temperatures[x] <= temperatures[last_day_index]:
                # Just add temperature to top of stack
                monotonic.append(x)
                continue
            
            # Case 2: new day is higher than top of stack
            else:   
                # temperatures[x] > temperatures[last_day_index]
                # Need to min monotonic stack; day on top must always be g/eq to new number
                while temperatures[x] > temperatures[monotonic[-1]]:
                    total_days = x - monotonic[-1]
                    answer[monotonic[-1]] = total_days
                    monotonic.pop()
                    if len(monotonic) == 0:
                        break
                monotonic.append(x)
        return answer

