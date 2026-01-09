class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        length=0
        for ch in s[::-1]:
            if ch==' ':
                break
            length += 1
        return length
