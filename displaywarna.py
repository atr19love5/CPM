
from colr import color


def disp(nama):
    firsttime = True
    Vnama = nama.split("[")
    disps = Vnama[0]
    for x in Vnama:
        if firsttime == False:
            code1 = f"{x[0:2]}"
            code2 = f"{x[2:4]}"
            code3 = f"{x[4:6]}"
            code1 = (int(code1, 16))
            code2 = (int(code2, 16))
            code3 = (int(code3, 16))
            huruf = x[7:8]
            disps += color(huruf,
                           fore=(code1,
                                 code2,
                                 code3),
                           back=(0, 0, 0))
        if firsttime:
            firsttime = False

    disps += Vnama[len(Vnama)-1][8:len(Vnama[len(Vnama)-1])]
    return(disps)
