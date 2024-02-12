# Les graphes

!!! info "Liens Capytale"
    * À la découvertes des graphes : [:fontawesome-solid-link: Notebook Capytale ceb1-2792273](https://capytale2.ac-paris.fr/web/c/ceb1-2792273)
    * Représentation des graphes : [:fontawesome-solid-link: Notebook Capytale 505c-2844042](https://capytale2.ac-paris.fr/web/c/505c-2844042)
    * Parcours en largeur : [:fontawesome-solid-link: Notebook Capytale be49-2854965](https://capytale2.ac-paris.fr/web/c/be49-2854965)
    * Parcours en profondeur : [:fontawesome-solid-link: Notebook Capytale e655-2874716](https://capytale2.ac-paris.fr/web/c/e655-2874716) Aïe aïe aïe la version impérative est erronée, faites un tour sur Wikipedia pour le pseudocode, ce que j'aurai dû faire ! Merci Louis ! 😰


## Synthèse

A venir ! Peut-être... 

## Détection de cycle / circuit

Dans la cas **non-orienté**, détecter un cycle est « simple » car un parcours en largeur suffit : si lors du parcours du voisinage d'un sommet on retombe sur un sommet déjà marqué, cela veut dire que l'on a détecté un cycle.

> Soit $s$ le sommet de départ. Si $u$ a été marqué, alors il existe une chaîne entre $s$ et $u$ car il est atteignable. On suppose qu'on défile le sommet $v$, il existe donc une chaîne entre $s$ et $v$ car il est lui aussi marqué. Donc si $u$ est un voisin de $v$ alors on a détecté le cycle $s ~\mathrm{-}~ \cdots ~\mathrm{-}~ u ~\mathrm{-}~ v ~\mathrm{-}~ \cdots ~\mathrm{-}~ s$.

Dans le **cas orienté**, la détection est plus délicate, car retomber sur un sommet déjà visité n'implique pas nécessairement la présence d'un circuit. Pour résoudre ce problème, il faut classifier les différents types d'arcs rencontrés par un parcours en profondeur. On suppose qu'un parcours en profondeur découvre les sommets A, B, C, F, H, E :

![](ressources/dfs.png){ width="75%" .center}

Seuls les **arcs de retour** témoigne d'un circuit ! Un arc de retour apparaît lorsqu'on parcours le voisinage d'un sommet, si l'on rencontre un des ancêtres. L'idée est donc d'ajouter un marquage supplémentaire : un sommet est dit « terminé » si on a découvert toute sa descendance. Si on tombe sur un sommet non-terminé, alors on a pris un arc de retour ! L'algorithme original colorie symboliquement les sommets en trois couleurs :

* Blanc : Sommet non-visité
* Gris : Sommet visité mais non-terminé
* Noir : Sommet terminé

L'algorithme se repose sur le parcours en profondeur récursif ici. Initialement, tous les sommets seront de couleur blanche. Lorsqu'on visitera un sommet $s$, si :

* $s$ est gris, on a pris un arc de retour, on vient de découvrir un circuit.
* $s$ est noir, on a pris un arc avant ou transverse, on ne fait rien.
* $s$ est blanc, on a pris un arc de liaison (ou $s$ est le sommet initial) :
    * Colorier le sommet $s$ en gris
    * Visiter tous les voisins de $s$ récursivement
    * Les différents appels récursifs font qu'à ce moment-là, tous les descendants de $s$ sont terminés, donc on colorie le sommet $s$ en noir

```py
BLANC, GRIS, NOIR = 0, 1, 2  # constantes symboliques

def parcours_profondeur_circuit(graphe, s, couleurs: dict) -> bool:
    pass

def possède_circuit(graphe):
    couleurs = {s: BLANC for s in graphe.sommets()}
    for s in graphe.sommets(): # on teste tous les sommets de départs possibles
        if parcours_profondeur_circuit(graphe, s, couleurs):
            return True
    return False
```

!!! question Question
    Compléter l'algorithme sur le TP Parcours en profondeur et le tester.


## Projet Dijkstra

!!! info "Lien vers le diaporama"
    * [Lien vers le diaporama sur l'algorithme de Dijkstra](ressources/dijkstra.pdf)

!!! question "Implémentation de l'algorithme de Dijkstra"
    * Implémenter la classe `GraphePondéré` qui représente un graphe non-orienté où les arêtes sont pondérées. La représentation par un dictionnaire d'adjacence est préférée. On stockera le poids d'une arête directement dans le dictionnaire d'adjacence dans un tuple :

        ```py title="Dictionnaire d'adjacence pour un graphe pondéré"
        graphe = GraphePondéré()
        graphe.adjdict = {
            'S': [('A', 4), ('B', 2)],
            'A': [('S', 4), ('B', 1), ('C', 3), ('D', 4)],
            'B': [('S', 2), ('A', 1), ('C', 6), ('E', 8)],
            'C': [('A', 3), ('B', 6), ('D', 3), ('E', 2)],
            'D': [('A', 4), ('C', 3), ('E', 2), ('F', 7)],
            'E': [('B', 8), ('C', 2), ('D', 2), ('F', 8)],
            'F': [('D', 7), ('E', 8)]
        }
        ```

        Ainsi on pourra facilement récupérer les poids des arêtes lorsqu'on parcourt le voisinage d'un sommet :

        ```py title="Exemple du parcours du voisinage pour un graphe pondéré" 
        for sommet_voisin, poids_arete in graphe.voisins('S'):
            # ...
        ```

    * Implémenter l'algorithme de Dijkstra `#!py def dijsktra(graphe, sommet_départ)` qui renvoie la distance minimale entre tous les sommets et le sommet de départ.

        ```py
        from pprint import pprint

        distances = dijkstra(graphe, 'S')
        pprint(distances)
        ```

        ```pycon
        {
            'S': 0,
            'A': 3,
            'B': 2,
            'C': 6,
            'D': 7,
            'E': 8,
            'F': 14
        }
        ```

    * Modifier l'algorithme pour connaître aussi les plus courts chemins en conservant le prédécesseur pour chaque sommet.

        ```py
        distances, prédécesseurs = dijkstra(graphe, 'S')
        pprint(prédécesseurs)
        ```

        ```pycon
        {
            'S': None,
            'A': 'B',
            'B': 'S',
            'C': 'A',
            'D': 'A',
            'E': 'C',
            'F': 'D'
        }
        ```

    * Écrire une fonction `#!py plus_court_chemin(prédécesseurs, sommet_destination)` qui renvoie les sommets du plus court chemin vers le sommet de destination.
  
        ```py
        >>> distances, prédécesseurs = dijkstra(graphe, 'S')
        >>> plus_court_chemin(prédécesseurs, 'F')
        ['S', 'B', 'A', 'D', 'F']
        ```

    * Télécharger les [données suivantes](ressources/17.zip) sur la Charente-Maritime. Déterminer le plus court chemin de Pons vers La Rochelle ! Le jeu de données est un graphe où les sommets sont les différentes communes et les arêtes des routes (artificiellement crées par mes petites mains à partir d'une triangulation de Delaunay).

        <center>
        ![](ressources/cm-dark.png#only-dark){ width="50%"}
        </center>

        <center>
        ![](ressources/cm-light.png#only-light){ width="50%"}
        </center>

    Vous pouvez utiliser la bibliothèque `matplotlib` pour afficher le plus court chemin de Pons vers La Rochelle (ChatGPT peut être utile ici).