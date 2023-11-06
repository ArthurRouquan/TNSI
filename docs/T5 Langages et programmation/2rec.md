# Récursivité

!!! info "Liens Capytale"
    * Exercices : [:fontawesome-solid-link: Notebook Capytale d7ca-1776728](https://capytale2.ac-paris.fr/web/c/15b1-2136113)
    * Correction : Disponible plus tard !


## Synthèse

* Une fonction est dite **récursive** si elle s'appelle elle-même au cours de son exécution.

    ```py title="Exemple de fonction récursive"
    def factorielle(n):
        if n == 0:  # condition terminale
            return 1
        return n * factorielle(n - 1)  # factorielle s'appelle elle-même
    ```

* La **condition terminale**, située au début de toute fonction récursive, définit le cas de base et permet d'arrêter la chaîne des appels.

* Si un programme récursif peut se traduire dans un style impératif (avec de simples boucles) et inversement, aborder de manière récursive un problème est parfois plus facile. 

    <div style="display:flex; justify-content: center; align-items: center; gap: 10px;">

    ```py title="Style récursif"
    def factorielle(n):
        if n == 0:
            return 1
        return n * factorielle(n - 1)
    ```
    :fontawesome-solid-arrow-right-arrow-left:
    ```py title="Style impératif"
    def factorielle(n):
        produit = 1
        for facteur in range(1, n + 1):
            produit *= facteur
        return produit
    ```
    </div>

* On peut correspondre le concept de récursivité à celui de récurrence en mathématiques.



* Lorsque $f$ s'appelle elle-même, on parle de récursivité **directe**. Lorsque $f$ appelle $g$ qui appelle $f$, on parle de récursivité **indirecte**.


