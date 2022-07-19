# https://www.hackerrank.com/challenges/balanced-brackets/problem

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack=[]
    s=list(s)
    ans=[]
    for i in range(len(s)):
        if len(stack)==0 and (s[i]==')' or s[i]==']' or s[i]=='}'):
            return "NO"
        if s[i]=='(' or s[i]=='[' or s[i]=='{':
            stack.append(s[i])
            # s.remove(s[i])
            continue
        if (s[i]==')' and stack[-1]=='(') or (s[i]==']' and stack[-1]=='[') or (s[i]=='}' and stack[-1]=='{'):
            stack.pop()
            # s.remove(s[i])
        else:
            ans.append(s[i])
            
    if len(stack)==0 and len(ans)==0:
        return "YES"
    else:
        return "NO"
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
