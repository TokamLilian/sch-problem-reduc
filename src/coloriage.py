import json
def coloriage_minimal(session):
    """
    Appliquer un coloriage simple aux cours de la session
    :param: Une session de type `Session`
    """
    cours_session = {}

    def getCoursId(courseName):
        for cours in cours_session:
            courX = cours_session[cours]
            if courX["nom"] == courseName :
                return cours
        
        return None


    def appendColors():
        for coursId in cours_session:
            if ("cours" not in coursId): break
            cours = cours_session[coursId]
            adjacencesCours = cours["adjacences"]

            for nomCoursAdjacent in adjacencesCours:
                coursAdjacentId = getCoursId(nomCoursAdjacent)
                coursAdjacent = cours_session[coursAdjacentId]

                if cours["couleur"] == coursAdjacent["couleur"]:
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