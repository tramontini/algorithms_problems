class Solution:
    def reverseWords(self, s: str) -> str:
        words_vec = s.split()

        return " ".join(words_vec[::-1])
