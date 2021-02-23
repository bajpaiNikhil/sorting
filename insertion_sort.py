

def insertion_sort(a):

    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while(j>=0 and key<a[j]):
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return a

n=[90,5,3,4,66,100]
e=insertion_sort(n)
print(e)