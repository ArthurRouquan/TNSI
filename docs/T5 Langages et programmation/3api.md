# Modularité et API

## Objectifs

 * Utiliser des API ou des bibliothèques.

* Exploiter leur documentation.

* Créer des modules simples et les documenter.

## Définition de modularité

La **modularité** en programmation se réfère à la décomposition d'un programme en modules autonomes et interdépendants. Un module est une unité logique qui regroupe des fonctionnalités spécifiques. Cette approche facilite la gestion, la maintenance, et la réutilisation du code.

??? example "Le module `math`"
    Le module `math` est un excellent exemple de modularité. Il regroupe un ensemble de fonctions mathématiques standards, telles que les fonctions trigonométriques, logarithmiques, etc. Les développeurs peuvent l'importer et l'utiliser dans leurs programmes, profitant ainsi des fonctionnalités prêtes à l'emploi sans avoir à réinventer la roue.

    === "Import complet"
        ```py
        import math

        print(math.sqrt(25)) 
        print(math.sin(math.pi))
        ```

        Toutes les fonctions du module `math` sont importées, et elles sont accessibles dans un namespace spécifique. Les fonctions sont appelées en les préfixant par le nom du module, c'est-à-dire `math`.

    === "Import complet avec alias"
        ```py
        import math as m

        print(m.sqrt(25)) 
        print(m.sin(m.pi))
        ```

        Similaire à l'import complet, mais les fonctions du module sont appelées en les préfixant par l'alias du module, ici `m`.

    === "Import partiel dans le namespace courant"
        ```py
        from math import sqrt, sin

        print(sqrt(25)) 
        print(sin(pi))
        ```

        Seules les fonctions `sqrt` et `sin` sont importées, directement dans le namespace principal du fichier effectuant l'import. Les autres fonctions du module `math` ne sont pas accessibles, comme `cos` par exemple.


    === "Import complet dans le namespace courant"
        ```py
        from math import *

        print(sqrt(25)) 
        print(sin(pi))
        print(cos(pi))
        ```

        En informatique, `*` signifie souvent « tout ». Toutes les fonctions sont importées directement dans l'espace de nom principal du fichier effectuant l'import. Cependant, cette méthode d'importation peut entraîner des conflits (fonctions ayant le même nom), il convient donc de l'utiliser avec précaution.




## Votre premier module

### Un exemple

Dans un script Python `mon_module.py`, on définit les fonctions suivantes :

```py title="mon_module.py"
def celsius_vers_fahrenheit(T_celsius: float) -> float:
    """
    Convertit une température degrés Celsius en degrés Fahrenheit.

    Paramètres :
    - T_celsius (float) : Température en degrés Celsius à convertir.

    Retourne :
    - float : Température convertie en degrés Fahrenheit.
    """
    return T_celsius * 9 / 5 + 32


def fahrenheit_vers_celsius(T_fahrenheit: float) -> float:
    """
    Convertit une température degrés Fahrenheit en degrés Celsius.

    Paramètres :
    - T_fahrenheit (float) : Température en degrés Fahrenheit à convertir.

    Retourne :
    - float : Température convertie en degrés Celsius.
    """
    return (T_fahrenheit - 32) * 5 / 9
```

Dans un second script Python `test.py` crée dans le même répertoire, on pourra alors importer les fonctions de ce module grâce à `#!py import nom_du_module` :

```py title="test.py"
import mon_module

print(mon_module.celsius_vers_fahrenheit(42.0))
print(mon_module.fahrenheit_vers_celsius(50.0))
```

```pycon title="Sortie"
107.6
10.0
```

### Exercice - L'art de la guerre

Créer un module `polynome2` qui définit une classe `Polynome2` représentant un polynôme du second degré. Un objet de cette classe possédera trois attributs `a`, `b` et `c`, à savoir les trois coefficients réels du polynôme $ax^2 + bx + c$. Implémenter les méthodes suivantes :

* `#!py évaluer(self, x: float) -> float` qui évalue le polynôme à un `x` spécifique.

* `#!py discriminant(self) -> float` qui renvoie le discriminant $\Delta$ du polynôme. Pour rappel :

    $$
    \Delta = b^2 - 4ac
    $$

