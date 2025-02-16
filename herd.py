from yak import Yak


class Herd:
    def __init__(self, yak_list):
        self._yaks = [Yak(**vals) for vals in yak_list]

    def __len__(self):
        return len(self._yaks)

    def __getitem__(self, position):
        return self._yaks[position]

    def get_stock(self, T):

        tot_herd = []
        tot_milk = 0
        tot_wool = 0
        for yak in self._yaks:
            m, w, n, a, s = yak(T)
            tot_milk += m
            tot_wool += w
            tot_herd.append({"name": n, "age": a, "age-last-shaved": s})

        stock_dict = {
            "milk": tot_milk,
            "skins": tot_wool,
            "herd": tot_herd
        }

        return stock_dict
