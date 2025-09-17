def famous_births(people):
    def extract_year(dob):
        try:
            return int(dob)
        except Exception:   #หาเลข 4 หลักที่เป็นปีจากสตริง
            for token in reversed(dob.split()):
                if token.isdigit() and len(token) == 4:
                    return int(token)
            #ถ้าไม่เจอ ให้คืนค่าที่เยอะ เพื่อให้ไปอยู่ท้ายสุด
            return 10**9

    #เรียงค่าตามปีที่ได้จาก date_of_birth
    sorted_people = sorted(people.values(), key=lambda entry: extract_year(entry.get("date_of_birth", "")))

    #แสดงผลตามรูปแบบที่ต้องการ
    for entry in sorted_people:
        name = entry.get("name", "Unknown")
        dob = entry.get("date_of_birth", "Unknown")
        print(f"{name} is a great scientist born in {dob}.")
        
women_scientists = {
        "ada":    { "name": "Ada Lovelace",  "date_of_birth": "1815" },
        "cecilia":{ "name": "Cecilia Payne", "date_of_birth": "1900" },
        "lise":   { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace":  { "name": "Grace Hopper",  "date_of_birth": "1906" }
}

famous_births(women_scientists)