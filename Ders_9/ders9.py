import pyautogui
"""
pyautogui.moveTo(500,500,duration=2,tween=pyautogui.easeInQuad)
pyautogui.moveTo(1000,1000,duration=2,tween=pyautogui.easeInQuad)
pyautogui.moveTo(50,50,duration=2,tween=pyautogui.easeInQuad)
pyautogui.moveTo(500,500,duration=2,tween=pyautogui.easeInQuad)"""


"""
#Ekran çözünürlüğü
screenWidth,screenHeight=pyautogui.size()
print("Ekran çözünürlüğü:",screenWidth,screenHeight)"""

"""
#Fare pozisyonu

currentMouseX,currentMouseY=pyautogui.position()
print(currentMouseX,currentMouseY)"""


distance=200
pyautogui.moveTo(500,500,duration=2,tween=pyautogui.easeInQuad)
while distance>0:
    pyautogui.drag(distance,0,duration=0.5)
    distance-=5
    pyautogui.drag(0,distance,duration=0.5)
    pyautogui.drag(-distance,0,duration=0.5)
    distance-=5
    pyautogui.drag(0,-distance,duration=0.5)


