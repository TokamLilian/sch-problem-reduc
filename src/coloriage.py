import json
def coloriage_minimal(session):
    """
    Appliquer un coloriage simple aux cours de la session
    :param: Une session de type `Session`
    """
    cours_session = {}

    def getCoursId(courseName):
        """
        Renvoie le f'cours{id}' du cours correspondant au nom passé en paramètre.
        """
        for cours in cours_session:
            courX = cours_session[cours]
            if courX["nom"] == courseName :
                return cours
        
        return None


    def getCouleursDesAdjacences(cours):
        """
        Retourne un tableau contenant les couleurs des cours adjacents au cour
        """
        CouleursDesAdjacences = []
        adjacences = cours["adjacences"]

        for adjacence in adjacences:
            adjacenceCoursId = getCoursId(adjacence)
            adjacenceCours = cours_session[adjacenceCoursId]
            # On ajoute une couleur pour chaque module du cours
            CouleursDesAdjacences.append(adjacenceCours["couleur"])

        return CouleursDesAdjacences


    def appendColors():
        for coursId in cours_session:
            if ("cours" not in coursId): break
            cours = cours_session[coursId]
            adjacencesCours = cours["adjacences"]

            for nomCoursAdjacent in adjacencesCours:
                coursAdjacentId = getCoursId(nomCoursAdjacent)
                coursAdjacent = cours_session[coursAdjacentId]

                if cours["couleur"] == coursAdjacent["couleur"]:
                    #avant de d'affecter une coleur, on s'assure que 
                    #aucun cours adjacent au cours adjacent actuel n'a deja cette couleur
                    #sinon on donne a l'adjacence une couleur de valeur max(color de ses adjacence) + 1
                    #s'il n'y a pas la couleur parmi ses adjacences, on peut lui donner la couleur ci dessous
                    couleursDesAdjacencesDeCoursAdjacent = getCouleursDesAdjacences(coursAdjacent)
                    if cours["couleur"] in couleursDesAdjacencesDeCoursAdjacent:
                        coursAdjacent["couleur"] = max(couleursDesAdjacencesDeCoursAdjacent) + 1
                        #TODO :si le cours adjacent n'est pas adjacent au cours 0, on peut lui donner la couleur 0
                        #TODO :sinon si le cours adjacent n'est pas adjacent au cours 1, on peut lui donner la couleur 1
                        #ainsi de suite...
                    else:
                        coursAdjacent["couleur"] = cours["couleur"] + 1

        return cours_session


    try:
        with open(session.session_file, "r", encoding='utf-8') as json_file:
            cours_session = json.load(json_file)
            appendColors()

        with open(session.session_file, "w", encoding='utf-8') as json_file: #save to static directory
            try:
                json.dump(cours_session, json_file, indent=3)
            except Exception as e:
                print("Error:", e)

    except Exception as e:
         print("Failed with:", str(e))