
def longest_palindrome(s: str):
    length = len(s)
    start = 0
    max_length = 1
    for i in range(1, length):
        low = i-1
        high = i
        while low >= 0 and high < length and s[low] == s[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low = low - 1
            high = high + 1

        low = i-1
        high = i+1
        while low >=0 and high < length and s[low] == s[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low = low-1
            high = high+1

    print(s[start:start+max_length])



s = input()
longest_palindrome(s)


