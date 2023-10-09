# Les files

## Description et interface

Une **file** est une structure de données linéaire, homogène et dynamique. Elle est fondée sur le principe du « *premier entré, premier sorti* » (en anglais « *First In, First Out* », **FIFO**). Une file d'attente en est la parfaite analogie !

![type:video](./ressources/file.mp4){: style='width: 100%'}

L'interface d'une file est composée des primitives suivantes :

| Opération         | Description                                                         |
| ----------------- | ------------------------------------------------------------------- |
| Constructeur      | Créer une file vide.                                                |
| `file.enfiler(e)` | Ajoute l'élément `e` à la fin de la file.                          |
| `file.défiler()`  | Retire et renvoie l'élément au début de la file.   |
| `file.tête()`     | Renvoie l'élément au début de la file.           |
| `file.queue()`    | Renvoie l'élément à la fin de la file.           |
| `file.taille()`   | Renvoie le nombre d'éléments dans la file.                          |
| `file.est_vide()` | Renvoie `True` si la file ne contient aucun élément, `False` sinon. |

## Exercices

??? question "Deux implémentations classiques"

    ```py title="Exemple d'utilisation d'une file"
    >>> f = File()
    >>> f.enfiler(10)
    >>> f.enfiler(42)
    >>> f.enfiler(888)
    >>> f.enfiler(31)
    >>> f.afficher()
    31 -> 888 -> 42 -> 10
    >>> f.tête()
    10
    >>> f.queue()
    31
    >>> f.défiler()
    10
    >>> f.défiler()
    42
    >>> f.taille()
    2
    >>> f.afficher()
    31 -> 888
    >>> f.est_vide()
    False
    >>> f.défiler()
    888
    >>> f.défiler()
    31
    >>> f.est_vide()
    True
    ```

    1. Implémenter une file à partir d'un tableau dynamique (`#!py list`) comme conteneur sous-jacent (utiliser les méthodes `.insert` et `.pop`). Donner la complexité en temps des primitives.

    2. Implémenter une file à partir d'une liste doublement chaînée comme conteneur sous-jacent (vous pouvez utiliser mon implémentation [:fontawesome-brands-python: `liste_doublement_chainee.py`](ressources/liste_doublement_chainee.py)). Donner la complexité en temps des primitives.

    3. Quelle est la structure de données la plus adaptée pour implémenter une file ; est-ce un tableau dynamique ou une liste doublement chaînée ? Justifier.

<!-- 
## Exercices

* Implémenter une file statique à partir d'un tableau statique circulaire (à implémenter aussi).

* Implémentation d'une file avec deux piles. -->


## Jeu de Bataille

Le but de ce projet est de coder un jeu de Bataille en Python et de réutiliser à bon escient les structures de données vues jusqu'à maintenant (objets, piles, files, tableaux etc.).

### Règles

![](ressources/war.jpg)

* On distribue aléatoirement 52 cartes à deux joueurs.
* À chaque tour, chaque joueur retourne la carte du haut de sa main.
* Celui qui a la carte de la plus haute valeur, récupère la levée qu'il place sous son paquet.
* En cas d'égalité de valeurs — cas appelé *bataille* —  les joueurs commencent par placer une première carte face cachée puis une seconde carte face visible pour décider qui fera la levée. En cas de nouvelle égalité, la procédure est répétée.
* Lorsqu'un joueur a en sa possession toutes les cartes du jeu, la partie se termine et il est déclaré gagnant.

### Implémentation

1. Quelle structure de données est adaptée pour représenter :
   
    1. une carte de jeu ?

    2. le paquet de départ ?
   
    2. la main d'un joueur ?
   
    3. le tas de cartes d'un joueur lors d'une bataille ?

2. Écrire la classe `Carte` dont les attributs sont `valeur` et `couleur` (on représentera la couleur par un entier entre 0 et 3 et la valeur par un entier entre 1 et 13). Définir la méthode `#!py __str__` qui permettra d'afficher facilement une carte avec `#!py print` (utiliser les caractères spéciaux `♥ ♦️ ♣️ ♠️`).

3. Proposer une implémentation du jeu de la Bataille.