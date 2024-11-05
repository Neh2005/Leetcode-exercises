class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_check,t_check={},{}
        for i in s:
            s_check[i]=s_check.get(i,0)+1
        
        for j in t:
            t_check[j]=t_check.get(j,0)+1
                
        return s_check==t_check

  """Time complexity: O(n)"""
  """Space complexity: O(1)"""
