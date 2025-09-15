import sys
import re

if len(sys.argv) != 3: # ตรวจสอบว่ามีครบสองตัว
    print("none")
else:
    keyword = sys.argv[1]
    string = sys.argv[2]
    occurrences = len(re.findall(rf"{re.escape(keyword)}", string)) #re.findall() เพื่อหาการปรากฏของคำสำคัญในสตริง

    if occurrences == 0:
        print("none")
    else:
        print(occurrences)

#python scan_it.py
#python scan_it.py "the"
#python scan_it.py "the" "the quick brown fox jumps over the lazy dog"