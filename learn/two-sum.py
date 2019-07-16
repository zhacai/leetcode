list = [1,2,3,3,5,6,4,4,6,2,7,1,5,5]

def two_sum(list, sum):
    map = {}
    all_result = []
    for i in range(len(list)):
        if list[i] not in map:
           map[sum - list[i]] = i 
        else:
            all_result.append([map[list[i]]+1, i+1])
            #return map[list[i]], i
    return all_result

print(two_sum(list, 8))