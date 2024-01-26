# Programmation Dynamique

## Définition générale

La <span class=h>programmation dynamique</span> est une stratégie algorithmique de résolution optimale d'un problème d'optimisation. Cette stratégie repose sur deux grands principes :

* <span class=h>:fontawesome-solid-sitemap: Décomposition</span> : Le problème est décomposé en sous-problèmes plus petits par une définition récursive.

* <span class=h>:fontawesome-solid-box-archive: Mémoïsation</span> : Lorsqu'un sous-problème est résolu, afin d'éviter de le rerésoudre si celui-ci se présente à nouveau ultérieurement, le coût de sa solution est conservé.


La résolution d'un problème d'optimisation repose souvent sur une série de <span class=h>choix</span> successifs. Un choix guide la transition d'un <span class=h>état</span> à un autre. Un état étant l'ensemble des informations qui caractérisent totalement la situation au moment d'effectuer un choix.

La définition récursive du problème se manifeste à travers la **fonction d'état**. Cette fonction récursive exprime le coût optimal d'un état donné en fonction des coûts optimaux des états qui le suivent dans la séquence de décision.



<!-- 

## Exemple introductif

Afin de mettre en lumière les différentes étapes à suivre pour appliquer cette stratégie à un problème quelconque, étudions le problème du rendu de monnaie.

!!! note "Problème du rendu de monnaie"
    Vous devez rendre une somme $S$ d'argent à un vendeur. Pour cela, vous disposez d'une quantité illimitée de pièces de différentes valeurs $V = \left\{ v_1,~ v_2,~ \ldots~ ,~ v_n \right\}$. Votre objectif est de rembourser cette somme en utilisant le moins de pièces possible.

1. Définir les **données** fixes du problème. Ce sont les paramètres qui définissent entièrement une instance du problème.

    > * Somme $S \in \mathbb{N}$ à rendre.
    * Les différentes valeurs de pièces $V = \left\{ v_1,~ v_2,~ \ldots~ ,~ v_n \right\}$.

2. Identifier une succession de **choix** à effectuer.
   
    > Ici, à chaque étape, je choisie une pièce d'une valeur particulière à rendre. 

3. Définir les variables qui caractérisent totalement l'**état** d'une étape de décision (au moment où un choix est effectué). Que modifie un choix lors de ma prochaine prise de décision ?
   
    > Lorsque que je choisie une pièce de valeur $v$ et la rend, la somme à rendre se retrouve soustrait de $v$. Donc l'état d'une étape est caractérisé par une somme $s$ à rendre.

 -->

<!-- Soit un problème d'optimisation. La programmation dynamique s'applique de manière générale en suivant les étapes :

1. Définir les **données** fixes.
2. Définir l'**objectif** du problème, c'est-à-dire la quantité que l'on souhaite maximiser ou minimiser.
3. Identifier une succession de **choix** à effectuer.
4. Définir les variables qui définissent totalement l'état lors d'une étape de décision.
5. Écrire la **fonction d'état**. -->









<!-- 

## Fibonacci

La suite de Fibonnaci :

\begin{equation}
f(n) = \begin{cases}
f(n-1) + f(n-2) & \text{si } n \geq 1 \\
n & \text{sinon}
\end{cases}
\end{equation}

=== "Récursif"
    La définition naïve et récursive.
    ```py
    def fibonacci(n):
        if n <= 1:  # cas de base
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    ```
    La complexité en temps de cet algorithme est exponentielle, plus précisement $\Theta(\varphi^n)$ où $\varphi \approx 1.6180$ est le nombre d'or. L'arbre des appels de la fonction :

    ![type:video](./ressources/fibonacci-light.mp4){: style='width: 100%'}

    On remarque des calculs redondants, par exemple $f(3)$ est calculé 2 fois lors de l'appel $f(5)$.


=== "Récursif & Cache"
    On cache les différents termes de la suite de Fibonacci pour éviter des calculs redondants, c'est le principe de **mémoïsation**.
    ```py
    def fibonacci_dp(n):
        def fibonacci_cache(n):
            if cache[n] is None:  # si le n-ième terme n'a pas été calculé
                cache[n] = fibonacci_cache(n - 1) + fibonacci_cache(n - 2)
            return cache[n]

        cache = [0, 1] + [None] * (n - 1)  # les deux premiers termes inclus
        return fibonacci_cache(n)
    ```
