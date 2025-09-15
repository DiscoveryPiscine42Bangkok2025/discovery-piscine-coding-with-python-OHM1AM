import sys

if len(sys.argv) < 3:
    print("none")
else:
    for param in reversed(sys.argv[1:]):
        print(param)

#python aff_rev_params.py
#python aff_rev_params.py "coucou"
#python aff_rev_params.py "Python" "piscine" "hello"