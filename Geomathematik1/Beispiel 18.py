from lib2d.Circle import Circle
from lib2d.Point import Point
from lib2d.Line import Line
from lib.Angle import Angle, gon
from lib2d.Plot import Plot
from lib2d.Algorithms import HA1, HA2, Vorwärtsschnitt_Winkel

P1 = Point(5207864.64, -70178.81)
P2 = Point(5208032.30, -70021.36)

# unorientierte Richtungen
rN1P1 = gon(0)
rN1P2 = gon(54.593)
rN1N2 = gon(106.778)

rN2N1 = gon(0)
rN2P1 = gon(22.426)
rN2P2 = gon(71.204)

w1 = rN1P2 - rN1P1
w2 = rN1N2 - rN1P2
w3 = rN2P1 - rN2N1
w4 = rN2P2 - rN2P1
w5 = gon(200) - w2 - w3
w6 = gon(200) - w5
w7 = gon(200) - w4 - w6
w8 = gon(200) - w1 - w6

# sP1_P2 = P1.distance_to(P2)

# """
#   sP1_P2 / w4.sin() = sP2_N2 / w10.sin()
#   sP1_P2 / w1.sin() = sP1_N1 / w9.sin()
#   w9 + w10 = gon(200) - w5
# """


# Finde N1, N2

p = Plot(Point(5207600, -70200), Point(5208100, -69800))
p.add_point(P1, "P1")
p.add_point(P2, "P2")


for g in range(0, 200, 5):
    alpha = gon(g)
    gamma = w1
    beta = gon(200) - alpha - gamma
    if beta.rad < 0:
        continue

    N = Vorwärtsschnitt_Winkel(P1, P2, alpha, beta)
    p.add_point(N)

for g in range(0, 200, 5):
    alpha = gon(g)
    gamma = w4
    beta = gon(200) - alpha - gamma
    if beta.rad < 0:
        continue

    N = Vorwärtsschnitt_Winkel(P1, P2, alpha, beta)
    p.add_point(N)

p.save("Geomathematik1/Beispiel 18.png")