=== "Itératif & Cache"
    Une approche *ascendante* (bottom-up) permet de remplir le cache de manière itérative.
    ```py
    def fibonacci_dp_ascendant(n):
        cache = [0, 1] + [None] * (n - 1)
        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]
    ```
=== "Itératif"
    Finalement, il est suffisant de retenir les deux derniers termes.
    ```py
    def fibonacci_dp_ascendant_optimise(n):
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b if n >= 2 else n
    ```
=== "Comparaison"
    Des mesures réelles permettent bien de démontrer que l'ajout d'un cache permet d'obtenir un algorithme de complexité linéaire.

    <figure markdown>
    ![](ressources/fibonacci-dark.svg#only-dark)
    ![](ressources/fibonacci-light.svg#only-light)
    </figure>

=== "Formule exacte"
    Il existe une formule exacte de la suite de Fibonacci, la formule de Binet :

    $$
    f(n) = \frac{\varphi^n - \varphi^{\prime n}  }{\sqrt{5}} \quad \text{avec} \quad \varphi = \frac{1 + \sqrt{5}}{2} \quad \text{et} \quad \varphi^\prime = \frac{1 - \sqrt{5}}{2} = - \frac{1}{\varphi}
    $$

    Où $\varphi$ est le fameux nombre d'or. Il serait alors tentant de calculer le $n$-ième terme de la suite de Fibonacci en temps constant :

    ```py
    import math

    def fibonacci_binet(n):
        p1 = (1 + math.sqrt(5)) / 2
        p2 = (1 - math.sqrt(5)) / 2
        résultat = (math.pow(p1, n) - math.pow(p2, n)) / math.sqrt(5)
        return int(résultat)
    ```

    Or, travailler avec des nombres en virgule flottante implique inévitablement des imprécisions de calcul. Par conséquent, à partir de $n = 72$, les termes calculés se révèlent incorrects :
    <center>

    | $n$ |     $f(n)$      |                                                 `fibonacci_binet(n)`                                                 |
    | :-: | :-------------: | :------------------------------------------------------------------------------------------------------------------: |
    | 70  | 190392490709135 |                                                   190392490709135                                                    |
    | 71  | 308061521170129 |                                                   308061521170129                                                    |
    | 72  | 498454011879264 | <span style="background-color: rgba(213, 42, 42, 0.5); padding: 0px 5px; border-radius: 5px;">498454011879265</span> |
    | 73  | 806515533049393 | <span style="background-color: rgba(213, 42, 42, 0.5); padding: 0px 5px; border-radius: 5px;">806515533049395</span> |</center>



## Rendu de monnaie

* Données du problème : Une somme initiale à rendre $V$ et un système de pièces $P = (p_1,~ p_2,~ \ldots,~ p_n)$.

* L'état d'un problème : Une somme restante à rendre $v$.

* Choix à partir d'un état : Choisir une pièce $p \in P$.

* Pour une somme $v$ à rendre, on définit $f(v)$ comme le nombre de pièces minimal à rendre. Définition récursive de la fonction d'état $f$ :

    $$
    f(v) = 1 + \min \bigg\{  f(v - p) ~\bigg|~ p \in P \bigg\}
    $$

    * Cas de bases de la fonction d'état :
        * $f(0) = 0$
        * $f(v) = \infty \text{ si } v < 0$

    * Solution au problème initial : $f(V)$

## Sac-à-dos

* Données du problème : Un ensemble d'objets $I$ où objet $i \in I$ est caractérisé par un poids $p_i$ et une valeur $v_i$. Et un sac avec une capacité $C$.

* L'état d'un problème : Une capacité restante $c$. Et un indice $i$ qui indique que l'objet considéré

* Choix à partir d'un état : Ajouter l'objet au sac ou l'ignorer.

* Fonction d'état $f$ :

    $$
    f(c, i) = \max \bigg\{  v_i + f(c - p_i, i - 1), f(c, i - 1) \bigg\}
    $$
 -->
