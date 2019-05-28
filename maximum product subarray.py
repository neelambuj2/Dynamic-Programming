
def maximum_product(array):
    prev_max = array[0]
    prev_min = array[0]
    ans = array[0]

    for i in range(1, len(array)):
        current_max = max(prev_max*array[i], prev_min*array[i], array[i])
        current_min = min(prev_max * array[i], prev_min* array[i], array[i])
        ans = max(ans, current_max)
        prev_max = current_max
        prev_min = current_min

    return ans



array = [2,3,-2,4]
print(maximum_product(array))