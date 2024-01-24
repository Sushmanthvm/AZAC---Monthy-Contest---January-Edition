# Problem link
[https://www.hackerrank.com/contests/january-monthly/challenges/msd-2](url)

# Approach

1. Straightforward, sum the ascii values of each character and check if divisible by 7.
2. Time complexity: O(n) where n is the length of the string.

## Code snippet
```
def solution(s):
    # Write your code here
    sum =0
    for i in s:
        sum = sum + ord(i)
    
    if sum%7 == 0:
        return "THALA FOR A REASON"
    else:
        return "IAM SAD"

```