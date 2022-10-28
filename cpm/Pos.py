import httpx,json
import random as rdm

Vhost="us-central1-cp-multiplayer.cloudfunctions.net"
Vdata={}
Vheader={
    "Content-Type": "application/json",
    "X-Android-Package": "com.olzhas.carparking.multyplayer",
    "X-Android-Cert": "D4962F8124C2E09A66B97C8E326AFF805489FE39",
    "Accept-Language": "in-ID, en-US",
    "X-Client-Version": "Android/Fallback/X21000008/FirebaseCore-Android",
    "X-Firebase-GMPID": "1:581727203278:android:af6b7dee042c8df539459f",
    "X-Firebase-Client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
    "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})",
    "Host": "www.googleapis.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
  }
# for cekdata in ["data"]:
#     if cekdata not in Vdata:
#         Vdata[cekdata]=input(f"{cekdata} : ")
Vdata["key"]="AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM"
Vdata["firebase-instance-id-token"]="ea9gG_uUWlo:APA91bGw8J3rXLD26czTasH4UqHxJ8wZ6aVn1mKQpHUVs5_wWzh3mkivULK6yNtjKpTolKX4iso4_9xWwXa5AQH9kDTQl04MQCnT1r5C6rSeZeXugaVIo62vjtTyWZpiYcplo2JfVL1n"
Vdata["data"]="9FD07A11C3494803B517F92545ED5A6702AD0AD2"


def verifyPassword(email,password):
    uri=f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={Vdata['key']}"
    data={"email":email,"password":password,"returnSecureToken":True}
    req=httpx.post(uri,data=json.dumps(data),headers=Vheader)
    if req.status_code==200:
        ress=json.loads(req.text)
        print(f"verifyPassword : {len(ress)}")
        Vdata["idToken"]=ress["idToken"]
def getAccountInfo():
    uri=f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key={Vdata['key']}"
    data={"idToken":Vdata["idToken"]}
    req=httpx.post(uri,data=json.dumps(data),headers=Vheader)
    if req.status_code==200:
        ress=json.loads(req.text)
        print(f"getAccountInfo : {len(ress)}")
def GetPlayerRecords():
    uri=f"https://{Vhost}/GetPlayerRecords2"
    heder={
        "Host":Vhost,
        "authorization":f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token":Vdata["firebase-instance-id-token"],
        "content-type":"application/json; chatset=utf-8",
        "accept-encoding":"gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    data={"data":Vdata["data"]}
    req=httpx.post(uri,data=json.dumps(data),headers=heder)
    if req.status_code==200:
        ress=json.loads(req.text)
        resss=json.loads(ress["result"])
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump({"data":resss}, f, ensure_ascii=False, indent=4)
        print(f"Data Player : {len(resss)}")
        print(resss["Name"])
        print(resss["localID"])
def GetCarHash():
    uri=f"https://{Vhost}/GetCarHash"
    heder={
        "Host":Vhost,
        "authorization":f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token":Vdata["firebase-instance-id-token"],
        "content-type":"application/json; chatset=utf-8",
        "accept-encoding":"gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    data={"data":""}
    req=httpx.post(uri,data=json.dumps(data),headers=heder)
    if req.status_code==200:
        ress=json.loads(req.text)
        resss=json.loads(ress["result"])
        with open('carhash.json', 'w', encoding='utf-8') as f:
            json.dump({"result":resss}, f, ensure_ascii=False, indent=4)
        print(f"Car Hash : {len(resss)}")
def SavePlayerRecords7(dataakun):
    print("Save Account Info")
    uri=f"https://{Vhost}/SavePlayerRecords7"
    heder={
        "Host":Vhost,
        "authorization":f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token":Vdata["firebase-instance-id-token"],
        "content-type":"application/json; chatset=utf-8",
        "accept-encoding":"gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    pipit=json.dumps(dataakun["data"])
    data={"data":pipit}
    req=httpx.post(uri,data=json.dumps(data),headers=heder)
    # print(req.status_code)
    # print(req.text)
    if req.status_code==200:
        ress=json.loads(req.text)
        resss=json.loads(ress["result"])
        # print(resss)
        return True
    return False
def SaveCarHash(dataakun):
    print("Save Car Hash")
    uri=f"https://{Vhost}/SaveCarHash"
    heder={
        "Host":Vhost,
        "authorization":f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token":Vdata["firebase-instance-id-token"],
        "content-type":"application/json; chatset=utf-8",
        "accept-encoding":"gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    pipit=json.dumps(dataakun)
    data={"data":pipit}
    req=httpx.post(uri,data=json.dumps(data),headers=heder)
    # print(req.status_code)
    # print(req.text)
    if req.status_code==200:
        ress=json.loads(req.text)
        resss=json.loads(ress["result"])
        # print(resss)
        return True
    return False

def SaveCars(data):
    print("Save Cars")
    uri=f"https://{Vhost}/SaveCars"
    heder={
        "Host":Vhost,
        "authorization":f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token":Vdata["firebase-instance-id-token"],
        "content-type":"application/json; chatset=utf-8",
        "accept-encoding":"gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    # pipit=json.dumps(data["data"])
    data=json.dumps(data)
    print(json.load(data["data"]))
    req=httpx.post(uri,data=data,headers=heder)
    print(req.status_code)
    print(req.text)
    if req.status_code==200:
        ress=json.loads(req.text)
        resss=json.loads(ress["result"])
        # print(resss)
        return True
    return False





def signupNewUser(email,password):
    uri=f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key={Vdata['key']}"
    data={"email":email,"password":password}
    req=httpx.post(uri,data=json.dumps(data),headers=Vheader)
    if req.status_code==200:
        ress=json.loads(req.text)
        print(f"signupNewUser : {len(ress)}")
        Vdata["idToken"]=ress["idToken"]
        return True
    return False