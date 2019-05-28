def verify_string(s):
    if len(s) == 0:
        return False
    if s[0] == '0':
        return False
    if int(s)<=26 and int(s) >=0:
        return True
    else:
        return False

def decode_ways(s, pointer, cache):
    if pointer == len(s):
        return 1
    if cache[pointer] is not None:
        return cache[pointer]
    total_ways = 0

    if pointer < len(s):
        one_len_string = s[pointer]
        if verify_string(one_len_string):
            total_ways=total_ways+decode_ways(s,pointer+1,cache)
    if pointer + 1< len(s):
        two_len_string = s[pointer:pointer+2]
        if verify_string(two_len_string):
            total_ways = total_ways + decode_ways(s, pointer+2, cache)
    cache[pointer] = total_ways

    return total_ways



def numDecodings(s: str) -> int: # faster
    dp = [1]+[0]*len(s)
    for i in range(1,len(dp)):
        if s[i-1]!='0':
            dp[i] = dp[i-1]
        if i>=2 and '09' < s[i-2:i] < '27':
            dp[i] += dp[i-2]

    return dp[-1]



s = input()
pointer = 0
cache = [None for i in s]
print(numDecodings(s))