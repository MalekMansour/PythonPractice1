'''
The function first sorts the array in ascending order. 
Then, it calculates the total sum of all elements.
'''

def miniMaxSum(arr):
    arr.sort()
    total_sum = sum(arr)
    min_sum = total_sum - arr[-1]
    max_sum = total_sum - arr[0]
    print(min_sum, max_sum)

if __name__ == '__main__':
   
    arr = [1, 3, 5, 7, 9]
    miniMaxSum(arr)
