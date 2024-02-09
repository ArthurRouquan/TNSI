# Les graphes

!!! info "Liens Capytale"
    * À la découvertes des graphes : [:fontawesome-solid-link: Notebook Capytale ceb1-2792273](https://capytale2.ac-paris.fr/web/c/ceb1-2792273)
    * Représentation des graphes : [:fontawesome-solid-link: Notebook Capytale 505c-2844042](https://capytale2.ac-paris.fr/web/c/505c-2844042)
    * Parcours en largeur : [:fontawesome-solid-link: Notebook Capytale be49-2854965](https://capytale2.ac-paris.fr/web/c/be49-2854965)
    * Parcours en profondeur : [:fontawesome-solid-link: Notebook Capytale e655-2874716](https://capytale2.ac-paris.fr/web/c/e655-2874716)


## Synthèse

A venir ! Peut-être... 

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