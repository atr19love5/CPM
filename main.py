import os,json
import cpm as cpm

if __name__=="__main__":
    sistem_operasi=os.name
    print("=================== verifyPassword")
    cpm.verifyPassword(input("email : "),input("password : "))
    print("=================== getAccountInfo")
    cpm.getAccountInfo()
    print("=================== GetPlayerRecords")
    cpm.GetPlayerRecords()
    print("=================== GetCarHash")
    cpm.GetCarHash()
    print("=================== SavePlayerRecords7")
    disp=""
    while True:
        # if sistem_operasi=="nt":os.system("cls")
        # if sistem_operasi=="posix":os.system("clear")
        print(disp)
        menus="""Topix SB CPM TOOLS V1.0
=========================
1. save
2. unbanned
========================="""
        print(menus)
        inp=input("number (x exit): ")

        if inp=="x" or inp=="X":break
        elif inp=="1":
            if cpm.SavePlayerRecords7()==1 and cpm.SaveCarHash()==1:
                disp="Sukses"
            else:
                disp="Gagal"
        elif inp=="2":
            with open('data.json', 'r') as openfile:
                dataakun = json.load(openfile)
        else:
            print("Wrong...!")