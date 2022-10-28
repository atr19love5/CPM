import os,json,random
import cpm as cpm


def tes():
    with open('request_body.json', 'r') as openfile:
        dataakun = json.load(openfile)
    data={"data":json.loads(dataakun["data"])}
    with open('car13.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return data
# pl=tes()
# print(pl)
# exit()





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
1. edit account
2. create account
number (x exit): """
        inp=input(menus)
        if inp=="x" or inp=="X":break
        elif inp=="1":
            print("=================== verifyPassword")
            cpm.verifyPassword(input("email : "),input("password : "))
            print("=================== getAccountInfo")
            cpm.getAccountInfo()
            print("=================== GetPlayerRecords")
            cpm.GetPlayerRecords()
            print("=================== GetCarHash")
            cpm.GetCarHash()
            print("=================== SavePlayerRecords7")
            menusedit="""
=========================
1. save
2. inject mod
3. save cars
number (x exit): """
            with open('data.json', 'r') as openfile:
                data = json.load(openfile)
            with open('carhash.json', 'r') as openfile:
                datacar = json.load(openfile)
            while True:
                inp=input(menusedit)
                if inp=="x" or inp=="X":break
                elif inp=="1":
                    if cpm.SavePlayerRecords7(data) and cpm.SaveCarHash(datacar):
                        disp="Sukses"
                    else: disp="Gagal"
                elif inp=="2":
                    with open('data_mod.json', 'r') as openfile:
                        datamod = json.load(openfile)
                    with open('carhash_mod.json', 'r') as openfile:
                        datacar = json.load(openfile)
                    # datamod["data"]["allData"]=data["data"]["allData"]
                    datamod["data"]["Name"]=data["data"]["Name"]
                    datamod["data"]["localID"]=data["data"]["localID"]
                    datamod["data"]["FriendsID"]=data["data"]["FriendsID"]
                    datamod["data"]["money"]=data["data"]["money"]
                    datamod["data"]["coin"]=data["data"]["coin"]
                    data=datamod
                elif inp=="3":
                    if input(" 1:ori 2:mod = ")=="2":
                        tipe="mod"
                    else:tipe="ori"
                    with open(f'cpm/cars/{tipe}/13', 'r') as openfile:
                        datacar = json.load(openfile)
                    if cpm.SaveCars(datacar):
                        disp="Sukses"
                    else: disp="Gagal"
        elif inp=="2":
            print("Create Account")
            if cpm.signupNewUser(input(" Email : "),input(" Password : ")):
                with open('basedata.json', 'r') as openfile:
                    data = json.load(openfile)
                data["data"]["localID"]="TSB"+str(random.randint(11111,99999))
                with open('basecarhash.json', 'r') as openfile:
                    datacar = json.load(openfile)
                if cpm.SavePlayerRecords7(data) and cpm.SaveCarHash(datacar):
                    disp="Sukses"
                else: disp="Gagal"
            else:
                disp="Email sudah terdaftar"
                
        else:
            print("Wrong...!")