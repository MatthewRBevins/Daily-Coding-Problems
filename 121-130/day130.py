k = 2
stocksArr = [5,2,4,0,1]
def findBestPrice(arr, index, profit, buys, sells):
    if index == len(arr):
        return profit
    if buys == sells:
        return max(findBestPrice(arr, index+1, profit, buys, sells), findBestPrice(arr, index+1, profit-arr[index], buys-1, sells))
    else:
        return max(findBestPrice(arr, index+1, profit, buys, sells), findBestPrice(arr, index+1, profit+arr[index], buys, sells-1))
print(findBestPrice(stocksArr, 0, 0, k, k))