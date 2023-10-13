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

2. Écrire la classe `Carte` dont les attributs sont `valeur` et `couleur` (on représentera la couleur par un entier entre 0 et 3 et la valeur par un entier entre 2 et 14, où 14 correspond à l'As). Définir la méthode `#!py __repr__`  qui permettra d'afficher facilement une carte avec `#!py print` (utiliser les caractères spéciaux `♥ ♦️ ♣️ ♠️`).

    ```pycon title="Exemple d'utilisation de la classe Carte"
    >>> print(Carte(2, 0))
    2♥
    >>> print(Carte(14, 3))
    As♠️
    >>> print(Carte(11, 1))
    V♦️
    ```

3. On propose d'implémenter un paquet de cartes avec un tableau dynamique `#!py list` comme conteneur sous-jacent. Compléter la classe suivante :

    ```py title="Classe Paquet à compléter"
    class Paquet:
        """ Représente un paquet de cartes. """

        def __init__(self, cartes: list[Carte]) -> None:
            self.cartes = cartes  # [carte_dessous, ..., carte_dessus]

        def tirer_carte_dessus(self) -> Carte:
            """ Retire et renvoie la carte au desssus du paquet. """
            pass

        def ajouter_carte_dessus(self, carte: Carte) -> None:
            """ Ajoute une carte au dessus du paquet. """
            pass

        def ajouter_carte_dessous(self, carte: Carte) -> None:
            """ Ajoute une carte au dessous du paquet. """
            pass

        def ajouter_paquet_dessous(self, autre) -> None:
            """ Ajoute un autre paquet de carte en dessous du paquet. """
            pass

        def est_vide(self) -> bool:
            """ Renvoie True si le paquet est vide, False sinon. """
            pass

        def __repr__(self) -> str:
            pass

        def mélanger(self) -> None:
            """ Mélange les cartes du paquet. """
            pass
    ```


4. Compléter les fonctions libres suivantes :

    ```py title="Fonctions libres à compléter"
    def générer_paquet_52_cartes() -> Paquet:
        """ Génère un paquet classique de 52 cartes. """
        pass


    def couper(paquet: Paquet) -> tuple[Paquet, Paquet]:
        """ Coupe le paquet en deux et renvoie les deux nouveaux paquets. """
        pass

    ```

    ```pycon title="Exemple d'utilisation"
    >>> paquet = générer_paquet_52_cartes()
    >>> print(paquet)
    [2♥, 3♥, 4♥, 5♥, 6♥, 7♥, 8♥, 9♥, 10♥, V♥, D♥, R♥, As♥, 2♦️, 3♦️, 4♦️, 5♦️, 6♦️, 7♦️, 8♦️, 9♦️, 10♦️, V♦️, D♦️, R♦️, As♦️, 2♣️, 3♣️, 4♣️, 5♣️, 6♣️, 7♣️, 8♣️, 9♣️, 10♣️, V♣️, D♣️, R♣️, As♣️, 2♠️, 3♠️, 4♠️, 5♠️, 6♠️, 7♠️, 8♠️, 9♠️, 10♠️, V♠️, D♠️, R♠️, As♠️]
    >>> p, q = couper(paquet)
    >>> print(q)
    [2♣️, 3♣️, 4♣️, 5♣️, 6♣️, 7♣️, 8♣️, 9♣️, 10♣️, V♣️, D♣️, R♣️, As♣️, 2♠️, 3♠️, 4♠️, 5♠️, 6♠️, 7♠️, 8♠️, 9♠️, 10♠️, V♠️, D♠️, R♠️, As♠️]
    ```

5. Implémenter une classe `Bataille` qui comprend une méthode `réinitialiser` qui distribue aléatoirement les cartes entre deux joueurs et `jouer` qui joue automatiquement le jeu de Bataille.

6. En moyenne, sur un grand nombre de parties, combien de tours de jeu comporte une partie de Bataille ?