class Student():
    def __init__(self,nom, prenom, numero_etudiant,numero_credits=0):
        self.__nom=nom
        self.__prenom=prenom
        self.__numero_etudiant=numero_etudiant
        self.__numero_credits=numero_credits
        self.__level=self.__student_eval()

    def add_credits(self,credits):
        if int(credits)>0:
            self.__numero_credits+=credits
        else:
            print(f"impossible d'ajouter {credits}")
        return self.__numero_credits
    def student_info(self):
        print(f"nom: {self.__nom}. \nprenom: {self.__prenom}. \nnumero etudiant: {self.__numero_etudiant}. \nniveau: {self.__level}")

    def __student_eval(self):
        if self.__numero_credits>=90:
            return "Excellent"
        elif self.__numero_credits>=80:
            return "Trés bien"
        elif self.__numero_credits>=70:
            return "Bien"
        elif self.__numero_credits>=60:
            return "passable"
        elif self.__numero_credits<=60:
            return "passable"
    

student1=Student("laurent","fleur",145,50)
student1.add_credits(3)
student1.add_credits(24)
student1.add_credits(3)

student1.student_info()
