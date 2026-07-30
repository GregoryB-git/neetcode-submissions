class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in '+-*/':
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if tokens[i] == '+':
                        res = a + b
                    elif tokens[i] == '-':
                        res = a - b
                    elif tokens[i] == '*':
                        res = a * b
                    elif tokens[i] == '/':
                        res = int(a / b)
                    print(tokens)
                    print(i)
                    print(tokens[:i-2])
                    print(str(res))
                    print(tokens[i+1:])
                    
                    tokens = tokens[:i-2] + [str(res)] + tokens[i+1:]
                    print(tokens)
                    break
        return int(tokens[0])

                


        return eval(res)
