from os import walk
import sys
if len(sys.argv) == 1:
    exit("Usage:\nscript.py -d <directory> -p <prefix before filename> -c <Custom family name>\nWorks best with google fonts\n")
args = sys.argv[1:]
opts = dict()
for arg in ["-d","-p","-c"]:
    try:
        opts[arg]=args[args.index(arg)+1]
    except:
        opts[arg]=""
if opts["-d"] == "":
    opts["-d"]="."
f = []
for (dirpath, dirnames, filenames) in walk(opts["-d"]):
    f.extend(filenames)
    break
if len(f) == 0:
    exit("No files in Directory")
elif opts["-c"] == "":
    args = f[0].split("-")
    opts["-c"]=args[0]
print(f"- family: \"{opts['-c']}\"")
print("  fonts:")
prepend = opts["-p"]
for file in f:
    print(f"    - asset: \"{prepend+file}\"")
    args = file.lower().split("-")
    if args[1].find("italic") != -1:
        print("      style: italic")
    if args[1].find("thin") != -1:
        print("      weight: 100")
    elif args[1].find("extralight") != -1:
        print("      weight: 200")
    elif args[1].find("light") != -1:
        print("      weight: 300")
    elif args[1].find("regular") != -1 or args[1].find("normal") != -1 or args[1].find("plain") != -1:
        print("      weight: 400")
    elif args[1].find("medium") != -1:
        print("      weight: 500")
    elif args[1].find("semibold") != -1:
        print("      weight: 600")
    elif args[1].find("bold") != -1:
        print("      weight: 700")
    elif args[1].find("extrabold") != -1:
        print("      weight: 800")
    elif args[1].find("black") != -1:
        print("      weight: 900")
