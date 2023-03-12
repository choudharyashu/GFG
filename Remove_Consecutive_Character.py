#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        result=""
        top=0
        for c in S:
            if len(result)==0:
                result+=c
                top=0
            elif result[top]!=c:
                result+=c
                top+=1
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends