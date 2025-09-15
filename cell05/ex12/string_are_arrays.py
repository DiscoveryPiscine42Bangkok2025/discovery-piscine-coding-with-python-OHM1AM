import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]

    if 'z' not in input_string:
        print("none")
    else:
        # แสดง 'z' สำหรับทุกครั้งที่พบในข้อความ
        for char in input_string:
            if char == 'z':
                print('z', end='') # end='' ทำให้ไม่ขึ้นบรรทัดใหม่

#python string_are_arrays.py
#python string_are_arrays.py "The character z is not found in this string"
#python string_are_arrays.py "The character z is found in this string"
#python string_are_arrays.py "Zaz visits the zoo with Zazie"