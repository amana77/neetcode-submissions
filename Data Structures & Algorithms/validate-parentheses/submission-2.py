class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        b={")" : "(", "]" : "[", "}" : "{"}
        for i in s:
            if i in b:
                if stack and stack[-1]==b[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False