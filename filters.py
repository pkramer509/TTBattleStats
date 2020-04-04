def damage_total(df, character):
    return df[df.Target.str.contains(character)].Damage.sum()

def damage_avg(df, character):
    return df[df.Target.str.contains(character)].Damage.mean()
