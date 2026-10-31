class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        count = 0
        s = s.strip()
        for i in range (len(s)):
            if s[i] == ' ':
                break

            count += 1
            
        return count