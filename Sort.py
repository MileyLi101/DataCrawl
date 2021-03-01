
# Sort

########################### insert sort #############################
def insert_sort(array):
	for j in range(1, len(array)):
		i = j - 1
		x = array[j]
		while i >= 0 and array[i] > array[j]:
			array[i+1] = array[i]
			i -= 1
		array[i+1] = x
	return array

print(insert_sort([1,5,2,4,7,9]))


########################### heap sort #############################
import random
 
def sift(data, root, end):
    #temp = root
    while True:
        #最大子树索引先赋给左子树        
        max_child = root * 2 +1                             
        if max_child > end:
            break
        #右子树的关键字大于左子树
        if max_child+1 <= end and data[max_child] < data[max_child+1]:  
            #最大子树索引赋给右子树
            max_child += 1
        #最大子树的关键字大于根节点                                             
        if data[root] < data[max_child]:                                        
            #交换这两个数
            data[root], data[max_child] = data[max_child], data[root]   
            #修改根节点的索引
            root = max_child                                            
        else:
            break
 
def heap_sort(data):
    n = len(data)
    #创建大根堆
    for root in range(n//2,-1,-1):
        sift(data,root,n-1)
    #堆排序，堆顶元素和堆末尾的元素交换，然后把剩下的元素调整为一个大根堆
    for end in range(n-1, -1, -1):
        data[0], data[end] = data[end], data[0]
        sift(data,0,end-1)
 
 
 
if __name__ == "__main__":
    li = [35, 1, 9, 32, 24, 18, 27, 41]
    heap_sort(li)
    print(li)