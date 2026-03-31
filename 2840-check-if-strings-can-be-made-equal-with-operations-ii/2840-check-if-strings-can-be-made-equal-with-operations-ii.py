class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # simply keep track of a dictionary that keeps track the unique number of character in 
        # the even position or in the odd position 

        even_dict_1 = {}
        odd_dict_1 = {}

        even_dict_2 = {}
        odd_dict_2 =  {}

        #do an even loop : 
        for i in range(0, len(s1), 2):
            
            #store the character's occurance
            even_dict_1[s1[i]] = even_dict_1.get(s1[i], 0) + 1
            
            even_dict_2[s2[i]] = even_dict_2.get(s2[i], 0) + 1

        #loop through all keys in
        if len(even_dict_1) != len(even_dict_2) : 
            return False

        for key in even_dict_1 : 

            if key not in even_dict_2 or even_dict_2[key] != even_dict_1[key]: 
                return False

        #repeat for odd iteration
        for i in range(1, len(s1), 2) : 

            #store the character's occurance for odd case
            odd_dict_1[s1[i]] = odd_dict_1.get(s1[i], 0) + 1
            odd_dict_2[s2[i]] = odd_dict_2.get(s2[i], 0) + 1
        
        if len(odd_dict_1) != len(odd_dict_2) : 
            return False
        
        #check that each unique character is identital 
        for key in odd_dict_1 : 
            if key not in odd_dict_2 or odd_dict_2[key] != odd_dict_1[key] : 
                return False
        

        #finally return True
        return True 