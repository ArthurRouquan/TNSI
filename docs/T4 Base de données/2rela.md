# Le modèle relationnel

## Introduction et histoire

## Définition et exemple

On considère la table suivante :

<figure markdown>
|         Titre          |    Auteur     | Année | Note |      ISBN      |
| :--------------------: | :-----------: | :---: | :--: | :------------: |
|          1984          | George Orwell | 1949  | 8.3  | 978-2070368228 |
|          Dune          | Frank Herbert | 1965  | 8.1  | 978-2221249482 |
|       Fondation        | Isaac Asimov  | 1951  | 8.1  | 978-2070415700 |
| Le Meilleur des mondes | Aldous Huxley | 1931  | 7.6  | 978-2266128568 |
|     Fahrenheit 451     | Ray Bradbury  | 1953  | 7.7  | 978-1451673319 |
<figcaption style="font-style: normal">Table <code>Livres</code></figcaption>
</figure>

* Le modèle relationnel sépare les données dans plusieurs **tables** appelées **relations**.
   > `Livres` est une relation.

* Le nom d'une colonne d'une relation est appelé **attribut**.
   > `Titre` est un attribut de la relation `Livres`.

* Le **domaine** d'un attribut correspond à un ensemble de valeurs admissibles : il correspond généralement à son **type**. 
   > L'attribut `Note` de type `Float` a comme domaine l'ensemble des réels compris entre 0 et 10.

* Une ligne d'une relation est appelé **élément**, **enregistrement**, **entité** ou **n-uplet**. 
   > Dans la relation `Livres`, `("1984", "George Orwell", 1949, 8.3, "978-2070368228")` est un élément / enregistrement / entité / n-uplet. 

* Le nombre d'entités d'une relation `R` est appelé **cardinal**, noté `#R`.
   > `#Livres` = 5.

* Le **schéma d'une relation** est l'ensemble *ordonné* de ses attributs sous la forme suivante :
   > <code>Livres(Titre: String, Auteur: String, Année: Int, Note: Float, ISBN: String)</code>

* Lorsqu'une base de données contient plusieurs relations, l'ensemble des schémas des relations constitue le **schéma relationnel** de la base de données.

## :fontawesome-solid-key: Clés primaires et étrangères

Les clés primaires et étrangères sert à établir des relations entres les différentes tables.

* Une **clé primaire** est un attribut dont la valeur permet d'identifier de manière **unique** une entité. Dans le schéma d'une relation, l'attribut qui correspond à la clé primaire est souligné.
   > <code>Livres(Titre: String, Auteur: String, Année: Int, Note: Float, <span class="underline">ISBN: String</span>)</code>

    Si on ne dispose pas d'attribut pouvant servir de clé primaire, il est courant d'ajouter un numéro d'identifiant `id` comme clé primaire.

* Une **clé étrangère** (ou secondaire) est un attribut qui fait référence à une clé primaire d'une autre relation. Dans le schéma d'une relation, l'attribut qui correspond à une clé étrangère est précédé d'un `#` ou souligné en pointillé.
   > <code>Emprunt(<span class="underline">#ISBN: String</span>, #id_client: Int, retour: Date)</code>
   >
   > Une clé étrangère peut aussi être une clé primaire !


## Contraintes d'intégrité

Les trois contraintes d'intégrité assurent la **cohérence** des données :

* **Contrainte de relation** : chaque entité est identifiée de manière unique à l'aide d'une clé primaire.

* **Contrainte de domaine** : les valeurs d'un attribut sont restreintes à un domaine prédéfini de valeurs.

* **Contrainte de référence** : la valeur d’une clé étrangère doit toujours être également une des valeurs de la clé référencée.

## Normalisation

En plus des contraintes d'intégrité, lors de sa conception, une base de données doit respecter certains principes afin de prévenir l’apparition d'anomalies : on parle de **normalisation** de la base de données. Parmi ces principes :

   * Principe de **non-redondance** des données : les données ne doivent pas apparaître plusieurs fois.

   * Principe d'**atomicité** des données : les données doivent être insécables (pas de tableaux par exemple).