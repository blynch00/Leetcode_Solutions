class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create stack
        stack = []
        # Create separate list of (pos, speed) pairs
        car_values = [p for p in zip(position, speed)]
        
        # sort tuples in decreasing order
        car_values.sort(reverse=True)

        # for x in range(0, len(pairs))
        for x in range(0, len(car_values)):

            # Determine time to reach end
            tte = float((target - car_values[x][0]) / car_values[x][1])
            # If stack is empty, append and continue
            if len(stack) == 0:
                stack.append(car_values[x])
                continue
            # Compare time to top of stack:
            top_tte = (target - stack[-1][0]) / stack[-1][1]
            if top_tte < tte:
                stack.append(car_values[x])
            # If top of stack reaches the destination before the current car, append and continue

            # Else, the top of stack is ge/eq to current car, so we can pop() the car which moves slower
            else:
                if stack[-1][0] > car_values[x][0]:
                    continue
                else:
                    stack.pop()
                    stack.append(car_values[x])
        return len(stack)
            # return len(stack)