class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        # list1=[""]
        # if int(num)%2==1:
        #     return num
        # else:
        #     for i in num:
        #         if int(i)%2==1:
        #             list1.append(i)
                        
        #     return max(list1)
   
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""
            