# Programmation Orientée Objet

!!! info "Liens Capytale"
    * Exercices : [:fontawesome-solid-link: Notebook Capytale d7ca-1776728](https://capytale2.ac-paris.fr/web/c/d7ca-1776728)
    * Correction : [:fontawesome-solid-link: Notebook Capytale 4e10-1778758](https://capytale2.ac-paris.fr/web/c/4e10-1778758)  

## Préambule

La Programmation Orientée Objet (abrégée POO) est un **paradigme de programmation**, au même titre que la programmation impérative que nous pratiquons déjà ou la programmation fonctionnelle que nous étudierons cette année. Chaque paradigme de programmation peut être considéré comme une philosophie, un parti-pris revendiqué dans la manière d'aborder un problème à résoudre.

En optant pour la POO, nous faisons le choix d'organiser et structurer notre code de manière à regrouper des données et des fonctionnalités associées au sein d'entités autonomes appelées objets. C'est un outil que tout programmeur doit maîtriser !

## Un objet ? Un agglomérat de valeurs.

Il arrive parfois que certaines valeurs, prises séparément, n'aient pas de signification en elles-mêmes. Par exemple, un livre peut être représenté par plusieurs valeurs : un titre, un auteur, une année de parution etc. Un exemple de livre concret :

```py
titre  = "L'Étranger"
auteur = "Albert Camus"
année  = 1942
```

Or le lien logique entre ces trois valeurs n'apparaît pas dans ce programme, elles sont effectivement indépendantes. La POO propose alors un moyen de regrouper, de lier logiquement, plusieurs valeurs au sein d'une même entité, un **objet**. Ces valeurs sont alors appelées **attributs** de l'objet. Ainsi dans l'exemple précédent, on regroupera ces trois valeurs (titre, auteur et année) dans un même objet. On aboutira à :

```py
un_livre = Livre("L'Étranger", "Albert Camus", 1942) #(1)!
print(un_livre.titre)  # affiche "L'Étranger"
print(un_livre.année)  # affiche "1942"
```

1. `#!py Livre("L'Étranger", "Albert Camus", 1942)` crée un nouveau livre.

Au lieu de manipuler trois valeurs séparément, on manipulera alors qu'un seul objet. Puisqu'un objet regroupe plusieurs valeurs, un objet peut être vu comme une *grosse* variable, une variable qui contient d'autres variables !

!!! tip "Accès à un attribut"
    Pour accéder à un attribut d'un objet, on écrira `objet.attribut`.

Une **classe** est le modèle général à partir duquel les objets sont créés, elle définit notamment les attributs de l'objet. De la même manière qu'une valeur est une instance d'un type, **un objet est une instance d'une classe**. Une classe définit donc un **type personnalisé**, il arrive souvent que les notions de classe et de type soient confondues.

<figure markdown>
![](ressources/type.png#only-light){ width=400 }
![](ressources/type-dark.png#only-dark){ width=400 }
</figure>

En Python, la définition de la classe `Livre` s'écrira comme :


```py
class Livre:  #(1)!
    def __init__(self, un_titre, un_auteur, une_année): #(2)!
        self.titre  = un_titre #(3)!
        self.auteur = un_auteur
        self.année  = une_année
```

1. Début de la définition de la classe. Il est usuel de commencer le nom d'une classe par une **majuscule** pour le différencier d'un nom de variable.

2. `__init__` une fonction spéciale, c'est le **constructeur**. Pour qu'un utilisateur crée un nouveau livre, il aura besoin de fournir son titre, son auteur et son année de parution. C'est précisément la fonction qui est appelée lorsque l'expression `#!py Livre("L'Étranger", "Albert Camus", 1942)` est évaluée.

3. `#!py self.titre` est le premier attribut de l'objet en cours de création. On y affecte alors le titre passé en argument au constructeur, à savoir `un_titre`. Le mot-clé `#!py self` est une référence à l'instance courante de la classe (l'objet en cours de création ou de manipulation), ce qui vous permet d'accéder aux attributs de cette instance.


À la suite de cette définition, on pourra alors **instancier** plusieurs objets (ici des livres) de la classe `Livre` :


```py
livre1 = Livre("L'Étranger", "Albert Camus", 1942)
livre2 = Livre("Martin Eden", "Jack London", 1909)
livre3 = Livre("Les Frères Karamazov", "Fiodor Dostoïevski", 1880)
```

!!! info "Visualisation du déroulement avec PythonTutor"
    Il est possible de visualiser l’exécution du programme pas-à-pas grâce à [ :fontawesome-solid-link: PythonTutor](https://pythontutor.com/render.html#code=class%20Livre%3A%20%20%0A%20%20%20%20def%20__init__%28self,%20un_titre,%20un_auteur,%20une_ann%C3%A9e%29%3A%20%0A%20%20%20%20%20%20%20%20self.titre%20%20%3D%20un_titre%20%0A%20%20%20%20%20%20%20%20self.auteur%20%3D%20un_auteur%0A%20%20%20%20%20%20%20%20self.ann%C3%A9e%20%20%3D%20une_ann%C3%A9e%0A%0Alivre1%20%3D%20Livre%28%22L'%C3%89tranger%22,%20%22Albert%20Camus%22,%201942%29%0Alivre2%20%3D%20Livre%28%22Martin%20Eden%22,%20%22Jack%20London%22,%201909%29%0Alivre3%20%3D%20Livre%28%22Les%20Fr%C3%A8res%20Karamazov%22,%20%22Fiodor%20Dosto%C3%AFevski%22,%201880%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false). Il est indispensable en programmation de connaître exactement le déroulement des opérations !

!!! tip "Code de base d'une classe"
    Une nouvelle classe s'écrit souvent comme :

    ```py
    class NomDeLaClasse:
        def __init__(self, paramètre1, paramètre2, ...):
            self.attribut1 = ...
            self.attribut2 = ...
            ...
    ```

    Côté utilisateur, un objet de cette classe sera instancié comme :

    ```py
    mon_objet = NomDeLaClasse(paramètre1, paramètre2, ...)
    print(mon_objet.attribut1)  # accès à un attribut
    ```


??? note "Similarité avec un dictionnaire"
    Finalement, un objet est une structure de données plus ou moins similaire à un dictionnaire. En effet, il aurait été possible de représenter un livre comme :

    ```py
    livre1 = {
        "titre": "L'Étranger",
        "auteur": "Albert Camus",
        "année": 1942
    }

    print(livre1["titre"])  # accès similaire à un attribut
    ```

    Alors pourquoi s'embêter avec la POO ? Patience, les objets offrent tout un tas de fonctionnalités spécifiques que l'on étudiera par la suite.

??? question ":fontawesome-solid-book:   Exercice 1 - Un rat de bibliothèque"
  
    1. Instancier un nouveau livre `mon_livre_favori` et afficher ensuite son titre.

    2. Le professeur documentaliste souhaite que vos livres prennent en compte la langue originale d'écriture. Modifiez donc la classe `Livre` pour inclure un nouvel attribut appelé `langue_originale`. Ensuite, mettez à jour l'instantiation des quatre livres précédemment créés pour inclure également l'information sur la langue originale.
   
    3. Écrire une fonction `plus_ancien(livre1, livre2)` qui renvoie le titre du livre ayant été publié en premier parmi les deux livres passés en argument.

        ```py title="Exemple d'utilisation de la classe"
        >>> livre1 = Livre("L'Étranger", "Albert Camus", 1942)
        >>> livre2 = Livre("Martin Eden", "Jack London", 1909)
        >>> livre3 = Livre("Les Frères Karamazov", "Fiodor Dostoïevski", 1880)
        >>> plus_ancien(livre1, livre3)
        'Les Frères Karamazov'
        ```

??? question ":fontawesome-solid-user:   Exercice 2 - Classe et salle de classe"
    1. Écrire une classe `Eleve` contenant les attributs `nom`, `classe` et `moyenne`.
    
    2. Instancier trois élèves de cette classe de NSI.
    
    3. Écrire une fonction `chouchou(eleve1, eleve2)` qui renvoie le nom de l'élève ayant la meilleure moyenne.
        
        ```py title="Exemple d'utilisation de la classe"
        >>> riri = Eleve("Hubert", "TG2", 12)
        >>> fifi = Eleve("Louie", "TG6", 15)
        >>> loulou = Eleve("Hugues", "TG1", 8)
        >>> chouchou(riri, fifi)
        'Louie'
        ```

??? question ":fontawesome-solid-square-root-variable:   Exercice 3 - Un constructeur plus original"
    Écrire une classe `TriangleRectangle` qui contiendra les attributs `cote1`, `cote2` et `hypotenuse`. Cependant, le constructeur ne prendra en paramètres que `cote1` et `cote2`, l'attribut `hypotenuse` se calculera automatiquement.

    ```py title="Exemple d'utilisation de la classe"
    >>> mon_triangle = TriangleRectangle(3, 4)
    >>> mon_triangle.cote1
    3
    >>> mon_triangle.cote2
    4
    >>> mon_triangle.hypotenuse
    5.0
    ```

??? note "On vous a menti !"
    En Python, tout est objet. Il n'existe pas de types primitifs comme dans la plupart des langages ! Même un simple entier est en fait un objet :

    ```py
    >>> n = 42
    >>> type(n)
    <class 'int'>
    >>> n.real
    42
    ```

    Les chaînes de caractères, les flottants, les listes, les dictionnaires etc. sont tous des objets !
   

## Un objet ? Un agglomérat de valeurs ET de fonctions.


Un objet regroupe des valeurs (attributs) et aussi des fonctions qui agissent sur ces valeurs, et ces fonctions sont appelées **méthodes**. Par exemple, définissons une classe `Rectangle` rudimentaire :

```py
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur  = largeur
```

On pourrait alors souhaiter calculer l'aire des rectangles de cette classe, une manière de faire serait de définir une simple fonction :

```py
def calculer_aire(rectangle):
    return rectangle.longueur * rectangle.largeur
```

Une fois la classe `Rectangle` et la fonction `calculer_aire` définies, l'utilisateur peut les utiliser comme :

```py
# Création d'objets de la classe Rectangle
rect1 = Rectangle(5, 3)
rect2 = Rectangle(7, 4)

# Appel de la fonction calculer_aire
aire1 = calculer_aire(rect1)
aire2 = calculer_aire(rect2)

# Affichage des aires calculées
print(aire1)
print(aire2)
```

Une nouvelle manière de faire est de déplacer la fonction `calculer_aire` **à l'intérieur de la classe**, cette fonction devient alors une **méthode** :

```py hl_lines="6 7 15 16"
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur  = largeur

    def calculer_aire(self):
        return self.longueur * self.largeur


# Création d'objets de la classe Rectangle
rect1 = Rectangle(5, 3)
rect2 = Rectangle(7, 4)

# Appel de la méthode calculer_aire
aire1 = rect1.calculer_aire()
aire2 = rect2.calculer_aire()

# Affichage des aires calculées
print(aire1)
print(aire2)
```

!!! tip "Appel d'une méthode"
    Pour appeler une méthode sur un objet, on écrira `objet.méthode(arg1, arg2, ...)`.


!!! note "Plus de précision sur `self`"
    * Lorsque `#!py calculer_aire(rect1)` est évalué, le paramètre `rectangle` de la fonction `calculer_aire(rectangle)` reçoit une référence à l'objet `rect1`.

    * Exactement de la même manière, lorsque `#!py rect1.calculer_aire()` est évalué, le paramètre `#!py self` de la méthode `#!py calculer_aire(self)` reçoit une référence à l'objet `#!py rect1`.
   
    En d'autres termes, `#!py self` est une référence à l'objet sur lequel la méthode est appelée.

??? note "Juste une autre façon d'appeler une fonction ?"
    Finalement, quelle différence entre `rect1.calculer_aire()` et `calculer_aire(rect1)` ? La différence réside dans la façon dont le calcul de l'aire est organisé :

    - En Python, `calculer_aire(rectangle)` est une fonction indépendante et générale qui prend un objet de n'importe quel type en tant que paramètre.

    - `rect1.calculer_aire()` est appelé en tant que méthode de l'objet `rect1`. Cela signifie que la méthode `calculer_aire` est définie *spécifiquement* pour les objets de la classe `Rectangle`. Une nouvelle classe `Cercle` pourrait alors définir une méthode `calculer_aire` spécifique.

Le **constructeur** `#!py def __init__(self, ...):` est donc une méthode spéciale qui permet d'instancier un nouvel objet et d'**initialiser** ses attributs.

## Exercices

??? question ":fontawesome-solid-shapes:   Exercice 4 - Ça ne manque pas d'aire !"
    1. Créer une fonction `calculer_périmètre(rectangle)` externe qui renvoie le périmètre du rectangle donné en argument.
    
    2. Transformer cette fonction en une méthode de la classe `Rectangle`.

    3. Au sein du même script où est définit la classe `Rectangle`, définir une nouvelle classe `Cercle`. On souhaite une fonction ou une méthode qui permet de calculer aussi l'aire pour les instances de `Cercle`.

??? question ":fontawesome-solid-car:   Exercice 5 - Vroum Vroum"
    1. Écrire une classe `Voiture` qui contiendra les attributs `kilometrage`, `consommation` (nombre de litres de carburant consommé par kilomètre) dont les valeurs seront données comme arguments à l'initialisation et un dernier attribut `carburant` valant 0 par défaut.

    2. Doter la classe d'une méthode `affiche` qui affiche le kilométrage et le carburant disponible.

    3. Doter la classe d'une méthode `remplir` qui prend en argument un entier correspondant au volume de carburant à ajouter au réservoir.

    4. Doter la classe d'une méthode `avance` qui prend en argument un entier correspondant au nombre de kilomètres parcourus et qui actualise les valeurs des attributs `kilometrage` et `consommation`.

    ```pycon title="Exemple d'utilisation de la classe"
    >>> vega_myssil = Voiture(0, 8)
    >>> vega_myssil.affiche()
    La voiture a parcouru 0 kilomètres et il y a 0 litres d'essence dans le réservoir.
    >>> vega_myssil.remplir(25)
    >>> vega_myssil.avance(200)
    >>> vega_myssil.affiche()
    La voiture a parcouru 200 kilomètres et il y a 9.0 litres d'essence dans le réservoir.
    ```

??? question ":fontawesome-solid-clock:   Exercice 6 - Tic Tac"
    1. Écrire une classe `Horloge` qui contiendra les attributs `heures`, `minutes` et `secondes`.

    2. Doter la classe d'une méthode `#!py affiche(self)` qui affiche le temps de l'instance `#!py self`.
    
    3. Doter la classe d'une méthode `#!py avance(self, s)` qui avance le temps de `s` secondes de l'instance `#!py self`.

    ```pycon title="Exemple d'utilisation de la classe"
    >>> h = Horloge(17, 25, 38)
    >>> h.heures
    17
    >>> h.minutes
    25
    >>> h.secondes
    38
    >>> h.affiche()
    Il est 17 heures, 25 minutes et 38 secondes.
    >>> h.avance(27)
    >>> h.affiche()
    Il est 17 heures, 26 minutes et 5 secondes.
    ```

??? question ":fontawesome-solid-gamepad:   Exercice 7 - Un début de jeu vidéo"
    Écrire une classe ```Player``` qui :

    - ne prendra aucun argument lors de l'instanciation.
    - affectera à chaque objet créé un attribut ```energie``` valant 3 par défaut. 
    - affectera à chaque objet créé un attribut ```alive``` valant ```True``` par défaut.
    - fournira à chaque objet une méthode ```blessure()``` qui diminue l'attribut ```energie``` de 1.
    - fournira à chaque objet une méthode ```soin()``` qui augmente l'attribut ```energie``` de 1.
    - si l'attribut ```energie``` passe à 0, l'attribut ```alive``` doit passer à ```False``` et ne doit plus pouvoir évoluer.

    ```pycon title="Exemple d'utilisation de la classe"
    >>> mario = Player()
    >>> mario.energie
    3
    >>> mario.soin()
    >>> mario.energie
    4
    >>> mario.blessure()
    >>> mario.blessure()
    >>> mario.blessure()
    >>> mario.alive
    True
    >>> mario.blessure()
    >>> mario.alive
    False
    >>> mario.soin()
    >>> mario.alive
    False
    >>> mario.energie
    0
    ```

??? question ":fontawesome-solid-sack-dollar:   Exercice 8 - Un stage chez la Société Générale"
    Définir une classe `CompteBancaire` dont le constructeur recevra en paramètres :

    * un attribut `titulaire` stockant le nom du propriétaire.
    * un attribut `solde` contenant le solde disponible sur le compte.

    Cette classe contiendra deux méthodes `retrait` et `depot` qui permettront de retirer ou de déposer de l'argent sur le compte.

    
    ```pycon title="Exemple d'utilisation de la classe"
    >>> mon_compte = CompteBancaire("A. Rouquan", 1000)
    >>> mon_compte.retrait(50)
    Vous avez retiré 50 euros
    Solde actuel du compte : 950 euros
    >>> mon_compte.retrait(40000)
    Retrait impossible
    >>> mon_compte.depot(10000000)
    Vous avez déposé 10000000 euros
    Solde actuel du compte : 10000950 euros
    ```



??? question ":fontawesome-solid-dice:   Exercice 9 - Des dès"
    On souhaite construire une base d'objets servant à créer des jeux utilisant des dés.

    - Un dé possède un nombre de faces, ainsi qu'une valeur (la face supérieure du dé une fois qu'on l'a lancé, et la valeur -1 s'il n'a pas encore été lancé). On doit pouvoir lancer le dé, c'est-à-dire lui attribuer une valeur aléatoire entre 1 et son nombre de faces. 

    - Un jeu de dés est un ensemble de dés. On doit pouvoir lancer tous les dés (en une fois), faire la somme des valeurs des dés, et on souhaite afficher la valeur des dés ainsi que leur somme.
    
    Questions :

    1. Déterminer les attributs et méthodes pour deux classes représentant ce problème : une classe `Jeu` et une classe `Dé`.
    
    2. Définir les classes en Python. sachant qu'une instance de classe `Jeu` doit prendre en arguments le nombre de dés et le nombre de faces de chaque dé (identique pour tous les dés), et qu'une instance de classe `De` doit prendre en argument son nombre de faces.

    ```pycon title="Exemple d'utilisation"
    >>> j = Jeu(3, 6)  # création d'un jeu de 3 dés à 6 faces
    >>> j.afficher()
    Les dés n'ont pas été lancés !
    >>> j.lancer()
    >>> j.somme()
    13
    >>> j.afficher()
    Les dés valent 2, 5 et 6 et leur somme vaut 13.
    ```

## Résumé et vocabulaire

![type:video](./ressources/objet.mp4){: style='width: 100%'}

| Terme            | Définition                                                                                     |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| **Classe**       | Type personnalisé. Modèle pour créer des objets définissant leurs attributs et leurs méthodes. |
| **Objet**        | Instance concrète d'une classe. Agglomère un ensemble de valeurs (attributs).                  |
| **Attributs**    | Valeurs agglomérées dans un objet.                                                             |
| **Méthodes**     | Fonctions spécifiques et internes à une classe.                                                |
| **Constructeur** | Méthode spéciale qui permet d'instancier un nouvel objet et d'initialiser ses attributs.       |

## Mini-Projet : Mettre le paquet

L'objectif principal de ce projets est d'apprendre à structurer son code en définissant des classes pertinentes.

On souhaite créer le jeu de cartes *Bataille* (un peu plus tard). Pour y parvenir, on souhaite d'abord représenter **un paquet de cartes** qui soit général : il pourra s'agir du paquet des 52 cartes, mais aussi de la main d'un joueur ou d'un tas de cartes quelconque. 

```pycon title="Exemple d'utilisation"
>>> paquet = créer_52_cartes()
>>> paquet.mélanger() 
>>> print(paquet)
Le paquet contient les cartes :
3♦️ 10♥ D♥ 4♥ 9♠️ 3♥ As♠️ 8♠️ 4♦️ 6♣️ R♥ V♥ V♠️ 2♥ 5♣️ 8♣️ 9♣️ D♦️ V♣️ 6♦️ 3♠️ 7♥ D♣️ 3♣️ R♠️ 7♣️ 2♣️ 6♥ 2♠️ As♣️ 2♦️ 5♠️ V♦️ 5♦️ 7♦️ 8♥ 6♠️ 7♠️ 9♥ 8♦️ 9♦️ 10♣️ R♣️ R♦️ As♦️ As♥ 4♠️ 5♥ 4♣️ 10♦️ D♠️ 10♠️
>>> carte = paquet.tirer_carte()
>>> print(carte)
10♠️
>>> len(paquet)
51
>>> paquet.ajouter_carte_dessous(carte)
>>> len(paquet)
52
>>> paquet1, paquet2 = couper(paquet)
>>> print(paquet1)
Le paquet contient les cartes :
10♠️ 3♦️ 10♥ D♥ 4♥ 9♠️ 3♥ As♠️ 8♠️ 4♦️ 6♣️ R♥ V♥ V♠️ 2♥ 5♣️ 8♣️ 9♣️ D♦️ V♣️ 6♦️ 3♠️ 7♥ D♣️ 3♣️ R♠️
```

Implémenter les classes (attributs, méthodes) et les fonctions pertinentes pour aboutir à ces fonctionnalités.





<!-- 
=== "Un jeu similaire à agar.io"
    L'objectif de ce projet est de créer une version simplifiée du jeu [agar.io](https://agar.io/) en utilisant Python et Pygame. Le joueur contrôle une cellule circulaire avec les touches directionnelles pour absorber les cellules plus petites tout en évitant les cellules plus grandes. Vous pouvez utiliser des objets pour représenter ces cellules par exemple. On se propose initialement de créer des cellules ennemies fixes de différentes tailles.

    [:fontawesome-solid-link: La documentation Pygame](https://www.pygame.org/docs/)

    ```py title="Un code minimal introductif à Pygame"
    import pygame

    # Initialisation de Pygame
    pygame.init()
    fenêtre = pygame.display.set_mode((1280, 720))  # création d'une nouvelle fenêtre
    pygame.display.set_caption("Mon super programme")  # titre de la fenêtre


    # Boucle principale du jeu
    continuer = True
    while continuer:
        
        # Gestion des événements (touche clavier pressée, clic de souris etc.)
        for événement in pygame.event.get():
            if événement.type == pygame.QUIT:  # lorsque l'utilisateur ferme la fenêtre
                continuer = False
        
        # Dessin (draw)
        fenêtre.fill("#21222c")  # efface l'écran (fill = remplir)
        pygame.draw.circle(fenêtre, "#f3bc3e", (320, 240), 10) # dessine un disque
        pygame.display.flip()  # mise à jour de l'affichage
        

    # Sortie
    pygame.quit()
    ```

=== "Combat Pokémon"
    L'objectif de ce projet est de créer une version très simplifiée du jeu de combat au tour par tour Pokémon. 

    * Un pokémon a un nom, un type, un niveau, un nombre de PV, une statistique d'attaque et de défense, et un ensemble de 4 capacités.

    * Une capacité possède une puissance de base, un type et un pourcentage d'échec critique.

    * La formule suivante permet de déterminer le nombre de PV perdus :
        $$
            \texttt{PV}_\text{perdus} = \left\lfloor \left( \left\lfloor 0.02 \times \frac{\left\lfloor \texttt{Niv} \times 0.4 +2 \right\rfloor \times \texttt{Att} \times \texttt{Pui}}{\texttt{Déf}} \right\rfloor + 2 \right) \times \texttt{CM} \right\rfloor
        $$

        * $\texttt{Niv}$ (resp. $\texttt{Att}$) est le niveau (resp. attaque) du Pokémon attaquant
        * $\texttt{Déf}$ est la défense du Pokémon attaqué
        * $\texttt{Pui}$ est la puissance de base de la capacité utilisée
        * $\texttt{CM}$ est un coefficient multiplicateur qui résulte de la multiplication des paramètres suivants :
            * $\times 1.5$ si le Pokémon est du même type que la capacité qu'il lance 
            * $\times 1$ ou $\times 2$ ou $\times 0.5$ suivant l'efficacité du type de la capacité 
            * Un nombre généré aléatoirement compris entre 0.85 et 1
    * Un Pokémon adversaire est choisi aléatoirement et le joueur choisit un Pokémon parmi trois propositions. Le combat débute et se termine quand un des deux Pokémons est KO. Les combats sont au tour par tour, avec le joueur choisissant la capacité à lancer pour son Pokémon.


<!-- ## Compléments

??? note "Points clés de la POO non abordés"
    Curieusement, les concepts les plus importants de la POO ne seront pas abordés cette année, à savoir l'**héritage**, le **polymorphisme** et l'**encapsulation**. Les concepts abordés ici sont finalement plus ou moins transposables dans n'importe quel langage au paradigme impératif comme le C. 
 -->