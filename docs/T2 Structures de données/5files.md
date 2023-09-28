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

## Implémentation

* Implémenter une file à partir d'un tableau dynamique (`#!py list`) comme conteneur sous-jacent (utiliser les méthodes `.insert` et `.pop`). Donner la complexité en temps des primitives.

* Implémenter une file à partir d'une liste doublement chaînée. Donner la complexité en temps des primitives.



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


## Exercices

* Paquet de cartes

* Implémenter une file statique à partir d'un tableau statique circulaire (à implémenter aussi).

* Implémentation d'une file avec deux piles.