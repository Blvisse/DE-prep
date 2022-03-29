class Solution:
    def romanToInt(self, s: str) -> int:
        #first we check the lenght of the string
        #we create a dictionary containing roman conversions
        number=0
        stringlen=len(s)
        
        roman_conv={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += roman_conv[char]
        return number
        
        
        
#         if stringlen ==1:
#             number=roman_conv.get(s,'Incorrect Value')
#             return number
        
#         elif stringlen==2:
#             if s[0]==s[1]:
#                 number=roman_conv.get(s,'Incorrect Value')*2
#                 return number
#             else:
#                 last_number=roman_conv.get(s[1],'Incorrect Value')
#                 prior_number=roman_conv.get(s[0],'Incorrect Value')
                
#                 return last_number-prior_number
                
                

#         if stringlen ==1:
#             if s=='I':
#                 number=0
#                 return number
#             elif s=='V':
                 
#                 number=5
                
#                 return number
#             elif s=='X':
#                 number=10
#             elif s=='L':
                
#                 number=50
#                 return number
#             elif s=='C':
                
#                 number = 100
#                 return number 
#             elif s=='D':
                
#                 number =500
#                 return number
#             elif s=='M':
                
#                 number=1000
#                 return number
#             else:
#                 print('Invalid choice')
#                 return False
            
                
            
        