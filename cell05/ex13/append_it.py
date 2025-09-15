import sys

if len(sys.argv) == 1:
    print("none")
else:
    for param in sys.argv[1:]:
        if not param.endswith('ism'): # มี ism ข้าม
            print(param + 'ism')

#python append_it.py
#python append_it.py "parallel" "egoism" "human"