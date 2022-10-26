import json
import requests
import colorama
from colorama import Fore, Style
colorama.init()
def c(colr, tex, dim):
    try:
        w = {
            "BLACK": Fore.BLACK,
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "BLUE": Fore.BLUE,
            "MAGENTA": Fore.MAGENTA,
            "CYAN": Fore.CYAN,
            "WHITE": Fore.WHITE,
            "RESET": Fore.RESET,
        }
        if dim == 1:
            return f"{Style.DIM}{w[colr.upper()]} {tex} {Style.RESET_ALL}"
        else:
            return f"{w[colr.upper()]} {tex} {Style.RESET_ALL}"
    except:
        return tex


with open("data.json") as t:
    readData=t.read()
readData1=readData.replace('\\"','"').replace('"{','{').replace('}"','}')
print(readData1)
readData2=json.loads(readData1)
for dt1 in readData2["data"]:
    print(dt1)


dat={
    "idToken":"",
    "ftoken":input("firebase token : "),
    "key":""
}

vbase={
    "1":"https://www.googleapis.com/identitytoolkit/v3/relyingparty/$mode?key=$key",
    "2":"https://us-central1-cp-multiplayer.cloudfunctions.net/",
}
vuri={
    "1":
    {
        "verifyPassword":"verifyPassword",
        "getAccountInfo":"getAccountInfo",
    },
    "2":
    {
        "Check4":"Check4",
        "GetCarIDnStatus":"GetCarIDnStatus",
        "GetCarHash":"GetCarHash",
        "GetDeletedCarList":"GetDeletedCarList",
        "SavePlayerRecords4":"SavePlayerRecords4",
        "SaveCars":"SaveCars",
        "SaveCarsHash":"SaveCarsHash",
    }
}
vdata={
    "verifyPassword":{"email": "tsbshop11@gmail.com","password": "hehehe","returnSecureToken": True},
    "getAccountInfo":{"idToken":dat["idToken"]},
    "Check4":{"data":{"var2":""}},
    "GetCarIDnStatus":{"data":""},
    "GetCarHash":{"data":""},
    "GetDeletedCarList":{"data":""},
    "SavePlayerRecords4":readData2,
    "SaveCars":{"data":""},
    "SaveCarsHash":{"data":[0,0,0,0,0,0,0,0,0,0,0,0,0,-2048228082,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1179404253,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
}

vheaders={
    "1":{
    "Content-Type": "application/json",
    "X-Android-Package": "com.olzhas.carparking.multyplayer",
    "X-Android-Cert": "D4962F8124C2E09A66B97C8E326AFF805489FE39",
    "Accept-Language": "in-ID, en-US",
    "X-Client-Version": "Android/Fallback/X21000003/FirebaseCore-Android",
    "X-Firebase-GMPID": "1:581727203278:android:af6b7dee042c8df539459f",
    "X-Firebase-Client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
    "Content-Length": "76",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G988N Build/NRD90M)",
    "Host": "www.googleapis.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
},
    "2":{
    "Host": "us-central1-cp-multiplayer.cloudfunctions.net",
    "authorization": "",
    "firebase-instance-id-token": dat["ftoken"],
    "content-type": "application/json; charset=utf-8",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/3.12.1",
}}



def sen(xbase,rute):
    xuri,param,headers="",{},""
    if xbase=="1":
        xuri=""
        if "$key" in vbase[xbase]:
            if dat["key"]=="":
                polol=input("key : ")
                xuri=vbase[xbase].replace("$mode",rute).replace("$key",polol)
                dat["key"]=polol
            else:
                xuri=vbase[xbase].replace("$mode",rute).replace("$key",dat["key"])
        else:
            xuri=vbase[xbase]
        try:
            if "idToken" in vdata[rute]:
                vdata[rute]["idToken"]=dat["idToken"]
            param = vdata[rute]
        except:
            param = vdata[rute]
    elif xbase=="2":
        xuri=f"{vbase[xbase]}{rute}"
        param = vdata[rute]
    else:
        xuri=vbase[xbase]
    
    if "authorization" in vheaders[xbase]:
        vheaders[xbase]["authorization"]=f"Bearer {dat['idToken']}"
    headers=vheaders[xbase]

    # print()
    # print(f"xbase : {xbase}")
    # print(f"rute : {rute}")
    # print(f"xuri : {xuri}")
    try:
        req = requests.post(xuri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        
        print()
        print(c("green",xuri,0))
        # print(c("cyan",json.dumps(param,indent=2),0))
        # print(c("magenta",json.dumps(headers,indent=2),0))
        if xbase=="1":
            if dat["idToken"]=="":
                dat["idToken"]=ress["idToken"]
                print(c("green","idToken Added",0))
        return[0,ress]
    except Exception as e:
        return[99,f"Error : {e}"]

def rik(inpbase):
    for t in vuri[inpbase]:
        print(c("green",f"\t\t[ {t} ]",0))
        hsl=sen(inpbase,t)
        if hsl[0]==0:
            if "error" in hsl[1]:
                print(c("red",hsl[1],0))
            else:
                print(json.dumps(hsl[1],indent=2))
        else:
            print(c("red",hsl,0))

#eiITW4OfCgg:APA91bFvxWYHWPHfyLq3M_vVQzwTbODA92gPm4BwEuNNBZoYL6Y26BaqOotNgE-tJWJCx61LFNMArN1PSy3P6kru4vnz_ZLHeFZskN5be-8BnpGNRzXTICpiPIOVX15hlpTmTrlz9q5X

akun={
    "tsbshop11":"AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM"
}
while True:
    if len(dat["idToken"])<1:
        istoken="UnDefinied"
    else:
        istoken="Ready"
    menu=f"\nyour token is {istoken}\n1. getToken\n2. Save & Exit\n3. Show all"
    inpp=input(f"{menu}\npilihan : ")
    if inpp=="1":
        rik(inpp)
    if inpp=="2":
        rik(inpp)
    elif inpp=="3":
        for dt1 in readData2["data"]:
            print(f"\t\t[ {dt1} ]")
            if type(readData2["data"][dt1]) not in [str,int]:
                print(f"{str(readData2['data'][dt1])}")
            else:
                dfd=readData2['data'][dt1]
                print(f"{dt1} : {dfd}")