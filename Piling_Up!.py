# https://www.hackerrank.com/challenges/piling-up/problem

# =======================================:Approch 1:========================================= 
for test in range(int(input())):
    n = int(input())
    values = list(map(int, input().split()))
    
    i = 0
    while i < n - 1 and values[i] >= values[i + 1]:
        i += 1
    # print(i)
    while i < n - 1 and values[i] <= values[i + 1]:
        i += 1
    # print(i)
    
    
    if i==n-1:
        print('Yes')
    else:
        print('No')


# =======================================:Approch 2:========================================= 
def blocksfun(n, blocks):
    i=0
    j=n-1
    cube  = list(blocks)
    stack = []
    while i<j:
        if cube[i]>cube[j]:
            stack.append(cube[i])
            i+=1
        else:
            stack.append(cube[j])
            j-=1
            
    stack.append(cube[i])
            
    # print(stack)
    count=0
    for x in range(len(stack)-1):
        if stack[x] >= stack[x+1]:
            continue
        else:
            count+=1
            
    if count==0:
        return "Yes"
    else:
        return "No"
        
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
            
        result = blocksfun(n, arr)
        
        print(result)