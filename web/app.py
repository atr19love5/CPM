from flask import Flask, render_template, frequest,redirect
from forms import *
import httpx,json
import random as rdm

app = Flask(__name__)
app.config["SECRET_KEY"]="asddasdwadsadwa"


Vhost = "us-central1-cp-multiplayer.cloudfunctions.net"
Vheader = {
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
Vdata = {}
Vdata["idToken"] = "ini token"
Vdata["key"] = "AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM"
Vdata["firebase-instance-id-token"] = "fchcZJLSMpo:APA91bF8nZQY5awRdIgI41tGbAr59K6SuXEeHXC9lQiHcjNR7SN2lD4OKlQ8VuhsgJrF38NgXkDufWoDCXKz-iixYUjeNx7KildcWuQimgagDhWDMxslXhFpaQtujmqn1JywoTEvXVYZ"
Vdata["data"] = "9FD07A11C3494803B517F92545ED5A6702AD0AD2"
Vdata["login"]=False
Vdata["player"]={"data":{"Name":"Bro"}}


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

def verifyPassword(email, password):
    uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={Vdata['key']}"
    data = {"email": email, "password": password, "returnSecureToken": True}
    req = httpx.post(uri, data=json.dumps(data), headers=Vheader)
    if req.status_code == 200:
        ress = json.loads(req.text)
        print(f"verifyPassword : {len(ress)}")
        Vdata["idToken"] = ress["idToken"]
        # print(Vdata["idToken"])
        return True
    return False

def GetPlayerRecords():
    uri = f"https://{Vhost}/GetPlayerRecords2"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    data = {"data": Vdata["data"]}
    req = httpx.post(uri, data=json.dumps(data), headers=heder)
    if req.status_code == 200:
        ress = json.loads(req.text)
        resss = json.loads(ress["result"])
        Vdata["player"]={"data": resss}
        return [1,resss]
    else:
        return [0,req.text]

@app.route('/')
def index():
    return redirect("TopixSB")

@app.route('/TopixSB', methods = ['GET', 'POST'])
def hello():
    linktiktok=[['T', '#ff2d00'], ['i', '#ff5a00'], ['k', '#ff8700'], ['t', '#ffb400'], ['o', '#ffe100'], ['k', '#d2ff00'], ['_', '#a5ff00'], ['=', '#78ff00'], ['_', '#4bff00'], ['t', '#1eff00'], ['o', '#00d2ff'], ['p', '#00a5ff'], ['i', '#0078ff'], ['x', '#004bff'], ['s', '#001eff'], ['b', '#ff2d00'], ['o', '#ff5a00'], ['f', '#ff8700'], ['f', '#ffb400'], ['i', '#ffe100'], ['c', '#d2ff00'], ['i', '#a5ff00'], ['a', '#78ff00'], ['l', '#4bff00']]
    linkyt=[['Y', '#d2ff00'], ['o', '#a5ff00'], ['u', '#78ff00'], ['T', '#4bff00'], ['u', '#1eff00'], ['b', '#00d2ff'], ['e', '#00a5ff'], ['_', '#0078ff'], ['=', '#004bff'], ['_', '#001eff'], ['T', 
'#ff2d00'], ['o', '#ff5a00'], ['p', '#ff8700'], ['i', '#ffb400'], ['x', '#ffe100'], ['S', '#d2ff00'], ['B', '#a5ff00']]
    forml = Login()
    formk = Konsol()

    vemail , vpassword = forml.email.data,  forml.password.data
    print(f"em and pw : {vemail} {vpassword} {frequest.method}")
    if frequest.method=="POST":
        terisi=False
        if formk.cname!=None:terisi=True
        if terisi==True:
            return render_template('kode.html', form = formk, output=Vdata["player"]["data"]["Name"],linktiktok=linktiktok,linkyt=linkyt)
        else:
            disp= "visit_my_youtube_and_tiktok_to_see_more_cheats"
            return render_template('index.html', form = forml, output=disp,linktiktok=linktiktok,linkyt=linkyt)
    else:
        islogin=verifyPassword(vemail,vpassword)
        if islogin==True:
            rek=GetPlayerRecords()
            if rek[0]==1:
                namanya=Vdata["player"]["data"]["Name"]
                if cekamanwarna(namanya)==True:
                    namanya=plitcolornama(namanya)
                else:
                    namanya=Vdata["player"]["data"]["Name"]
                print(f"nama : {namanya}")
                
                return render_template('kode.html', form = formk, output=namanya,linktiktok=linktiktok,linkyt=linkyt)
            disp= "Login gagal"
            return render_template('index.html', form = forml,output=disp,linktiktok=linktiktok,linkyt=linkyt)
        
@app.route('/TopixSB', methods = ['GET', 'POST'])
def cname():
    return "cname"
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
