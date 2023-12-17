"""
################################################## Travail à faire ####################################################

question pour le fichier astartp.py :

1 - ecrire une fonction  heuristic(a, b) qui calcule la distance euclidienne entre deux point 2D
        exemple a = (1,2), b = (1,0)
        heuristic(a, b) = 2
2 - ecrire une fonction  heuristic(a, b) qui calcule la distance de Manhattan entre deux point 2D
3 - ecrire une fonction  heuristic(a, b) qui calcule la distance de Manhattan entre deux vecteurs
        exemple a = (1,2,1,3), b = (1,0,1,0)
        heuristic(a, b) = 0 + 2 + 0 + 3 = 5


4 - ecrire une foction voisins(grille, noeud) qui retourne une liste des viosins d'un noeud dans une grille
        exemple noeud = (0,0)
        voisins(grid, noeud) = [(0,1), (1,0)]
    reecrire cette foction pour qu'elle retourne aussi les voisins diagonaux
        exemple noeud = (0,1)
        voisins(grid, noeud) = [(0,0), (1,0), (1,1), (1,2)]

grid = numpy.array([
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
])



5 - utilisé les fonction heuristic et voisins pour completer le programme Astar.py
    Executer Astar et afficher le chemin trouvé avec print()
    afficher le resultat sous forme de grille + le chemin trouvé(indiqué par des '8' comme l'exemple)


--astar(grid, (0,0), (9,9)) :

[[8 0 1 1 0 1 1 1 1 1]
 [0 8 0 1 0 0 1 1 1 1]
 [0 8 1 1 0 0 0 1 1 1]
 [1 1 8 8 8 8 8 0 1 1]
 [0 1 1 0 0 1 1 8 0 1]
 [0 1 1 0 0 1 1 8 0 0]
 [0 0 0 0 1 1 1 8 1 1]
 [0 0 0 0 1 1 1 8 1 1]
 [1 1 1 0 1 1 1 0 8 0]
 [1 1 1 0 0 0 0 0 0 8]]

4 - calculer et afficher le nombre d'iterartions effectuer par astar
5 - afficher le chemin en utilisant le code mathplotlib fournit


####################################

question pour le fichier drone.py :

5 - dans un autre ficher python drone.py utilisé le meme code de astar pour trouver le plus court chemin
    dans une grille 3d
    exemple


grid3d = numpy.array([[
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    ]])

chemin3d :

[[[8 1 8 8 0 1 0 0 0 0]
  [1 1 1 1 1 0 0 0 0 0]
  [0 0 0 1 8 1 1 1 1 1]
  [0 1 1 1 8 1 0 0 0 0]
  [0 1 0 0 8 1 0 1 1 0]
  [1 1 0 0 0 1 8 0 0 0]
  [0 1 1 0 1 1 8 1 1 0]
  [0 1 0 0 0 0 8 8 8 0]
  [1 1 1 0 1 1 1 1 1 0]
  [0 0 0 0 0 0 0 0 0 0]]

 [[8 8 8 0 0 0 0 0 0 0]
  [0 0 1 1 8 0 0 0 0 0]
  [0 0 0 1 8 1 1 1 1 1]
  [0 1 0 1 0 1 0 0 0 0]
  [0 1 1 0 0 1 0 1 1 0]
  [0 1 0 0 0 8 8 0 0 0]
  [0 1 1 0 1 0 0 1 1 0]
  [0 1 0 0 0 0 0 0 0 0]
  [1 1 1 0 1 1 1 1 1 8]
  [0 0 0 0 0 0 0 0 1 8]]]

6 - calculer et afficher le nombre d'iterartions effectuer par drone
7 - afficher le chemin 3d en utilisant le code mathplotlib fournit
"""




