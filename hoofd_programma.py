from mijn_pakket import *
from helper import onderstreep
print(speelgoed[0])
print(voeg_namen_samen("Jan", "Janssen"))

uitvoer = onderstreep("AANBIEDING")
uitvoer.append("Aardbeienijs emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")
print()
for el in uitvoer:
    print (el)
   
