from LML import LML
from maps import vadi_anuanuvadi,vadi_anuvadi,vadi_samvadi
class Raga:
    """Raga object. Attribute of this object are the components that from the Raga
        self.vadi : None #most important swar of the raga
        self.numSwaras : 0 #number of swars used in this raga
        self.varjyaAaroha : [] #excluded from aaroha
        self.varjyaAvaroha : [] #swars excluded from avaroha
        self.psamvadi : None #Second most important swar
        self.ssamvadi : None #Third most important swar
        self.anuvadi : [] #Pair of supporting swars. 
        self.anuanuvadi :  [] #Pair of other supporting swars
        self.aaroha : []
        self.avaroha : []
    
    """
    def __init__(self, vadi, mode = "auto", varjyaAaroha = [], varjyaAvaroha = [] ):
        self.representationArray = []
        self.vadi = vadi #most important swar of the raga
        self.mode  = mode #auto generate or ask user.
        self.varjyaAaroha = varjyaAaroha #excluded from aaroha
        self.varjyaAvaroha = varjyaAvaroha #swars excluded from avaroha
        self.psamvadi = None #Second most important swar
        self.ssamvadi = None #Third most important swar
        self.anuvadi = [] #Pair of supporting swars. 
        self.anuanuvadi = [] #Pair of other supporting swars
        self.aaroha = []
        self.avaroha = []
        self.graha = []
        self.nyasa = []
        self.sama = []
        self.amsa = []
        self.swars = []
        self.emotive = []
        # [self.swars.extend(l) for l in (list(self.vadi), list(self.psamvadi), list(self.ssamvadi), self.anuanuvadi, self.anuvadi)]
        # self.numSwars = numSwars
        if mode == "auto":
            self.__set_samvadi__()
            self.__set_anuvadi__()
            self.__set_anuanuvadi__()
            [self.swars.extend(l) for l in ([self.vadi], [self.psamvadi], [self.ssamvadi], self.anuanuvadi, self.anuvadi)]
            self.__set_aaroha__()
            self.__set_avaroha__()
            self._display()
            self._set_imp_swaras()
    
        else:
            print("choose samvadi, anuvadi and anuanuvadi pair for your composition.")
            print("the first element of the arry is primary and second is secondary and third(if any) is optionally accepted swar.")
            self._custom_samvadi()
            self._custom_anuvadi()
            self._custom_anuanuvadi()
            if self.ssamvadi == " ": 
                [self.swars.extend(l) for l in ([self.vadi], [self.psamvadi], self.anuanuvadi, self.anuvadi)]
            else:
                [self.swars.extend(l) for l in ([self.vadi], [self.psamvadi], [self.ssamvadi], self.anuanuvadi, self.anuvadi)]
            self.__set_aaroha__()
            self.__set_avaroha__()
            self._display()
            self._get_imp_swaras()

        

    def set_vadi(self,vadi):
        """A function to set vadi swar of the raga.
                vadi: there can be only one vadi swar hence its a string containing a single element.the name of the vadi swar. 
            Nishad and Komal Nishad cannot be vadi swaras of the raag because of their harmonal weakness.
        """
        self.vadi = vadi
    
    def set_varjya(self, varjyaAaroha, varjyaAvaroha):
        """A function to set varjya swaras of the raag. 
                varjyaAaroha: A list of swars varjya from aaroha.
                varjyaAvaroha: A list of swars varjya from avaroha.
        """
        self.varjyaAaroha = varjyaAaroha
        self.varjyaAvaroha = varjyaAvaroha

    def __set_aaroha__(self):
        """The function must generate aaroha and avaroha using varjya aaroha and swars"""
        self.aaroha = list(set(self.swars) - set(self.varjyaAaroha))
        # print(self.aaroha)
        if None in self.aaroha:
            self.aaroha.remove(None)
        lml =LML()
        index_map = {element: index for index, element in enumerate(lml.LMLarray)} 
        # print(index_map)
        self.aaroha = sorted(self.aaroha, key=lambda x: index_map[x])
        ##Sort them according to sequence, Maybe we need to use the swar_map for frequencies.
    
    def __set_avaroha__(self):
        """The function must generate aaroha and avaroha using varjya aaroha and swars"""
        self.avaroha = list(set(self.swars) - set(self.varjyaAvaroha))
        if None in self.avaroha:
            self.avaroha.remove(None)
        lml = LML()
        index_map = {element: index for index, element in enumerate(lml.LMLarray)} 
        self.avaroha = sorted(self.avaroha, key=lambda x: index_map[x])
        self.avaroha.reverse()




        ##Sort decsending using swar map.
                           
    def __set_samvadi__(self):
        #complete later     
        lml = LML()
        p_related = lml.spa(s1=self.vadi)
        m_related = lml.sma(s1=self.vadi)
        # if p_related in self.varjyaAaroha or p_related in self.varjyaAvaroha:
        #     self.psamvadi = m_related
        #     self.ssamvadi = None
        # elif m_related in self.varjyaAaroha or m_related in self.varjyaAvaroha:
        #     self.psamvadi = p_related
        #     self.ssamvadi = None
        # else:
        if lml.LNS(s1=p_related) and not lml.LNS(s1=m_related):
            self.psamvadi = p_related
            self.ssamvadi = m_related
        elif not lml.LNS(s1=p_related) and lml.LNS(s1=m_related):
            self.ssamvadi = p_related
            self.psamvadi = m_related
        else:
            self.ssamvadi = m_related
            self.psamvadi = p_related
        if p_related in self.varjyaAaroha and p_related in self.varjyaAvaroha:
            self.psamvadi = self.ssamvadi
            self.ssamvadi = None
        # print(self.psamvadi, self.ssamvadi)
    
    def __set_anuvadi__(self):
        lml = LML()
        kg_related1, kg_related2 = lml.skga(self.vadi)
        g_related1, g_related2 = lml.sga(self.vadi)
        temp_anuvadi = [kg_related1,kg_related2,g_related1,g_related2]
        for i in temp_anuvadi:
            if lml.LNS(i):
                self.anuvadi.append(i)
                break
            i = None
        if i == kg_related1:
            self.anuvadi.append(lml.LHS(kg_related2, g_related2))
        elif i == g_related1:
            self.anuvadi.append(lml.LHS(kg_related2, g_related2))
        elif i == kg_related2:
            self.anuvadi.append(lml.LHS(kg_related1, g_related1))
        elif i == g_related2:
            self.anuvadi.append(lml.LHS(kg_related1, g_related1))
        elif i == None:
            s1 = lml.LHS(kg_related1,g_related1)
            s2 = lml.LHS(kg_related2,g_related2)
            s3 = lml.LHS(s1,s2)
            panuvadi = s3
            sanuvadi = s2 if s1==s3 else s1
            self.anuvadi = [panuvadi,sanuvadi]

    def __set_anuanuvadi__(self):
        lml = LML()
        kg_related1, kg_related2 = lml.skre(self.vadi)
        g_related1, g_related2 = lml.sre(self.vadi)
        temp_anuanuvadi = [kg_related1,kg_related2,g_related1,g_related2]
        for i in temp_anuanuvadi:
            if lml.LNS(i):
                self.anuanuvadi.append(i)
                break
            i = None
        if i == kg_related1:
            self.anuanuvadi.append(lml.LHS(kg_related2, g_related2))
        elif i == g_related1:
            self.anuanuvadi.append(lml.LHS(kg_related2, g_related2))
        elif i == kg_related2:
            self.anuanuvadi.append(lml.LHS(kg_related1, g_related1))
        elif i == g_related2:
            self.anuanuvadi.append(lml.LHS(kg_related1, g_related1))
        elif i == None:
            s1 = lml.LHS(kg_related1,g_related1)
            s2 = lml.LHS(kg_related2,g_related2)
            s3 = lml.LHS(s1,s2)
            panuanuvadi = s3
            sanuanuvadi = s2 if s1==s3 else s1
            self.anuanuvadi = [panuanuvadi,sanuanuvadi]
           
    def _display(self):
        print("Your raag structure:")
        print("Vadi: "+self.vadi)
        print("Psamvadi: "+self.psamvadi)
        print("Ssamvadi: "+ self.ssamvadi if self.ssamvadi!= None else "Ssamvadi = -")
        print("Anuvadi: ", self.anuvadi)
        print("Anuanuvadi", self.anuanuvadi)
        print("Aaroha: " ,self.aaroha)
        print("Avaroha: ", self.avaroha)
    
