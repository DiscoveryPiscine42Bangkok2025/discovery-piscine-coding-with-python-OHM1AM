def average(grades_dict): # ฟังก์ชันคำนวณค่าเฉลี่ย
    if not grades_dict:
        return 0  # กันการหารด้วย0 ถ้าไม่มีข้อมูลเลย
    total = sum(grades_dict.values())
    count = len(grades_dict)
    return total / count

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")