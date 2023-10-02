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
        self.suivant = chaînon_suivant # référence du chaînon suivant


class ListeChaînée:
    def __init__(self):
        """ Initialise une liste chaînée vide. """
        self.tête = None  # référence du premier chaînon

    def insérer_devant(self, élément):
        """ Insère un nouvel élément à la tête de la liste. """
        chaînon = Chaînon(élément, self.tête)  #(1)!
        self.tête = chaînon  #(2)!

    def est_vide(self):
        """ Renvoie True si la liste ne contient aucun élément, False sinon. """
        return self.tête is None

    def retirer_tête(self):
        """ Retire le premier élément de la liste. """
        if self.est_vide():
            return None
        self.tête = self.tête.suivant  #(3)!

    def insérer_après(self, chaînon, élément):
        """ Insère un nouvel élément après le chaînon donné. """
        pass
    
    def premier_élément(self):
        """ Renvoie l'élément du premier chaînon de la liste. """
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

## Exercices supplémentaires

??? question "Exercices"
   
    1. Écrire une fonction `créer_liste_depuis_tab(tab)` qui crée une liste chaînée à partir du tableau passé en argument.

        ```py
        >>> l = créer_liste_depuis_tab([12, 15, 17])
        >>> l.afficher()
        12 -> 15 -> 17
        ```
   
    2. Ajouter une méthode `n_ième_élément(self, n)` à la classe `ListeChaînée` qui renvoie la valeur du $n$-ième élément de la liste chaînée `self`.
   
        ```py
        >>> l = créer_liste_depuis_tab([12, 35, 8, 42, 27, 35])
        >>> l.n_ième_élément(4)
        27
        ```

    3. Écrire une fonction `concaténer_listes(l1, l2)` qui renvoie une liste chaînée obtenue par concaténation de `l1` et `l2` (sans copier les chaînons).

        ```py
        >>> l1 = créer_liste_depuis_tab([12, 15, 17])
        >>> l2 = créer_liste_depuis_tab([887, 998])
        >>> l3 = concaténer_listes(l1, l2)
        >>> l3.afficher()
        12 -> 15 -> 17 -> 887 -> 998
        ```

    4. Ajouter une méthode `renverser(self)` à la classe `ListeChaînée` qui renverse les éléments de la liste chaînée `self`.

        ```py
        >>> l = créer_liste_depuis_tab([12, 15, 17])
        >>> l.renverser()
        >>> l.afficher()
        17 -> 15 -> 12
        ```

    5. Ajouter une méthode `insérer(self, élément, n)` à la classe `ListeChaînée` qui insère l'élément `élément` à la $n$-ième position de la liste chaînée `self`.

        ```py
        >>> l = créer_liste_depuis_tab([12, 15, 17, 45])
        >>> l.insérer(999, 2)
        >>> l.afficher()
        12 -> 15 -> 999 -> 17 -> 45
        ```

    6. Ajouter une méthode `retirer(self, n)` à la classe `ListeChaînée` qui retire l'élément à la $n$-ième position de la liste chaînée `self`.

        ```py
        >>> l = créer_liste_depuis_tab([12, 15, 17, 45])
        >>> l.retirer(2)
        >>> l.afficher()
        12 -> 15 -> 45
        ```

    7. Ajouter une méthode `occurrences(self, élément)` à la classe `ListeChaînée` qui renvoie le nombre d’occurrences de `élément` dans la liste chaînée `self`.
   
        ```py
        >>> l = créer_liste_depuis_tab([12, 35, 12, 42, 12, 35])
        >>> l.occurrences(12)
        3
        ```

    8. Établir la complexité en temps pour chacune des méthodes et fonctions écrites précédemment.

    9. Ajouter une méthode `vers_tableau(self)` à la classe `ListeChaînée` qui renvoie un tableau des éléments de la liste chaînée `self`. Cette dernière méthode vous permettra de quasiment connaître votre note à l'avance ! Nommer votre fichier contenant votre classe Liste et les différentes fonctions demandées sous le nom `liste.py`, puis enregistrer le fichier [:fontawesome-brands-python: `note_liste.py`](ressources/note_liste.py) à coté et exécuter-le !

    10. Les 4 derniers points de la note seront réservés à la clarté et à la documentation de votre code (description des méthodes / fonctions, typage des paramètres et de la valeur renvoyée si possible, noms de variables clairs).



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

## Clarification sur l'allocation de mémoire

### Tableau dynamique `#!py list`

<div class="video-wrap">
    <div class="video-container">
        <iframe src="https://peertube.lyceeconnecte.fr/videos/embed/38dce6db-0d99-4041-b7d1-e8b085508711" frameborder="0" allowfullscreen="1"></iframe>
    </div>
</div>


### Liste chaînée `ListeChaînée`

<!-- ![type:video](./ressources/alllists.mp4){: style='width: 100%'} -->

![type:video](./ressources/alllists.mp4){: style='width: 100%'}

### Différence de complexité des primitives


|     Structure de données      |        Ajouter au début        |           Ajouter à la fin            |            Insérer             |      Supprimer un élément      |    Accès au $i$-ème élément    |
| :---------------------------: | :----------------------------: | :-----------------------------------: | :----------------------------: | :----------------------------: | :----------------------------: |
| Tableau dynamique `#!py list` | <div class="on">\(O(n)\)</div> | <div class="o1">\(O(1)\)</div> amorti | <div class="on">\(O(n)\)</div> | <div class="on">\(O(n)\)</div> | <div class="o1">\(O(1)\)</div> |
|         Liste chaînée         | <div class="o1">\(O(1)\)</div> |    <div class="on">\(O(n)\)</div>     | <div class="o1">\(O(1)\)</div> | <div class="o1">\(O(1)\)</div> | <div class="on">\(O(n)\)</div> |
|   Liste doublement chaînée    | <div class="o1">\(O(1)\)</div> |    <div class="o1">\(O(1)\)</div>     | <div class="o1">\(O(1)\)</div> | <div class="o1">\(O(1)\)</div> | <div class="on">\(O(n)\)</div> |

Ainsi il faut bien choisir, selon son utilisation, le conteneur sous-jacent des éléments lorsqu'on implémente une nouvelle structure de données comme une pile ou une file.