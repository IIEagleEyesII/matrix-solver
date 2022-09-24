class equation:
    def __init__(self, row):
        self.row = row
        self.size = len(row)-1

    def __str__(self):
        """Imprime l'equation sous la forme a.x + b.y + ... = z"""
        x = ""
        for idx in range(len(self.row)):
            if idx == len(self.row) - 1:
                x += f" = { self.row[idx]}"
            else:
                if self.row[idx] < 0:
                    x += f" {self.row[idx]}*{chr(idx + ord('a'))}"
                elif idx == 0:
                    x += f" {self.row[idx]}*{chr(idx + ord('a'))}"
                else:
                    x += f" +{self.row[idx]}*{chr(idx + ord('a'))}"
        return x

    def GetEquation(self):
        return self.row

    def SetTerms(self, idx, val):
        """Mets à jour une equation si un des inconnus à été trouvé"""
        rate = self.row.pop(idx)
        self.row[-1]-=rate*val

    def CheckSolution(self):
        """Verifie si une equation ne contient qu'un seul inconnu, si c'est le cas renvoie l'indice du terme et sa valeur
        ex : si on a [0,0,5,3] -> return : (2 , 3/5)
        """
        if self.row[:-1].count(0) == self.size -1:
            for term in self.row :
                if term !=0 :
                   # print("check == " , (self.row[:-1].index(term), self.row[-1] / term))
                    return (self.row[:-1].index(term), self.row[-1]/term)

"""
equa = [1,1,4,5,0]
equa  = equation(equa)
print(equa)
equa.SetTerms(2,2)
print(equa)
print(equa.size)
print("*"*100)
"""

class Matrix:
    def __init__(self ,matrice):
        self.matrice = [equation(equa) for equa in matrice]
        self.size = self.matrice[0].size
       # self.sizeM = len(self.matrice)
        print("matrice : ",matrice)
        self.dict = self.dico()
        self.__str__()
        self.DicoTerms = {}
        for i in range(self.size):
            self.DicoTerms.setdefault(i,None)
        print("terms : " ,self.DicoTerms)
        print(" \nEnd of initialisation \n")
        #self.matriceTemporaire = [[0 for i in range(len(matrice[0]))]for j in range(len(matrice))]

    def __str__(self):
        print( "\nsystem :","\n--")
        for i in self.dict:
            print(self.dict[i])
        print("--")
        return ""

    def show(self):
        for i in range(self.size):
            print(self.matrice[i])

    def dico(self):
        dico = {}
        for row in self.matrice:
            if row.GetEquation()[:-1].count(0) < row.size:
                dico.setdefault(self.matrice.index(row), str(row))
        return dico

    def solve(self):
        """1 2 1   1 2 1   a 0 x
           2 3 4   0 x y   0 b y
           3 4 5   0 d f   0 0 c """
        mybool1= True
        iter = 0
        while mybool1 and iter < self.size :
            row = 0
            mybool2 = True
            while row < self.size and mybool2 :
                #print("row",row,"iter",iter,"len",self.matrice[row-1].size,sep=" ")
                if self.matrice[iter].GetEquation()[iter] != 0 and iter != row:
                    rate = self.matrice[row].GetEquation()[iter] / self.matrice[iter].GetEquation()[iter]
                    col = 0
                    for col in range(self.size + 1):
                        #à changer en une boucle while
                        self.matrice[row].GetEquation()[col] = rate * self.matrice[iter].GetEquation()[col] - \
                                                               self.matrice[row].GetEquation()[col]
                row += 1
                check = self.matrice[iter].CheckSolution()
                if check != None :
                    mybool2 = False

                    self.matrice[iter].SetTerms(check[0],check[1])
                    self.DicoTerms[check[0]]=check[1]
                    #self.redefine(check)

            iter+=1
        print(self.DicoTerms)
        self.show()

    def redefine(self,*terms):
        for equa in self.matriceTemporaire :
            for term in terms :
                equa.SetTerms(term[0],term[1])
            self.size = equa.size



"""
matrice = [[1,1,1,6],[1,-1,-1,-4],[1,1,-1,0]]
m = Matrix(matrice)
m.solve()
print(m)

print("*"*100 , "\n")
"""
"""
matrice = [[1, 1, 1, 6], [1, -1, -1, -4], [1, 1, -1, 0]]
m = Matrix(matrice)

print("test", "\n")
m.solve()


print("*"*100 , "\n")
"""
mtr = [[1,1,1,7],[1,1,-1,3],[-1,1,-1,-5]]
mtr = Matrix(mtr)
mtr.solve()



