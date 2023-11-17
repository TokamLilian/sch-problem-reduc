import Cour

class Etudiant:
    def __init__(self, userName, matricule, cours):
        """
        Creait une instance d'un etudiant
        """
        self.__userName   = userName    #Nom de l'etudiant
        self.__matricule  = matricule
        self.__cours        = cours    #liste des cours


    def add_cours(self, c):
        """
        Ajoute un cours parmi les cours aux quels l'etudiant est inscrit
        """

        if not isinstance(c,Cour):
            raise TypeError("L'argument doit être de type 'Cour'.")
        
        else :
            self.cours.append(c)


    def get_nom(self):
        return self.__userName


    def get_matricule(self):
        return self.__matricule


    def get_cours(self):
        return self.__cours