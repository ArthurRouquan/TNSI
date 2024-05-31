from liste import *


class Test:
    def __init__(self) -> None:
        self.nb_tests = 0
        self.nb_tests_réussis = 0

    def évaluer(self, expression):
        self.nb_tests += 1
        try:
            résultat = eval(expression)
        except Exception as e:
            print("[ERREUR]", e)
            résultat = False

        if résultat:
            self.nb_tests_réussis += 1
            print("[OK] Test réussi :", expression)
        else:
            print("[FAIL] Test échoué :", expression)

    def conclusion(self):
        print(f"{self.nb_tests_réussis} / {self.nb_tests}")


test = Test()


l = créer_liste_depuis_tab([12, 15, 17])
vide = créer_liste_depuis_tab([])
test.évaluer("l.vers_tableau() == [12, 15, 17]")
test.évaluer("vide.vers_tableau() == []")
test.évaluer("l.n_ième_élément(2) == 17")
test.évaluer("l.n_ième_élément(0) == 12")


l2 = créer_liste_depuis_tab([887, 998])
test.évaluer("concaténer_listes(l, l2).vers_tableau() == [12, 15, 17, 887, 998]")
test.évaluer("concaténer_listes(vide, vide).vers_tableau() == []")
test.évaluer("concaténer_listes(vide, l2).vers_tableau() == [887, 998]")
l = créer_liste_depuis_tab([12, 15, 17])
test.évaluer("concaténer_listes(l, vide).vers_tableau() == [12, 15, 17]")


l.renverser()
test.évaluer("l.vers_tableau() == [17, 15, 12]")
vide.renverser()
test.évaluer("vide.vers_tableau() == []")


l = créer_liste_depuis_tab([12, 15, 17, 45])
l.insérer(999, 2)
test.évaluer("l.vers_tableau() == [12, 15, 999, 17, 45]")
l.insérer(-999, 0)
test.évaluer("l.vers_tableau() == [-999, 12, 15, 999, 17, 45]")


l = créer_liste_depuis_tab([12, 15, 17, 45])
l.retirer(2)
test.évaluer("l.vers_tableau() == [12, 15, 45]")
l.retirer(0)
test.évaluer("l.vers_tableau() == [15, 45]")


l = créer_liste_depuis_tab([12, 35, 12, 42, 12, 35])
test.évaluer("l.occurrences(12) == 3")
test.évaluer("vide.occurrences(12) == 0")


print(test.conclusion())
