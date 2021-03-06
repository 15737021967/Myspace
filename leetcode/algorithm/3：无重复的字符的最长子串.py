class Solution:
    """
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        right, left = 0, 0
        s_length = len(s)
        s_map = {}
        result = 0
        while right < s_length:
            flag = s_map.get(s[right])
            if flag is not None and flag >= left:
                left = flag + 1

            s_map[s[right]] = right
            right += 1

            result = max(right - left, result)

        return result


print(Solution().lengthOfLongestSubstring("aabcabcbbadcfd"))
