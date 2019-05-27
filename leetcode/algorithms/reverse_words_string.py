class Solution:
    def reverseWords(self, s: str) -> str:
        words_vec = s.split()
        words_vec = words_vec[::-1]


        return " ".join(words_vec)
