import pandas as pd
import numpy as np
from character import Character

pd.set_option("display.max_rows", 20, "display.max_columns", 12, 'display.width', 150)

header = ["Round", "Order", "Character", "Event", "Attack", "Target", "isMajor", "isPC", "AC", "DC", "Damage", "Assist"]
datatype = {"Round":        "int",          # Combat Round
            "Order":        "int",          # Index within a round, used to handle multiple actions from same character
            "Character":    "string",       # Character Identifier String
            "Event":        "string",       # Event Identifier String (Attack|Heal|Death|Movement)
            "Attack":       "string",       # Attack Descriptive String (type accumulation)
            "Target":       "string",       # Character Identifier String
            "isMajor":      "bool",         # Defines character is important, in contrast to grunts and meat popsicles
            "isPC":         "bool",         # Defines character is a Player Character
            "AC":           "int",          # Adversarial AC roll
            "DC":           "int",          # Sympathetic DC Roll [leverage Attack Reference for threshold]
            "Damage":       "int",          # Damage Total (negative values represent healing)
            "Assist":       "string"}       # Character Identifier String (Can be a list)

xl = pd.ExcelFile("data/data.xlsx")

data = pd.DataFrame()

for sheet in xl.sheet_names:
    data = xl.parse(sheet)

# Set/Coerce Data Types
for column in header:
    print(column)

    if datatype[column] == "int":
        data[column] = pd.to_numeric(data[column], errors='coerce')
        data[column] = data[column].dropna().astype('int')

    if datatype[column] == "string":
        data[column] = data[column].dropna().astype('U').str.strip()

    if datatype[column] == "bool":
        data[column] = np.where(data[column] == 1, True, False)

print(data.dtypes)

# Filter and create character objects
characters = dict()
for ch in data['Character'].unique():
    characters[ch] = Character(ch, data.loc[data['Character'] == ch])

for ch in characters:
    characters[ch].calculate_statistics()
    print(characters[ch].df)

    # print(characters[ch].name)
    # print(characters[ch].damage_total)
    # print(characters[ch].damage_mean)
    # print(characters[ch].damage_median)
    # print(characters[ch].damage_mode)
    print("~~~")

#
# print(characters['Garrin'].df)