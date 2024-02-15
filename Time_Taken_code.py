ct = 4

import numpy as np
arr = np.array([1, 2, 4, 5])
flag = -1
se = int(input("Enter a number to find : "))
for i in range(0, len(arr)):
    if(arr[i]==se):
        print(f'Element {se} found at  index {i}')
        flag = 1
        ct = ct + 5
        break
    else:
        ct = ct + 2
        pass
if flag == -1:
    print("Element not found")
    ct = ct + 2
ct = ct + 1    

print(f"\nNumber of comparisons made are {ct}")

best_case = 10
average_case = (arr[0]+arr[1]+arr[2]+arr[3])/len(arr)
worst_case = 16
print(f"\nBest case time complexity is O({best_case})")
print(f"Average case time complexity is O({average_case})")
print(f"Worst case time complexity is O({worst_case})")


