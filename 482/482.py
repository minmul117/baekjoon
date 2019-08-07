class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        from collections import OrderedDict
        removed_dash_str = ''.join(OrderedDict.fromkeys(S))
        removed_dash_str = removed_dash_str.replace('-', '')
        
        if removed_dash_str == '':
            return ''

        if len(S) < K:
            return S.upper()

        removed_dash_str = S.replace('-', '').upper()
        if (len(removed_dash_str) / K) != int(len(removed_dash_str) / K):
            # 이 경우는, 균일하게 K개로 나눌 수 없는 구간이다.
            # 4 / 2
            # 4 / 3
            # 15 / 4 = 3. xx, 3 - 4 - 4 - 4
            import math
            first_group_counts = len(removed_dash_str) - K * int(math.floor(len(removed_dash_str) / K))
            first_str = removed_dash_str[0:first_group_counts]
            removed_dash_str = removed_dash_str[first_group_counts:len(removed_dash_str)]
            results = '-'.join([removed_dash_str[i:i+K].upper() for i in range(0, len(removed_dash_str), K)])
            results = first_str + '-' + results
        else:
            results = '-'.join([removed_dash_str[i:i+K].upper() for i in range(0, len(removed_dash_str), K)])
        return results

s = Solution()
print(s.licenseKeyFormatting('5F3Z-2e-9-w', 3))
print(s.licenseKeyFormatting('2-5g-3-J', 2))