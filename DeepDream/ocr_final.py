from subprocess import call
import os
FNULL = open(os.devnull, 'w')
print("1")
img_path = r"D:\Face Masking YOLO\DeepDream\obfuscated_images\test.jpg"
print("2")
call(["tesseract", img_path, r"D:\Face Masking YOLO\DeepDream\ocr"], stdout=FNULL)