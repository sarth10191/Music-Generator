#Laws of music logic are coded here. Using these laws one can decide samvadi anuvadi anuanuvadi swars of raag. 
#This is totally a helper class

class LML:
    def __init__(self):
        self.LHSarray = ["sa", "pa", "ma", "ga", "re", "kga", "kre", "dha", "kdha", "ni", "kni", "mat" ]
        self.LMLarray = ["sa", "kre", "re", "kga", "ga", "ma", "mat", "pa", "kdha", "dha", "kni", "ni" ]

    
    def LHS(self, s1, s2):
        """Law of harmonic strengths."""
        if(self.LHSarray.index(s1)<self.LHSarray.index(s2)):
            return s1
        else:
            return s2
    
    def LNS(self, s1)->bool:
        """Law of nitya swaras. Returns if the swar is nitya swar or not."""
        if s1 in ["sa","ma","pa"]:
            # print(s1,"is Nitya")
            return True
        return False

    def CoEx(self, s1)->str:
        """Lae of coexistance of swars.Takes in Vadi Swar and returns CoExistant Swar."""
        index = self.LMLarray.index(s1)
        index = (index+7)%12 -1
        return self.LMLarray[index]
    
    def sw(self, s1):
        """Swa-Bhava"""
        return s1

    def ss(self, s1):
        return s1+"'"

    def spa(self, s1):
        """Sa-Pa bhava."""
        index = self.LMLarray.index(s1)
        index = (index+7)%12 
        # print(index)
        return self.LMLarray[index]

    def sma(self, s1):
        """Sa-Ma bhava."""
        index = self.LMLarray.index(s1)
        index = (index+5)%12 
        # print(index)
        return self.LMLarray[index]
        

    def sga(self, s1):
        """Sa-Ga bhava."""
        index = self.LMLarray.index(s1)
        index1 = (index+4)%12
        index2 = (index-4)%12 
        return self.LMLarray[index1], self.LMLarray[index2]

    def sre(self, s1):
        """Sa-Re bhava."""
        index = self.LMLarray.index(s1)
        index1 = (index+2)%12
        index2 = (index-2)%12 
        return self.LMLarray[index1], self.LMLarray[index2]

    def skga(self, s1):
        """Sa-Komal ga bhava."""
        index = self.LMLarray.index(s1)
        index1 = (index+3)%12
        index2 = (index-3)%12 
        return self.LMLarray[index1], self.LMLarray[index2]

    def skre(self, s1):
        """Sa-Komal re bhava."""
        index = self.LMLarray.index(s1)
        index1 = (index+1)%12
        index2 = (index-1)%12 
        return self.LMLarray[index1], self.LMLarray[index2]
    
    # def sdha(self, s1):
    #     """Sa-Dha bhava."""
    #     pass

    # def skdha(self, s1):
    #     """Sa-Komal Dha bhava."""
    #     pass

    # def sni(self, s1):
    #     """Sa-Ni bhava."""
    #     pass

    # def skni(self, s1):
    #     """Sa-Komal Ni bhava."""
    #     pass

    # def smat(self, s1):
    #     """Sa-Tivra MA bhava."""
    #     pass
    