from flask import Flask, render_template, request
from forms import *
import httpx,json
import random as rdm

app = Flask(__name__)
app.secret_key = 'development key topixsb'



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
Vdata["player"]={}


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

@app.route('/', methods = ['GET', 'POST'])
def hello():
    forml = Login()
    formk = Konsol()
    if request.method == 'POST':
        vemail , vpassword = forml.email.data,  forml.password.data
        if verifyPassword(vemail,vpassword)==True:
            GetPlayerRecords()
            disp=f"welcome {Vdata['player']['data']['Name']}"
            return render_template('kode.html', form = formk, output=disp)
        else:
            disp= "wrong email or password"
            return render_template('index.html', form = forml,output=disp)
    elif request.method == 'GET':
        return render_template('index.html', form = forml,output="Email & Password CPM Account Required")

if __name__ == "__main__":
    app.run(debug=True)
