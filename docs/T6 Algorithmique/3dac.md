# Diviser pour régner

!!! info "Liens Capytale"
    * TP Tri Fusion : [:fontawesome-solid-link: Notebook Capytale b99a-2247717](https://capytale2.ac-paris.fr/web/c/b99a-2247717)
    * Correction : Disponible plus tard !


## Synthèse

Une fonction `résoudre(problème)` qui applique la méthode « Diviser pour régner » se déroule suivant les étapes :

* **Cas de base** : Si le `problème` est trivial, le résoudre immédiatement et renvoyer sa solution.

* **Diviser** : Sinon, diviser le `problème` en plusieurs sous-problèmes indépendants.
  
* **Régner** : Résoudre ces sous-problèmes récursivement (c'est-à-dire appeler `résoudre` sur ces sous-problèmes).

* **Combiner** : Combiner les différentes solutions des sous-problèmes pour obtenir la solution au problème initial et la renvoyer. C'est usuellement l'étape la plus difficile à élaborer.

Par exemple, si l'on divise par deux le problème :

<figure markdown>
![](ressources/dac.png#only-light)
![](ressources/dac-dark.png#only-dark)
</figure>

Déterminer la solution d'un sous-problème s'effectue récursivement :

<figure markdown>
![](ressources/dac-calls.png#only-light)
![](ressources/dac-calls-dark.png#only-dark)
</figure>

Une fois les feuilles de l'arbre atteint (les cas de base), les solutions se propagent des feuilles à la racine grâce à l'étape combiner.