import os
import json
class Session:
    def __init__(self, nom):
        """
        Créeer une instance d'une session. \\
        ``nom`` : String
        ``Etudiants`` :  { userName: String, couses: list
                                  userName: String, couses: list \\
                                        ... n-fois
                                }
        ``Cours``:  { name: String, hours: int, adjacences: list
                         name: String, hours: int, adjacences: list
                                        ... n-fois
                       }
        ``Periodes``: int
        """
        self.__nom = nom                                                            #Le nom de la session
        self.__Etudiants = {"userName": None, "courses": None }                     #Le dictionnaire de chaque etudiant avec les cours qu'il a
        self.__Cours = {"name": None, "hours": None, "adjacences": None}            #Le dictionnaire des cours ayant le nombre d'heures et ses adjacences
        self.__Periodes = 0                                                         #Le nombres de periodes d'1h disponible en une journée
        self.current_dir = os.path.join(os.path.dirname(__file__), 'frontend')
        self.session_file = os.path.join(self.current_dir, 'session.json')


    def set_etudiants(self, e):
        """
        Attributs les etudiants inscrits à une session

        :params: un dictionnaire contenant des objets de type Etudiant
        """
        self.__Etudiants = e


    def set_cours(self, c):
        """
        Attributs les cours proposés dans une session
        :params: un dictionnaire contenant des objets de type Cours
        """
        self.__Cours = c


    def set_periodes(self, p):
        """
        Attributs le nombre de periode pour une session
        :params: un entier
        """
        self.__Periodes = p


    def get_nom(self):
        """
        :returns le nom de la session
        """
        return self.__nom
    

    def get_etudiants(self):
        """
        Retourne un chaque etudiant et ses attributs
        """
        return self.__Etudiants


    def get_cours(self):
        return self.__Cours
    

    def afficher_cours(self):
        """
        Retourne un affichage de chaque cours et le reste des attributs
        """
        pass


    def save_to_file(self):
        """
        Sauvegarder l'object de type Session dans le fichier .json\\
        sous forme de dictionnaire.
        """
        try:
            with open(self.session_file, "w", encoding='utf-8') as json_file:
                cours_dict = {}
                
                for cours in self.__Cours:
                    
                    cour = self.__Cours[cours]
                    courX = {}
                    
                    courX["nom"] = cour.get_nom()
                    courX["heures"] = cour.get_hours()

                    adjacences = cour.get_adjacences()
                    adjacences_tab = []

                    if len(adjacences) > 0:
                        for cour_adjacent in adjacences:
                            adjacences_tab.append(cour_adjacent.get_nom())

                    courX["adjacences"] = adjacences_tab

                    cours_dict[f'{cours}'] = courX

                try:
                    json.dump(cours_dict, json_file)
                except Exception as e:
                    print("Error writing to file")
        except:
            print('File error')