from jarat import BelfoldiJarat, NemzetkoziJarat
from legitarsasag import LegiTarsasag
from jegyfoglalas import JegyFoglalas

def betolt_adatok():
    legitarsasag = LegiTarsasag("SkyAir")

    j1 = BelfoldiJarat("B101", "Budapest", 12000)
    j2 = NemzetkoziJarat("N202", "London", 45000)
    j3 = NemzetkoziJarat("N303", "Párizs", 47000)

    legitarsasag.jarat_hozzaad(j1)
    legitarsasag.jarat_hozzaad(j2)
    legitarsasag.jarat_hozzaad(j3)

    foglalasok = [
        JegyFoglalas("Anna", j1),
        JegyFoglalas("Béla", j2),
        JegyFoglalas("Cecília", j3),
        JegyFoglalas("Dénes", j1),
        JegyFoglalas("Eszter", j2),
        JegyFoglalas("Ferenc", j3),
    ]

    return legitarsasag, foglalasok
