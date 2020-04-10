

class Character:
    def __init__(self, name, df):
        self.name = name
        self.df = df
        self.damage_total = 0
        self.damage_mean = 0
        self.damage_median = 0
        self.damage_mode = 0

    def calculate_statistics(self):
        self.damage_total = self.df.Damage.sum()
        self.damage_mean = self.df.Damage.mean()
        self.damage_median = self.df.Damage.median()
        self.damage_mode = self.df.Damage.mode().max()
