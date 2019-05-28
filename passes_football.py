# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @param C : list of integers
#     # @return an integer
#     def solve(self, A, B, C):
#         last = B
#         pointer = B
#         for player in C:
#             if player != 0:
#                 last = pointer
#                 pointer = player
#             elif player == 0:
#                 temp = pointer
#                 pointer = last
#                 last = temp
#
#         return pointer
# print(Solution().solve(10,23,[86,63,60,0,47,0,99,9,0,0]))
seq = [{'data': 'a','rank':3}, {'data':'b','rank': 1},{'data':'n','rank': 2}, {'data':'c','rank': 1}]

n=sorted(seq,key=lambda x:x['rank'],reverse=True)
new = list(map(lambda x:x['rank'],n))
print(n)
print(new)