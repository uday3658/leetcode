class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        left = 0
        count = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[i])
            count = max(count, i - left + 1)

        return count
        # count=0
        # dict1=dict()
        # for i in range(len(s)-1):
        #     if str(s[i])==str(s[i+1]):
        #         count+=0
        #     else:
        #         count+=1 
        #         dict1[count]=count   
        # print(dict1)    
        # return count  

        
        