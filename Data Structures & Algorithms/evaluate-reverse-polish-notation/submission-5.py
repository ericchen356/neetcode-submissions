import math 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        for element in tokens: 
            if element != "+" and element != "-" and element != "*" and element != "/":
                stack.append(element)
            else: 
                if element == "+": 
                    evaluated = int(stack[-2]) + int(stack[-1])
                if element == "-":
                    evaluated = int(stack[-2]) - int(stack[-1])
                if element == "*":
                    evaluated = int(stack[-2]) * int(stack[-1])
                if element == "/":
                    evaluated = math.trunc(int(stack[-2]) / int(stack[-1]))
                
                stack.pop()
                stack.pop()
                stack.append(evaluated)
    
        return int(stack[0])