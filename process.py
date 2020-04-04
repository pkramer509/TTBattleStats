import pandas as pd
import numpy as np
import filters
from character import Character

pd.set_option("display.max_rows", 20, "display.max_columns", 12, 'display.width', 150)

header = ["Round", "Order", "Character", "Event", "Attack", "Target", "AC", "DC", "Damage", "Assist"]
datatype = {"Round":        "int",          # Combat Round
            "Order":        "int",          # Index within a round, used to handle multiple actions from same character
            "Character":    "string",       # Character Identifier String
            "Event":        "string",       # Event Identifier String (Attack|Heal|Death|Movement)
            "Attack":       "string",       # Attack Descriptive String (type accumulation)
            "Target":       "string",       # Character Identifier String (Can be a list)
            "AC":           "int",          # Adversarial AC roll
            "DC":           "int",          # Sympathetic DC Roll [leverage Attack Reference for threshold]
            "Damage":       "int",          # Damage Total (negative values represent healing)
            "Assist":       "string"}       # Character Identifier String (Can be a list)

data = pd.read_csv("data/Jan-23-2020.csv",
                   sep=",",
                   names=header,
                   encoding="utf-8")

# Drop the header row
data = data.drop(data.index[0])

# Set Data Types
for column in header:
    if datatype[column] == "int":
        data[column] = pd.to_numeric(data[column], errors='coerce')
        data[column] = data[column].dropna().astype('int32')

    if datatype[column] == "string":
        data[column] = data[column].dropna().astype('U').str.strip()

# Filter and create character objects
characters = dict()
for ch in data['Character'].unique():
    characters[ch] = Character(ch, data.loc[data['Character'] == ch])




for ch in characters:
    characters[ch].print_name()
    print(characters[ch].damage_total())
    print(characters[ch].damage_avg())
    print("~~~")

print(characters['Garrin'].df)

# def total_damage(df, character): df[df.Target.str.contains(character)].Damage.sum()
# print(data[data.Target.str.contains("Automaton")].Damage.sum())
# print(damage_total(data, "Automaton"))
# print(data[data.Target.str.contains("Zombie 1")].Damage.sum())
# print(damage_total(data, "Zombie 1"))
# print(data[data.AC != 0].AC.min())


# print(data)

