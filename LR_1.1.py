arr = []
target = int(input())
s = 'None'
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            s = "{}, {}".format(arr[i], arr[j])
            break
print(s)