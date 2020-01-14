def check(lst):
    size=len(lst)
    size=size-1
    i=0
    while(i!=(size-1)):
        if(lst[i]<lst[i+1]):
            i=i+1
        else:
            return False
    return True

def bubblesort(lst):
    "Sorts lst in place and returns it."
    size=len(lst)
    if len(lst)==0:
        return "no imput"
    for passesLeft in range(len(lst) - 1, 0, -1):  # run from the end to the start
        for index in range(passesLeft):
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    if(size!=len(lst)):
        return "the array lost value"
    if(check(lst)==False):
        return "List not Sorted"
    else:
      return lst

a=[1,4,3,7,8,3,0]
bubblesort(a)
print(a)
