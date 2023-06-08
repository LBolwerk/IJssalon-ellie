from itertools import count
from typing import ItemsView
from algemene_functies import mijn_functie_2



def aanbieding_1(smaak,prijs,korting):
    korting = prijs * (1 - korting)
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak",smaak,"van",prijs,"euro voor",korting,"euro.")


def inkomsten_totaal(inkomsten):
    inkomsten = sum(inkomsten)
    btw = inkomsten * 0.09
    print (f"Het totaal van alle inkomsten van deze week is",inkomsten,"euro, waarover",btw,"euro btw betaald dient te worden.")

def gemiddelde(mijn_lijst):
    mijn_lijst = sum(mijn_lijst)/7
    print (f"De gemiddelde inkomsten deze week zijn",mijn_lijst,"euro.")


def laag_en_hoog(mijn_lijst):
    mijn_lijst = max(mijn_lijst), min(mijn_lijst)
    return mijn_lijst


def meervoudig(invoer_lijst):
    invoer_lijst = laag_en_hoog(invoer_lijst)
    return invoer_lijst

def combinatie(invoer_lijst_2):
    invoer_lijst_2 = meervoudig(invoer_lijst_2)
    return invoer_lijst_2

korte_lijst = combinatie([1, 2, 3, 4, 5])
print(mijn_functie_2(korte_lijst[0], korte_lijst[1]))
