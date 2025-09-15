import sys

num_params = len(sys.argv) - 1 # ลบ 1 เพราะ sys.argv[0] ชื่อไฟล์โปรแกรม

print(f"Number of parameters: {num_params}")

#python parameters.py
#python parameters.py 'initiation'
#python parameters.py 'this' 'is' 'crazy' 'there's' 'everywhere!'