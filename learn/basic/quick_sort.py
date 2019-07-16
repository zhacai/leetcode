arr = [1,3,4,5,2,3,2,67,75,7,2,4,3,67,58,18,38,68,66,88]

# 分而治之，但用了额外的空间及递归，性能低
def quick_sort_cur_fake(arr):
    if len(arr) < 2:
        return arr
    else:
        q = arr[0]
        left = [i for i in arr if i<q]
        right = [i for i in arr if i>q]
        return  quick_sort(left) + [q] + quick_sort(right)

print quick_sort_cur_fake(arr)

def quick_sort_cur(arr):
    # 分区