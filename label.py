from tkinter import*

root = Tk()
root.title(" ")
label = Label(root, text = " ") #type(label)=<class 'tkinter.Label'>
plabel = label.pack() #type(plabel)=<class 'NoneType'>
alabel = Label(root, text = "功能", fg = "red", bg = "lightyellow", height = 3, width = 30,
               anchor = 'nw', wraplength = 10, font = "Helvetic 20 bold", justify = "right")
# fg : 文字顏色    bg : 背景顏色    height : label高    width : label寬
# anchor : 文字位置 nw    n    ne   'se' = SE
#                  w  center  e   大寫表示用constant，不加引號
#                 sw     s    se                                         用tuple來表示font參數
# wraplength : 幾個pixel後換行, default置中
# font : 字型與大小，"Helvetic 20 bold" = ("Helvetic", 20, "bold")
# justify :　指定多行文字對齊方式，"left" "center" "right"
blabel = Label(root, bitmap = "hourglass", text = "沙漏", compound = "left", relief = "raised",
               padx = 20, pady = 20)
# bitmap : 內建的bitmap，"hourglass" "error" "info" "questhead" "question" "warning"
#                        "gray12" "gray25" "gray50" "gray75"
# compound : 圖文共存時，圖像(bitmap or image)在左。如無指定compound，text不會顯示
#            "left" "right" "center" "top" "bottom"
# relief : 邊框特效 "flat" "groove" "raised"("raise") "ridge" "solid" "sunken"
# padx pady : 標籤文字到標籤邊框距離
# image : image = photoi    photoi = PhotoImage(file = "cat.gif")
#                           photoi = PhotoImage(file = "cat.png")
# from PLI import Image, ImageTk  image : image = photoi
#                                 imag = Image.open("cat.jpg")  photoi = ImageTk.PhotoImage(imag)
alabel.pack()
blabel.pack()
import time
time.sleep(5)    # 5 seconds
blabel.config(text = "更換")   #更換label內容
# def run_counter(blabel):
#     def counting():
#         blabel.after(1000, counting)   # 每1秒呼叫一次counting()
for s in ["a", "b", "c"]:
    print(s)


root.mainloop()