class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right: # makes sure you're working within the bounds of the leftmost/rightmost
            while left < right and not s[left].isalnum(): # starts from the left assuring char is alphanumeric
                left += 1# move forward if it is not an alnum
            while right > left and not s[right].isalnum(): 
                right -= 1# move backward if it is not an alnum
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True



