# Problem: Given an  array print the next greater element(NGE) to left  for every element
# The next greater element for an element x is the first greater element on left side of x in array. Elements for which no greater element exist,consider next greater element as -1

def nextGreaterElementToLeft(arr,n):
    list=[]
    stack=[]
    for i in range(n):
        if len(stack)==0:
            list.append(-1)
        elif len(stack)>0 and stack[-1]>arr[i]:
            list.append(stack[-1])
        elif len(stack)>0 and stack[-1]<=arr[i]:
            while len(stack)!=0 and stack[-1]<=arr[i]:
                stack.pop(-1)
            # if stack is empty then no  next element is greater to left for current element
            if len(stack)==0:
                list.append(-1)
            else:
                list.append(stack[-1])
        stack.append(arr[i])
    return list
# driver code
if __name__=='__main__':
    arr1=[5,15,10,8,6,12,9,18]
    arr2=[5,4,3,2,1]
    ans1=nextGreaterElementToLeft(arr1,len(arr1))
    ans2=nextGreaterElementToLeft(arr2,len(arr2))
    print(ans1)
# output [-1,-1,15,10,8,15,12,-1]
    print(ans2)
# output [-1, 5, 4, 3, 2]