# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:29:05 2020

@author: wangjingxian
"""

#1、快速排序
'''
（1）从数列中挑出一个元素作为’基准‘（pivot)
（2）重新排序序列，所有比基准值小的元素放在基准前面，所有比基准值大的元素放在基准后面。
在这个分割结束之后，该基准就处于数列中间位置，称为分割操作。
（3）递归的把小于基准值元素的子数列和大于基准值元素的子树列进行排序。
递归到最底部时，数列的大小是0或1，排序完成。
'''
#平均时间复杂度：O（nlogn),不稳定
def quick_sort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i<=pivot]
        greater=[i for i in array[1:] if i>pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)

array_original=[3,2,7,5,9,6]
array_sorted=quick_sort(array_original)
print(array_sorted)


#2、归并排序
'''
分治法的典型应用，先分解再合并，在合并的过程中实现排序。
（1）使用递归将原数列使用二分法分成多个子列；
（2）申请空间将两个子列排序合并然后返回；
（3）将所有子列一步一步合并最后完成排序

如何将两个有序数列合并？
比较两个数列的第一个数，谁小先取谁，取后再对应数列中删除这个数。然后在进行比较，如果
有数列为空，那直接将另一数列的数据取出即可。
'''
#时间复杂度：O（nlog2n),稳定

def merge(left,right):
    result=[]
    while left and right:
        if left[0]<right[0]:
            result.append(left.pop(0))           
        else:
            result.append(right.pop(0))            
    if left:
        result+=left
    if right:
        result+=right
    return result

def merge_sort(numberlist):
    if len(numberlist)<=1:
        return numberlist
    mid=int(len(numberlist)/2)
    left=numberlist[:mid]
    right=numberlist[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)

array_original=[3,2,7,5,9,6]
array_sorted=merge_sort(array_original)
print(array_sorted)    
    
    
#3、插入排序 
'''
核心思想：不断比较并移动   
（1）第一个元素已经认为被排序。
（2）取出下一个元素，在已经排序的元素序列中从后往前扫描，如果前面的元素比当前元素大，则将前面元素后移，
当前元素依次前移，直到找到比它小或等于它的元素查到其后面。
'''
#平均时间复杂度：O（n^2),稳定性好

def insert_sort(data):
    for k in range(1,len(data)):
        cur=data[k]
        j=k
        while j>0 and data[j-1]>cur:
            data[j]=data[j-1]
            j-=1
        data[j]=cur
    return data

array_original=[3,2,7,5,9,6]
array_sorted=insert_sort(array_original)
print(array_sorted)        
  
  
#4、堆排：还没看懂
'''
核心思想：把数组转换成最大堆积（Max-Heap Heap),这是一种满足最大堆积性质的二叉树：对于除了根之外的每个节点i，
A[parent（i）]>=A[i]
重复从最大堆积取出数值最大的节点（把根节点和最后一个节点交换，把交换后的最后一个节点移除堆），并让残余的堆积维持最大堆性质。
算法步骤：
（1）构造最大堆（Build_Max_Heap）：若数组下标范围为0~n,考虑到单独一个元素是大根堆，则从下标n/2开始的元素均为大根堆。于是，只要从n/2-1开始，
向前依次构成大根堆，这样就能保证，构造到某个节点时，它的左右子树都已经是大根堆。
（2）堆排序(HeapSort)：由于堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。因此需要将堆化数组有序化。
思想是移除根节点，并做最大堆调整的递归运算。第一次将heap[0]与heap[n-1]交换，再对heap[0...n-2]做最大堆调整。
第二次将heap[0]和heap[n-2]交换，再对heap[0...n-3]做最大堆调整。重复该操作直至heap[0]和heap[1]交换。
（3）最大堆调整（Max-Heapify):该方法是提供给上述两个过程调用的。目的是将堆的末端子节点做调整，使得子节点永远小于父节点。
归纳：
堆排序就是把堆顶的最大数取出，把剩余的堆继续调整为最大堆，以递归实现。
'''
def heap_sort(ary):
    n=len(ary)
    first=int(n/2-1)#最后一个非叶子节点
    for start in range(first,-1,-1):#构建最大堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):#堆排，将最大堆排转换成有序数组
        ary[end],ary[0]=ary[0],ary[end]#将根节点元素与最后叶子节点进行互换，取出最大根节点元素，对剩余节点重新构建最大堆。
        max_heapify(ary,0,end-1)#因为end上面取的是n-1，因此这里直接房end-1，相当于忽略了最后最大根节点元素ary[n-1]
    return ary


#最大堆调整：将堆的末端子节点做调整，使得子节点永远小于父节点。
#start为当前需要调整最大堆的位置，end为调整边界。
def max_heapify(ary,start,end):
    root=start
    while True:
        child=root*2+1
        if child>end:
            break
        if child+1<=end and ary[child]<ary[child+1]:
            child=child+1
        if ary[root]<ary[child]:
            ary[root],ary[child]=ary[child],ary[root]
            root=child
        else:
            break

array_original=[3,2,7,5,9,6]
array_sorted=heap_sort(array_original)
print(array_sorted) 


#5、希尔排序
'''
整体思想：
将固定间隔的几个元素之间排序，然后再缩小这个间隔。
（1）计算一个增量（间隔）值。
(2)对元素进行增量元素比较，比如增量值为7，那么就对0，7，14，21...个元素进行插入排序
（3）然后对1，8，15，...进行排序，依次递增进行排序。
（4）所有元素排序完成，缩小增量比如为3，然后重复上述第2，3步
（5）最后缩小增量至1，数列已经基本有序，最后一遍普通插入即可。
'''
#平均时间复杂度：O（nlog2n),不稳定。


def shell_sort(alist):
    # [5,4,3,2,1] ([5,3,1] [4,2]) ([3,5,1] [2,4]) ([1,3,5] [2,4])[1,2,3,4,5]
    n = len(alist)
    gap = int(n/2)
    while gap>0:
        for i in range(gap,n):
            while i > 0:
                if alist[i - gap] > alist[i]:
                    alist[i - gap], alist[i] = alist[i], alist[i - gap]
                i = i - gap
        gap = gap//2
    return alist

array_original=[3,2,7,5,9,6]
array_sorted=shell_sort(array_original)
print(array_sorted) 



#6、简单选择排序
'''
（1)首先在未排序序列中找到最小（大）元素，存放在排序序列的起始位置
（2）然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
（3）以此类推，直到所有元素均排序完毕。
'''
#平均时间复杂度：O（n^2),处理数组问题不稳定，链表问题则稳定。
def findSmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if smallest>arr[i]:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def selectSort(arr):
    newArr=[]
    while arr:
        smallest=findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
        
array_original=[3,2,7,5,9,6]
array_sorted=selectSort(array_original)
print(array_sorted)          




#7、冒泡排序
'''
(1)从第一个元素和第二个元素开始比较，如果第一个比第二个大，就交换位置，然后比较第二个和第三个，逐渐往后，
经过第一轮后最大的元素已经排在最后。
（2）重复上述操作，第二大的则会排在倒数第二的位置，第i大的会排在第i位置。
（3）将这个步骤重复n-1次即可完成排序，因为最后一次只有一个元素，所以不需要比较。
'''
#平均时间复杂度：O（n^2),稳定。

def bubble_sort(numberlist):
    length=len(numberlist)
    for i in range(length):
        for j in range(1,length-i):
            if numberlist[j-1]>numberlist[j]:
                numberlist[j],numberlist[j-1]=numberlist[j-1],numberlist[j]
    return numberlist

array_original=[3,2,7,5,9,6]
array_sorted=bubble_sort(array_original)
print(array_sorted)   

 
    