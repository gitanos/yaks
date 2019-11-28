from yak import Yak


class Herd:
    def __init__(self, yak_list):
        self._yaks = [Yak(**vals) for vals in yak_list]

    def __len__(self):
        return len(self._yaks)

    def __getitem__(self, position):
        return self._yaks[position]

    def get_stock(self, T):
        print('Herd: ')

        tot_milk = 0
        tot_wool = 0
        for yak in self._yaks:
            m, w = yak(T)
            tot_milk += m
            tot_wool += w

        print('In stock: ')
        print('    {0:0.3f} liters of milk'.format(tot_milk))
        print('    {} skins of wool'.format(tot_wool))
