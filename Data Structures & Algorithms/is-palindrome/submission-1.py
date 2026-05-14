class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        
        len_new_str = len(new_str)
        for i in range(len_new_str - 1):
            if new_str[i] != new_str[len_new_str - 1 - i]:
                return False
        return True