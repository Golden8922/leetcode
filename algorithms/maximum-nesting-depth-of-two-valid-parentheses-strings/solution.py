class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        level=0
        for i in s:
        
            if i=='(':
               level=level+1
               count=max(level,count)
            elif i==')':
                level=level-1  
        return count       