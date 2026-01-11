class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = set("aeiou")
        words = s.split()

        def count_vowels(word):
            return sum(c in vowels for c in word)

        target = count_vowels(words[0])

        for i in range(1, len(words)):
            if count_vowels(words[i]) == target:
                words[i] = words[i][::-1]

        return " ".join(words)