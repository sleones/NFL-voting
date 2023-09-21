import time
import pyautogui
import opencv

i=0
j=0
l=0
k=0
m=0
n=0

time.sleep(3)
while i<3:
    while j<1:
        if pyautogui.locateCenterOnScreen('Nacua.png', confidence = .95, region = (1280, 0 , 1280, 720)) is not None:
            x,y = pyautogui.locateCenterOnScreen('Nacua.png', confidence = .95, region = (1280, 0 , 1280, 720))
            pyautogui.click(x,y)
            j+=1
            n=0
    while k<1:
        if pyautogui.locateCenterOnScreen('Vote.png',confidence = .9) is not None:
            x,y = pyautogui.locateCenterOnScreen('Vote.png', confidence = .9)
            pyautogui.click(x,y)
            k+=1
            j-=1
    while l<1:
        if pyautogui.locateCenterOnScreen('Submit.png', confidence = .9) is not None:
            x,y = pyautogui.locateCenterOnScreen('Submit.png', confidence = .9)
            pyautogui.click(x,y)
            l+=1
            k-=1
    while m<1:
        if pyautogui.locateCenterOnScreen('Again.png', confidence = .9) is not None:
            x,y = pyautogui.locateCenterOnScreen('Again.png', confidence = .9)
            pyautogui.click(x,y)
            m+=1
            l-=1
    while n<1:
        if pyautogui.locateCenterOnScreen('Counter.png', confidence = .9, region = (0, 0, 1280, 720)) is not None:
            x,y = pyautogui.locateCenterOnScreen('Counter.png', confidence = .9, region = (0, 0, 1280, 720))
            pyautogui.click(x,y)
            m-=1
            n+=1
            
   
