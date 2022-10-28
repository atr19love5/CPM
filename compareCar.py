import json

patt="cpm/cars"

dat={}
for switcher in range(2):
    if switcher%2==0:
        mode="mod"
    else:
        mode="ori"
    with open(f'{patt}/{mode}/13', 'r') as openfile:
        dat[mode]= json.loads(json.load(openfile)["data"])

inp=input("mode mod/ori:")
if inp=="mod":
    print(json.dumps(dat["mod"],indent=2))
elif inp=="ori":
    print(json.dumps(dat["ori"],indent=2))