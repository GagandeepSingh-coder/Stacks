# Problem: Given an  array print the next greater element(NGE) to right for every element
# The next greater element for an element x is the first greater element on right side of x in array. Elements for which no greater element exist,consider next greater element as -1

def nextGreaterElementToRight(arr,n):
    list=[]
    stack=[]
    list.append(-1)
    stack.append(arr[n-1])
    for i in range(n-2,-1,-1):
        while (len(stack)!=0 and stack[-1]<=arr[i]):
            stack.pop(-1)
        if len(stack)==0:
            list.append(-1)
        else:
            list.append(stack[-1])
        stack.append(arr[i])
    list.reverse()
    return list
if __name__=='__main__':
    arr=[5,15,10,8,6,12,9,18]
    ans=nextGreaterElementToRight(arr,len(arr))
    print(ans)
# output  [15,18,12,12,12,18,18,-1]


    
    
