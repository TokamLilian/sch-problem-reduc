class Cour:

    def __init__(self, nom, hours):
        """
        Creait une instance d'un cour.\\
        ``nom``           = ""         Nom du cours \\
        ``hours``         = 0          Nombre d'heures requis \\
        ``adjacences``    = []         Liste d'adjacences des cours
        """
        
        self.nom           = nom         #Nom du cours
        self.hours         = hours       #Nombre d'heures requis
        self.adjacences    = []          #list d'adjacences des cours


    def add_adjacence(self, c):
        """Ajoute un adjacence au cour"""
        if not isinstance(c,Cour):
            raise TypeError("L'argument doit être de type 'Cour'.")
        
        else:
            self.adjacences.append(c)


    def not_adjacent(self, cours):
        """
        Retourne vrai si le cours passé en commentaire n'est pas adjacent au cours courrant
        :params: ``cours`` de type Cour
        :returns: Si les deux cours sont adjacents
        """
        if cours not in self.adjacences:
            return True


    def get_nom(self):
        return self.nom
    

    def get_hours(self):
        return self.hours
    
    
    def get_adjacences(self):
        return self.adjacences