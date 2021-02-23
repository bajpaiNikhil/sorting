


def partition(a,low,high):
    i=low-1
    pivot=a[high]

    for j in range(low,high):
        if a[j]<=pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1
def quick_sort(a,low,high):

    if len(a)==1:
        return a
    if low<high:

        pi=partition(a,low,high)

        quick_sort(n,low,pi-1)
        quick_sort(n,pi,high)
    return n
n=[90,80,100,1,0,3,2]
m=len(n)
e=quick_sort(n,0,m-1)
print(e)