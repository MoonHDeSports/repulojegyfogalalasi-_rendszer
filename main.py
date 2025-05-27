from adatbazis import betolt_adatok
from jegyfoglalas import JegyFoglalas

def main():
    legitarsasag, foglalasok = betolt_adatok()

    while True:
        print("\n1. Jegy foglalása\n2. Foglalás lemondása\n3. Foglalások listázása\n4. Kilépés")
        valasz = input("Válassz: ")

        if valasz == "1":
            utas_nev = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a járatszámot: ")
            jarat = legitarsasag.jarat_leker(jaratszam)
            if jarat:
                foglalasok.append(JegyFoglalas(utas_nev, jarat))
                print(f"Foglalás sikeres! Ár: {jarat.jegyar} Ft")
            else:
                print("Nincs ilyen járat.")

        elif valasz == "2":
            utas_nev = input("Add meg az utas nevét a lemondáshoz: ")
            siker = False
            for f in foglalasok:
                if f.utas_nev == utas_nev:
                    foglalasok.remove(f)
                    print("Foglalás lemondva.")
                    siker = True
                    break
            if not siker:
                print("Nem található ilyen foglalás.")

        elif valasz == "3":
            for f in foglalasok:
                print(f"{f.utas_nev} - {f.jarat.jaratszam} ({f.jarat.celallomas})")

        elif valasz == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
