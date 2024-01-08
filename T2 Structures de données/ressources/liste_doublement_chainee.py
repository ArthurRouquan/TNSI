
class ChaînonDoublementChainée:
    """ Représente un chaînon dans une liste doublement chaînée. """

    def __init__(self, élément, suivant, précédent) -> None:
        self.élément = élément
        self.suivant = suivant
        self.précédent = précédent


class ListeDoublementChainée:
    """ Représente une liste doublement chaînée. """

    def __init__(self) -> None:
        """ Initialise une liste doublement chaînée vide en O(1). """
        self.tête = None
        self.queue = None
        self.taille = 0

    def __len__(self) -> int:
        """ Renvoie le nombre d'élément dans la liste en O(1). """
        return self.taille

    def est_vide(self) -> bool:
        return len(self) == 0

    def insérer_devant(self, élément) -> None:
        """ Insère un élément à la tête de la liste en O(1). """
        chaînon = ChaînonDoublementChainée(élément, self.tête, None)
        if self.est_vide():
            self.queue = chaînon
        else:
            self.tête.précédent = chaînon
        self.tête = chaînon
        self.taille += 1

    def premier_élément(self):
        """ Renvoie le premier élément de la liste en O(1). """
        return None if self.est_vide() else self.tête.élément

    def dernier_élément(self):
        """ Renvoie le dernier élément de la liste en O(1). """
        return None if self.est_vide() else self.queue.élément

    def retirer_queue(self) -> None:
        """ Supprime le dernier élément de la liste en O(1). """
        if self.est_vide():
            return
        elif len(self) == 1:
            self.tête = None
        else:
            self.queue.précédent.suivant = None
        self.queue = self.queue.précédent
        self.taille -= 1

    def vers_tableau(self) -> list:
        """ Retourne les éléments de la liste dans un tableau en O(n). """
        éléments = []
        courant = self.tête
        while courant != None:
            éléments.append(courant.élément)
            courant = courant.suivant
        return éléments

    def __repr__(self) -> str:
        return '[' + ' ↔ '.join(map(str, self.vers_tableau())) + ']'


# l = ListeDoublementChainée()
# l.insérer_devant(17)
# l.insérer_devant(54)
# l.insérer_devant(25)
# print(l)
# l.retirer_queue()
# print(l)
# l.retirer_queue()
# print(l)
# print(l.dernier_élément())
# print(l.premier_élément())
# l.retirer_queue()
# print(l)
# print(l.dernier_élément())
# print(l.premier_élément())
# l.retirer_queue()
# print(l)
# l.insérer_devant(17)
# l.insérer_devant(54)
# l.insérer_devant(25)
# l.insérer_devant(25)
# l.insérer_devant(200)
# print(l)
# print(l.dernier_élément())
# print(l.premier_élément())
