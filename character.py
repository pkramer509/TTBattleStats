

class Character:
    def __init__(self, name, df):
        self.name = name
        self.df = df

    def print_name(self):
        print(self.name)

    def damage_total(self):
        return self.df.Damage.sum()

    def damage_mean(self):
        return self.df.Damage.mean()
