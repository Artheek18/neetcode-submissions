class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.replace(" ","")
        string_remove= [char for char in string if char.isalnum()]
        i = 0
        j = len(string_remove)-1

        while i <= j:
            if string_remove[i].lower() != string_remove[j].lower():
                return False
            else:
                i +=1
                j -=1

        return True