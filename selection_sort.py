

def selection_sort(a):

    for i in range(len(a)):
        mim_index=i
        for j in range(i+1,len(a)-1):
            if a[j]<a[mim_index]:
                mim_index=j
        a[i],a[mim_index]=a[mim_index],a[i]
    return a

n=[11,34,5,3,1,2,55]
e=selection_sort(n)
print(e)