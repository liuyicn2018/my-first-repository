from PIL import ImageGrab
import tkinter as tk
import time
import keyboard
######


######
def save(photo):
    def save_input(event=None):
        user_input = entry.get()
        if user_input.strip():  # 检查输入是否为空
            try:
                photo.save(user_input + ".png")
                print("Input saved")
                entry.delete(0, tk.END)  # 清空输入框
            except IOError:
                print("Error saving input to file.")
        else:
            print("Input cannot be empty.")

    root = tk.Tk()
    root.title("Save Input on Enter")

    entry = tk.Entry(root, font=("Arial", 14))
    entry.pack(padx=20, pady=10)

    # 绑定 Enter 键按下事件到 save_input 函数
    entry.bind("<Return>", save_input)

    save_button = tk.Button(root, text="Save", command=save_input, font=("Arial", 12))
    save_button.pack(pady=10)



######

root = tk.Tk()
root.title("截图工具")

root.config(bg="#add8e6")

root.geometry("400x160")

label = tk.Label(root, text="please chose the mode:")
label.pack()
label.config(bg="#add8e6")

def ScreenshotN():
    screen = ImageGrab.grab()
    
    print("Button clicked!")
    save(screen)

button1 = tk.Button(root, text="Screenshot now", command=ScreenshotN,width=40, height=1)
button1.place(x=100, y=50)
button1.pack()
button1.config(bg="#add8e6")


def ScreenshotW():
    time.sleep(5)
    screen = ImageGrab.grab()

    print("Button clicked!")
    save(screen)

button2 = tk.Button(root, text="Screenshot after 5s", command=ScreenshotW,width=40, height=1)
button2.place(x=100, y=50)
button2.pack()
button2.config(bg="#add8e6")


def ScreenshotB():
    while True:
        if keyboard.is_pressed('enter'):
            screen = ImageGrab.grab()
            break

    print("Button clicked!")
    save(screen)

button3 = tk.Button(root, text="Screenshot by 'enter'", command=ScreenshotB,width=40, height=1)
button3.place(x=100, y=100)
button3.pack()
button3.config(bg="#add8e6")

root.mainloop()

