import math


class Yak():

    def __init__(self, name, age):
        self.name = name
        self.age_yrs = float(age)
        self.milk = 0
        self.wool = 0
        self.next_shave = 0
        self.last_shave = None

    def __call__(self, T):

        for t in range(T):

            if self._is_alive():

                # Shepherd milks the Yak
                self.milk += self.get_milk_per_day(self.age_days)

                # Shepherd shaves
                if self._is_adult():
                    # check if it's shave day
                    shave_today = int(self.next_shave) == int(t)
                    if shave_today:
                        self.wool += 1
                        self.last_shave = self.age_yrs

                self.next_shave = self.get_wool_day(self.age_days)

                self.update_age()

        print('    Yak {0}, {1:0.2f} years old'.format(self.name, self.age_yrs))

        return (self.milk, self.wool, self.name, self.format_age(self.age_yrs), self.format_age(self.last_shave))

    def update_age(self):
        self.age_yrs += 0.01

    @staticmethod
    def format_age(num):
        return float('{0:0.2f}'.format(num))

    @staticmethod
    def get_milk_per_day(days):
        milk_val = 50 - (days * 0.03)
        return milk_val

    @staticmethod
    def get_wool_day(days):
        day_of_wool = 8 + (days * 0.01)
        return math.floor(day_of_wool) + 1

    def _is_alive(self):
        if self.age_yrs < 10.0:
            return True

    def _is_adult(self):
        if self.age_yrs > 1.0:
            return True

    @property
    def age_days(self):
        return self.age_yrs * 100
