import os,json

def cariurutan(cariid):
    with open('nomer_car.json', 'r',encoding='utf-8') as openfile: data = json.load(openfile)
    for mydatacar in data["result"]:
        if mydatacar["id"]==cariid:
            return mydatacar["urutan"]

sistem_operasi=os.name
while True:
    if sistem_operasi=="nt":os.system("cls")
    if sistem_operasi=="posix":os.system("clear")
    dir_list=os.listdir("cpm/cars/livery/")
    itrlivery=1
    listUrutan={}
    for idnya in dir_list:
        if "_" not in idnya:
            listUrutan[int(cariurutan(idnya))]=idnya
    listUrutan=dict(sorted(listUrutan.items()))
    for urutannya in listUrutan:
        print(f"{itrlivery}. {urutannya}\t\tCarID : {listUrutan[urutannya]}")
        itrlivery+=1
    print("\n  [ Urutan Livery yang tersedia ]")
    input("Enter to refresh")