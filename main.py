import os,json,random,shutil,time,sys
import cpm as cpm


def tes():
    pass
# while True:
#     tes()
#     input()
# exit()


def randomcolorname(nama):
    chars = '0123456789ABCDEF'
    generatecolor=[''.join(random.sample(chars,6)) for i in range(len(nama))]
    resultname=""
    for i in range(len(nama)):
        resultname+=f"[{generatecolor[i]}]{nama[i:i+1]}"
    return resultname
def cariid(urutan):
    with open('nomer_car.json', 'r',encoding='utf-8') as openfile: data = json.load(openfile)
    for mydatacar in data["result"]:
        if mydatacar["urutan"]==urutan:
            return mydatacar["id"]
def cariurutan(cariid):
    with open('nomer_car.json', 'r',encoding='utf-8') as openfile: data = json.load(openfile)
    for mydatacar in data["result"]:
        if mydatacar["id"]==cariid:
            return mydatacar["urutan"]


def cekdatalivery(carid):
    path = "cpm/cars/livery/"
    dir_list = os.listdir(path)
    dir_list=sorted(dir_list, key=len, reverse=False)
    if str(carid) in dir_list:
        return True
    else:return False

def savewscar(carid,data):
    datacarname=str(carid)
    itrliverydata=1
    while True:
        print(datacarname)
        if cekdatalivery(datacarname)==False:
            break
        else:
            datacarname=f"{carid}_"+str(itrliverydata)
            itrliverydata+=1
                
        time.sleep(1)
    print(f"bisa di save {datacarname}")
    dataforsave={
        "data":data["thisCarData"]
    }
    dataforsave["data"]["Vynils"]=data["thisCarVynils"]
    print(dataforsave)
    with open(f'cpm/cars/livery/{datacarname}', 'w', encoding='utf-8') as f:
        json.dump(dataforsave, f, ensure_ascii=False, indent=4)
    return datacarname




