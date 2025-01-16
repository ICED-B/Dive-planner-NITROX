# Dive-planner-NITROX
My versions of dive planners

Popis aplikace:
Celá aplikace je určena pro ponory s kyslíkem a nitroxové směsi s obsahem kyslíku 32%, 34%, 36% a 40%.
V levé části zadáváte hlavní údaje pro ponor a to minutovou spotřebu, objem lahve, max hloubku a čas v této hloubce.
Uprostřed se po vykreslení grafu zobrazí ponor v grafické podobě a v případě že čas na dně dosáhne určitých hodnot budete muset dodržet dekompresní zastávky které jsou zahrnuty v grafu.
Na pravé části se zobrazí číselné hodnoty pro dekompresní zastávky a Spotřeba v Barech číselně znázorňuje ze zadaných informací Bary které by jste spotřebovali za váš ponor.
Ponory by měly být naplánovány tak aby se začalo v největší hloubce a pak se stoupalo napovrch.
Aplikace muže vykazovat chyby u dekompresních zastávek při zadání více ponorů na jednou.


Základní informace:

Maximální hloubka pro kyslík:

    (parciální tlak / (procenta kyslíku / 100) -1) *10 = matry určující max deep
    (1.5 / (21 / 100) - 1) * 10 = 61.4 [m]
    (1.5 / (32 / 100) - 1) * 10 = 36.87 [m]
    (1.5 / (34 / 100) - 1) * 10 = 34.1 [m]
    (1.5 / (36 / 100) - 1) * 10 = 31.67 [m]
    (1.5 / (40 / 100) - 1) * 10 = 27.5 [m]

Tlak na hladině:

    1 bar = 0.1 MPa.
    Tlak narůstá o 0.01 MPa na každý metr hloubky:
        V 10 m = 2 bary (0.2 MPa).
        V 20 m = 3 bary (0.3 MPa).
        V 30 m = 4 bary (0.4 MPa).

Objem vzduchu v lahvi:

    Tlakové lahve jsou rozděleny na Objem v litrech z pravidla 18, 15, 12, 10, 7 a 5. Naplněny jsou na tlak mezi 230 - 200 Barů.
    10litrová láhev při tlaku 200 barů obsahuje 2000 litrů vzduchu při normálním atmosférickém tlaku (1 bar).

Spotřeba vzduchu:

    Na hladině: 30 l/min → 2000 l / 30 l/min = 66.7 minut.
    V hloubce spotřeba roste úměrně tlaku:
        V 10 m (2 bary): 60 l/min → 33.3 minut.
        V 20 m (3 bary): 90 l/min → 22.22 minut.
        V 30 m (4 bary): 120 l/min → 16.66 minut.

