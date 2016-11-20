#Vérifie qu'une variable peut être parser en entier
def isInt(s):
    try :
        int(s)
        return True
    except ValueError:
        return False

# Verifie que la formule est 2-SAT.
# Chaque élément du tableau doit contenir 2 éléments (Ou).
def isFormulaCorrect(T):
    retour = True;

    # Nombre de ou paire
    for i in range(0,len(T)):
        if (len(T[i]) != 2):
            retour = False;

    # Les variables dans les ou sont soit des chiffres (int), soit des chiffres commençant par un ! (not).
    for i in range(0, len(T)):
        for y in range (0,2):
            if not((isInt(T[i][y])) or (T[i][y][0] == '!' and isInt(T[i][y][1:]))) :
                retour = False;

    return retour;

# Trouver la forme négatitive d'un champ,
def renverse(s):
    if s[0]=='!':
        s = s.replace('!','');
    else:
        s = '!' + s;
    return s;

T = [['1','!2'],['3','4'],['!2','!3'],['4','!5'],['2','!5']];

def graphe2_sat(T):
    # Verifie que la formule est 2-SAT
    if not(isFormulaCorrect(T)):
        return false;

    # Fait le graphe avec les 2 premiers variables
    g = DiGraph({renverse(T[0][0]):{T[0][1]}, renverse(T[0][1]):{T[0][0]}});

    # Ajoute les autre arc
    for i in range(1, len(T)):
        g.add_path([renverse(T[i][0]),T[i][1]]);
        g.add_path([renverse(T[i][1]),T[i][0]]);

    # Affiche le graphe
    show(g)
    return true;

graphe2_sat(T);
