class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str =  "".join(char for char in s if char.isalnum())
        reversed_str = cleaned_str[::-1]
        if cleaned_str.lower() == reversed_str.lower():
            return True
        else: 
            return False