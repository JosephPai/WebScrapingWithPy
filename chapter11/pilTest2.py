from PIL import Image
import subprocess

def cleanFile(filePath, newFielPath):
    image = Image.open(filePath)

    # 对图片进行阈值过滤，然后保存
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFielPath)

    # 调用系统的tesseract命令对图片进行OCR识别
    subprocess.call(["tesseract", newFielPath, "output"])

    # 打开文件读取结果
    outputFile = open("output.txt", 'r')
    print(outputFile.read())
    outputFile.close()

cleanFile("chan1.png","chanover1.png")