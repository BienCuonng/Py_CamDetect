import subprocess

# Chạy file FaceDetect.py
print("[INFO] Đang chạy FaceDetect.py...")
subprocess.run(["python", "FaceDetect.py"])

# Chạy file train.py
print("[INFO] Đang chạy train.py...")
subprocess.run(["python", "train.py"])

# Chạy file Recognize.py
print("[INFO] Đang chạy Recognize.py...")
subprocess.run(["python", "Recognize.py"])

print("[INFO] Tất cả các file đã được thực thi thành công.")
