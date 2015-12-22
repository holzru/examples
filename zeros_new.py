import math
def zeros(n):
    total = 0
    count = 1
    while 5**count < n:
        result = n/(5**count)
        total += math.floor(result)
        count += 1
    print int(total)
    #divide n by increasing factors of 5 while adding truncated results to total


zeros(23)
