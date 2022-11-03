nama="budi"
disp=[
["T","#00ffff"],
["i","#00ff00"],
["K","#ffff00"],
]
def plitcolornama(nama):
    disp=[]
    xcx=nama.split("[")
    if len(xcx)==1:
        return [[nama,"#ffffff"]]
    xcx.pop(0)
    kolorkode="#ffffff"
    for rer in xcx:
        try:
            if rer[6]=="]":
                disp.append([rer[7:len(rer)],f"#{rer[0:6]}"])
                # print(f"code #{rer[0:6]} tex {rer[7:len(rer)]}")
            else:
                disp.append([rer,kolorkode])
                # print(f"{rer} {rer[6]}")
        except Exception as e:
            print(f"error : {rer}")
            # for p in nama:
            #     disp.append([p,kolorkode])
            pass
    return disp
def cekamanwarna(nama):
    #cek kode warna
    carikurung=nama.split("]")
    warnaaman=True
    for pk in range(len(carikurung)-1):
        try:
            # print(carikurung[pk][-7])
            if carikurung[pk][-7]!="[":
                warnaaman=False
        except IndexError:
            # print(carikurung[pk][1])
            warnaaman=False
            return warnaaman
    return warnaaman

print(cekamanwarna(nama))
print(plitcolornama("YT TopixSBSB"))