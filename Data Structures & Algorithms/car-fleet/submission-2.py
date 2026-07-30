class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pair = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        
        pair.sort()

        for i in range(len(pair)-1, -1, -1):
            time = (target - pair[i][0]) / pair[i][1]
            stack.append(time)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()                
        
        return len(stack)