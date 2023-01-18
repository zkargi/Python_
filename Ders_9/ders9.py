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




"""
distance=200
pyautogui.moveTo(500,500,duration=2,tween=pyautogui.easeInQuad)
while distance>0:
    pyautogui.drag(distance,0,duration=0.5)
    distance-=5
    pyautogui.drag(0,distance,duration=0.5)
    pyautogui.drag(-distance,0,duration=0.5)
    distance-=5
    pyautogui.drag(0,-distance,duration=0.5)
"""



from tkinter import *
"""
window =Tk()

window.title("Python Gui")


lbl= Label(window,text="kullanıcı adı: ")
lbl.grid(column=0,row=0)
#lbl2.grid(column=1,row=0)
window.geometry('500x400')
txt=Entry(window,width=10)
txt.grid(column=1,row=0)
lbl= Label(window,text="şifre: ")
lbl.grid(column=0,row=1)
txt=Entry(window,width=10)
txt.grid(column=1,row=1)
btn=Button(window,text="giriş")
btn.grid(column=1,row=2)"""

master = Tk()

master.geometry("200x200")

def openNewWindow():

    newWindow = Toplevel(master)

    newWindow.title("New Window")

    newWindow.geometry("200x200")

    Label(newWindow,
          text="This is a new window").pack()
    txt = Entry(master, width=10)
    txt.grid(column=1, row=0).pack()


label = Label(master,
              text="kullanıcı adı:")

label.pack(pady=10)

btn = Button(master,
             text="giriş",
             command=openNewWindow)
btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()
window2 =Tk()


#window.mainloop() #programın kapanmaması için
