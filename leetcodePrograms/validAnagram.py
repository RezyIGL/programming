class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {let: 0 for let in s}
        lenS = len(dictS.keys())
        dictT = {let: 0 for let in t}
        lenT = len(dictT.keys())

        for letter in s:
            dictS[letter] += 1
        
        for letter in t:
            dictT[letter] += 1

        if lenS == lenT:
            for keyS, valueS in dictS.items():
                try:
                    if dictT[keyS] != valueS:
                        return False
                except:
                    return False
            return True
        
        return False