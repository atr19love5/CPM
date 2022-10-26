import requests,json
import colorama
from colorama import Fore, Style, Back
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


headers={
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
}

def sen(mode,keyy):
    xuri=f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/{mode}?key={keyy}"
    param = {
  "email": "tsbshop11@gmail.com",
  "password": "hehehe",
  "returnSecureToken": True
}
        
    try:
        req = requests.post(xuri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        print()
        print(c("green",xuri,0))
        print(c("cyan",json.dumps(param,indent=2),0))
        print(c("magenta",json.dumps(headers,indent=2),0))
        return[0,ress]
    except:
        return[99,"failed..."]

akun={
    "tsbshop11":"AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM"
}
steps=["verifyPassword","getAccountInfo"]
for step in steps:
    print(c("green",f"\t\t[ {step} ]",0))
    hsl=sen(step,akun["tsbshop11"])
    if hsl[0]==0:
        print(json.dumps(hsl[1],indent=2))