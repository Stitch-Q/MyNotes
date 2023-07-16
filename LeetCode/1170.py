"""
定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。
例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。
现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。
请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。

示例 1：
输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
"""


class Solution:
    def numSmallerByFrequency(self, queries, words):
        res = []

        def f(x: str):
            y = list(x)
            z = set(y)
            z = sorted(z)
            return y.count(z[0])

        for i in range(len(queries)):
            queries[i] = f(queries[i])

        for i in range(len(words)):
            words[i] = f(words[i])

        words.sort()
        for i in range(len(queries)):
            left, right = 0, len(words) - 1
            if queries[i] >= words[-1]:
                res.append(0)
                continue
            while left < right:
                mid = (left + right) // 2
                if words[mid] <= queries[i]:
                    left = mid + 1
                else:
                    right = mid
            res.append(len(words) - left)
        return res


if __name__ == "__main__":
    a = Solution()
    quer = ["cbd"]
    word = ["zaaaz"]
    result = a.numSmallerByFrequency(quer, word)
    print(result)