if __name__=="__main__":
    sistem_operasi=os.name
    disp=""
    while True:
        # if sistem_operasi=="nt":os.system("cls")
        # if sistem_operasi=="posix":os.system("clear")
        print(disp)
        menus="""
=========================
        Topix SB CPM TOOLS V1.0
=========================
0. tes
1. edit account
2. create account
number (x exit): """
        inp=input(menus)
        if inp=="x" or inp=="X":break
        elif inp=="0":
            pass

        elif inp=="1":
            print("=================== verifyPassword")
            while True:
                teslogin=cpm.verifyPassword(input("email : "),input("password : "))
                if teslogin!=None:break
            print("=================== getAccountInfo")
            cpm.getAccountInfo()
            print("=================== GetPlayerRecords")
            cpm.GetPlayerRecords()
            print("=================== TestGetAllCars")
            shutil.rmtree('player/cars')
            os.mkdir('player/cars') 
            cpm.TestGetAllCars()
            print("=================== GetCarHash")
            cpm.GetCarHash()
            print("=================== SavePlayerRecords7")
            menusedit="""
=========================
1. manual edit save
2. inject mod
3. change cars to mod/ori
4. World Sale
5. edit player cars
6. unlock klakson
7. inject livery car
8. edit money
9. edit coin
10. edit ID
11. reset animation
number (x exit): """
            
            while True:
                inp=input(menusedit)
                if inp=="x" or inp=="X":break
                elif inp=="1":
                    with open('player/data.json', 'r',encoding='utf-8') as openfile: data = json.load(openfile)
                    with open('player/carhash.json', 'r',encoding='utf-8') as openfile: datacar = json.load(openfile)
                    
                    if cpm.SavePlayerRecords7(data) and cpm.SaveCarHash(datacar): disp="Sukses"
                    else: disp="Gagal"
                elif inp=="2":
                    print("=================== GetPlayerRecords")
                    cpm.GetPlayerRecords()
                    with open('player/data.json', 'r',encoding='utf-8') as openfile: data = json.load(openfile)
                    with open('data_mod.json', 'r',encoding='utf-8') as openfile: datamod = json.load(openfile)
                    with open('carhash_mod.json', 'r',encoding='utf-8') as openfile: datacar = json.load(openfile)

                    datamod["data"]["allData"]=data["data"]["allData"]
                    datamod["data"]["Name"]=data["data"]["Name"]
                    datamod["data"]["localID"]=data["data"]["localID"]
                    datamod["data"]["FriendsID"]=data["data"]["FriendsID"]
                    # datamod["data"]["money"]=data["data"]["money"]
                    # datamod["data"]["coin"]=data["data"]["coin"]
                    data=datamod

                    with open('player/data.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                    with open('player/carhash.json', 'w', encoding='utf-8') as f:
                        json.dump(datacar, f, ensure_ascii=False, indent=4)

                    if cpm.SavePlayerRecords7(data) and cpm.SaveCarHash(datacar): disp="Sukses"
                    else: disp="Gagal"
                    
                    path = "cpm/cars/mod/"
                    dir_list = os.listdir(path)
                    print("Files and directories in '", path, "' :")
                    dir_list=sorted(dir_list, key=len, reverse=False)
                    for idcar in dir_list:
                        print(f"  >> Inject Car id [{idcar}]")
                        with open(f'cpm/cars/mod/{idcar}', 'r',encoding='utf-8') as openfile: datacar = json.load(openfile)
                        if cpm.SaveCars(datacar): disp="Sukses"
                        else: disp="Gagal"
                elif inp=="3":
                    if input(" 1:ori 2:mod = ")=="2": tipe="mod"
                    else:tipe="ori"
                    idcar=input("ID CAR : ")
                    with open(f'cpm/cars/{tipe}/{idcar}', 'r',encoding='utf-8') as openfile: datacar = json.load(openfile)
                    if cpm.SaveCars(datacar): disp="Sukses"
                    else: disp="Gagal"
                elif inp=="4":
                    print()
                    autosep=False
                    if input("auto save [y/n] : ").lower()=="y":
                        autosep=True
                    wsvalue=input("World Value : ")
                    while True:
                        xpo=cpm.GetCarListWorldSale2(wsvalue)
                        if xpo != None:
                            klp=xpo.strip('][').split('},{')
                            idxsale=0
                            if len(klp)>1:
                                for tyy in klp:
                                    print(f"{idxsale} - {len(klp)}")
                                    if idxsale==0:
                                        aitem=tyy+"}"
                                    elif idxsale==len(klp)-1:
                                        aitem="{"+tyy[:-1]
                                    else:
                                        aitem="{"+tyy+"}"
                                    try:
                                        caitem=json.loads(aitem)
                                        print("<<------------------------------------>>")
                                        for itemv in caitem:
                                            print(f"{itemv}\t:{caitem[itemv]}")
                                        idxsale+=1
                                        carxpo=cpm.TestGetOneCarFromWorldSale(caitem["ownerAccountID"],caitem["carID"],wsvalue)
                                        datacar=json.dumps(json.loads(carxpo),indent=2)
                                        datacar=json.loads(datacar)
                                        print(f'OwnerID : {datacar["ownerID"]}')
                                        print(f'Name    : {datacar["ownerName"]}')
                                        print(f'Car id  : {datacar["carID"]}')
                                        print(f'Price   : {datacar["price"]}')
                                        print(f'Desc    : {datacar["description"]}')
                                        datacarname=savewscar(datacar["carID"],datacar)
                                        print("<<------------------------------------>>")
                                        print()
                                        if autosep:
                                            print("> Save To Account")
                                            with open(f'cpm/cars/livery/{datacarname}', 'r',encoding='utf-8') as openfile: datacar = json.load(openfile)
                                            datacar["data"]["floats"][0]=1
                                            if cpm.SaveCars(datacar): disp="Sukses"
                                            else: disp="Gagal"
                                    except:
                                        print(f"gagal ambil item : {aitem}")
                            else:
                                pass
                                # print(f"Len klp : {len(klp)}")
                        for tunggu in range(60,0,-1):
                            sys.stdout.write(f" wait {tunggu} \r")
                            sys.stdout.flush()
                            time.sleep(1)
                elif inp=="5":
                    dir_list=sorted(os.listdir("cpm/cars/livery/"), key=len, reverse=False)
                    itrlivery=1
                    print("\n  [ Urutan Livery yang tersedia ]")
                    for idnya in dir_list:
                        if "_" not in idnya:
                            print(f"  {itrlivery}. {cariurutan(idnya)}")
                        itrlivery+=1
                    urutcar=input("\nurutan car : ")
                    idcar=cariid(int(urutcar))
                    if idcar==None:
                        print("ga ada data id car")
                    else:
                        print(f"ID CAR NYA ADALAH {idcar}")
                        with open(f'player/cars/{idcar}', 'r',encoding='utf-8') as openfile: datacar = json.load(openfile)
                        menuscar="""
                
     [ Menu Edit ]
x to save
1. Police on
2. Police off
3. Timpa pakai livery
choice : 
"""
                        
                            
                        while True:
                            caredit=input(menuscar)
                            if caredit=="x":break
                            elif caredit=="1":
                                datacar["data"]["floats"][0]=1
                            elif caredit=="2":
                                datacar["data"]["floats"][0]=0
                            elif caredit=="3":
                                try:
                                    with open(f'cpm/cars/livery/{input("nama file di folder livery : ")}', 'r',encoding='utf-8') as openfile: datacar = json.load(openfile)
                                except:
                                    print(f"Belum punya data livery mobil ke {urutcar}")

                        if cpm.SaveCars(datacar): disp="Sukses"
                        else: disp="Gagal"
                elif inp=="6":
                    print("=================== GetPlayerRecords")
                    cpm.GetPlayerRecords()
                    with open('player/data.json', 'r',encoding='utf-8') as openfile: data = json.load(openfile)
                    data["data"]["floats"][27]=1
                    data["data"]["floats"][28]=1
                    data["data"]["floats"][29]=1
                    data["data"]["floats"][30]=1
                    data["data"]["floats"][31]=1

                    if cpm.SavePlayerRecords7(data): disp="Sukses"
                    else: disp="Gagal"
                elif inp=="7":
                    dir_list=os.listdir("cpm/cars/livery/")
                    dir_list.sort(key=int)
                    for idcar in dir_list:
                        if "_" not in idcar:
                            try:
                                print(idcar)
                                with open(f'cpm/cars/livery/{idcar}', 'r',encoding='utf-8') as openfile: datacar = json.load(openfile)
                                datacar["data"]["floats"][0]=1
                                if cpm.SaveCars(datacar): disp="Sukses"
                                else: disp="Gagal"
                            except:
                                print(f"Belum punya data livery mobil ke {urutcar}")
                elif inp=="8":
                    print("=================== GetPlayerRecords")
                    cpm.GetPlayerRecords()
                    muniy=input("Money : ")
                    with open('player/data.json', 'r',encoding='utf-8') as openfile: data = json.load(openfile)
                    data["data"]["money"]=int(muniy)
                    if cpm.SavePlayerRecords7(data): disp="Sukses"
                    else: disp="Gagal"
                elif inp=="9":
                    print("=================== GetPlayerRecords")
                    cpm.GetPlayerRecords()
                    muniy=input("Coin : ")
                    with open('player/data.json', 'r',encoding='utf-8') as openfile: data = json.load(openfile)
                    data["data"]["coin"]=int(muniy)
                    if cpm.SavePlayerRecords7(data): disp="Sukses"
                    else: disp="Gagal"
                elif inp=="10":
                    print("=================== GetPlayerRecords")
                    cpm.GetPlayerRecords()
                    muniy=input("localID : ")
                    with open('player/data.json', 'r',encoding='utf-8') as openfile: data = json.load(openfile)
                    data["data"]["localID"]=int(muniy)
                    if cpm.SavePlayerRecords7(data): disp="Sukses"
                    else: disp="Gagal"
                elif inp=="11":
                    print("=================== GetPlayerRecords")
                    cpm.GetPlayerRecords()
                    with open('player/data.json', 'r',encoding='utf-8') as openfile: data = json.load(openfile)
                    data["data"]["animations"]=[]
                    if cpm.SavePlayerRecords7(data): disp="Sukses"
                    else: disp="Gagal"

        elif inp=="2":
            print("Create Account")
            if cpm.signupNewUser(input(" Email : "),input(" Password : ")):
                with open('data_basic.json', 'r') as openfile:
                    data = json.load(openfile)
                data["data"]["localID"]="TSB"+str(random.randint(11111,99999))
                data["data"]["Name"]=randomcolorname("Subscribe YT TopixSB & DragChannel")
                with open('carhash_basic.json', 'r') as openfile:
                    datacar = json.load(openfile)
                if cpm.SavePlayerRecords7(data) and cpm.SaveCarHash(datacar):
                    disp="Sukses"
                else: disp="Gagal"
            else:
                disp="Email sudah terdaftar"
                
        else:
            print("Wrong...!")