##those selected in init function are first choice for the vadi and samvadi.
##create a table with other choices and 
##we will need a set of dictionaries/lists and a set of functions of format _custom_samvadi(self,mode):
#the function will print possible combinations for samvadi/anuvadi/vadi swars and input the choice.
#source the list from table
    
    def _custom_samvadi(self):
        print("Select samvadi swars from below:")
        for i,j in enumerate(vadi_samvadi[self.vadi]):
            print(i+1,".", j)
        num = int(input("Enter your choice:" ))
        self.psamvadi = vadi_samvadi[self.vadi][num-1][0]
        self.ssamvadi = vadi_samvadi[self.vadi][num-1][1]

    def _custom_anuvadi(self):
        print("Select anuvadi swars from below:")
        for i,j in enumerate(vadi_anuvadi[self.vadi]):
            print(i+1,".", j)
        num = int(input("Enter your choice:" ))
        self.anuvadi=[vadi_anuvadi[self.vadi][num-1][0],vadi_anuvadi[self.vadi][num-1][1]]

    def _custom_anuanuvadi(self):
        print("Select anuanuvadi swars from below:")
        for i,j in enumerate(vadi_anuanuvadi[self.vadi]):
            print(i+1,".", j)
        num = int(input("Enter your choice:" ))
        self.anuanuvadi=[vadi_anuanuvadi[self.vadi][num-1][0],vadi_anuanuvadi[self.vadi][num-1][1]]
        
    def _get_imp_swaras(self):
        """Function to input graha, sama, nyasa and amsha swaras"""
        print("Enter a string of graha swaras seperated by " "." )
        self.graha = input().split(" ")
        print("Enter a string of nyasa swaras seperated by " "." )
        self.nyasa = input().split(" ")
        print("Enter a string of sama swaras seperated by " "." )
        self.sama = input().split(" ")
        print("Enter a string of amsa swaras seperated by " "." )
        self.amsa = input().split(" ")
        Emotive = ["kre","kdha","kni","kga","mat"]
        for i in Emotive:
            if i in self.swars:
                self.emotive.append(i)


    def _set_imp_swaras(self):
        """Auto set hardcoded values for sama, amsa, graha, nysa swars."""
        graha = ["sa", "ma", "pa","kni","ni","ga","kga",self.vadi, self.psamvadi,self.ssamvadi]
        for i in graha:
            if i in self.swars and i not in self.graha and i!=None:
                self.graha.append(i)
        nyasa = [self.vadi, self.ssamvadi, self.psamvadi,self.anuvadi[0],"sa","ma","pa"]
        for i in nyasa:
            if i in self.swars and i not in self.nyasa and i!=None:
                self.nyasa.append(i)
        sama = ["sa","ga","ma","pa", self.vadi, self.psamvadi]
        for i in sama:
            if i in self.swars:
                self.sama.append(i)
        amsa = ["sa","ma","pa",self.vadi, self.psamvadi]
        for i in amsa:
            if i in self.swars:
                self.amsa.append(i)
        Emotive = ["kre","kdha","kni","kga","mat"]
        for i in Emotive:
            if i in self.swars:
                self.emotive.append(i)
        
        
    


            