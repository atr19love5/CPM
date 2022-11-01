import os
import json


dir_list = os.listdir("cpm/cars/livery/")
dir_list.sort(key=int)
for idcar in dir_list:
    if "_" not in idcar:
        try:
            print(idcar)
            with open(f'cpm/cars/livery/{idcar}', 'r', encoding='utf-8') as openfile:
                datacar = json.load(openfile)
        except:
            print(f"Belum punya data livery mobil ke")
