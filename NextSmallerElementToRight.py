# Problem: Given an  array print the next smaller element(NGE) to right for every element
# The next smaller element for an element x is the first smaller element on right side of x in array. Elements for which no smaller element exist,consider next smaller element as -1

def nextSmallerElementToRight(arr,n):
    list=[]
    stack=[]
    for i in range(n-1,-1,-1):
        if len(stack)==0:
            list.append(-1)
        elif len(stack)>0 and stack[-1]<arr[i]:
            list.append(stack[-1])
        elif len(stack)>0 and stack[-1]>=arr[i]:
            while len(stack)!=0 and stack[-1]>=arr[i]:
                stack.pop(-1)
            # if stack is empty then no  next element is smaller to left for current element
            if len(stack)==0:
                list.append(-1)
            else:
                list.append(stack[-1])
        stack.append(arr[i])
    list.reverse()
    return list
# driver code
if __name__=='__main__':
    arr1=[5,15,10,8,6,12,9,18]
    arr2=[5,4,3,2,1]
    ans1=nextSmallerElementToRight(arr1,len(arr1))
    print(ans1)
    # output ans1=[-1,10,8,6,-1,9,-1,-1]
    ans2=nextSmallerElementToRight(arr2,len(arr2))
    # output ans2=[4,3,2,1,-1]
    print(ans2)