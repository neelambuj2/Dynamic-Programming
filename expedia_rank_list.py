from copy import deepcopy
class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        good_word_list = A.split('_')
        rank_list = list()
        template = {'index': None, 'rank': None}
        for index in range(len(B)):
            rank = 0
            for word in good_word_list:
                temp_list = B[index].split('_')
                if word in temp_list:
                    rank = rank + 1
            template['rank'] = rank
            template['index'] = index
            rank_list.append(deepcopy(template))

        sorted_rank_list = sorted(rank_list, key=lambda x: x['rank'], reverse=True)
        index_list = list(map(lambda x: x['index'], sorted_rank_list))
        print(sorted_rank_list)
        return index_list
print(Solution().solve('cool_ice_wifi', ['water_is_cool',
                                         'cold_ice_drink',
                                         'cool_wifi_speed']))