* `#!py racines(self) -> tuple[float, float]` qui renvoie les deux racines réelles du polynôme dans l'ordre croissant. Pour rappel :

    $$
    r_{1, 2} = \frac{-b \pm \sqrt \Delta}{2a}
    $$

    Les racines sont les valeurs $x$ telles que $ax^2 + bx + c = 0$. La méthode renvoie `None` s'il n'existe pas de racines réelles, c'est-à-dire lorsque le discriminant du polynôme est négatif.

* `#!py extremum(self)` qui renvoie le maximum (respectivement minimum) du polynôme si $a > 0$ (resp. $a < 0$). Renvoie `None` si $a = 0$. Pour vous aider :

<center>
![](ressources/max-light.png#only-light){ width="50%" }
![](ressources/max-dark.png#only-dark){ width="50%" }
</center>

* `#!py distance_racines(self) -> float` renvoie la distance absolue entre les deux racines.

N'oubliez pas de bien documenter vos méthodes !

Louis XIV souhaite utiliser votre nouveau module pour calculer la trajectoire de ses armes de jet sur le champ de bataille. Il vient vous voir avec les fonctions décrivant la trajectoire parabolique des projectiles de plusieurs armes :

<figure markdown>
| Arme      | Équation de la trajectoire |
| --------- | -------------------------- |
| Arc       | $−0.06x^2 + 20x + 1.6$     |
| Trébuchet | $−0.1x² + 70x + 1.0$       |
| Catapulte | $−0.05x² + 18x + 0.5$      |
| Fronde    | $−0.1x^2 + 5x + 1.8$       |</figure>

Dans un nouveau fichier Python `test_armes.py` importer votre module `polynome2` et calculer la portée et la flèche de chacune des armes :

<center>
![](ressources/fleche-light.png#only-light){ width="50%" }
![](ressources/fleche-dark.png#only-dark){ width="50%" }
</center>

## Définition d'une API

Une **API**, Application Programming Interface, est un moyen pour deux programmes informatiques ou plus de communiquer entre eux. Une API expose un ensemble normalisé de classes, de méthodes, de fonctions et de constantes qui sert de façade par laquelle un logiciel offre des services à d'autres logiciels. 

Typiquement les différentes méthodes de votre classe `polynome2` définissent une API !

## Une première API Web

On se propose d'utiliser l'API Web [OpenWeather](https://openweathermap.org/api) qui fournit des données météorologiques en temps réel et bien plus. Inscrivez-vous pour obtenir une **clé API** qui vous autorisera à utiliser cet API.

Sur le site, OpenWeather expose différents APIs, comme l'API [Geocoding](https://openweathermap.org/api/geocoding-api) qui permet de déterminer la latitude et longitude d'une ville. Pour appeler cette API en Python, on utilise le module `requests` pour effectuer une requête HTTP et le module `json` pour convertir les données reçues en un dictionnaire. Le module `pprint` permet d'afficher plus lisiblement des dictionnaires :

```py
import requests
import json
from pprint import pprint

API_KEY = 'd2902337c4a97a1d8fc513d7ab......'  # me demander le reste de la clé
city_name = 'Pons'

response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}')
data = json.loads(response.text)

pprint(data)
```

Finalement, tout se passe comme si on appelait une fonction d'un module extérieure, les différents paramètres sont passés directement dans l'URL.

!!! question "Exercice" 
    Écrire la fonction `coordonnées(ville: str) -> tuple[float, float]` qui renvoie la latitude et la longitude de ville `ville` donnée en paramètre. (note: `API_KEY` sera une variable globale)


## Le temps est bon, le ciel et bleu

Ce projet a pour but d'écrire le code Python qui affiche le bulletin météo des trois prochains jours de manière élégante d'une ville donnée :

```

     Bulletin météo de Pons en France

┃          Mercredi 6 Décembre 2023
┃
┃ • Température
┃     – Maximale             : 5.63  °C
┃     – Moyenne              : 2.93  °C
┃     – Minimale             : -2.03 °C
┃ • Humidité moyenne         : 89.8%
┃ • Vitesse moyenne du vent  : 8.68 km/h
┃ • Pression moyenne         : 1018.4 hPa


┃           Jeudi 7 Décembre 2023
┃
┃ • Température
┃     – Maximale             : 11    °C
┃     – Moyenne              : 6.28  °C
┃     – Minimale             : 3.36  °C
┃ • Humidité moyenne         : 84.75%
┃ • Vitesse moyenne du vent  : 18.49 km/h
┃ • Pression moyenne         : 1012.88 hPa


┃          Vendredi 8 Décembre 2023
┃
┃ • Température
┃     – Maximale             : 12.86 °C
┃     – Moyenne              : 10.46 °C
┃     – Minimale             : 9.35  °C
┃ • Humidité moyenne         : 85.75%
┃ • Vitesse moyenne du vent  : 14.58 km/h
┃ • Pression moyenne         : 1013.0 hPa
```

### Démarche et outils

* L'API [5 Day / 3 Hour Forecast](https://openweathermap.org/forecast5) dont la documentation en anglais sera à lire pour récupérer les données météorologiques sur les prochains jours. Il faudra ensuite filtrer ces données pour récupérer ce que l'on souhaite.

* Le module [`datetime`](https://docs.python.org/fr/3/library/datetime.html) qui permettra de manipuler facilement les dates.

* Pour arrondir des nombres, centrer du texte etc. on utilisera les [f-strings](http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf) de manière un peu plus avancée.


??? tip "Le module `datetime`"
    * La classe `datetime.date` permet de représenter une date (jour, mois, année) et de la manipuler facilement. Par exemple, `datetime.date.today()` renvoie la date actuelle sour la forme d'un objet de type `datetime.date` :
    
        ```py
        >>> import datetime
        >>> datetime.date.today()
        datetime.date(2023, 12, 11)
        >>> d = datetime.date(2024, 4, 6)  # 6 Avril 2024
        ```

    * La classe `datetime.timedelta` représente une durée, soit un écart entre deux objets de `datetime.date` :
        
        ```py
        >>> datetime.date(2023, 12, 25) + datetime.timedelta(days=1)
        datetime.date(2023, 12, 26)
        ```

    * Une instance de `datetime.date` se convertit en chaîne de caractères grâce à `date.strftime(format)` ou `format` est une chaîne de caractères qui représente la mise en forme souhaitée :

        ```py
        >>> d = datetime.date(2023, 12, 25)
        >>> d.strftime('%d / %m / %Y')
        '25 / 12 / 2023'
        ```

        Rendez-vous sur [ce lien](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) pour connaître tous les formatages possibles.

    * Pour que `date.strftime` « parle » français, il faudra spécifier la constante `LC_TIME` au début de votre programme :

        ```py
        import locale
        locale.setlocale(locale.LC_TIME, 'fr_FR')
        ```

    * La méthode `datetime.date.fromtimestamp` sera très utile pour récupérer la date depuis les données météorologiques.

??? tip "Formatage avancé"

    * Il est courant d'insérer des valeurs dans une chaîne de caractères en définissant une f-string :
    
        ```py
        >>> a = 42
        >>> f"La variable a contient la valeur {a} !"
        'La variable a contient la valeur 42 !'
        ```

    * On peut spécifier en plus d'autres paramètres, comme le nombre de chiffres après la virgule à afficher :

        ```py
        >>> a = 10.123456789
        >>> f"La variable a contient la valeur {a:.3} !"
        'La variable a contient la valeur 10.123 !'
        ```
    
    * Rendez-vous sur [ce lien](http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf) pour en savoir plus, surtout au niveau des alignements par exemple !


### Spécifications

* Le bulletin météo des 3 prochains jours (pas aujourd'hui).

* Pour chaque jour :

    * Afficher correctement la date comme dans l'exemple.

    * Donner la température maximale, moyenne et minimale en degré Celsius.

    * Donner l'humidité moyenne.

    * Donner la vitesse moyenne du vent en km/h.

    * Donner la pression moyenne en hPa.

* Décomposer votre programme en fonctions spécifiques et pertinentes pour rendre le code plus intelligible.
  
* Ne pas oublier les commentaires (pour chaque fonction) et d'utiliser des noms de variables pertinents.