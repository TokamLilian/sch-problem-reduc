import os
import json

from Session import *
from Etudiant import *
from Cour import *

class main:
    
    def __init__(self):
        self.Year = {}
        self.files_dir = os.path.join(os.path.dirname(__file__), 'files')
        self.students_file = os.path.join(self.files_dir, 'Etudiants.json')
        self.cours_file = os.path.join(self.files_dir, 'Cours.json')

    def ajouter(self, s):
        if not isinstance(s,Session) : raise TypeError("La session doit etre de type 'Session'")

        else: 
            x = len(self.Year)
            self.Year[f"session{x}"] = s


    def creer_etudiants(self, obj):
        """
        Retourne un dictionnaire d'etudiants
        """
        #taille = len(obj)
        return {f'{etudiant}':Etudiant(obj[etudiant]["userName"], obj[etudiant]["matricule"], obj[etudiant]["coursInscrits"]) for etudiant in obj }
    

    def creer_cours(self, obj):
        """
        Retourne un dictionnaire de cours
        """
        taille = len(obj)
        return {f'{cours}':Cour(obj[cours]["nom"], obj[cours]["heures"]) for cours in obj }
    

    def set_adjacences(self, session):
        """
        Set les adjacences entre les cours 
        """
        students = session.get_etudiants()
        
        for current_student in students:
            student = students[current_student]

            cours = student.get_cours()
            for course in cours:
                print(course.get_nom())



    def start(self, session):
        """
        Permet de lancer la session en question, en creant les objets \\
        de type Cours et les objects de type Etudians dans l'instance de la Session
        """
        try:
           with open(self.cours_file, "r", encoding='utf-8') as courses_file:
                Cours = json.load(courses_file) 
                session.set_cours(i.creer_cours(Cours))
        except Exception as e:
            print(e)

        try:
           with open(self.students_file, "r", encoding='utf-8') as students_file:
               Etudiants = json.load(students_file) 
               session.set_etudiants(i.creer_etudiants(Etudiants))
        except Exception as e:

            print(e)

        self.set_adjacences(session)
    

if __name__ == "__main__":
    i = main()

    nom = "Automne 2023"                                             ##le nom de la session doit etre au debut du fichie lu ou le nom du fichier

    session = Session(nom)
    i.start(session)
    
    #session.save_to_file()
    i.ajouter(session)
