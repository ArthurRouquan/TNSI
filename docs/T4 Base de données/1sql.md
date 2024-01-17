# Le langage SQL

!!! info "Liens Capytale"
    * Requêtes SQL simples : [:fontawesome-solid-link: Notebook Capytale 162d-1816379](https://capytale2.ac-paris.fr/web/c/162d-1816379)
    * Les jointures : [:fontawesome-solid-link: Notebook Capytale 078b-2687034](https://capytale2.ac-paris.fr/web/c/078b-2687034)
    * Création et mise à jour de tables : [:fontawesome-solid-link: Notebook Capytale 7b83-2715803](https://capytale2.ac-paris.fr/web/c/7b83-2715803)
    * Un crime à SQL City 🕵️ : [:fontawesome-solid-link: Notebook Capytale 7351-2739806](https://capytale2.ac-paris.fr/web/c/7351-2739806)


## Synthèse SQL

* Récupérer des données d'une table :

    ```sql
    SELECT colonne, autre_colonne, ...
    FROM nom_table
    WHERE condition AND/OR autre_condition AND/OR ...
    ORDER BY colonne ASC/DESC
    ```

* Récupérer des données de plusieurs tables (jointure) :
  
    ```sql
    SELECT table1.colonne, table2.colonne, ...
    FROM table1
    JOIN table2 ON table1.id = table2.id
    JOIN table3 ON table2.id = table3.id
    ...
    WHERE condition(s)
    ORDER BY colonne ASC/DESC
    ```

* Ajouter une ligne :

    ```sql
    INSERT INTO nom_table
    VALUES (valeur1, valeur2, ...)
    ```

* Mettre à jour une ou des lignes :

    ```sql
    UPDATE nom_table
    SET colonne = valeur_ou_expression, 
        autre_colonne = valeur_ou_expression, 
        ...
    WHERE condition(s)
    ```

* Supprimer une ou des lignes :

    ```sql
    DELETE FROM nom_table
    WHERE condition(s)
    ```