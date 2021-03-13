import pyautogui
import time
# 구글 크롬 오픈후 최대화후 아래 영역 캡춰.
# w =  pyautogui.getWindowsWithTitle("YouTube - Chrome")[0]
# print(w)
# if w.isActive == False:
#     w.activate()
# if w.isMaximized == False:
#     w.maximize()

from PIL import Image
import pytesseract
#pip install pytesseract
#pip install opencv-python #주요 모듈 설치.
#pip install opencv-contrib-python #주요 및 추가 모듈 설치.
import cv2

# 해당 탭을 닫거나 다른 탭으로 변경하는 경우 자동 exception발생되어 종료된다.
w =  pyautogui.getWindowsWithTitle("YouTube - Chrome")[0]

# 5초 마다 무한 loop
while w is not None:
    text = ''
    if w.isActive == False:
        w.activate()
    if w.isMaximized == False:
        w.maximize()  
    # 캡춰시 글자 주위 밖 공간이 생기도록 충분히 캡춰해야함.
    # 글자에 딱맞게 캡춰하거나 잘리면 안됨.
    # 두 모니터일 경우 메인 모니터에 브라우즈 있어야 함.
    img_ad = pyautogui.screenshot('ad.png', region=(1229, 784, 121, 39))
    #img_ad = pyautogui.screenshot('ad.png')

    # 캡춰후 글자 인식하여 "광고 건너뛰기" 일 경우
    #   해당 영역 중간 클릭.
    # 1229, 784
    # 1350 813
    # left=1229, top=784, width=121, height=29-->39    

    img_bgr = cv2.imread('ad.png', cv2.IMREAD_GRAYSCALE)
    # img_bgr = cv2.imread('ad.png', cv2.IMREAD_COLOR)
    # convert from BGR to RGB format/mode
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    #cmd경로설정
    pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'
    # psm 7 : Treat the image as a single text line.
    text = pytesseract.image_to_string(img_rgb, lang='kor+eng', config='--oem 3 --psm 7')
    text = text.replace(' ','') #공백제거.
    #print(text)
    if '광고건너뛰기' in text:
        print(text)
        #mouse click
        # left=1229, top=784, width=121, height=29-->39
        pyautogui.moveTo(1229+120/2,784+40/2, duration=0.25)
        pyautogui.click()
    time.sleep(5) # 5초 지연.
    # 해당 탭을 닫거나 다른 탭으로 변경하는 경우 자동 exception발생되어 종료된다.
    try:
        w =  pyautogui.getWindowsWithTitle("YouTube - Chrome")[0]  
        print(w)
    except:
        print('YouTube - Chrome is None')
