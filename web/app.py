from flask import Flask, render_template, request, redirect
from forms import *
import httpx
import json
import random as rdm

app = Flask(__name__)
app.config["SECRET_KEY"] = "asddasdwadsadwa"


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
Vdata["login"] = False
Vdata["player"] = {"data": {}}


def plitcolornama(nama):
    disp = []
    xcx = nama.split("[")
    if len(xcx) == 1:
        return [[nama, "#ffffff"]]
    xcx.pop(0)
    kolorkode = "#ffffff"
    for rer in xcx:
        try:
            if rer[6] == "]":
                disp.append([rer[7:len(rer)], f"#{rer[0:6]}"])
                # print(f"code #{rer[0:6]} tex {rer[7:len(rer)]}")
            else:
                disp.append([rer, kolorkode])
                # print(f"{rer} {rer[6]}")
        except Exception as e:
            print(f"error : {rer}")
            # for p in nama:
            #     disp.append([p,kolorkode])
            pass
    return disp


def cekamanwarna(nama):
    # cek kode warna
    carikurung = nama.split("]")
    warnaaman = True
    for pk in range(len(carikurung)-1):
        try:
            # print(carikurung[pk][-7])
            if carikurung[pk][-7] != "[":
                warnaaman = False
        except IndexError:
            # print(carikurung[pk][1])
            warnaaman = False
            return warnaaman
    return warnaaman


def cekhornaccess(dty):
    akses = 0
    if dty[27] == 1:
        akses += 1
    if dty[28] == 1:
        akses += 1
    if dty[29] == 1:
        akses += 1
    if dty[30] == 1:
        akses += 1
    if dty[31] == 1:
        akses += 1
    if akses == 0:
        return "locked"
    elif akses == 5:
        return "full access"
    elif akses < 5:
        return "access sebagian"


def verifyPassword(email, password):
    uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={Vdata['key']}"
    data = {"email": email, "password": password, "returnSecureToken": True}
    req = httpx.post(uri, data=json.dumps(data), headers=Vheader)
    if req.status_code == 200:
        ress = json.loads(req.text)
        print(f"verifyPassword : {len(ress)}")
        Vdata["idToken"] = ress["idToken"]
        Vdata["login"] = True
        # print(Vdata["idToken"])
        return True
    return False


def SavePlayerRecords7():
    uri = f"https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecords7"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    pipit = json.dumps(Vdata["player"]["data"])
    print(pipit)
    data = {"data": pipit}
    req = httpx.post(uri, data=json.dumps(data), headers=heder)
    # print(req.status_code)
    # print(req.text)
    if req.status_code == 200:
        ress = json.loads(req.text)
        print(f"Save Account Info {ress}")
        resss = json.loads(ress["result"])
        if resss == 1:
            return True
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
        Vdata["player"] = {"data": resss}
        return [1, resss]
    else:
        return [0, req.text]


def cekform(dtcit):
    datachange = False
    arrform = {}
    for dtdata in dtcit:
        if dtcit[dtdata] == None:
            pass
        elif dtcit[dtdata] == False:
            pass
        elif dtcit[dtdata] == "":
            pass
        else:
            if dtdata not in ["submit", "csrf_token"]:
                print(f"{dtdata}\t:{dtcit[dtdata]}")
                datachange = True
                arrform[dtdata] = dtcit[dtdata]
    print(f"\ndata has change : {datachange}\n")
    return [datachange, arrform]


@app.route('/')
def index():
    return redirect("TopixSB")


