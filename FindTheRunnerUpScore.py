#Find the Runner-Up Score! 
n = int(input())
arr = list(map(int, input().split()))
largest = max(arr)
arr.remove(largest)
while max(arr) == largest:
    arr.remove(largest)
run = max(arr)
print(run)

