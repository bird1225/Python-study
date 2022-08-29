# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/8/29

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        word_len = len(words)
        z =[]
        for i in range(word_len):
            print(sorted(words[i]))
        # return [w for i, w in enumerate(words) if i == 0 or sorted(words[i - 1]) != sorted(words[i])]


if __name__ == "__main__":
    s = Solution()
    print(s.removeAnagrams(words=["abba", "baba", "bbaa", "cd", "cd"]))
