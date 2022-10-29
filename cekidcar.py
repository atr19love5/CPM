import json,os

path = "cpm/cars/ori/"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
dir_list=sorted(dir_list, key=len, reverse=False)

hasil=[]
# prints all files
for filename in dir_list:
    with open(f'cpm/cars/ori/{filename}', 'r') as openfile:
        datacar=json.load(openfile)
    try:
        if len(datacar["data"]["Vynils"]["oneVynil"])>0:
            urutanmobil=datacar["data"]["Vynils"]["oneVynil"][0]["text"]
            idmobil=filename
            hasil.append({"urutan":int(urutanmobil),"id":idmobil})
        else:
            # print("belum di kasih vynils")
            pass
    except:
        # print(f"belum beli mobilnya")
        pass

hasil.sort(key=lambda x: x.get('urutan'))
print(hasil)
for hsl in hasil:
    print(f"{hsl}")
input()
