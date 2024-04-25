# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Input 1: s = "()"        
# Output: true

# Input 2: s = "()[]{}"
# Output: true

#Input 3: s = "(]"
# Output: false
# shorter code 
def isValid(s: str) -> bool:
    stack=[]
    for i in s:
        if i=='[':
            stack.append(']')
        elif i=='{':
            stack.append('}')
        elif i=='(':
            stack.append(')')
        elif len(stack)==0 or stack.pop()!=i:
            return False
    return len(stack)==0
if __name__=='__main__':
    expression1="[[()]]" #gives true as an output
    expression2="[[))" # gives false as an output
    print(isValid(expression1))
    print(isValid(expression2))
    




