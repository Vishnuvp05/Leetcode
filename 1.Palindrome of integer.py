class solution:
    def is_palindrome(self,x:int)->bool:
        a=str(x)
        reverse=a[::-1]
        if reverse==a:
            return True 
        else:
            return False
        