@app.route('/TopixSB', methods=['GET', 'POST'])
def hello():
    userweb = str(request.remote_addr).replace(".", "")
    linktiktok = [['T', '#ff2d00'], ['i', '#ff5a00'], ['k', '#ff8700'], ['t', '#ffb400'], ['o', '#ffe100'], ['k', '#d2ff00'], ['_', '#a5ff00'], ['=', '#78ff00'], ['_', '#4bff00'], ['t', '#1eff00'], ['o', '#00d2ff'], ['p', '#00a5ff'], [
        'i', '#0078ff'], ['x', '#004bff'], ['s', '#001eff'], ['b', '#ff2d00'], ['o', '#ff5a00'], ['f', '#ff8700'], ['f', '#ffb400'], ['i', '#ffe100'], ['c', '#d2ff00'], ['i', '#a5ff00'], ['a', '#78ff00'], ['l', '#4bff00']]
    linkyt = [['Y', '#d2ff00'], ['o', '#a5ff00'], ['u', '#78ff00'], ['T', '#4bff00'], ['u', '#1eff00'], ['b', '#00d2ff'], ['e', '#00a5ff'], ['_', '#0078ff'], ['=', '#004bff'], ['_', '#001eff'], ['T',
                                                                                                                                                                                                   '#ff2d00'], ['o', '#ff5a00'], ['p', '#ff8700'], ['i', '#ffb400'], ['x', '#ffe100'], ['S', '#d2ff00'], ['B', '#a5ff00']]
    forml = Login()
    formk = Cdata()

    dtlogin = {
        "vemail": forml.email.data,
        "vpassword": forml.password.data
    }
    dtcit = {
        "vname": formk.cname.data,
        "vnamer": formk.cnamer.data,
        "vmoney": formk.cmoney.data,
        "vcoin": formk.ccoin.data,
        "vhorn": formk.chorn.data,
        # "vsirine": formk.csirine.data,
    }

    print(f"""
            [ data ]""")
    for dtdata in dtcit:
        print(f"{dtdata}\t:{dtcit[dtdata]}")

    if request.method == 'POST':
        print("-> POST Method")
        print(f"-> is login : {Vdata['login']}")
        if Vdata['login'] == False:
            print("-> Login")
            verifyPassword(dtlogin['vemail'], dtlogin['vpassword'])
            print("-> Check Login")
            if Vdata['login'] == True:
                print("-> Login Success")
                print(f"{Vdata['login']} = {dtlogin}")
                GetPlayerRecords()

                print("-> Cek aman warna")
                dispnama = Vdata["player"]["data"]["Name"]
                if cekamanwarna(Vdata["player"]["data"]["Name"]) == True:
                    print("-> Coloring nama")
                    dispnama = plitcolornama(Vdata["player"]["data"]["Name"])

                dtatas = {
                    "ID": Vdata["player"]["data"]["localID"],
                    "name": Vdata["player"]["data"]["Name"],
                    "money": Vdata["player"]["data"]["money"],
                    "coin": Vdata["player"]["data"]["coin"],
                    "horn access": cekhornaccess(Vdata["player"]["data"]["floats"]),
                }
                otput = json.dumps(dtatas, indent=2)
                return render_template('kode.html', output=otput, form=formk, dispvar=dispnama, linktiktok=linktiktok, linkyt=linkyt)
            else:
                print("-> Login Failed")
                disp = "Login_Failed"
                return render_template('index.html', form=forml, dispvar=disp, linktiktok=linktiktok, linkyt=linkyt)
        else:
            print(f"-> REFRESH PAGE {Vdata['login']} = {dtlogin}")

            keytov = {
                "cname": "Name",
                "cmoney": "money",
                "ccoin": "coin",
            }
            dataubah = cekform(formk.data)
            if dataubah[0] == True:
                for itemubah in dataubah[1]:
                    print(itemubah)

                # SavePlayerRecords7()

            if cekamanwarna(Vdata["player"]["data"]["Name"]) == True:
                print("-> Coloring nama")
                dispnama = plitcolornama(Vdata["player"]["data"]["Name"])

            dtatas = {
                "ID": Vdata["player"]["data"]["localID"],
                "name": Vdata["player"]["data"]["Name"],
                "money": Vdata["player"]["data"]["money"],
                "coin": Vdata["player"]["data"]["coin"],
                "horn access": cekhornaccess(Vdata["player"]["data"]["floats"]),
            }
            otput = json.dumps(dtatas, indent=2)
            return render_template('kode.html', output=otput, form=formk, dispvar=dispnama, linktiktok=linktiktok, linkyt=linkyt)
    else:
        print("-> GET Method")
        Vdata["idToken"] = "ini token"
        Vdata["key"] = "AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM"
        Vdata["firebase-instance-id-token"] = "fchcZJLSMpo:APA91bF8nZQY5awRdIgI41tGbAr59K6SuXEeHXC9lQiHcjNR7SN2lD4OKlQ8VuhsgJrF38NgXkDufWoDCXKz-iixYUjeNx7KildcWuQimgagDhWDMxslXhFpaQtujmqn1JywoTEvXVYZ"
        Vdata["data"] = "9FD07A11C3494803B517F92545ED5A6702AD0AD2"
        Vdata["login"] = False
        Vdata["player"] = {"data": {"Name": "Bro"}}
        disp = "visit_my_youtube_and_tiktok_to_see_more_cheats"
        otput = f"{userweb}"
        return render_template('index.html', output=otput, form=forml,  dispvar=disp, linktiktok=linktiktok, linkyt=linkyt)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
