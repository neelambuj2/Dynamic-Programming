def verifyString(s):
    if len(s) == 0:
        return False
    if s[0] == '0':
        return False
    if int(s) <= 26 and int(s) >= 1:
        return True
    else:
        return False




def doit(s, pointer, cache):
    if pointer == len(str(s)):
        return 1

    if cache[pointer] != -float('inf'):
        return cache[pointer]

    totalWays = 0

    if pointer < len(str(s)):
        oneLengthString = s[pointer]
        if verifyString(oneLengthString):
            totalWays += doit(s, pointer + 1, cache)

    if pointer + 1 < len(s):
        twoLengthString = s[pointer:pointer + 2]
        if verifyString(twoLengthString):
            totalWays += doit(s, pointer + 2, cache)
    cache[pointer] = totalWays

    return cache[pointer]


s = input()
cache = [-float('inf') for _ in range(len(s) + 1)]
print(doit(s, 0, cache))