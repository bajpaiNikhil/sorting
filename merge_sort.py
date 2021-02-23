



def merge_sort(a):
    if len(a)>1:
        mid=len(a)//2
        l=a[0:mid]
        r=(a[mid:])

        merge_sort(l)
        merge_sort(r)

        i,j,k=0,0,0

        while(i<len(l) and j<len(r)):
            if l[i]<r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1
        while(i<len(l)):
            a[k]=l[i]
            i+=1
            k+=1

        while(j<len(r)):
            a[k]=r[j]
            j+=1
            k+=1
    return a

n=[90,1,2,34,65,0]
e=merge_sort(n)
print(e)