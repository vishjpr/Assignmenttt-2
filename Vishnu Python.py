def sum_avg_list(lst, n):
    if n == 0:
        return (0, 0)
    else:
        sum, avg = sum_avg_list(lst, n-1)
        return (sum + lst[n-1], avg + 1)
 
def avg_list(lst):
    sum, avg = sum_avg_list(lst, len(lst))
    return sum/avg
 
lst = [4, 5, 1, 2, 9, 7, 10, 8]
print("Sum of the list: ", sum_avg_list(lst, len(lst))[0])
print("Average of the list: ", avg_list(lst))
