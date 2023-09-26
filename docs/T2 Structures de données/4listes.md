# Les listes chaînées

## Clarification sur les références

Vous avez sûrement déjà eu envie de copier une liste de cette manière :

```py title="Une copie malheureuse"
>>> a = [1, 2, 3, 4]
>>> b = a
>>> b.append(5)
>>> a
[1, 2, 3, 4, 5]
```

Aïe, la liste `a` a été modifiée, mais pourquoi ? Vidéo explicative.

![type:video](./ressources/ref.mp4){: style='width: 100%'}

On retient que, en Python, tous les objets (tout excepté les entiers et les flottants finalement) sont manipulés par **référence**.

## Interface et implémentation d'une liste chaînée

Une **liste chaînée** est une structure de données linéaire, homogène et dynamique composée de **chaînons** (ou nœuds). Chaque chaînon contient :

* un élément 
* une référence vers le chaînon suivant

Une telle structure ne stockera alors que la référence du premier chaînon, appelé tête.


![type:video](./ressources/liste.mp4){: style='width: 100%'}

Contrairement à un tableau dynamique, les éléments ne sont plus stockés de manière contiguës dans la mémoire. Si l'opération d'insertion et de suppression d'un élément se déroule en temps constant, l'accès au $i$-ème élément d'une liste chaînée s'effectue en contrepartie en temps linéaire.

```py
class Chaînon:
    def __init__(self, élément, chaînon_suivant):
        self.élément = élément
        self.chaînon_suivant = chaînon_suivant # référence du chaînon suivant


class ListeChaînée:
    def __init__(self):
        """ Initialise une liste chaînée vide. """
        self.chaînon_tête = None  # référence du premier chaînon

    def insérer_devant(self, élément):
        """ Insère un nouvel élément à la tête de la liste. """
        chaînon = Chaînon(élément, self.chaînon_tête)  #(1)!
        self.chaînon_tête = chaînon  #(2)!

    def est_vide(self):
        """ Renvoie True si la liste ne contient aucun élément, False sinon. """
        return self.chaînon_tête is None

    def retirer_tête(self):
        """ Retire le premier élément de la liste. """
        if self.est_vide():
            return None
        self.chaînon_tête = self.chaînon_tête.suivant  #(3)!

    def insérer_après(self, chaînon, élément):
        """ Insère un nouvel élément après le chaînon donnée. """
        pass
    
    def tête(self):
        """ Renvoie l'élément du premier élément de la liste. """
        pass

    def taille(self):
        """ Renvoie le nombre d'éléments de la liste. """
        pass

    def afficher(self):
        """ Affiche les éléments de la liste. """
        pass
```

1. On crée un nouveau chaînon que l'on connecte au premier chaînon de notre liste.
2. On met à jour la tête de notre liste.
3. Puisque le chaînon que l'on déconnecte ne sera plus accessible dans le programme, Python le supprimera de la mémoire (par le biais du garbage collector).

??? question "Exercices"
    1. Compléter les trois dernières méthodes.

        ```py title="Exemple d'utilisation d'une liste chaînée"
        >>> l = ListeChaînée()
        >>> l.insérer_devant(36)
        >>> l.insérer_devant(7)
        >>> l.insérer_devant(15)
        >>> l.insérer_devant(42)
        >>> l.afficher()
        42 -> 15 -> 7 -> 36
        >>> l.taille()
        4
        >>> l.tête()
        42
        >>> l.retirer_tête()
        >>> l.afficher()
        15 -> 7 -> 36
        >>> l.insérer_après(l.tête.suivant, 999)
        >>> l.afficher()
        15 -> 7 -> 999 -> 36
        ```

    2. Quelle est la complexité en temps du calcul de la taille de la liste ? Quel attribut aurait-on pu ajouter à `ListeChaînée` pour améliorer cette complexité ? 

    3. Implémenter une pile à partir d'une liste chaînée.


## Liste doublement chaînée

Une liste chaînée a un seul sens de parcours, on la parcours toujours en partant de la tête. Pour remédier à ce problème, on peut inclure une référence au chaînon précédent dans chaque chaînon : on aboutit alors à une nouvelle structure de données (toujours linéaire, homogène et dynamique) appelée **liste doublement chaînée**.

![type:video](./ressources/liste2.mp4){: style='width: 100%'}

On pourra alors inclure une référence vers le dernier chaînon (la queue) dans l'objet de type `ListeDoublementChaînée` :

```py title="Définition des attributs d'une liste doublement chaînée", hl_lines="4 10"
class ChaînonDoublementChaînée:
    def __init__(self, élément, précédent, suivant):
        self.élément = élément
        self.précédent = précédent
        self.suivant = suivant

class ListeDoublementChaînée:
    def __init__(self):
        self.tête = None
        self.queue = None
```

On pourra alors définir tout un tas de primitives sur cette structure : `taille`, `est_vide`, `tête`, `queue`, `insérer_devant`, `insérer_derrière` etc. Une liste doublement chaînée est souvent utilisée comme conteneur sous-jacent de la prochaine structure de données étudiée, les **files**.