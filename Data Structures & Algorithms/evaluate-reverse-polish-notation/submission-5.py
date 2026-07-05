class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op=[]
        for t in tokens:
            if t in '+-*/':
                b=op.pop()
                a=op.pop()
                if t=='+':
                    a=a+b
                elif t=='-':
                    a=a-b
                elif t=='*':
                    a=a*b
                elif t=='/':
                    a=int(a/b)
                op.append(a)
            else:
                op.append(int(t))
        return op[0]
